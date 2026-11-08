package org.example.processlab.report;

import java.util.*;
import org.example.processlab.domain.ArtifactRef;
import org.example.processlab.rules.CheckStatus;
import org.example.processlab.workflow.ChangeProcess.TaskView;
import org.example.processlab.workflow.ChangeState;
import org.example.processlab.workflow.WorkflowChecks;

/** Read-only educational projection, not a process command or domain assessment. */
public final class OperatorCard {
    private OperatorCard() {}
    public static String render(String id, ChangeState state, List<TaskView> tasks, ChangeState previous) {
        Objects.requireNonNull(id); Objects.requireNonNull(state); Objects.requireNonNull(tasks);
        var current = state.snapshot().current();
        boolean applied = state.proposal().ref().equals(current.get(state.scope().requirementId()));
        var checks = WorkflowChecks.checks(state);
        var out = new StringBuilder("# TextStats — karta pracy\n\n");
        out.append("SYMULACJA EDUKACYJNA. TextStats nie uruchomiono. Oceny i odbiory są fikcyjne.\n\n");
        out.append("Podstawa: sprawa ").append(inline(id)).append(" · stan ").append(state.version()).append(".\n\n");
        out.append("## Teraz\n\n").append(recommendation(state, tasks, checks, applied)).append("\n\n");
        out.append("## Zakres i podstawa pracy\n\n");
        for (var logicalId : List.of(state.scope().requirementId(), state.scope().testId(), state.scope().softwareId())) {
            var ref = current.get(logicalId);
            if (ref == null) {
                out.append("Brak bieżącej referencji: ").append(inline(logicalId)).append("\n\n");
            } else {
                out.append("**").append(label(logicalId, state)).append(" · ").append(reference(ref)).append("**\n\n");
                var artifact = state.snapshot().artifacts().stream().filter(a -> a.ref().equals(ref)).findFirst();
                out.append(quote(artifact.map(a -> a.content()).orElse("Brak treści wskazanej rewizji"))).append("\n\n");
            }
        }
        out.append("## Propozycja i zgoda\n\n");
        if (applied) {
            out.append("Propozycja jest już zastosowana: ").append(reference(state.proposal().ref())).append(".\n\n");
            out.append("Brak aktywnego upoważnienia po zastosowaniu nie oznacza braku wcześniejszej zgody.\n\n");
        } else {
            out.append("Osobna propozycja: ").append(reference(state.proposal().ref())).append("\n\n")
                    .append(quote(state.proposal().content())).append("\n\n");
            out.append(state.authorized() ? "Aktywne upoważnienie do zastosowania propozycji: udzielone w fabule."
                    : "Aktywne upoważnienie do zastosowania propozycji: brak.").append("\n\n");
        }
        out.append("## Co mówią zapisane kontrole\n\n");
        if (!applied) out.append("Te wyniki dotyczą dotychczasowej podstawy; nie oceniają nowej propozycji.\n\n");
        out.append("- Ocena opisu zachowania: ").append(status(checks.get("requirementReview"))).append(".\n")
                .append("- Ocena oczekiwań testu: ").append(status(checks.get("testReview"))).append(".\n")
                .append("- Zapis wyniku testu: ").append(status(checks.get("testExecution"))).append(".\n\n")
                .append("Brak rzeczywistego logu, wyniku programu, danych wykonania i środowiska. "
                        + "Brak potwierdzonej tożsamości recenzenta i opisu metody przeglądu. "
                        + "Powód merytoryczny wymaga analizy treści; raport go nie odgaduje.\n\n");
        out.append("## Odbiór\n\n");
        if (state.acceptance() == null) out.append("Odbiór tej sprawy: brak.\n\n");
        else {
            out.append("Odbiór tej sprawy: zapisany w fabule.\n\n");
            acceptance(out, state.acceptance());
        }
        if (state.previousProcessId() != null) {
            if (previous == null) out.append("Brak odczytu poprzedniej sprawy ")
                    .append(inline(state.previousProcessId())).append("; nie odtwarzamy odbioru z bieżących danych.\n\n");
            else if (previous.acceptance() == null) out.append("Poprzednia sprawa nie zawiera zapisu odbioru.\n\n");
            else {
                out.append("Poprzedni odbiór — sprawa ").append(inline(state.previousProcessId())).append(".\n\n");
                acceptance(out, previous.acceptance());
                out.append("Ten odbiór nie obejmuje nowej propozycji.\n\n");
            }
        }
        out.append("## Zadanie silnika i szczegóły\n\n");
        if (tasks.isEmpty()) out.append("Brak aktywnych zadań w odczycie.\n");
        tasks.stream().sorted(Comparator.comparing(TaskView::id)).forEach(t -> out.append("- ")
                .append(inline(t.name())).append(" · ").append(inline(t.assignee())).append(" · ")
                .append(inline(t.key())).append(" · ID ").append(inline(t.id())).append("\n"));
        out.append("\nRola zadania nie potwierdza tożsamości osoby. Raport nie udziela zgody ani nie wykonuje polecenia.\n\n");
        out.append("### Zachowane zapisy ocen i testów\n\n")
                .append("Poniżej również historia; aktualność i sprzeczności rozliczają kontrole powyżej, nie ostatni PASS.\n\n");
        state.snapshot().reviews().stream().sorted(Comparator.comparing(r -> r.id())).forEach(r -> out.append("- ")
                .append(inline(r.id())).append(" · ").append(reference(r.subject())).append(" · podstawa: ")
                .append(references(r.basis())).append(" · ").append(r.outcome()).append(" · ")
                .append(inline(r.rationale())).append("\n"));
        state.snapshot().runs().stream().sorted(Comparator.comparing(r -> r.id())).forEach(r -> out.append("- ")
                .append(inline(r.id())).append(" · ").append(reference(r.testCase())).append(" / ")
                .append(reference(r.software())).append(" · fikcyjny ").append(r.outcome()).append("\n"));
        out.append("\n### Polecenia w historii\n\n");
        state.receipts().stream().sorted(Comparator.comparingLong(ChangeState.Receipt::baseVersion)).forEach(r -> out.append("- v")
                .append(r.baseVersion() + 1).append(" · ").append(inline(r.commandId())).append(" · ")
                .append(r.role()).append(" · ").append(inline(r.action())).append(" · ").append(inline(r.reason())).append("\n"));
        return out.toString();
    }

