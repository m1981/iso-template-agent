# 03. Doprecyzowanie i korekta — błędy wejścia

**Pełne zdjęcie hipotetycznego repozytorium.** Decyzje są fikcyjne; oznaczone wyniki wykonania demonstratora pochodzą z rzeczywistych prób w katalogu tymczasowym. [Jak czytać](README.md).

**Bodziec:** Przed użyciem trzeba rozstrzygnąć Q1 i sprawdzić niepoprawne dane.

**Operator:** Fikcyjna D3 definiuje oczekiwanie; nie wyprowadzamy go z przypadkowego tracebacku.

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
│   ├── corrections.md
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
| Z | `design/components.md` | projekt komponentów | WP.16 — mały projekt i interfejsy | # Projekt techniczny<br>C1 count_words(text): czysta funkcja str → int, realizuje logikę R1/R1a.<br>C2 main(): adapter argumenty → plik UTF-8 → C1 → JSON; planowany dla R1/R2.<br>Funkcja nie czyta plików. Adapter nie definiuje słowa ponownie.<br>C2 przechwytuje OSError i UnicodeError na granicy odczytu, realizując R3. C1 bez zmian. |
| Z | `docs/usage.md` | instrukcja użytkownika | WP.18 — skrócona instrukcja | # Użycie<br>Z katalogu repo: python3 -B src/cli.py /pełna/ścieżka/do/pliku.txt<br>Dla „Ala ma kota” wynik: {&quot;words&quot;: 3}.<br>Liczenie fragmentów oddzielonych białymi znakami, bez analizy językowej.<br>Błąd odczytu lub UTF-8: kod 2 i stderr „Nie można odczytać pliku UTF-8.”, bez wyniku stdout. Sprawdź ścieżkę, uprawnienia i kodowanie. |
| = | `process/working-rules.md` | zasady działania | nasza adaptacja, nie wymagania produktu | # Reguły pracy<br>Czytaj cel, zakres, pojęcia, wymagania i decyzję dotyczącą zadania.<br>Nowe zachowanie: przykład → test RED → kod GREEN → refaktoryzacja.<br>Wynik testu jest oddzielny od oceny przydatności i zgody odbiorcy.<br>Nie zgaduj odpowiedzi na otwarte pytania. Poszerzaj kontekst o dotknięte interfejsy. |
| Z | `project/decisions.md` | rozstrzygnięcia i pytania | własny zapis uzgodnień; nie pełny WP.07 | # Decyzje w fabule<br>FIKCYJNE UZGODNIENIA — nie są odpowiedziami Michała.<br>D1. Odbiorca wybiera liczenie fragmentów rozdzielonych białymi znakami, ze wskazanym ograniczeniem dla interpunkcji.<br>D2. Pierwszy przyrost liczy słowa.<br>D3. W fabule odbiorca zamyka Q1 i przyjmuje R3; traceback nie jest uzgodnionym interfejsem. |
| = | `project/purpose.md` | potrzeba odbiorcy | WP.02 — część celu i opisu produktu | # Potrzeba<br>TextStats pomaga redaktorowi policzyć słowa przed wysłaniem notatki.<br>Odbiorca demonstracyjny używa terminala. Dostawa: lokalny program i instrukcja.<br>To fikcyjny opis potrzeby, nie rzeczywista podpisana umowa. |
| N | `records/corrections.md` | niezgodność i korekta | WP.04 — mały rejestr | # Korekta C01<br>Po dodaniu R3 testy T6/T7 wykazały kod 1 i traceback zamiast wymaganego kontraktu.<br>Przyczyna: wyjątki propagowane z adaptera. Korekta: obsługa OSError i UnicodeError na granicy.<br>Ponowne sprawdzenie: T6/T7 i wcześniejsze testy przechodzą.<br>Nie wykonano jeszcze osobnego przypadku odmowy dostępu. |
| = | `records/reviews/requirements.md` | rekord przeglądu wymagań | WP.23 — przykład wybranego przeglądu | # Przegląd wymagań przed kodem — FABUŁA<br>Przedmiot: R1/R1a/R2 i projekt C1/C2.<br>Kryteria: znaczenie słowa jawne; pusty tekst rozstrzygnięty; wynik obserwowalny; każda reguła ma sposób sprawdzenia.<br>Wynik w fabule: zakres poprawnego wejścia można implementować; Q1 blokuje dopuszczenie do użycia docelowego.<br>To przykładowy rekord, nie wykonany niezależny przegląd ani podpis. |
| Z | `records/trace.md` | ślad | WP.21 | # Relacje<br>R1/R1a → C1 → count_words → T1–T4 → tests/test_stats.py → reports/tests.md.<br>R1/R2 → C2 → main → T5 → tests/test_cli.py → reports/tests.md.<br>R3 → C2 → main → T6/T7 → tests/test_cli.py → reports/tests.md. Luka: brak osobnego testu PermissionError. |
| = | `records/validation-increment.md` | rekord walidacji przyrostu | WP.22 — przykład informacji zwrotnej | # Demonstracja pierwszego przyrostu — FABUŁA<br>Cel: sprawdzić, czy redaktor rozumie liczbę słów i potrafi odczytać wynik.<br>Przykładowa obserwacja: poprawny tekst daje oczekiwaną liczbę; użytkownik potrzebuje jeszcze jasnego komunikatu po wskazaniu złego pliku.<br>Wniosek w fabule: rozstrzygnąć Q1, zachować pierwszą funkcję. Nie jest to odbiór wydania.<br>Nie odbyła się rzeczywista sesja z odbiorcą; rekord obrazuje walidację podczas rozwoju, nie tylko na końcu. |
| Z | `reports/tests.md` | wynik wykonania testów | WP.20 — skrócony raport | # Wynik 03 GREEN<br>Rzeczywiste wykonanie demonstratora w katalogu tymczasowym, nie testy iso-template-agent.<br>Środowisko: Python 3.14.6, Darwin arm64.<br>Polecenie: python3 -B -m unittest discover -s tests -v<br>Kod wyjścia: 0.<br>Wynik: 7 testów przechodzi. W tym przyroście najpierw 2 testy ujawniły niezgodność R3; potem poprawiono kod. Brak osobnego testu PermissionError.<br>Wejścia: kod i testy z tego zdjęcia; wynik nie przenosi się automatycznie na następne zdjęcie. |
| = | `spec/glossary.md` | definicje | WP.13 — pomoc w jednoznaczności | # Pojęcia<br>Słowo: maksymalny niepusty fragment między znakami uznawanymi przez str.split() Pythona za białe znaki.<br>Interpunkcja nie dzieli fragmentu: „kot,pies” jest jednym słowem.<br>Wejście: plik tekstowy dekodowany ściśle jako UTF-8. |
| Z | `spec/requirements.md` | wymagania produktu | WP.13 — wybrany zakres | # Wymagania<br>R1. Dla poprawnego pliku UTF-8 system wypisuje JSON z polem words równym liczbie słów według słownika; kod procesu 0.<br>R1a. Pusty tekst i same białe znaki dają words=0.<br>R2. System nie zmienia bajtów pliku wejściowego.<br>R3. Przy błędzie dostępu, braku pliku lub błędnym UTF-8 system kończy się kodem 2, pozostawia stdout pusty i wypisuje na stderr: Nie można odczytać pliku UTF-8. |
| = | `spec/scope.md` | granice produktu | WP.02 — część zakresu | # Zakres<br>IN: jeden plik UTF-8, wynik w terminalu, odczyt bez zmiany bajtów wejścia.<br>OUT: PDF, DOCX, GUI, sieć, baza danych i modyfikowanie plików.<br>Pierwsza funkcja: liczba słów. Liczba wierszy nie jest jeszcze zamówiona. |
| Z | `src/cli.py` | kod adaptera | WP.15 — C2 | Pełna treść: blok 1 poniżej. |
| = | `src/stats.py` | kod komponentu | WP.15 — C1 | Pełna treść: blok 2 poniżej. |
| Z | `tests/cases.md` | przypadki i procedura | WP.19 — wejścia, oczekiwania i warunki | # Przypadki<br>T1 → R1: „Ala ma kota” daje 3.<br>T2 → R1a: pusty tekst daje 0.<br>T3 → R1a: spacja, tabulator i LF dają 0.<br>T4 → R1: „zażółć　gęślą” ze spacją ideograficzną daje 2.<br>Procedura: wywołać C1 i porównać z oczekiwaniem. Środowisko: Python 3.10+, biblioteka standardowa.<br>T5 → R1/R2: uruchomić CLI dla pliku o nazwie ze spacją; oczekiwać words=3, kodu 0, pustego stderr i identycznych bajtów wejścia.<br>T6 → R3: brak pliku; T7 → R3: bajt 0xff. Oczekiwane: kod 2, puste stdout, uzgodniony stderr; poziom integracji. |
| Z | `tests/test_cli.py` | testy integracyjne | WP.19 — T5–T7 | Pełna treść: blok 3 poniżej. |
| = | `tests/test_stats.py` | testy funkcji | WP.19 — automatyzacja T1–T4 | Pełna treść: blok 4 poniżej. |

