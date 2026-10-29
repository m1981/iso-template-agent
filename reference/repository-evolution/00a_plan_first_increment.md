# 00a. Przed przyrostem 1 — plan, kryteria i środowisko

**Pełne zdjęcie hipotetycznego repozytorium.** Plany, role i decyzje są fikcyjne; oznaczone wyniki testów demonstratora pochodzą z rzeczywistych wcześniejszych prób. [Jak czytać](README.md).

**Bodziec:** Mamy cel; potrzebujemy kolejności i warunków ukończenia pierwszego zachowania.

**Operator:** P1 zatwierdza w fabule sposób wykonania I1; kod i wyniki jeszcze nie istnieją.

**Chronologia planu:** Najpierw P1 i plan I1, potem projekt/przegląd i przypadki. Następne zdjęcie pokazuje pierwsze wykonanie testu.

## Struktura

```text
textstats/
├── design/
│   └── components.md
├── plans/
│   ├── increment-01.md
│   └── verification-validation.md
├── process/
│   ├── environment.md
│   └── working-rules.md
├── project/
│   ├── decisions.md
│   ├── plan.md
│   └── purpose.md
├── records/
│   └── reviews/
│       └── requirements.md
├── reports/
│   └── progress.md
├── spec/
│   ├── glossary.md
│   ├── requirements.md
│   └── scope.md
└── tests/
    └── cases.md
```

Wszystkie pliki robocze są w tabeli. Metadane Git i cache są poza widokiem. Pełna treść dokumentów jest w tabeli, kod i JSON poniżej. N = nowy, Z = zmieniony, = = bez zmian względem bezpośrednio poprzedniego zdjęcia.

