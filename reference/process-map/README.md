# Mapa procesu operator–agenci

2026-10-25 · D-82 · materiał objaśniający, nie nowa instrukcja procesu.

## Wybierz materiał

Bieżącą pracę prowadzi [punkt wznowienia](../process-modeling/brief.md#punkt-wznowienia) i wskazany w nim plan. Ten indeks służy nauce oraz odnajdywaniu konkretnych rezultatów.

| Potrzeba | Materiał i granica |
| --- | --- |
| Uporządkować pojęcia i kontekst | [Co jest czym: proces, produkt, zadanie, karta i ślad](concepts-and-context.md); słownik, diagramy, źródła i rejestry — analiza bez zmiany reguł |
| Zobaczyć role, produkty i kontrole | [Przewodnik z trzema widokami](index.html); datowana mapa ustaleń, nie stan wykonania projektu |
| Zrozumieć relację ISO i Scrum | [Objaśnienie i diagramy](iso-and-scrum.md) |
| Poznać mechanizację Flowable | [Instrukcja eksperymentu](flowable-trial/README.md), [diagramy architektury](flowable-trial/architecture.md), [wynik F5](flowable-trial/f5-report.md); ograniczona próba techniczna |
| Obejrzeć kartę operatora | [Gotowa karta przykładowego odbioru](flowable-trial/evidence/operator-card/07-show.md), [mapa pól](operator-preview/textstats-card-data-map.md), [dowody generatora](flowable-trial/evidence/operator-card/README.md); odczyt archiwalny, nie żywy stan ani decyzja użytkownika |

Poniższy plan i rejestr dokumentują powstawanie mapy od 2026-10-25. Kolejność lektury nie jest kolejnością zleconych działań. Szersza [mapa repozytorium](../repository-audit/README.md) rozdziela pozostałe cele.

## Cel i zakres

Zobaczyć odpowiedzialności, produkty pracy, kontekst oraz granice istniejących kontroli. To mapa obecnych ustaleń i narzędzi, nie deklaracja, że cały przebieg został wdrożony w Kitchen. Nie jest raportem wykonania projektu ani odbiorem.

## Plan wykonania

1. Powiązać kroki i kontrole z istniejącymi źródłami.
2. Narysować przebieg w torach odpowiedzialności, zależności produktów oraz kontrole i luki.
3. Dodać dwa przejścia dydaktyczne: z przeglądem i z pominięciem przeglądu; wskazać skutki zmiany po przeglądzie.
4. Wygenerować SVG/PNG, obejrzeć obrazy i sprawdzić odnośniki. Zapisać wynik i punkt wznowienia.

## Decyzje agenta

- 2026-10-25: statyczny przewodnik HTML z lokalnymi obrazami SVG, tekstową alternatywą i źródłami; działa bez serwera, JavaScriptu i sieci. Powód: użytkownik ma oglądać mapę bez utrzymania aplikacji i utraty stanu serwera.
- 2026-10-25: diagramy w DOT, generowane istniejącym Graphviz do SVG i PNG. Powód: jeden edytowalny opis dla obu formatów, bez nowej zależności; PNG służy również kontroli czytelności.
- 2026-10-25: trzy widoki i stałe oznaczenia M/I/L/P. Powód: oddzielić narzędzie od instrukcji i brak od propozycji, bez kolorowania całego etapu jako „gotowy”.

## Punkt wejścia

[Otwórz przewodnik — index.html](index.html). Zacznij od widoku 1, potem przejdź do dwóch historii na końcu. Każdy diagram otwiera się osobno do powiększenia.

- [1. Przebieg i odpowiedzialności](flow.svg)
- [2. Produkty i kontekst](context.svg)
- [3. Kontrole i luki](controls.svg)
- [4. Statyczny model encji — Mermaid](static-model.md) — trzy widoki pojęciowe; wymaga podglądu Markdown z Mermaid, nie jest schematem wdrożonych narzędzi.
- [5. Jeden przykład: ISO → model → wykonywalna reguła](worked-transition.md) — przegląd przygotowanego wydania, istniejące W02 i proponowane połączenie z rzeczywistym raportem.
- [6. Prześledzenie i osobna recenzja przykładu](transition-review.md) — warunki, kontrprzykłady, siedem wykonanych prób modelu i rozliczenie uwag recenzenta.
- [7. Kontrakt odbioru przyrostu przez API](acceptance-contract.md) — propozycja granicy operator–wykonawca–system, operacje, niezmienniki i scenariusze; bez implementacji. [Przebieg recenzji](acceptance-contract-review.md).
- [8. Porównanie z kontraktem iso-model-state](api-contract-comparison.md) — wspólne założenia, różne przedmioty odbioru i przypadek nowego negatywnego wyniku przed decyzją.
- [9. Sprawdzenie karty zmiany wymagania](change-card-check.md) — rzeczywisty przypadek TST-02, powtórzenie RED/GREEN, ograniczenia dowodów i minimalne doprecyzowania karty.
- [10. Karta pracy nad wykonywalnym modelem procesu](../process-modeling/work-card.md) — mandat multieksperta, [brief](../process-modeling/brief.md) i [kryteria odbioru](../process-modeling/acceptance.md); propozycja oparta na istniejącym `iso-model-state`, bez rozpoczęcia implementacji.
- [11. Pełny cykl wydań](../process-modeling/release-cycle.md) — kontrakty W01–W07, zmiana po odbiorze, odmowy i powroty; [plan](../process-modeling/release-cycle-plan.md) oraz [wynik prób i osobnej recenzji](../process-modeling/release-cycle-report.md). Mapowanie istniejących reguł, nie dowód zakończenia całego E3.

Źródła diagramów: `flow.dot`, `context.dot`, `controls.dot`. Odtworzenie wszystkich obrazów: `python3 reference/process-map/render.py` z korzenia repozytorium (wymaga istniejącego polecenia `dot`). Skrypt nadpisuje wyłącznie odpowiadające im SVG/PNG w tym folderze. Nie odczytuje stanu projektu ani nie wykonuje pokazanych bramek.

## Źródła i granice

| Klucz | Źródło | Co z niego pokazujemy |
| --- | --- | --- |
| S1 | [AGENTS procesu](../../template/process/AGENTS.md), P-03–P-08 i „Role i sesje” | Powiązania, instrukcje, zakres kontroli |
| S2 | [Role](../../template/process/roles/README.md), „Teraz”/„Odłożone”; [karta weryfikatora](../../template/process/roles/verifier.md) | Recenzent, zakaz poprawiania ocenianego produktu, Q-04–Q-06 |
| S3 | [Schemat](../../template/process/tools/id.toml), [trace.py](../../template/process/tools/trace.py), [hook](../../template/process/hooks/pre-commit) | Struktura, ślad, ostrzegawczy W5 i migawka indeksu |
| S4 | [E9](../../template/process/tools/check_separation.py), [raport testów](../../template/process/tools/test_report.py), [postęp](../../template/process/tools/progress.py) | Zakres mechanicznej oceny, odrębne polecenia |
| S5 | [Minimalny proces Kitchen](../KITCHEN-MINIMAL-PROCESS.md), D-81 | Kierunek pilota; nie działające bramki w Kitchen |
| S6 | [Role i kontekst](../OPERATOR-AGENT-ROLES-AND-CONTEXT.md), §1–11 | Mandat, kontekst, luki i propozycje; korekta interpretacji niezależności |
| S7 | [RKD AGENTS](../../../rkd/AGENTS.md), §1–4; [wymagania](../../../rkd/RKD-wymagania.md) | Źródła produktu i wzorce; nie nadpisujemy ich nową specyfikacją |
| S8 | [Stan iso-model-state](../../../iso-model-state/docs/STAN.md) | Model i wykonawca sztucznych instancji, nie adapter całego rzeczywistego procesu |
| S9 | [Postęp symulatora](../process-simulator/progress.md) | Lekcja edukacyjna, granice i incydent utraty stanu |

Karty szablonu opisują rozdział autora i recenzenta mocniej niż uwaga 2 przy SI.O7; dokładne rozróżnienie jest w S6 §10. Mapa pokazuje naszą politykę projektu, nie przypisuje jej wprost normie. Reguły commitowania/pushu z innych repozytoriów nie przenoszą uprawnień do tej sesji.

## Rejestr wykonania

2026-10-25: wszystkie cztery kroki planu zakończone. Powstały trzy diagramy DOT/SVG/PNG i lokalny przewodnik HTML. Obejrzano trzy obrazy, dodano połączenie przekazania kryteriów do przeglądu. Przewodnik zawiera dwa przejścia dydaktyczne oraz zmianę po przeglądzie. Te opisy są analizą reguł, nie nowymi przebiegami wykonawcy procesu.

Sprawdzenie przeglądarkowe: Chrome headless z osobnym tymczasowym profilem, dokument lokalny `file:`, bez serwera. Wszystkie trzy SVG załadowane; brak przepełnienia strony przy 1440 px i 390 px; sekcje szczegółów otwierają się. Na wąskim ekranie diagram przewija się we własnym obszarze. Obejrzano [zrzut desktop](preview-desktop.png) i [zrzut telefonu](preview-mobile.png). Zapis techniczny: [visual-check.txt](visual-check.txt). Przegląd wyglądu wykonany przez autora, nie niezależnego recenzenta.

Sprawdzono lokalne odnośniki HTML i README oraz składnię XML trzech SVG. Parser XML w Homebrew Python 3.14 napotkał problem symbolu biblioteki systemowej expat; tę kontrolę powtórzono poprawnie przez istniejący `/usr/bin/python3`, bez zmiany środowiska. `make check`: 248 elementów, 0 błędów, 4 ostrzeżenia (MIG-01/MIG-02 bez AT, D-81/D-82 bez wzmianki w commicie). `git diff --check`: bez błędów. To kontrole materiału dokumentacyjnego; nie ponawiano testów niezmienionego kodu szablonu lub symulatora.

Nie zmieniono mechanizmów procesu ani zewnętrznych repozytoriów. Nie utworzono commita ani pusha. Otwarte po stronie agenta: poprowadzić czytanie mapy od widoku 1 i uwzględnić obserwacje w przygotowaniu pilota. Użytkownik ocenia czytelność; nie zapisano jej jako potwierdzonej. Dalszy kierunek D-81 zachowany: rozpoznanie istniejącego produktu przed wyborem przyrostu.

2026-10-26: po zleceniu „wejdz w role i wykonaj” przeprowadzono analizę przykładu W02 i osobną recenzję kontrprzykładów. [Raport](transition-review.md) zawiera plan, tabelę kontroli, decyzje agenta i punkt wznowienia. Recenzent pracował bez historii rozmowy i bez analizy autora. Cztery uwagi rozliczono, przykład doprecyzowano; pierwotna treść i odpowiedź recenzenta zachowane jako dowody. Siedem prób rzeczywistego wykonawcy modelu uruchomiono na kopii: potwierdziły m.in. brak wymogu raportu W02, brak ponownego sprawdzenia nowej blokady oraz działające W03. To nie implementacja adaptera ani pełna regresja modelu. Nie zmienia to zakresu D-81/D-82, nie wdraża nowych reguł ani nie zatwierdza wydania.
