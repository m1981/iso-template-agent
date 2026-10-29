# Repozytorium od Day 1 do lokalnego wdrożenia — historia w zdjęciach

Data: 2026-10-23. Rewizja 2: plany i ich chronologia. Materiał dydaktyczny dla operatora i agenta. To samodzielny przykład, a nie aktualizacja działającego pakietu procesu.

## Jak rozumiemy eksperyment

Obserwujesz jeden fikcyjny projekt w kolejnych punktach rozwoju. Każdy dokument jest pełnym zdjęciem plików roboczych repozytorium: drzewo, tabela ścieżek z treścią, powiązanie z normą oraz wskazanie nowych i zmienionych plików. Krótkie dokumenty mają pełną treść w tabelach; pełny kod jest bezpośrednio pod nimi.

Jeden rodzaj treści na plik: wymagania nie zawierają kodu, przypadki testowe nie zawierają wyników, raport testu nie zastępuje decyzji odbiorczej. Powtórzenie niezmienionej treści między zdjęciami jest celowe — nie musisz rekonstruować stanu z kilku rozdziałów.

Pokazujemy plany operacyjne: cel, zakres, kroki, zależności, sposób sprawdzenia, warunki wejścia i zakończenia oraz decyzje. Zachowujemy wcześniejsze wyłączenie harmonogramów, zasobów i kosztów. Migracja nie występuje w tym produkcie, więc nie dokładamy sztucznego planu migracji. Pokazujemy wybrane informacje ISO/IEC 29110 i ich przepływ; **nie deklarujemy pełnego spełnienia Basic**, pełnej treści WP.10 ani wszystkich warunków wejścia z §5.2.

## Kolejność czytania

| Zdjęcie | Co się wydarzyło | Czego uczy |
|---|---|---|
| [00 — Day 1](00_day1.md) | Potrzeba, zakres, pojęcia, wymagania, plan projektu v1 i V&V v1 | Kierunek i sposób oceny powstają przed kodem; przyszłej prośby o wiersze jeszcze nie znamy |
| [00a — plan przyrostu 1](00a_plan_first_increment.md) | Plan I1, projekt, przypadki i środowisko; brak kodu | Szczegółowa kolejność i kryteria poprzedzają RED |
| [01 — przyrost słów, RED](01_increment_words_red.md) | Projekt, przegląd, przypadki i nieprzechodzące testy | Wymaganie, test i wynik są różnymi informacjami |
| [02 — przyrost słów, GREEN](02_increment_words_green.md) | Funkcja, CLI, test integracji, instrukcja i demonstracja w fabule | Jeden przyrost przechodzi przez kilka czynności SDLC; walidacja zaczyna się podczas rozwoju |
| [02a — plan obsługi błędów](02a_plan_input_errors.md) | D3 rozstrzyga Q1; plan E1, projektu v2 i V&V v2 | Nowe wymaganie ma plan, ale jeszcze nie ma implementacji ani dowodu |
| [03 — błędy wejścia](03_increment_input_errors.md) | Decyzja o kontrakcie błędów, RED, poprawka i regresja | Jedna zmiana rozchodzi się przez kilka powiązanych artefaktów |
| [03a — plan drugiego przyrostu](03a_plan_lines_increment.md) | Z1/D4 rozszerza zakres; plan I2, projektu v3 i V&V v3 | Najpierw decyzja i aktualizacja planu, potem nowa funkcja |
| [04 — przyrost wierszy](04_increment_lines.md) | Nowa potrzeba dodaje drugą funkcję | Przyrost produktu nie wymusza rozbudowy procesu |
| [04a — plan wydania](04a_plan_release.md) | W1, V&V v4 i instrukcja próby; bez manifestu i wyniku | Przygotowanie próby nie jest jeszcze dostawą ani odbiorem |
| [05 — lokalne wdrożenie](05_local_deployment.md) | Zestaw dostawy, manifest, próba poza repo i miejsce odbioru | Działanie w repo, działanie dostawy, przydatność i akceptacja są różnymi ocenami |

Nie są to fazy kaskadowe „najpierw wszystkie dokumenty, potem cały kod, na końcu wszystkie testy”. Pierwszy plan jest ogólny; szczegółowy plan kolejnego zakresu powstaje przed jego wykonaniem. Zdjęcia z literą „a” pokazują ten moment. Zachowano nazwy wcześniejszych plików. Oznaczenia N/Z/= zawsze odnoszą się do bezpośrednio poprzedniego zdjęcia w powyższej kolejności.

## Jakie plany, kiedy i co się w nich zmienia

Poniższe ścieżki są plikami hipotetycznego repo wewnątrz zdjęć, a nie dodatkowymi plikami instalowanymi w szablonie. Pełna treść jest w tabelach każdego zdjęcia.

