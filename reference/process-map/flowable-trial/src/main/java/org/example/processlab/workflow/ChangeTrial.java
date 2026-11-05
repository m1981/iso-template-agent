package org.example.processlab.workflow;

import java.util.Map;
import java.util.UUID;
import java.util.concurrent.atomic.AtomicReference;
import org.example.processlab.engine.*;

/** Composition root for one isolated, sequential experiment. */
public final class ChangeTrial implements AutoCloseable {
    private final EngineSession session;
    private final ChangeProcess process;
    private ChangeTrial(EngineSession session, ChangeProcess process) { this.session=session; this.process=process; }
    public static ChangeTrial open(String name) {
        var qualifier=new AtomicReference<DmnQualifier>();
        var session=EngineSession.openInMemory(name,Map.of("qualificationStep",new QualificationStep(qualifier::get)));
        try {
            var parent=UUID.randomUUID().toString();
            session.decisions().getDmnRepositoryService().createDeployment().parentDeploymentId(parent)
                    .addClasspathResource("qualification.dmn").deploy();
            qualifier.set(new DmnQualifier(session.decisions(),parent));
            var repository=session.processes().getRepositoryService();
            var deployment=repository.createDeployment().addClasspathResource("change.bpmn20.xml").deploy();
            var definition=repository.createProcessDefinitionQuery().deploymentId(deployment.getId()).singleResult();
            return new ChangeTrial(session,new ChangeProcess(session.processes(),qualifier.get(),definition.getId()));
        } catch (RuntimeException failure) {
            try {session.close();} catch (RuntimeException cleanup) {failure.addSuppressed(cleanup);}
            throw failure;
        }
    }
    public EngineSession session() { return session; }
    public ChangeProcess process() { return process; }
    @Override public void close() {session.close();}
}
