package org.example.processlab.workflow;

import java.util.*;
import org.example.processlab.domain.*;
import org.example.processlab.engine.DmnQualifier;
import org.example.processlab.rules.*;
import org.example.processlab.workflow.ChangeCommands.*;
import org.flowable.engine.ProcessEngine;

/** Sequential local command facade. Direct engine access is outside this trust boundary. */
public final class ChangeProcess {
    public static final String STATE = "caseState";
    private final ProcessEngine engine;
    private final DmnQualifier qualifier;
    private final String definitionId;
    public ChangeProcess(ProcessEngine engine, DmnQualifier qualifier, String definitionId) {
        this.engine=Objects.requireNonNull(engine); this.qualifier=Objects.requireNonNull(qualifier);
        this.definitionId=Objects.requireNonNull(definitionId);
    }
    public String start(String businessKey, ChangeState.Scope scope, ProjectSnapshot baseline, ArtifactRevision proposal) {
        return start(businessKey,scope,baseline,proposal,null);
    }
    public String startNext(String businessKey, String previousId, ArtifactRevision proposal) {
        var previous=state(previousId);
        require(previous.acceptance()!=null && tasks(previousId).isEmpty(),"Previous case was not accepted");
        return start(businessKey,previous.scope(),previous.snapshot(),proposal,previousId);
    }
    private String start(String businessKey, ChangeState.Scope scope, ProjectSnapshot baseline, ArtifactRevision proposal, String previousId) {
        ChangeCommands.text(businessKey);
        require(engine.getHistoryService().createHistoricProcessInstanceQuery().processInstanceBusinessKey(businessKey).count()==0,
                "Business key already used");
        require(new HashSet<>(List.of(scope.requirementId(),scope.testId(),scope.softwareId())).size()==3,"Scope IDs must differ");
        require(baseline.current().containsKey(scope.requirementId()),"Missing initial requirement");
        require(baseline.artifacts().stream().anyMatch(a->a.ref().equals(baseline.current().get(scope.requirementId()))
                && a.kind()==ArtifactRevision.Kind.REQUIREMENT),"Missing initial requirement revision");
        requireNew(baseline,proposal,scope.requirementId(),ArtifactRevision.Kind.REQUIREMENT);
        requireKnownEvidence(baseline);
        var state=new ChangeState(0,scope,baseline,proposal,false,previousId,List.of(),null);
        return engine.getRuntimeService().startProcessInstanceById(definitionId,businessKey,Map.of(STATE,StateCodec.encode(state))).getId();
    }
    public void execute(Envelope command, Operation operation) {
        Objects.requireNonNull(command); Objects.requireNonNull(operation);
        var before=state(command.processId());
        require(before.acceptance()==null,"Case already accepted");
        require(before.version()==command.expectedVersion(),"Stale state version");
        require(before.receipts().stream().noneMatch(r->r.commandId().equals(command.id())),"Repeated command ID");
        var task=engine.getTaskService().createTaskQuery().taskId(command.taskId()).processInstanceId(command.processId()).singleResult();
        require(task!=null,"Task not active in this process");
        var key=task.getTaskDefinitionKey();
        var snapshot=before.snapshot(); var proposal=before.proposal(); boolean authorized=before.authorized();
        ChangeState.Acceptance acceptance=null;
        String action;
        if (operation instanceof Authorize authorize) {
            allow(command,Role.OPERATOR,key,"authorize");
            authorized=authorize.allowed(); action=authorize.allowed()?"ALLOW":"DENY";
        } else if (operation instanceof Propose propose) {
            allow(command,Role.AGENT,key,"impact","prepare","assess","accept");
            requireNew(snapshot,propose.requirement(),before.scope().requirementId(),ArtifactRevision.Kind.REQUIREMENT);
            proposal=propose.requirement(); authorized=false; action="PROPOSE";
        } else if (operation instanceof ApplyChange) {
            allow(command,Role.AGENT,key,"impact"); require(authorized,"No authorization for this proposal");
            requireNew(snapshot,proposal,before.scope().requirementId(),ArtifactRevision.Kind.REQUIREMENT);
            var artifacts=new ArrayList<>(snapshot.artifacts()); artifacts.add(proposal);
            var current=new HashMap<>(snapshot.current()); current.put(proposal.ref().id(),proposal.ref());
            snapshot=new ProjectSnapshot(artifacts,current,snapshot.dependencies(),snapshot.reviews(),snapshot.runs());
            authorized=false; action="APPLY";
        } else if (operation instanceof Prepare prepare) {
            allow(command,Role.AGENT,key,"prepare");
            requireNew(snapshot,prepare.test(),before.scope().testId(),ArtifactRevision.Kind.TEST_CASE);
            requireNew(snapshot,prepare.software(),before.scope().softwareId(),ArtifactRevision.Kind.SOFTWARE);
            var artifacts=new ArrayList<>(snapshot.artifacts()); artifacts.add(prepare.test()); artifacts.add(prepare.software());
            var current=new HashMap<>(snapshot.current());
            current.put(prepare.test().ref().id(),prepare.test().ref()); current.put(prepare.software().ref().id(),prepare.software().ref());
            var dependencies=new ArrayList<>(snapshot.dependencies().stream()
                    .filter(d->!d.dependent().id().equals(before.scope().testId())).toList());
            dependencies.add(new Dependency(current.get(before.scope().requirementId()),prepare.test().ref(),Dependency.Kind.VERIFIES));
            snapshot=new ProjectSnapshot(artifacts,current,dependencies,snapshot.reviews(),snapshot.runs()); action="PREPARE";
        } else if (operation instanceof Assess assess) {
            allow(command,Role.AGENT,key,"assess");
            for (var review:assess.reviews()) snapshot=snapshot.append(review);
            for (var run:assess.runs()) snapshot=snapshot.append(run);
            requireKnownEvidence(snapshot);
            action="ASSESS";
        } else if (operation instanceof Rework) {
            allow(command,Role.AGENT,key,"assess"); action="REWORK";
        } else if (operation instanceof Decide decide) {
            allow(command,Role.OPERATOR,key,"accept");
            if (decide.accepted()) {
                require(qualifier.evaluateWithoutHistory(WorkflowChecks.facts(before))==Qualification.TO_OPERATOR,"Basis is not ready for acceptance");
                acceptance=new ChangeState.Acceptance(command.id(),before.version()+1,snapshot.current(),operation.reason());
            }
            action=decide.accepted()?"ACCEPT":"REJECT";
        } else throw new IllegalArgumentException("Unsupported operation");
        var receipts=new ArrayList<>(before.receipts());
        receipts.add(new ChangeState.Receipt(command.id(),command.taskId(),before.version(),command.role(),action,operation.reason()));
        var next=new ChangeState(before.version()+1,before.scope(),snapshot,proposal,authorized,before.previousProcessId(),receipts,acceptance);
        // Single write boundary: the synchronous BPMN continuation and DMN share this transaction.
        engine.getTaskService().complete(command.taskId(),Map.of(STATE,StateCodec.encode(next),"action",action));
    }
    private static void allow(Envelope command, Role role, String key, String... keys) {
        require(command.role()==role,"Role cannot execute this operation");
        require(Arrays.asList(keys).contains(key),"Operation not permitted at this task");
    }
    private static void requireNew(ProjectSnapshot snapshot,ArtifactRevision artifact,String id,ArtifactRevision.Kind kind) {
        require(artifact.ref().id().equals(id) && artifact.kind()==kind,"Wrong artifact ID or kind");
        int latest=snapshot.artifacts().stream().filter(a->a.ref().id().equals(id)).mapToInt(a->a.ref().revision()).max().orElse(0);
        require(artifact.ref().revision()>latest,"New revision must be greater than every stored revision");
    }
    private static void requireKnownEvidence(ProjectSnapshot snapshot) {
        var known=new HashSet<ArtifactRef>();
        snapshot.artifacts().forEach(a->known.add(a.ref()));
        for (var review:snapshot.reviews()) {
            require(known.contains(review.subject()) && known.containsAll(review.basis()),"Evidence refers to a nonexistent revision");
        }
        for (var run:snapshot.runs()) {
            require(known.contains(run.testCase()) && known.contains(run.software()),"Run refers to a nonexistent revision");
        }
    }
    private static void require(boolean condition,String message) {if (!condition) throw new IllegalArgumentException(message);}
    public ChangeState state(String processId) {
        ChangeCommands.text(processId);
        var variable=engine.getHistoryService().createHistoricVariableInstanceQuery().processInstanceId(processId).variableName(STATE).singleResult();
        require(variable!=null,"Unknown process state");
        return StateCodec.decode((String)variable.getValue());
    }
    public List<TaskView> tasks(String processId) {
        return engine.getTaskService().createTaskQuery().processInstanceId(processId).list().stream()
                .map(t->new TaskView(t.getId(),t.getTaskDefinitionKey(),t.getName(),t.getAssignee())).toList();
    }
    public String report(String processId) {
        var state=state(processId); var tasks=tasks(processId);
        var out=new StringBuilder("# SYMULACJA — zmiana wymagania\n\n");
        out.append("Instancja: ").append(processId).append(" · wersja stanu: ").append(state.version()).append("\n\n");
        out.append("Poprzednia instancja: ").append(state.previousProcessId()==null?"brak":state.previousProcessId()).append("\n\n");
        out.append("Propozycja: ").append(ref(state.proposal().ref())).append(" · ").append(state.proposal().content()).append("\n\n");
        out.append("Upoważnienie do zastosowania tej propozycji: ").append(state.authorized()?"udzielone":"brak aktywnego upoważnienia").append("\n\n");
        out.append("Odbiór: ").append(state.acceptance()==null?"brak":"przyjęto w fabule; "+state.acceptance().commandId()).append("\n\n");
        out.append("## Bieżące rewizje i kontrole\n\nKontrole odnoszą się do bieżących rewizji poniżej. Nie potwierdzają jeszcze niezastosowanej propozycji.\n\n");
        state.snapshot().current().entrySet().stream().sorted(Map.Entry.comparingByKey()).forEach(e->out.append("- ")
                .append(ref(e.getValue())).append(": ").append(state.snapshot().artifacts().stream()
                        .filter(a->a.ref().equals(e.getValue())).map(ArtifactRevision::content).findFirst().orElse("brak treści")).append("\n"));
        out.append("\n"); WorkflowChecks.checks(state).forEach((name,result)->out.append("- ").append(name).append(": ").append(result).append("\n"));
        out.append("\n## Oczekujące zadania\n\n");
        if(tasks.isEmpty()) out.append("Brak aktywnych zadań. Zakończenie bez odbioru nie oznacza przyjęcia.\n");
        for(var task:tasks) out.append("- ").append(task.key()).append(" · ").append(task.name()).append(" · ").append(task.assignee()).append(" · ID ").append(task.id()).append("\n");
        out.append("\n## Kandydaci wpływu (doradczo)\n\n");
        Rules.impact(state.snapshot(),state.scope().requirementId()).forEach((id,path)->out.append("- ").append(String.join(" → ",path)).append("\n"));
        out.append("\n## Historia zadań z silnika\n\n");
        engine.getHistoryService().createHistoricTaskInstanceQuery().processInstanceId(processId).orderByHistoricTaskInstanceStartTime().asc().list()
                .forEach(t->out.append("- ").append(t.getTaskDefinitionKey()).append(" · ").append(t.getId()).append(" · ").append(t.getEndTime()==null?"oczekuje":"zakończono").append("\n"));
        out.append("\n## Polecenia (kolejność wersji stanu)\n\n");
        for(var receipt:state.receipts()) out.append("- v").append(receipt.baseVersion()+1).append(" · ").append(receipt.commandId()).append(" · ").append(receipt.role()).append(" · ").append(receipt.action()).append(" · ").append(receipt.reason()).append("\n");
        out.append("\n## Zachowane oceny i wykonania\n\n");
        for(var review:state.snapshot().reviews()) out.append("- ").append(review.id()).append(" · ").append(ref(review.subject())).append(" · ").append(review.basis().stream().map(ChangeProcess::ref).toList()).append(" · ").append(review.outcome()).append("\n");
        for(var run:state.snapshot().runs()) out.append("- ").append(run.id()).append(" · ").append(ref(run.testCase())).append(" / ").append(ref(run.software())).append(" · ").append(run.outcome()).append("\n");
        return out.toString();
    }
    private static String ref(ArtifactRef ref) {return ref.id()+"@"+ref.revision();}
    public record TaskView(String id, String key, String name, String assignee) {}
}
