package org.example.processlab;

import java.util.ArrayList;
import java.util.List;
import org.example.processlab.domain.ArtifactRef;
import org.example.processlab.domain.ArtifactRevision;
import org.example.processlab.domain.Dependency;
import org.example.processlab.domain.ReviewRecord;
import org.example.processlab.domain.TestRunRecord;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class DomainModelTest {
    @Test
    void rejectsUnidentifiableArtifactReferences() {
        assertAll(
                () -> assertThrows(IllegalArgumentException.class, () -> new ArtifactRef(" ", 1)),
                () -> assertThrows(IllegalArgumentException.class, () -> new ArtifactRef("CAP-01", 0)),
                () -> assertThrows(NullPointerException.class, () -> new ArtifactRef(null, 1)));
    }

    @Test
    void preservesReviewBasisAgainstChangesByCaller() {
        var requirementV1 = new ArtifactRef("CAP-01", 1);
        var requirementV2 = new ArtifactRef("CAP-01", 2);
        var testCase = new ArtifactRef("AT-01", 1);
        var basis = new ArrayList<>(List.of(requirementV1));
        var review = new ReviewRecord("VER-01", testCase, basis, ReviewRecord.Outcome.PASS, "Fictional review");
        basis.set(0, requirementV2);
        assertEquals(List.of(requirementV1), review.basis());
        assertThrows(UnsupportedOperationException.class, () -> review.basis().clear());
    }

    @Test
    void keepsOldEvidenceAndNewVersionsDistinctWithoutInferringValidity() {
        var before = new ArtifactRevision(new ArtifactRef("CAP-01", 1),
                ArtifactRevision.Kind.REQUIREMENT, "biało-czerwony → 1");
        var after = new ArtifactRevision(new ArtifactRef("CAP-01", 2),
                ArtifactRevision.Kind.REQUIREMENT, "biało-czerwony → 2");
        var test = new ArtifactRef("AT-01", 1);
        var link = new Dependency(before.ref(), test, Dependency.Kind.VERIFIES);
        var review = new ReviewRecord("VER-01", test, List.of(before.ref()),
                ReviewRecord.Outcome.PASS, "Fictional adequacy assessment");
        var run = new TestRunRecord("RUN-01", test, new ArtifactRef("CODE-01", 1), TestRunRecord.Outcome.PASS);

        assertNotEquals(before.ref(), after.ref());
        assertEquals(before.ref(), link.basis());
        assertEquals(before.ref(), review.basis().get(0));
        assertEquals(test, run.testCase());
        assertEquals(new ArtifactRef("CODE-01", 1), run.software());
    }

    @Test
    void rejectsIncompleteEvidenceAndLinks() {
        var requirement = new ArtifactRef("CAP-01", 1);
        assertAll(
                () -> assertThrows(NullPointerException.class,
                        () -> new ArtifactRevision(requirement, null, "Example")),
                () -> assertThrows(IllegalArgumentException.class,
                        () -> new ArtifactRevision(requirement, ArtifactRevision.Kind.REQUIREMENT, "")),
                () -> assertThrows(NullPointerException.class,
                        () -> new Dependency(requirement, null, Dependency.Kind.VERIFIES)),
                () -> assertThrows(NullPointerException.class,
                        () -> new ReviewRecord("VER-01", requirement, List.of(), null, "Example")),
                () -> assertThrows(IllegalArgumentException.class,
                        () -> new ReviewRecord("VER-01", requirement, List.of(), ReviewRecord.Outcome.FAIL, " ")),
                () -> assertThrows(NullPointerException.class,
                        () -> new TestRunRecord("RUN-01", requirement, null, TestRunRecord.Outcome.PASS)));
    }
}
