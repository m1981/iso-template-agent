# 02. Przyrost 1 — działający przepływ

**Pełne zdjęcie hipotetycznego repozytorium.** Plany, role i decyzje są fikcyjne; oznaczone wyniki testów demonstratora pochodzą z rzeczywistych wcześniejszych prób. [Jak czytać](README.md).

**Bodziec:** Łączymy funkcję z plikiem i terminalem.

**Operator:** Demonstracja przyrostu nie jest jeszcze akceptacją wydania.

**Chronologia planu:** Wykonanie I1 trafia do postępu i raportu. Pierwotny plan pozostaje zapisem przyjętej kolejności, bez dopisywania do niego wyniku.

## Struktura

```text
textstats/
├── design/
│   └── components.md
├── docs/
│   └── usage.md
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
| Z | `design/components.md` | projekt komponentów | WP.16 — mały projekt i interfejsy | # Projekt techniczny<br>C1 count_words(text): czysta funkcja str → int, realizuje logikę R1/R1a.<br>C2 main(): adapter argumenty → plik UTF-8 → C1 → JSON; adapter dla R1/R2.<br>Funkcja nie czyta plików. Adapter nie definiuje słowa ponownie. |
| N | `docs/usage.md` | instrukcja użytkownika | WP.18 — skrócona instrukcja | # Użycie<br>Z katalogu repo: python3 -B src/cli.py /pełna/ścieżka/do/pliku.txt<br>Dla „Ala ma kota” wynik: {&quot;words&quot;: 3}.<br>Liczenie fragmentów oddzielonych białymi znakami, bez analizy językowej.<br>Błędy odczytu są jeszcze nieuzgodnione. Przyrost do demonstracji, nie do wydania. |
| = | `plans/increment-01.md` | plan — zamiar i kryteria | nasz szczegółowy plan przyrostu — rozwinięcie WP.10 | # Plan I1 v1 — pierwsze liczenie słów<br>Źródła: D1/D2, R1/R1a/R2 i project/plan.md v1. Poza zakresem: nierozstrzygnięte Q1.<br>Wejście: znaczenie słowa uzgodnione, projekt C1/C2 i kryteria przejrzane w fabule, środowisko opisane.<br>Kroki: przygotować T1–T4 → wykonać RED na szkielecie C1 → zaimplementować count_words → GREEN → dołączyć C2 i test T5 → regresja → instrukcja → demonstracja.<br>T5 sprawdza rzeczywisty plik, JSON, kod wyjścia, stderr i niezmienność bajtów. Nie zastępuje T1–T4.<br>Wyjście: poprawny przepływ działa, dowód wskazuje wersję wejść, luki zapisane, instrukcja pozwala wykonać demonstrację.<br>Następne decyzje: wynik demonstracji i Q1. Nie ma zgody na wydanie ani na nowe funkcje.<br>Ten plik opisuje zamiar; RED/GREEN i stopień wykonania trafią do raportów. |
| = | `plans/verification-validation.md` | plan — zamiar i kryteria | nasz plan V&V; SI.O7 i informacyjny B.11 w części testowej | # Plan V&amp;V v1 — przed pierwszym kodem<br>Cel: sprawdzić zgodność z wymaganiami bieżącego zakresu oraz przydatność wyniku dla redaktora; początkowo R1/R1a/R2.<br>Weryfikacja dokumentów: przed kodem przejrzeć definicje, mierzalność wymagań i kontrakty C1/C2.<br>Testy: przykłady dla słów, pustego tekstu, białych znaków i Unicode; po połączeniu komponentów test plik → CLI → JSON oraz niezmienność wejścia.<br>Walidacja: po pierwszym działającym przyroście odbiorca w fabule użyje instrukcji i oceni, czy rozumie wynik.<br>Środowisko: Python i syntetyczne pliki; dokładną instrukcję przygotować przed pierwszym uruchomieniem testów.<br>Kryterium przyrostu: wykonane testy jego zakresu i jawne luki. Kryterium wydania: zamknięte Q1, uzgodnione testy całego zakresu, próba dostawy i osobna decyzja.<br>Przewidziane dowody: reports/tests.md; rekord przeglądu i rekord walidacji osobno. Plan nie potwierdza ich wykonania.<br>Zmiana wymagania lub granicy uruchamia przegląd tego planu; wynik jednego środowiska nie jest dowodem wszystkich platform. |
| = | `process/environment.md` | środowisko wykonania | WP.05 — skrócony opis | # Środowisko<br>Python 3.10+, biblioteka standardowa, bez instalacji bibliotek.<br>Testy: python3 -B -m unittest discover -s tests -v<br>Program: python3 -B src/cli.py ścieżka<br>Przed pierwszym testem zapisać wersję interpretera w raporcie. Próba na jednym środowisku nie potwierdza wszystkich wersji i systemów. |
| = | `process/working-rules.md` | zasady działania | nasza adaptacja, nie wymagania produktu | # Reguły pracy<br>Czytaj cel, zakres, pojęcia, wymagania i decyzję dotyczącą zadania.<br>Nowe zachowanie: przykład → test RED → kod GREEN → refaktoryzacja.<br>Wynik testu jest oddzielny od oceny przydatności i zgody odbiorcy.<br>Nie zgaduj odpowiedzi na otwarte pytania. Poszerzaj kontekst o dotknięte interfejsy. |
| = | `project/decisions.md` | rozstrzygnięcia i pytania | własny zapis uzgodnień; nie pełny WP.07 | # Decyzje w fabule<br>FIKCYJNE UZGODNIENIA — nie są odpowiedziami Michała.<br>D1. Odbiorca wybiera liczenie fragmentów rozdzielonych białymi znakami, ze wskazanym ograniczeniem dla interpunkcji.<br>D2. Pierwszy przyrost liczy słowa.<br>Q1. Kontrakt błędu odczytu pozostaje otwarty.<br>P0. FABUŁA: przyjęto operacyjny plan projektu v1 i plan V&amp;V v1; Q1 blokuje wydanie, nie implementację poprawnego wejścia.<br>P1. FABUŁA: plan I1 przyjęty przed testem RED; nie rozszerza D2 ani nie rozstrzyga Q1. |
| = | `project/plan.md` | plan — zamiar i kryteria | WP.10 — część planowania operacyjnego | # Plan projektu v1 — Day 1<br>Cel: lokalne liczenie słów; potrzeba i granice w project/purpose.md oraz spec/scope.md.<br>Cykl: małe przyrosty; doprecyzowanie → projekt → test → kod → sprawdzenie → demonstracja.<br>Wynik I1: poprawny plik daje words, kod 0 i niezmienione wejście.<br>Dalszy krok: rozstrzygnąć Q1 i obsłużyć uzgodnione błędy. Innych funkcji jeszcze nie planujemy.<br>Po gotowym zakresie: sprawdzić komplet dostawy w osobnym katalogu, przeprowadzić walidację i przedstawić do odbioru.<br>Produkty: program, instrukcja, testy, raporty i identyfikacja dostawy. Kod i instrukcja stanowią pakiet użytkownika.<br>Warunki: implementację poprawnej ścieżki można rozpocząć; wydanie czeka na Q1, testy uzgodnionego zakresu i decyzję odbiorcy.<br>Ryzyko: niejasne znaczenie słowa oraz mylenie zielonego testu z gotowością wydania; odpowiedź: słownik, przegląd i jawne luki.<br>Zmiana celu lub zakresu: decyzja i nowa wersja planu; wykonanie zapisujemy w reports/progress.md.<br>To operacyjny wycinek WP.10, bez harmonogramu, zasobów, kosztów i polityki kopii; nie pełny plan normatywny. |
| = | `project/purpose.md` | potrzeba odbiorcy | WP.02 — część celu i opisu produktu | # Potrzeba<br>TextStats pomaga redaktorowi policzyć słowa przed wysłaniem notatki.<br>Odbiorca demonstracyjny używa terminala. Dostawa: lokalny program i instrukcja.<br>To fikcyjny opis potrzeby, nie rzeczywista podpisana umowa. |
| = | `records/reviews/requirements.md` | rekord przeglądu wymagań | WP.23 — przykład wybranego przeglądu | # Przegląd wymagań przed kodem — FABUŁA<br>Przedmiot: R1/R1a/R2 i projekt C1/C2.<br>Kryteria: znaczenie słowa jawne; pusty tekst rozstrzygnięty; wynik obserwowalny; każda reguła ma sposób sprawdzenia.<br>Wynik w fabule: zakres poprawnego wejścia można implementować; Q1 blokuje dopuszczenie do użycia docelowego.<br>To przykładowy rekord, nie wykonany niezależny przegląd ani podpis. |
| Z | `records/trace.md` | ślad | WP.21 | # Relacje<br>R1/R1a → C1 → count_words → T1–T4 → tests/test_stats.py → reports/tests.md.<br>R1/R2 → C2 → main → T5 → tests/test_cli.py → reports/tests.md.<br>Q1 pozostaje otwarte; obsługa błędów nie ma uzgodnionego wymagania. |
| N | `records/validation-increment.md` | rekord walidacji przyrostu | WP.22 — przykład informacji zwrotnej | # Demonstracja pierwszego przyrostu — FABUŁA<br>Cel: sprawdzić, czy redaktor rozumie liczbę słów i potrafi odczytać wynik.<br>Przykładowa obserwacja: poprawny tekst daje oczekiwaną liczbę; użytkownik potrzebuje jeszcze jasnego komunikatu po wskazaniu złego pliku.<br>Wniosek w fabule: rozstrzygnąć Q1, zachować pierwszą funkcję. Nie jest to odbiór wydania.<br>Nie odbyła się rzeczywista sesja z odbiorcą; rekord obrazuje walidację podczas rozwoju, nie tylko na końcu. |
| Z | `reports/progress.md` | stan wykonania, nie plan | WP.09 — fragment bez rozliczeń zasobów i kosztu | # Postęp — kolejne punkty historii<br>00: przygotowano zakres i plany; kod, testy i dostawa niewykonane.<br>00a: plan I1, projekt, przypadki i środowisko przygotowane; RED jeszcze nie wykonany.<br>01: I1 w toku; wykonano 4 testy i uzyskano RED. Pozostałe kroki I1 oczekują.<br>02: I1 ma 5 testów GREEN i instrukcję; demonstracja w fabule wskazuje potrzebę rozstrzygnięcia Q1. Wydanie wciąż niedopuszczone.<br>Wyniki testów są wykonane na demonstratorze; decyzje i przeglądy odbiorcy oznaczone FABUŁA nie są rzeczywistymi zatwierdzeniami. |
| Z | `reports/tests.md` | wynik wykonania testów | WP.20 — skrócony raport | # Wynik 02 GREEN<br>Rzeczywiste wykonanie demonstratora w katalogu tymczasowym, nie testy iso-template-agent.<br>Środowisko: Python 3.14.6, Darwin arm64.<br>Polecenie: python3 -B -m unittest discover -s tests -v<br>Kod wyjścia: 0.<br>Wynik: 5 testów przechodzi: 4 funkcji i 1 integracyjny. Błędy wejścia pozostają poza sprawdzonym kontraktem.<br>Wejścia: kod i testy z tego zdjęcia; wynik nie przenosi się automatycznie na następne zdjęcie. |
| = | `spec/glossary.md` | definicje | WP.13 — pomoc w jednoznaczności | # Pojęcia<br>Słowo: maksymalny niepusty fragment między znakami uznawanymi przez str.split() Pythona za białe znaki.<br>Interpunkcja nie dzieli fragmentu: „kot,pies” jest jednym słowem.<br>Wejście: plik tekstowy dekodowany ściśle jako UTF-8. |
| = | `spec/requirements.md` | wymagania produktu | WP.13 — wybrany zakres | # Wymagania<br>R1. Dla poprawnego pliku UTF-8 system wypisuje JSON z polem words równym liczbie słów według słownika; kod procesu 0.<br>R1a. Pusty tekst i same białe znaki dają words=0.<br>R2. System nie zmienia bajtów pliku wejściowego.<br>Otwarte Q1: kontrakt błędu odczytu trzeba ustalić przed użyciem docelowym. |
| = | `spec/scope.md` | granice produktu | WP.02 — część zakresu | # Zakres<br>IN: jeden plik UTF-8, wynik w terminalu, odczyt bez zmiany bajtów wejścia.<br>OUT: PDF, DOCX, GUI, sieć, baza danych i modyfikowanie plików.<br>Pierwsza funkcja: liczba słów. Liczba wierszy nie jest jeszcze zamówiona. |
| N | `src/cli.py` | kod adaptera | WP.15 — C2; C1+C2 tworzą oprogramowanie WP.14 | Pełna treść: blok 1 poniżej. |
| Z | `src/stats.py` | kod komponentu | WP.15 — C1 | Pełna treść: blok 2 poniżej. |
| Z | `tests/cases.md` | przypadki i procedura | WP.19 — wejścia, oczekiwania i warunki | # Przypadki<br>T1 → R1: „Ala ma kota” daje 3.<br>T2 → R1a: pusty tekst daje 0.<br>T3 → R1a: spacja, tabulator i LF dają 0.<br>T4 → R1: „zażółć　gęślą” ze spacją ideograficzną daje 2.<br>Procedura: wywołać C1 i porównać z oczekiwaniem. Środowisko: Python 3.10+, biblioteka standardowa.<br>T5 → R1/R2: uruchomić CLI dla pliku o nazwie ze spacją; oczekiwać words=3, kodu 0, pustego stderr i identycznych bajtów wejścia. |
| N | `tests/test_cli.py` | testy integracyjne | WP.19 — proces, plik i JSON | Pełna treść: blok 3 poniżej. |
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

Nowe: `docs/usage.md`, `records/validation-increment.md`, `src/cli.py`, `tests/test_cli.py`.

Zmienione: `design/components.md`, `records/trace.md`, `reports/progress.md`, `reports/tests.md`, `src/stats.py`, `tests/cases.md`.

Test integracyjny pojawia się przy pierwszym połączeniu komponentów. Nie odkładamy go do końca projektu.

**Granica dowodu:** Brak kontraktu błędów, próby instalacji i odbioru.

**Sprawdź rozumienie:** co było zaplanowane przed działaniem, co dopiero wykonano i która decyzja dotyczyła zakresu, próby lub odbioru?

[Poprzednie zdjęcie](01_increment_words_red.md)

[Następne zdjęcie](02a_plan_input_errors.md)
