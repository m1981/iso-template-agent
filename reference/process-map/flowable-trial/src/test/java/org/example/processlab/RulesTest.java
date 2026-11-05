package org.example.processlab;

import java.util.*;
import org.example.processlab.domain.*;
import org.example.processlab.rules.*;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import static org.example.processlab.rules.CheckStatus.*;

class RulesTest {
    static final ArtifactRef R1 = ref("CAP-01", 1), R2 = ref("CAP-01", 2);
    static final ArtifactRef T1 = ref("AT-01", 1), T2 = ref("AT-01", 2);
    static final ArtifactRef C1 = ref("CODE-01", 1), C2 = ref("CODE-01", 2);
    static ArtifactRef ref(String id, int rev) { return new ArtifactRef(id, rev); }
    static ArtifactRevision artifact(ArtifactRef ref, ArtifactRevision.Kind kind) {
        return new ArtifactRevision(ref, kind, "Fictional " + ref);
    }
    static List<ArtifactRevision> artifacts() {
        return List.of(artifact(R1, ArtifactRevision.Kind.REQUIREMENT), artifact(R2, ArtifactRevision.Kind.REQUIREMENT),
                artifact(T1, ArtifactRevision.Kind.TEST_CASE), artifact(T2, ArtifactRevision.Kind.TEST_CASE),
                artifact(C1, ArtifactRevision.Kind.SOFTWARE), artifact(C2, ArtifactRevision.Kind.SOFTWARE));
    }
    static ReviewRecord review(String id, ArtifactRef subject, List<ArtifactRef> basis, ReviewRecord.Outcome result) {
        return new ReviewRecord(id, subject, basis, result, "Fictional assessment");
    }
    static TestRunRecord run(String id, ArtifactRef test, ArtifactRef code, TestRunRecord.Outcome result) {
        return new TestRunRecord(id, test, code, result);
    }
    static ProjectSnapshot snapshot(List<ReviewRecord> reviews, List<TestRunRecord> runs) {
        return new ProjectSnapshot(artifacts(), Map.of("CAP-01", R2, "AT-01", T2, "CODE-01", C2),
                List.of(new Dependency(R2, T2, Dependency.Kind.VERIFIES)), reviews, runs);
    }

    @Test void R1_rejectsAmbiguousIdentityButDoesNotChooseHighestRevision() {
        var sameRefDifferentContent = new ArtifactRevision(R2, ArtifactRevision.Kind.REQUIREMENT, "Contradiction");
        var duplicate = new ArrayList<>(artifacts()); duplicate.add(sameRefDifferentContent);
        assertThrows(IllegalArgumentException.class, () -> new ProjectSnapshot(duplicate, Map.of(), List.of(), List.of(), List.of()));
        var wrongKind = List.of(artifact(R1, ArtifactRevision.Kind.REQUIREMENT), artifact(R2, ArtifactRevision.Kind.SOFTWARE));
        assertThrows(IllegalArgumentException.class, () -> new ProjectSnapshot(wrongKind, Map.of(), List.of(), List.of(), List.of()));
        assertThrows(IllegalArgumentException.class, () -> new ProjectSnapshot(artifacts(), Map.of("wrong", R2), List.of(), List.of(), List.of()));
        var oldCurrent = new ProjectSnapshot(artifacts(), Map.of("CAP-01", R1), List.of(),
                List.of(review("V1", R1, List.of(), ReviewRecord.Outcome.PASS)), List.of());
        assertEquals(PASSED, Rules.review(oldCurrent, R1));
        assertEquals(REVIEW_REQUIRED, Rules.review(oldCurrent, R2));
    }

