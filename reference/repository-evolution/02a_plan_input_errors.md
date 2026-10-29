# 02a. Przed obsługą błędów — decyzja i aktualizacja planów

**Pełne zdjęcie hipotetycznego repozytorium.** Plany, role i decyzje są fikcyjne; oznaczone wyniki testów demonstratora pochodzą z rzeczywistych wcześniejszych prób. [Jak czytać](README.md).

**Bodziec:** Demonstracja ujawniła potrzebę jasnego kontraktu błędu.

**Operator:** Najpierw D3 rozstrzyga Q1, następnie P2 przyjmuje zakres i kryteria E1.

**Chronologia planu:** D3 → projekt v2/V&V v2/E1 → przypadki T6/T7 → dopiero potem RED i implementacja.

## Struktura

```text
textstats/
├── design/
│   └── components.md
├── docs/
│   └── usage.md
├── plans/
│   ├── increment-01.md
│   ├── input-errors.md
│   └── verification-validation.md
├── process/
│   ├── environment.md
│   └── working-rules.md
├── project/
│   ├── decisions.md
│   ├── plan.md
│   └── purpose.md
├── records/
│   ├── reviews/
│   │   └── requirements.md
│   ├── trace.md
│   └── validation-increment.md
├── reports/
│   ├── progress.md
│   └── tests.md
├── spec/
│   ├── glossary.md
│   ├── requirements.md
│   └── scope.md
├── src/
│   ├── cli.py
│   └── stats.py
└── tests/
    ├── cases.md
    ├── test_cli.py
    └── test_stats.py
```

Wszystkie pliki robocze są w tabeli. Metadane Git i cache są poza widokiem. Pełna treść dokumentów jest w tabeli, kod i JSON poniżej. N = nowy, Z = zmieniony, = = bez zmian względem bezpośrednio poprzedniego zdjęcia.

