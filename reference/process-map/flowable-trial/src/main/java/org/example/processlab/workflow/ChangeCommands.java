package org.example.processlab.workflow;

import java.util.List;
import java.util.Objects;
import org.example.processlab.domain.*;

/** Commands from the trusted local teaching harness, not authentication credentials. */
public final class ChangeCommands {
    private ChangeCommands() {}
    public enum Role { AGENT, OPERATOR }
    public record Envelope(String id, String processId, String taskId, long expectedVersion, Role role) {
        public Envelope {
            text(id); text(processId); text(taskId); Objects.requireNonNull(role);
            if (expectedVersion < 0) throw new IllegalArgumentException("Negative state version");
        }
    }
    public sealed interface Operation permits Authorize, ApplyChange, Prepare, Assess, Decide, Propose, Rework {
        String reason();
    }
    public record Authorize(boolean allowed, String reason) implements Operation { public Authorize { text(reason); } }
    public record ApplyChange(String reason) implements Operation { public ApplyChange { text(reason); } }
    public record Prepare(ArtifactRevision test, ArtifactRevision software, String reason) implements Operation {
        public Prepare { Objects.requireNonNull(test); Objects.requireNonNull(software); text(reason); }
    }
    public record Assess(List<ReviewRecord> reviews, List<TestRunRecord> runs, String reason) implements Operation {
        public Assess { reviews=List.copyOf(reviews); runs=List.copyOf(runs); text(reason); }
    }
    public record Decide(boolean accepted, String reason) implements Operation { public Decide { text(reason); } }
    public record Propose(ArtifactRevision requirement, String reason) implements Operation {
        public Propose { Objects.requireNonNull(requirement); text(reason); }
    }
    public record Rework(String reason) implements Operation { public Rework { text(reason); } }
    static void text(String text) {
        if (text == null || text.isBlank()) throw new IllegalArgumentException("Nonblank text required");
    }
}
