# F5 — odczyt trwałej symulacji

Role, wyniki i decyzje są fikcyjne. Każde wywołanie uruchamia nową JVM.

# SYMULACJA — zmiana wymagania

Instancja: 7 · wersja stanu: 0

Poprzednia instancja: brak

Propozycja: CAP-01@2 · TextStats: myślnik rozdziela słowa; biało-czerwony daje 2.

Upoważnienie do zastosowania tej propozycji: brak aktywnego upoważnienia

Odbiór: brak

## Bieżące rewizje i kontrole

Kontrole odnoszą się do bieżących rewizji poniżej. Nie potwierdzają jeszcze niezastosowanej propozycji.

- AT-01@1: Przypadek: biało-czerwony; nadal oczekiwane 1 (do oceny wobec nowego wymagania).
- CAP-01@1: TextStats: biało-czerwony liczymy jako jedno słowo.
- CODE-01@1: Fikcyjna wersja programu 1; nie uruchamiamy TextStats w tej próbie.

- requirementReview: PASSED
- testReview: PASSED
- testExecution: PASSED

## Oczekujące zadania

- authorize · Zgoda na konkretną propozycję · OPERATOR · ID 14

## Kandydaci wpływu (doradczo)

- CAP-01 → AT-01

## Historia zadań z silnika

- authorize · 14 · oczekuje

## Polecenia (kolejność wersji stanu)


## Zachowane oceny i wykonania

- baseCap · CAP-01@1 · [] · PASS
- baseTest · AT-01@1 · [CAP-01@1] · PASS
- baseRun · AT-01@1 / CODE-01@1 · PASS
