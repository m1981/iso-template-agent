# Przykładowy plan przyrostu I1 — spójność relacji

Status: **demonstracyjny, niewykonany**. Rodzic: [plan projektu, T/2](project-plan.md). Okno 03–04.11.2026; DEV 10 h, REV 2 h. Poprawki po przeglądzie korzystają z osobnego limitu T/6. To plan przyrostu produktu, nie wdrożenie obecnego szablonu.

## Wynik dla użytkownika

Opiekun wskazuje manifest projektu i otrzymuje raport brakujących powiązań. Program nie przedstawia pustego ani nieodczytanego zakresu jako gotowego do wydania.

## Wejścia i granice

Wejścia: ustalony format demonstracyjny, zakres wydania i kryteria z T/1. Brak uzgodnionego znaczenia pola blokuje dotyczącą go implementację; agent nie zastępuje odpowiedzi założeniem. Format i ID w tym pliku służą wyłącznie przykładowi.

In: parser manifestu, kontrola ID, kontrola zadań i testów dla wymagań w zakresie, deterministyczny raport. Out: wykonywanie testów, ocena ich jakości, formalny solver, zatwierdzanie oraz publikacja wydania.

## Wymagania przyrostu i kryteria

| ID | Wymaganie demonstracyjne | Kryterium |
|---|---|---|
| DEMO/REQ/S1 | Dla każdego wymagania w zakresie wydania system zgłasza brak przypisanego zadania realizacyjnego. | Usunięcie jedynego zadania powoduje lukę z ID wymagania. |
| DEMO/REQ/S2 | Dla każdego wymagania w zakresie system zgłasza brak przypisanego przypadku sprawdzenia. | Usunięcie jedynego przypadku powoduje lukę; test poza wybranym zakresem nie wystarcza. |
| DEMO/REQ/S3 | Przy nieznanym lub zduplikowanym ID system zgłasza błąd danych. | Obie klasy błędu mają osobne przypadki; parser nie odrzuca ich po cichu. |
| DEMO/REQ/S4 | Przy błędzie odczytu albo pustym zakresie system odmawia uznania kontroli za kompletną. | Brak pliku i pusty zakres nie dają wyniku ready. |

## Plan TDD

| Krok | DEV | Wynik do zachowania |
|---|---:|---|
| Przykłady akceptacyjne i kontrakt raportu | 1 h | Oczekiwane komunikaty dla manifestu poprawnego i wadliwego |
| Parser: testy S3/S4, RED, implementacja | 2 h | Log niepowodzenia nowego testu i log GREEN |
| Reguły S1/S2, RED, implementacja | 3 h | Raporty dla braku zadania, braku testu i poprawnego zakresu |
| CLI i test integracyjny wejście → raport | 2 h | Sprawdzenie kodu wyjścia i diagnostyki na rzeczywistym pliku |
| Refaktoryzacja i instrukcja | 2 h | Zielone regresje i instrukcja demonstracji |

REV: 2 h na semantykę reguł, pominięte przypadki i czytelność raportu. Test od razu zielony opisujemy jako sprawdzenie istniejącego zachowania; mutacja nie jest historycznym RED implementacji.

## Projekt kodu i ślad

Proponowany podział: parser danych → model domenowy → czysta funkcja kontroli → adapter CLI. Parser nie decyduje o gotowości wydania, a funkcja domenowa nie czyta plików i nie uruchamia procesów. Prosty rekord `Finding(code, item_id, details)` wystarcza; bez frameworka reguł.

| Wymaganie | Planowany symbol | Test zachowania |
|---|---|---|
| S1 | `check_structure` | wymaganie bez zadania |
| S2 | `check_structure` | wymaganie bez testu w zakresie |
| S3 | `parse_manifest` | duplikat / nierozpoznane odwołanie |
| S4 | `load_manifest`, `check_structure` | błąd odczytu / pusty zakres |

To widok dydaktyczny. Po wdrożeniu relacje powinny mieć jedno źródło i generowany widok odwrotny. Sam wpis w tabeli nie dowodzi istnienia funkcji ani wykonania testu.

## Warunki zakończenia

Wszystkie cztery wymagania mają wykonane testy, demonstracja CLI pokazuje pozytywny i negatywny przypadek, raport nie myli kompletności relacji z jakością testów, instrukcja i ślad odpowiadają implementacji. Brak wymaganych wejść lub błąd narzędzia nie może zamienić się w pass.

## Rejestr przyrostu — początek

| Data | Fakt | Wynik / dowód | Następny krok |
|---|---|---|---|
| 2026-10-22 | Utworzono przykład planu | Brak implementacji i uruchomień | Po zleceniu rzeczywistego projektu uzgodnić wejścia |

Po wykonaniu dopisywać rzeczywiste RED/GREEN, czas, odstępstwa i luki. Nie wypełniać z góry przyszłych wyników.
