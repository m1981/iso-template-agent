Wygenerowano z usług Flowable podczas rzeczywistego testu F4. Role, oceny i odbiory są fikcyjne; program TextStats nie był uruchamiany.

# 1. Oczekiwanie na zgodę

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

---

# 2. Fail skierował pracę do poprawki

# SYMULACJA — zmiana wymagania

Instancja: 7 · wersja stanu: 4

Poprzednia instancja: brak

Propozycja: CAP-01@2 · TextStats: myślnik rozdziela słowa; biało-czerwony daje 2.

Upoważnienie do zastosowania tej propozycji: brak aktywnego upoważnienia

Odbiór: brak

## Bieżące rewizje i kontrole

Kontrole odnoszą się do bieżących rewizji poniżej. Nie potwierdzają jeszcze niezastosowanej propozycji.

- AT-01@2: Przypadek: biało-czerwony; nadal oczekiwane 1 (do oceny wobec nowego wymagania).
- CAP-01@2: TextStats: myślnik rozdziela słowa; biało-czerwony daje 2.
- CODE-01@2: Fikcyjna wersja programu 2; nie uruchamiamy TextStats w tej próbie.

- requirementReview: PASSED
- testReview: CORRECTION
- testExecution: PASSED

## Oczekujące zadania

- prepare · Przygotowanie testu i programu · AGENT · ID 56

## Kandydaci wpływu (doradczo)

- CAP-01 → AT-01

## Historia zadań z silnika

- authorize · 14 · zakończono
- impact · 24 · zakończono
- prepare · 33 · zakończono
- assess · 41 · zakończono
- prepare · 56 · oczekuje

## Polecenia (kolejność wersji stanu)

- v1 · command-2 · OPERATOR · ALLOW · Zgoda symulowanego operatora na CAP-01@2
- v2 · command-3 · AGENT · APPLY · Ocena wpływu: AT-01 wymaga rozliczenia
- v3 · command-4 · AGENT · PREPARE · Przygotowano nowy test i program w fabule
- v4 · command-5 · AGENT · ASSESS · Fikcyjne wyniki ocen i wykonania

## Zachowane oceny i wykonania

- baseCap · CAP-01@1 · [] · PASS
- baseTest · AT-01@1 · [CAP-01@1] · PASS
- demoFailcap · CAP-01@2 · [] · PASS
- demoFailtest · AT-01@2 · [CAP-01@2] · FAIL
- baseRun · AT-01@1 / CODE-01@1 · PASS
- demoFailrun · AT-01@2 / CODE-01@2 · PASS

---

# 3. Gotowe do decyzji, bez automatycznego odbioru

# SYMULACJA — zmiana wymagania

Instancja: 7 · wersja stanu: 6

Poprzednia instancja: brak

Propozycja: CAP-01@2 · TextStats: myślnik rozdziela słowa; biało-czerwony daje 2.

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

- accept · Odbiór konkretnej podstawy · OPERATOR · ID 78

## Kandydaci wpływu (doradczo)

- CAP-01 → AT-01

## Historia zadań z silnika

- authorize · 14 · zakończono
- impact · 24 · zakończono
- prepare · 33 · zakończono
- assess · 41 · zakończono
- prepare · 56 · zakończono
- assess · 64 · zakończono
- accept · 78 · oczekuje

## Polecenia (kolejność wersji stanu)

- v1 · command-2 · OPERATOR · ALLOW · Zgoda symulowanego operatora na CAP-01@2
- v2 · command-3 · AGENT · APPLY · Ocena wpływu: AT-01 wymaga rozliczenia
- v3 · command-4 · AGENT · PREPARE · Przygotowano nowy test i program w fabule
- v4 · command-5 · AGENT · ASSESS · Fikcyjne wyniki ocen i wykonania
- v5 · command-6 · AGENT · PREPARE · Przygotowano nowy test i program w fabule
- v6 · command-7 · AGENT · ASSESS · Fikcyjne wyniki ocen i wykonania

## Zachowane oceny i wykonania

- baseCap · CAP-01@1 · [] · PASS
- baseTest · AT-01@1 · [CAP-01@1] · PASS
- demoFailcap · CAP-01@2 · [] · PASS
- demoFailtest · AT-01@2 · [CAP-01@2] · FAIL
- demoPasscap · CAP-01@2 · [] · PASS
- demoPasstest · AT-01@3 · [CAP-01@2] · PASS
- baseRun · AT-01@1 / CODE-01@1 · PASS
- demoFailrun · AT-01@2 / CODE-01@2 · PASS
- demoPassrun · AT-01@3 / CODE-01@3 · PASS

