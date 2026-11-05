package org.example.processlab.rules;

import java.util.*;
import org.example.processlab.domain.*;

/** Immutable input; missing references are assessed by rules, ambiguous identity is rejected here. */
public record ProjectSnapshot(List<ArtifactRevision> artifacts, Map<String, ArtifactRef> current,
                              List<Dependency> dependencies, List<ReviewRecord> reviews, List<TestRunRecord> runs) {
    public ProjectSnapshot {
        artifacts = List.copyOf(artifacts);
        current = Map.copyOf(current);
        dependencies = List.copyOf(dependencies);
        reviews = List.copyOf(reviews);
        runs = List.copyOf(runs);
        var refs = new HashSet<ArtifactRef>();
        var kinds = new HashMap<String, ArtifactRevision.Kind>();
        for (var artifact : artifacts) {
            if (!refs.add(artifact.ref())) throw new IllegalArgumentException("Duplicate revision: " + artifact.ref());
            var previous = kinds.putIfAbsent(artifact.ref().id(), artifact.kind());
            if (previous != null && previous != artifact.kind()) throw new IllegalArgumentException("Changed artifact kind");
        }
        current.forEach((id, ref) -> {
            if (!id.equals(ref.id())) throw new IllegalArgumentException("Current key differs from reference ID");
        });
        var evidenceIds = new HashSet<String>();
        for (var review : reviews) requireUnique(evidenceIds, review.id());
        for (var run : runs) requireUnique(evidenceIds, run.id());
    }
    private static void requireUnique(Set<String> ids, String id) {
        if (!ids.add(id)) throw new IllegalArgumentException("Duplicate evidence ID: " + id);
    }
    public ProjectSnapshot append(ReviewRecord review) {
        var next = new ArrayList<>(reviews);
        next.add(Objects.requireNonNull(review));
        return new ProjectSnapshot(artifacts, current, dependencies, next, runs);
    }
    public ProjectSnapshot append(TestRunRecord run) {
        var next = new ArrayList<>(runs);
        next.add(Objects.requireNonNull(run));
        return new ProjectSnapshot(artifacts, current, dependencies, reviews, next);
    }
}
