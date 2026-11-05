package org.example.processlab.domain;

public record ArtifactRef(String id, int revision) {
    public ArtifactRef {
        id = Values.nonBlank(id, "id");
        if (revision < 1) {
            throw new IllegalArgumentException("revision must be positive");
        }
    }
}
