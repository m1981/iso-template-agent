# Wynik ograniczonej próby P3

2026-11-08 · A-24 · **wykonane technicznie, bez odbioru U i bez wdrożenia API**.

## Wniosek dla operatora

Możemy mechanicznie rozdzielić zapis starego wyniku, jego zastosowanie do bieżącej pracy i odbiór. W określonych niżej granicach TLC nie znalazło naruszeń V1–V8; znalazło legalne przebiegi i wykryło każde z sześciu celowych uszkodzeń. Nie jest to dowód poprawności produktu, całego ISO, rzeczywistych logów ani transakcyjności bazy.

**Wykonano 58 uruchomień TLC:** 26 konfiguracji bezpieczeństwa bez naruszeń; 26 świadków osiągalności; 6 mutacji z oczekiwanym naruszeniem właściwej kontroli. **8/8 testów runnera** przechodzi, w tym odmowa zaliczenia samego niezerowego kodu, złej własności, błędu parsera, braku śladu i przeżycia mutanta. Nie deklarujemy TDD implementacji produktu: to sprawdzanie specyfikacji i czułości jej kontroli.

Źródła: [kontrakt P3](../worked-transition.md#11-p3--zapis-spóźnionego-wyniku-po-zmianie-podstawy), [mapa](../p3-formal-map.md), [model](P3.tla), [konfiguracje](cases.json). Dowód: [podsumowanie](evidence/final/summary.json), [pełne logi i cfg](evidence/final/runs.jsonl), [testy runnera](evidence/runner-tests.log). Pliki w evidence/final odpowiadają SHA-256 z podsumowania; zgodność z bieżącymi źródłami sprawdzono po wykonaniu. Nie opieramy wyniku na zachowaniu katalogów tymczasowych.

## Granice wyniku

- Każda konfiguracja eksploruje przeploty jej workloadu od Init do horyzontu **8 akcji**. To nie jest wyłącznie odtworzenie z góry ustalonej kolejności; świadków nie użyto do filtrowania Next. TLC raportuje również wygenerowaną granicę grafu; nie rozszerzamy gwarancji na przebiegi poza horyzontem.
- Dwie zarejestrowane próby, jeden projekt/klient/kryterium, do trzech kluczy, jedna zmiana kontekstu. Stałe pochodzenie/metadane i warianty błędów na konfigurację; uprawnienie może zostać odwołane w osobnym wariancie. Nie jest to pełny iloczyn wszystkich błędów wejść, wszystkich aktorów i dowolnej liczby zmian.
- Wersja zlecenia/wymagania/testu/kodu/kryteriów jest krotką symbolicznych ID; przy zmianie samych kryteriów pierwsze cztery pola pozostają identyczne. Projekt/klient w przestrzeni klucza są stałe; nie sprawdzono izolacji wielu tenantów.
- Użyto `CONSTRAINT WithinHorizon`, bez ograniczania warunków biznesowych budżetem. `CHECK_DEADLOCK FALSE`: nie dowiedziono braku zakleszczeń ani postępu. Nie ma fairness, dowodu indukcyjnego, redukcji uzasadniającej wszystkie rozmiary ani testu implementacji.
- O3 ma atomowy skutek. Awaria przed zapisem i utrata odpowiedzi po nim są sprawdzone w abstrakcji; awarie pomiędzy realnymi zapisami wymagają testów magazynu. E1–E4 z mapy pozostają założeniami: tożsamość/pochodzenie, rzetelność dowodu, atomowość/trwałość, trafność analizy wpływu.
- Zliczanie wyników oraz porównanie ID jest mechaniczne. Uznanie starego defektu za istotny i zastosowanie do nowej podstawy dostarcza środowisko; model sprawdza widoczność tej informacji. `Credit` nie jest odbiorem ani pełną gotowością przyrostu.

Pakiet narzędzi: tla2tools release **1.7.4**, silnik **TLC2 2.19**, lokalny Temurin **17.0.21+9**; jeden worker, seed 1, fingerprint 0, sterta 512 MiB, timeout 60 s/próba. Zero timeoutów w końcowej serii. TLC stosuje fingerprinty stanów; wynik nie jest dowodem dedukcyjnym. Odtworzenie i źródła narzędzi: [README](README.md#odtworzenie).

## T01–T12: rzeczywiście wykonane

Dla każdego wiersza: bazowa kontrola V1–V8 bez naruszeń oraz osobne naruszenie `NotGoal`, którego ślad potwierdza osiągalność oczekiwania. Liczby stanów są lokalne dla konfiguracji; nie sumujemy ich jako unikalnych stanów całego procesu. Kroki nie obejmują Init.

| Przypadek | Sprawdzona obserwacja | Odrębne stany kontroli bazowej | Kroki świadka |
| --- | --- | ---: | ---: |
| T01 | stary wynik zapisany bez zaliczenia nowej podstawy | 165 | 3 |
| T02 | odmowa → dostarczenie → nowe żądanie/token → zapis | 15205 | 6 |
| T03 | log starej próby nie przypisuje się nowej | 131 | 2 |
| T04 | nieznane wykonanie odrzucone | 131 | 2 |
| T05 | zmiana samych kryteriów nie przenosi pass | 165 | 3 |
| T06 | utrata odpowiedzi po zapisie → identyczny replay | 165 | 5 |
| T07 | konkurujące żądania: jeden wynik i odmowa zamkniętej próby | 15205 | 4 |
| T08 | przerwanie przed zapisem → retry → zapis | 165 | 4 |
| T09 | zapis przy nieznanym bieżącym kontekście bez zaliczenia | 165 | 3 |
| T10 | deklaracja bez pochodzenia odrzucona | 105 | 2 |
| T11 | bieżący pass zachowany po starym pass | 16015 | 5 |
| T12 | bieżący pass nie ukrywa starego istotnego fail | 16015 | 5 |

Dodatkowe 14 konfiguracji: kolizja klucza z inną treścią, brak uprawnienia, odwołanie uprawnienia przed replay, niedozwolone pola, brak źródła, brak podstawy, inne kryterium, sprzeczność outcome z raportem, niewłaściwy projekt, niezwiązana zmiana, fail, inconclusive oraz wpływ applies/not_applicable. Każda ma bazę i osiągalny świadek. To symboliczne warianty adaptera, nie testy realnego logowania lub systemu plików.

## Czułość: błędy, które model wykrył

Mutacje włącza stała `Mutation`; bazowe konfiguracje zawsze mają `none`. Dla mutanta włączono jego konkretną kontrolę, aby ogólna wcześniejsza porażka nie maskowała nieskuteczności właściwego sprawdzenia.

| Mutacja | Naruszona własność | Kroki do kontrprzykładu |
| --- | --- | ---: |
| latest_basis | `V1_TypedAndBound` | 3 |
| omit_criteria | `V6_NoFalseCredit` | 3 |
| token_before_replay | `V4_ReplayStable` | 5 |
| duplicate_result | `V3_SingleCompletion` | 4 |
| auto_accept | `V2_HistoryPreserved` | 2 |
| hide_old_finding | `V8_NoHiddenFinding` | 3 |

Przykład rzeczywistego śladu `mutant-token_before_replay`:

1. Żądanie ma token 0.
2. Zapis wyniku tworzy potwierdzenie i podnosi token do 1.
3. Odpowiedź ginie.
4. Klient ponawia identyczne żądanie z tokenem 0.
5. Błędna kolejność sprawdza token przed potwierdzeniem i zwraca CONFLICT. Narusza V4: powinno wrócić poprzednie potwierdzenie.

W bazowym `witness-T06` ten sam rodzaj sytuacji kończy się poprawnym replay, bez drugiego wyniku. To konkretny argument za kolejnością kontroli, nie obietnica obsługi wszystkich awarii sieci.

## Korekty i przegląd własnej pracy

**Istotny defekt pierwszego modelu:** zapis `monitor' = monitor /\ property` został potraktowany jako koniunkcja warunków akcji; nie obserwował naruszenia. Cztery z sześciu mutantów przechodziły, ponieważ błędne przejścia znikały. Poprawka `monitor' = (monitor /\ property)` zachowuje przejście i zapisuje fałsz. Po poprawce wszystkie sześć mutacji wykrywa właściwa kontrola. Dlatego nie wystarczy raport „niezmienniki zielone”.

Ślad odtworzenia: [development.zip](evidence/development.zip), katalog `development-05` zawiera zgodne sumy źródeł i wyniki 4 przeżyłych mutacji; końcowa wersja i wyniki leżą w evidence/final. Pozostałe próby rozwojowe nie zastępują końcowego wyniku. Drobne błędy składni/inicjalizacji/sentinel oraz blokada lokalnego RMI przez sandbox zostały usunięte/obsłużone; nie policzono ich jako wykrycia błędu procesu.

W przeglądzie autora wzmocniono świadków: T02 wymaga dostarczenia odmowy, następnie nowego żądania z odświeżonym tokenem; T06 utraty odpowiedzi udanego zapisu; T08 zapisu po przerwaniu; T09 zapisu podczas braku bieżącego kontekstu. Obecność zdarzeń w dowolnej kolejności nie była wystarczającym oczekiwaniem.

Techniczne odwzorowanie mapy: M1 jako stała funkcja podstaw prób; M2 jako sekwencja wyników i phase (dopuszcza wykrywalny mutant duplikacji zamiast wykluczać go samym typem mapy); M3–M6 w rekordzie s; M7 jako jawny parametr danej konfiguracji. `seen`, `refreshed` i monitory są obserwatorami badania, nie nowymi rejestrami produktu. Retencja receipts, import dowodów, start prób, decyzja operatora i rozstrzyganie sporów nie zostały dopisane do zakresu.

Ocena zgodności z kontraktem: **przegląd autora**, bez osobnej sesji recenzenta. Niezależne są zapisane oczekiwania względem funkcji `Reason`, nie osoba autora. Mutacje zwiększają czułość badania, nie zapewniają niezależności rozumowania. Przed uznaniem modelu za wiążącą specyfikację pozostaje osobny przegląd znaczenia i decyzja o zmianie źródła specyfikacji.

## Praktyczny następny krok

Najpierw pokazać operatorowi jeden poprawny ślad i odpowiadający mu kontrprzykład: co system zapamiętał, dlaczego nie żąda odbioru oraz co robi agent. Właściciel przygotowania: agent. Dopiero po sprawdzeniu zrozumiałości dobrać testy zgodności do wybranej implementacji; ta próba nie uruchamia nowego API, pilota Kitchen ani prac drugiego repo.

Otwarte przed wdrożeniem Q1/Q3/Q4 (identyfikacja podstawy, pochodzenie, trwałość) pozostają w kontrakcie odbioru; właściciel przygotowania agent, decyzje operatora w zakresie ryzyka/źródła prawdy. Nie są przeszkodą w odczytaniu tego wyniku. W5, delegowanie i historyczne odbiory bez zmian. Bez commita/pushu.
