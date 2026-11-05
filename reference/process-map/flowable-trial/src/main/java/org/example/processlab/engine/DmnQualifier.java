package org.example.processlab.engine;

import java.util.Map;
import java.util.Objects;
import org.example.processlab.rules.AssessmentFacts;
import org.example.processlab.rules.Qualification;
import org.flowable.dmn.api.DmnDecisionService;
import org.flowable.dmn.engine.DmnEngine;
import org.flowable.dmn.api.DmnRepositoryService;
import org.flowable.dmn.api.DmnDecision;

/** Executes one pinned deployment. TO_OPERATOR is a qualification, never an approval. */
public final class DmnQualifier {
    private final DmnDecisionService service;
    private final String parentDeploymentId;

    private final DmnRepositoryService repository;
    private final String definitionId;
    private final int decisionVersion;

    public DmnQualifier(DmnEngine engine, String parentDeploymentId) {
        this.service = Objects.requireNonNull(engine).getDmnDecisionService();
        this.parentDeploymentId = Objects.requireNonNull(parentDeploymentId);
        if (parentDeploymentId.isBlank()) throw new IllegalArgumentException("Deployment ID is blank");
        this.repository = engine.getDmnRepositoryService();
        var definition = resolve();
        this.definitionId = definition.getId();
        this.decisionVersion = definition.getVersion();
    }
    public Qualification evaluate(AssessmentFacts facts) { return evaluate(facts, false); }
    public Qualification evaluateWithoutHistory(AssessmentFacts facts) { return evaluate(facts, true); }

    private Qualification evaluate(AssessmentFacts facts, boolean withoutHistory) {
        Objects.requireNonNull(facts);
        // Sequential experiment: verify the pinned definition still exists before each execution.
        if (!definitionId.equals(resolve().getId())) throw new IllegalStateException("Pinned definition changed");
        var builder = service.createExecuteDecisionBuilder().decisionKey("qualification")
                .parentDeploymentId(parentDeploymentId)
                .variables(Map.of("basisKnown", facts.basisKnown(), "conflict", facts.conflict(),
                        "failed", facts.failed(), "pending", facts.pending()));
        if (withoutHistory) builder.disableHistory();
        var audit = builder.executeWithAuditTrail();
        // The deployment ID field of the 8.0.0 audit is not populated; check key/version instead.
        if (!"qualification".equals(audit.getDecisionKey()) || decisionVersion != audit.getDecisionVersion()) {
            throw new IllegalStateException("DMN executed a different definition than the pinned one");
        }
        if (Boolean.TRUE.equals(audit.isFailed())
                || (audit.getValidationMessage() != null && !audit.getValidationMessage().isBlank())
                || audit.getDecisionResult() == null || audit.getDecisionResult().size() != 1) {
            throw new IllegalStateException("DMN must produce exactly one valid qualification");
        }
        var value = audit.getDecisionResult().get(0).get("qualification");
        if (!(value instanceof String text)) throw new IllegalStateException("Missing qualification output");
        try {
            return Qualification.valueOf(text);
        } catch (IllegalArgumentException failure) {
            throw new IllegalStateException("Unknown qualification: " + text, failure);
        }
    }
    private DmnDecision resolve() {
        var definitions = repository.createDecisionQuery().decisionKey("qualification")
                .parentDeploymentId(parentDeploymentId).list();
        if (definitions.size() != 1) throw new IllegalStateException("Expected one definition in the requested deployment");
        return definitions.get(0);
    }

}
