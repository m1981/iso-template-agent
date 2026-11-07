package org.example.processlab.workflow;

import java.io.*;
import java.nio.file.Path;
import java.util.*;
import java.util.concurrent.atomic.AtomicReference;
import java.util.function.Function;
import org.example.processlab.engine.*;

/** Composition root for one isolated, sequential experiment; no model/schema migration. */
public final class ChangeTrial implements AutoCloseable {
    private final EngineSession session;
    private final ChangeProcess process;
    private ChangeTrial(EngineSession session, ChangeProcess process) { this.session=session; this.process=process; }
    public static ChangeTrial open(String name) {
        return open(beans->EngineSession.openInMemory(name,beans),true);
    }
    public static ChangeTrial createPersistent(Path database) {
        return open(beans->EngineSession.openFile(database,true,beans),true);
    }
    public static ChangeTrial reopenPersistent(Path database) {
        return open(beans->EngineSession.openFile(database,false,beans),false);
    }
    private static ChangeTrial open(Function<Map<String,Object>,EngineSession> factory,boolean deploy) {
        var qualifier=new AtomicReference<DmnQualifier>();
        var session=factory.apply(Map.of("qualificationStep",new QualificationStep(qualifier::get)));
        try {
            var decisions=session.decisions().getDmnRepositoryService();
            var repository=session.processes().getRepositoryService();
            if(deploy) {
                decisions.createDeployment().parentDeploymentId(UUID.randomUUID().toString())
                        .addClasspathResource("qualification.dmn").deploy();
                repository.createDeployment().addClasspathResource("change.bpmn20.xml").deploy();
            }
            // One pair of models in this experiment; never choose "latest" on resume.
            var processDefinitions=repository.createProcessDefinitionQuery().list();
            var decisionDefinitions=decisions.createDecisionQuery().list();
            if(processDefinitions.size()!=1 || decisionDefinitions.size()!=1
                    || repository.createDeploymentQuery().count()!=1 || decisions.createDeploymentQuery().count()!=1) {
                throw new IllegalStateException("Expected exactly one BPMN and one DMN deployment/definition");
            }
            var definition=processDefinitions.get(0);
            var decision=decisionDefinitions.get(0);
            var decisionDeployment=decisions.createDeploymentQuery().deploymentId(decision.getDeploymentId()).singleResult();
            sameResource(repository.getResourceAsStream(definition.getDeploymentId(),"change.bpmn20.xml"),"change.bpmn20.xml");
            sameResource(decisions.getResourceAsStream(decision.getDeploymentId(),"qualification.dmn"),"qualification.dmn");
            qualifier.set(new DmnQualifier(session.decisions(),decisionDeployment.getParentDeploymentId()));
            return new ChangeTrial(session,new ChangeProcess(session.processes(),qualifier.get(),definition.getId()));
        } catch (RuntimeException failure) {
            try {session.close();} catch (RuntimeException cleanup) {failure.addSuppressed(cleanup);}
            throw failure;
        }
    }
    private static void sameResource(InputStream stored,String resource) {
        try(stored; var current=ChangeTrial.class.getClassLoader().getResourceAsStream(resource)) {
            if(stored==null || current==null || !Arrays.equals(stored.readAllBytes(),current.readAllBytes())) {
                throw new IllegalStateException("Stored model differs from this build: "+resource);
            }
        } catch(IOException failure) {throw new UncheckedIOException(failure);}
    }
    public EngineSession session() { return session; }
    public ChangeProcess process() { return process; }
    @Override public void close() {session.close();}
}
