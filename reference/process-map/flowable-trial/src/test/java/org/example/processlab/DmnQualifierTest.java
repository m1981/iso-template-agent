package org.example.processlab;

import java.nio.charset.StandardCharsets;
import java.util.List;
import java.util.UUID;
import org.example.processlab.domain.*;
import org.example.processlab.engine.*;
import org.example.processlab.rules.*;
import org.junit.jupiter.api.*;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import static org.junit.jupiter.api.Assertions.*;
import static org.example.processlab.RulesTest.*;

class DmnQualifierTest {
    static EngineSession engine;
    static String xml;
    static DmnQualifier qualifier;
    @BeforeAll static void start() throws Exception {
        try (var input = DmnQualifierTest.class.getResourceAsStream("/qualification.dmn")) {
            xml = new String(input.readAllBytes(), StandardCharsets.UTF_8);
        }
        engine = EngineSession.openInMemory("dmn_" + UUID.randomUUID().toString().replace("-", ""));
        qualifier = deploy(xml);
    }
    @AfterAll static void close() { if (engine != null) engine.close(); }
    static DmnQualifier deploy(String definition) {
        var parent = UUID.randomUUID().toString();
        engine.decisions().getDmnRepositoryService().createDeployment().parentDeploymentId(parent)
                .addString("qualification.dmn", definition).deploy();
        return new DmnQualifier(engine.decisions(), parent);
    }
    @ParameterizedTest
    @CsvSource({
        "false,false,false,false,MISSING_BASIS", "false,false,false,true,MISSING_BASIS",
        "false,false,true,false,MISSING_BASIS", "false,false,true,true,MISSING_BASIS",
        "false,true,false,false,MISSING_BASIS", "false,true,false,true,MISSING_BASIS",
        "false,true,true,false,MISSING_BASIS", "false,true,true,true,MISSING_BASIS",
        "true,false,false,false,TO_OPERATOR", "true,false,false,true,REVIEW_REQUIRED",
        "true,false,true,false,CORRECTION", "true,false,true,true,CORRECTION",
        "true,true,false,false,REVIEW_REQUIRED", "true,true,false,true,REVIEW_REQUIRED",
        "true,true,true,false,REVIEW_REQUIRED", "true,true,true,true,REVIEW_REQUIRED"
    })
    void R6_allSixteenFactCombinations(boolean known, boolean conflict, boolean failed, boolean pending, Qualification expected) {
        assertEquals(expected, qualifier.evaluate(new AssessmentFacts(known, conflict, failed, pending)));
    }
    @Test void R6_missingMultipleAndUnknownOutputFailClosed() {
        var ready = new AssessmentFacts(true,false,false,false);
        var noMatch = xml.replaceAll("(?s)<rule id=\"rule4\">.*?</rule>", "");
        assertThrows(IllegalStateException.class, () -> deploy(noMatch).evaluate(ready));
        var rule = xml.substring(xml.indexOf("<rule id=\"rule4\">"), xml.indexOf("</rule>", xml.indexOf("<rule id=\"rule4\">")) + 7);
        var duplicate = xml.replace("</decisionTable>", rule.replace("r4", "r9").replace("rule4", "rule9") + "</decisionTable>");
        assertThrows(IllegalStateException.class, () -> deploy(duplicate).evaluate(ready));
        assertThrows(IllegalStateException.class, () -> deploy(xml.replace("'TO_OPERATOR'", "'APPROVED'")).evaluate(ready));
        assertThrows(NullPointerException.class, () -> qualifier.evaluate(null));
    }
    @Test void R6_newDeploymentDoesNotChangePinnedDecision() {
        var changed = deploy(xml.replace("'TO_OPERATOR'", "'CORRECTION'"));
        var ready = new AssessmentFacts(true,false,false,false);
        assertEquals(Qualification.CORRECTION, changed.evaluate(ready));
        assertEquals(Qualification.TO_OPERATOR, qualifier.evaluate(ready));
    }
    @Test void R6_currentReviewsAndExecutionQualifyWithoutGrantingApproval() {
        var s = snapshot(List.of(review("cap",R2,List.of(),ReviewRecord.Outcome.PASS),
                review("at",T2,List.of(R2),ReviewRecord.Outcome.PASS)),
                List.of(run("execution",T2,C2,TestRunRecord.Outcome.PASS)));
        assertEquals(Qualification.TO_OPERATOR, qualifier.evaluate(Rules.facts(List.of(
                Rules.review(s,R2), Rules.review(s,T2), Rules.testRun(s,T2,C2)))));
        assertEquals(Qualification.MISSING_BASIS, qualifier.evaluate(Rules.facts(List.of())));
        var stale = snapshot(List.of(review("cap",R2,List.of(),ReviewRecord.Outcome.PASS),
                review("at",T2,List.of(R1),ReviewRecord.Outcome.PASS)), s.runs());
        assertEquals(Qualification.REVIEW_REQUIRED, qualifier.evaluate(Rules.facts(List.of(
                Rules.review(stale,R2), Rules.review(stale,T2), Rules.testRun(stale,T2,C2)))));
    }
    @Test void R6_unknownDeploymentCannotFallBackToAnotherDefinition() {
        try (var isolated = EngineSession.openInMemory("missing_" + UUID.randomUUID().toString().replace("-", ""))) {
            isolated.decisions().getDmnRepositoryService().createDeployment().parentDeploymentId("known")
                    .addString("qualification.dmn", xml).deploy();
            assertThrows(IllegalStateException.class, () -> new DmnQualifier(isolated.decisions(), "missing")
                    .evaluate(new AssessmentFacts(true,false,false,false)));
        }
    }

    @Test void R6_removedPinnedDeploymentCannotUseFallback() {
        try (var isolated = EngineSession.openInMemory("removed_" + UUID.randomUUID().toString().replace("-", ""))) {
            var repository = isolated.decisions().getDmnRepositoryService();
            var original = repository.createDeployment().parentDeploymentId("original").addString("qualification.dmn",xml).deploy();
            var pinned = new DmnQualifier(isolated.decisions(),"original");
            repository.createDeployment().parentDeploymentId("other").addString("qualification.dmn",xml).deploy();
            repository.deleteDeployment(original.getId());
            assertThrows(IllegalStateException.class, () -> pinned.evaluate(new AssessmentFacts(true,false,false,false)));
        }
    }
    @Test void R6_reusedParentCannotSilentlyChangePinnedDefinition() {
        try (var isolated = EngineSession.openInMemory("reused_" + UUID.randomUUID().toString().replace("-", ""))) {
            var repository = isolated.decisions().getDmnRepositoryService();
            repository.createDeployment().parentDeploymentId("same").addString("qualification.dmn",xml).deploy();
            var pinned = new DmnQualifier(isolated.decisions(),"same");
            repository.createDeployment().parentDeploymentId("same").addString("qualification.dmn",xml).deploy();
            assertThrows(IllegalStateException.class, () -> new DmnQualifier(isolated.decisions(),"same"));
            assertThrows(IllegalStateException.class, () -> pinned.evaluate(new AssessmentFacts(true,false,false,false)));
        }
    }

}
