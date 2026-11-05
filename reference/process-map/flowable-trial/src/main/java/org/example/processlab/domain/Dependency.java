package org.example.processlab.domain;

import java.util.Objects;

/** Direction: basis to dependent, irrespective of the relationship's name. */
public record Dependency(ArtifactRef basis, ArtifactRef dependent, Kind kind) {
    public Dependency {
        Objects.requireNonNull(basis, "basis");
        Objects.requireNonNull(dependent, "dependent");
        Objects.requireNonNull(kind, "kind");
    }

    public enum Kind { DERIVED_FROM, VERIFIES }
}
