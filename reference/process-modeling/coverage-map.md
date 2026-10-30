# Mapa kryteriów, istniejącego modelu i braków

2026-10-29 · D-83 · wykonanie polecenia „commit(y), a następnie Dalej”. Analiza i ograniczone próby na kopii; bez zmian reguł modelu i bez odbioru za operatora.

**Aktualizacja 2026-10-30 — D-86:** bieżący [audyt wymagań i kryteriów](#8-audyt-wymagań-i-kryteriów-2026-10-30) jest w §8. Sekcje 1–7 zachowują wynik odczytu z 2026-10-29; ich „następne działania” nie są aktualnym poleceniem. W drugim repozytorium wykonano już translację E3.5 i przyjęto korektę L/F przez DEC-PRO-017. Nie należy ponownie implementować tej dostawy na podstawie starej mapy.

## Wniosek decyzyjny

**Mamy działający rdzeń symulacyjny, ale nie kompletny mechanizm prowadzenia rzeczywistego projektu.** Istniejące E1/E2 należy zachować. Najbliższa praca to domknięcie pokrycia pełnego zachowania w E3, zgodnie z obecnym planem `iso-model-state`. Późniejsze E4/E5 mają sprawdzić przejście od symbolicznych danych do historii i dowodów projektu.

Nasze AC-01–AC-10 nie są zamiennikiem przyjętego DoD. Część porządkuje już istniejące zobowiązania, część łączy różne etapy, a część proponuje dodatkowe wymagania operacyjne. Nie wolno z ich redakcji wywnioskować zgody na nowy system, API czy obowiązkowe formularze.

## 1. Przedmiot i sposób sprawdzenia

Odczytano robocze `iso-model-state`, HEAD `0bf7addff2242e2dea2c12515c18b397dc6aa2e1`, z niezacommitowanymi zmianami dokumentów. PLAN/STAN zawierają DEC-PRO-016: próba P0–P4 zamknięta z ograniczeniami, dalej E3; odbiór N1–N3 pozostaje otwarty. To rozpoznanie źródeł, nie nowa decyzja naszego operatora.

Model YAML, kod wykonawcy i dane WIT skopiowano do katalogu tymczasowego, a następnie uruchomiono pięć świadków i trzy próby diagnostyczne. Trwały [wynik JSON w gzip](evidence/mapping-probes.json.gz) zawiera pełne stany przed/po, zdarzenia i SHA-256 skopiowanych plików oraz głównych dokumentów. Kopia tymczasowa nie jest potrzebna do odczytania wyniku ani ponowienia prób. Skrót pliku YAML i skrót jego sparsowanej postaci są różnymi tożsamościami; nie porównujemy ich jako tej samej wartości.

**Nie wykonano:** pełnej regresji E2/E3, TLC, nowego pilota użytkowego ani recenzji przez osobnego agenta. Wyniki dawnych raportów są oznaczone niżej jako zastane. Wykonanie pięciu ścieżek nie dowodzi własności dla wszystkich kombinacji.

## 2. Najważniejsze ustalenia

| Kategoria | Problem → plik i dowód | Skutek | Minimalne dalsze działanie |
| --- | --- | --- | --- |
| **Brak w wykonaniu przyjętego planu** | [Raport E3.4](../../../iso-model-state/docs/E3-04-RAPORT.md), „Granice”: wycinek z głębokością 16, `CHECK_DEADLOCK FALSE`, bez pełnych S/L/F i L1 | Brak podstaw do twierdzenia o zakończonym badaniu całego zachowania | Dokończyć istniejące E3; nie budować drugiego silnika |
| **Brak operacyjnego powiązania** | [Model](../../../iso-model-state/model/process.yaml), `notation`: `tests_ok` i `checks_ok` to założenia. Próba `tests_false_only_at_W04` dochodzi do accepted, natomiast późne pytanie blocking zatrzymuje W04 | Negatywny wynik musi zostać odwzorowany na właściwy stan/ustalenie; samo przekazanie flagi przy W04 nie blokuje odbioru | W E4 określić mapowanie faktów do zdarzeń i blokad, a w E5 sprawdzić wybrany adapter. Nie zmieniać teraz W04 bez decyzji o regule |
| **Brak kompletnego pokrycia pojęć operacyjnych** | [Model](../../../iso-model-state/model/process.yaml), `item_types`: PLAN/REQ/AT/DES/CODE; [N3](../../../iso-model-state/docs/preparations/n3/REPORT.md) to próba modelu informacji, nie wdrożony profil Task/Run/material/result | Nie można utożsamić zatwierdzenia PLAN z istnieniem pełnej mapy prac ani śladu ID z rzeczywistym wykonaniem testów | Wykorzystać N3 do doboru minimalnych informacji na podstawie E4; nie wdrażać pełnego ręcznego profilu |
| **Brak pełnego dowodu użytkowego** | [Próba vcs-lite](../../../iso-model-state/docs/PROBA-ZMIANY-ARCHIWIZACJA.md), §16–17 i DEC-PRO-016: wznowienie wykonane, pełny ARC-11 oraz koszt U niesprawdzone; N3 ujawniło narzut ręcznych zapisów | Sukces wybranej próby nie potwierdza całej obsługi zgód ani wygody przyszłego narzędzia | Zachować wyniki i ograniczenia; brakujące aspekty sprawdzić w istniejących E4/E5, bez ponownego otwierania P0–P4 |
| **Propozycja porządkująca** | [Nasze AC](acceptance.md) łączą model, trwałość operacji i użyteczność widoków; [przyjęty plan](../../../iso-model-state/PLAN.md) oddziela E3, E4, E5 | Łatwo dołożyć do E3 nowy zakres i ponownie rozmyć cel | Zachować przyjęty DoD jako wiążący; AC stosować jako mapę pytań do dowodów, z rozszerzeniami jawnymi przed ich realizacją |

Nie zgłaszamy tutaj nowego potwierdzonego defektu rdzenia. Drugi wiersz jest wykazaną granicą abstrakcji modelu wobec przyszłego użycia operacyjnego, a nie niezgodnością implementacji z obecnym guard W04.

## 3. Mapowanie każdego kryterium

„Pokrycie” poniżej oznacza zakres istniejących mechanizmów i dowodów; nie nadaje statusu odbioru całego AC.

| AC | Przyjęty DoD / etap | Istniejący mechanizm lub dowód | Co pozostaje; kwalifikacja |
| --- | --- | --- | --- |
| 01: granica i źródła | DoD 1, 8; E1 | [Katalog](../../../iso-model-state/docs/KATALOG.md), §„Moc dokumentów”; model z `iso`, [interpretacje](../../../iso-model-state/docs/INTERPRETACJE.md); E1/E2 odebrane według PLAN | Źródła i granica modelu są ustalone. G6 sprawdza adnotacje, nie realizację wszystkich składowych ISO. Rozszerzona granica naszego briefu pozostaje propozycją |
| 02: tożsamości i historia | DoD 1, 3; E1/E2 | `item_variables`, `predecessor`, kopie odbiorów; WIT3 i WIT5 ponownie wykonane | Rdzeń wersji działa. Materiał pliku, wykonanie i wynik nie są pełnymi encjami tego rdzenia; ich profil jest propozycją N2/N3 |
| 03: kontrakty operacji i błędy | DoD 1–3, 9; E2, potem E5 | [execute_step](../../../iso-model-state/src/isomodel/execution.py): odczyt actor/from/guard/effects, praca na kopii; [testy atomowości](../../../iso-model-state/tests/test_v07_scope.py), `test_observer_failure_rolls_back_external_change_and_consumed_consent` | Atomowość operacji w pamięci nie dowodzi odporności trwałego magazynu na awarię. Trwałość i idempotencja przyszłego adaptera są warunkowym rozszerzeniem, nie luką w czystej funkcji |
| 04: wpływ i dowody | DoD 3, 9; S4–S7/S10–S14 | `dependents`, `suspect`, T11/T14/W07, obserwatory; [testy zastąpienia](../../../iso-model-state/tests/test_replacement.py), WIT3/WIT5; odmowa późnego blocking ponowiona | Powiązania i zmiana formalnego PLAN są objęte modelem; wykrycie ręcznej zmiany pliku, semantycznie starego planu lub sprzecznej prozy wymaga E4/E5 i osądu. `suspect` nie jest pełną kontrolą świeżości testu |
| 05: struktura i postęp | DoD 2–5; G/S/L/F | [E2](../../../iso-model-state/docs/E2-RAPORT.md): świadek każdego z 28 przejść; [E3.4](../../../iso-model-state/docs/E3-04-RAPORT.md): zgodność wycinka z osobną wyrocznią | Przyjęte zobowiązanie nadal otwarte: pełna relacja w granicach, pełne własności, CTL L1, OBS. Pokrycie przejść nie oznacza pokrycia ich interakcji |
| 06: czułość i semantyka | DoD 6, 9 | Zastane raporty E2: mutanty S; E3.4: 34 mutanty oraz osobne wyrocznie; [testy danych dowodowych](../../../iso-model-state/tests/test_evidence.py) | Domknąć macierz własność → konkretny mutant → właściwa przyczyna naruszenia dla pozostałego E3. Nie zastępować tego procentem testów. Nie powtarzano tych badań tutaj |
| 07: scenariusze | DoD 7; E2/E3 | WIT1–WIT5 ponownie wykonane: 29/33/54/13/40 kroków | To świadkowie symulacji Python. DoD wymaga także wygenerowania/przeglądu U w zakresie E3. Nasze dodatkowe awarie trwałego wykonania nie są automatycznie objęte WIT |
| 08: fakty i decyzje | DoD 3, 9; cel użytkowy | Wymagane pola evidence, pytanie związane z elementem/wersją/operacją, odrębne `simulation`; W04 odmówił aktorowi A | Źródło tekstowego dowodu i rzeczywista tożsamość nie są uwierzytelniane. E4/E5 mają powiązać rekord z realnym materiałem; sam parametr actor=U nie chroni przed podszyciem |
| 09: orientacja i wznowienie | [Karta celu](../../../iso-model-state/docs/KARTA-CELU-I-ZAKRESU.md), kryteria użytkowe; E5 | Katalog, STAN, raporty; N3: osobny odczyt; próba P3: dwa wznowienia według jej raportu | Wykorzystać istniejące dowody, nie zaliczać ich jako próby końcowego narzędzia. Automatyczne, wspólne widoki z jednego stanu są naszą propozycją realizacji, nie warunkiem już odebranego E2 |
| 10: odtwarzanie i recenzja | DoD 5, 10; bramki etapów | Raporty i archiwa E3; [recenzja E2](../../../iso-model-state/docs/reviews/E2-V07-PRZEGLAD-2026-10-26.md); osobne recenzje E3.4 | Istnieją przeglądy konkretnych dostaw. Końcowa recenzja/odbiór E3 oraz E5 nadal przyszłe; ta mapa jest analizą autora |

## 4. Pokrycie zachowania — bez mieszania wykonawcy z dowodem formalnym

| Operacje | Wykonawca Python | Zastane badania TLA+/TLC | Następne rozliczenie |
| --- | --- | --- | --- |
| T00–T04: utworzenie, sprawdzenie, zatwierdzenie/odrzucenie, baseline | Zdefiniowane w YAML; świadkowie i testy E2 | E3.1–E3.3 oraz wybrane użycia w E3.4 | Zachować wyniki wycinków; złożyć z pełną relacją i historią |
| T05, T11–T13: otwarcie zmiany i obsługa suspect | Modelowane, wykonywane przez WIT3/WIT5 | E3.4 bada wybrane interakcje od jawnego prefiksu | Nie przenosić dowodu wycinka na dowolny stan pełnego procesu |
| T06–T10, T14: podważenie, zastąpienie, wycofanie, odłożenie/wznowienie, przepięcie | Istnieją świadkowie E2, T14 wykonane w WIT3 | Pełne mapowanie wymienione jako pozostała praca E3 | Kontrakt → oczekiwane skutki/odmowy → własności → mapowanie do TLA+ |
| P00–P05: pytania | WIT4 oraz zgody w WIT3/WIT5 | E3.4 obejmuje wybrane P01/P02; nie całą kolejkę i jej postęp | Pełna relacja P, L2 przy założeniach; nie utożsamiać kolejki modelu z rozumieniem odpowiedzi w języku naturalnym |
| W01–W07: wydanie | WIT1/WIT5, odmowy W03/W05 w zastanym E2, W07 w WIT3 | Konteksty wydań w E3.4 nie są pełnym cyklem W | Pełny cykl „odbiór v1 → zmiana → odbiór v2”, także odmowy i powrót do przygotowania |
| Obserwatory wpływu przed/po odbiorze | Testy E2 i E3.4, wpływ spoza zakresu | Wycinki i izolowane konteksty | Złożenie z całym procesem; historyczny accepted pozostaje niezmienny |

Źródła tej tabeli: [model](../../../iso-model-state/model/process.yaml), [E2](../../../iso-model-state/docs/E2-RAPORT.md), [plan dokończenia E3](../../../iso-model-state/PLAN.md), [E3.4](../../../iso-model-state/docs/E3-04-RAPORT.md). To mapa zobowiązań, nie gotowy kontrakt translatora dla pozostałych operacji.

## 5. Wykonane próby

| Próba | Oczekiwanie zapisane przed wykonaniem | Rzeczywisty wynik |
| --- | --- | --- |
| WIT1 / WIT2 / WIT3 / WIT4 / WIT5 | completed; odpowiednio 29/33/54/13/40 kroków | Zgodne we wszystkich pięciu |
| Odbiór W04 przez A | Odmowa z przyczyny actor | rejected / actor |
| P00 blocking po W02, przed W04 | Odmowa W04 z przyczyny guard | rejected / guard |
| Samo `tests_ok=False` dopiero przy W04 | Według obecnego guard nadal completed; próba granicy abstrakcji | completed, stan accepted |

Ostatni wynik **nie potwierdza poprawności takiego odbioru w realnym projekcie**. Pokazuje, że model reaguje na jawne zdarzenia i przesłanki, a nie na każdą informację, którą wykonawca może otrzymać. Aby realny późny wynik ujemny blokował odbiór, trzeba zdefiniować jego odwzorowanie na blokadę/utratę gotowości. To przedmiot przyszłego adaptera albo decyzji o zmianie reguły, nie automatyczna zmiana przyjętego YAML.

Odtworzenie z katalogu `iso-template-agent`, z użyciem istniejącego środowiska drugiego repozytorium:

```sh
/Users/michal/PycharmProjects/iso-model-state/.venv/bin/python -B reference/process-modeling/probe.py --source ../iso-model-state --output reference/process-modeling/evidence/mapping-probes-rerun.json.gz
```

[Skrypt](probe.py) odmawia nadpisania wyniku. Używa nowej kopii źródeł; porównaj ich hashe z zapisanym wynikiem. Kopiuje aktualne źródła, nie odtwarza sam dawnego stanu zmienionego repozytorium. Pierwsze wykonanie przez względną ścieżkę środowiska dało ostrzeżenie Python o `sys.prefix`; zakończyło się kodem 0 i wszystkimi wynikami powyżej. Polecenie odtworzenia używa ścieżki kanonicznej. Nie instalowano zależności.

## 6. Rozbieżności do obsłużenia w odpowiednim momencie

| Temat | Właściciel / najmniejszy następny krok | Moment decyzji |
| --- | --- | --- |
| Zakres DoD: rdzeń versus dowody operacyjne i widoki | Agent utrzymuje to mapowanie; wiążący pozostaje DoD `iso-model-state`, AC są propozycją uzupełniającą | Przed aktywacją wymagań wykraczających poza E3–E5, nie przed samym dokończeniem mapowania |
| Swoboda A versus T04 zawsze wykonywane przez U, także dla DES/CODE | Agent rozróżni techniczne sprawdzenie, baseline i odbiór; opisze liczbę i sens rzeczywistych decyzji w E4 | Przed przeniesieniem modelu do procesu Kitchen; nie zmieniamy odebranej semantyki E2 |
| W02/W04 symbolicznym aktorem versus rzeczywisty recenzent i operator | Agent dobierze zapis źródła decyzji/recenzji do konkretnej integracji; autentyczność oddzieli od kontroli pomyłek | Przed operacyjnym użyciem narzędzia; osobny model zagrożeń przed obietnicą odporności na fałszowanie |
| Pomiar czasu w starszej karcie celu versus wyłączenie go w tej rozmowie | Agent zachowuje historyczny brak pomiaru; dla przyszłej próby proponuje obserwacje błędów, fałszywych alarmów i duplikacji | Przy uzgodnieniu przyszłych kryteriów użytkowych; bez cichego przerabiania dawnego odbioru |

## 7. Następne działania i punkt wznowienia

1. **Agent: uszczegółowić mapowanie pozostałego E3**, zaczynając od pełnego cyklu wydań. Rezultat: dla każdej operacji W oraz powiązanych T/P wejścia, warunki, efekty, odmowy, własności i oczekiwane przypadki. Koniec: brak nieopisanej operacji w wybranym przekroju, rozliczone różnice ze źródłami, pakiet gotowy do osobnej recenzji. Nie dodawać nowych reguł.
2. **Po mapowaniu: osobny recenzent ocenia kontrprzykłady**, zanim zmieni się generator. Rezultat: uwagi powiązane z regułami i przypadkami. Koniec: brak nierozstrzygniętej sprzeczności blokującej implementację; zmiana zaakceptowanej reguły trafia do U. To przyszły punkt recenzji z karty pracy, nie recenzja już wykonana.
3. **Następnie implementacja w istniejącym E3 i jego bramka.** Rezultat: TDD, porównanie z osobną wyrocznią, badanie w jawnych granicach i raport. Koniec: spełniony przyjęty zakres E3, odtworzenie dowodów i osobny odbiór U. E4/E5 następują w przyjętej kolejności; żadnego nowego pilota ani API teraz.

**Stan tego zlecenia:** wcześniejszy pakiet zapisany w commicie `d6f932d`; mapa przygotowana, osiem prób wykonanych. Nie zmieniono drugiego repozytorium. Karta/brief/AC nadal mają status propozycji tam, gdzie wykraczają poza wcześniej przyjęty zakres. Otwarta praca agenta: krok 1 powyżej; pytania dla U dopiero przy wykazanej zmianie reguły lub zakresu.

**Decyzja agenta A3, 2026-10-29:** mapa rozdziela pokrycie Python, badania TLC i użycie operacyjne, bo ich połączenie w jeden status dawałoby fałszywe „gotowe”. Osiem prób to diagnostyka istniejącej semantyki, nie nowe kryteria odbioru ani pełna regresja.

**Kontrola dokumentacji:** `make check` — kod 0, 249 elementów, 0 błędów; dwa wcześniejsze ostrzeżenia W1 MIG-01/MIG-02. Osobna kontrola sześciu dokumentów: 113 lokalnych odnośników do istniejących plików/katalogów, domknięte bloki kodu, brak błędów; kotwic nie sprawdzano. Skompresowany dowód odczytano: osiem wyników zgodnych z zapisanymi oczekiwaniami. `git diff --check` bez błędów. Mapa, skrypt i wyniki powstały po commicie wcześniejszego pakietu i pozostają zmianami roboczymi.

## 8. Audyt wymagań i kryteriów 2026-10-30

**Wynik:** nie ma podstaw, by uznać całą specyfikację za jednoznaczną i wolną od duplikacji znaczenia. Nie znaleziono identycznych zdań w 57 wymaganiach szablonu. Potwierdzono natomiast rozbieżności zakresu zapisów, niejasność domknięcia DoD i nieaktualne wskazówki kontynuacji. Część powtórzeń jest uzasadniona: opisuje regułę, sposób jej sprawdzenia i wynik. Problemem są niezależnie utrzymywane definicje tej samej reguły.

To ograniczony audyt semantyczny autora, z kontrolą historii i jedną wykonaną próbą narzędzia. Nie jest certyfikacją, pełną weryfikacją kodu ani niezależnym przeglądem. Nie nadaje `verified` lub `approved` wymaganiom, nie odbiera D-85 ani E3. Zalecane zmiany znaczenia pozostają propozycjami.

### 8.1 Zakres i wykorzystanie Git

Stan wejściowy: `iso-template-agent` **dd8f353e92abb5a227231eb8ab73e25c4b527427**, 302 pliki śledzone, w tym 112 Markdown; jedyny nieśledzony plik to eksport użytkownika `ISO 29110 a nasz model śladu.md`, pozostawiony bez zmian. `iso-model-state` **79cab4da4284b6bac1ee9f5fc2d88b0d97dba4dc**, 626 plików śledzonych, 118 Markdown, czyste drzewo przy odczycie. Liczby dotyczą wejścia, nie rozmiaru specyfikacji; większość plików drugiego repozytorium stanowią kod i dowody.

Przeskanowano nagłówki wszystkich 230 śledzonych Markdown pod kątem wymagań, kryteriów i DoD: 19 kandydatów tutaj, 28 w modelu. Ten filtr służył nawigacji, nie dowodzi braku reguł ukrytych w innych akapitach. Czytanie szczegółowe objęło wszystkie 57 zdań REQ i 55 AT szablonu, słownik, instrukcje, plan i decyzje; pełne DoD 1–10 modelu, definicje G0–G6, S1–S15 z S7a/S7b, L1–L5, F1–F3 i WIT1–WIT5; kartę celu, hierarchię i aktualny plan; dziewięć E3-AC, dziesięć naszych AC i siedem RC. Implementacje i raporty czytano celowo przy konkretnym ustaleniu, nie wszystkie linie kodu i archiwa dowodów.

Materiały edukacyjne, propozycje API, N1–N3 i zamknięta próba vcs-lite zostały rozdzielone według statusu i przedmiotu. Nie przeprowadzono ponownego szczegółowego audytu wszystkich ich historycznych kryteriów, implementacji L1 ani normy. Ten audyt nie upoważnia do twierdzenia „sprawdzone wszystkie 300 plików”.

| Użycie historii | Co rzeczywiście ustalono | Praca, której nie trzeba powtarzać |
| --- | --- | --- |
| `git log`, `git blame`, `git show` dla REQ/AT i narzędzi | UPD-04 oraz LAY-03 mają obecne problematyczne brzmienie od `11ddded`; nie powstało ono przy ostatnim mapowaniu. D-53/D-64 zapisują wyjątki; przeniesienie `b866213`/`12acb1d` nie jest nową regułą | Nie przypisywać błędu przeniesieniu plików; nie badać każdej dawnej lokalizacji jako osobnej specyfikacji |
| Początek DoD i G5 w modelu | „Każda właściwość ma mutanta” oraz G5 „raport, nie test” współistnieją już w `d60d7f9`; późniejszy raport E2 jawnie wyłącza G5 | Nie otwierać ponownie testów E2 w poszukiwaniu regresji, której historia nie wskazuje |
| `d6f932d` → `dd8f353` | Nasze AC od początku są propozycją; RC dotyczą tylko mapowania. Commit nie jest zatwierdzeniem AC ani odbiorem D-85 | Nie scalać wszystkich AC/RC z przyjętym DoD jako nowych obowiązków |
| Model: `04485cc` → `36819a0` → `79cab4d` | Zapisano E3-AC, przyjęto warunkowe L/F (DEC-PRO-017), wykonano E3.5. Relacja YAML v0.7 pozostaje bez zmiany, zmieniły się gwarancje i wykonanie translatora | Nie odtwarzać starej diagnozy „brak translacji 17 przejść”; nie powtarzać jej implementacji |

Git zawęża dochodzenie i identyfikuje przedmiot. Nie dowodzi sensu wymagania, autorstwa decyzji U ani kolejności pisania plików wewnątrz jednego commita. Każdą podejrzaną parę porównano również w bieżącej treści; brak zmiany od pierwszego commita nie oznacza poprawności.

### 8.2 Gdzie obowiązuje które kryterium

| Przedmiot | Źródło definicji i mocy | Sprawdzenie i wynik | Czego z nim nie scalać |
| --- | --- | --- | --- |
| Szablon procesu | [REQ](../../spec/requirements.md), [decyzje](../../project/decisions.md), instrukcje i słownik; wszystkie 57 REQ mają obecnie `initiated`, nie `approved` | [AT](../../spec/tests/process-kit.feature); kryteria wydania MS-01 w [planie](../../project/plan.md); wyniki testów i rekordy przeglądów są odrębne | Formalne S/L modelu ani fikcyjne wymagania TextStats nie są wymaganiami tego produktu |
| Abstrakcyjny model procesu | [YAML](../../../iso-model-state/model/process.yaml), [WLASCIWOSCI](../../../iso-model-state/docs/WLASCIWOSCI.md), [INTERPRETACJE](../../../iso-model-state/docs/INTERPRETACJE.md), decyzje STAN według [katalogu](../../../iso-model-state/docs/KATALOG.md) | Pełne DoD w WLASCIWOSCI; PLAN zawiera skrót i etapy; raport odpowiedniego E identyfikuje zakres dowodu | Raport z przykładowych ścieżek nie zamyka całego DoD |
| Domknięcie E3 | Powyższe reguły i [E3-AC01–09](../../../iso-model-state/docs/E3-KRYTERIA-ODBIORU.md) jako konkretyzacja dowodów | [Raport E3.5](../../../iso-model-state/docs/E3-05-RAPORT.md) rozlicza dostawę krokową; pełny graf, S/L/F i odbiór E3 nadal otwarte | Nasze wcześniejsze „co przenieść do generatora” nie jest aktualną listą braków |
| Użyteczność narzędzia | [Przyjęta karta celu](../../../iso-model-state/docs/KARTA-CELU-I-ZAKRESU.md), decyzje i przyszły zakres E4/E5 | Próby wznowienia, wpływu, zgód i działania operatora na określonym materiale; dotychczasowe próby mają jawne ograniczenia | `tests_ok`, aktor `U` w symulacji i green TLC nie dowodzą realnego wykonania lub zgody |
| Nasza propozycja całej pracy | [AC-01–10](acceptance.md), D-83: zlecenie opracowania, nie odbiór kryteriów | Mapa w §8.5 poniżej; rozszerzenia nie są obowiązkowe bez decyzji | Nie ustanawia drugiego nadrzędnego DoD |
| Nasze mapowanie wydań | [RC-01–07](release-cycle-plan.md), D-84 | [Raport i 36 prób](release-cycle-report.md); odbiór D-85 osobny | RC-05 wymaga mapy do formalizacji, nie dowodu całej żywotności |
| Lekcja edukacyjna L1 | [I1](../process-simulator/increment-01.md), D-79 | Testy i próba interfejsu opisane w rejestrze L1 | Odbiór w fabule nie jest odbiorem modelu lub symulatora |
| API, przykłady planowania i ewolucji repo | Własne nagłówki „propozycja”/„przykład”; [kontrakt API](../process-map/acceptance-contract.md), [przykład planu](../planning-examples/increment-plan.md) | Materiały do nauki i późniejszej decyzji, nie obecna specyfikacja wdrożenia | Ich manifesty, budżety, stany lub kryteria nie rozszerzają automatycznie E3 ani Kitchen |

### 8.3 Pięć najważniejszych ustaleń

Identyfikatory AUD służą tylko lokalizacji ustaleń tego przeglądu; nie są nowym katalogiem wymagań. „Defekt” poniżej dotyczy dokumentacji, chyba że wskazano inaczej.

| ID / kategoria | Problem i dowód | Konsekwencja | Najmniejsza poprawka i priorytet |
| --- | --- | --- | --- |
| AUD-01 — **potwierdzony defekt** | [UPD-04](../../spec/requirements.md), linia 325: każdy plik projektu poza pakietem ma pozostać identyczny; [AT-40](../../spec/tests/process-kit.feature) powtarza „wszystkie”. UPD-03 dopuszcza zmianę Answers File, a [snapshot](../../tests/test_distribution.py), linie 157–166, wyłącza answers i `.git`. G-DST-03 lokuje answers w projekcie | Wymaganie i kryterium obiecują więcej niż sprawdza test; prawidłowa zmiana wersji copiera narusza dosłowne „wszystkie” | Dopisać jawny zakres porównania: poza pakietem, Answers File i metadanymi Git; odesłać do UPD-03/D-53. **P1 przed następnym odbiorem szablonu** |
| AUD-02 — **potwierdzony defekt** | [LAY-03](../../spec/requirements.md), linia 392: nieistniejąca ścieżka w dokumencie/skrypcie ma dać błąd, chyba że ma uzasadniony wyjątek. [check_refs.py](../../template/process/tools/check_refs.py), `scanned`, pomija m.in. całe `reference/`, decyzje i testy; D-64(3) zatwierdza to wyłączenie. Próba §8.6: ten sam błędny link daje kod 1 w korzeniu, kod 0 w reference | Czytający REQ może błędnie uznać nasze materiały za skontrolowane przez zielone `make check` | Ograniczyć LAY-03 do jawnie zdefiniowanego zakresu skanowania i wskazać zatwierdzone wyłączenia; nie poszerzać skanera. **P1 przed deklaracją pokrycia dokumentów** |
| AUD-03 — **potwierdzony defekt** | [WLASCIWOSCI](../../../iso-model-state/docs/WLASCIWOSCI.md): DoD 2 mówi „G1–G6 / testy pytest”, DoD 6 „każda właściwość / 100% mutantów”; G5 ma „raport, nie test”. [E2-RAPORT](../../../iso-model-state/docs/E2-RAPORT.md), tabela G5: `report_not_test`, mutant „nie dotyczy”. E3-AC06 mówi już „właściwość wymagająca dowodu” | Brak jednolitej odpowiedzi, czy raport G5 wystarcza do końcowego DoD i jaki jest mianownik pokrycia mutantami | W jednym pełnym DoD jawnie przypisać G5 do przeglądu raportu, pozostałe właściwości do właściwych testów/mutantów; decyzja U, bo zmienia dosłowne przyjęte kryterium. Nie cofać historycznego odbioru E2. **P1 przed zamknięciem całego DoD** |
| AUD-04 — **brak** | [AC-03/04/07/08](acceptance.md) mieszają kontrolę modelu z trwałością operacji, aktualnością rzeczywistych dowodów i konfliktem prozy. „Poprawnie wpływa” w AC-04 nie określa samodzielnie wejścia ani oczekiwanego zbioru; mapa §3 ostrzega, ale nie dzieli każdego AC na odsyłacz i rozszerzenie | Autor może uznać zgodność z modelem za spełnienie operacyjne albo dołożyć niezlecony adapter do E3. WIT1 dodatkowo używa nieostrego określenia „rzeczywista decyzja … w granicy trybu” | Używać mapowania §8.5: źródłowe S/DoD są kryteriami, a brakujące zachowania operacyjne pozostają propozycją. Doprecyzować przy wyborze E4/E5; nie dopisywać nowych REQ teraz. **P1 przed użyciem AC jako bramki** |
| AUD-05 — **potwierdzony defekt** | Przed audytem [brief](brief.md), [rejestr](../process-simulator/progress.md) i [raport](release-cycle-report.md) wskazywały dalsze mapowanie/generator. `iso-model-state` ma już `79cab4d` i E3.5. [Kontrakt](release-cycle.md) §6 mówi o „trwałym odbiorze po ustaniu zmian”, podczas gdy DEC-PRO-017 przyjmuje warunkową gotowość i nie wymusza pozytywnej decyzji | Nowy agent może powtórzyć ukończoną translację lub zaimplementować dawną, zbyt silną gwarancję | Zaznaczyć datę starego odczytu i odsyłać bieżącą kontynuację do PLAN/STAN oraz L/F w WLASCIWOSCI. **P1 przed wznowieniem implementacji**; lokalne ostrzeżenia i punkty wejścia poprawiono w tym audycie, historycznych wyników nie nadpisano |

Pierwsze dwa ustalenia są niezgodnością treści z zapisanymi wyjątkami, nie nowymi awariami aktualizatora/skanera. AUD-03 wymaga rozstrzygnięcia treści kryterium; nie dowodzi, że E2 miał ukryte nieudane testy. AUD-04 jest brakiem precyzji propozycji, nie naruszeniem już przyjętego nowego wymagania.

### 8.4 Przegląd wymagań szablonu i duplikacji

Każde z 57 REQ ma `source`, `quality`, wzorzec i status `initiated`. Każde poza MIG-01/02 ma wskazujący je AT; dwa AT są ręczne. Istniejący [VER-01](../../records/verification.md) dotyczy kopii repozytorium, nie semantycznego odbioru wszystkich REQ. „TSK-01 completed” oznacza wykonanie dokumentacji, nie zatwierdzenie każdego wymagania. Dlatego poniższa tabela jest oceną treści, nie wynikiem testów produktów.

| Zakres przeczytanych REQ | Powiązane AT | Ocena relacji i precyzji |
| --- | --- | --- |
| TRC-01–19 | AT-01–17, AT-50, AT-52 | Warunki i obserwowalne błędy są przeważnie konkretne. TRC-14 wymaga odczytania wspieranych interpreterów z planu; TRC-13 „changed” trzeba czytać z D-39/AT-12 (bez samej zmiany statusu). Brak duplikatu zdania, ale sama EARS nie usuwa zależności od definicji |
| HKS-01–05 | AT-18–21, AT-53 | HKS-01 i 03 kontrolują inne raporty; HKS-05 precyzuje przedmiot kontroli wszystkich hooków. To rozdzielone aspekty, nie kandydaci do usunięcia |
| SEP-01–02 | AT-22–23 | Zasada i wyjątek pierwszego commita. SEP-01/G-ART-08 nazywa tylko VER, podczas gdy D-38/P-Role opisują także VAL: katalog nie wyczerpuje całej instrukcji E9. Test nazwany „autor nie weryfikuje sam siebie” sprawdza rozdział commitów, nie tożsamość osoby |
| PLN-01–03 | AT-24–26 | PLN-02 jest konkretyzacją jednego pola wyniku PLN-01; utrzymywać jako odrębny sprawdzalny aspekt, bez drugiej definicji osiągnięcia kamienia |
| REC-01–02 | AT-27–28 | Nieznany punkt listy i sprzeczny wynik pass to różne błędy; podobne słownictwo nie jest duplikatem |
| REP-01–02 | AT-29–30 | Porównanie kopii i opcjonalny zapis wyniku to różne efekty; dwa AT mogą legalnie używać wspólnego runnera |
| ISO-01 | AT-31 | Generowanie strony z danych; nie wymaganie osiągnięcia zgodności produktu z normą |
| INI-01–03 | AT-32–34 | Odmowa startu, utworzenie dokumentów, przejście hooków to różne zachowania. „Niezacommitowana zmiana” w AT-32 jest skrótem — REQ mówi o plikach śledzonych |
| DST-01–02 | AT-35–36 | Zakres dostawy i identyfikacja wersji; stanowią również kontekst AUD-01 |
| UPD-01–08 | AT-37–44 | UPD-03 jest odmową, UPD-04 gwarancją udanej operacji — uzasadnione uzupełnienie, ale muszą używać tego samego wyjątku (AUD-01). UPD-07 określa ponowienie, nie drugi ogólny zakaz zmian |
| MIG-01–02 | brak | Znany zaplanowany brak AT, nie nowo odkryta awaria. Zakres migracji nadal zależy od zmian wydania i TSK-07 |
| LAY-01–03 | AT-45, AT-54–55 | LAY-02 chroni dokument wygenerowany wcześniej z wzorca; jest konkretnym przypadkiem ochrony z UPD-04. LAY-03: AUD-02 |
| LEK-01–02 | AT-46–47 | ID i pojęcie to inne wejścia. Zakres słownika jest już otwartą sprawą D-75; przegląd jej nie rozstrzyga |
| TST-01–02 | AT-48–49 | Istnienie runnera i wiarygodna interpretacja wyniku to różne kontrole. Naprawa D-76 doprecyzowała TST-02 i AT razem; nie ma powodu powtarzać naprawy |
| LNG-01 | AT-51 | Szerokie „every … file … English” ma znany wyjątek `kontrakt-decyzji.md` w D-20. Przy przyszłym porządkowaniu ograniczyć kwantyfikator do zakresu decyzji; EARS nie dowodzi precyzji tej deklaracji |

Powyższe drobniejsze uwagi SEP/TRC/LNG pozostają po stronie agenta do redakcyjnego porównania z odpowiednimi decyzjami podczas następnej zmiany danego obszaru; nie dopisano dla nich nowych obowiązków produktu ani nowych pytań do U. Nie wydajemy zbiorowego „pass” dla całych 57 REQ.

Uzasadnione powtórzenia w modelu: S2 pilnuje zatwierdzenia, S3 wcześniejszej weryfikacji; S7a aktualnej gotowości, S7b chwili odbioru, S10 historii po odbiorze; S13 zakresu rekordu roboczego. S15 i L4 współdzielą budżet odrzuceń wersji — L4 już odsyła do S15. Nie należy usuwać jednej z własności tylko dlatego, że wymienia ten sam licznik. Skrót DoD w PLAN jest pochodny wobec pełnego WLASCIWOSCI; E3-AC określają sposób dowodzenia, a RC zakres naszego mapowania. Potrzebna jest zgodność znaczenia, nie usunięcie wszystkich powtórzonych słów.

### 8.5 Rozliczenie naszych AC bez tworzenia drugiej specyfikacji

| AC | Co odsyła do istniejącego zobowiązania | Konkretyzacja lub proponowane rozszerzenie |
| --- | --- | --- |
| 01 | DoD 1/8, hierarchia KATALOG, INT i decyzje | Mapa zakresu jest sposobem rozliczenia; szersza granica briefu nie została przyjęta |
| 02 | YAML + DoD 1/3; tożsamość, wersja, predecessor, S10 | Task/Run/material/result poza obecnym rdzeniem: propozycja informacji, nie warunek odbioru E3 |
| 03 | Kontrakty YAML/wykonawcy, DoD 2/3/9; odmowy i atomowy krok | Trwały magazyn, odporność na przerwanie i idempotencja dotyczą przyszłego adaptera, jeśli będzie objęty zakresem |
| 04 | S4–S7, S10–S14; E4 w DoD 9 | Dla modelu używać dokładnego S i oczekiwanego stanu. Świeżość testu rzeczywistego pliku i rozumienie sprzecznej prozy wymagają osobno wybranego przypadku operacyjnego |
| 05 | DoD 2–5, E3-AC03–05/08; G/S/L/F | Nie nowy katalog właściwości. Odwołanie do aktualnych L/F po DEC-PRO-017, zamiast kopiowania starej gwarancji |
| 06 | DoD 6/9; E3-AC02/06 oraz TDD z PLAN | Osobna wyrocznia doprecyzowuje metodę. Wyjątek G5 wymaga AUD-03; nasze AC go nie rozstrzygają |
| 07 | DoD 7, WIT1–5, E3-AC07 | Awarie trwałego zapisu i semantyczny konflikt kontekstu nie są automatycznie częścią WIT. Symulowany W04 to krok aktora U; prawdziwa decyzja U dotyczy późniejszego przeglądu/odbioru świadków, nie każdego kliknięcia fabuły |
| 08 | DoD 9, karta celu; rozróżnienie simulation i rzeczywistego wykonania | Powiązanie realnego uruchomienia z materiałem należy doprecyzować w E4/E5; nie dowodzą go same pola evidence. Mechanizm tożsamości nie został przyjęty |
| 09 | Karta celu: wznowienie i możliwość podjęcia działania; E5 | Próba odczytu jest konkretyzacją. Obowiązkowy zestaw nowych widoków byłby wyborem rozwiązania, nie zatwierdzonym już wymaganiem |
| 10 | DoD 5/10, E3-AC08/09 | Odtworzenie i rozliczenie recenzji konkretyzują dowody; nie zastępują podpisu U |

DoD modelu rozliczamy nadal osobno: 1 → G0; 2 → G1–G6 z niejasnością G5; 3 → 16 właściwości S; 4 → L1–L5/F według DEC-PRO-017; 5 → OBS/bounds; 6 → macierz mutacji z AUD-03; 7 → świadkowie i ich przegląd U; 8 → G6/adnotacje, bez obietnicy pełnej zgodności ISO; 9 → wspólny YAML oraz rzeczywista historia w E4; 10 → R i U. E3-AC01/02 konkretyzują relację i zgodność, 03 bezpieczeństwo, 04 CTL L1, 05 pozostałe L/F, 06 czułość, 07 świadków, 08 odtwarzalność, 09 recenzję. Nie zmieniają same z siebie kryterium nadrzędnego.

RC-01–07 mają zachować własne wyniki mapowania: kontrakty, dwie migawki, legalne kroki/odmowy, wpływ zmiany, granica formalizacji, czułość oczekiwań i odtwarzanie/R. Ich obecne spełnienie nie jest siedmioma dodatkowymi „zaliczonymi” punktami DoD całego modelu. Raport RC pozostaje dowodem przedmiotu opisanego jego hashami.

### 8.6 Co uruchomiono i jak odtworzyć ustalenia

Uruchomiono inwentaryzację Git, skan nagłówków Markdown, ekstrakcję REQ/AT i dokładne porównanie zdań `text:`: **57 REQ, 55 AT, 0 identycznych zdań, MIG-01/02 bez AT, 57 statusów initiated**. To kontrola struktury i podobieństwa dosłownego; semantyczne pary oceniono ręcznie powyżej.

Próba AUD-02 odbyła się w świeżym lokalnym klonie `dd8f353` w katalogu tymczasowym, bez zapisów w źródłowym repozytorium. Do indeksu kopii dodano `audit-control.md` i `reference/audit-control.md` o tej samej treści: `[Kontrola](audit-missing/never-exists.md)`. Nie utworzono commita. Dla każdego pliku wykonano `python3 -B template/process/tools/check_refs.py <ścieżka>`:

```text
audit-control.md:
  audit-control.md:1: brak ścieżki „audit-missing/never-exists.md”
  check_refs: 1 plików, 1 błędów, wyjątków użytych 0
  exit = 1
reference/audit-control.md:
  check_refs: 0 plików, 0 błędów, wyjątków użytych 0
  exit = 0
```

Do odtworzenia wystarczają wskazany commit, dwa podane pliki i polecenie; żadna ścieżka `/private/tmp` nie jest częścią dowodu. Próba pokazuje świadome wyłączenie, a nie uszkodzenie skanera. AUD-01 oceniono przez odczyt AT, słownika, decyzji i `snapshot`; nie uruchamiano ponownie copiera. Nie powtarzano pytest, TLC ani dawnych dowodów tylko z powodu zmian w prozie. W szczególności liczby z E3.5 są wynikami zastanego raportu, nie testami tego audytu.

**Kontrola zapisu audytu:** `make check` zakończone kodem 0: 252 elementy, 0 błędów; wcześniejsze W1 MIG-01/02 oraz W2 dla nowego D-86 bez commita. Osobna kontrola ośmiu zmienionych Markdown: 140 lokalnych odnośników do istniejących plików, sześć odwołań do kotwic audytu, domknięte bloki kodu; 0 błędów. Pierwszy prosty skaner linków błędnie potraktował dosłowny przykład brakującej ścieżki wewnątrz kodu jako link dokumentu; po wyłączeniu treści kodu kontrola przeszła. Innych kotwic nie walidowano. `git diff --check` bez błędów; drugie repozytorium pozostało czyste. Te kontrole nie zatwierdzają semantyki wymagania.

### 8.7 Zalecenia i punkt wznowienia

**Jedyny bieżący plan działań po audycie — D-87, 2026-10-30.** Opiekun: agent. Zakres tego planu to obsługa ustaleń audytu, nie zastąpienie planu wydania szablonu ani PLAN drugiego projektu. Decyzje U są w [rejestrze decyzji](../../project/decisions.md); przebieg i dowody w §8.8; krótki wskaźnik bieżącej pracy w [briefie](brief.md). Pozostałe dokumenty odsyłają tutaj zamiast utrzymywać własną kopię tabeli.

Statusy: `proposed` — przygotowana propozycja, bez zlecenia wykonania; `planned` — wykonanie zlecone, nierozpoczęte; `in_progress` — rozpoczęte; `blocked` — rozpoczęte lub zlecone, zatrzymane konkretną przeszkodą; `completed` — rezultat i sprawdzenie zapisane. Zakończenie techniczne nie oznacza odbioru U. Lokalne identyfikatory A-01–03 oznaczają działania, nie nowe wymagania. Przy zmianie statusu, zakresu lub kolejności dopisz przyczynę i dowód w §8.8; zmianę przyjętego ustalenia powiąż z rzeczywistą decyzją U.

| Działanie / przedmiot | Właściciel / status | Zależności i upoważnienie | Rezultat i warunek zakończenia | Następny krok |
| --- | --- | --- | --- | --- |
| **A-01 — szablon:** doprecyzowanie UPD-04/AT-40 i LAY-03 (AUD-01/02) | Agent / `completed` | D-88: „Dalej” po wskazaniu A-01. Korekta zgodna z wyjątkami D-53/D-64, bez zmiany narzędzi | UPD-04/AT-40 mają jawne wyjątki; LAY-03 i wejście AT-45 wskazują zakres kontroli. Przypadki zgodne z przyjętymi wyjątkami, kontrola dokumentów bez błędów; dowód Z-05 | Brak dalszej pracy w A-01; nie zmieniać statusu REQ na verified/approved na podstawie samej korekty |
| **A-02 — model:** jednoznaczne rozliczenie G5 (AUD-03) | Agent przygotowuje rozstrzygnięcie, U decyduje / `proposed` | Aktualny DoD i decyzje drugiego projektu; uzgodnienie przed zamknięciem tego kryterium. Nie zależy technicznie od A-01 i nie blokuje całego E3. Zmiana w drugim repozytorium wymaga właściwego upoważnienia | Jeden pełny DoD i pochodny skrót. Koniec: jawny zbiór właściwości wymagających mutantów oraz osobny dowód przeglądu G5; zachowany odbiór historycznego E2 | Przy zamykaniu DoD przedstawić U rekomendację poniżej, sprawdziwszy, czy sprawy nie rozstrzygnięto już w źródle |
| **A-03 — model:** dalsza realizacja według aktualnego źródła (AUD-04/05) | Agent / `proposed` | Odczyt aktualnych PLAN/STAN, E3-AC i właściwego zlecenia przed kontynuacją. E3.5 już istnieje. D-85 pozostaje osobnym odbiorem naszego mapowania | Poprawnie wybrany następny przyrost z planu źródłowego, bez powtarzania translacji i rozszerzania E3 o operacyjne propozycje. Koniec tego działania: zapisany aktualny przedmiot, podstawa upoważnienia i odsyłacz do źródłowego planu; nie zakończenie całego E3 | Przy zleceniu kontynuacji sprawdzić bieżące źródło; propozycje operacyjne z §8.5 rozpatrzyć dopiero we właściwym zakresie E4/E5 |

Kolejność A-01 → A-02 → A-03 jest kolejnością rekomendacji audytu; zależności i moment decyzji podano osobno. Nie ustanawia nowego harmonogramu drugiego projektu. Utrzymanie to aktualizacja jednego wiersza i dopisanie wyniku przy rzeczywistej zmianie. Obecne kontrole nie wystarczają: dla A-01 składnia EARS i link AT nie wykrywają szerszego kwantyfikatora; dla A-02 raport N/A nie rozstrzyga dosłownego „każda”; dla A-03 niezależne kopie planu już spowodowały nieaktualną instrukcję wznowienia.

**Zastosowana korekta A-01 — D-88, wynik Z-05:** UPD-04 i AT-40 wyłączają z ochrony plik copiera i metadane git; notatka wymagania zachowuje ochronę także plików ignorowanych. LAY-03 ogranicza obowiązek do objętych kontrolą plików i rozpoznawanych lokalnych odwołań; notatka odsyła do zakresu D-64(3) i opisu `check_refs.py`, a AT-45 jawnie wymaga śledzonego dokumentu objętego kontrolą. Źródła REQ uzupełniono o odpowiednie decyzje. Pozytywny przypadek aktualizacji może zmienić answers; zmiana README poza pakietem nadal wymaga odmowy. Próby skanera z §8.6 nadal ilustrują właściwą granicę 1/0; nie ponawiano ich w A-01. Kod i wyjątki nie zostały zmienione.

**Gotowa rekomendacja dotycząca G5 — wymaga decyzji U w modelu:** DoD 2 rozdzielić na testy G1–G4/G6 i przegląd raportu kompletności G5; DoD 6 zastosować do G0–G4/G6, S i L wymagających badania, z jawną tabelą właściwość–mutant–naruszenie. G5 zachowuje obowiązek kompletnego raportu i jego przeglądu, bez fikcyjnego mutanta. To propozycja usunięcia sprzeczności, nie decyzja podjęta przez autora audytu; termin eskalacji: przed zamykaniem kryterium, nie przed samym czytaniem źródeł.

**Wykonane porządkowanie:** datowany audyt dopisano do istniejącej mapy, a punkty wejścia odsyłają do niego i aktualnego źródła modelu. Następnie w A-01 doprecyzowano dwa istniejące REQ i dwa teksty AT; nie tworzono kolejnego katalogu wymagań, nie zmieniono DoD, pakietu procesu, modelu ani Kitchen. D-85 pozostaje otwarte; commit wymaga osobnego polecenia. Pozostałe sprawy z §6 zachowują właścicieli i moment decyzji.

**Decyzja agenta A4, 2026-10-30 — zapis z audytu:** użyć historii Git do doboru źródeł i wykluczenia powtórnej pracy, ale oceniać aktualne znaczenie; raport zachować w istniejącej mapie, zamiast mnożyć specyfikacje. Zaproponowana wtedy korekta A-01 została później zlecona w D-88 i wykonana (Z-05); prace w modelu wymagają odczytania jego aktualnego stanu i właściwego upoważnienia, nie przenoszenia starego polecenia.

### 8.8 Rejestr zmian i wykonania

Dopisuj zdarzenia w kolejności wykonania. Plan w §8.7 pokazuje aktualny zamiar i status; ten rejestr zapisuje fakty i wyniki. Korekta wcześniejszego wyniku jest nowym wpisem wskazującym poprzedni, nie zmianą dawnych danych. Zgody nie powstają przez wpis agenta — wskazujemy decyzję U w rejestrze projektu. Lokalne numery Z-01… identyfikują wpisy, nie commity ani rekordy odbioru.

| Wpis / data / podstawa | Działanie i powód | Zmienione pliki | Sprawdzenie i rzeczywisty wynik |
| --- | --- | --- | --- |
| Z-01 / 2026-10-30 / D-86; wpis retrospektywny przy utworzeniu rejestru | Wykonano audyt i poprawiono odsyłacze do aktualnego stanu, ponieważ kryteria i instrukcje kontynuacji zaczęły się rozchodzić. A-01/02 pozostały propozycjami; nie zmieniono REQ/DoD | `coverage-map.md`, `acceptance.md`, `brief.md`, `release-cycle.md`, `release-cycle-report.md`, `reference/process-simulator/progress.md`, `project/decisions.md`, wygenerowany `reports/trace.md` | Szczegóły i granice w §8.6: próba skanera 1/0, `make check` 252 elementy / 0 błędów, osobne linki i diff poprawne. To wcześniejsze wykonanie, nie nowe uruchomienie |
| Z-02 / 2026-10-30 / D-87 | Utrwalono plan z właścicielami, statusami, zależnościami i warunkami zakończenia; dodano rejestr oraz drogę wejścia po kompakcji. Nie zastosowano proponowanych poprawek | `AGENTS.md`, `coverage-map.md` §8.7–8.8, `brief.md`, `project/decisions.md`; odświeżenie `reports/trace.md` przez narzędzie | Zapis przygotowany; kontrola dokumentów i przejścia od instrukcji startowej do następnego kroku do wykonania |
| Z-03 / 2026-10-30 / D-87, sprawdzenie Z-02 | Zakończono utrwalenie i kontrolę drogi wznowienia. Odczyt autora: AGENTS → brief → plan/rejestr/decyzje pozwala wskazać A-01, właściciela, status propozycji, granicę zlecenia D-87 i brak commita; to przegląd dokumentów, nie próba nowej niezależnej sesji | Wynik dopisany tutaj; brief odsyła do tego wpisu. `reports/trace.md` odświeżony przez `make check` | `make check`: kod 0, 253 elementy, 0 błędów; W1 MIG-01/02 i W2 D-86/87 bez commitów. Cztery dokumenty: 83 lokalne linki, cztery kotwice mapy i bloki kodu poprawne. `git diff --check` bez błędów. Zlecenie utrwalenia wykonane; statusów A-01–03 nie podniesiono. Bez testów niezmienionego kodu, commita i pushu |
| Z-04 / 2026-10-30 / D-88 | Rozpoczęto A-01 po poleceniu „Dalej”. Sprawdzono wyjątki D-53/D-64, zakres `check_refs.py`, `snapshot` testów dystrybucji i istniejące REQ/AT. A-01 zmieniono z `proposed` na `in_progress` | `project/decisions.md`, plan §8.7 i ten rejestr; dalsza zmiana obejmie `spec/requirements.md` i tekst AT | Przegląd źródeł potwierdza korektę dokumentacji bez zmiany kodu; wynik końcowy jeszcze nieustalony |
| Z-05 / 2026-10-30 / D-88, zakończenie A-01 | Zastosowano korekty UPD-04/AT-40 i LAY-03/wejścia AT-45. Przegląd autora: chronione pliki, w tym ignorowane, odpowiadają `snapshot`; answers i `.git/` są wyłączone; niedozwolona zmiana README nadal odpowiada odmowie UPD-03/AT-39. LAY-03 rozróżnia zakres skanowania i wyjątek ścieżki | `spec/requirements.md`, `spec/tests/process-kit.feature`, `project/decisions.md`, plan/rejestr, punkt wznowienia w `brief.md`; `reports/trace.md` wygenerowany | `make check`: kod 0, 254 elementy, 0 błędów; W1 MIG-01/02 i W2 D-86/87. Tekst oraz kod istniejących przypadków porównano, bez ponownego uruchomienia dystrybucji i prób skanera. Brak zmian kodu/runnerów: nie deklarujemy TDD RED/GREEN ani nowej regresji produktu. A-01 `completed`; REQ nadal `initiated`. Bez commita i zmian drugiego repozytorium |

**Decyzja agenta A5, 2026-10-30 — stan przy D-87:** statusy A-01–03 pozostają `proposed`, ponieważ D-87 zatwierdza organizację pamięci pracy, nie wykonanie napraw ani kontynuację innego projektu. Pełny plan utrzymuję tylko w §8.7; brief wskazuje bieżącą pozycję, a Git zachowuje historię redakcji. Późniejsza zmiana A-01: Z-04 / D-88.

**Decyzja agenta A6, 2026-10-30:** w A-01 doprecyzować także warunek wejściowy AT-45, aby kryterium LAY-03 jawnie dotyczyło śledzonego pliku objętego skanowaniem; zachować runner i zachowanie. Dla zmiany wyłącznie dokumentacyjnej wykonać kontrolę składni/śladu i przegląd zgodności z istniejącymi przypadkami, bez sztucznego RED/GREEN.

**Końcowa kontrola zapisu A-01:** cztery dokumenty, 82 lokalne odnośniki, cztery kotwice audytu i bloki kodu — bez błędów; `git diff --check` bez błędów. Diff `template/` i `tests/` pusty. To kontrola dokumentacji, nie ponowne wykonanie runnerów z katalogu AT.