---

# 4. Przyjęta pierwsza sprawa

# SYMULACJA — zmiana wymagania

Instancja: 7 · wersja stanu: 7

Poprzednia instancja: brak

Propozycja: CAP-01@2 · TextStats: myślnik rozdziela słowa; biało-czerwony daje 2.

Upoważnienie do zastosowania tej propozycji: brak aktywnego upoważnienia

Odbiór: przyjęto w fabule; command-8

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
- impact · 24 · zakończono
- prepare · 33 · zakończono
- assess · 41 · zakończono
- prepare · 56 · zakończono
- assess · 64 · zakończono
- accept · 78 · zakończono

## Polecenia (kolejność wersji stanu)

- v1 · command-2 · OPERATOR · ALLOW · Zgoda symulowanego operatora na CAP-01@2
- v2 · command-3 · AGENT · APPLY · Ocena wpływu: AT-01 wymaga rozliczenia
- v3 · command-4 · AGENT · PREPARE · Przygotowano nowy test i program w fabule
- v4 · command-5 · AGENT · ASSESS · Fikcyjne wyniki ocen i wykonania
- v5 · command-6 · AGENT · PREPARE · Przygotowano nowy test i program w fabule
- v6 · command-7 · AGENT · ASSESS · Fikcyjne wyniki ocen i wykonania
- v7 · command-8 · OPERATOR · ACCEPT · Fikcyjny odbiór w scenariuszu testowym

## Zachowane oceny i wykonania

- baseCap · CAP-01@1 · [] · PASS
- baseTest · AT-01@1 · [CAP-01@1] · PASS
- demoFailcap · CAP-01@2 · [] · PASS
- demoFailtest · AT-01@2 · [CAP-01@2] · FAIL
- demoPasscap · CAP-01@2 · [] · PASS
- demoPasstest · AT-01@3 · [CAP-01@2] · PASS
- baseRun · AT-01@1 / CODE-01@1 · PASS
- demoFailrun · AT-01@2 / CODE-01@2 · PASS
- demoPassrun · AT-01@3 / CODE-01@3 · PASS

---

# 5. Nowa sprawa nie odnawia starych ocen i nie zmienia wcześniejszego odbioru

# SYMULACJA — zmiana wymagania

Instancja: 89 · wersja stanu: 3

Poprzednia instancja: 7

Propozycja: CAP-01@3 · TextStats: myślnik i spacja nierozdzielająca rozdzielają słowa; oba przykłady dają 2.

Upoważnienie do zastosowania tej propozycji: brak aktywnego upoważnienia

Odbiór: brak

## Bieżące rewizje i kontrole

Kontrole odnoszą się do bieżących rewizji poniżej. Nie potwierdzają jeszcze niezastosowanej propozycji.

- AT-01@4: Przypadki: biało-czerwony i dwa słowa ze spacją nierozdzielającą; oczekiwane 2.
- CAP-01@3: TextStats: myślnik i spacja nierozdzielająca rozdzielają słowa; oba przykłady dają 2.
- CODE-01@4: Fikcyjna wersja programu 4; nie uruchamiamy TextStats w tej próbie.

- requirementReview: REVIEW_REQUIRED
- testReview: REVIEW_REQUIRED
- testExecution: REVIEW_REQUIRED

## Oczekujące zadania

- assess · Przeglądy i wynik wykonania · AGENT · ID 123

## Kandydaci wpływu (doradczo)

- CAP-01 → AT-01

## Historia zadań z silnika

- authorize · 96 · zakończono
- impact · 106 · zakończono
- prepare · 115 · zakończono
- assess · 123 · oczekuje

## Polecenia (kolejność wersji stanu)

- v1 · command-9 · OPERATOR · ALLOW · Zgoda w fabule na nową propozycję
- v2 · command-10 · AGENT · APPLY · Nowa ocena wpływu
- v3 · command-11 · AGENT · PREPARE · Przygotowano nowy test i program w fabule

## Zachowane oceny i wykonania

- baseCap · CAP-01@1 · [] · PASS
- baseTest · AT-01@1 · [CAP-01@1] · PASS
- demoFailcap · CAP-01@2 · [] · PASS
- demoFailtest · AT-01@2 · [CAP-01@2] · FAIL
- demoPasscap · CAP-01@2 · [] · PASS
- demoPasstest · AT-01@3 · [CAP-01@2] · PASS
- baseRun · AT-01@1 / CODE-01@1 · PASS
- demoFailrun · AT-01@2 / CODE-01@2 · PASS
- demoPassrun · AT-01@3 / CODE-01@3 · PASS
