# Plan warstwy procesu

Plan prac nad samym szablonem procesu (D-48, D-63), w formacie planu projektu (ISO/IEC 29110 WP.10). Do przeniesienia (D-54) leży w docelowym miejscu, a ślad i postęp liczy dla niego `make process-kit`.

## Produkt i zakres
Szablon procesu człowiek + agent wzorowany na ISO/IEC 29110-5-1-2 Basic, dostarczany do projektów przez copier (D-43, D-47). Wymagania: spec/requirements.md. Pierwszy projekt: gtd2 jako pilot (Q-03).

## Cykl wytwarzania
Przyrostowo: każda zmiana przez rejestr decyzji, commit z ID i kontrole; wydania vX.Y.Z z przetestowanego commita (D-49).

## Zespół i zasoby
Użytkownik (klient, decyzje kierownika projektu, walidacja i odbiór); sesja autora; sesja weryfikatora (roles/verifier.md). Narzędzia: git, python3 (3.10 na Macu, 3.13 w kopii agenta), copier 9.19.1.

## Wersjonowanie i dostarczenie
- repozytorium: github.com/m1981/iso-template-agent (D-13), push z tagami
- etapy pracy nad procesem: tagi baseline-nn; wydania: tagi vX.Y.Z, nigdy na tym samym commicie (D-49)
- dostarczenie: copier copy i copier update z jawną wersją; aktualizacja projektu przez make process-update (D-52)

## Cele

### OBJ-01 Szablon gotowy do użycia w projektach
- measure: wydanie v1.0.0 odebrane przez Użytkownika (rekord ACC) po pilocie na gtd2

## Kamienie milowe

### MS-01 Wydanie v1.0.0
- objective: OBJ-01
- due: 2026-11-30
- tag: v1.0.0
- acceptance_criteria: AC-1 każde wymaganie szablonu ma co najmniej jeden test, który przechodzi (raport testów i trace.md bez wymagań bez testu) · AC-2 make test i make test-distribution przechodzą na Linuksie (Python 3.13) i na Macu (Python 3.10) · AC-3 każdą kontrolę bramek łapie test po jej wyłączeniu (lista mutantów w rekordzie VER) · AC-4 przeniesienie: złoty wzorzec identyczny, niezmienniki spełnione, check_refs.py bez błędów (rekord VER) · AC-5 gtd2 założony przez copier, migracja nazw z D-17 zakończona, make check czyste, migrated_to ustawione (rekord VAL Użytkownika) · AC-6 próbne wydanie v1.0.1 dochodzi do gtd2 przez bramkę bez zmiany plików projektu (rekord VER) · AC-7 nowy projekt od pustego katalogu do pierwszego baseline'u według README bez pytań o kontekst spoza repozytorium (rekord VAL Użytkownika) · AC-8 brak przecieku domeny: check_leak.py przechodzi w gtd2, przegląd rejestru szablonu według listy TPL (rekord VER) · AC-9 restore-check przechodzi, a tag v1.0.0 stoi na przetestowanym commicie (rekord VER)
- notes: tag v1.0.0 dopiero po rekordzie ACC Użytkownika (D-63); termin to założenie do potwierdzenia (rejestr, D-64)

## Zadania

### TSK-01 Wymagania szablonu ze źródłami w decyzjach
- milestone: MS-01
- produces: REQ, G
- status: completed
- completed: 2026-10-19

### TSK-02 Katalog testów akceptacyjnych z runner: i raport testów
- milestone: MS-01
- produces: AT
- status: completed
- completed: 2026-10-19

### TSK-03 Złoty wzorzec wyjść narzędzi przed przeniesieniem
- milestone: MS-01
- produces: VER
- notes: pliki wzorca w reference/golden/; rekord VER powstaje przy porównaniu po przeniesieniu (TSK-06)
- status: completed
- completed: 2026-10-19

### TSK-04 Kontrole check_refs.py i check_leak.py w make check
- milestone: MS-01
- produces: LAY-03, LEK-01, LEK-02
- status: completed
- completed: 2026-10-19

### TSK-05 Przeniesienie na trzy warstwy według mapy (D-54)
- milestone: MS-01
- produces: LAY-01, LAY-02
- status: planned

### TSK-06 Weryfikacja przeniesienia: złoty wzorzec, niezmienniki, odwołania
- milestone: MS-01
- produces: VER
- status: planned

### TSK-07 Migracje: MIGRATIONS.md i ostrzeżenie migrated_to
- milestone: MS-01
- produces: MIG-01, MIG-02
- status: planned

### TSK-08 Pilot: gtd2 z szablonu przez copier i migracja nazw z D-17
- milestone: MS-01
- produces: VAL
- status: planned

### TSK-09 Próbne wydanie v1.0.1 i aktualizacja gtd2 przez bramkę
- milestone: MS-01
- produces: VER
- status: planned

### TSK-10 Niezależny przegląd plików procesu w sesji weryfikatora
- milestone: MS-01
- produces: VER
- status: planned

## Ryzyka projektu

### PRK-01 Przeniesienie gubi zależność, której nie widać w testach
- concerns: TSK-05
- status: open
- mitigation: złoty wzorzec, check_refs.py i mapa sprawdzana skryptem przed i po przeniesieniu (D-61)

### PRK-02 Treść projektu klienta przecieka do procesu
- concerns: TSK-08
- status: open
- mitigation: check_leak.py w make check i lista TPL przy przeglądzie rejestru (D-62)
