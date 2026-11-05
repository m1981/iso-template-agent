package org.example.processlab.workflow;

import java.util.function.Supplier;
import org.example.processlab.engine.DmnQualifier;
import org.flowable.engine.delegate.JavaDelegate;
import org.flowable.engine.delegate.DelegateExecution;

/** Runs synchronously inside the BPMN completion transaction, including DMN history. */
public final class QualificationStep implements JavaDelegate {
    private final Supplier<DmnQualifier> qualifier;
    public QualificationStep(Supplier<DmnQualifier> qualifier) { this.qualifier=qualifier; }
    @Override public void execute(DelegateExecution execution) {
        var state=StateCodec.decode((String)execution.getVariable(ChangeProcess.STATE));
        execution.setVariable("qualification",qualifier.get().evaluate(WorkflowChecks.facts(state)).name());
    }
}
