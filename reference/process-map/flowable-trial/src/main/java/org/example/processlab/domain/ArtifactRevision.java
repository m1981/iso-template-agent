package org.example.processlab.domain;

import java.util.Objects;

public record ArtifactRevision(ArtifactRef ref, Kind kind, String content) {
    public ArtifactRevision {
        Objects.requireNonNull(ref, "ref");
        Objects.requireNonNull(kind, "kind");
        content = Values.nonBlank(content, "content");
    }

    public enum Kind { REQUIREMENT, TEST_CASE, SOFTWARE }
}
