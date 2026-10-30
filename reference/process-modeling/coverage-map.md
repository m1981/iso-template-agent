# Mapa kryteriów, istniejącego modelu i braków

2026-10-29 · D-83 · wykonanie polecenia „commit(y), a następnie Dalej”. Analiza i ograniczone próby na kopii; bez zmian reguł modelu i bez odbioru za operatora.

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
