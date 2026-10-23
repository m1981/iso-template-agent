# 01. Przyrost 1 — RED

**Pełne zdjęcie hipotetycznego repozytorium.** Decyzje są fikcyjne; oznaczone wyniki wykonania demonstratora pochodzą z rzeczywistych prób w katalogu tymczasowym. [Jak czytać](README.md).

**Bodziec:** Potrzebujemy sprawdzalnego oczekiwania przed napisaniem algorytmu.

**Operator:** Praca mieści się w D2; nie ma nowego pytania o tę samą funkcję.

## Struktura

```text
textstats/
├── design/
│   └── components.md
├── process/
│   └── working-rules.md
├── project/
│   ├── decisions.md
│   └── purpose.md
├── records/
│   ├── reviews/
│   │   └── requirements.md
│   └── trace.md
├── reports/
│   └── tests.md
├── spec/
│   ├── glossary.md
│   ├── requirements.md
│   └── scope.md
├── src/
│   └── stats.py
└── tests/
    ├── cases.md
    └── test_stats.py
```

Wszystkie pliki robocze przykładu są w tabeli. Metadane Git, cache i logi narzędzia tworzącego lekcję są poza widokiem. Treść dokumentów podano w całości; pełny kod i JSON są pod tabelą. N = nowy, Z = zmieniony, = = bez zmian.

