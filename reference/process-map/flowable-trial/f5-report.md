# F5 — wznowienie i ocena dopasowania

2026-11-06 · D-99 · wynik techniczny, nie odbiór użytkowy.

Późniejsza ocena: [bilans wobec Pythona, 2026-11-08](#bilans-wobec-pythona--2026-11-08). Rozdziela historyczny wynik F5, późniejszą próbę karty i odczyt PY-01; nie nadpisuje dawnych dowodów.

**Wynik:** po zamknięciu JVM nowy proces odczytuje tę samą sprawę, kontynuuje pracę i zachowuje wcześniejszy odbiór. Flowable dostarcza rzeczywisty mechanizm trwałego sterowania zadaniami. Własny kod nadal odpowiada za znaczenie rewizji, ślad, aktualność wyników i dozwolone polecenia. To dodatni wynik ograniczonej próby, nie wybór platformy produkcyjnej ani dowód kompletności procesu ISO.

## Co dostarczono

- EngineSession: wspólna konfiguracja oraz H2 plikowe, jawne create/reopen; przy reopen `IFEXISTS=TRUE` i `databaseSchemaUpdate=false`.
- ChangeTrial: wznowienie zapisanych definicji i parentDeploymentId DMN, bez redeployu i inicjalizacji sprawy; odmowa przy innych XML lub niejednoznacznym zestawie modeli.
- Testy w osobnych JVM, polecenie `resume-demo`, raporty stanu i historii z bazy. Brak nowej biblioteki lub serwera; H2 pozostaje testową zależnością.
- Zaktualizowane [diagramy](architecture.md) i [instrukcja](README.md#f5--jak-odtworzyć-i-obejrzeć-próbę).

Baza lokalnego demo autora pozostaje w `.runs/f5-20261106/process.mv.db`, na etapie oczekującego odbioru. Można ją odczytać przez `./resume-demo show f5-20261106`. Trwały eksport do czytania niezależnie od tej bazy: [stan po wznowieniu, przed odbiorem](evidence/f5-restart/07-show.json.md). Baza jest ignorowana przez Git; instrukcja tworzenia nowej próby i testy są w repozytorium.

## Kryteria i dowody

| Kryterium | Wynik i dowód | Granica |
| --- | --- | --- |
| F5-01 Restart i tożsamość | PASS: 10 kolejnych JVM, każda zakończona kodem 0. Porównano instancje, taskId, stan i historię caseState, zadania, definicje/parent DMN i historię DMN. [GREEN](evidence/f5-green.log), [eksporty](evidence/f5-restart) | Poprawne zamknięcie, ten sam build; nie awaria zasilania |
| F5-02 Kontynuacja i korekta | PASS: po wznowieniu fail przeglądu → prepare; nowe rewizje/wyniki → accept bez automatycznego odbioru. Dawne wyniki zachowane; ponowienie skutecznego ID komendy odmówione | Wyniki w scenariuszu są fikcyjne, TextStats nie był uruchamiany |
| F5-03 Odbiór i następca | PASS: jawny fikcyjny odbiór i nowa instancja; dwa odczyty po kolejnych restartach zachowują stary odbiór, nowy zakres oczekuje zgody | Nie oznacza rzeczywistego odbioru użytkownika |
| F5-04 Odmowy | PASS: brak bazy, próba ponownego create, zmieniony BPMN/DMN, powielone definicje, magazyn bez modeli i niedozwolona składnia ścieżki | Wznowienie jednej pary modeli, bez migracji |
| F5-05 Widok | PASS technicznie: raport zawiera podstawę, wyniki, historię i zadanie. Odczyty nie zmieniają sprawy ani historii DMN. Osobny agent prawidłowo odczytał stan bez XML | Czytelność dla operatora nadal wymaga jego obserwacji |
| F5-06 Odtworzenie i ocena | Recenzent: 58/58 PASS, 2 własne kontrprzykłady PASS i 8/8 wywołań demo. [Raport R](evidence/f5-review/review.json) | Odbiór użyteczności przez użytkownika nie został wykonany |

### TDD i próby usterek

- Pierwszy kompilujący się [RED](evidence/f5-red.log): **5 testów, 5 porażek asercji, 0 błędów**. Stub otwierał wyłącznie wariant pamięciowy.
- Po dopisaniu dwóch granicznych przypadków: [GREEN całej regresji](evidence/f5-green.log) **58/58**, w tym 7 testów F5 i 51 wcześniejszych. Bez pominiętych testów.
- [Odtworzenie RED](evidence/f5-red-replay.json): **7 porażek asercji / 0 błędów**. Skrypt dodaje tylko kompilujący stub później wprowadzonego API openFile; pierwotne źródła RED są zachowane.
- [Cztery celowe usterki](evidence/f5-faults.json): **4/4 wykryte asercją**, bez błędów kompilacji/infrastruktury: pamięć zamiast pliku, zezwolenie na aktualizację schematu, pominięcie porównania XML, wybór pierwszej z wielu definicji. Test schematu sprawdza konfigurację; dodatkowy test recenzenta sprawdza również faktyczne zachowanie bazy bez schematu.
- Historyczny odtwarzacz F4 dostosowano: na kopii pomija klasy testów F5, których dawne API nie miało. Odtworzono **13 porażek asercji / 0 błędów**; nie rozszerza to dowodu F4 na wszystkie ścieżki.

Pierwsza próba skryptów Python zatrzymała się na niespójnym lokalnym libexpat Homebrew 3.14; ponowienie działającym `/usr/bin/python3` 3.9.6 dało powyższe wyniki. Pierwszy wrapper demo wymagał nieobecnego offline pluginu dependency; zastąpiono go istniejącym Surefire. Nie zaliczano tych błędów środowiska jako RED produktu, nie instalowano nic systemowo.

## Osobne odtworzenie

Recenzent pracował na własnej kopii, współdzieląc jedynie cache narzędzi. Oprócz regresji uruchomił własny [ReviewerPersistenceTest](evidence/f5-review/ReviewerPersistenceTest.java):

1. Istniejąca surowa H2 zawierająca tylko tabelę SENTINEL: reopen odmawia, nie tworzy schematu Flowable i nie zmienia danych.
2. Dodatkowy deployment BPMN z samym plikiem tekstowym: reopen odmawia mimo tylko jednej definicji procesu.

Dowody: [log regresji](evidence/f5-review/verify.log), [log kontrprzykładów](evidence/f5-review/counterexamples.log), [wyniki poleceń demo](evidence/f5-review/manual-results.json), [sumy odczytanych wejść](evidence/f5-review/reviewed-inputs.sha256). Wszystkie przeniesiono do repo; stare ścieżki w logach opisują miejsce uruchomienia, nie warunek odtworzenia.

Aby powtórzyć własne testy R, na **osobnej kopii próby** skopiuj ReviewerPersistenceTest.java z evidence/f5-review do src/test/java/org/example/processlab, a następnie wykonaj `./verify -o -Dtest=ReviewerPersistenceTest test`. Instrukcja regresji i demo jest w README. Recenzent nie zmieniał źródłowego repozytorium.

Odczyt agenta z raportu: OPERATOR czeka na odbiór CAP-01@2, AT-01@3 i CODE-01@3; kontrole PASSED, wcześniejszy FAIL zachowany, odbioru brak. Zgłosił niejasność „brak aktywnego upoważnienia”: instrukcja wyjaśnia teraz, że poprzednia zgoda została wykorzystana (ALLOW/APPLY), a nie pominięta. Brak otwartych blokerów technicznych w granicach próby. Osobna sesja nie gwarantuje niezależności rozumowania; jej wartość tutaj to własne przypadki i własne uruchomienie.

## Co zapewnia silnik, a co trzeba utrzymywać samemu

To inwentaryzacja tej implementacji, nie uniwersalna klasyfikacja możliwości Flowable ani porównanie produktywności.

| Potrzeba | Mechanizm rzeczywiście użyty | Własna praca / koszt utrzymania |
| --- | --- | --- |
| Zadania, oczekiwanie, pętle korekty | Flowable BPMN i zapytania Task/History | Jeden XML: 5 user tasks i delegat kwalifikacji; utrzymanie dopuszczonych poleceń fasady |
| Trwałość i historia | H2 + persistence/historia FULL Flowable, wspólna transakcja BPMN/DMN | Konfiguracja create/reopen, kontrola zgodności modeli; nie własny SQL magazynu domenowego |
| Jawna kwalifikacja faktów | Flowable DMN, tabela UNIQUE i audyt | 5 reguł DMN; adapter pilnuje definicji i wyniku. Fakty dostarczają funkcje domenowe |
| Rewizje, ślad, aktualność | Nasze rekordy i Rules, niezależne od silnika | Model referencji, BFS, dobór podstaw i porównania wyników — tego Flowable nie wyprowadza ze znaczenia tekstów |
| Komendy i decyzje | Nasza fasada + aktywne zadanie silnika | Wersja stanu, ID polecenia, rola, taskId, kontrola podstawy przy odbiorze; role są nadal deklaracją harnessu |
| Widok dla operatora | Nasz raport z publicznych usług i caseState | Format raportu i objaśnienia; brak gotowej aplikacji operatora i automatycznej oceny użyteczności |

Jedna zmiana w fabule wymaga wskazania nowej treści wymagania, testu/programu, wyników ocen i decyzji. Fasada dopisuje rewizje, zmienia current, wiąże nowy test z wymaganiem i zapisuje polecenia; silnik zmienia zadania oraz historię. **Nie edytujemy ręcznie kilku kopii statusu.** Nadal trzeba dostarczyć sensowne dane i oceny, a obecny Prepare obsługuje tylko wybrany test/program — nie ogólny projekt wielomodułowy.

Koszt próby: utrzymanie Java/Maven i bibliotek Flowable/H2/Jackson, dwóch modeli XML oraz naszych reguł/raportu. F5 zmieniło dwa pliki kodu głównego; dodało 7 testów i lokalny harness/skrypty, bez nowej zależności. Nie mierzono czasu obsługi przez użytkownika, oszczędności ani przewagi ekonomicznej nad Pythonem. Liczby testów nie są miarą dojrzałości procesu.

**Rekomendacja:** zakończyć rozbudowę techniczną tej próby na F5 i sprawdzić użyteczność otrzymanego widoku. Mechanizm trwałych zadań wnosi wartość, ale nie uzasadnia jeszcze migracji całego procesu lub budowy REST/UI. Jeśli operator nie potrafi ustalić stanu i następnego kroku, poprawiać najpierw konkretną niejasność widoku.

## Granice i następny krok

Nie sprawdzono utraty zasilania, awarii dysku, backupu/odtwarzania, migracji schematu/modelu/JSON, współbieżnych klientów, tożsamości ani odporności na celową zmianę bazy. Porównanie XML nie dowodzi zgodności innego kodu Java. Próba nie jest kompletnym ALM, wykonaniem Kitchen ani dowodem poprawności programu TextStats. Nie aktywuje P1/P2 ani nie zmienia istniejących W5/E9 w szablonie.

**Otwarte:** użytkownik ocenia zrozumiałość [raportu oczekującego odbioru](evidence/f5-restart/07-show.json.md); agent zapisuje konkretne trudności i proponuje najmniejszą poprawkę, jeżeli wystąpią. Bez udawania, że niezlecony test z użytkownikiem już się odbył. A-06 w mapie rozdziela zakończenie techniczne i otwartą ocenę użytkową. Inne historyczne decyzje pozostają w swoim rejestrze.


Kontrola końcowego zapisu: `make check` — 265 elementów, 0 błędów, ostrzeżenia W1 MIG-01/02 i W2 D-99 (bez commita F5). Sprawdzono 190 lokalnych odnośników w sześciu dokumentach, bez braków; kotew nie walidowano. Wszystkie osiem diagramów wyrenderowano; zmienione widoki przechowywania obejrzano. R odczytał również końcowy raport i podtrzymał granice wyniku; doprecyzowano, że istniejące W5/E9 pozostają bez zmian.


## Obserwacja użytkownika — 2026-11-07

Użytkownik zgłosił, że nie rozumie interpretacji 07-show, a identyfikatory i nazwy niewiele mu mówią. Jako możliwą przyczynę wskazuje mały udział w całym przebiegu — nie traktujemy tego jako ustalonego wyjaśnienia. Dotychczasowy pozytywny odczyt agenta nie wystarczył do potwierdzenia czytelności dla operatora. Nie udzielono odbioru użyteczności; dowody techniczne pozostają aktualne. Właściciel: agent; następny krok na prośbę U to objaśnienie struktury funkcji, zadań, produktów pracy i zależności w znanym mu ujęciu narzędzi projektowych. Nie zlecono jeszcze przebudowy widoku.

## Bilans wobec Pythona — 2026-11-08

A-16, na zlecenie U po uporządkowaniu repozytorium. **Flowable wniósł gotowe mechanizmy wykonywania workflow, ale nie wykazaliśmy przewagi całego rozwiązania dla operatora nad Pythonem.** Trwałość i transakcje nie są jego wyłączną korzyścią: w drugim repo istnieje już osobny prototyp Python/SQLite. Poniżej porównanie tego, co rzeczywiście zbudowaliśmy, a nie wszystkich możliwości platformy Flowable.

### Podstawa i chronologia

- `5471272` (2026-10-24): L1 w Pythonie — przejścia, warunki, historia, rewizje, odczyt/eksport/import i interfejs przeglądarkowy. [session.py](../../process-simulator/app/session.py) odtwarza komendy; [server.py](../../process-simulator/app/server.py) utrzymuje sesję w pamięci i serializuje jej zmiany blokadą. To działające mechanizmy, nie tylko wcześniejsza propozycja z technical-plan.md.
- `8fa127b` (2026-11-06): zapis F1–F4 — Java/Flowable, własny model/reguły, DMN i wykonywalny BPMN. `16f5ff8` (2026-11-07): F5, trwały zapis i wznowienie. Daty commitów wskazują zapis paczek; praca opisana w raportach zaczynała się wcześniej.
- `cf7bdb6` / `ca8f336` (2026-11-08): własny formatter karty, jej dowody i wynik ograniczonej próby czytelności. To nie UI otrzymane od Flowable. Operator nie rozumiał początkowego raportu; po poprawkach i pomocy odpowiedział „przyjmuje” w ćwiczeniu. Nie wykazano samodzielnej użyteczności całego narzędzia.
- Odczyt `iso-model-state` przy **HEAD f74f55f**, czysty katalog roboczy: oprócz referencyjnego modelu Python/TLC istnieje **PY-01, src/isowork/**. Commit `858fb23` (2026-11-04) wprowadził trwałe CLI Python. [README, PY-01](../../../../iso-model-state/README.md) wyraźnie odróżnia je od całego modelu v0.7 i zaznacza brak odbioru wydania. Nie wolno przypisać jednemu prototypowi łącznego zakresu wszystkich narzędzi Python.

Odczytano kod, testy i istniejące wyniki; nie uruchamiano teraz Java, Pythona, TLC ani nowego scenariusza porównawczego. To nie benchmark, certyfikacja równoważności ani nowy odbiór drugiego projektu.

### Co rzeczywiście zapewniło Flowable

| Obszar | Wkład biblioteki/silnika w naszej próbie | Nadal nasza odpowiedzialność |
| --- | --- | --- |
| Przebieg i zadania | Instancja BPMN, aktywne zadania z ID, oczekiwanie, zakończenie zadania, przejście do następnego i historia zadań | [change.bpmn20.xml](src/main/resources/change.bpmn20.xml): sami opisaliśmy 5 user tasks, rozgałęzienia i powroty. Nazwa userTask nie uruchamia agenta |
| Trwałość | Zapis danych silnika, stanu zadania i historii do H2; wspólna granica transakcji przy synchronicznym zakończeniu zadania i kwalifikacji | Konfiguracja, JSON caseState, create/reopen, odczyt/walidacja modeli, sens historii produktu; brak testu awarii zasilania i migracji |
| Tabela decyzji technicznych | Wykonanie DMN UNIQUE i zapis historii/audytu jego wykonania | [qualification.dmn](src/main/resources/qualification.dmn): 5 napisanych przez nas reguł. `basisKnown/conflict/failed/pending` oblicza własny WorkflowChecks/Rules. TO_OPERATOR nie jest decyzją odbiorczą |
| Atomowy krok | `TaskService.complete` zapisuje przekazane zmienne i kontynuuje BPMN/DMN; wybrany wyjątek cofa skutki tego kroku | [ChangeProcess](src/main/java/org/example/processlab/workflow/ChangeProcess.java): sami umieściliśmy zapis w tej granicy. [F4_06 w teście](src/test/java/org/example/processlab/ChangeProcessTest.java) sprawdza wyjątek po kwalifikacji. Nie jest to dowód bezpieczeństwa wieloklientowej aplikacji |
| Zapytania o wykonanie | Publiczne usługi Task/History/Runtime, identyfikatory definicji i instancji | Fasada, raport i dobór właściwego zakresu. Nie uruchomiliśmy gotowych aplikacji Modeler/Task/Admin/IDM ani REST/CMMN |

**Sami napisaliśmy:** model rewizji i relacji, analizę wpływu BFS, ocenę aktualności/konfliktów, związanie wyniku z podstawą, sprawdzanie komend/wersji/roli, ponowne sprawdzenie przed odbiorem, zachowanie poprzedniego odbioru, reguły kwalifikacji, raport i kartę. Flowable przechowuje i wykonuje ich wybrany workflow, ale nie wywodzi tych zasad z ISO, kodu produktu lub rozmowy.

### Co już dawał Python i czego nie porównano jeden do jednego

| Potrzeba | L1 Python w tym repo | Python w iso-model-state | Flowable F1–F5 |
| --- | --- | --- | --- |
| Legalne przejścia i odmowy | Własny silnik jednej lekcji | Referencyjny wykonawca modelu; osobno ograniczone reguły PY-01 | BPMN + własna fasada/reguły. Ponowne pokrycie znanej potrzeby, lecz innym sposobem |
| Rewizje, wyniki, zachowanie historii | Istnieją jako dane lekcji | Referencyjny model ma m.in. WIT3/WIT5; PY-01 ma własny węższy agregat | Własne rekordy Java i historia sprawy; nie automatyczna funkcja interpretacji ISO |
| Restart i trwały stan | Po ręcznym eksporcie/import odtwarza polecenia. Bez eksportu restart serwera traci sesję | [PY-01 store.py](../../../../iso-model-state/src/isowork/store.py): SQLite, stan i receipts, odczyt przez nowe połączenia | Wznowienie sprawy i aktywnego taskId z H2 w kolejnych JVM; wyraźna korzyść wobec samego L1 |
| Atomowość | Walidacja/nowy stan i blokada w obrębie działającego serwera; nie transakcja dyskowa | PY-01: BEGIN IMMEDIATE, aktualizacja stanu i receipt w jednej transakcji; [testy](../../../../iso-model-state/tests/test_py01_store.py) wstrzykują wyjątki po obu zapisach | Wspólna transakcja wybranego kroku BPMN/DMN i danych; nie unikalna zdolność języka Java lub Flowable |
| Ponowienie komendy | Lekcja sprawdza dozwolone akcje; to nie taki sam kontrakt sieciowego retry | PY-01 zwraca poprzedni wynik identycznego żądania; odmawia innego żądania pod tym samym ID | Własna fasada odmawia ponowienia skutecznego commandId. Po wycofanym błędnym kroku można ponowić. **Inna semantyka, nie równoważne API** |
| Wygoda operatora | Interaktywna lekcja w przeglądarce, graf i historia | PY-01 CLI; osobne raporty modelu | Techniczny raport, następnie własna karta archiwalnego eksportu. Flowable nie dostarczył nam gotowego czytelnego interfejsu |

PY-01 ma kontrolowane testy współbieżnych zapisów oraz komend z nieaktualną rewizją. W próbie Flowable współbieżni klienci pozostali poza zakresem. Sam większy silnik nie uzasadnia przypisania naszej fasadzie gwarancji, których nie sprawdziliśmy. Z drugiej strony PY-01 nie wykonuje odbioru wydania; nie należy uznać go za pełny zamiennik F5 bez porównania kontraktów.

### Co pokrywa zakres próby, a co pozostaje luką

Próba pokrywa **jedną syntetyczną sprawę zmiany wymagania**: zgodę → zastosowanie → przygotowanie testu/programu → zapis ocen i kwalifikację → korektę albo decyzję operatora; następnie powiązaną nową sprawę i ochronę wcześniejszego odbioru. Daje trwałe oczekiwanie i odczyt stanu. To nie pełny PM/SI, prowadzenie backlogu, automatyczne kodowanie, wykonywanie rzeczywistych testów TextStats/Kitchen, integracja Git/agentów, uwierzytelnianie ani dowód zgodności procesu.

Wspólna luka pozostaje: dane `PASS` w fabule nie są zaufanym dowodem wykonania zewnętrznego testu. Pole roli nie dowodzi tożsamości. Dodatkowo późniejsza koncepcja karty wymaga analizy przed decyzją, a obecny BPMN zaczyna od zadania authorize; nasz formatter objaśnia tę różnicę, nie zmienia workflow. Źródło: [mapa pól, §3–4](../operator-preview/textstats-card-data-map.md).

### Ocena wartości i rekomendacja

1. **Potwierdzona wartość techniczna:** działający silnik standardowych definicji BPMN/DMN, trwałe zadania z historią i wybrany atomowy krok. F5 udokumentowało 10 kolejnych JVM; F4_06 sprawdza wycofanie skutków wyjątku. Nie musieliśmy implementować własnych tabel życia zadań i zapytań historii silnika.
2. **Potwierdzona wartość poznawcza:** próba pokazała granicę między mechaniką workflow a znaczeniem danych/dowodów. Gotowy silnik nie usunął kosztu specyfikacji reguł ani problemu czytelności. To użyteczny wynik eksperymentu, choć nie korzyść produkcyjna dla Kitchen.
3. **Niewykazana przewaga:** brak porównania kosztu utrzymania, czasu wznowienia i liczby błędów operatora na tym samym zadaniu w obu rozwiązaniach. Nie wolno przypisywać Flowable całej trwałości i reguł jako nowości wobec obecnego Pythona. Część funkcji zrealizowaliśmy ponownie we własnym kodzie Java.

**Rekomendacja:** zachować próbę i dowody, nie migrować teraz całego procesu na Flowable. Dla kolejnego rzeczywistego zadania wykorzystać istniejące narzędzia projektu; nie uruchamiać dwóch równoległych implementacji procesu. Do wyboru silnika wrócić, jeśli pojawi się konkretna potrzeba utrzymywania wielu trwałych zadań/instancji lub wykonywania wspólnych definicji BPMN/DMN, której koszt w prostszym rozwiązaniu zostanie wykazany. Wtedy porównać ten sam kontrakt i scenariusz, w tym retry, restart i czytelność — obecne próby mają różne zakresy.

Koszt Flowable w naszej próbie: Java/Maven, biblioteki i ich konfiguracja, modele XML oraz nadal własne reguły i widoki. Python także wymaga utrzymania swojego wykonawcy i zapisu. Nie zmierzono przewagi kosztowej żadnej strony. Rekomendacja nie zmienia stosu, planu ani przyjętych decyzji drugiego projektu i nie otwiera nowego benchmarku.