| Stan | Ścieżka | Jeden rodzaj treści | Powiązanie z normą | Treść pliku |
|---|---|---|---|---|
| Z | `design/components.md` | projekt komponentów | WP.16 — mały projekt i interfejsy | # Projekt techniczny<br>C1 count_words(text): czysta funkcja str → int, realizuje logikę R1/R1a.<br>C2 main(): adapter argumenty → plik UTF-8 → C1 → JSON; adapter dla R1/R2.<br>Funkcja nie czyta plików. Adapter nie definiuje słowa ponownie.<br>Projekt rozszerzenia: C2 ma przechwytywać OSError i UnicodeError na granicy odczytu, realizując R3. C1 bez zmian. |
| = | `docs/usage.md` | instrukcja użytkownika | WP.18 — skrócona instrukcja | # Użycie<br>Z katalogu repo: python3 -B src/cli.py /pełna/ścieżka/do/pliku.txt<br>Dla „Ala ma kota” wynik: {&quot;words&quot;: 3}.<br>Liczenie fragmentów oddzielonych białymi znakami, bez analizy językowej.<br>Błędy odczytu są jeszcze nieuzgodnione. Przyrost do demonstracji, nie do wydania. |
| = | `plans/increment-01.md` | plan — zamiar i kryteria | nasz szczegółowy plan przyrostu — rozwinięcie WP.10 | # Plan I1 v1 — pierwsze liczenie słów<br>Źródła: D1/D2, R1/R1a/R2 i project/plan.md v1. Poza zakresem: nierozstrzygnięte Q1.<br>Wejście: znaczenie słowa uzgodnione, projekt C1/C2 i kryteria przejrzane w fabule, środowisko opisane.<br>Kroki: przygotować T1–T4 → wykonać RED na szkielecie C1 → zaimplementować count_words → GREEN → dołączyć C2 i test T5 → regresja → instrukcja → demonstracja.<br>T5 sprawdza rzeczywisty plik, JSON, kod wyjścia, stderr i niezmienność bajtów. Nie zastępuje T1–T4.<br>Wyjście: poprawny przepływ działa, dowód wskazuje wersję wejść, luki zapisane, instrukcja pozwala wykonać demonstrację.<br>Następne decyzje: wynik demonstracji i Q1. Nie ma zgody na wydanie ani na nowe funkcje.<br>Ten plik opisuje zamiar; RED/GREEN i stopień wykonania trafią do raportów. |
| N | `plans/input-errors.md` | plan — zamiar i kryteria | nasz plan zadania stabilizacyjnego — część WP.10 | # Plan stabilizacji E1 v1 — kontrakt błędów<br>Źródła: wynik demonstracji, decyzja D3 i wymaganie R3. To domknięcie przewidzianego obszaru Q1.<br>Wejście: uzgodniony kod 2, puste stdout i komunikat stderr; działająca poprawna ścieżka I1.<br>Kroki: dodać T6/T7 → wykazać RED na obecnym CLI → obsłużyć błędy na granicy C2 → uruchomić wszystkie regresje → poprawić instrukcję i ślad.<br>Wyjście tego przyrostu: T6/T7 oraz wcześniejsze testy przechodzą; R3 ma implementację; niesprawdzone warianty pozostają jawne.<br>Przed wydaniem: dołożyć osobną kontrolę PermissionError; sam brak pliku nie dowodzi całego kontraktu dostępu.<br>Dowody: raport testów i rekord C01, jeśli test ujawni niezgodność. Przyjęcie planu nie oznacza, że wynik lub C01 już istnieje.<br>Poza zakresem: nowe liczniki i zmiana formatu poprawnego JSON. |
| Z | `plans/verification-validation.md` | plan — zamiar i kryteria | nasz plan V&V; SI.O7 i informacyjny B.11 w części testowej | # Plan V&amp;V v2 — przed realizacją R3<br>Cel: sprawdzić zgodność z wymaganiami bieżącego zakresu oraz przydatność wyniku dla redaktora; początkowo R1/R1a/R2.<br>Weryfikacja dokumentów: przed kodem przejrzeć definicje, mierzalność wymagań i kontrakty C1/C2.<br>Testy: przykłady dla słów, pustego tekstu, białych znaków i Unicode; po połączeniu komponentów test plik → CLI → JSON oraz niezmienność wejścia.<br>Walidacja: po pierwszym działającym przyroście odbiorca w fabule użyje instrukcji i oceni, czy rozumie wynik.<br>Środowisko: Python i syntetyczne pliki; dokładną instrukcję przygotować przed pierwszym uruchomieniem testów.<br>Rozszerzenie R3: T6/T7 dla braku pliku i złego UTF-8; osobny test odmowy dostępu przed wydaniem. Przyrost E1 może zakończyć się z jawną luką tego ostatniego testu, wydanie nie.<br>Dowody I1 zachowują zakres R1/R2; nie potwierdzają nowego R3. Nowy wynik powstanie dopiero po wykonaniu rozszerzonych testów.<br>Zmiana wymagania lub granicy uruchamia przegląd tego planu; wynik jednego środowiska nie jest dowodem wszystkich platform. |
| = | `process/environment.md` | środowisko wykonania | WP.05 — skrócony opis | # Środowisko<br>Python 3.10+, biblioteka standardowa, bez instalacji bibliotek.<br>Testy: python3 -B -m unittest discover -s tests -v<br>Program: python3 -B src/cli.py ścieżka<br>Przed pierwszym testem zapisać wersję interpretera w raporcie. Próba na jednym środowisku nie potwierdza wszystkich wersji i systemów. |
| = | `process/working-rules.md` | zasady działania | nasza adaptacja, nie wymagania produktu | # Reguły pracy<br>Czytaj cel, zakres, pojęcia, wymagania i decyzję dotyczącą zadania.<br>Nowe zachowanie: przykład → test RED → kod GREEN → refaktoryzacja.<br>Wynik testu jest oddzielny od oceny przydatności i zgody odbiorcy.<br>Nie zgaduj odpowiedzi na otwarte pytania. Poszerzaj kontekst o dotknięte interfejsy. |
| Z | `project/decisions.md` | rozstrzygnięcia i pytania | własny zapis uzgodnień; nie pełny WP.07 | # Decyzje w fabule<br>FIKCYJNE UZGODNIENIA — nie są odpowiedziami Michała.<br>D1. Odbiorca wybiera liczenie fragmentów rozdzielonych białymi znakami, ze wskazanym ograniczeniem dla interpunkcji.<br>D2. Pierwszy przyrost liczy słowa.<br>D3. W fabule odbiorca zamyka Q1 i przyjmuje R3; traceback nie jest uzgodnionym interfejsem.<br>P0. FABUŁA: przyjęto operacyjny plan projektu v1 i plan V&amp;V v1; Q1 blokuje wydanie, nie implementację poprawnego wejścia.<br>P1. FABUŁA: plan I1 przyjęty przed testem RED; nie rozszerza D2 ani nie rozstrzyga Q1.<br>P2. FABUŁA: po D3 przyjęto plan projektu v2, V&amp;V v2 i E1; wariant odmowy dostępu pozostaje warunkiem przed wydaniem. |
| Z | `project/plan.md` | plan — zamiar i kryteria | WP.10 — część planowania operacyjnego | # Plan projektu v2 — po rozstrzygnięciu Q1<br>Cel: lokalne liczenie słów; potrzeba i granice w project/purpose.md oraz spec/scope.md.<br>Cykl: małe przyrosty; doprecyzowanie → projekt → test → kod → sprawdzenie → demonstracja.<br>Wynik I1: poprawny plik daje words, kod 0 i niezmienione wejście.<br>Najbliższa stabilizacja E1: R3 według D3 i plans/input-errors.md; przed wydaniem sprawdzić wszystkie uzgodnione warianty. Innych funkcji jeszcze nie planujemy.<br>Po gotowym zakresie: sprawdzić komplet dostawy w osobnym katalogu, przeprowadzić walidację i przedstawić do odbioru.<br>Produkty: program, instrukcja, testy, raporty i identyfikacja dostawy. Kod i instrukcja stanowią pakiet użytkownika.<br>Warunki wydania: wykonane I1 i E1, sprawdzony wariant odmowy dostępu, próba dostawy i decyzja odbiorcy. Q1 rozstrzygnięte przez D3.<br>Ryzyko: niejasne znaczenie słowa oraz mylenie zielonego testu z gotowością wydania; odpowiedź: słownik, przegląd i jawne luki.<br>Zmiana celu lub zakresu: decyzja i nowa wersja planu; wykonanie zapisujemy w reports/progress.md.<br>To operacyjny wycinek WP.10, bez harmonogramu, zasobów, kosztów i polityki kopii; nie pełny plan normatywny. |
| = | `project/purpose.md` | potrzeba odbiorcy | WP.02 — część celu i opisu produktu | # Potrzeba<br>TextStats pomaga redaktorowi policzyć słowa przed wysłaniem notatki.<br>Odbiorca demonstracyjny używa terminala. Dostawa: lokalny program i instrukcja.<br>To fikcyjny opis potrzeby, nie rzeczywista podpisana umowa. |
| = | `records/reviews/requirements.md` | rekord przeglądu wymagań | WP.23 — przykład wybranego przeglądu | # Przegląd wymagań przed kodem — FABUŁA<br>Przedmiot: R1/R1a/R2 i projekt C1/C2.<br>Kryteria: znaczenie słowa jawne; pusty tekst rozstrzygnięty; wynik obserwowalny; każda reguła ma sposób sprawdzenia.<br>Wynik w fabule: zakres poprawnego wejścia można implementować; Q1 blokuje dopuszczenie do użycia docelowego.<br>To przykładowy rekord, nie wykonany niezależny przegląd ani podpis. |
| Z | `records/trace.md` | ślad | WP.21 | # Relacje<br>R1/R1a → C1 → count_words → T1–T4 → tests/test_stats.py → reports/tests.md.<br>R1/R2 → C2 → main → T5 → tests/test_cli.py → reports/tests.md.<br>Q1 rozstrzygnięte w D3. R3 → projekt rozszerzenia C2 → planowane T6/T7; brak wdrożenia i dowodu R3. Raport I1 ma wcześniejszy zakres. |
| = | `records/validation-increment.md` | rekord walidacji przyrostu | WP.22 — przykład informacji zwrotnej | # Demonstracja pierwszego przyrostu — FABUŁA<br>Cel: sprawdzić, czy redaktor rozumie liczbę słów i potrafi odczytać wynik.<br>Przykładowa obserwacja: poprawny tekst daje oczekiwaną liczbę; użytkownik potrzebuje jeszcze jasnego komunikatu po wskazaniu złego pliku.<br>Wniosek w fabule: rozstrzygnąć Q1, zachować pierwszą funkcję. Nie jest to odbiór wydania.<br>Nie odbyła się rzeczywista sesja z odbiorcą; rekord obrazuje walidację podczas rozwoju, nie tylko na końcu. |
| Z | `reports/progress.md` | stan wykonania, nie plan | WP.09 — fragment bez rozliczeń zasobów i kosztu | # Postęp — kolejne punkty historii<br>00: przygotowano zakres i plany; kod, testy i dostawa niewykonane.<br>00a: plan I1, projekt, przypadki i środowisko przygotowane; RED jeszcze nie wykonany.<br>01: I1 w toku; wykonano 4 testy i uzyskano RED. Pozostałe kroki I1 oczekują.<br>02: I1 ma 5 testów GREEN i instrukcję; demonstracja w fabule wskazuje potrzebę rozstrzygnięcia Q1. Wydanie wciąż niedopuszczone.<br>02a: Q1 rozstrzygnięte przez D3; plany zaktualizowane przed nowym testem. R3 jeszcze niewdrożone.<br>Wyniki testów są wykonane na demonstratorze; decyzje i przeglądy odbiorcy oznaczone FABUŁA nie są rzeczywistymi zatwierdzeniami. |
| = | `reports/tests.md` | wynik wykonania testów | WP.20 — skrócony raport | # Wynik 02 GREEN<br>Rzeczywiste wykonanie demonstratora w katalogu tymczasowym, nie testy iso-template-agent.<br>Środowisko: Python 3.14.6, Darwin arm64.<br>Polecenie: python3 -B -m unittest discover -s tests -v<br>Kod wyjścia: 0.<br>Wynik: 5 testów przechodzi: 4 funkcji i 1 integracyjny. Błędy wejścia pozostają poza sprawdzonym kontraktem.<br>Wejścia: kod i testy z tego zdjęcia; wynik nie przenosi się automatycznie na następne zdjęcie. |
| = | `spec/glossary.md` | definicje | WP.13 — pomoc w jednoznaczności | # Pojęcia<br>Słowo: maksymalny niepusty fragment między znakami uznawanymi przez str.split() Pythona za białe znaki.<br>Interpunkcja nie dzieli fragmentu: „kot,pies” jest jednym słowem.<br>Wejście: plik tekstowy dekodowany ściśle jako UTF-8. |
| Z | `spec/requirements.md` | wymagania produktu | WP.13 — wybrany zakres | # Wymagania<br>R1. Dla poprawnego pliku UTF-8 system wypisuje JSON z polem words równym liczbie słów według słownika; kod procesu 0.<br>R1a. Pusty tekst i same białe znaki dają words=0.<br>R2. System nie zmienia bajtów pliku wejściowego.<br>R3. Przy błędzie dostępu, braku pliku lub błędnym UTF-8 system kończy się kodem 2, pozostawia stdout pusty i wypisuje na stderr: Nie można odczytać pliku UTF-8. |
| = | `spec/scope.md` | granice produktu | WP.02 — część zakresu | # Zakres<br>IN: jeden plik UTF-8, wynik w terminalu, odczyt bez zmiany bajtów wejścia.<br>OUT: PDF, DOCX, GUI, sieć, baza danych i modyfikowanie plików.<br>Pierwsza funkcja: liczba słów. Liczba wierszy nie jest jeszcze zamówiona. |
| = | `src/cli.py` | kod adaptera | WP.15 — C2; C1+C2 tworzą oprogramowanie WP.14 | Pełna treść: blok 1 poniżej. |
| = | `src/stats.py` | kod komponentu | WP.15 — C1 | Pełna treść: blok 2 poniżej. |
| Z | `tests/cases.md` | przypadki i procedura | WP.19 — wejścia, oczekiwania i warunki | # Przypadki<br>T1 → R1: „Ala ma kota” daje 3.<br>T2 → R1a: pusty tekst daje 0.<br>T3 → R1a: spacja, tabulator i LF dają 0.<br>T4 → R1: „zażółć　gęślą” ze spacją ideograficzną daje 2.<br>Procedura: wywołać C1 i porównać z oczekiwaniem. Środowisko: Python 3.10+, biblioteka standardowa.<br>T5 → R1/R2: uruchomić CLI dla pliku o nazwie ze spacją; oczekiwać words=3, kodu 0, pustego stderr i identycznych bajtów wejścia.<br>T6 → R3: brak pliku; T7 → R3: bajt 0xff. Oczekiwane: kod 2, puste stdout, uzgodniony stderr; poziom integracji. |
| = | `tests/test_cli.py` | testy integracyjne | WP.19 — proces, plik i JSON | Pełna treść: blok 3 poniżej. |
| = | `tests/test_stats.py` | testy funkcji | WP.19 — automatyzacja T1–T4 | Pełna treść: blok 4 poniżej. |

