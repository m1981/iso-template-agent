# 05. Lokalne wdrożenie i miejsce odbioru

**Pełne zdjęcie hipotetycznego repozytorium.** Decyzje są fikcyjne; oznaczone wyniki wykonania demonstratora pochodzą z rzeczywistych prób w katalogu tymczasowym. [Jak czytać](README.md).

**Bodziec:** Kod działa w repo; sprawdzamy zestaw dostawy z innego katalogu.

**Operator:** Próbę techniczną wykonano. Rekordy weryfikatora i odbiorcy są oznaczone jako fikcyjne.

## Struktura

```text
textstats/
├── design/
│   └── components.md
├── docs/
│   └── usage.md
├── process/
│   ├── environment.md
│   └── working-rules.md
├── project/
│   ├── changes/
│   │   └── lines.md
│   ├── decisions.md
│   └── purpose.md
├── records/
│   ├── acceptance.md
│   ├── corrections.md
│   ├── reviews/
│   │   └── requirements.md
│   ├── trace.md
│   ├── validation-increment.md
│   ├── validation.md
│   └── verification.md
├── release/
│   ├── delivery.md
│   └── manifest.json
├── reports/
│   ├── deployment.md
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
    ├── test_boundary.py
    ├── test_cli.py
    └── test_stats.py
```

Wszystkie pliki robocze przykładu są w tabeli. Metadane Git, cache i logi narzędzia tworzącego lekcję są poza widokiem. Treść dokumentów podano w całości; pełny kod i JSON są pod tabelą. N = nowy, Z = zmieniony, = = bez zmian.

