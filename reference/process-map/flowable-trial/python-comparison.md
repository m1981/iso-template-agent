# Flowable i PY-01: dane, funkcje i testy

2026-11-08 · A-17 · analiza dwóch istniejących implementacji, nie specyfikacja nowego produktu ani decyzja o migracji.

## Wniosek

**To dwa częściowo pokrywające się prototypy, a nie dwa wykonania tego samego kontraktu.** Flowable ma szerszą obsługę drogi do odbioru i następującej po nim sprawy. PY-01 ma węższą dziedzinę, ale bardziej dopracowany kontrakt ponawiania komend, wybrane współbieżne zapisy i obsługę błędów CLI. W obu większość znaczenia procesu zapisaliśmy sami.

Flowable wnosi silnik zadań, przejść, historii i tabel decyzji. Nie dostarczył nam gotowego modelu produktów pracy, śladu, aktualności ani niezależności recenzji. Trwałość występuje w obu rozwiązaniach. Żadne nie jest obecnie kompletnym systemem prowadzenia projektu Kitchen.

## 1. Przedmiot, metoda i granice

| Przedmiot | Badana wersja | Co włączono |
| --- | --- | --- |
| Próba Flowable F1–F5 i późniejsza karta | iso-template-agent `6845f799a57cdb2269879995c0b7bb92be9434fa` | `src/main`, BPMN/DMN, osiem klas testowych, konfiguracja, historyczne eksporty używane jako dane testów karty |
| PY-01 | iso-model-state `f74f55f2ea68d30fca22b4ddf7c9d05eb9ad82cb`, czysty katalog roboczy przy odczycie | `src/isowork`, cztery moduły `test_py01_*`, konfiguracja uruchomienia |

Odczytano implementacje i treść asercji, nie tylko nazwy testów. Regresje uruchomiono z kopii tych commitów; wyniki i odtwarzacz w §5. Nie zmieniano implementacji ani drugiego repozytorium. Testy nie uruchamiają rzeczywistego TextStats, eksportu CSV ani CNC: wyniki produktu wewnątrz opowieści są fikcyjnymi danymi, podczas gdy testy mechanizmów procesu wykonują się naprawdę.

**Nie włączono do zakresu PY-01** modelu `isomodel`/`process.yaml`, WIT1–WIT5, badań TLC ani lekcji L1 z tego repo. Mają osobne funkcje i dowody. Nie przypisujemy PY-01 ich możliwości. Także potencjalne funkcje biblioteki Flowable, których nie używa próba, nie są funkcjami naszej aplikacji.

Oznaczenia w tabelach: **jest** — realizacja w badanym kodzie; **część** — realizacja ograniczona podanym warunkiem; **brak** — nie znaleziono realizacji w zdefiniowanym zakresie. Brak funkcji spoza zamiaru prototypu nie oznacza defektu.

## 2. Struktury danych