| Plan w repozytorium przykładu | Powstaje | Aktualizacja | Co zawiera |
|---|---|---|---|
| `project/plan.md` | 00: v1 | 02a: v2 po D3; 03a: v3 po D4 | Cel, znany zakres, kolejność wyników, produkty, ryzyka i warunki wydania |
| `plans/verification-validation.md` | 00: v1 | 02a: R3; 03a: R4; 04a: próba wydania i T9 | Co i jak sprawdzić, granice dowodu, przegląd, walidacja, kryteria i wyjścia |
| `plans/increment-01.md` | 00a, przed RED | Pozostaje zapisem przyjętego I1 | Wejścia, kroki pierwszej funkcji, regresja, demonstracja i warunki zakończenia |
| `plans/input-errors.md` | 02a, po D3 i przed nowymi testami | Pozostaje zapisem przyjętego E1 | Testy negatywne, korekta adaptera, instrukcja, jawna luka do domknięcia przed wydaniem |
| `plans/increment-02.md` | 03a, po Z1/D4 i przed kodem R4 | Pozostaje zapisem przyjętego I2 | Granice liczenia wierszy, wpływ na JSON, regresja i odbiór przyrostu |
| `plans/release.md` | 04a, przed T9, manifestem i kopiowaniem | W 05 nie zamienia się w raport | Kandydat, skład, warunki, kolejność kontroli, próba i osobny odbiór |

**Plan → wykonanie → dowód → ocena.** `reports/progress.md` pojawia się w 00 i zachowuje kolejne fakty wykonania. `reports/tests.md` pojawia się dopiero po pierwszym RED. `reports/deployment.md` dopiero po próbie. Zgoda na plan lub próbę nie jest zgodą na wydanie.

Pierwotny plan I1 nie zostaje dopisany wstecz o R4. Nowe wymaganie powoduje plan I2 oraz nową wersję planu głównego. Na wczesnych zdjęciach nie ma przyszłych decyzji i funkcji. Po samym wykonaniu zadania nie zmieniamy kryteriów planu na takie, które przypadkiem spełniła implementacja.

## Projekt: TextStats

Małe lokalne CLI czyta jeden plik UTF-8 i zwraca JSON z liczbą słów, później także wierszy. Nie ma sieci, bazy danych, usług, logowania, trwałego zapisu danych użytkownika ani migracji. Prosta domena pozwala obserwować rozwój repo bez dodatkowych wątków architektonicznych.

To osobne hipotetyczne repozytorium, a nie nowy produkt wdrożony w iso-template-agent. Przykładowe katalogi i ID nie podlegają parserom aktualnego szablonu. Kopiowanie przykładu do prawdziwego projektu wymaga dostosowania jego zasad i zakresu.

## Co wynika z normy, a co dodaliśmy dydaktycznie

| Warstwa | Znaczenie |
|---|---|
| Norma | Określa cele czynności oraz rodzaje informacji w produktach pracy; tabela przy każdym pliku wskazuje odpowiedni WP lub własną adaptację |
| Nasza reprezentacja | Nazwy ścieżek, Markdown, Python, układ tabel, ID R/T/C/D i jeden rodzaj treści na plik |
| Fabuła | Potrzeby redaktora, jego decyzje oraz przykładowe zapisy przeglądu, walidacji i akceptacji |
| Wykonany eksperyment techniczny | Uruchomione testy zamieszczonego kodu oraz próba lokalnej dostawy na danych syntetycznych |

Nie każdy plik jest pełnym produktem pracy normy. Przykładowo purpose i scope przedstawiają fragmenty WP.02; nie zawierają rzeczywistych podpisów. Manifest wydania wspiera identyfikację WP.17, ale nie zastępuje programu i dokumentacji. Instrukcje dostawy pokazują fragment tematyki WP.10, bez planowania zarządczego.

Źródła: [§5.1–5.3 — cykle i warunki wejścia](../../../iso-29110-5-1/chapters/05-overview.md), [PM.01–PM.03 — planowanie, wykonanie i kontrola](../../../iso-29110-5-1/chapters/06-project-management-pm-process.md), [SI.O2–SI.O7 — wymagania, projekt, kod, testy i V&V](../../../iso-29110-5-1/chapters/07-software-implementation-si-process.md), [rozdział 9 — produkty pracy, WP.10 i możliwość ich dzielenia/łączenia](../../../iso-29110-5-1/chapters/09-description-of-work-products.md), [B.11 — informacyjny opis planu testów](../../../iso-29110-5-1/chapters/annex-b-additional-testing-tasks.md). B.11 wspiera część testową naszego V&V, nie jest pełnym opisem całego V&V. Linki zakładają lokalne repozytoria sąsiadujące na dysku.

