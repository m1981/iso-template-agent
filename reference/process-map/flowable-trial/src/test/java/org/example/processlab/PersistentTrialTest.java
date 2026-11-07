package org.example.processlab;

import java.nio.file.*;
import java.util.*;
import java.util.concurrent.TimeUnit;
import org.example.processlab.workflow.ChangeTrial;
import org.example.processlab.engine.EngineSession;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.io.TempDir;
import tools.jackson.databind.JsonNode;
import tools.jackson.databind.json.JsonMapper;
import static org.junit.jupiter.api.Assertions.*;

class PersistentTrialTest {
    @TempDir Path temporary;
    static final JsonMapper JSON=JsonMapper.builder().build();
    int count;
    final Set<Long> pids=new HashSet<>();
    Path database() { return temporary.resolve("process"); }
    JsonNode phase(String phase) throws Exception {
        var output=temporary.resolve(String.format("%02d-%s.json",++count,phase));
        var log=output.resolveSibling(output.getFileName()+".log");
        String cp=System.getProperty("surefire.test.class.path",System.getProperty("java.class.path"));
        var child=new ProcessBuilder(Path.of(System.getProperty("java.home"),"bin","java").toString(),"-cp",cp,
                RestartWorker.class.getName(),phase,database().toString(),output.toString())
                .redirectErrorStream(true).redirectOutput(log.toFile()).start();
        try {
            assertTrue(child.waitFor(45,TimeUnit.SECONDS),"Child timed out");
            assertEquals(0,child.exitValue(),()->Files.exists(log)?read(log):"Missing child log");
        } finally { if(child.isAlive()) {child.destroyForcibly(); child.waitFor();} }
        var node=JSON.readTree(Files.readString(output));
        assertTrue(pids.add(node.get("pid").asLong()),"Each phase must use a new JVM PID");
        System.out.println("F5 subprocess "+phase+" pid="+node.get("pid")+" exit=0");
        var export=System.getProperty("restart.output");
        if(export!=null) {
            var directory=Path.of(export); Files.createDirectories(directory);
            for(var suffix:List.of("",".md",".log")) {
                var source=output.resolveSibling(output.getFileName()+suffix);
                Files.copy(source,directory.resolve(source.getFileName()),StandardCopyOption.REPLACE_EXISTING);
            }
        }
        return node;
    }
    static String read(Path p) { try {return Files.readString(p);} catch(Exception e) {throw new RuntimeException(e);} }
    static JsonNode first(JsonNode n) {return n.at("/cases/first");}
    static String task(JsonNode n) {return first(n).at("/tasks/0/key").asText();}
    static void sameStored(JsonNode a,JsonNode b) {
        for(var key:List.of("cases","bpmnDefinitions","dmnDefinitions","dmnParents","dmnHistory"))
            assertEquals(a.get(key),b.get(key),"Persisted "+key);
    }
    @Test void F5_01_to_03_and_05_resumeInNewJvmsAndPreserveAcceptedHistory() throws Exception {
        var created=phase("create");
        assertTrue(Files.isRegularFile(Path.of(database()+".mv.db")),"A file database must survive JVM exit");
        assertEquals("authorize",task(created)); sameStored(created,phase("show"));
        var applied=phase("apply"); assertEquals("assess",task(applied)); sameStored(applied,phase("show"));
        assertTrue(first(applied).at("/state/acceptance").isNull());
        var failed=phase("fail"); assertEquals("prepare",task(failed)); assertEquals(1,failed.get("dmnHistory").size());
        var ready=phase("correct"); assertEquals("accept",task(ready)); sameStored(ready,phase("show"));
        assertTrue(first(ready).at("/state/acceptance").isNull(),"Read/restart must not accept");
        assertEquals(6,first(ready).at("/state/receipts").size());
        assertEquals(6,first(ready).at("/state/snapshot/reviews").size());
        assertEquals(3,first(ready).at("/state/snapshot/runs").size());
        assertEquals(2,ready.get("dmnHistory").size());
        var next=phase("accept-next"); sameStored(next,phase("show")); sameStored(next,phase("show"));
        assertFalse(first(next).at("/state/acceptance").isNull()); assertEquals(0,first(next).get("tasks").size());
        assertEquals(first(next).get("id"),next.at("/cases/next/state/previousProcessId"));
        assertEquals("authorize",next.at("/cases/next/tasks/0/key").asText());
        assertEquals(first(next).at("/state/snapshot"),next.at("/cases/next/state/snapshot"));
        assertTrue(next.at("/cases/next/state/acceptance").isNull());
        assertEquals(created.get("bpmnDefinitions"),next.get("bpmnDefinitions"));
        assertEquals(created.get("dmnDefinitions"),next.get("dmnDefinitions"));
    }
    @Test void F5_04_missingDatabaseIsNotSilentlyCreated() {
        assertThrows(IllegalArgumentException.class,()->{try(var ignored=ChangeTrial.reopenPersistent(database())) {}});
        assertFalse(Files.exists(Path.of(database()+".mv.db")));
    }
    @Test void F5_04_creationCannotOverwriteAnExistingTrial() {
        try(var ignored=ChangeTrial.createPersistent(database())) {}
        assertThrows(IllegalArgumentException.class,()->{try(var ignored=ChangeTrial.createPersistent(database())) {}});
        try(var trial=ChangeTrial.reopenPersistent(database())) {
            assertEquals(1,trial.session().processes().getRepositoryService().createProcessDefinitionQuery().count());
        }
    }
    @Test void F5_04_changedXmlIsRefusedForBothEngines() {
        for(boolean dmn:List.of(false,true)) {
            var db=temporary.resolve("changed_"+dmn);
            try(var t=ChangeTrial.createPersistent(db)) {
                if(dmn) {
                    var r=t.session().decisions().getDmnRepositoryService();
                    var dep=r.createDeploymentQuery().singleResult(); r.deleteDeployment(dep.getId());
                    r.createDeployment().parentDeploymentId(dep.getParentDeploymentId())
                        .addString("qualification.dmn",resource("qualification.dmn").replace("name=\"", "name=\"Changed ")).deploy();
                } else {
                    var r=t.session().processes().getRepositoryService();
                    r.deleteDeployment(r.createDeploymentQuery().singleResult().getId());
                    r.createDeployment().addString("change.bpmn20.xml",resource("change.bpmn20.xml").replace("name=\"", "name=\"Changed ")).deploy();
                }
            }
            assertThrows(IllegalStateException.class,()->{try(var ignored=ChangeTrial.reopenPersistent(db)) {}},"Changed XML: "+dmn);
        }
    }
    @Test void F5_04_duplicateDefinitionsAreRefusedForBothEngines() {
        for(boolean dmn:List.of(false,true)) {
            var db=temporary.resolve("duplicate_"+dmn);
            try(var t=ChangeTrial.createPersistent(db)) {
                if(dmn) t.session().decisions().getDmnRepositoryService().createDeployment().parentDeploymentId("duplicate")
                    .addClasspathResource("qualification.dmn").deploy();
                else t.session().processes().getRepositoryService().createDeployment().addClasspathResource("change.bpmn20.xml").deploy();
            }
            assertThrows(IllegalStateException.class,()->{try(var ignored=ChangeTrial.reopenPersistent(db)) {}},"Duplicate definitions: "+dmn);
        }
    }
    @Test void F5_04_emptyModelStoreIsNotInitializedOnReopen() {
        try(var t=ChangeTrial.createPersistent(database())) {
            var b=t.session().processes().getRepositoryService();
            var d=t.session().decisions().getDmnRepositoryService();
            b.deleteDeployment(b.createDeploymentQuery().singleResult().getId());
            d.deleteDeployment(d.createDeploymentQuery().singleResult().getId());
        }
        assertThrows(IllegalStateException.class,()->{try(var ignored=ChangeTrial.reopenPersistent(database())) {}});
        try(var session=EngineSession.openFile(database(),false,Map.of())) {
            assertEquals("false",session.processes().getProcessEngineConfiguration().getDatabaseSchemaUpdate());
            assertEquals(0,session.processes().getRepositoryService().createDeploymentQuery().count());
            assertEquals(0,session.decisions().getDmnRepositoryService().createDeploymentQuery().count());
        }
    }
    @Test void F5_04_databasePathCannotInjectJdbcSettings() {
        assertThrows(IllegalArgumentException.class,()->{try(var ignored=ChangeTrial.createPersistent(temporary.resolve("bad;IFEXISTS=FALSE"))) {}});
    }
    static String resource(String name) {
        try(var in=PersistentTrialTest.class.getClassLoader().getResourceAsStream(name)) {
            return new String(Objects.requireNonNull(in).readAllBytes(),java.nio.charset.StandardCharsets.UTF_8);
        } catch(java.io.IOException e) {throw new java.io.UncheckedIOException(e);}
    }
}
