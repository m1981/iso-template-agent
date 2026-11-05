package org.example.processlab;

import java.util.*;
import org.example.processlab.domain.*;
import org.example.processlab.rules.*;
import org.example.processlab.workflow.*;
import org.example.processlab.workflow.ChangeCommands.*;
import org.flowable.common.engine.api.delegate.event.*;
import org.flowable.engine.delegate.event.*;
import org.junit.jupiter.api.*;
import static org.junit.jupiter.api.Assertions.*;
import static org.example.processlab.RulesTest.*;
import static org.example.processlab.workflow.ChangeCommands.Role.*;

class ChangeProcessTest {
    ChangeTrial trial;
    ChangeProcess process;
    int sequence;
    static final ChangeState.Scope SCOPE=new ChangeState.Scope("CAP-01","AT-01","CODE-01");
    @BeforeEach void open() {
        trial=ChangeTrial.open("workflow_"+UUID.randomUUID().toString().replace("-",""));
        process=trial.process();
    }
    @AfterEach void close() { if (trial!=null) trial.close(); }
    static ArtifactRevision artifact(ArtifactRef ref,ArtifactRevision.Kind kind) {
        String content=switch(kind) {
            case REQUIREMENT -> ref.revision()==1 ? "TextStats: biało-czerwony liczymy jako jedno słowo." :
                    ref.revision()==2 ? "TextStats: myślnik rozdziela słowa; biało-czerwony daje 2." :
                    "TextStats: myślnik i spacja nierozdzielająca rozdzielają słowa; oba przykłady dają 2.";
            case TEST_CASE -> ref.revision()<=2 ? "Przypadek: biało-czerwony; nadal oczekiwane 1 (do oceny wobec nowego wymagania)." :
                    ref.revision()==3 ? "Przypadek: biało-czerwony; oczekiwane 2." :
                    "Przypadki: biało-czerwony i dwa słowa ze spacją nierozdzielającą; oczekiwane 2.";
            case SOFTWARE -> "Fikcyjna wersja programu "+ref.revision()+"; nie uruchamiamy TextStats w tej próbie.";
        };
        return new ArtifactRevision(ref,kind,content);
    }
    static ProjectSnapshot baseline() {
        return new ProjectSnapshot(List.of(artifact(R1,ArtifactRevision.Kind.REQUIREMENT),artifact(T1,ArtifactRevision.Kind.TEST_CASE),
                artifact(C1,ArtifactRevision.Kind.SOFTWARE)),Map.of("CAP-01",R1,"AT-01",T1,"CODE-01",C1),
                List.of(new Dependency(R1,T1,Dependency.Kind.VERIFIES)),
                List.of(review("baseCap",R1,List.of(),ReviewRecord.Outcome.PASS),review("baseTest",T1,List.of(R1),ReviewRecord.Outcome.PASS)),
                List.of(run("baseRun",T1,C1,TestRunRecord.Outcome.PASS)));
    }
    String start() {
        var id=process.start("change-"+ ++sequence,SCOPE,baseline(),artifact(R2,ArtifactRevision.Kind.REQUIREMENT));
        assertNotNull(id,"A real BPMN instance must be started");
        assertEquals("authorize",task(id).key());
        return id;
    }
    ChangeProcess.TaskView task(String id) {
        var tasks=process.tasks(id); assertEquals(1,tasks.size()); return tasks.get(0);
    }
    Envelope envelope(String id, Role role) {
        return new Envelope("command-"+ ++sequence,id,task(id).id(),process.state(id).version(),role);
    }
    Envelope send(String id, Role role, Operation op) {
        var command=envelope(id,role); process.execute(command,op); return command;
    }
    void prepare(String id,int rev) {
        send(id,AGENT,new Prepare(artifact(ref("AT-01",rev),ArtifactRevision.Kind.TEST_CASE),
                artifact(ref("CODE-01",rev),ArtifactRevision.Kind.SOFTWARE),"Przygotowano nowy test i program w fabule"));
    }
    String readyToAssess() {
        var id=start(); send(id,OPERATOR,new Authorize(true,"Zgoda w fabule"));
        send(id,AGENT,new ApplyChange("Oceniono wpływ na AT-01 i zastosowano propozycję")); prepare(id,2);
        assertEquals("assess",task(id).key()); return id;
    }
    Assess results(String id,String prefix,ReviewRecord.Outcome cap,ReviewRecord.Outcome test,TestRunRecord.Outcome run) {
        var current=process.state(id).snapshot().current();
        var r=current.get("CAP-01"); var t=current.get("AT-01"); var c=current.get("CODE-01");
        return new Assess(List.of(review(prefix+"cap",r,List.of(),cap),review(prefix+"test",t,List.of(r),test)),
                List.of(run(prefix+"run",t,c,run)),"Fikcyjne wyniki ocen i wykonania");
    }
    void pass(String id,String prefix) { send(id,AGENT,results(id,prefix,ReviewRecord.Outcome.PASS,ReviewRecord.Outcome.PASS,TestRunRecord.Outcome.PASS)); }
    long dmnCount() { return trial.session().decisions().getDmnHistoryService().createHistoricDecisionExecutionQuery().count(); }
    long taskHistory(String id) { return trial.session().processes().getHistoryService().createHistoricTaskInstanceQuery().processInstanceId(id).count(); }

