package org.example.processlab;

import java.nio.file.*;
import java.util.*;
import org.example.processlab.domain.*;
import org.example.processlab.workflow.*;
import org.example.processlab.workflow.ChangeCommands.*;
import org.flowable.engine.history.HistoricVariableUpdate;
import tools.jackson.databind.json.JsonMapper;
import static org.example.processlab.workflow.ChangeCommands.Role.*;

/** Trusted fictional demo harness, intentionally in test scope. Each invocation is a new JVM. */
public final class RestartWorker {
    private static final JsonMapper JSON=JsonMapper.builder().build();
    public static void main(String[] args) throws Exception {
        if(args.length!=3) throw new IllegalArgumentException("phase database output.json");
        String phase=args[0]; Path database=Path.of(args[1]); Path output=Path.of(args[2]);
        try(var trial=phase.equals("create") ? ChangeTrial.createPersistent(database) : ChangeTrial.reopenPersistent(database)) {
            var p=trial.process();
            if(phase.equals("create")) p.start("textstats-change",ChangeProcessTest.SCOPE,ChangeProcessTest.baseline(),
                    artifact("CAP-01",2,ArtifactRevision.Kind.REQUIREMENT));
            String id=find(trial,"textstats-change");
            switch(phase) {
                case "create", "show" -> { }
                case "apply" -> {
                    send(p,id,"authorize",OPERATOR,new Authorize(true,"Zgoda w fikcyjnym scenariuszu"));
                    send(p,id,"apply",AGENT,new ApplyChange("Wpływ na AT-01"));
                    prepare(p,id,2);
                }
                case "fail" -> send(p,id,"fail",AGENT,results(p,id,"failed",ReviewRecord.Outcome.FAIL));
                case "correct" -> {
                    prepare(p,id,3);
                    send(p,id,"pass",AGENT,results(p,id,"passed",ReviewRecord.Outcome.PASS));
                    // Same old command ID, but current version/task and otherwise legal operation.
                    try {
                        send(p,id,"apply",AGENT,new Propose(artifact("CAP-01",3,ArtifactRevision.Kind.REQUIREMENT),"Powtórzone ID"));
                        throw new AssertionError("Repeated command accepted after restart");
                    } catch(IllegalArgumentException expected) {
                        if(!expected.getMessage().equals("Repeated command ID")) throw expected;
                    }
                }
                case "accept-next" -> {
                    send(p,id,"accept",OPERATOR,new Decide(true,"FIKCYJNY odbiór, nie decyzja użytkownika"));
                    p.startNext("textstats-next",id,artifact("CAP-01",3,ArtifactRevision.Kind.REQUIREMENT));
                }
                default -> throw new IllegalArgumentException("Unknown phase: "+phase);
            }
            var cases=new LinkedHashMap<String,Object>();
            cases.put("first",observe(trial,id));
            var next=trial.session().processes().getHistoryService().createHistoricProcessInstanceQuery()
                    .processInstanceBusinessKey("textstats-next").singleResult();
            if(next!=null) cases.put("next",observe(trial,next.getId()));
            var result=new LinkedHashMap<String,Object>();
            result.put("pid",ProcessHandle.current().pid()); result.put("phase",phase); result.put("cases",cases);
            var b=trial.session().processes().getRepositoryService();
            var d=trial.session().decisions().getDmnRepositoryService();
            result.put("bpmnDefinitions",b.createProcessDefinitionQuery().list().stream().map(x->x.getId()).sorted().toList());
            result.put("dmnDefinitions",d.createDecisionQuery().list().stream().map(x->x.getId()).sorted().toList());
            result.put("dmnParents",d.createDeploymentQuery().list().stream().map(x->x.getParentDeploymentId()).sorted().toList());
            result.put("dmnHistory",trial.session().decisions().getDmnHistoryService().createHistoricDecisionExecutionQuery().list()
                    .stream().map(x->Map.of("id",x.getId(),"definition",x.getDecisionDefinitionId(),"json",x.getExecutionJson())).sorted(Comparator.comparing(x->x.get("id"))).toList());
            var report=new StringBuilder("# F5 — odczyt trwałej symulacji\n\nRole, wyniki i decyzje są fikcyjne. Każde wywołanie uruchamia nową JVM.\n\n");
            report.append(p.report(id)); if(next!=null) report.append("\n---\n\n").append(p.report(next.getId()));
            Files.writeString(output.resolveSibling(output.getFileName()+".md"),report);
            Files.writeString(output,JSON.writerWithDefaultPrettyPrinter().writeValueAsString(result));
        }
        System.out.println("F5 phase="+phase+" pid="+ProcessHandle.current().pid()+" closed");
    }
    private static String find(ChangeTrial trial,String key) {
        var instance=trial.session().processes().getHistoryService().createHistoricProcessInstanceQuery().processInstanceBusinessKey(key).singleResult();
        if(instance==null) throw new IllegalStateException("Missing case: "+key);
        return instance.getId();
    }
    private static Map<String,Object> observe(ChangeTrial trial,String id) {
        var p=trial.process(); var h=trial.session().processes().getHistoryService();
        return Map.of("id",id,"state",JSON.readTree(StateCodec.encode(p.state(id))),"tasks",p.tasks(id),
                "taskHistory",h.createHistoricTaskInstanceQuery().processInstanceId(id).list().stream()
                    .map(t->t.getId()+"/"+t.getTaskDefinitionKey()+"/"+t.getStartTime().getTime()+"/"+(t.getEndTime()==null?"pending":t.getEndTime().getTime())).sorted().toList(),
                "stateHistory",h.createHistoricDetailQuery().processInstanceId(id).variableUpdates().list().stream()
                    .map(x->(HistoricVariableUpdate)x).filter(x->x.getVariableName().equals(ChangeProcess.STATE))
                    .map(x->Map.of("id",x.getId(),"value",JSON.readTree((String)x.getValue()))).sorted(Comparator.comparing(x->x.get("id").toString())).toList());
    }
    private static ArtifactRevision artifact(String id,int revision,ArtifactRevision.Kind kind) {
        return ChangeProcessTest.artifact(new ArtifactRef(id,revision),kind);
    }
    private static void send(ChangeProcess p,String id,String command,Role role,Operation op) {
        p.execute(new Envelope(command,id,p.tasks(id).get(0).id(),p.state(id).version(),role),op);
    }
    private static void prepare(ChangeProcess p,String id,int revision) {
        send(p,id,"prepare-"+revision,AGENT,new Prepare(artifact("AT-01",revision,ArtifactRevision.Kind.TEST_CASE),
                artifact("CODE-01",revision,ArtifactRevision.Kind.SOFTWARE),"Fikcyjna poprawka testu/programu"));
    }
    private static Assess results(ChangeProcess p,String id,String prefix,ReviewRecord.Outcome test) {
        var c=p.state(id).snapshot().current(); var r=c.get("CAP-01"); var t=c.get("AT-01"); var code=c.get("CODE-01");
        return new Assess(List.of(new ReviewRecord(prefix+"-cap",r,List.of(),ReviewRecord.Outcome.PASS,"Ocena w fabule"),
                new ReviewRecord(prefix+"-test",t,List.of(r),test,"Ocena testu w fabule")),
                List.of(new TestRunRecord(prefix+"-run",t,code,TestRunRecord.Outcome.PASS)),"Fikcyjne oceny, bez uruchomienia TextStats");
    }
}
