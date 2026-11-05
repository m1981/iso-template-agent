package org.example.processlab.workflow;

import java.util.List;
import java.util.Map;
import java.util.Objects;
import org.example.processlab.domain.*;
import org.example.processlab.rules.ProjectSnapshot;
import org.example.processlab.workflow.ChangeCommands.Role;

/** Domain state only; the phase and task lifecycle belong to BPMN. */
public record ChangeState(long version, Scope scope, ProjectSnapshot snapshot, ArtifactRevision proposal,
                          boolean authorized, String previousProcessId, List<Receipt> receipts, Acceptance acceptance) {
    public ChangeState {
        if (version < 0) throw new IllegalArgumentException("Negative state version");
        Objects.requireNonNull(scope); Objects.requireNonNull(snapshot); Objects.requireNonNull(proposal);
        receipts = List.copyOf(receipts);
    }
    public record Scope(String requirementId, String testId, String softwareId) {
        public Scope { ChangeCommands.text(requirementId); ChangeCommands.text(testId); ChangeCommands.text(softwareId); }
    }
    public record Receipt(String commandId, String taskId, long baseVersion, Role role, String action, String reason) {}
    public record Acceptance(String commandId, long stateVersion, Map<String,ArtifactRef> basis, String reason) {
        public Acceptance { basis=Map.copyOf(basis); }
    }
}