| Informacja | Flowable + nasz kod Java | PY-01 + nasz kod Python | Znaczenie różnicy |
| --- | --- | --- | --- |
| Produkt i rewizja | `ArtifactRef(id, revision)`; `ArtifactRevision(ref, kind, content)`; typy REQUIREMENT, TEST_CASE, SOFTWARE | Słownik `artifacts`, zamknięte klucze R, TA, TB; `current` i lista `versions(version, content)` | Java: dowolne ID w strukturze, ale workflow ograniczony do jednej trójki wymaganie/test/program. Python: jedno wymaganie i dwa testy, brak programu |
| Bieżąca podstawa | `ProjectSnapshot.current`: ID → dokładna referencja; osobna lista wszystkich rewizji | Numer `current`, wersje 1…n; bieżąca treść z ostatniej wersji | Java nie wybiera automatycznie najwyższej rewizji przy dowolnym imporcie. W komendach wymaga numeru większego od wszystkich zapisanych, niekoniecznie +1. Python dodaje dokładnie +1 |
| Zależność | Jawna `Dependency(basis, dependent, kind)` dla DERIVED_FROM i VERIFIES | Powiązania TA→R i TB→R zakodowane w regułach; nie ma kolekcji dowolnych krawędzi | Java może badać graf w czystych funkcjach. Python rozlicza tylko dwie ustalone relacje |
| Przegląd | `ReviewRecord(id, subject, basis[], outcome, rationale)`; PASS/FAIL | Ocena pary test/wymaganie: obie wersje, valid/invalid, reason, actor, role | Java ocenia produkt na zbiorze podstaw. Python ocenia relację dwóch wersji. Nie są to te same rekordy |
| Wykonanie testu | `TestRunRecord(id, testCase, software, outcome)`; PASS/FAIL/ERROR | `check_runs(id, test, test_version, requirement_version, result, evidence)` | Java wiąże wynik z wersją programu. Python nie ma programu; `check_runs` są zachowywanym przykładem, bez komendy dopisania nowego wykonania |
| Propozycja i zgoda | W `ChangeState`: jedna bieżąca `proposal`, `authorized`, historia receipts i danych silnika | Słownik wielu propozycji; każda ma treść, cel, wersję bazową, SHA-256, autora, jednorazową decyzję i `applied` | Python utrzymuje propozycje jako osobne obiekty z ich cyklem; Java steruje jedną propozycją w instancji BPMN |
| Zadanie / faza | Rzeczywiste instancje zadań BPMN z taskId, kluczem, assignee i historią | Brak encji zadania; `owner` i `next_action` wylicza `build_view` | W Pythonie rekomendacja nie jest utrwalonym zadaniem do zakończenia |
| Odbiór i kolejna sprawa | `Acceptance(commandId, stateVersion, basis, reason)` oraz `previousProcessId` | Brak odbioru i łańcucha odebranych spraw | `review_complete=True` w PY-01 nie jest odpowiednikiem odbioru |
| Wykonawca | Role AGENT/OPERATOR w kopercie; receipt zapisuje rolę, nie osobę; przegląd nie ma autora | `Actor(role, subject)` z A/U/R; autor propozycji i oceny w stanie | Więcej danych o autorze w Pythonie nie daje uwierzytelnienia ani niezależności |
| Utrwalenie | Cały własny `ChangeState` jako JSON w zmiennej `caseState`; zadania, historia BPMN/DMN w tabelach silnika; H2 plikowe | SQLite: jeden wiersz stanu z JSON i rewizją + tabela `receipts(command_id, request_digest, result)` | Oba używają agregatu JSON. Java nie zamienia naszych artefaktów automatycznie w encje ALM zarządzane przez silnik |

Źródła Java: [domain/](src/main/java/org/example/processlab/domain/), [ProjectSnapshot](src/main/java/org/example/processlab/rules/ProjectSnapshot.java), [ChangeState](src/main/java/org/example/processlab/workflow/ChangeState.java), [StateCodec](src/main/java/org/example/processlab/workflow/StateCodec.java). Python: [core.py](../../../../iso-model-state/src/isowork/core.py), [store.py](../../../../iso-model-state/src/isowork/store.py).

## 3. Funkcje, które można rzeczywiście wywołać