    private static String recommendation(ChangeState state, List<TaskView> tasks, Map<String, CheckStatus> checks, boolean applied) {
        String prefix = "Rekomendacja doradcza, nie decyzja ani wynik analizy domenowej.\n\n";
        if (tasks.size() > 1) return prefix + "Kilka aktywnych zadań — sprawdź ich zakres; raport nie wybiera jednego za operatora.";
        if (tasks.isEmpty()) return prefix + (state.acceptance() != null
                ? "Sprawa odebrana w fabule. Od operatora teraz: nic."
                : "Brak aktywnego zadania i brak odbioru. Nie oznacza to przyjęcia wyniku; sprawdź historię.");
        return prefix + switch (tasks.get(0).key()) {
            case "authorize" -> "Silnik oczekuje zgody operatora na propozycję. Agent: przygotuj analizę przed decyzją poza workflow; "
                    + "ta analiza nie jest zadaniem zapisanym w F5. Od operatora teraz: rekomendujemy odłożyć decyzję "
                    + "o wykonaniu do otrzymania uzasadnienia; silnik nadal oczekuje.";
            case "prepare" -> (checks.get("testReview") == CheckStatus.CORRECTION
                    && checks.get("testExecution") == CheckStatus.PASSED
                    ? "Ocena oczekiwań testu wymaga korekty; pozytywny zapis wykonania nie usuwa zastrzeżenia.\n\n" : "")
                    + "Agent: przygotuj poprawkę w dotychczasowym zakresie i nowe oceny. "
                    + "Od operatora teraz: nic, o ile poprawka nie zmienia zakresu ani przyjętego ryzyka.";
            case "accept" -> applied && checks.values().stream().allMatch(s -> s == CheckStatus.PASSED)
                    ? "### Rekomendacja agenta\n\n"
                        + "**Rekomendacja: przyjmij wynik wyłącznie w ćwiczeniu.**\n\n"
                        + "### Co możesz teraz napisać\n\n"
                        + "Jeśli się zgadzasz, możesz napisać:\n\n> Przyjmuję wynik w ćwiczeniu.\n\n"
                        + "**Dlaczego:** trzy bieżące kontrole mają pozytywne zapisy dla wskazanych wersji; "
                        + "czekamy już na odbiór. Operator: oceń podstawę poniżej.\n\n"
                        + "**Jeśli masz zastrzeżenie:** napisz je zamiast przyjmować wynik; odbiór pozostanie otwarty.\n\n"
                        + "To decyzja w symulacji, nie potwierdzenie działania produktu. Raport nie zapisuje decyzji w silniku."
                    : "Niespójność: zadanie odbioru nie ma aktualnej pozytywnej podstawy albo propozycja nie jest zastosowana. "
                        + "Agent: wyjaśnij rozbieżność; raport nie rekomenduje odbioru.";
            case "impact" -> "Agent: oceń wpływ w granicach upoważnienia; sama lista zależności nie wystarcza do oceny znaczenia.";
            case "assess" -> "Agent: uzupełnij aktualne oceny lub wyjaśnij ich sprzeczności. Od operatora teraz: brak rekomendacji odbioru.";
            default -> "Nieznany rodzaj zadania; brak rekomendacji. Sprawdź szczegóły silnika.";
        };
    }

