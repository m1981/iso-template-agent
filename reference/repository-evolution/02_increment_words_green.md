# 02. Przyrost 1 — działający przepływ

**Pełne zdjęcie hipotetycznego repozytorium.** Decyzje są fikcyjne; oznaczone wyniki wykonania demonstratora pochodzą z rzeczywistych prób w katalogu tymczasowym. [Jak czytać](README.md).

**Bodziec:** Łączymy funkcję z plikiem i terminalem.

**Operator:** Demonstracja przyrostu nie jest jeszcze akceptacją wydania.

## Struktura

```text
textstats/
├── design/
│   └── components.md
├── docs/
│   └── usage.md
├── process/
│   └── working-rules.md
├── project/
│   ├── decisions.md
│   └── purpose.md
├── records/
│   ├── reviews/
│   │   └── requirements.md
│   ├── trace.md
│   └── validation-increment.md
├── reports/
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

Wszystkie pliki robocze przykładu są w tabeli. Metadane Git, cache i logi narzędzia tworzącego lekcję są poza widokiem. Treść dokumentów podano w całości; pełny kod i JSON są pod tabelą. N = nowy, Z = zmieniony, = = bez zmian.

| Stan | Ścieżka | Jeden rodzaj treści | Powiązanie z normą | Treść pliku |
|---|---|---|---|---|
| = | `design/components.md` | projekt komponentów | WP.16 — mały projekt i interfejsy | # Projekt techniczny<br>C1 count_words(text): czysta funkcja str → int, realizuje logikę R1/R1a.<br>C2 main(): adapter argumenty → plik UTF-8 → C1 → JSON; planowany dla R1/R2.<br>Funkcja nie czyta plików. Adapter nie definiuje słowa ponownie. |
| N | `docs/usage.md` | instrukcja użytkownika | WP.18 — skrócona instrukcja | # Użycie<br>Z katalogu repo: python3 -B src/cli.py /pełna/ścieżka/do/pliku.txt<br>Dla „Ala ma kota” wynik: {&quot;words&quot;: 3}.<br>Liczenie fragmentów oddzielonych białymi znakami, bez analizy językowej.<br>Błędy odczytu są jeszcze nieuzgodnione. Przyrost do demonstracji, nie do wydania. |
| = | `process/working-rules.md` | zasady działania | nasza adaptacja, nie wymagania produktu | # Reguły pracy<br>Czytaj cel, zakres, pojęcia, wymagania i decyzję dotyczącą zadania.<br>Nowe zachowanie: przykład → test RED → kod GREEN → refaktoryzacja.<br>Wynik testu jest oddzielny od oceny przydatności i zgody odbiorcy.<br>Nie zgaduj odpowiedzi na otwarte pytania. Poszerzaj kontekst o dotknięte interfejsy. |
| = | `project/decisions.md` | rozstrzygnięcia i pytania | własny zapis uzgodnień; nie pełny WP.07 | # Decyzje w fabule<br>FIKCYJNE UZGODNIENIA — nie są odpowiedziami Michała.<br>D1. Odbiorca wybiera liczenie fragmentów rozdzielonych białymi znakami, ze wskazanym ograniczeniem dla interpunkcji.<br>D2. Pierwszy przyrost liczy słowa.<br>Q1. Kontrakt błędu odczytu pozostaje otwarty. |
| = | `project/purpose.md` | potrzeba odbiorcy | WP.02 — część celu i opisu produktu | # Potrzeba<br>TextStats pomaga redaktorowi policzyć słowa przed wysłaniem notatki.<br>Odbiorca demonstracyjny używa terminala. Dostawa: lokalny program i instrukcja.<br>To fikcyjny opis potrzeby, nie rzeczywista podpisana umowa. |
| = | `records/reviews/requirements.md` | rekord przeglądu wymagań | WP.23 — przykład wybranego przeglądu | # Przegląd wymagań przed kodem — FABUŁA<br>Przedmiot: R1/R1a/R2 i projekt C1/C2.<br>Kryteria: znaczenie słowa jawne; pusty tekst rozstrzygnięty; wynik obserwowalny; każda reguła ma sposób sprawdzenia.<br>Wynik w fabule: zakres poprawnego wejścia można implementować; Q1 blokuje dopuszczenie do użycia docelowego.<br>To przykładowy rekord, nie wykonany niezależny przegląd ani podpis. |
| Z | `records/trace.md` | ślad | WP.21 | # Relacje<br>R1/R1a → C1 → count_words → T1–T4 → tests/test_stats.py → reports/tests.md.<br>R1/R2 → C2 → main → T5 → tests/test_cli.py → reports/tests.md.<br>Q1 pozostaje otwarte; obsługa błędów nie ma uzgodnionego wymagania. |
| N | `records/validation-increment.md` | rekord walidacji przyrostu | WP.22 — przykład informacji zwrotnej | # Demonstracja pierwszego przyrostu — FABUŁA<br>Cel: sprawdzić, czy redaktor rozumie liczbę słów i potrafi odczytać wynik.<br>Przykładowa obserwacja: poprawny tekst daje oczekiwaną liczbę; użytkownik potrzebuje jeszcze jasnego komunikatu po wskazaniu złego pliku.<br>Wniosek w fabule: rozstrzygnąć Q1, zachować pierwszą funkcję. Nie jest to odbiór wydania.<br>Nie odbyła się rzeczywista sesja z odbiorcą; rekord obrazuje walidację podczas rozwoju, nie tylko na końcu. |
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

Zmienione: `records/trace.md`, `reports/tests.md`, `src/stats.py`, `tests/cases.md`.

Test integracyjny pojawia się przy pierwszym połączeniu komponentów. Nie odkładamy go do końca projektu.

**Granica dowodu:** Brak kontraktu błędów, próby instalacji i odbioru.

**Kontekst następnego kroku:** cel i decyzje → dotknięte wymagania i pojęcia → projekt → właściwe testy i wyniki. Pełne zdjęcie pomaga w nauce; rzeczywisty agent nie musi czytać ponownie całej niezmienionej treści.

**Sprawdź rozumienie:** który plik określa oczekiwanie, który pokazuje wykonanie, a który decyzję? Czy zielony test zastępuje pozostałe dwa?

[Poprzednie zdjęcie](01_increment_words_red.md)

[Następne zdjęcie](03_increment_input_errors.md)
