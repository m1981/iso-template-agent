# P3: mapa kontraktu na model zachowania

2026-11-08 · A-23 · **mapowanie półformalne, nie uruchomiony model ani nowa instrukcja procesu**.

Przedmiot: zapis końcowego wyniku jednego kryterium wcześniej zarejestrowanej próby. Źródło zachowania: [kontrakt P3 §11.3–11.7](worked-transition.md#113-kontrakt-operacji-record_check_result). Ta mapa przygotowuje mały model TLA+, nie zastępuje kontraktu. Apostrof oznacza stan po akcji; formuły poniżej to pseudonotacja, nie plik do TLC. Identyfikatory M/O/V/E/B są lokalne dla tej mapy; T01–T12 pochodzą z P3.

**Sens dla operatora:** system może zapamiętać „stary test przeszedł”, a jednocześnie pokazać „nowa wersja nie została jeszcze sprawdzona”. Ponowienie zgłoszenia po zerwaniu połączenia nie powinno tworzyć drugiego wyniku ani odbioru.

## 1. Co wykorzystujemy, a czego nie przenosimy

Odczyt `iso-model-state`: HEAD `f74f55f2ea68d30fca22b4ddf7c9d05eb9ad82cb`, czyste drzewo. Ścieżki poniżej wskazują żywe pliki; wersję analizy określa ten commit. Nie zmieniono drugiego repo.

| Źródło / miejsce | Przydatny wzorzec | Granica ponownego użycia |
| --- | --- | --- |
| [E3.5 — mapowanie §4–7](../../../iso-model-state/docs/E3-05-MAPOWANIE.md) | Niezależne oczekiwania, pełny skutek i pola niezmieniane, legalne przebiegi, celowe uszkodzenia, oddzielenie granicy badania od odmowy | Metoda; dawne 28 przejść nie jest specyfikacją P3 |
| [tla_process.py: validate_schema, emitowane Init/Next, Boundary](../../../iso-model-state/src/isomodel/tla_process.py) | Jawny stan, relacja kroku, kontrola historii i ograniczeń | Generator jest związany ze schematem item/question/release. Nie ma tu gotowej relacji `record_check_result`; nie importować go jako silnika P3 |
| [store.py: execute](../../../iso-model-state/src/isowork/store.py) | Potwierdzenie sprawdzane przed wersją, porównanie treści, transakcja i punkty wstrzykiwania awarii | Inspiracja do przyszłych testów implementacji. Magazyn zapisuje sukcesy; nie realizuje pełnego kontraktu odmów/wykonań P3. Actor/digest nie dowodzą uwierzytelnienia |
| [Flowable: F4_04](flowable-trial/src/test/java/org/example/processlab/ChangeProcessTest.java) i [ChangeProcess.execute](flowable-trial/src/main/java/org/example/processlab/workflow/ChangeProcess.java) | Stare polecenie odrzucone, stare oceny można zachować bez zaliczenia nowej podstawy | `Assess` oraz odmowa ponowionego ID mają inne granice niż P3; test nie jest dowodem nowej operacji |
| [PLAN: DEC-PRO-028](../../../iso-model-state/PLAN.md) | Właściwa moc historycznych rezultatów | E3/E4 zakończone jako badania bez odbioru; nie przywracamy obowiązku ich ukończenia |

**Decyzja agenta:** ponownie użyć sposobu specyfikacji i doświadczeń z ponowieniami, bez kopiowania generatora i bez nowego języka YAML/DSL. Koszt utrzymania: mapa do kontraktu i jeden mały model, jeżeli jego wykonanie zostanie zlecone. Obecne przykłady nie badają dowolnej kolejności zmiany, zapisu i ponowienia; temu ma służyć próba modelu.

## 2. Stan i jawne wejścia spoza modelu

| ID / nazwa | Dziedzina i znaczenie | Źródło |
| --- | --- | --- |
| M1 `executions` | Stała mapa ID → projekt, mandat, podstawa, kryterium. Podstawa to krotka identyfikatorów rewizji zlecenia, wymagania, testu, kodu i zestawu kryteriów | §11.2–11.3; A-19 |
| M2 `phase`, `results` | Stan próby `running/completed`; częściowa mapa ID próby → niezmienny wynik z odnośnikiem do zachowanego dowodu. Klucz próby ogranicza przekrój do jednego wyniku końcowego | §11.2–11.4 |
| M3 `currentBasis`, `contextKnown`, `controlRevision` | Bieżąca wymagana podstawa; dostępność jej wiążącego odczytu; wersja kontroli. Token i identyfikacja podstawy są różnymi rzeczami | §11.3–11.5; T09/T11 |
| M4 `receipts` | Częściowa mapa `(projekt, uwierzytelniony klient, request_id)` → niezmienna treść żądania i odpowiedź. Także zapamiętane odmowy dziedzinowe; brak retencji w pierwszej próbie | §11.4: to samo ID/treść, poprawka z nowym ID |
| M5 `pending`, `delivered` | Żądania w drodze z utrwalonym tokenem/treścią; obserwacja odpowiedzi. Umożliwia rozdzielenie zatwierdzenia zapisu i dostarczenia odpowiedzi | §11.4/7; T06–T08 |
| M6 `submissions`, `decisions` | Stałe migawki przykładowego zgłoszenia i wcześniejszej decyzji; nie zawierają nowych decyzji. Obserwujemy ich niezmienność | §11.3/11.5; D-78 |
| M7 `impact` | Dla istotnego negatywnego ustalenia: `unknown/applies/not_applicable`, z jawną podstawą oceny dostarczaną z zewnątrz | §11.5; T12 |

| ID / założenie | Co można badać w modelu | Czego model nie dowodzi |
| --- | --- | --- |
| E1 — uprawnienie i pochodzenie | Odrzucenie przy negatywnym/nieustalonym wyniku kontroli, także przy ponowieniu | Tożsamości klienta ani odporności kanału na fałszowanie |
| E2 — dowód | Porównanie deklarowanego wykonania/podstawy/kryterium/wyniku z zachowanymi metadanymi raportu; brak danych nie jest pass | Że log jest prawdziwy, runner sprawdził właściwy produkt lub kryterium jest trafne |
| E3 — trwały atomowy zapis | Skutki jednej zatwierdzonej operacji, awaria przed zatwierdzeniem i utrata odpowiedzi po nim | Odporności realnej bazy na awarię. Atomowość akcji jest założeniem, nie wynikiem TLC |
| E4 — kontekst i analiza wpływu | Konserwatywny odczyt przy braku wiedzy; brak cichego pomijania starego istotnego defektu | Prawidłowości kwalifikacji istotności, zależności i analizy wpływu przez człowieka/agenta |

Brak dostępnego magazynu/tokenu lub starego dowodu wyklucza zapis. Brak dostępnego *bieżącego zakresu* przy dostępnej podstawie próby nie musi wykluczać historii (T09). Nie modelujemy czasu, identyfikatorów Git, treści logów ani transportu HTTP; reprezentujemy tylko rozróżnienia potrzebne tym regułom.

## 3. Akcje i kolejność

`Init`: próby wcześniej zarejestrowane, w stanie running; brak nowych wyników/potwierdzeń, znana stara podstawa. Wariant z istniejącym bieżącym wynikiem powinien być osiągany przez tę samą operację zapisu, nie przez dopisanie pass do warunku początkowego. Zachowane zgłoszenie i odbiór są stałymi wejściami historycznymi.

| ID / akcja | Warunek i skutek | Pola chronione |
| --- | --- | --- |
| O1 `Send` | Klient odczytuje dostępny token, tworzy żądanie; dozwolone również błędne pola i stary token w próbach negatywnych | Cały stan dziedzinowy |
| O2 `ChangeContext` | Zewnętrzne, uprawnione zdarzenie zmienia bieżącą podstawę/dostępność/istotny kontekst; podnosi token. Zgoda na zakres jest przesłanką przykładu | Podstawy wykonanych/rozpoczętych prób, stare wyniki i decyzje |
| O3 `Handle` | Atomowo wykonuje uporządkowane rozstrzygnięcie poniżej, ponownie na bieżącym stanie | Wszystko poza wskazanym skutkiem danej gałęzi |
| O4 `DeliverOrLose` | Dostarcza albo gubi odpowiedź po obsłudze; nie cofa utrwalenia | Cały trwały stan |
| O5 `Retry` | Ponawia to samo żądanie/ID; po jawnej odmowie poprawione zgłoszenie przechodzi przez O1 z nowym ID | Stan dziedzinowy do ponownego O3 |
| O6 `AbortBeforeCommit` | Zakończenie próby obsługi bez trwałego skutku; klient może nie znać wyniku transportu | Cały trwały stan |

Półformalny wybór gałęzi O3 (pierwsza pasująca, zgodnie z §11.4):

```text
nieuprawniony lub nierozpoznane źródło -> odmowa bez ujawnienia receipt
znany key, inna treść                 -> REQUEST_ID_REUSED; receipt bez zmian
znany key, ta sama treść              -> zapamiętana odpowiedź; bez nowego wyniku
nieznany key, nieaktualny token       -> CONFLICT
nieznany key, błędna próba/podstawa/dowód/pola -> właściwa odmowa
w przeciwnym razie                   -> Record

Record:
  results'[execution] = wynik powiązany z executions[execution]
  phase'[execution] = completed
  receipts'[key] = (treść, recorded + ID + oceniona podstawa)
  controlRevision' = controlRevision + 1
  pozostałe wyniki i potwierdzenia bez zmian
  executions, currentBasis, submissions, decisions bez zmian
```

Odmowa dziedzinowa może dodać potwierdzenie odmowy, lecz nie wynik ani zakończenie próby. Nie wolno więc testować jej jako „żaden bajt magazynu się nie zmienia”. Potwierdzenie odmowy nie zmienia podstawy ani tokenu kontekstu; odwołanie uprawnień jest kontrolowane także przy replay. Równoległe wywołania O3 są w abstrakcji porządkowane atomowo. Udowodnienie, że kod rzeczywiście zachowuje tę kolejność i atomowość, będzie odrębnym zadaniem integracyjnym.

`Next` będzie wyborem jednej z O1–O6. Przy zmianie niezwiązanego dokumentu podstawa pozostaje identyczna; token może się zmienić. Zmiana tokenu powoduje odświeżenie polecenia, a nie automatyczne unieważnienie dowodu. Interpretacja istotnego ustalenia jest wejściem E4; P3 nie implementuje rozstrzygania sporu.

## 4. Własności i odczyty

| ID | Własność do zapisania w modelu | Rodzaj |
| --- | --- | --- |
| V1 `TypedAndBound` | Każdy wynik wskazuje istniejącą próbę, jej dokładną podstawę i kryterium; outcome należy do pass/fail/inconclusive | Niezmiennik stanu |
| V2 `HistoryPreserved` | Każdy wcześniejszy wynik i receipt pozostaje identyczny; zgłoszenia, decyzje i podstawy prób niezmienione | Własność kroku; do TLC monitor porównujący pre/post, nie samo sprawdzenie typu |
| V3 `SingleCompletion` | Dla każdej próby najwyżej jeden końcowy wynik; completed wtedy i tylko wtedy, gdy istnieje jej wynik w tym przekroju | Niezmiennik stanu |
| V4 `ReplayStable` | To samo uprawnione żądanie zwraca to samo potwierdzenie, mimo starego tokenu; inna treść klucza nie nadpisuje potwierdzenia | Własność kroku/odpowiedzi |
| V5 `GuardedWrite` | Nowy wynik pojawia się tylko przy wszystkich przesłankach z §11.4 i tokenie aktualnym w chwili zatwierdzenia; odmowa nie kończy próby | Własność kroku z kontrolą pełnego skutku |
| V6 `NoFalseCredit` | Wynik różnej lub nieznanej podstawy nie uzupełnia bieżącego kryterium; zmiana samych kryteriów również rozróżnia podstawy | Własność odczytu |
| V7 `NoFalseInvalidation` | Przy tej samej podstawie i znanym kontekście dopisanie starego pass bez istotnych ustaleń nie zmienia bieżącego pokrycia | Własność kroku/odczytu |
| V8 `NoHiddenFinding` | Istotne negatywne ustalenie o nieustalonym wpływie pozostaje widoczne jako niepewność; applied jako problem, niezależnie od nowszego pass | Własność odczytu, warunkowa względem E4 |

Minimalny odczyt jest parą: **pokrycie kryterium + stan ustaleń**, a nie jednym zielonym statusem. W pseudonotacji:

```text
Applicable(r) = unknown, jeśli !contextKnown
             = matches_basis, jeśli basis(r) = currentBasis
             = different_basis, w przeciwnym razie
MatchingPass = istnieje r: Applicable(r)=matches_basis i outcome(r)=pass
OpenImpact   = istnieje istotne ustalenie z impact=unknown
```

`MatchingPass` nie jest predykatem odbioru/gotowości przyrostu. Wyniki fail/inconclusive dla właściwej podstawy oraz ustalenia pokazujemy obok; nie ukrywamy ich przez znalezienie pass. Pełne rozstrzyganie konfliktów kilku aktualnych prób pozostaje poza P3. Nie dodajemy własności „operator kiedyś zaakceptuje”. Legalny zapis i retry muszą mieć osiągalne przykłady; brak naruszeń w modelu, który zawsze odmawia, byłby bezużyteczny.

## 5. Pokrycie wszystkich przypadków kontraktu

To przypisanie przyszłych sprawdzeń, **nie wyniki PASS**.

| Przypadek | Akcje / własności | Oczekiwanie i granica |
| --- | --- | --- |
| T01 | O2→O1→O3; V1/V2/V3/V6 | Stary wynik zapisany, bieżącego pokrycia brak; decyzje bez zmian |
| T02 | O1→O2→O3; V5 | Stary token odrzucony; nowe ID/token umożliwiają zapis tej samej starej podstawy |
| T03 | O1/O3; V1/V5, E2 | Raport starej próby skierowany do nowej odmówiony; porównujemy metadane, nie dowodzimy autentyczności |
| T04 | O1/O3; V1/V5 | Nieznane ID lub nieodtwarzalna podstawa odmówione |
| T05 | O2/O3; V6 | Podstawy różniące się wyłącznie kryteriami nie są zamienne |
| T06 | O3→O4(lose)→O5→O3; V3/V4 | Jeden wynik, to samo potwierdzenie; bieżący odczyt osobno |
| T07 | Dwa O1, przeplot O3; V3/V4/V5 | Różne żądania najwyżej raz zamykają próbę; zmiana treści tego samego klucza odmówiona |
| T08 | O6 lub O3→O4(lose); V2/V3/V4, E3 | Modeluje przed/po atomowym zapisie; rzeczywiste awarie częściowych zapisów wymagają testów magazynu |
| T09 | O2(contextKnown=false)→O3; V5/V6 | Dostępny token, magazyn i stary dowód: historia tak, stosowalność unknown |
| T10 | O1/O3; V2/V5, E1/E2 | Niedozwolone pola lub deklaracja zamiast dowodu odmówione; żadna akcja nie dopisuje odbioru |
| T11 | Zapis nowego wyniku→zapis starego pass; V6/V7 | Bieżące pokrycie pozostaje; osobny wariant zmiany tokenu bez zmiany podstawy |
| T12 | O3, odczyt M7; V2/V8, E4 | Stary istotny defekt nie znika; trafność analizy jego wpływu nie jest dowodem modelu |

## 6. Granica przyszłej próby i kryterium jej sensu

**B1 — mała rodzina konfiguracji, nie cały SDLC.** Jeden projekt i uprawniony klient plus wariant nieuprawniony; jedno kryterium; do dwóch wcześniej zarejestrowanych prób (stara/nowa). Trzy wartości podstawy: stara, zmieniona, różniąca się tylko kryteriami. W każdej konfiguracji dobiera się podstawy dwóch prób do przypadku; to nie jest dowód wystarczalności dwóch prób dla systemu ogólnego.

**B2 — żądania i tokeny.** Do trzech różnych kluczy żądań: odmówione, poprawione oraz konkurujące; ponowienie używa istniejącego klucza. Skończone reprezentanty poprawnych/błędnych treści, wszystkich trzech outcomes, dostępności i oceny wpływu. Granice licznika tokenu i liczby zmian muszą być jawne w konfiguracji; przekroczenie oznacza granicę badania, nigdy odmowę procesu. Dobór dokładnych zbiorów i koszt eksploracji zapisuje się przed uruchomieniem TLC.

**B3 — warunek zakończenia próby.** V1–V8 bez naruszeń w podanych granicach; osiągalny poprawny zapis starego wyniku i poprawny replay po utracie odpowiedzi; rozliczone T01–T12 (z granicami E1–E4); co najmniej mutacje: przypisanie latest zamiast podstawy próby, pominięcie wersji kryteriów, token przed replay, brak ochrony końcowego wyniku, automatyczny odbiór, pomijanie starego istotnego ustalenia. Każda mutacja ma powodować konkretną porażkę odpowiedniej kontroli, nie błąd składni lub timeout.

Nie przyjmujemy fairness ani niezawodności sieci, żeby obiecać ukończenie. Sprawdzamy bezpieczeństwo i istnienie legalnych ścieżek, nie zakończenie każdego przebiegu. Retencja receipts, anulowanie, wiele kryteriów, start runnera i implementacja adapterów są poza próbą. Wygaśnięcie receipt wymaga później osobnego przypadku; nie wolno przenieść na nie gwarancji V4 bez warunku retencji.

**Kolejny rezultat:** mały `.tla` z konfiguracjami i raportem granic/własności/kontrprzykładów. Nie generator całego ISO ani drugi silnik procesu. Zlecenie A-23 kończy się na tej mapie; nie zmienia źródła specyfikacji i nie uruchamia tej próby.

**Kontynuacja A-24:** U zlecił wykonanie rekomendowanej próby. Pakiet i odtworzenie: [p3-tla/README.md](p3-tla/README.md); wynik i granice: [raport](p3-tla/report.md). Historyczne sformułowania „przyszła próba” powyżej dokumentują mapowanie przed wykonaniem; nie nadają wynikowi statusu odbioru ani reguły produkcyjnej.
