# F5 — wznowienie i ocena dopasowania

2026-11-06 · D-99 · wynik techniczny, nie odbiór użytkowy.

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