| Stan | Ścieżka | Jeden rodzaj treści | Powiązanie z normą | Treść pliku |
|---|---|---|---|---|
| = | `design/components.md` | projekt komponentów | WP.16 — mały projekt i interfejsy | # Projekt techniczny<br>C1 count_words(text): czysta funkcja str → int, realizuje logikę R1/R1a.<br>C2 main(): adapter argumenty → plik UTF-8 → C1 → JSON; planowany dla R1/R2.<br>Funkcja nie czyta plików. Adapter nie definiuje słowa ponownie.<br>C2 przechwytuje OSError i UnicodeError na granicy odczytu, realizując R3. C1 bez zmian.<br>C1 count_lines(text): str → liczba wierszy R4. C2 dodaje lines do JSON. |
| = | `docs/usage.md` | instrukcja użytkownika | WP.18 — skrócona instrukcja | # Użycie<br>Z katalogu repo: python3 -B src/cli.py /pełna/ścieżka/do/pliku.txt<br>Dla „Ala ma kota” wynik: {&quot;words&quot;: 3, &quot;lines&quot;: 1}.<br>Liczenie fragmentów oddzielonych białymi znakami, bez analizy językowej.<br>Błąd odczytu lub UTF-8: kod 2 i stderr „Nie można odczytać pliku UTF-8.”, bez wyniku stdout. Sprawdź ścieżkę, uprawnienia i kodowanie.<br>Wiersze rozdziela LF; końcowy LF nie dodaje pustego wiersza. Pusty plik: oba liczniki 0. |
| N | `process/environment.md` | środowisko wykonania | WP.05 — skrócony opis | # Środowisko<br>Python 3.10+, biblioteka standardowa, bez instalacji bibliotek.<br>Testy: python3 -B -m unittest discover -s tests -v<br>Program: python3 -B src/cli.py ścieżka<br>Wyniki dotyczą środowiska wskazanego w raporcie; nie sprawdzono wszystkich wersji Pythona i systemów. |
| = | `process/working-rules.md` | zasady działania | nasza adaptacja, nie wymagania produktu | # Reguły pracy<br>Czytaj cel, zakres, pojęcia, wymagania i decyzję dotyczącą zadania.<br>Nowe zachowanie: przykład → test RED → kod GREEN → refaktoryzacja.<br>Wynik testu jest oddzielny od oceny przydatności i zgody odbiorcy.<br>Nie zgaduj odpowiedzi na otwarte pytania. Poszerzaj kontekst o dotknięte interfejsy. |
| = | `project/changes/lines.md` | wniosek zmiany | WP.03 — część funkcjonalna | # Wniosek Z1 — liczba wierszy<br>Fikcyjny odbiorca prosi o drugą miarę w tym samym JSON, aby ocenić długość notatki.<br>Propozycja: separator LF; CRLF daje ten sam wynik; końcowy LF nie dodaje wiersza, pusty tekst ma 0.<br>Wpływ: R4, słownik, C1/C2, testy, instrukcja i ślad. R1–R3 pozostają.<br>Brak oceny harmonogramu i kosztu — poza zakresem tego ćwiczenia. |
| = | `project/decisions.md` | rozstrzygnięcia i pytania | własny zapis uzgodnień; nie pełny WP.07 | # Decyzje w fabule<br>FIKCYJNE UZGODNIENIA — nie są odpowiedziami Michała.<br>D1. Odbiorca wybiera liczenie fragmentów rozdzielonych białymi znakami, ze wskazanym ograniczeniem dla interpunkcji.<br>D2. Pierwszy przyrost liczy słowa.<br>D3. W fabule odbiorca zamyka Q1 i przyjmuje R3; traceback nie jest uzgodnionym interfejsem.<br>D4. W fabule odbiorca przyjmuje Z1; lines dodajemy do words. |
| = | `project/purpose.md` | potrzeba odbiorcy | WP.02 — część celu i opisu produktu | # Potrzeba<br>TextStats pomaga redaktorowi policzyć słowa przed wysłaniem notatki.<br>Odbiorca demonstracyjny używa terminala. Dostawa: lokalny program i instrukcja.<br>To fikcyjny opis potrzeby, nie rzeczywista podpisana umowa. |
| N | `records/acceptance.md` | decyzja odbiorcza | WP.01 — przykład, nie rzeczywisty odbiór | # Przykładowy odbiór — FABUŁA<br>Przedmiot: TextStats 0.1.0, pliki wskazane w release/manifest.json i instrukcja.<br>Decyzja w historii: odbiorca przyjmuje lokalny licznik słów i wierszy.<br>Ograniczenia: jeden plik UTF-8, terminal, brak formatów biurowych i gwarancji wszystkich platform.<br>To nie zgoda Michała. Rzeczywiste podpisy i data odbioru nie istnieją. |
| = | `records/corrections.md` | niezgodność i korekta | WP.04 — mały rejestr | # Korekta C01<br>Po dodaniu R3 testy T6/T7 wykazały kod 1 i traceback zamiast wymaganego kontraktu.<br>Przyczyna: wyjątki propagowane z adaptera. Korekta: obsługa OSError i UnicodeError na granicy.<br>Ponowne sprawdzenie: T6/T7 i wcześniejsze testy przechodzą.<br>Nie wykonano jeszcze osobnego przypadku odmowy dostępu. |
| = | `records/reviews/requirements.md` | rekord przeglądu wymagań | WP.23 — przykład wybranego przeglądu | # Przegląd wymagań przed kodem — FABUŁA<br>Przedmiot: R1/R1a/R2 i projekt C1/C2.<br>Kryteria: znaczenie słowa jawne; pusty tekst rozstrzygnięty; wynik obserwowalny; każda reguła ma sposób sprawdzenia.<br>Wynik w fabule: zakres poprawnego wejścia można implementować; Q1 blokuje dopuszczenie do użycia docelowego.<br>To przykładowy rekord, nie wykonany niezależny przegląd ani podpis. |
| Z | `records/trace.md` | ślad | WP.21 | # Relacje<br>R1/R1a → C1 → count_words → T1–T4 → tests/test_stats.py → reports/tests.md.<br>R1/R2 → C2 → main → T5 → tests/test_cli.py → reports/tests.md.<br>R3 → C2 → main → T6/T7 → tests/test_cli.py → reports/tests.md. T9 → tests/test_boundary.py sprawdza wstrzyknięty PermissionError; uprawnienia systemu nie są testowane.<br>R4 → C1/C2 → count_lines/main → T8/T5 → test_stats.py/test_cli.py → reports/tests.md. |
| = | `records/validation-increment.md` | rekord walidacji przyrostu | WP.22 — przykład informacji zwrotnej | # Demonstracja pierwszego przyrostu — FABUŁA<br>Cel: sprawdzić, czy redaktor rozumie liczbę słów i potrafi odczytać wynik.<br>Przykładowa obserwacja: poprawny tekst daje oczekiwaną liczbę; użytkownik potrzebuje jeszcze jasnego komunikatu po wskazaniu złego pliku.<br>Wniosek w fabule: rozstrzygnąć Q1, zachować pierwszą funkcję. Nie jest to odbiór wydania.<br>Nie odbyła się rzeczywista sesja z odbiorcą; rekord obrazuje walidację podczas rozwoju, nie tylko na końcu. |
| N | `records/validation.md` | rekord przydatności | WP.22 — przykład, nie wynik automatycznych testów | # Przykładowa walidacja — FABUŁA<br>Odbiorca demonstracyjny: redaktor, cel: ocena długości notatki.<br>Próba w fabule: samodzielne uruchomienie według instrukcji, odczyt liczb, rozpoznanie błędu.<br>Przykładowa ocena: przydatne do uzgodnionej definicji słowa i wiersza.<br>Nie odbyła się walidacja z Michałem ani innym rzeczywistym odbiorcą. |
| N | `records/verification.md` | rekord weryfikacji | WP.23 — przykład wybranej treści | # Przykładowy przegląd — FABUŁA<br>Przedmiot: R1–R4, C1/C2, ślad i kandydat 0.1.0.<br>Kryteria: jednoznaczne pojęcia; każda reguła ma sprawdzenie; raport ujawnia ograniczenia.<br>Przykładowa ocena: spójność w wybranym zakresie; brak pełnej macierzy platform.<br>Forma dydaktyczna: nie wykonano niezależnego przeglądu ani nie uzyskano podpisu recenzenta. |
| N | `release/delivery.md` | instrukcja dostarczenia | instrukcje dostawy WP.10 / SI.O6 — nie pełny plan | # Dostarczenie 0.1.0<br>Warunek: testy zakresu przechodzą, ograniczenia znane, zgoda odbiorcy dotyczy kandydata.<br>Skopiować src/cli.py, src/stats.py i docs/usage.md do nowego katalogu, zachowując podkatalogi.<br>Nie nadpisywać istniejącej instalacji. Sprawdzić skróty manifestu.<br>Uruchomić z innego katalogu: poprawny tekst daje words=3, lines=1 i kod 0; brak pliku daje kod 2.<br>Wynik próby i decyzja odbiorcy są osobne. Brak serwera i publikacji sieciowej. |
| N | `release/manifest.json` | identyfikacja wydania | element produktu WP.17; sam manifest nie jest produktem | Pełna treść: blok 1 poniżej. |
| N | `reports/deployment.md` | wynik próby dostawy | WP.20 — test dostarczonego zestawu | # Próba dostawy<br>Rzeczywiście skopiowano 3 pliki do nowego katalogu tymczasowego i porównano SHA-256.<br>Start spoza instalacji: kod 0, stdout {&quot;words&quot;: 3, &quot;lines&quot;: 1}.<br>Brak pliku: kod 2, stdout pusty, stderr Nie można odczytać pliku UTF-8..<br>Python 3.14.6, Darwin arm64.<br>To wykonana próba techniczna, nie wdrożenie docelowe ani walidacja klienta. |
| Z | `reports/tests.md` | wynik wykonania testów | WP.20 — skrócony raport | # Wynik 05 kandydat<br>Rzeczywiste wykonanie demonstratora w katalogu tymczasowym, nie testy iso-template-agent.<br>Środowisko: Python 3.14.6, Darwin arm64.<br>Polecenie: python3 -B -m unittest discover -s tests -v<br>Kod wyjścia: 0.<br>Wynik: 9 testów przechodzi. T9 od razu był GREEN na istniejącym kodzie; nie deklarujemy RED tego testu. Błąd uprawnień jest symulowany.<br>Wejścia: kod i testy z tego zdjęcia; wynik nie przenosi się automatycznie na następne zdjęcie. |
| = | `spec/glossary.md` | definicje | WP.13 — pomoc w jednoznaczności | # Pojęcia<br>Słowo: maksymalny niepusty fragment między znakami uznawanymi przez str.split() Pythona za białe znaki.<br>Interpunkcja nie dzieli fragmentu: „kot,pies” jest jednym słowem.<br>Wejście: plik tekstowy dekodowany ściśle jako UTF-8.<br>Wiersz: fragment zakończony LF lub ostatni niepusty fragment; pusty tekst ma 0. CR przed LF nie tworzy osobnego wiersza. |
| = | `spec/requirements.md` | wymagania produktu | WP.13 — wybrany zakres | # Wymagania<br>R1. Dla poprawnego pliku UTF-8 system wypisuje JSON z polem words równym liczbie słów według słownika; kod procesu 0.<br>R1a. Pusty tekst i same białe znaki dają words=0.<br>R2. System nie zmienia bajtów pliku wejściowego.<br>R3. Przy błędzie dostępu, braku pliku lub błędnym UTF-8 system kończy się kodem 2, pozostawia stdout pusty i wypisuje na stderr: Nie można odczytać pliku UTF-8.<br>R4. Dla poprawnego wejścia JSON zawiera także lines według definicji wiersza. |
| = | `spec/scope.md` | granice produktu | WP.02 — część zakresu | # Zakres<br>IN: jeden plik UTF-8, wynik w terminalu, odczyt bez zmiany bajtów wejścia.<br>OUT: PDF, DOCX, GUI, sieć, baza danych i modyfikowanie plików.<br>Bieżący zakres: liczba słów oraz liczba wierszy według D4/Z1. |
| = | `src/cli.py` | kod adaptera | WP.15 — C2 | Pełna treść: blok 2 poniżej. |
| = | `src/stats.py` | kod komponentu | WP.15 — C1 | Pełna treść: blok 3 poniżej. |
| Z | `tests/cases.md` | przypadki i procedura | WP.19 — wejścia, oczekiwania i warunki | # Przypadki<br>T1 → R1: „Ala ma kota” daje 3.<br>T2 → R1a: pusty tekst daje 0.<br>T3 → R1a: spacja, tabulator i LF dają 0.<br>T4 → R1: „zażółć　gęślą” ze spacją ideograficzną daje 2.<br>Procedura: wywołać C1 i porównać z oczekiwaniem. Środowisko: Python 3.10+, biblioteka standardowa.<br>T5 → R1/R2: uruchomić CLI dla pliku o nazwie ze spacją; oczekiwać words=3, kodu 0, pustego stderr i identycznych bajtów wejścia.<br>T6 → R3: brak pliku; T7 → R3: bajt 0xff. Oczekiwane: kod 2, puste stdout, uzgodniony stderr; poziom integracji.<br>T8 → R4: pusty tekst, bez LF, końcowy LF, sam LF, dwa wiersze i CRLF; wyniki 0,1,1,1,2,2. T5 dodatkowo sprawdza lines=1.<br>T9 → R3: wstrzyknąć PermissionError w odczycie i porównać kod 2, stdout i stderr. Test izolowany. |
| N | `tests/test_boundary.py` | test izolowanej granicy | WP.19 — wstrzyknięty PermissionError, nie test uprawnień OS | Pełna treść: blok 4 poniżej. |
| = | `tests/test_cli.py` | testy integracyjne | WP.19 — T5–T7 | Pełna treść: blok 5 poniżej. |
| = | `tests/test_stats.py` | testy funkcji | WP.19 — T1–T4 i T8 | Pełna treść: blok 6 poniżej. |