    @Test void R2_appendPreservesHistoryAndRejectsReplacementAndReplay() {
        var first = review("V1", R2, List.of(), ReviewRecord.Outcome.FAIL);
        var original = snapshot(List.of(first), List.of());
        var before = original.toString();
        var next = original.append(review("V2", R2, List.of(), ReviewRecord.Outcome.PASS));
        assertEquals(List.of(first), original.reviews());
        assertEquals(2, next.reviews().size());
        assertThrows(IllegalArgumentException.class, () -> original.append(first));
        assertThrows(IllegalArgumentException.class, () -> original.append(review("V1", R2, List.of(), ReviewRecord.Outcome.PASS)));
        assertThrows(IllegalArgumentException.class, () -> original.append(run("V1", T2, C2, TestRunRecord.Outcome.PASS)));
        var withRun = original.append(run("X1", T2, C2, TestRunRecord.Outcome.PASS));
        assertEquals(1, withRun.runs().size());
        assertThrows(IllegalArgumentException.class, () -> withRun.append(run("X1", T2, C2, TestRunRecord.Outcome.FAIL)));
        assertThrows(IllegalArgumentException.class, () -> snapshot(List.of(first, first), List.of()));
        assertEquals(before, original.toString());
        assertThrows(UnsupportedOperationException.class, () -> next.reviews().clear());
    }

    @Test void R3_reachabilityUsesIdsAndReturnsDeterministicPathsWithoutDuplicates() {
        var a = ref("A", 1); var b = ref("B", 1); var c = ref("C", 1); var d = ref("D", 1); var x = ref("X", 1);
        var nodes = List.of(a,b,c,d,x).stream().map(r -> artifact(r, ArtifactRevision.Kind.REQUIREMENT)).toList();
        var edges = List.of(new Dependency(a,c,Dependency.Kind.DERIVED_FROM), new Dependency(a,b,Dependency.Kind.DERIVED_FROM),
                new Dependency(b,d,Dependency.Kind.DERIVED_FROM), new Dependency(c,d,Dependency.Kind.DERIVED_FROM),
                new Dependency(d,a,Dependency.Kind.DERIVED_FROM));
        var s = new ProjectSnapshot(nodes, Map.of("A",a,"B",b,"C",c,"D",d,"X",x),edges,List.of(),List.of());
        var found = Rules.impact(s,"A");
        assertEquals(Set.of("B","C","D"), found.keySet());
        assertEquals(List.of("A","B","D"),found.get("D"));
        assertEquals(Map.of(), Rules.impact(s,"X"));
        assertThrows(IllegalArgumentException.class, () -> Rules.impact(s,"MISSING"));
        var revised = new ProjectSnapshot(artifacts(),Map.of("CAP-01",R2,"AT-01",T2),
                List.of(new Dependency(R1,T2,Dependency.Kind.VERIFIES)),List.of(),List.of());
        assertEquals(List.of("CAP-01","AT-01"),Rules.impact(revised,"CAP-01").get("AT-01"));
    }

    @Test void R4_requiresExactCurrentSubjectAndBasis() {
        var pass = review("V1",T2,List.of(R2),ReviewRecord.Outcome.PASS);
        assertEquals(PASSED, Rules.review(snapshot(List.of(pass),List.of()),T2));
        assertEquals(REVIEW_REQUIRED, Rules.review(snapshot(List.of(),List.of()),T2));
        assertEquals(REVIEW_REQUIRED, Rules.review(snapshot(List.of(review("old",T2,List.of(R1),ReviewRecord.Outcome.PASS)),List.of()),T2));
        assertEquals(REVIEW_REQUIRED, Rules.review(snapshot(List.of(review("old",T1,List.of(R2),ReviewRecord.Outcome.PASS)),List.of()),T2));
        assertEquals(REVIEW_REQUIRED, Rules.review(snapshot(List.of(review("missingBasis",T2,List.of(),ReviewRecord.Outcome.PASS)),List.of()),T2));
        assertEquals(REVIEW_REQUIRED, Rules.review(snapshot(List.of(review("extraBasis",T2,List.of(R2,C2),ReviewRecord.Outcome.PASS)),List.of()),T2));
        assertEquals(PASSED, Rules.review(snapshot(List.of(review("duplicateBasis",T2,List.of(R2,R2),ReviewRecord.Outcome.PASS)),List.of()),T2));
        var staleEdge = new ProjectSnapshot(artifacts(),snapshot(List.of(),List.of()).current(),
                List.of(new Dependency(R1,T2,Dependency.Kind.VERIFIES)),List.of(pass),List.of());
        assertEquals(REVIEW_REQUIRED, Rules.review(staleEdge,T2));
        var staleDependent = new ProjectSnapshot(artifacts(),snapshot(List.of(),List.of()).current(),
                List.of(new Dependency(R2,T1,Dependency.Kind.VERIFIES)),List.of(pass),List.of());
        assertEquals(REVIEW_REQUIRED, Rules.review(staleDependent,T2));
    }

