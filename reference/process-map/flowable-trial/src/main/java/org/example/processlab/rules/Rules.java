package org.example.processlab.rules;

import java.util.*;
import java.util.function.Function;
import java.util.stream.Collectors;
import org.example.processlab.domain.*;
import static org.example.processlab.rules.CheckStatus.*;

/** Structural calculations only; no assessment of truth, completeness of scope, or permission. */
public final class Rules {
    private Rules() {}

    /** Advisory reachability by logical ID, including edges still pointing to earlier revisions. */
    public static Map<String, List<String>> impact(ProjectSnapshot s, String source) {
        if (s.artifacts().stream().noneMatch(a -> a.ref().id().equals(source))) {
            throw new IllegalArgumentException("Unknown impact source: " + source);
        }
        var adjacency = new HashMap<String, SortedSet<String>>();
        for (var edge : s.dependencies()) {
            adjacency.computeIfAbsent(edge.basis().id(), ignored -> new TreeSet<>()).add(edge.dependent().id());
        }
        var paths = new LinkedHashMap<String, List<String>>();
        var visited = new HashSet<String>();
        var queue = new ArrayDeque<String>();
        visited.add(source);
        paths.put(source, List.of(source));
        queue.add(source);
        while (!queue.isEmpty()) {
            var node = queue.remove();
            for (var dependent : adjacency.getOrDefault(node, Collections.emptySortedSet())) {
                if (visited.add(dependent)) {
                    var path = new ArrayList<>(paths.get(node));
                    path.add(dependent);
                    paths.put(dependent, List.copyOf(path));
                    queue.add(dependent);
                }
            }
        }
        paths.remove(source);
        return Collections.unmodifiableMap(paths);
    }

    public static CheckStatus review(ProjectSnapshot s, ArtifactRef subject) {
        var index = index(s);
        var subjectState = currentState(s, index, subject);
        if (subjectState != PASSED) return subjectState;
        var basis = new HashSet<ArtifactRef>();
        boolean stale = false;
        for (var edge : s.dependencies()) {
            if (!edge.dependent().id().equals(subject.id())) continue;
            var basisState = currentState(s, index, edge.basis());
            var dependentState = currentState(s, index, edge.dependent());
            if (basisState == UNKNOWN || dependentState == UNKNOWN) return UNKNOWN;
            if (edge.kind() == Dependency.Kind.VERIFIES
                    && (index.get(edge.basis()).kind() != ArtifactRevision.Kind.REQUIREMENT
                    || index.get(edge.dependent()).kind() != ArtifactRevision.Kind.TEST_CASE)) return UNKNOWN;
            stale |= basisState != PASSED || dependentState != PASSED;
            basis.add(s.current().get(edge.basis().id()));
        }
        if (stale) return REVIEW_REQUIRED;
        var outcomes = EnumSet.noneOf(ReviewRecord.Outcome.class);
        for (var review : s.reviews()) {
            if (review.subject().equals(subject) && new HashSet<>(review.basis()).equals(basis)) {
                outcomes.add(review.outcome());
            }
        }
        return outcome(outcomes.contains(ReviewRecord.Outcome.PASS), outcomes.contains(ReviewRecord.Outcome.FAIL));
    }

    public static CheckStatus testRun(ProjectSnapshot s, ArtifactRef test, ArtifactRef software) {
        var index = index(s);
        var testState = currentState(s, index, test);
        var softwareState = currentState(s, index, software);
        if (testState == UNKNOWN || softwareState == UNKNOWN) return UNKNOWN;
        if (index.get(test).kind() != ArtifactRevision.Kind.TEST_CASE
                || index.get(software).kind() != ArtifactRevision.Kind.SOFTWARE) return UNKNOWN;
        if (testState != PASSED || softwareState != PASSED) return REVIEW_REQUIRED;
        var outcomes = EnumSet.noneOf(TestRunRecord.Outcome.class);
        for (var run : s.runs()) {
            if (run.testCase().equals(test) && run.software().equals(software)) outcomes.add(run.outcome());
        }
        if (outcomes.contains(TestRunRecord.Outcome.ERROR)) return UNKNOWN;
        return outcome(outcomes.contains(TestRunRecord.Outcome.PASS), outcomes.contains(TestRunRecord.Outcome.FAIL));
    }

    public static AssessmentFacts facts(List<CheckStatus> checks) {
        var known = List.copyOf(checks);
        return new AssessmentFacts(!known.isEmpty() && !known.contains(UNKNOWN), known.contains(CONFLICT),
                known.contains(CORRECTION), known.contains(REVIEW_REQUIRED));
    }

    private static Map<ArtifactRef, ArtifactRevision> index(ProjectSnapshot s) {
        return s.artifacts().stream().collect(Collectors.toMap(ArtifactRevision::ref, Function.identity()));
    }
    private static CheckStatus currentState(ProjectSnapshot s, Map<ArtifactRef, ArtifactRevision> index, ArtifactRef ref) {
        Objects.requireNonNull(ref);
        var current = s.current().get(ref.id());
        if (!index.containsKey(ref) || current == null || !index.containsKey(current)) return UNKNOWN;
        return ref.equals(current) ? PASSED : REVIEW_REQUIRED;
    }
    private static CheckStatus outcome(boolean pass, boolean fail) {
        if (pass && fail) return CONFLICT;
        if (fail) return CORRECTION;
        return pass ? PASSED : REVIEW_REQUIRED;
    }
}
