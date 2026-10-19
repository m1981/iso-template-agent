# Rekord postępu

Plik generowany przez tools/progress.py z plan.md, rekordów, stanów produktów i tagów git; nie edytuj ręcznie (ISO/IEC 29110 WP.09).

Zadania: 10 · planned 6 · in_progress 0 · completed 4

## Kamienie milowe

| Kamień | Cel | Termin | Tag | Osiągnięty | Akceptacja |
| --- | --- | --- | --- | --- | --- |
| MS-01 Wydanie v1.0.0 | OBJ-01 | 2026-11-30 | v1.0.0 | nie | — |

## Zadania: planowane i rzeczywiste

| Zadanie | Kamień | Status | Termin | Zakończono | Produkuje | Produkty według stanu |
| --- | --- | --- | --- | --- | --- | --- |
| TSK-01 Wymagania szablonu ze źródłami w decyzjach | MS-01 | completed | — | 2026-10-19 | REQ, G | initiated 82 |
| TSK-02 Katalog testów akceptacyjnych z runner: i raport testów | MS-01 | completed | — | 2026-10-19 | AT | initiated 52 |
| TSK-03 Złoty wzorzec wyjść narzędzi przed przeniesieniem | MS-01 | completed | — | 2026-10-19 | VER | brak elementów |
| TSK-04 Kontrole check_refs.py i check_leak.py w make check | MS-01 | completed | — | 2026-10-19 | LAY-03, LEK-01, LEK-02 | initiated 3 |
| TSK-05 Przeniesienie na trzy warstwy według mapy (D-54) | MS-01 | planned | — | — | LAY-01, LAY-02 | initiated 2 |
| TSK-06 Weryfikacja przeniesienia: złoty wzorzec, niezmienniki, odwołania | MS-01 | planned | — | — | VER | brak elementów |
| TSK-07 Migracje: MIGRATIONS.md i ostrzeżenie migrated_to | MS-01 | planned | — | — | MIG-01, MIG-02 | initiated 2 |
| TSK-08 Pilot: gtd2 z szablonu przez copier i migracja nazw z D-17 | MS-01 | planned | — | — | VAL | brak elementów |
| TSK-09 Próbne wydanie v1.0.1 i aktualizacja gtd2 przez bramkę | MS-01 | planned | — | — | VER | brak elementów |
| TSK-10 Niezależny przegląd plików procesu w sesji weryfikatora | MS-01 | planned | — | — | VER | brak elementów |

## Ryzyka projektu

| Ryzyko | Status | Dotyczy | Działanie |
| --- | --- | --- | --- |
| PRK-01 Przeniesienie gubi zależność, której nie widać w testach | open | TSK-05 | złoty wzorzec, check_refs.py i mapa sprawdzana skryptem przed i po przeniesieniu (D-61) |
| PRK-02 Treść projektu klienta przecieka do procesu | open | TSK-08 | check_leak.py w make check i lista TPL przy przeglądzie rejestru (D-62) |

## Korekty niezakończone (WP.04)

| Korekta | Status | Przyczyna | Działanie |
| --- | --- | --- | --- |

## Stan produktów pracy

| Typ | ISO | initiated | verified | approved |
| --- | --- | --- | --- | --- |
| G Pojęcie słownika | WP.13 | 26 | 0 | 0 |
| REQ Wymaganie EARS | WP.13 | 56 | 0 | 0 |
| AT Test akceptacyjny | WP.19 | 52 | 0 | 0 |
