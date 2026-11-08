package org.example.processlab;

import java.nio.file.*;
import java.util.*;
import org.example.processlab.domain.*;
import org.example.processlab.report.OperatorCard;
import org.example.processlab.rules.*;
import org.example.processlab.workflow.*;
import org.example.processlab.workflow.ChangeProcess.TaskView;
import org.junit.jupiter.api.Test;
import tools.jackson.databind.json.JsonMapper;
import static org.junit.jupiter.api.Assertions.*;

class OperatorCardTest {
    static final JsonMapper JSON = JsonMapper.builder().build();
    record Sample(String id, ChangeState state, List<TaskView> tasks, ChangeState previous) {
        String render() { return OperatorCard.render(id, state, tasks, previous); }
        Sample with(ProjectSnapshot snapshot) {
            return new Sample(id, new ChangeState(state.version(), state.scope(), snapshot, state.proposal(),
                    state.authorized(), state.previousProcessId(), state.receipts(), state.acceptance()), tasks, previous);
        }
    }
    static Sample sample(String name, String key) throws Exception {
        var cases = JSON.readTree(Files.readString(Path.of("evidence/f5-restart/" + name + ".json"))).get("cases");
        var node = cases.get(key);
        var state = StateCodec.decode(node.get("state").toString());
        List<TaskView> tasks = new ArrayList<>();
        for (var task : node.get("tasks")) tasks.add(JSON.treeToValue(task, TaskView.class));
        ChangeState previous = null;
        for (var other : cases) if (other.get("id").asText().equals(state.previousProcessId()))
            previous = StateCodec.decode(other.get("state").toString());
        return new Sample(node.get("id").asText(), state, tasks, previous);
    }
    @Test void failedReviewIsNotHiddenByPassingRun() throws Exception {
        var text = sample("05-fail", "first").render();
        assertAll(() -> assertTrue(text.contains("Ocena oczekiwań testu: wymaga korekty")),
                () -> assertTrue(text.contains("Zapis wyniku testu: pozytywne zapisy")),
                () -> assertTrue(text.contains("Agent: przygotuj poprawkę")),
                () -> assertTrue(text.contains("pozytywny zapis wykonania nie usuwa zastrzeżenia")),
                () -> assertTrue(text.contains("Od operatora teraz: nic")),
                () -> assertTrue(text.contains("Ocena testu w fabule")),
                () -> assertTrue(text.contains("TextStats nie uruchomiono")));
    }
    @Test void currentBasisWaitsForAcceptanceAndOldFailureRemainsHistory() throws Exception {
        var text = sample("07-show", "first").render();
        int details = text.indexOf("## Zakres i podstawa pracy");
        assertTrue(details >= 0, "Report must contain the basis section before inspecting its opening");
        var opening = text.substring(0, details);
        assertTrue(opening.contains("### Rekomendacja agenta"));
        assertTrue(opening.contains("> Przyjmuję wynik w ćwiczeniu."));
        assertTrue(opening.contains("Jeśli się zgadzasz, możesz napisać"));
        assertAll(() -> assertTrue(text.contains("Odbiór tej sprawy: brak")),
                () -> assertTrue(text.contains("Operator: oceń podstawę")),
                () -> assertTrue(text.contains("Rekomendacja: przyjmij wynik wyłącznie w ćwiczeniu")),
                () -> assertTrue(text.contains("CAP-01@2")), () -> assertTrue(text.contains("AT-01@3")),
                () -> assertTrue(text.contains("CODE-01@3")), () -> assertTrue(text.contains("failed-test")),
                () -> assertTrue(text.contains("FAIL")), () -> assertTrue(text.contains("stan 6")),
                () -> assertTrue(text.contains("7521")));
    }
    @Test void nextProposalDoesNotInheritAcceptanceOrChecks() throws Exception {
        var text = sample("10-show", "next").render();
        assertAll(() -> assertTrue(text.contains("Poprzedni odbiór — sprawa 7")),
                () -> assertTrue(text.contains("CAP-01@2")), () -> assertTrue(text.contains("CAP-01@3")),
                () -> assertTrue(text.contains("nie oceniają nowej propozycji")),
                () -> assertTrue(text.contains("OPERATOR")),
                () -> assertTrue(text.contains("analizę przed decyzją poza workflow")),
                () -> assertTrue(text.contains("nie jest zadaniem zapisanym w F5")),
                () -> assertTrue(text.contains("Odbiór tej sprawy: brak")));
    }
    @Test void consumedAuthorizationIsNotDescribedAsMissingHistoricalConsent() throws Exception {
        var text = sample("07-show", "first").render();
        assertTrue(text.contains("Propozycja jest już zastosowana"));
        assertTrue(text.contains("nie oznacza braku wcześniejszej zgody"));
    }
    @Test void missingPreviousCaseIsExplicit() throws Exception {
        var sample = sample("10-show", "next");
        var text = OperatorCard.render(sample.id(), sample.state(), sample.tasks(), null);
        assertTrue(text.contains("Brak odczytu poprzedniej sprawy 7"));
        assertFalse(text.contains("Poprzedni odbiór — sprawa 7"));
    }
    @Test void conflictingResultsCannotRecommendAcceptance() throws Exception {
        var sample = sample("07-show", "first"); var p = sample.state().snapshot();
        var text = sample.with(p.append(new ReviewRecord("extra-fail", p.current().get("AT-01"),
                List.of(p.current().get("CAP-01")), ReviewRecord.Outcome.FAIL, "Zastrzeżenie"))).render();
        assertTrue(text.contains("Ocena oczekiwań testu: sprzeczne wyniki"));
        assertTrue(text.contains("Niespójność: zadanie odbioru"));
        assertFalse(text.contains("Operator: oceń podstawę"));
    }
    @Test void missingCurrentArtifactIsUnknownNotPassed() throws Exception {
        var sample = sample("07-show", "first"); var p = sample.state().snapshot();
        var current = new HashMap<>(p.current()); current.remove("AT-01");
        var text = sample.with(new ProjectSnapshot(p.artifacts(), current, p.dependencies(), p.reviews(), p.runs())).render();
        assertTrue(text.contains("Ocena oczekiwań testu: brak wystarczającej podstawy"));
        assertTrue(text.contains("Brak bieżącej referencji: AT-01"));
        assertFalse(text.contains("Operator: oceń podstawę"));
    }
    @Test void staleDependencyNeedsNewReviewEvenWithPassRecorded() throws Exception {
        var sample = sample("07-show", "first"); var p = sample.state().snapshot();
        var stale = new Dependency(new ArtifactRef("CAP-01", 1), p.current().get("AT-01"), Dependency.Kind.VERIFIES);
        var text = sample.with(new ProjectSnapshot(p.artifacts(), p.current(), List.of(stale), p.reviews(), p.runs())).render();
        assertTrue(text.contains("Ocena oczekiwań testu: potrzebna aktualna ocena"));
        assertFalse(text.contains("Operator: oceń podstawę"));
    }
    @Test void acceptedCaseKeepsExactBasisWithoutRequestingAnotherAcceptance() throws Exception {
        var text = sample("10-show", "first").render();
        assertTrue(text.contains("Odbiór tej sprawy: zapisany w fabule"));
        assertTrue(text.contains("CAP-01@2"));
        assertTrue(text.contains("Od operatora teraz: nic"));
        assertFalse(text.contains("Operator: oceń podstawę"));
    }
    @Test void repeatedRenderingDoesNotChangeStateOrInput() throws Exception {
        var file = Path.of("evidence/f5-restart/07-show.json"); var bytes = Files.readAllBytes(file);
        var sample = sample("07-show", "first"); var state = StateCodec.encode(sample.state());
        var first = sample.render();
        assertFalse(first.isBlank());
        assertEquals(first, sample.render());
        assertEquals(state, StateCodec.encode(sample.state()));
        assertArrayEquals(bytes, Files.readAllBytes(file));
    }
}
