# Przykładowy plan projektu — Release Ledger

Wersja dokumentu: 0.1, 2026-10-22. Status: **przykład, niezatwierdzony i niewykonany**. Zasady i źródła: [przewodnik](README.md). Wszystkie liczby i obsada są fikcyjne.

## 1. Produkt i potrzeba

Mały zespół chce przed wydaniem wiedzieć, czy wymagania mają zaplanowaną realizację i sprawdzenie oraz czy wyniki dotyczą dostarczanej wersji. Release Ledger odczytuje lokalny manifest projektu, raportuje luki i tworzy niezmienny manifest wydania. Odbiorcą jest opiekun projektu.

## 2. Zakres i cele

In: jeden projekt, jedno konto lokalne, wymagania/zadania/testy, jawny zakres wydania, identyfikacja wejść, lokalny raport, manifest wydania, migracja własnego formatu v1 → v2.

Out: uruchamianie dowolnych poleceń z niezaufanego manifestu, hosting, podpisy kryptograficzne i potwierdzanie tożsamości recenzenta, certyfikacja, integracja z GitHubem, automatyczna ocena sensu wymagania.

| Cel | Kryterium demonstracyjne |
|---|---|
| DEMO/OBJ/1 — widoczne luki | Każdy celowo niepowiązany element zestawu kontrolnego zostaje wskazany z ID i rodzajem luki. |
| DEMO/OBJ/2 — aktualny dowód | Po zmianie każdego kontrolowanego wejścia wcześniejszy pass nie dopuszcza nowego wydania. |
| DEMO/OBJ/3 — bezpieczna dostawa | Próba na czystym środowisku odtwarza wydanie, a przerwana migracja nie zmienia oryginału. |

Cele ocenia się względem jawnego zestawu przypadków i uzgodnionej granicy wejść. Nie oznaczają wykrywania wszystkich możliwych wad.

## 3. Cykl i produkty

Rozwój przyrostowy. W każdym przyroście: doprecyzowanie wymagania → przykład akceptacyjny → RED → implementacja → GREEN → refaktoryzacja → przegląd → demonstracja.

Produkty: specyfikacja i model danych, CLI Python, testy, raport V&V, dokumentacja obsługi, procedura migracji i odtworzenia, manifest wydania ze skrótami plików. Modele formalne są opcjonalnym pilotem; projekt nie czeka na ich wdrożenie, jeśli aktualny zakres dopuszcza sprawdzenie prostszymi metodami.

Mapa: I1 — spójność relacji; I2 — aktualność dowodów i dopuszczenie wydania; I3 — dostawa i migracja. I1 opisuje [plan przyrostu](increment-plan.md); szczegóły I2 i I3 zostaną dopracowane przed ich rozpoczęciem.

## 4. Zespół, zasoby i kalendarz

Przykładowe okno: 2026-11-02–2026-11-13, dni pon.–pt., strefa Europe/Warsaw. W tej demonstracji 11 listopada jest dniem wolnym. Razem 9 dni roboczych.

| Rola | Obsada przykładowa | Dostępność | Zadania |
|---|---|---|---|
| DEV — inżynier | Osoba A | Do 6 h dziennie, 54 h w oknie | Analiza, projekt, kod, testy, dokumentacja, poprawki |
| REV — recenzent | Osoba B | 2 h w dniach 04, 06, 10 i 12 listopada | Przeglądy i sprawdzenie dowodów; 8 h |
| OWN — odbiorca i kierownik | Osoba C | 1 h w dniach 02, 06, 10 i 13 listopada | Zakres, decyzje, demonstracje, odbiór; 4 h |

Zasoby: lokalny komputer deweloperski, osobne czyste środowisko odbioru, Git, przypięty interpreter i zależności, syntetyczne dane testowe, lokalny dysk kopii. DEV ma 2 h w pierwszym zadaniu na poznanie formatu manifestu i zasad dowodów. Dostęp do katalogów roboczych tylko dla zespołu; dane prywatne nie są potrzebne.

Oczekiwanie na OWN nie jest czasem pracy DEV. Osoba A nie zastępuje automatycznie osoby B. Nieobecność recenzenta jest ryzykiem harmonogramu.

## 5. Harmonogram, zależności i nakład

Godziny DEV poniżej sumują się do 46. Zakres dat oznacza okno zadania, nie ciągłe zajęcie każdego dnia.

| Zadanie | Okno | Poprzednik | DEV | Pozostały nakład | Rezultat / warunek wyjścia |
|---|---|---|---:|---|---|
| DEMO/T/1 — potrzeby, zakres, wejścia | 02.11 | — | 4 h | OWN 1 h | Spis przykładów i jawne kryteria; przygotowany zakres do uzgodnienia |
| DEMO/T/2 — I1 relacje i raport | 03–04.11 | T/1 | 10 h | REV 2 h, 04.11 | Testy I1 i przegląd raportu |
| DEMO/T/3 — I2 wersje i dopuszczenie | 05–06.11 | T/2 | 10 h | REV 2 h + OWN 1 h, 06.11 | Zmiana wejścia unieważnia uprawnienie do nowego wydania |
| DEMO/T/4 — integracja i awarie | 09–10.11 | T/3 | 8 h | REV 2 h + OWN 1 h, 10.11 | Raport V&V, znane luki i demonstracja |
| DEMO/T/5 — dostawa, migracja, instrukcja | 12.11 | T/4 | 6 h | REV 2 h | Próba instalacji, migracji i odtworzenia |
| DEMO/T/6 — poprawki i odbiór | 04–13.11 | Przeglądy T/2, T/3; odbiór po T/5 | 8 h w całym oknie* | OWN 1 h, 13.11 | Poprawki, ponowne testy i pakiet do odbioru |