## Blok 1: `src/cli.py`

```python
import argparse
import json
from pathlib import Path
from stats import count_words


def main():
    parser = argparse.ArgumentParser(description="Licznik tekstu UTF-8")
    parser.add_argument("path", type=Path)
    args = parser.parse_args()
    text = args.path.read_text(encoding="utf-8")
    print(json.dumps({"words": count_words(text)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

## Blok 2: `src/stats.py`

```python
def count_words(text: str) -> int:
    return len(text.split())
```

## Blok 3: `tests/test_cli.py`

```python
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

CLI = Path(__file__).resolve().parents[1] / "src" / "cli.py"


class CliTests(unittest.TestCase):
    def invoke(self, path):
        return subprocess.run([sys.executable, "-B", str(CLI), str(path)],
                              capture_output=True, text=True)

    def test_file_to_json_without_modification(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "tekst ze spacją.txt"
            original = "Ala ma kota\n".encode("utf-8")
            path.write_bytes(original)
            result = self.invoke(path)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(result.stderr, "")
            self.assertEqual(json.loads(result.stdout), {"words": 3})
            self.assertEqual(path.read_bytes(), original)
```

## Blok 4: `tests/test_stats.py`

```python
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from stats import count_words


class WordTests(unittest.TestCase):
    def test_words(self):
        self.assertEqual(count_words("Ala ma kota"), 3)

    def test_empty(self):
        self.assertEqual(count_words(""), 0)

    def test_whitespace(self):
        self.assertEqual(count_words(" \t\n"), 0)

    def test_unicode_space(self):
        self.assertEqual(count_words("zażółć　gęślą"), 2)
```

## Różnica i lekcja

Nowe: `plans/input-errors.md`.

Zmienione: `design/components.md`, `plans/verification-validation.md`, `project/decisions.md`, `project/plan.md`, `records/trace.md`, `reports/progress.md`, `spec/requirements.md`, `tests/cases.md`.

Plan zmienia się z powodu uzgodnionego wymagania. Stary raport 5 testów nie staje się dowodem R3.

**Granica dowodu:** R3 przyjęte w fabule, ale CLI i testy wciąż z I1. Brak wyników E1 i brak rekordu C01.

**Sprawdź rozumienie:** co było zaplanowane przed działaniem, co dopiero wykonano i która decyzja dotyczyła zakresu, próby lub odbioru?

[Poprzednie zdjęcie](02_increment_words_green.md)

[Następne zdjęcie](03_increment_input_errors.md)
