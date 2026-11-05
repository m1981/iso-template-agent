package org.example.processlab.domain;

import java.util.List;
import java.util.Objects;

public record ReviewRecord(String id, ArtifactRef subject, List<ArtifactRef> basis, Outcome outcome, String rationale) {
    public ReviewRecord {
        id = Values.nonBlank(id, "id");
        Objects.requireNonNull(subject, "subject");
        basis = List.copyOf(basis);
        Objects.requireNonNull(outcome, "outcome");
        rationale = Values.nonBlank(rationale, "rationale");
    }

    public enum Outcome { PASS, FAIL }
}