*T/6 rozdzielono: do 2 h poprawek po przeglądzie T/2 w dniach 03–04, do 2 h po T/3 w dniach 05–06 i 4 h na odbiór 13.11. To zadanie przekrojowe; jego poprawki zależą od odpowiednich przeglądów, a końcowy odbiór od T/5. Nie należy modelować całych 8 h jako pracy dopiero po T/5.

Kontrola obciążenia DEV: 02.11 — 4 h; 03–04.11 — 12 h; 05–06.11 — 12 h; 09–10.11 — 8 h; 12.11 — 6 h; 13.11 — 4 h. Razem 46 h, z 8 h wolnej pojemności. Jest to ręczne sprawdzenie sum, bez analizy solverem. Kolejność wewnątrz dnia i dostępność recenzenta muszą zostać uzgodnione przed baseline.

Kamienie: M1 koniec 04.11 — wynik I1; M2 koniec 10.11 — kandydat po integracji; M3 koniec 13.11 — decyzja odbiorcza. Sam upływ daty lub utworzenie tagu nie oznacza akceptacji.

## 6. Koszt i wykonalność

| Pozycja | Obliczenie | Koszt przykładowy |
|---|---|---:|
| DEV | 46 h × 150 PLN | 6900 PLN |
| REV | 8 h × 180 PLN | 1440 PLN |
| OWN | 4 h × 200 PLN | 800 PLN |
| Narzędzia i materiały | Limit demonstracyjny | 100 PLN |
| Razem bazowo |  | 9240 PLN |
| Rezerwa | 20% kosztu bazowego | 1848 PLN |
| Limit łączny |  | 11088 PLN |

To model kosztu pracy, bez podatków i zobowiązania handlowego. Rezerwa finansowa nie tworzy dodatkowych godzin w kalendarzu. Wolne 8 h DEV nie zastępuje brakującej dostępności REV/OWN. Estymacja opiera się na małym demonstratorze; przed rzeczywistą realizacją potrzebny jest spike dla formatu i pomiar czasu pierwszego przyrostu. Po I1 należy ponownie ocenić terminy i koszt.

## 7. Ryzyka i reakcje

| Ryzyko | Sygnał | Reakcja | Właściciel |
|---|---|---|---|
| Niepełny zakres wejść dowodu | Zmiana konfiguracji nie zmienia identyfikatora | Zatrzymać wydanie, uzupełnić granicę i test regresyjny | DEV |
| Przeciążenie recenzenta | Brak potwierdzonego okna do dnia poprzedzającego | OWN uzgadnia nowy termin lub zastępstwo; bez fikcyjnego pass | OWN |
| Migracja zmienia oryginał | Porównanie skrótów nie przechodzi | Przerwać próbę, zachować kopię, poprawić przed dostawą | DEV |
| Pilot formalny przekracza koszt | Wyczerpane 8 h pilota | Zakończyć z wynikiem częściowym i osobną decyzją o dalszej pracy | OWN |

Pilot z ostatniego wiersza ma osobny budżet i nie jest zawarty w 46 h DEV ani w harmonogramie produktu.

## 8. Wersjonowanie, kopie i dowody

Przykładowa lokalizacja repozytorium: `/work/release-ledger`; kopia: `/backup/release-ledger`. Dostęp przez konta systemowe zespołu. Lokalizacje są fikcyjne.

Baseline zakresu: uzgodniona rewizja po T/1; baseline projektu: model i kontrakty po przeglądzie; baseline produktu: commit i skróty składników wydania. Numery wersji danych, produktu i dowodów są oddzielne. Dowód identyfikuje wymagania, kod, testy, konfigurację, fixture i narzędzia.

Kopia obejmuje Git oraz dane i artefakty spoza Git. Wykonanie po każdym dniu zmian; sprawdzenie odtworzenia przed M3. Odtwarzanie do osobnego katalogu i porównanie manifestu. Archiwum poprzednich baseline i manifestów tylko do odczytu; indeks wersji umożliwia odnalezienie pakietu. Nie nadpisywać historycznych wyników nowym raportem.

## 9. Dostarczenie i kryteria ukończenia

Kolejność: zamrozić kandydata → wykonać V&V na jego wejściach → przejrzeć luki → przygotować wersjonowany pakiet i skróty → sprawdzić instalację na czystym środowisku → wykonać demonstrację → uzyskać decyzję odbiorcy → przekazać pakiet.

Medium: lokalny katalog wydania skopiowany na nośnik odbiorcy. Zawartość: program, blokada zależności, specyfikacja, instrukcja, raport, manifest wersji i procedura odtworzenia. Szczegóły: [plan wydania, migracji i utrzymania](delivery-migration-operations.md).

Gotowość: testy uzgodnionego zakresu przechodzą, nie ma nierozstrzygniętej wady blokującej, dowody odpowiadają kandydatowi, próba odtworzenia przechodzi. Akceptacja klienta pozostaje osobną decyzją.

## 10. Zatwierdzanie i zmiany

Klient: rola OWN — **brak zatwierdzenia, przykład**. Kierownik projektu: rola OWN — **brak zatwierdzenia, przykład**. Plan nie jest przyjętą bazą realizacji.

Zmiana celu, terminu, budżetu lub kryterium odbioru wymaga decyzji OWN i oceny wpływu. Doprecyzowanie zadania w przyjętych granicach zapisuje wykonawca. Historia zachowuje poprzednią bazę oraz uzasadnienie i datę zmiany. Rejestr wykonania zawiera osobno planowane i rzeczywiste godziny, wynik, odchylenie i odnośnik do dowodu; obecnie wszystkie zadania są niewykonane.
