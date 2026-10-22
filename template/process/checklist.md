# Listy kontrolne przeglądu

Kryteria, według których przegląda się produkty pracy (ISO/IEC 29110 WP.23: „verification checklist”). Rekord weryfikacji wskazuje użytą listę w polu `checklist:` (kody sekcji, np. `REQ, UC`) i wypisuje niespełnione punkty w polu `failed:` (np. `REQ.3, REQ.5`); trace.py sprawdza, że takie punkty istnieją i że wynik `pass` nie ma niespełnionych punktów.

Punkty mówią, czego szukać; skrypty i tak sprawdzają format (EARS, słownik, ślad), więc listy dotyczą sensu. Kolejne punkty dopisuje się na końcu sekcji; numerów się nie zmienia ani nie używa ponownie, bo wskazują je rekordy.

## REQ Wymaganie

Źródło: SI.02.04 (poprawne, testowalne, kompletne, jednoznaczne, niesprzeczne), WP.13 (identyfikowalne, weryfikowalne, charakterystyki jakości).

- REQ.1 Poprawne: wynika ze źródła (`source:`) i mówi to, czego naprawdę potrzebuje Użytkownik.
- REQ.2 Testowalne: da się napisać test akceptacyjny z jednoznacznym wynikiem; wartości liczbowe mają jednostki i progi.
- REQ.3 Jednoznaczne: tylko jeden sposób odczytu; terminy pochodzą ze słownika i znaczą to, co w nim.
- REQ.4 Niesprzeczne: nie koliduje z innymi wymaganiami, zasadami projektowymi ani pozycjami Out zakresu.
- REQ.5 Kompletne: obejmuje warunki brzegowe; dla każdego „co, jeśli się nie uda” istnieje wymaganie unwanted (If …, then …).
- REQ.6 Atomowe: jedna potrzeba w jednym zdaniu; „i”, „oraz” łączące dwie potrzeby oznaczają dwa wymagania.
- REQ.7 Co, nie jak: nie narzuca rozwiązania (ekranu, technologii), chyba że to świadome ograniczenie (`quality: constraint`).
- REQ.8 Wykonalne w zakresie i planie projektu.
- REQ.9 Charakterystyka jakości przypisana albo świadomie pominięta (pole `quality:`).

## UC Przypadek użycia

Źródło: SI.02.02, SI.02.05 (potrzeby i oczekiwania, użyteczność); Cockburn.

- UC.1 Cel aktora głównego zwykłymi słowami, na właściwym poziomie (sea: jedna sesja, cel użytkownika).
- UC.2 Aktor główny jest pojęciem ze słownika.
- UC.3 Gwarancja minimalna i gwarancja sukcesu są zapisane i sprawdzalne.
- UC.4 Scenariusz główny ma 3–9 kroków, bez szczegółów interfejsu.
- UC.5 Każdy krok, który może się nie udać, ma rozszerzenie.
- UC.6 Wynika ze scenki albo pozycji In zakresu i nie wychodzi poza zakres.

## SC Scenka

Źródło: persona (rozdział 3, 3.17), SI.02.02 (konsultacja źródeł wymagań).

- SC.1 Konkretna osoba w konkretnej sytuacji, nie użytkownik „ogólnie”.
- SC.2 Każde zdanie wskazuje cel albo interes tej osoby.
- SC.3 Opisuje życie lub pracę osoby, nie funkcje systemu.

## IO Pozycja zakresu

- IO.1 Rodzaj In albo Out ma uzasadnienie.
- IO.2 Pozycja Out, która ogranicza system, ma wymaganie-ograniczenie.

## G Pojęcie słownika

Źródło: SI.02.04 (jednoznaczność).

- G.1 Definicja: rodzaj nadrzędny i cecha odróżniająca.
- G.2 Jeden termin ma jedno znaczenie w całej specyfikacji; brak synonimów bez wpisu.
- G.3 Definicja nie jest kołowa (nie używa definiowanego terminu).
- G.4 Angielska nazwa w nawiasie zgadza się z użyciem w wymaganiach EARS.

## DP Zasada projektowa

- DP.1 Da się sprawdzić w przeglądzie, czy produkt ją spełnia.
- DP.2 Wyjątki są zapisane przy zasadzie, z decyzją.

## RSK Ryzyko produktu

Źródło: załącznik D (identyfikacja i ocena ryzyk oprogramowania).

- RSK.1 Skutek dla Użytkownika jest konkretny.
- RSK.2 Ma co najmniej jedno wymaganie, które je ogranicza (zwykle unwanted).
- RSK.3 Ryzyka bezpieczeństwa (poufność, integralność, dostępność danych) zostały rozważone.

## AT Test akceptacyjny

Źródło: SI.03.06, SI.03.08 (zgodność testów z wymaganiami), WP.19.

- AT.1 Sprawdza dokładnie wymaganie wskazane w `verifies:`, a nie inne.
- AT.2 Given, When, Then z konkretnymi danymi wejściowymi.
- AT.3 Oczekiwany wynik jest obserwowalny i jednoznaczny.
- AT.4 Nie zależy od kolejności ani wyniku innych testów.

## E Ekran

Źródło: SI.03.03 (wygląd i zachowanie interfejsu), załącznik C (dostępność).

- E.1 Realizuje przypadek użycia wskazany w `realizes:`.
- E.2 Zawsze widać następny krok albo drogę powrotu.
- E.3 Dostępność: działa z klawiatury, ma czytelny kontrast i etykiety dla czytników ekranu.

## PLAN Plan projektu

Źródło: PM.01.13 (elementy planu wykonalne i spójne), WP.10.

- PLAN.1 Każdy cel ma miarę, a każdy kamień milowy termin i kryteria akceptacji.
- PLAN.2 Każde zadanie ma kamień i to, co wytwarza (`produces:`); weryfikacje i walidacje też są zadaniami.
- PLAN.3 Terminy są wykonalne przy zasobach z sekcji „Zespół i zasoby”.
- PLAN.4 Ryzyka projektu mają działania ograniczające.

## REPO Repozytorium i kopia zapasowa

Źródło: PM.02.06, PM.02.07 (sprawdzenie odtworzenia z kopii), WP.11, WP.12.

- REPO.1 Klon z kopii ma ten sam ostatni commit co repozytorium lokalne.
- REPO.2 Klon ma te same tagi baseline.
- REPO.3 W klonie kontrole śladu przechodzą bez błędów.

## TPL Rejestr i dokumenty szablonu

Źródło: D-57, D-62 (proces oddzielony od produktu klienta). Lista dla przeglądu rejestru i dokumentów w repozytorium szablonu, nie w projekcie.

- TPL.1 Decyzja dotyczy procesu albo szablonu, a nie produktu, który powstaje w projekcie.
- TPL.2 Treść nie zawiera pojęć, ID, zadań ani danych projektu klienta; przykłady używają ID zastępczych z „nn”.
- TPL.3 Wniosek z projektu (np. z pilota) jest zapisany jako potrzeba procesu ze wskazaniem źródła, bez przenoszenia treści dziedziny.