## Blok 1: `release/manifest.json`

```json
{
  "version": "0.1.0",
  "sha256": {
    "src/cli.py": "f91b2238ba5af8538aa943071de1dacca754cdbc864e0c13eb66064a47c043b9",
    "src/stats.py": "17b1d1346055458ae6ed5eac980d90741d2a74b47aeb6d7eb337903e5c340ba8",
    "docs/usage.md": "61d23ae7bdd04c22d375857b03443dcb54e99bc147a8f9494f7660f93e126326"
  }
}
```

## Blok 2: `src/cli.py`

```python
import argparse
import json
import sys
from pathlib import Path
from stats import count_words, count_lines


def main():
    parser = argparse.ArgumentParser(description="Licznik tekstu UTF-8")
    parser.add_argument("path", type=Path)
    args = parser.parse_args()
    try:
        text = args.path.read_text(encoding="utf-8")
    except (OSError, UnicodeError):
        print("Nie można odczytać pliku UTF-8.", file=sys.stderr)
        return 2
    print(json.dumps({"words": count_words(text), "lines": count_lines(text)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

## Blok 3: `src/stats.py`

```python
def count_words(text: str) -> int:
    return len(text.split())
def count_lines(text: str) -> int:
    return text.count("\n") + int(bool(text) and not text.endswith("\n"))