    @Test void F4_01_authorizationAndAcceptanceAreSeparateAndSilenceWaits() {
        var id=start(); var original=process.state(id);
        assertTrue(process.report(id).contains("Propozycja: CAP-01@2"));
        assertThrows(IllegalArgumentException.class,()->send(id,AGENT,new ApplyChange("Too early")));
        assertThrows(IllegalArgumentException.class,()->send(id,AGENT,new Authorize(true,"Not operator")));
        assertThrows(IllegalArgumentException.class,()->send(id,OPERATOR,new Decide(true,"Not authorization")));
        assertEquals(original,process.state(id));
        send(id,OPERATOR,new Authorize(true,"Allow this proposal"));
        assertEquals(R1,process.state(id).snapshot().current().get("CAP-01"));
        send(id,AGENT,new ApplyChange("Impact assessed")); prepare(id,2); pass(id,"current");
        assertEquals("accept",task(id).key());
        assertNull(process.state(id).acceptance());
        assertThrows(IllegalArgumentException.class,()->send(id,AGENT,new Decide(true,"Not operator")));
        var beforeDmn=dmnCount(); var report=process.report(id);
        assertTrue(report.contains("OPERATOR")); assertEquals(beforeDmn,dmnCount(),"Reading must not append DMN history");
        send(id,OPERATOR,new Decide(true,"Odebrano w fabule"));
        assertTrue(process.tasks(id).isEmpty());
        assertNotNull(process.state(id).acceptance());
        assertEquals(R2,process.state(id).acceptance().basis().get("CAP-01"));
        assertEquals(beforeDmn,dmnCount(),"Decision re-check must not create an independent DMN transaction");
    }
    @Test void F4_02_failLoopsToNewPreparationWithoutRewritingOldEvidence() {
        var id=readyToAssess();
        send(id,AGENT,results(id,"failed",ReviewRecord.Outcome.PASS,ReviewRecord.Outcome.FAIL,TestRunRecord.Outcome.PASS));
        assertEquals("prepare",task(id).key()); var before=process.state(id).snapshot();
        prepare(id,3); pass(id,"corrected");
        assertEquals("accept",task(id).key());
        assertTrue(process.state(id).snapshot().reviews().containsAll(before.reviews()));
        assertTrue(process.state(id).snapshot().runs().containsAll(before.runs()));
        send(id,OPERATOR,new Decide(false,"Odbiorca potrzebuje poprawki"));
        assertEquals("prepare",task(id).key()); assertNull(process.state(id).acceptance());
    }
    @Test void F4_02_dmnPriorityHandlesMissingAndConflictingEvidence() {
        var id=readyToAssess();
        send(id,AGENT,results(id,"error",ReviewRecord.Outcome.FAIL,ReviewRecord.Outcome.PASS,TestRunRecord.Outcome.ERROR));
        assertEquals("assess",task(id).key());
        assertEquals("MISSING_BASIS",trial.session().processes().getRuntimeService().getVariable(id,"qualification"));
        send(id,AGENT,new Rework("ERROR requires a new program version")); assertEquals("prepare",task(id).key());
        prepare(id,3);
        var batch=results(id,"conflict",ReviewRecord.Outcome.FAIL,ReviewRecord.Outcome.PASS,TestRunRecord.Outcome.PASS);
        var reviews=new ArrayList<>(batch.reviews()); reviews.add(review("testFail",ref("AT-01",3),List.of(R2),ReviewRecord.Outcome.FAIL));
        send(id,AGENT,new Assess(reviews,batch.runs(),"Conflicting review"));
        assertEquals("assess",task(id).key());
        assertEquals("REVIEW_REQUIRED",trial.session().processes().getRuntimeService().getVariable(id,"qualification"));
    }
    @Test void F4_03_oldTaskVersionInstanceAndCommandIdentityAreCheckedSeparately() {
        var id=readyToAssess(); var old=envelope(id,AGENT);
        process.execute(old,new Assess(List.of(),List.of(),"Still missing"));
        var before=process.state(id); var now=task(id);
        assertNotEquals(old.taskId(),now.id()); assertEquals("assess",now.key());
        assertThrows(IllegalArgumentException.class,()->process.execute(new Envelope("new-id",id,old.taskId(),before.version(),AGENT),new Assess(List.of(),List.of(),"Old task")));
        assertThrows(IllegalArgumentException.class,()->process.execute(new Envelope("new-id",id,now.id(),old.expectedVersion(),AGENT),new Assess(List.of(),List.of(),"Old version")));
        assertThrows(IllegalArgumentException.class,()->process.execute(new Envelope(old.id(),id,now.id(),before.version(),AGENT),new Assess(List.of(),List.of(),"Replay on new task")));
        var other=readyToAssess();
        var otherBefore=process.state(other);
        assertThrows(IllegalArgumentException.class,()->process.execute(new Envelope("foreign",other,now.id(),otherBefore.version(),AGENT),new Assess(List.of(),List.of(),"Wrong case")));
        assertEquals(otherBefore,process.state(other));
        assertEquals(before,process.state(id)); assertEquals(now,task(id));
    }
    @Test void F4_04_newProposalRevokesPriorAuthorizationBeforeApplication() {
        var id=start(); send(id,OPERATOR,new Authorize(true,"Allow R2"));
        var proposed=artifact(ref("CAP-01",3),ArtifactRevision.Kind.REQUIREMENT);
        send(id,AGENT,new Propose(proposed,"Different proposal"));
        assertEquals(R1,process.state(id).snapshot().current().get("CAP-01"));
        assertFalse(process.state(id).authorized());
        assertThrows(IllegalArgumentException.class,()->send(id,AGENT,new ApplyChange("Old permission")));
        send(id,OPERATOR,new Authorize(false,"Decline new proposal"));
        assertTrue(process.tasks(id).isEmpty()); assertNull(process.state(id).acceptance());
        assertEquals(R1,process.state(id).snapshot().current().get("CAP-01"));
        assertThrows(IllegalArgumentException.class,()->process.startNext("not-accepted",id,proposed));
    }
    @Test void F4_04_changeDuringReviewRejectsLateCommandAndPreservesOldResults() {
        var id=readyToAssess(); var late=envelope(id,AGENT); var oldResults=results(id,"late",ReviewRecord.Outcome.PASS,ReviewRecord.Outcome.PASS,TestRunRecord.Outcome.PASS);
        send(id,AGENT,new Propose(artifact(ref("CAP-01",3),ArtifactRevision.Kind.REQUIREMENT),"New basis during review"));
        send(id,OPERATOR,new Authorize(true,"Allow R3")); send(id,AGENT,new ApplyChange("New impact")); prepare(id,3);
        var before=process.state(id);
        assertThrows(IllegalArgumentException.class,()->process.execute(late,oldResults)); assertEquals(before,process.state(id));
        send(id,AGENT,oldResults); // Historic evidence may be recorded, but cannot renew the new basis.
        assertEquals("assess",task(id).key()); assertNull(process.state(id).acceptance());
        assertEquals(CheckStatus.REVIEW_REQUIRED,Rules.review(process.state(id).snapshot(),ref("CAP-01",3)));
    }
    @Test void F4_04_changeBeforeAcceptanceCannotReuseOldDecision() {
        var id=readyToAssess(); pass(id,"first"); var decision=envelope(id,OPERATOR);
        send(id,AGENT,new Propose(artifact(ref("CAP-01",3),ArtifactRevision.Kind.REQUIREMENT),"New scope before acceptance"));
        send(id,OPERATOR,new Authorize(true,"Allow R3")); send(id,AGENT,new ApplyChange("Impact")); prepare(id,3);
        var before=process.state(id);
        assertThrows(IllegalArgumentException.class,()->process.execute(decision,new Decide(true,"Stale decision")));
        assertEquals(before,process.state(id)); assertNull(before.acceptance());
        assertTrue(process.report(id).contains("REVIEW_REQUIRED"));
    }
    @Test void F4_05_nextChangePreservesPreviousAcceptanceAndRejectsOverwrite() {
        var id=readyToAssess(); pass(id,"accepted"); send(id,OPERATOR,new Decide(true,"Accept A"));
        var accepted=process.state(id);
        var next=process.startNext("next",id,artifact(ref("CAP-01",3),ArtifactRevision.Kind.REQUIREMENT));
        assertEquals(id,process.state(next).previousProcessId());
        send(next,OPERATOR,new Authorize(true,"Allow B")); send(next,AGENT,new ApplyChange("Impact B")); prepare(next,3);
        var unchanged=process.state(next);
        assertThrows(IllegalArgumentException.class,()->send(next,AGENT,new Assess(List.of(review("acceptedcap",ref("CAP-01",3),List.of(),ReviewRecord.Outcome.FAIL)),List.of(),"Overwrite")));
        assertEquals(unchanged,process.state(next));
        send(next,AGENT,new Propose(artifact(ref("CAP-01",4),ArtifactRevision.Kind.REQUIREMENT),"Propose C"));
        send(next,OPERATOR,new Authorize(false,"Decline C"));
        assertEquals(ref("CAP-01",3),process.state(next).snapshot().current().get("CAP-01"));
        assertTrue(process.state(next).snapshot().reviews().containsAll(accepted.snapshot().reviews()));
        assertEquals(accepted,process.state(id));
        assertThrows(IllegalArgumentException.class,()->process.startNext("next",id,artifact(ref("CAP-01",3),ArtifactRevision.Kind.REQUIREMENT)));
    }
    @Test void F4_06_failureAfterQualificationRollsBackAllEffectsAndAllowsExactRetry() {
        var id=readyToAssess(); var command=envelope(id,AGENT); var operation=results(id,"atomic",ReviewRecord.Outcome.PASS,ReviewRecord.Outcome.PASS,TestRunRecord.Outcome.PASS);
        var state=process.state(id); var tasks=process.tasks(id); var history=taskHistory(id); var dmn=dmnCount();
        var historicTasks=historicTasks(id);
        var details=trial.session().processes().getHistoryService().createHistoricDetailQuery().processInstanceId(id).count();
        var reached=new java.util.concurrent.atomic.AtomicBoolean();
        var listener=new FlowableEventListener() {
            public void onEvent(FlowableEvent event) {
                if (event instanceof FlowableActivityEvent activity && "qualify".equals(activity.getActivityId())) {
                    reached.set(true); throw new IllegalStateException("Injected after qualification");
                }
            }
            public boolean isFailOnException() {return true;}
            public boolean isFireOnTransactionLifecycleEvent() {return false;}
            public String getOnTransaction() {return null;}
        };
        var runtime=trial.session().processes().getRuntimeService();
        runtime.addEventListener(listener,FlowableEngineEventType.ACTIVITY_COMPLETED);
        assertThrows(RuntimeException.class,()->process.execute(command,operation)); assertTrue(reached.get());
        runtime.removeEventListener(listener);
        assertEquals(state,process.state(id)); assertEquals(tasks,process.tasks(id));
        assertEquals(history,taskHistory(id)); assertEquals(dmn,dmnCount());
        assertEquals(historicTasks,historicTasks(id));
        assertEquals(details,trial.session().processes().getHistoryService().createHistoricDetailQuery().processInstanceId(id).count());
        process.execute(command,operation);
        assertEquals("accept",task(id).key());
        assertEquals(1,process.state(id).receipts().stream().filter(r->r.commandId().equals(command.id())).count());
        assertEquals(dmn+1,dmnCount());
    }
    @Test void F4_07_codecAndViewUseStoredStateAndEngineHistory() {
        var id=readyToAssess(); var state=process.state(id);
        assertEquals(state,StateCodec.decode(StateCodec.encode(state)));
        var report=process.report(id);
        assertTrue(report.contains("CAP-01@2")); assertTrue(report.contains("AT-01@2"));
        assertTrue(report.contains("baseRun")); assertTrue(report.contains("authorize")); assertTrue(report.contains("assess"));
        assertTrue(report.contains("SYMULACJA"));
        assertTrue(trial.session().processes().getHistoryService().createHistoricDetailQuery().processInstanceId(id).count()>0);
    }
    @Test void F4_08_futureReferencesAreRejectedOnResults() {
        var id=readyToAssess(); var before=process.state(id);
        var future=ref("CAP-01",3);
        var valid=review("valid",R2,List.of(),ReviewRecord.Outcome.PASS);
        var invalid=review("future",future,List.of(),ReviewRecord.Outcome.PASS);
        assertThrows(IllegalArgumentException.class,()->send(id,AGENT,new Assess(List.of(valid,invalid),List.of(),"Future subject")));
        assertThrows(IllegalArgumentException.class,()->send(id,AGENT,new Assess(List.of(review("basis",T2,List.of(future),ReviewRecord.Outcome.PASS)),List.of(),"Future basis")));
        assertThrows(IllegalArgumentException.class,()->send(id,AGENT,new Assess(List.of(),List.of(run("futureTest",ref("AT-01",3),C2,TestRunRecord.Outcome.PASS)),"Future test")));
        assertThrows(IllegalArgumentException.class,()->send(id,AGENT,new Assess(List.of(),List.of(run("futureCode",T2,ref("CODE-01",3),TestRunRecord.Outcome.PASS)),"Future program")));
        assertEquals(before,process.state(id));
    }
    @Test void F4_08_futureReferencesAreRejectedOnInitialImport() {
        var invalid=review("future",ref("CAP-01",3),List.of(),ReviewRecord.Outcome.PASS);
        var bad=baseline().append(invalid);
        var count=trial.session().processes().getHistoryService().createHistoricProcessInstanceQuery().count();
        assertThrows(IllegalArgumentException.class,()->process.start("invalid-import",SCOPE,bad,artifact(R2,ArtifactRevision.Kind.REQUIREMENT)));
        assertThrows(IllegalArgumentException.class,()->process.start("invalid-run-import",SCOPE,
                baseline().append(run("future",T1,ref("CODE-01",3),TestRunRecord.Outcome.PASS)),artifact(R2,ArtifactRevision.Kind.REQUIREMENT)));
        assertEquals(count,trial.session().processes().getHistoryService().createHistoricProcessInstanceQuery().count());
    }