| Zachowanie | Flowable — realizacja | PY-01 — realizacja | Sprawdzenie w istniejących testach |
| --- | --- | --- | --- |
| Propozycja → decyzja → zastosowanie | **Jest:** `Propose`, `Authorize`, `ApplyChange`; zmiana propozycji wraca do autoryzacji | **Jest:** `propose`, `decide`, `apply`; decyzja wiąże digest konkretnej propozycji | Java F4_01, F4_04; Python exact_proposal, no_implicit_approval, wrong_digest, old_approval |
| Kto stosuje zatwierdzoną zmianę | **AGENT**, po zgodzie OPERATOR | **U**, także po wcześniejszej zgodzie U; A/R nie mogą stosować | To sprzeczne kontrakty delegowania, oba celowo testowane. Nie można bez uzgodnienia podmienić jednego API drugim |
| Kolejność i oczekiwanie na człowieka | **Jest:** BPMN, 5 rodzajów user task, pętle poprawy/zmiany, osobna zgoda i odbiór | **Część:** warunki czterech operacji; oczekująca propozycja w danych; brak grafu zadań i odbioru | F4_01–05; testy rules/CLI dotyczące zgody i odmowy |
| Wyznaczenie wpływu zmiany | **Jest:** `Rules.impact`, BFS po ID, ścieżki, ochrona przed cyklem i duplikatami | **Część:** nowe R unieważnia aktualność ocen TA/TB; zmiana testu tylko jego parę | Java R3: diament, cykl, izolowany węzeł, stara rewizja; Python stale_assessment i review_repair |
| Ślad w obu kierunkach | **Część:** jawne krawędzie; `impact` szuka zależnych, `review` znajduje podstawy produktu. Brak kompletnej macierzy pokrycia całego projektu | **Część:** dwie pary pokazują oba końce; brak dowolnego grafu, kontroli osieroconych produktów i ogólnej macierzy | Testy sprawdzają konkretne relacje; nie dowodzą kompletności śladu projektu |
| Aktualność przeglądu | **Jest:** dokładny przedmiot, zbiór podstaw i aktualne krawędzie; stare oceny pozostają historią | **Jest:** dokładna para wersji; brak jej oceny daje suspect; stara ocena odrzucona | Java R4/F4_04; Python stale_assessment, requirement_change_wins_race |
| Poprawa błędnej oceny/testu | **Część:** `Prepare` wymaga nowej rewizji **zarówno testu, jak i programu**; nie sprawdza zmiany treści | **Część:** invalid wymusza zmianę wersji; propozycja z identyczną treścią jest odrzucana; test można zmienić bez zmiany drugiego | Java F4_02; Python review_repair, noop_change, guidance_returns_to_review |
| Dwie sprzeczne oceny tej samej podstawy | **Jest:** oba rekordy zostają, wynik CONFLICT; późniejszy PASS nie przykrywa FAIL | **Inny kontrakt:** tylko jedna ocena pary; druga odrzucona jako assessment_exists/repair_required | Java R4/R5, F4_02; Python repair_required. Brak operacji rozstrzygnięcia błędnej oceny bez zmiany wersji w obu próbach |
| Wynik wykonania a przegląd | **Jest:** osobne dane; kwalifikacja wymaga przeglądu wymagania, testu i wyniku dla test/program | **Część:** osobne dane i komunikat; `review_complete` nie bierze wyniku wykonania pod uwagę | Java R5, R6/F4_02; Python view_reports… oraz full_demo pokazują `review_complete=True` przy zachowanym fail |
| Odbiór konkretnej podstawy | **Jest:** tylko OPERATOR, ponowne sprawdzenie przed przyjęciem, zapis referencji; odmowa wraca do poprawy | **Brak** | Java F4_01/F4_02/F4_04; Python jawnie odrzuca nieznane accept_release |
| Kolejna zmiana po odbiorze | **Jest:** `startNext`, nowa instancja powiązana z poprzednią, bez przepisywania poprzedniego odbioru | **Brak** takiego cyklu; można dalej zmieniać artefakty, ale bez odbiorów | Java F4_05 i F5 restart. To odbiór sprawy w fabule, nie pełny pakiet wydania produktu |
| Powtórzenie udanej komendy | **Jest odmowa:** ID komendy zapisane w receipts; dodatkowo wersja, taskId i processId | **Jest replay:** to samo ID i digest żądania wraz z aktorem zwraca stary wynik, także po wzroście rewizji; inna treść → konflikt | Java F4_03; Python command_persists, command_id_cannot…, concurrent_duplicate |
| Wyjątek w połowie kroku | **Jest:** stan, zakończenie zadania, kontynuacja BPMN i DMN we wspólnej transakcji | **Jest:** stan i receipt w jednej transakcji SQLite | Java F4_06 wstrzykuje wyjątek po kwalifikacji; Python after_state/after_receipt. Ponowienie po rollback działa w obu |
| Dwaj zapisujący jednocześnie | **Nie wykazano:** fasada jawnie sekwencyjna; odczyt i prekontrole są przed `complete` | **Jest dla badanych przeplotów:** BEGIN IMMEDIATE, expected_revision, kontrolowane konkurencyjne komendy | Python trzy testy store: stale change, duplicate, requirement change vs old review. Nie jest to dowód wszystkich przeplotów ani obciążenia |
| Restart procesu OS | **Jest:** H2; zachowane ID zadań, dane i historia w 10 kolejnych JVM | **Jest:** SQLite; kolejne wywołania CLI są odrębnymi procesami | Java PersistentTrialTest; Python pełny scenariusz CLI |
| Zmiana modelu przy wznowieniu | **Część:** odmowa przy innych bajtach BPMN/DMN lub innym zbiorze wdrożeń; nie wykrywa każdej zmiany Java | **Część:** `schema_version=1` i walidacja danych; brak przypięcia wersji reguł Python | Java F5_04; Python uszkodzone dane. W obu brak migracji i dowodu zgodności starego stanu z nową logiką |
| Widok operatora | **Jest:** raport ze stanu/historii; karta Markdown z archiwalnego JSON, jawnie nie na żywo | **Jest:** `status` tekst/JSON; wersje, propozycje, powody, właściciel, następna czynność; odwołuje do istniejącej propozycji naprawy | Java 10 testów karty + 3 eksportu; Python view/guidance/CLI. Testy treści nie dowodzą zrozumiałości |
| Obsługa błędnych poleceń | **Część:** typy i wyjątki Java, fasada; brak porównywalnego ogólnego CLI komend z katalogiem błędów | **Jest:** ścisłe pola, kody błędu, komunikat, następne działanie, kody wyjścia 0/1/2 | Java domena/F4; Python invalid_fields, bad_command, errors_are_machine_readable, corrupt_payload/receipt |