    @Test void R4_missingBasisAndConflictsAreNotHiddenByPass() {
        var pass = review("pass",T2,List.of(R2),ReviewRecord.Outcome.PASS);
        var fail = review("fail",T2,List.of(R2),ReviewRecord.Outcome.FAIL);
        assertEquals(CORRECTION,Rules.review(snapshot(List.of(fail),List.of()),T2));
        assertEquals(CONFLICT,Rules.review(snapshot(List.of(pass,fail),List.of()),T2));
        assertEquals(CONFLICT,Rules.review(snapshot(List.of(fail,pass),List.of()),T2));
        var oldFail = review("oldFail",T1,List.of(R1),ReviewRecord.Outcome.FAIL);
        assertEquals(PASSED,Rules.review(snapshot(List.of(oldFail,pass),List.of()),T2));
        assertEquals(UNKNOWN,Rules.review(snapshot(List.of(),List.of()),ref("MISSING",1)));
        var unknown = new ProjectSnapshot(artifacts(),snapshot(List.of(),List.of()).current(),
                List.of(new Dependency(ref("MISSING",1),T2,Dependency.Kind.VERIFIES)),List.of(pass),List.of());
        assertEquals(UNKNOWN,Rules.review(unknown,T2));
        var noCurrent = new ProjectSnapshot(artifacts(),Map.of(),List.of(),List.of(pass),List.of());
        assertEquals(UNKNOWN,Rules.review(noCurrent,T2));
        var capOnly = review("CAPpass",R2,List.of(),ReviewRecord.Outcome.PASS);
        assertEquals(REVIEW_REQUIRED,Rules.review(snapshot(List.of(capOnly),List.of()),T2));
    }

    @Test void R5_requiresCurrentTestAndSoftwareAndKeepsExecutionSeparate() {
        var pass = run("pass",T2,C2,TestRunRecord.Outcome.PASS);
        assertEquals(PASSED,Rules.testRun(snapshot(List.of(),List.of(pass)),T2,C2));
        assertEquals(REVIEW_REQUIRED,Rules.testRun(snapshot(List.of(),List.of(run("old",T1,C2,TestRunRecord.Outcome.PASS))),T2,C2));
        assertEquals(REVIEW_REQUIRED,Rules.testRun(snapshot(List.of(),List.of(run("old",T2,C1,TestRunRecord.Outcome.PASS))),T2,C2));
        assertEquals(REVIEW_REQUIRED,Rules.testRun(snapshot(List.of(review("V1",T2,List.of(R2),ReviewRecord.Outcome.PASS)),List.of()),T2,C2));
        assertEquals(UNKNOWN,Rules.testRun(snapshot(List.of(),List.of()),R2,C2));
        assertEquals(UNKNOWN,Rules.testRun(snapshot(List.of(),List.of()),T2,R2));
        var fail=run("fail",T2,C2,TestRunRecord.Outcome.FAIL);
        var error=run("error",T2,C2,TestRunRecord.Outcome.ERROR);
        assertEquals(CORRECTION,Rules.testRun(snapshot(List.of(),List.of(fail)),T2,C2));
        assertEquals(CONFLICT,Rules.testRun(snapshot(List.of(),List.of(pass,fail)),T2,C2));
        assertEquals(CONFLICT,Rules.testRun(snapshot(List.of(),List.of(fail,pass)),T2,C2));
        assertEquals(UNKNOWN,Rules.testRun(snapshot(List.of(),List.of(pass,error)),T2,C2));
        assertEquals(UNKNOWN,Rules.testRun(snapshot(List.of(),List.of(error)),T2,C2));
    }

