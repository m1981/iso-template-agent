# Repozytorium od Day 1 do lokalnego wdrożenia — historia w zdjęciach

Data: 2026-10-23. Materiał dydaktyczny dla operatora i agenta. To samodzielny przykład, a nie aktualizacja działającego pakietu procesu.

## Jak rozumiemy eksperyment

Obserwujesz jeden fikcyjny projekt w kolejnych punktach rozwoju. Każdy dokument jest pełnym zdjęciem plików roboczych repozytorium: drzewo, tabela ścieżek z treścią, powiązanie z normą oraz wskazanie nowych i zmienionych plików. Krótkie dokumenty mają pełną treść w tabelach; pełny kod jest bezpośrednio pod nimi.

Jeden rodzaj treści na plik: wymagania nie zawierają kodu, przypadki testowe nie zawierają wyników, raport testu nie zastępuje decyzji odbiorczej. Powtórzenie niezmienionej treści między zdjęciami jest celowe — nie musisz rekonstruować stanu z kilku rozdziałów.

Pomijamy planowanie harmonogramów, zasobów, kosztów i migracji zgodnie z zakresem ćwiczenia. Nie tworzymy dla nich pustych formularzy. Pokazujemy wybrane informacje ISO/IEC 29110 i ich przepływ; **nie deklarujemy pełnego spełnienia Basic**, pełnej treści WP.10 ani wszystkich warunków wejścia z §5.2.

## Kolejność czytania

| Zdjęcie | Co się wydarzyło | Czego uczy |
|---|---|---|
| [00 — Day 1](00_day1.md) | Potrzeba, zakres, pojęcia i pierwsze wymagania | Kontekst powstaje przed kodem, a brak decyzji pozostaje widoczny |
| [01 — przyrost słów, RED](01_increment_words_red.md) | Projekt, przegląd, przypadki i nieprzechodzące testy | Wymaganie, test i wynik są różnymi informacjami |
| [02 — przyrost słów, GREEN](02_increment_words_green.md) | Funkcja, CLI, test integracji, instrukcja i demonstracja w fabule | Jeden przyrost przechodzi przez kilka czynności SDLC; walidacja zaczyna się podczas rozwoju |
| [03 — błędy wejścia](03_increment_input_errors.md) | Decyzja o kontrakcie błędów, RED, poprawka i regresja | Jedna zmiana rozchodzi się przez kilka powiązanych artefaktów |
| [04 — przyrost wierszy](04_increment_lines.md) | Nowa potrzeba dodaje drugą funkcję | Przyrost produktu nie wymusza rozbudowy procesu |
| [05 — lokalne wdrożenie](05_local_deployment.md) | Zestaw dostawy, manifest, próba poza repo i miejsce odbioru | Działanie w repo, działanie dostawy, przydatność i akceptacja są różnymi ocenami |

Nie są to fazy kaskadowe „najpierw wszystkie dokumenty, potem cały kod, na końcu wszystkie testy”. Zdjęcia 01–03 pokazują kolejne iteracje pierwszego zachowania; 04 dodaje zachowanie, zachowując wcześniejsze. Zdjęcie 01 zatrzymuje historię przed GREEN, żeby moment TDD był widoczny.

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

Źródła: [§5.1–5.3 — cykle i warunki wejścia](../../../iso-29110-5-1/chapters/05-overview.md), [SI.O2–SI.O7 — wymagania, projekt, kod, testy i V&V](../../../iso-29110-5-1/chapters/07-software-implementation-si-process.md), [rozdział 9 — produkty pracy i możliwość ich dzielenia/łączenia](../../../iso-29110-5-1/chapters/09-description-of-work-products.md). Linki zakładają lokalne repozytoria sąsiadujące na dysku.

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

Kontekst dalszej nauki: [konspekt operacyjny](../OPERATIONAL-CONTEXT-AND-PRACTICE-ROLLOUT.md) i [PROPOSAL](../PROPOSAL-CONTEXT-AND-PRACTICE-PACKAGES.md).