Źródła realizacji: [ChangeCommands](src/main/java/org/example/processlab/workflow/ChangeCommands.java), [ChangeProcess](src/main/java/org/example/processlab/workflow/ChangeProcess.java), [Rules](src/main/java/org/example/processlab/rules/Rules.java), [WorkflowChecks](src/main/java/org/example/processlab/workflow/WorkflowChecks.java), [BPMN](src/main/resources/change.bpmn20.xml), [DMN](src/main/resources/qualification.dmn), [EngineSession](src/main/java/org/example/processlab/engine/EngineSession.java), [ChangeTrial](src/main/java/org/example/processlab/workflow/ChangeTrial.java), Python [core](../../../../iso-model-state/src/isowork/core.py), [store](../../../../iso-model-state/src/isowork/store.py), [CLI](../../../../iso-model-state/src/isowork/__main__.py).

### Konkretny przykład różnicy

Po zmianie wymagania test A nadal pasuje, test B wymaga zmiany:

- **PY-01:** ocena A jako valid, B jako invalid; propozycja zmiany B → decyzja U → zastosowanie przez U → ponowna ocena B. A i stary wynik wykonania pozostają niezmienione. Koniec oznacza rozliczony przegląd dwóch relacji; nie odbiór ani zielone wykonanie testów.
- **Flowable:** jedna sprawa obejmuje jeden wybrany test i program. Po negatywnym przeglądzie wraca do Prepare, które tworzy obie nowe rewizje; następnie zbiera przeglądy i wynik wykonania, kieruje do operatora i zapisuje odbiór. Obsługa kilku testów jako niezależnych prac wymaga rozszerzenia obecnego workflow, mimo że kolekcje danych mogą pomieścić więcej rekordów.

To **różnica funkcjonalna**, nie przewaga wynikająca z języka. W szczególności nie należy z liczby typów Java wywodzić, że gotowy workflow obsługuje dowolny graf projektu.

## 4. Czego nie ma w obu rozwiązaniach