    private static String status(CheckStatus status) {
        return switch (status) {
            case PASSED -> "pozytywne zapisy dla tej podstawy";
            case CORRECTION -> "wymaga korekty";
            case CONFLICT -> "sprzeczne wyniki";
            case REVIEW_REQUIRED -> "potrzebna aktualna ocena";
            case UNKNOWN -> "brak wystarczającej podstawy";
        };
    }
    private static String label(String id, ChangeState state) {
        if (id.equals(state.scope().requirementId())) return "Opis zachowania";
        if (id.equals(state.scope().testId())) return "Przypadek testowy";
        return "Opis wersji programu";
    }
    private static void acceptance(StringBuilder out, ChangeState.Acceptance acceptance) {
        out.append("Podstawa odbioru: ").append(references(acceptance.basis().values()))
                .append(" · stan ").append(acceptance.stateVersion()).append(" · polecenie ")
                .append(inline(acceptance.commandId())).append(".\n\n").append(quote(acceptance.reason())).append("\n\n");
    }
    private static String references(Collection<ArtifactRef> refs) {
        return refs.isEmpty() ? "brak" : refs.stream().sorted(Comparator.comparing(ArtifactRef::id)
                .thenComparingInt(ArtifactRef::revision)).map(OperatorCard::reference).reduce((a,b) -> a + ", " + b).orElseThrow();
    }
    private static String reference(ArtifactRef ref) { return inline(ref.id()) + "@" + ref.revision(); }
    private static String inline(String text) {
        if (text == null) return "nieprzypisane";
        return text.replaceAll("[\\r\\n]+", " ").replace("&", "&amp;").replace("<", "&lt;")
                .replace(">", "&gt;").replace("\\", "\\\\").replace("*", "\\*").replace("_", "\\_")
                .replace("[", "\\[").replace("]", "\\]").replace("`", "\\`");
    }
    private static String quote(String text) { return "> " + inline(text); }
}
