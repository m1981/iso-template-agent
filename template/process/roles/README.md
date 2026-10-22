# Role i sesje

Jak role ISO/IEC 29110 (rozdział 8 i załącznik B) rozkładają się na Użytkownika i sesje agenta (D-36). Norma pozwala jednej osobie pełnić wiele ról, ale rozdziela autora i zatwierdzającego (SI.02.04–05, SI.03.08) i wymaga niezależnej weryfikacji (uwaga 2 przy SI.O7). Rozdzielamy więc tylko na tych granicach: potrzeba a rozwiązanie, autor a weryfikator, wykonawca a mierzący postęp, poprawność a przydatność dla Użytkownika.

Model jest hipotezą. Sprawdza go pilot (Q-03 w decisions.md); dopóki pilot się nie zakończy, działa tylko to, co w sekcji „Teraz”.

## Teraz

| Kto | Role normy | Robi | Nie robi |
| --- | --- | --- | --- |
| Użytkownik | klient (CUS), decyzje kierownika projektu (PJM) | walidacja (VAL), akceptacja (ACC), zatwierdzanie wymagań i zmian planu (decyzje D) | — |
| sesja autora | analityk (AN), lider techniczny (TL), asystent kierownika (PJM), projektant ekranów (DES) | specyfikacja, plan, rejestr; według AGENTS.md | rekordów VER dla własnej pracy |
| sesja weryfikatora | niezależny weryfikator (SI.O7) | rekordy VER i propozycje korekt; według roles/verifier.md | poprawek w produktach, VAL, ACC |
| skrypty | pomiar postępu (PM.02.01, PM.03.01) | progress.md, trace.md, kontrole w hookach | — |

Mechanizm, który pilnuje granicy autor–weryfikator: błąd E9 (tools/check_separation.py). Sprawdza osobne commity, nie osobne sesje; osobną sesję zapewnia karta i sposób uruchomienia.

## Odłożone: wróć, gdy pilot albo projekt pokaże potrzebę

Każdy punkt ma pozycję w kolejce decisions.md z warunkiem powrotu.

### Karta sesji autora (Q-04)
Karta jak roles/verifier.md dla sesji autora: wejścia, pliki do zapisu, lista „czego nie robi” (np. nie wpisuje rozwiązań do wymagań, REQ.7), wynik sesji. Dziś zastępuje ją AGENTS.md.
Wróć, gdy: pilot pokaże, że weryfikator znajduje powtarzalne usterki tego samego rodzaju (np. „jak” zamiast „co”), które karta autora mogłaby zapobiec, albo gdy sesja autora zaczyna mieszać role.

### Sesje programisty i testera (Q-05)
Na etapie kodu: programista (PR, DES) i tester (TES, załącznik B) w osobnych sesjach. Tester pisze i wykonuje testy z wymagań, bez wglądu w kod (czarna skrzynka), i zapisuje raport testów (WP.20). Karty roles/programmer.md i roles/tester.md według wzoru weryfikatora.
Wróć, gdy: zaczyna się etap kodu.

### Rola w opisie commita i uprawnienia do plików (Q-06)
Linia `Role: verifier` w opisie commita i kontrola w hooku, że commit danej roli zmienia tylko dozwolone pliki (np. weryfikator: verification.md, corrections.md, pliki generowane). Mocniejsze niż E9, bo wiąże commit z rolą, a nie tylko z treścią.
Wróć, gdy: w pilocie weryfikator mimo karty zmieni plik produktu (kryterium 3) albo E9 okaże się za słabe.

### Pełna tabela ról i odpowiedzialności (Q-07)
Wszystkie role normy (CUS, PJM, TL, AN, DES, PR, TES, WT) przypisane do osób i zadań PM/SI, kto wykonuje, kto zatwierdza (macierz w stylu RACI).
Wróć, gdy: do projektu dołącza druga osoba albo zewnętrzny klient.

## Warunki pilota (Q-03)

1. Weryfikator w osobnej sesji, mając tylko repozytorium, kartę i listy kontrolne, przegląda 10 wymagań uznanych przez autora za gotowe i znajduje co najmniej jedną usterkę, którą Użytkownik potwierdza. Brak usterek oznacza, że przy tej skali rozdział ról się nie opłaca.
2. Użytkownik odrzuca najwyżej jedno na trzy zgłoszenia.
3. Zero zmian w plikach produktów z sesji weryfikatora.
4. Weryfikator zaczyna pracę bez pytań o kontekst albo z najwyżej dwoma.

Wynik pilota zapisuje się w projekcie pilotażowym jako kamień milowy z tymi kryteriami (`acceptance_criteria`) i rekord ACC; w szablonie jako decyzję zamykającą Q-03.