    @Test void R6_emptyAndMixedChecksProduceExplicitFacts() {
        assertEquals(new AssessmentFacts(false,false,false,false),Rules.facts(List.of()));
        assertEquals(new AssessmentFacts(true,false,false,false),Rules.facts(List.of(PASSED)));
        assertEquals(new AssessmentFacts(true,false,false,true),Rules.facts(List.of(PASSED,REVIEW_REQUIRED)));
        assertEquals(new AssessmentFacts(false,true,true,true),Rules.facts(List.of(UNKNOWN,CONFLICT,CORRECTION,REVIEW_REQUIRED)));
        assertThrows(NullPointerException.class, () -> Rules.facts(Arrays.asList(PASSED,null)));
    }
    @Test void R1_copiesCollectionsAndRejectsCrossKindEvidenceIds() {
        var nodes = new ArrayList<>(artifacts());
        var current = new HashMap<>(Map.of("CAP-01",R2));
        var s = new ProjectSnapshot(nodes,current,List.of(),List.of(),List.of());
        nodes.clear(); current.clear();
        assertEquals(6,s.artifacts().size());
        assertEquals(R2,s.current().get("CAP-01"));
        assertThrows(UnsupportedOperationException.class, () -> s.current().clear());
        assertThrows(IllegalArgumentException.class, () -> snapshot(
                List.of(review("shared",R2,List.of(),ReviewRecord.Outcome.PASS)),
                List.of(run("shared",T2,C2,TestRunRecord.Outcome.PASS))));
    }
    @Test void R3_edgeOrderDoesNotChooseDifferentDiamondPath() {
        var a=ref("A",1); var b=ref("B",1); var c=ref("C",1); var d=ref("D",1);
        var edges=new ArrayList<>(List.of(new Dependency(a,c,Dependency.Kind.DERIVED_FROM),
                new Dependency(a,b,Dependency.Kind.DERIVED_FROM),new Dependency(c,d,Dependency.Kind.DERIVED_FROM),
                new Dependency(b,d,Dependency.Kind.DERIVED_FROM)));
        var nodes=List.of(a,b,c,d).stream().map(r -> artifact(r,ArtifactRevision.Kind.REQUIREMENT)).toList();
        var first=Rules.impact(new ProjectSnapshot(nodes,Map.of(),edges,List.of(),List.of()),"A");
        Collections.reverse(edges);
        assertEquals(first,Rules.impact(new ProjectSnapshot(nodes,Map.of(),edges,List.of(),List.of()),"A"));
        assertEquals(List.of("A","B","D"),first.get("D"));
    }
    @Test void R4_basisOrderIsIrrelevantAndInvalidVerifiesTypeIsUnknown() {
        var s=snapshot(List.of(review("V",T2,List.of(C2,R2),ReviewRecord.Outcome.PASS)),List.of());
        var edges=List.of(new Dependency(R2,T2,Dependency.Kind.VERIFIES),new Dependency(C2,T2,Dependency.Kind.DERIVED_FROM));
        assertEquals(PASSED,Rules.review(new ProjectSnapshot(s.artifacts(),s.current(),edges,s.reviews(),s.runs()),T2));
        var bad=List.of(new Dependency(C2,T2,Dependency.Kind.VERIFIES));
        assertEquals(UNKNOWN,Rules.review(new ProjectSnapshot(s.artifacts(),s.current(),bad,s.reviews(),s.runs()),T2));
    }
    @Test void R5_unrelatedMissingDataAndOldErrorsDoNotPolluteCurrentPair() {
        var s=snapshot(List.of(),List.of(run("now",T2,C2,TestRunRecord.Outcome.PASS),
                run("oldError",T1,C1,TestRunRecord.Outcome.ERROR),run("oldFail",T1,C1,TestRunRecord.Outcome.FAIL)));
        var incomplete=List.of(new Dependency(ref("MISSING",1),R2,Dependency.Kind.DERIVED_FROM));
        assertEquals(PASSED,Rules.testRun(new ProjectSnapshot(s.artifacts(),s.current(),incomplete,s.reviews(),s.runs()),T2,C2));
        assertEquals(REVIEW_REQUIRED,Rules.testRun(s,T1,C2));
        assertEquals(UNKNOWN,Rules.testRun(s,T2,ref("MISSING",1)));
        var unknownCurrent=new HashMap<>(s.current()); unknownCurrent.put("CODE-01",ref("CODE-01",3));
        assertEquals(UNKNOWN,Rules.testRun(new ProjectSnapshot(s.artifacts(),unknownCurrent,s.dependencies(),s.reviews(),s.runs()),T2,C2));
    }

}
