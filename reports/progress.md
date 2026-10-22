# Rekord postępu

Plik generowany przez process/tools/progress.py z project/plan.md, rekordów, stanów produktów i tagów git; nie edytuj ręcznie (ISO/IEC 29110 WP.09).

Zadania: 10 · planned 5 · in_progress 1 · completed 4

## Kamienie milowe

| Kamień | Cel | Termin | Tag | Osiągnięty | Akceptacja |
| --- | --- | --- | --- | --- | --- |
| MS-01 Wydanie v1.0.0 | OBJ-01 | 2026-11-30 | v1.0.0 | nie | — |

## Zadania: planowane i rzeczywiste

| Zadanie | Kamień | Status | Termin | Zakończono | Produkuje | Produkty według stanu |
| --- | --- | --- | --- | --- | --- | --- |
| TSK-01 Wymagania szablonu ze źródłami w decyzjach | MS-01 | completed | — | 2026-10-19 | REQ, G | initiated 83 |
| TSK-02 Katalog testów akceptacyjnych z runner: i raport testów | MS-01 | completed | — | 2026-10-19 | AT | initiated 55 |
| TSK-03 Złoty wzorzec wyjść narzędzi przed przeniesieniem | MS-01 | completed | — | 2026-10-19 | VER | brak elementów |
| TSK-04 Kontrole check_refs.py i check_leak.py w make check | MS-01 | completed | — | 2026-10-19 | LAY-03, LEK-01, LEK-02 | initiated 3 |
| TSK-05 Przeniesienie na trzy warstwy według mapy (D-54) | MS-01 | in_progress | — | — | LAY-01, LAY-02 | initiated 2 |
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
| REQ Wymaganie EARS | WP.13 | 57 | 0 | 0 |
| AT Test akceptacyjny | WP.19 | 55 | 0 | 0 |

## Kryteria odbioru

| Element | Kryteria |
| --- | --- |
| MS-01 Wydanie v1.0.0 | AC-1 każde wymaganie szablonu ma co najmniej jeden test, który przechodzi (raport testów i trace.md bez wymagań bez testu) · AC-2 make test i make test-distribution przechodzą na Linuksie (Python 3.13) i na Macu (Python 3.10) · AC-3 każdą kontrolę bramek łapie test po jej wyłączeniu (lista mutantów w rekordzie VER) · AC-4 przeniesienie: złoty wzorzec identyczny, niezmienniki spełnione, check_refs.py bez błędów (rekord VER) · AC-5 gtd2 założony przez copier, migracja nazw z D-17 zakończona, make check czyste, migrated_to ustawione (rekord VAL Użytkownika) · AC-6 próbne wydanie v1.0.1 dochodzi do gtd2 przez bramkę bez zmiany plików projektu (rekord VER) · AC-7 nowy projekt od pustego katalogu do pierwszego baseline'u według README bez pytań o kontekst spoza repozytorium (rekord VAL Użytkownika) · AC-8 brak przecieku domeny: check_leak.py przechodzi w gtd2, przegląd rejestru szablonu według listy TPL (rekord VER) · AC-9 restore-check przechodzi, a tag v1.0.0 stoi na przetestowanym commicie (rekord VER) |
| TSK-05 Przeniesienie na trzy warstwy według mapy (D-54) | K-1 każdy śledzony plik jest tam, gdzie wskazuje reference/layout-map.md, i nic nie leży poza mapą (skrypt pokrycia przed i po) · K-2 nic nie zginęło: liczba plików po równa liczbie przed powiększonej o nowe pliki z części 4 mapy, wycofane narzędzia w archive/ · K-3 treść przeniesionych dokumentów bajt w bajt taka sama poza zmianami ścieżek wypisanymi w mapie · K-4 git log --follow każdego pliku sięga sprzed przeniesienia · K-5 make golden bez różnic po usunięciu prefiksów katalogów · K-6 ślad warstwy procesu liczony wprost: 0 błędów i tyle samo elementów co w widoku przed przeniesieniem, process_kit_view.py w archive/ · K-7 na prawdziwym template/: copier copy, init.py, make check i pierwszy commit przez hooki; aktualizacja do próbnej wersji nie zmienia plików projektu · K-8 LAY-01 i LAY-02 mają testy automatyczne, które przechodzą · K-9 w template/ nie ma plików warstwy procesu, a check_leak.py przechodzi na template/process/ · K-10 zbędne wyjątki check_refs usunięte, check_refs bez błędów · K-11 K-1…K-10 na Linuksie (Python 3.13) i na Macu (Python 3.10) |