| Stan | Ścieżka | Jeden rodzaj treści | Powiązanie z normą | Treść pliku |
|---|---|---|---|---|
| N | `design/components.md` | projekt komponentów | WP.16 — mały projekt i interfejsy | # Projekt techniczny<br>C1 count_words(text): czysta funkcja str → int, realizuje logikę R1/R1a.<br>C2 main(): adapter argumenty → plik UTF-8 → C1 → JSON; planowany dla R1/R2.<br>Funkcja nie czyta plików. Adapter nie definiuje słowa ponownie. |
| = | `process/working-rules.md` | zasady działania | nasza adaptacja, nie wymagania produktu | # Reguły pracy<br>Czytaj cel, zakres, pojęcia, wymagania i decyzję dotyczącą zadania.<br>Nowe zachowanie: przykład → test RED → kod GREEN → refaktoryzacja.<br>Wynik testu jest oddzielny od oceny przydatności i zgody odbiorcy.<br>Nie zgaduj odpowiedzi na otwarte pytania. Poszerzaj kontekst o dotknięte interfejsy. |
| = | `project/decisions.md` | rozstrzygnięcia i pytania | własny zapis uzgodnień; nie pełny WP.07 | # Decyzje w fabule<br>FIKCYJNE UZGODNIENIA — nie są odpowiedziami Michała.<br>D1. Odbiorca wybiera liczenie fragmentów rozdzielonych białymi znakami, ze wskazanym ograniczeniem dla interpunkcji.<br>D2. Pierwszy przyrost liczy słowa.<br>Q1. Kontrakt błędu odczytu pozostaje otwarty. |
| = | `project/purpose.md` | potrzeba odbiorcy | WP.02 — część celu i opisu produktu | # Potrzeba<br>TextStats pomaga redaktorowi policzyć słowa przed wysłaniem notatki.<br>Odbiorca demonstracyjny używa terminala. Dostawa: lokalny program i instrukcja.<br>To fikcyjny opis potrzeby, nie rzeczywista podpisana umowa. |
| N | `records/reviews/requirements.md` | rekord przeglądu wymagań | WP.23 — przykład wybranego przeglądu | # Przegląd wymagań przed kodem — FABUŁA<br>Przedmiot: R1/R1a/R2 i projekt C1/C2.<br>Kryteria: znaczenie słowa jawne; pusty tekst rozstrzygnięty; wynik obserwowalny; każda reguła ma sposób sprawdzenia.<br>Wynik w fabule: zakres poprawnego wejścia można implementować; Q1 blokuje dopuszczenie do użycia docelowego.<br>To przykładowy rekord, nie wykonany niezależny przegląd ani podpis. |
| N | `records/trace.md` | ślad | WP.21 — prosta mapa, bez automatycznego audytu | # Relacje<br>R1/R1a → C1 → src/stats.py::count_words → T1–T4 → tests/test_stats.py → reports/tests.md (RED).<br>R1/R2 → C2 → brak adaptera i testu integracji.<br>Relacje można czytać wstecz od testu do wymagania. Wpis nie oznacza ukończenia. |
| N | `reports/tests.md` | wynik wykonania testów | WP.20 — skrócony raport | # Wynik 01 RED<br>Rzeczywiste wykonanie demonstratora w katalogu tymczasowym, nie testy iso-template-agent.<br>Środowisko: Python 3.14.6, Darwin arm64.<br>Polecenie: python3 -B -m unittest discover -s tests -v<br>Kod wyjścia: 1.<br>Wynik: 4 testy kończą się NotImplementedError; nie istnieje jeszcze realizacja R1.<br>Wejścia: kod i testy z tego zdjęcia; wynik nie przenosi się automatycznie na następne zdjęcie. |
| = | `spec/glossary.md` | definicje | WP.13 — pomoc w jednoznaczności | # Pojęcia<br>Słowo: maksymalny niepusty fragment między znakami uznawanymi przez str.split() Pythona za białe znaki.<br>Interpunkcja nie dzieli fragmentu: „kot,pies” jest jednym słowem.<br>Wejście: plik tekstowy dekodowany ściśle jako UTF-8. |
| = | `spec/requirements.md` | wymagania produktu | WP.13 — wybrany zakres | # Wymagania<br>R1. Dla poprawnego pliku UTF-8 system wypisuje JSON z polem words równym liczbie słów według słownika; kod procesu 0.<br>R1a. Pusty tekst i same białe znaki dają words=0.<br>R2. System nie zmienia bajtów pliku wejściowego.<br>Otwarte Q1: kontrakt błędu odczytu trzeba ustalić przed użyciem docelowym. |
| = | `spec/scope.md` | granice produktu | WP.02 — część zakresu | # Zakres<br>IN: jeden plik UTF-8, wynik w terminalu, odczyt bez zmiany bajtów wejścia.<br>OUT: PDF, DOCX, GUI, sieć, baza danych i modyfikowanie plików.<br>Pierwsza funkcja: liczba słów. Liczba wierszy nie jest jeszcze zamówiona. |
| N | `src/stats.py` | kod komponentu | WP.15 — szkielet C1 | Pełna treść: blok 1 poniżej. |
| N | `tests/cases.md` | przypadki i procedura | WP.19 — wejścia, oczekiwania i warunki | # Przypadki<br>T1 → R1: „Ala ma kota” daje 3.<br>T2 → R1a: pusty tekst daje 0.<br>T3 → R1a: spacja, tabulator i LF dają 0.<br>T4 → R1: „zażółć　gęślą” ze spacją ideograficzną daje 2.<br>Procedura: wywołać C1 i porównać z oczekiwaniem. Środowisko: Python 3.10+, biblioteka standardowa. |
| N | `tests/test_stats.py` | testy funkcji | WP.19 — automatyzacja T1–T4 | Pełna treść: blok 2 poniżej. |

## Blok 1: `src/stats.py`

```python
def count_words(text: str) -> int:
    raise NotImplementedError("R1 niewdrożone")
```

## Blok 2: `tests/test_stats.py`

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

Nowe: `design/components.md`, `records/reviews/requirements.md`, `records/trace.md`, `reports/tests.md`, `src/stats.py`, `tests/cases.md`, `tests/test_stats.py`.

Zmienione: brak.

Przypadki, ich automatyzacja i wyniki wykonania mają osobne pliki. To rzeczywisty pokaz RED.

**Granica dowodu:** Kod jest szkieletem, testy nie przechodzą, CLI nie istnieje.

**Kontekst następnego kroku:** cel i decyzje → dotknięte wymagania i pojęcia → projekt → właściwe testy i wyniki. Pełne zdjęcie pomaga w nauce; rzeczywisty agent nie musi czytać ponownie całej niezmienionej treści.

**Sprawdź rozumienie:** który plik określa oczekiwanie, który pokazuje wykonanie, a który decyzję? Czy zielony test zastępuje pozostałe dwa?

[Poprzednie zdjęcie](00_day1.md)

[Następne zdjęcie](02_increment_words_green.md)
