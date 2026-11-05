package org.example.processlab.domain;

import java.util.Objects;

public record TestRunRecord(String id, ArtifactRef testCase, ArtifactRef software, Outcome outcome) {
    public TestRunRecord {
        id = Values.nonBlank(id, "id");
        Objects.requireNonNull(testCase, "testCase");
        Objects.requireNonNull(software, "software");
        Objects.requireNonNull(outcome, "outcome");
    }

    public enum Outcome { PASS, FAIL, ERROR }
}
