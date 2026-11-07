# F5 — odczyt trwałej symulacji

Role, wyniki i decyzje są fikcyjne. Każde wywołanie uruchamia nową JVM.

# SYMULACJA — zmiana wymagania

Instancja: 7 · wersja stanu: 7

Poprzednia instancja: brak

Propozycja: CAP-01@2 · TextStats: myślnik rozdziela słowa; biało-czerwony daje 2.

Upoważnienie do zastosowania tej propozycji: brak aktywnego upoważnienia

Odbiór: przyjęto w fabule; accept

## Bieżące rewizje i kontrole

Kontrole odnoszą się do bieżących rewizji poniżej. Nie potwierdzają jeszcze niezastosowanej propozycji.

- AT-01@3: Przypadek: biało-czerwony; oczekiwane 2.
- CAP-01@2: TextStats: myślnik rozdziela słowa; biało-czerwony daje 2.
- CODE-01@3: Fikcyjna wersja programu 3; nie uruchamiamy TextStats w tej próbie.

- requirementReview: PASSED
- testReview: PASSED
- testExecution: PASSED

## Oczekujące zadania

Brak aktywnych zadań. Zakończenie bez odbioru nie oznacza przyjęcia.

## Kandydaci wpływu (doradczo)

- CAP-01 → AT-01

## Historia zadań z silnika

- authorize · 14 · zakończono
- impact · 2508 · zakończono
- prepare · 2517 · zakończono
- assess · 2525 · zakończono
- prepare · 5014 · zakończono
- assess · 7507 · zakończono
- accept · 7521 · zakończono

## Polecenia (kolejność wersji stanu)

- v1 · authorize · OPERATOR · ALLOW · Zgoda w fikcyjnym scenariuszu
- v2 · apply · AGENT · APPLY · Wpływ na AT-01
- v3 · prepare-2 · AGENT · PREPARE · Fikcyjna poprawka testu/programu
- v4 · fail · AGENT · ASSESS · Fikcyjne oceny, bez uruchomienia TextStats
- v5 · prepare-3 · AGENT · PREPARE · Fikcyjna poprawka testu/programu
- v6 · pass · AGENT · ASSESS · Fikcyjne oceny, bez uruchomienia TextStats
- v7 · accept · OPERATOR · ACCEPT · FIKCYJNY odbiór, nie decyzja użytkownika

## Zachowane oceny i wykonania

- baseCap · CAP-01@1 · [] · PASS
- baseTest · AT-01@1 · [CAP-01@1] · PASS
- failed-cap · CAP-01@2 · [] · PASS
- failed-test · AT-01@2 · [CAP-01@2] · FAIL
- passed-cap · CAP-01@2 · [] · PASS
- passed-test · AT-01@3 · [CAP-01@2] · PASS
- baseRun · AT-01@1 / CODE-01@1 · PASS
- failed-run · AT-01@2 / CODE-01@2 · PASS
- passed-run · AT-01@3 / CODE-01@3 · PASS

---

# SYMULACJA — zmiana wymagania

Instancja: 10007 · wersja stanu: 0

Poprzednia instancja: 7

Propozycja: CAP-01@3 · TextStats: myślnik i spacja nierozdzielająca rozdzielają słowa; oba przykłady dają 2.

Upoważnienie do zastosowania tej propozycji: brak aktywnego upoważnienia

Odbiór: brak

## Bieżące rewizje i kontrole

Kontrole odnoszą się do bieżących rewizji poniżej. Nie potwierdzają jeszcze niezastosowanej propozycji.

- AT-01@3: Przypadek: biało-czerwony; oczekiwane 2.
- CAP-01@2: TextStats: myślnik rozdziela słowa; biało-czerwony daje 2.
- CODE-01@3: Fikcyjna wersja programu 3; nie uruchamiamy TextStats w tej próbie.

- requirementReview: PASSED
- testReview: PASSED
- testExecution: PASSED

## Oczekujące zadania

- authorize · Zgoda na konkretną propozycję · OPERATOR · ID 10014

## Kandydaci wpływu (doradczo)

- CAP-01 → AT-01

## Historia zadań z silnika

- authorize · 10014 · oczekuje

## Polecenia (kolejność wersji stanu)


## Zachowane oceny i wykonania

- baseCap · CAP-01@1 · [] · PASS
- baseTest · AT-01@1 · [CAP-01@1] · PASS
- failed-cap · CAP-01@2 · [] · PASS
- failed-test · AT-01@2 · [CAP-01@2] · FAIL
- passed-cap · CAP-01@2 · [] · PASS
- passed-test · AT-01@3 · [CAP-01@2] · PASS
- baseRun · AT-01@1 / CODE-01@1 · PASS
- failed-run · AT-01@2 / CODE-01@2 · PASS
- passed-run · AT-01@3 / CODE-01@3 · PASS
