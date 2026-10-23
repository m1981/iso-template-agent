# Zapis odpowiedzi: formalne sprawdzanie wykonalności

Zapisano: 2026-10-23 (odpowiedź z 2026-10-22), na prośbę użytkownika. Poniżej zachowano treść poprzedniej odpowiedzi asystenta. Jest to materiał archiwalny, a nie instrukcja wykonania lub zgoda na wdrożenie narzędzi. Dalsze rozwinięcie i granice zastosowania: [primer](FORMAL-MODELS-REQUIREMENTS-AND-PROCESS.md).

Pytanie użytkownika: „czy jako senior requirements engineer i senior SW Validation engineer czy sa metody na zamodelowanie i przetestowanie wykolnosci narzedziami? jakims jezykiem formalnym ?”

---

**Tak. Można zapisać plan lub wymagania jako model formalny i automatycznie sprawdzać jego wykonalność.** Wynik dotyczy jednak przyjętych założeń: solver może wykazać, że harmonogram mieści się w terminie przy zadanych czasach prac; poprawność tych szacunków wymaga osobnej walidacji.

W kontekście naszego szablonu rozdzieliłbym cztery pytania:

| Co chcemy sprawdzić? | Metoda i narzędzie | Przykładowe pytanie | Co otrzymujemy? |
|---|---|---|---|
| **Wykonalność harmonogramu i zasobów** | Programowanie z ograniczeniami: **MiniZinc**, **OR-Tools CP-SAT** | Czy zmieścimy zadania, zależności i przeglądy w terminie przy dostępności zespołu? | Harmonogram spełniający ograniczenia albo stwierdzenie niewykonalności modelu. |
| **Spójność struktury wymagań i planu** | Logika relacji: **Alloy** | Czy może istnieć wydanie zawierające wymaganie bez zaplanowanej weryfikacji? | Przykład lub kontrprzykład w zadanym zakresie analizy. |
| **Poprawność procesu w kolejnych krokach** | Maszyny stanów i logika temporalna: **TLA+ / TLC** | Czy po zmianie wymagania możemy omyłkowo wydać produkt na podstawie nieaktualnego wyniku testu? | Sekwencja prowadząca do naruszenia reguły albo zakończona weryfikacja badanego modelu. |
| **Zachowanie z ograniczeniami czasu** | Automaty czasowe: **UPPAAL** | Czy proces może się zakleszczyć podczas oczekiwania na odpowiedź lub przekroczyć ustalony limit? | Analiza osiągalności stanów i własności czasowych. |

To zastosowania oparte na możliwościach opisanych w dokumentacji: [MiniZinc](https://docs.minizinc.dev/en/stable/), [OR-Tools — harmonogramowanie](https://developers.google.com/optimization/scheduling/job_shop), [Alloy](https://alloytools.org/spec.html), [TLC](https://docs.tlapl.us/using%3Atlc%3Astart), [UPPAAL](https://uppaal.org/texts/small_tutorial.pdf).

**Dla wykonalności planu zacząłbym od modelu ograniczeń.** Przykład demonstracyjny:

| Zadanie | Czas | Zależność |
|---|---:|---|
| A — doprecyzowanie wymagań | 2 dni | — |
| B — implementacja | 4 dni | Po A |
| C — walidacja | 2 dni | Po B |

Można zapisać taki model w MiniZinc:

```minizinc
int: deadline = 7;

var 0..deadline: start_A;
var 0..deadline: start_B;
var 0..deadline: start_C;

constraint start_B >= start_A + 2;
constraint start_C >= start_B + 4;
constraint start_C + 2 <= deadline;

solve satisfy;
```

Z samych ograniczeń wynika, że potrzeba minimum **8 dni**, więc termin 7 dni jest niewykonalny. To przykład do objaśnienia — nie uruchamiałem tutaj solvera.

W rzeczywistym modelu dodalibyśmy kalendarze, dostępność osób, kompetencje, budżet i zasady przeglądów. Trzeba również odróżniać **udowodnioną niewykonalność** od wyniku „nie rozstrzygnięto”, np. po wyczerpaniu czasu obliczeń. [Statusy CP-SAT](https://github.com/google/or-tools/blob/stable/ortools/sat/cp_model.proto)

**Jako inżynier walidacji sprawdzałbym również sam model.** Proponuję taki przebieg ćwiczenia zgodny z TDD:

1. Zdefiniować małe przypadki o ręcznie znanym wyniku: plan wykonalny, niemożliwy termin, konflikt zasobów, cykliczne zależności.
2. Zobaczyć niepowodzenie testu, następnie dodać brakujące ograniczenie.
3. Usuwać lub osłabiać ograniczenia i sprawdzać, czy testy wykrywają błąd modelu.
4. Dla znalezionego harmonogramu niezależnie przeliczać spełnienie ograniczeń.
5. Powiązać wymagania z ograniczeniami, testami i raportami:

   `wymaganie ↔ ograniczenie modelu ↔ przypadek testowy ↔ wynik`

Istotne jest też sprawdzenie, czy model **w ogóle dopuszcza poprawny przebieg**. Sprzeczne założenia mogą sprawić, że reguła „każde wydanie jest poprawne” będzie pozornie spełniona, ponieważ żadne wydanie nie jest możliwe.

**Moja rekomendacja dla naszego boilerplate:** najpierw mały eksperyment z MiniZinc dotyczący wykonalności planu. Osobno TLA+ dla procesu „zmiana → ponowna weryfikacja → dopuszczenie wydania”. To dwa konkretne problemy, z mierzalnym wynikiem. Realność czasów, kosztów i potrzeb użytkownika nadal sprawdzalibyśmy pomiarami, prototypami i przeglądami z interesariuszami.