| Potrzeba | Stan badanych implementacji | Co już istnieje, ale nie wystarcza |
| --- | --- | --- |
| Uwierzytelnione polecenia operatora i ograniczenie niezaufanego agenta | Brak; role są wejściem lokalnej symulacji | Sprawdzenie enum/napisu roli nie potwierdza osoby. Dostęp do bazy/silnika omija fasadę. Nie rozszerzamy teraz modelu zagrożeń |
| Niezależny recenzent | Brak wymuszonego rozdzielenia autora i recenzenta | PY ma rolę R, lecz A także ocenia i nie ma kontroli autor ≠ recenzent. Java ma tylko AGENT/OPERATOR, a ReviewRecord nie ma autora. Osobne historyczne recenzje kodu nie dodają tej funkcji do programu |
| Rzeczywisty dowód testu produktu | Brak runnera, integracji CI i powiązania z rzeczywistym kodem/budową | Rekord PASS jest przyjmowany jako dane. Java wiąże symboliczne rewizje test/program; PY zachowuje syntetyczny run. Żaden nie dowodzi, że uruchomiono dany program |
| Cały projekt: potrzeby, zakres, plan, ryzyka, pytania, moduły i wydania | Brak kompletnego modelu i operacji | Tylko wybrany przekrój zmiany. Nie ma gotowego cyklu feature → wiele zadań → integracja → wydanie Kitchen |
| REST i gotowe aplikacje platformy | Brak wdrożonego API HTTP i gotowych UI Flowable | Java używa embedded BPMN/DMN; nie aktywowano CMMN, Modeler, Task, Admin, IDM; Python udostępnia lokalne CLI |
| Utrzymanie produkcyjne | Brak dowodów backup/restore, migracji, awarii dysku/zasilania, skalowania | Test nowego procesu OS i rollback wyjątku nie są testem wszystkich awarii trwałego magazynu |
| Pełna identyfikowalność i kompletność wymagań | Brak dowodu pełnego pokrycia potrzeb lub wszystkich przebiegów | Ścieżki grafu i 16 kombinacji faktów DMN nie dowodzą poprawności domeny ani kompletności procesu |

Ograniczenie dodatkowe z odczytu kodu: `store.validate_state` sprawdza format `check_runs`, ale nie istnienie wskazanych wersji; Java `requireKnownEvidence` sprawdza istnienie referencji importowanych przeglądów/wykonań. W PY-01 nie ma operacji dodawania runs, dlatego zapisujemy to jako granicę walidacji importu/stanu, nie jako wykazany błąd bieżącego przepływu. Nie przeprowadzono nowej próby uszkodzenia tych konkretnych pól.

## 5. Testy i rzeczywiste wykonanie

**Ponowienie 2026-11-08: Flowable 71/71 PASS, PY-01 77/77 PASS; bez błędów i pominiętych testów, oba polecenia zakończone kodem 0.** Python obejmuje trzy pozytywne sprawdzenia wykrycia celowych usterek. Flowable obejmuje test z dziesięcioma odrębnymi JVM. Nie są to 148 testów tego samego kontraktu ani porównanie procentowego pokrycia.

Wynik ponowienia oraz liczby poszczególnych zestawów: [summary.json](evidence/comparison-20261108/summary.json). Pełne logi: [Flowable](evidence/comparison-20261108/flowable.log), [Python](evidence/comparison-20261108/python.log); [JUnit Python](evidence/comparison-20261108/python-junit.xml). Przy zapisie usunięto z logów wyłącznie końcowe spacje/tabulatory w wierszach; odtwarzacz stosuje tę samą normalizację. Pliki `org.example.processlab.*.txt` w tym samym katalogu zawierają wyniki klas Java.

| Warstwa sprawdzenia | Flowable | PY-01 |
| --- | --- | --- |
| Dane i czyste reguły | DomainModelTest, RulesTest: tożsamość, niezmienność kolekcji, graf, aktualność i sprzeczne wyniki | test_py01_rules: propozycje/decyzje, obie wersje relacji, obowiązek naprawy, wyliczanie kolejnego kroku |
| Silnik / magazyn | EngineSessionTest, DmnQualifierTest, ChangeProcessTest: rzeczywiste BPMN/DMN, 16 kombinacji czterech faktów, odmowy i rollback | test_py01_store: rzeczywista SQLite, receipts, rollback, konkurencja, stare rewizje |
| Restart / interfejs | PersistentTrialTest: 10 JVM i ochrona definicji; OperatorCardTest/ExportCardTest: odczyty archiwów | test_py01_cli: odrębne procesy, pełna zmiana/naprawa, status, błędne dane i komunikaty |
| Czułość na usterkę | Obecna regresja obejmuje m.in. wadliwe DMN i uszkodzone wdrożenia. Historyczne osobne kampanie mutacyjne F3–F5 nie były teraz ponawiane | test_py01_sensitivity ponawia 3 mutanty: usunięta kontrola obu wersji, brak receipt, pominięta zatwierdzona propozycja w rekomendacji |