```

## Blok 4: `tests/test_boundary.py`

```python
import io
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from cli import main


class BoundaryTests(unittest.TestCase):
    def test_permission_denied(self):
        with patch("sys.argv", ["textstats", "blocked.txt"]), \
             patch("cli.Path.read_text", side_effect=PermissionError), \
             patch("sys.stdout", new_callable=io.StringIO) as out, \
             patch("sys.stderr", new_callable=io.StringIO) as err:
            self.assertEqual(main(), 2)
            self.assertEqual(out.getvalue(), "")
            self.assertEqual(err.getvalue().strip(), "Nie można odczytać pliku UTF-8.")
```

## Blok 5: `tests/test_cli.py`

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
            self.assertEqual(json.loads(result.stdout), {"words": 3, "lines": 1})
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

## Blok 6: `tests/test_stats.py`

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

    def test_lines(self):
        from stats import count_lines
        for text, expected in [("", 0), ("a", 1), ("a\n", 1), ("\n", 1),
                               ("a\nb", 2), ("a\r\nb\r\n", 2)]:
            with self.subTest(text=text):
                self.assertEqual(count_lines(text), expected)
```

## Różnica i lekcja

Nowe: `process/environment.md`, `records/acceptance.md`, `records/validation.md`, `records/verification.md`, `release/delivery.md`, `release/manifest.json`, `reports/deployment.md`, `tests/test_boundary.py`.

Zmienione: `records/trace.md`, `reports/tests.md`, `tests/cases.md`.

Test, raport testu, weryfikacja, walidacja i odbiór odpowiadają na różne pytania.

**Granica dowodu:** Brak rzeczywistej walidacji i podpisów. Nie testowano całej macierzy platform i dużych plików. To nie pełny profil Basic.

**Kontekst następnego kroku:** cel i decyzje → dotknięte wymagania i pojęcia → projekt → właściwe testy i wyniki. Pełne zdjęcie pomaga w nauce; rzeczywisty agent nie musi czytać ponownie całej niezmienionej treści.

**Sprawdź rozumienie:** który plik określa oczekiwanie, który pokazuje wykonanie, a który decyzję? Czy zielony test zastępuje pozostałe dwa?

[Poprzednie zdjęcie](04_increment_lines.md)