    List<String> historicTasks(String id) {
        return trial.session().processes().getHistoryService().createHistoricTaskInstanceQuery().processInstanceId(id).list().stream()
                .map(t->t.getId()+"/"+t.getTaskDefinitionKey()+"/"+t.getEndTime()+"/"+t.getDeleteReason()).sorted().toList();
    }
    @Test void F4_09_exportsExecutedScenario() throws Exception {
        var reports=new ArrayList<String>();
        var id=start(); reports.add("# 1. Oczekiwanie na zgodę\n\n"+process.report(id));
        send(id,OPERATOR,new Authorize(true,"Zgoda symulowanego operatora na CAP-01@2"));
        send(id,AGENT,new ApplyChange("Ocena wpływu: AT-01 wymaga rozliczenia")); prepare(id,2);
        send(id,AGENT,results(id,"demoFail",ReviewRecord.Outcome.PASS,ReviewRecord.Outcome.FAIL,TestRunRecord.Outcome.PASS));
        assertEquals("prepare",task(id).key()); reports.add("# 2. Fail skierował pracę do poprawki\n\n"+process.report(id));
        prepare(id,3); pass(id,"demoPass"); assertEquals("accept",task(id).key());
        reports.add("# 3. Gotowe do decyzji, bez automatycznego odbioru\n\n"+process.report(id));
        send(id,OPERATOR,new Decide(true,"Fikcyjny odbiór w scenariuszu testowym"));
        var accepted=process.state(id); reports.add("# 4. Przyjęta pierwsza sprawa\n\n"+process.report(id));
        var next=process.startNext("demo-next",id,artifact(ref("CAP-01",3),ArtifactRevision.Kind.REQUIREMENT));
        send(next,OPERATOR,new Authorize(true,"Zgoda w fabule na nową propozycję"));
        send(next,AGENT,new ApplyChange("Nowa ocena wpływu")); prepare(next,4);
        assertEquals(CheckStatus.REVIEW_REQUIRED,Rules.review(process.state(next).snapshot(),ref("CAP-01",3)));
        assertEquals(accepted,process.state(id));
        reports.add("# 5. Nowa sprawa nie odnawia starych ocen i nie zmienia wcześniejszego odbioru\n\n"+process.report(next));
        var output=System.getProperty("demo.output");
        if(output!=null) java.nio.file.Files.writeString(java.nio.file.Path.of(output),
                "Wygenerowano z usług Flowable podczas rzeczywistego testu F4. Role, oceny i odbiory są fikcyjne; program TextStats nie był uruchamiany.\n\n"+String.join("\n---\n\n",reports));
    }

}