W prawdziwym małym projekcie można połączyć część dokumentów. Tutaj rozdzielenie jest celowym zabiegiem dydaktycznym na prośbę użytkownika. Liczba plików w ostatnim zdjęciu nie jest minimalnym wymaganiem ISO ani rekomendacją dla każdego skryptu. Większość tych plików to krótkie informacje; do lokalnej dostawy trafiają tylko dwa pliki programu i instrukcja.

## Ulepszenia dydaktyczne

1. **Ten sam projekt i stabilne ID.** Możesz śledzić jedno wymaganie od potrzeby do testu, kodu i wydania.
2. **Pełny stan plus różnica.** Nie musisz domyślać się, które pliki nadal istnieją; oznaczenia N/Z/= pokazują koszt zmiany.
3. **Bodziec przed plikiem.** Każde zdjęcie wyjaśnia zdarzenie uzasadniające nową treść.
4. **Decyzja operatora osobno od pracy agenta.** Widać, kiedy potrzebne jest uzgodnienie znaczenia, a kiedy agent kontynuuje przyjęty zakres.
5. **Jawny niedoskonały moment.** RED i otwarte Q1 pokazują poprawne etapy pracy, nie tylko elegancki stan końcowy.
6. **Dowód z granicami.** Testy mają znany zakres; wstrzyknięcie PermissionError nie jest próbą rzeczywistych uprawnień systemu.
7. **Weryfikacja i walidacja podczas rozwoju.** Przegląd wymagań poprzedza implementację, a informacja zwrotna z pierwszego przyrostu poprzedza wydanie. Fikcyjne rekordy są oznaczone.
8. **Bez automatycznego dokładania praktyk.** R4 potrzebuje zwykłych testów i aktualizacji instrukcji; nie wymaga Alloy ani TLA+.
9. **Plan widoczny przed skutkiem.** Cztery zdjęcia planowania pozwalają sprawdzić, co wiadomo przed działaniem. Stare zielone testy pozostają dowodem wcześniejszego zakresu, gdy nowe wymaganie dopiero weszło do planu.

## Jak czytać jako operator

Na każdym zdjęciu odpowiedz sobie:

- Co teraz wiemy, czego nie wiedzieliśmy wcześniej?
- Jaki problem uzasadnia nowy plik? Co byśmy zgubili bez tej informacji?
- Czy zmiana dotyczy znaczenia produktu i wymaga mojej decyzji, czy wykonania już przyjętego zadania?
- Które wymaganie ma kod i dowód, a które tylko obietnicę lub link?
- Czy raport opisuje tę samą wersję, którą chcemy pokazać lub dostarczyć?

Odpowiedź prowadząca: R1 opisuje oczekiwanie, tests/test_stats.py sposób sprawdzenia, reports/tests.md wykonanie, a records/acceptance.md decyzję odbiorczą. Przejście testu nie tworzy automatycznie trzech pozostałych faktów.

## Rzeczywiście wykonane sprawdzenia tej lekcji

Kod ze zdjęć odtworzono w oddzielnych katalogach tymczasowych. Początkowy RED: cztery testy wykazały NotImplementedError. Kolejne GREEN: 5, 7, 8 i 9 testów. Dodatkowe RED poprzedziły obsługę błędów oraz liczenie wierszy. Test PermissionError dopisano do istniejącego poprawnego zachowania i od razu przeszedł — nie przypisujemy mu nieistniejącego RED.

Końcowe trzy pliki skopiowano do osobnego katalogu i porównano SHA-256 z manifestem. Uruchomienie spoza instalacji dało właściwy JSON oraz kod błędu dla nieistniejącego pliku. To próba lokalnego dostarczenia demonstratora. Nie wykonano wdrożenia do środowiska użytkownika, walidacji z rzeczywistym odbiorcą ani niezależnego audytu.

Dokumenty są materiałem do czytania. Zamieszczony kod można odtworzyć, ale nie trzeba nic instalować, aby przejść lekcję. Przyszłe zmiany przykładów wymagają ponownego sprawdzenia wyników; obecny opis nie jest wieczystym certyfikatem poprawności.

W rewizji 2 sprawdzono kolejność powstania planów, brak przyszłych wymagań na wczesnych zdjęciach, zachowanie pierwotnych planów przyrostów oraz zgodność kodu, testów i manifestu z wcześniej wykonanym demonstratorem. Kod i pakiet dostawy nie zostały zmienione; zachowane wyniki są wynikami wcześniejszych prób, nie nowymi uruchomieniami. Poprawiono też chronologię środowiska, aktualność mapy śladu po przyjęciu nowego wymagania i rozdzielenie zgody na próbę od odbioru.

Kontekst dalszej nauki: [konspekt operacyjny](../OPERATIONAL-CONTEXT-AND-PRACTICE-ROLLOUT.md) i [PROPOSAL](../PROPOSAL-CONTEXT-AND-PRACTICE-PACKAGES.md).