Źródła testów: [Java](src/test/java/org/example/processlab/), Python [rules](../../../../iso-model-state/tests/test_py01_rules.py), [store](../../../../iso-model-state/tests/test_py01_store.py), [CLI](../../../../iso-model-state/tests/test_py01_cli.py), [sensitivity](../../../../iso-model-state/tests/test_py01_sensitivity.py).

**Odtworzenie:** `/usr/bin/python3 reference/process-map/flowable-trial/evidence/comparison-20261108/reproduce.py <katalog-wyników>`. [Skrypt](evidence/comparison-20261108/reproduce.py) pobiera wskazane commity przez lokalny `git archive`, kopiuje istniejący cache Maven, używa już dostępnego JDK i środowiska Python, uruchamia offline `./verify -o verify` oraz tylko cztery moduły PY-01. Nie uruchamia TLC ani całego drugiego projektu. Potrzebne są lokalne repozytoria i istniejące narzędzia; niczego nie instaluje. Wyniki trwale zapisuje w podanym katalogu. Ścieżki robocze `/tmp` w logach wskazują miejsce wykonania; nie są potrzebne do odczytania wyników ani ponowienia z nową kopią.

### Granice dowodu testowego

Zielone wyniki potwierdzają asercje tych zestawów dla tych wersji. Nie porównują kontraktów jeden do jednego, nie mierzą jakości produktu, nie dowodzą wszystkich przeplotów ani wszystkich ścieżek i nie oznaczają odbioru użytkowego. `test_py01_sensitivity` jest testem, że wybrane zepsute kopie są wykrywane; ich oczekiwane niepowodzenie nie jest niepowodzeniem regresji.

W Flowable testy karty wykorzystują także stałe historyczne pliki JSON. Sam ich PASS nie dowodzi podłączenia karty do bieżącej bazy; karta jawnie pozostaje widokiem archiwalnym. W Pythonie testy CLI potwierdzają obecność treści i wskazówek, nie ich zrozumiałość dla użytkownika.

## 6. Co z tego wynika dla dalszych prac

1. **Zachować oba wyniki eksperymentów bez migracji.** Pokazują różne mechanizmy, a nie rozstrzygnięty wybór technologii. Obecna analiza wystarcza do odrzucenia twierdzenia „Flowable dodał nam wszystko” oraz „Python już robi dokładnie to samo”.
2. **Przed ewentualnym łączeniem uzgodnić mały kontrakt zachowania**, zwłaszcza kto stosuje zmianę, co oznacza ponowienie i kiedy wynik jest gotowy do odbioru. Problemem są wykazane różnice semantyczne; same testy obu aplikacji nie wystarczają. Minimalny koszt: kilka wspólnych przypadków wejście/oczekiwanie, bez nowego modelu całego ISO. Efekt: każda różnica jest celowa albo ma konkretne zadanie. To rekomendacja warunkowa, nie rozpoczęta przebudowa.
3. **Brakujący mechanizm dobierać dopiero do rzeczywistego przekroju Kitchen.** Nie aktywować wszystkich braków z §4 naraz. Obecne syntetyczne dane nie wykazują potrzeb wielomodułowego produktu ani kosztu obsługi przez operatora. Rozpoznanie Kitchen pozostaje osobnym A-12 do zlecenia; funkcja pilota nadal nie została wybrana.

Nie dodano reguł do pakietu procesu ani obowiązków operatora. Właściciel dalszej analizy: agent; wybór zakresu integracji, zmiana delegowania i przyjęcie ryzyka: operator, dopiero gdy taki krok zostanie zlecony.
