# Kontrakt lekcji TextStats I1

2026-10-24. Specyfikacja przed kodem. Zakres: [I1](increment-01.md), decyzja użytkownika D-79; szczegóły techniczne: decyzja agenta A6 w [rejestrze](progress.md).

Wszystkie produkty i wyniki lekcji są fikcyjne (`simulated`). ID są lokalne dla lekcji `textstats-i1`, wersja 1. Nie zapisujemy niczego do projektu TextStats ani do normy. Produktem jest informacja, przykładowy plik jest jej nośnikiem, R1 jest elementem specyfikacji, a WP.13 typem produktu. Odwołanie zawiera ID i rewizję; relację odwrotną wyliczamy.

## Przejścia i niezależne oczekiwania

| Polecenie | Podstawa | Powstaje / zmienia się | Oczekiwanie |
| --- | --- | --- | --- |
| scope | potrzeba N1 | zakres, słownik, R1/R1a/R2, pytanie Q1 | Brak kodu, wykonań i odbioru. |
| plan | wymagania | P1 — plan I1 | Plan poprzedza testy i kod. |
| design | wymagania | C1/C2 — kontrakty | Projekt można opracować przed albo po planie. |
| review | plan i kontrakty | V1 — fikcyjny przegląd | Nie udajemy niezależnego przeglądu. |
| tests | przegląd | T1–T5 — przypadki testowe | Zero wykonań. |
| red | przypadki, brak szkieletu | CODE1 r1, RUN1 (FAIL, T1–T4) | NotImplementedError; wynik dotyczy r1. |
| implement | RUN1 FAIL | CODE1 r2 | RUN1 pozostaje; brak wyniku r2. |
| unit | CODE1 r2 | RUN2 (PASS, T1–T4) | Jednostkowe GREEN nie sprawdza adaptera. |
| integrate | RUN2 PASS na aktualnym kodzie | CODE2 r1 | Brak wyniku T5. |
| integration | CODE1 r2 i CODE2 r1 | RUN3 (PASS, T5) | Plik → CLI → JSON; wejście niezmienione. |
| demo | aktualne RUN2/RUN3 | U1 — instrukcja, DEMO1 — demonstracja | Wynik przykładu; decyzja odbiorcza wciąż nie istnieje. |
| accept + powód | demonstracja bez nierozpatrzonej korekty | ACC1 — fikcyjny odbiór I1 | Q1 wciąż otwarte; brak zgody na wydanie. |
| reject + powód | demonstracja | DEC1 — odmowa, potrzeba korekty instrukcji | Przyczyna zachowana, brak ACC1. |
| clarify + opis korekty | odmowa | U1 kolejna rewizja | Korekta objaśnienia; nie zmienia kodu ani zakresu. |
| demo | poprawiona instrukcja | DEMO1 kolejna rewizja | Możliwy nowy odbiór albo kolejna odmowa. |

Ścieżka bazowa ma 12 poleceń: scope, plan, design, review, tests, red, implement, unit, integrate, integration, demo, accept. Alternatywna kolejność plan/design jest dozwolona. Korekta po odmowie dotyczy wyłącznie wyjaśnienia użycia (np. znaczenia słowa); inne powody wymagające zmiany zakresu są poza I1, interfejs mówi o tym jawnie. To wybór dydaktyczny, nie ogólna reguła odbiorów.

Odmowa nie zmienia żadnego rekordu. Powtórzone polecenia są odrzucane; powtórna demonstracja wymaga korekty. Odbiór kończy ćwiczenie. Historia jest niemutowalna; oglądanie przeszłości nie pozwala wydawać poleceń. Import odtwarza polecenia od początku i odrzuca nieznane pola/wersje/niedozwoloną kolejność. Zapis zawiera wersję formatu, lekcji, polecenia i kursor; nie przyjmuje gotowych raportów PASS.

## Pochodzenie treści i granice

- R1/R1a/R2, C1/C2, T1–T5, Q1, kolejność plan → RED → GREEN: [zdjęcie RED](../repository-evolution/01_increment_words_red.md), [zdjęcie GREEN](../repository-evolution/02_increment_words_green.md), tabele produktów i bloki kodu. Adaptacja dydaktyczna istniejącej lekcji; nie normatywna kolejność obowiązkowa dla każdego projektu.
- Rozdzielenie czynności i produktów: ISO 29110, [§5](../../../iso-29110-5-1/chapters/05-overview.md), procesy [PM](../../../iso-29110-5-1/chapters/06-project-management-pm-process.md) i [SI](../../../iso-29110-5-1/chapters/07-software-implementation-si-process.md), rysunki 3–4. Model lekcji wybiera mały wycinek przepływu, nie odtwarza całej normy.
- Typy produktów: [rozdział 9](../../../iso-29110-5-1/chapters/09-description-of-work-products.md), WP.10 plan, WP.13 wymagania, WP.16 projekt, WP.15 komponenty, WP.19 przypadki, WP.20 raport, WP.23 zapis weryfikacji, WP.18 instrukcja, WP.22 zapis walidacji, WP.01 zapis odbioru. Karty są fragmentami tych typów, nie kompletnymi produktami wymaganymi do zgodności.
- Potrzeba, słownik, pytanie i decyzja: lokalne informacje, bez wymuszania WP.02 lub WP.07. Wiązanie rewizji, lokalne ID, jawne polecenia, korekta instrukcji, format zapisu i blokada edycji przeszłości są własnymi regułami symulatora.

## Sprawdzenie

Testy oczekują powyższego przebiegu niezależnie od listy dostępnych akcji. Sprawdzają brak dowodu po samym zamiarze, odmowy i atomowość, zachowanie starego RED, dokładne rewizje wejść, odrzucenie odbioru bez demonstracji, korektę, odtwarzanie i błędny import. Testy transportu osobno sprawdzają konkurujące żądania i brak podmiany po błędzie. Kontrolowana mutacja omija wymagany przegląd przed przygotowaniem testów i musi spowodować błąd testu. Próba przeglądarkowa sprawdza działania człowieka i zgodność kart, grafu i historii; nie zastępuje próby edukacyjnej operatora.
