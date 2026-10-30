# Plan i odbiór mapowania cyklu wydań

2026-10-29 · D-84, kontynuacja D-83 · zlecenie: „zapisz plan oraz kryteria odbioru a następnie przejdź do realizacji”. Plan zapisany przed opracowaniem mapowania i uruchomieniem nowych prób.

## Rezultat i granica

Przygotować sprawdzony kontrakt cyklu **odbiór v1 → zmiana → ponowna ocena → odbiór v2** na podstawie istniejącego modelu v0.7. Wynik ma pozwolić implementatorowi dalszego E3 wskazać operacje, ich warunki, skutki, odmowy i własności do zbadania, a operatorowi zrozumieć zachowanie procesu.

W zakresie: wszystkie W01–W07, związki z T/P i obserwatorami, legalny przebieg dwóch wydań, odmowy i powroty, mapa do przyszłej formalizacji oraz oddzielna recenzja. Nie rozszerzamy generatora TLA+, nie zmieniamy YAML ani reguł, nie wdrażamy API/CLI i nie zamykamy całego E3. To realizacja najbliższego kroku z [mapy pokrycia](coverage-map.md), nie wykonanie wszystkich późniejszych etapów.

Źródła: `iso-model-state/model/process.yaml`, `docs/WLASCIWOSCI.md`, `docs/INTERPRETACJE.md`, `PLAN.md`, wykonawca i istniejące scenariusze. Źródła normatywne pozostają wskazane w polach modelu; to mapowanie przyjętej interpretacji, nie nowa interpretacja wszystkich zadań ISO.

## Kolejność

| Krok | Działanie | Rezultat i zakończenie |
| --- | --- | --- |
| 1 | Ustalić wersję wejścia, odczytać W/T/P i wymagane dane dowodowe | Rozpoznany komplet warunków, łącznie z kontrolami wykonawcy poza guard |
| 2 | Zapisać kontrakty i oczekiwane przypadki przed ich uruchomieniem | `release-cycle.md`: W01–W07, przykład, odmowy, mapa S/L/F oraz granice |
| 3 | Odtworzyć scenariusze i przypadki na kopii źródeł | Trwały raport pełnych stanów i porównań; nieudana próba zachowana z przyczyną |
| 4 | Osobny recenzent sprawdza kontrakty, własne przypadki i dowody | Uwagi z rozstrzygnięciem; brak otwartej uwagi blokującej techniczne zakończenie mapowania |
| 5 | Rozliczyć poniższe kryteria i uaktualnić punkt wznowienia | Krótki raport; odbiór U pozostaje oddzielny |

## Kryteria odbioru tego pakietu

| ID | Warunek | Dowód |
| --- | --- | --- |
| RC-01 | Wszystkie siedem W ma opis aktora, stanów, wejść, guard, skutków i niezmienianych pól | Tabela kontraktów zgodna z YAML i wykonawcą; źródła podane |
| RC-02 | Rozróżniono zmianę produktów roboczych, otwarcie nowego wydania i niezmienny wcześniejszy odbiór | Wykonany WIT5; porównanie całego rekordu v1 na każdym późniejszym kroku; a2 v1/v2 w odpowiednich migawkach |
| RC-03 | Dla każdego W wykonano legalne zastosowanie i istotną odmowę, ze wskazaniem dokładnego powodu | Tabela przypadków i wynik; odmowa zachowuje cały stan. W03/W05 obejmują utworzone pytania i późniejszy powrót |
| RC-04 | Ujęto W07 i zmianę zależności oraz wpływ T/P/obserwatorów na wydanie | WIT3, warunki T14/W07, tabela wyzwalaczy; odłożenie/wznowienie i zmiana po odbiorze opisane bez przypisywania niewykonanych prób |
| RC-05 | Mapa pokazuje, co trzeba przenieść do dalszego E3 i czego te próby nie dowodzą | Powiązania z S7a/S7b/S8/S10/S11/S12/S13/S14 oraz L1/L5, F i bounds; brak deklaracji dowodu żywotności |
| RC-06 | Sprawdzono czułość kluczowych oczekiwań | Celowo zmienione kopie: pominięcie przeglądu, brak blokady W04, naruszenie zachowania v1; właściwe oczekiwanie wykrywa zmianę, nie błąd narzędzia |
| RC-07 | Wynik jest odtwarzalny, a osobna recenzja rozliczona | Skrypt, pełne wyniki i hashe wejścia w repo; raport R; działające odnośniki i kontrole dokumentacji |

Próby badają istniejący model. Nie są nową funkcją produktu ani pełną regresją. Nie przedstawiamy czułości na mutanty jako RED/GREEN naprawy: nie naprawiamy kodu modelu. Przy wykrytej niezgodności reguły z zatwierdzonym zamiarem zapisujemy kontrprzykład i eskalujemy zmianę, zamiast samodzielnie zmieniać źródła.

## Rejestr i odpowiedzialność

- Zlecenie U: przygotowanie planu i realizacja mapowania; nie odbiór wyników z góry.
- Agent prowadzący: kontrakty, próby, rozliczenie ustaleń i punkt wznowienia.
- Recenzent: osobna sesja według [karty pracy](work-card.md), bez wprowadzania zmian w oceniany model; opinia nie zastępuje odbioru U.
- Decyzja agenta RC-A1: pracujemy w tym repozytorium na kopii źródeł drugiego projektu, bo nie potrzebujemy zmieniać jego implementacji do sprawdzenia kontraktu.
- Stan początkowy: plan zapisany; kroki 1–5 do wykonania. Aktualny wynik zostanie dopisany w raporcie wykonania, bez przepisywania tego zamiaru.

**Wykonanie:** kroki 1–5 zakończone; [raport i rozliczenie RC-01–07](release-cycle-report.md). Odbiór U pozostaje otwarty (D-85).