## Blok 1: `src/cli.py`

```python
import argparse
import json
import sys
from pathlib import Path
from stats import count_words


def main():
    parser = argparse.ArgumentParser(description="Licznik tekstu UTF-8")
    parser.add_argument("path", type=Path)
    args = parser.parse_args()
    try:
        text = args.path.read_text(encoding="utf-8")
    except (OSError, UnicodeError):
        print("Nie można odczytać pliku UTF-8.", file=sys.stderr)
        return 2
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

    def test_missing_file(self):
        with tempfile.TemporaryDirectory() as folder:
            result = self.invoke(Path(folder) / "missing.txt")
            self.assertEqual(result.returncode, 2)
            self.assertEqual(result.stdout, "")
            self.assertEqual(result.stderr.strip(), "Nie można odczytać pliku UTF-8.")

    def test_invalid_utf8(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "invalid.txt"
            path.write_bytes(b"\xff")
            result = self.invoke(path)
            self.assertEqual(result.returncode, 2)
            self.assertEqual(result.stdout, "")
            self.assertEqual(result.stderr.strip(), "Nie można odczytać pliku UTF-8.")
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

Nowe: `records/corrections.md`.

Zmienione: `design/components.md`, `docs/usage.md`, `project/decisions.md`, `records/trace.md`, `reports/tests.md`, `spec/requirements.md`, `src/cli.py`, `tests/cases.md`, `tests/test_cli.py`.

Jedno wymaganie zmienia projekt granicy, testy, kod, instrukcję i ślad. Nowy framework nie jest potrzebny.

**Granica dowodu:** 7 testów nie pokrywa jeszcze odmowy dostępu; luka pozostaje jawna.

**Kontekst następnego kroku:** cel i decyzje → dotknięte wymagania i pojęcia → projekt → właściwe testy i wyniki. Pełne zdjęcie pomaga w nauce; rzeczywisty agent nie musi czytać ponownie całej niezmienionej treści.

**Sprawdź rozumienie:** który plik określa oczekiwanie, który pokazuje wykonanie, a który decyzję? Czy zielony test zastępuje pozostałe dwa?

[Poprzednie zdjęcie](02_increment_words_green.md)

[Następne zdjęcie](04_increment_lines.md)