| Stan | Ścieżka | Jeden rodzaj treści | Powiązanie z normą | Treść pliku |
|---|---|---|---|---|
| N | `design/components.md` | projekt komponentów | WP.16 — mały projekt i interfejsy | # Projekt techniczny<br>C1 count_words(text): czysta funkcja str → int, realizuje logikę R1/R1a.<br>C2 main(): adapter argumenty → plik UTF-8 → C1 → JSON; planowany dla R1/R2.<br>Funkcja nie czyta plików. Adapter nie definiuje słowa ponownie. |
| N | `plans/increment-01.md` | plan — zamiar i kryteria | nasz szczegółowy plan przyrostu — rozwinięcie WP.10 | # Plan I1 v1 — pierwsze liczenie słów<br>Źródła: D1/D2, R1/R1a/R2 i project/plan.md v1. Poza zakresem: nierozstrzygnięte Q1.<br>Wejście: znaczenie słowa uzgodnione, projekt C1/C2 i kryteria przejrzane w fabule, środowisko opisane.<br>Kroki: przygotować T1–T4 → wykonać RED na szkielecie C1 → zaimplementować count_words → GREEN → dołączyć C2 i test T5 → regresja → instrukcja → demonstracja.<br>T5 sprawdza rzeczywisty plik, JSON, kod wyjścia, stderr i niezmienność bajtów. Nie zastępuje T1–T4.<br>Wyjście: poprawny przepływ działa, dowód wskazuje wersję wejść, luki zapisane, instrukcja pozwala wykonać demonstrację.<br>Następne decyzje: wynik demonstracji i Q1. Nie ma zgody na wydanie ani na nowe funkcje.<br>Ten plik opisuje zamiar; RED/GREEN i stopień wykonania trafią do raportów. |
| = | `plans/verification-validation.md` | plan — zamiar i kryteria | nasz plan V&V; SI.O7 i informacyjny B.11 w części testowej | # Plan V&amp;V v1 — przed pierwszym kodem<br>Cel: sprawdzić zgodność z wymaganiami bieżącego zakresu oraz przydatność wyniku dla redaktora; początkowo R1/R1a/R2.<br>Weryfikacja dokumentów: przed kodem przejrzeć definicje, mierzalność wymagań i kontrakty C1/C2.<br>Testy: przykłady dla słów, pustego tekstu, białych znaków i Unicode; po połączeniu komponentów test plik → CLI → JSON oraz niezmienność wejścia.<br>Walidacja: po pierwszym działającym przyroście odbiorca w fabule użyje instrukcji i oceni, czy rozumie wynik.<br>Środowisko: Python i syntetyczne pliki; dokładną instrukcję przygotować przed pierwszym uruchomieniem testów.<br>Kryterium przyrostu: wykonane testy jego zakresu i jawne luki. Kryterium wydania: zamknięte Q1, uzgodnione testy całego zakresu, próba dostawy i osobna decyzja.<br>Przewidziane dowody: reports/tests.md; rekord przeglądu i rekord walidacji osobno. Plan nie potwierdza ich wykonania.<br>Zmiana wymagania lub granicy uruchamia przegląd tego planu; wynik jednego środowiska nie jest dowodem wszystkich platform. |
| N | `process/environment.md` | środowisko wykonania | WP.05 — skrócony opis | # Środowisko<br>Python 3.10+, biblioteka standardowa, bez instalacji bibliotek.<br>Testy: python3 -B -m unittest discover -s tests -v<br>Program: python3 -B src/cli.py ścieżka<br>Przed pierwszym testem zapisać wersję interpretera w raporcie. Próba na jednym środowisku nie potwierdza wszystkich wersji i systemów. |
| = | `process/working-rules.md` | zasady działania | nasza adaptacja, nie wymagania produktu | # Reguły pracy<br>Czytaj cel, zakres, pojęcia, wymagania i decyzję dotyczącą zadania.<br>Nowe zachowanie: przykład → test RED → kod GREEN → refaktoryzacja.<br>Wynik testu jest oddzielny od oceny przydatności i zgody odbiorcy.<br>Nie zgaduj odpowiedzi na otwarte pytania. Poszerzaj kontekst o dotknięte interfejsy. |
| Z | `project/decisions.md` | rozstrzygnięcia i pytania | własny zapis uzgodnień; nie pełny WP.07 | # Decyzje w fabule<br>FIKCYJNE UZGODNIENIA — nie są odpowiedziami Michała.<br>D1. Odbiorca wybiera liczenie fragmentów rozdzielonych białymi znakami, ze wskazanym ograniczeniem dla interpunkcji.<br>D2. Pierwszy przyrost liczy słowa.<br>Q1. Kontrakt błędu odczytu pozostaje otwarty.<br>P0. FABUŁA: przyjęto operacyjny plan projektu v1 i plan V&amp;V v1; Q1 blokuje wydanie, nie implementację poprawnego wejścia.<br>P1. FABUŁA: plan I1 przyjęty przed testem RED; nie rozszerza D2 ani nie rozstrzyga Q1. |
| = | `project/plan.md` | plan — zamiar i kryteria | WP.10 — część planowania operacyjnego | # Plan projektu v1 — Day 1<br>Cel: lokalne liczenie słów; potrzeba i granice w project/purpose.md oraz spec/scope.md.<br>Cykl: małe przyrosty; doprecyzowanie → projekt → test → kod → sprawdzenie → demonstracja.<br>Wynik I1: poprawny plik daje words, kod 0 i niezmienione wejście.<br>Dalszy krok: rozstrzygnąć Q1 i obsłużyć uzgodnione błędy. Innych funkcji jeszcze nie planujemy.<br>Po gotowym zakresie: sprawdzić komplet dostawy w osobnym katalogu, przeprowadzić walidację i przedstawić do odbioru.<br>Produkty: program, instrukcja, testy, raporty i identyfikacja dostawy. Kod i instrukcja stanowią pakiet użytkownika.<br>Warunki: implementację poprawnej ścieżki można rozpocząć; wydanie czeka na Q1, testy uzgodnionego zakresu i decyzję odbiorcy.<br>Ryzyko: niejasne znaczenie słowa oraz mylenie zielonego testu z gotowością wydania; odpowiedź: słownik, przegląd i jawne luki.<br>Zmiana celu lub zakresu: decyzja i nowa wersja planu; wykonanie zapisujemy w reports/progress.md.<br>To operacyjny wycinek WP.10, bez harmonogramu, zasobów, kosztów i polityki kopii; nie pełny plan normatywny. |
| = | `project/purpose.md` | potrzeba odbiorcy | WP.02 — część celu i opisu produktu | # Potrzeba<br>TextStats pomaga redaktorowi policzyć słowa przed wysłaniem notatki.<br>Odbiorca demonstracyjny używa terminala. Dostawa: lokalny program i instrukcja.<br>To fikcyjny opis potrzeby, nie rzeczywista podpisana umowa. |
| N | `records/reviews/requirements.md` | rekord przeglądu wymagań | WP.23 — przykład wybranego przeglądu | # Przegląd wymagań przed kodem — FABUŁA<br>Przedmiot: R1/R1a/R2 i projekt C1/C2.<br>Kryteria: znaczenie słowa jawne; pusty tekst rozstrzygnięty; wynik obserwowalny; każda reguła ma sposób sprawdzenia.<br>Wynik w fabule: zakres poprawnego wejścia można implementować; Q1 blokuje dopuszczenie do użycia docelowego.<br>To przykładowy rekord, nie wykonany niezależny przegląd ani podpis. |
| Z | `reports/progress.md` | stan wykonania, nie plan | WP.09 — fragment bez rozliczeń zasobów i kosztu | # Postęp — kolejne punkty historii<br>00: przygotowano zakres i plany; kod, testy i dostawa niewykonane.<br>00a: plan I1, projekt, przypadki i środowisko przygotowane; RED jeszcze nie wykonany.<br>Wyniki testów są wykonane na demonstratorze; decyzje i przeglądy odbiorcy oznaczone FABUŁA nie są rzeczywistymi zatwierdzeniami. |
| = | `spec/glossary.md` | definicje | WP.13 — pomoc w jednoznaczności | # Pojęcia<br>Słowo: maksymalny niepusty fragment między znakami uznawanymi przez str.split() Pythona za białe znaki.<br>Interpunkcja nie dzieli fragmentu: „kot,pies” jest jednym słowem.<br>Wejście: plik tekstowy dekodowany ściśle jako UTF-8. |
| = | `spec/requirements.md` | wymagania produktu | WP.13 — wybrany zakres | # Wymagania<br>R1. Dla poprawnego pliku UTF-8 system wypisuje JSON z polem words równym liczbie słów według słownika; kod procesu 0.<br>R1a. Pusty tekst i same białe znaki dają words=0.<br>R2. System nie zmienia bajtów pliku wejściowego.<br>Otwarte Q1: kontrakt błędu odczytu trzeba ustalić przed użyciem docelowym. |
| = | `spec/scope.md` | granice produktu | WP.02 — część zakresu | # Zakres<br>IN: jeden plik UTF-8, wynik w terminalu, odczyt bez zmiany bajtów wejścia.<br>OUT: PDF, DOCX, GUI, sieć, baza danych i modyfikowanie plików.<br>Pierwsza funkcja: liczba słów. Liczba wierszy nie jest jeszcze zamówiona. |
| N | `tests/cases.md` | przypadki i procedura | WP.19 — wejścia, oczekiwania i warunki | # Przypadki<br>T1 → R1: „Ala ma kota” daje 3.<br>T2 → R1a: pusty tekst daje 0.<br>T3 → R1a: spacja, tabulator i LF dają 0.<br>T4 → R1: „zażółć　gęślą” ze spacją ideograficzną daje 2.<br>Procedura: wywołać C1 i porównać z oczekiwaniem. Środowisko: Python 3.10+, biblioteka standardowa. |

## Różnica i lekcja

Nowe: `design/components.md`, `plans/increment-01.md`, `process/environment.md`, `records/reviews/requirements.md`, `tests/cases.md`.

Zmienione: `project/decisions.md`, `reports/progress.md`.

Plan przyrostu konkretyzuje plan projektu. Przypadki testowe określają oczekiwania, ale nie są wynikiem testu.

**Granica dowodu:** Brak kodu i wykonanych testów. Przegląd wymagań jest fikcyjnym przykładem, nie rzeczywistym niezależnym audytem.

**Sprawdź rozumienie:** co było zaplanowane przed działaniem, co dopiero wykonano i która decyzja dotyczyła zakresu, próby lub odbioru?

[Poprzednie zdjęcie](00_day1.md)

[Następne zdjęcie](01_increment_words_red.md)
