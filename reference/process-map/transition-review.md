# Prześledzenie W02 przez inżyniera weryfikacji procesu

2026-10-26. Przegląd dokumentacyjny [przykładu](worked-transition.md), z osobną recenzją kontrprzykładów. Nie jest wdrożeniem adaptera, odbiorem ani przeglądem produktu Kitchen. Mandat: polecenie użytkownika „wejdz w role i wykonaj” po propozycji tych dwóch czynności.

## Plan i kryteria zakończenia

1. Odczytać źródła i oddzielić istniejący model od postulowanych kontroli repozytorium.
2. Przejść instancję i odmowy; zapisać tabelę warunek → dowód → wynik → luka.
3. Osobny subagent, bez historii rozmowy i tej analizy, szuka kontrprzykładów w pierwotnym przykładzie i źródłach. Zachować jego wynik oraz rozliczyć uwagi.
4. Skorygować wykazane błędy opisu, zapisać ograniczenia i punkt wznowienia.

Zakończenie: każdy warunek ma źródło, oczekiwany wynik i status sprawdzenia; uwagi recenzenta mają rozstrzygnięcie; niewdrożone reguły nie są przedstawione jako działające. Nie wymagamy pozytywnej oceny gotowości do implementacji.

## Źródła i zakres oceny

- [ISO §7.2 SI.O7 i uwaga 2](../../../iso-29110-5-1/chapters/07-software-implementation-si-process.md): cel weryfikacji i swoboda oceny. Uwaga nie wymaga dosłownie osobnego agenta ani nie dowodzi niezależności jego rozumowania.
- [ISO §9, tabela 35 WP.23](../../../iso-29110-5-1/chapters/09-description-of-work-products.md): zapis wykonania; lista pól „may include” nie jest obowiązkowym schematem.
- [Model, release_transitions W01–W04](../../../iso-model-state/model/process.yaml) oraz [execute_step, _check_evidence](../../../iso-model-state/src/isomodel/execution.py): faktyczna granica wykonawcy.
- [Testy test_forbidden_steps_are_atomic](../../../iso-model-state/tests/test_execution.py) i [stan projektu](../../../iso-model-state/docs/STAN.md): testy źródłowe i deklaracja postępu; nie utożsamiać ich z nowym uruchomieniem.

## Przejście krok po kroku — instancja dydaktyczna

Poniższe identyfikatory są przykładowe; nie oznaczają wykonania przeglądu rzeczywistego wydania.

1. **Zlecenie:** TASK-DEMO-REVIEW wskazuje REL-DEMO-1, materiał BASIS-DEMO-A i kryteria C1/C2 w ustalonej wersji. Operator nie musi ponownie zatwierdzać technicznego przeglądu objętego zakresem.
2. **Wykonanie:** RUN-DEMO-R odczytuje tę podstawę. Autor poprawia materiał w osobnym przebiegu; recenzent zapisuje oceny i ustalenia.
3. **Wynik:** VER-DEMO-1 wskazuje zlecenie, wykonanie, materiał, ocenę C1 i C2 oraz ustalenia. Sam status `pass` nie zastępuje tych odniesień.
4. **Kontrola przed przejściem:** porównuje zapis wyniku z oczekiwanym zleceniem i bieżącą podstawą. Brak, niezgodność lub nierozstrzygnięte kryterium oznacza brak W02 i komunikat o konkretnej przyczynie.
5. **Zmiana stanu:** dopiero pozytywny wynik kontroli pozwala utrwalić `reviewed` wraz z odniesieniem do oceny. Odbiór operatora pozostaje niewykonany.
6. **Wznowienie:** agent odczytuje zachowany wynik, podstawę i otwarte ustalenia. Nie rekonstruuje przeglądu z rozmowy. To wymagana własność przyszłego połączenia z repozytorium, nie obecna funkcja W02.

## Tabela autora: warunek → dowód → wynik → luka

M = mechanizm odczytany w kodzie; P = proponowana kontrola, bez implementacji. Wyniki P są oczekiwaniami, nie logami testów.

| Warunek | Źródło/dowód do sprawdzenia | Wynik kontroli | Status i luka |
| --- | --- | --- | --- |
| Dozwolony stan i rola | W02 `from: ready`, `actor: R`; execute_step | Inny stan lub A: odmowa przed zmianą wejściowego stanu | M; etykieta R nie identyfikuje rzeczywistej sesji |
| Wykonano właściwe zlecenie | TASK → RUN → VER; wynik musi istnieć i być czytelny | Brak raportu lub obce zlecenie: odmowa | P; W02 nie wymaga raportu |
| Oceniono właściwy materiał | Wydanie, zakres i wersje materiału w zleceniu i raporcie | Inne wydanie/wersja albo nieustalona podstawa: odmowa | P; sam HEAD z brudnym drzewem nie identyfikuje treści |
| Oceniono wszystkie wymagane kryteria | Wersja zestawu kryteriów zlecenia i wyniki dla każdego kryterium | Brak oceny, wynik pending/fail lub inna wersja kryteriów: odmowa | P; przykład nie definiuje dostatecznie źródła i wersji zestawu kryteriów |
| Nie pominięto blokujących ustaleń | Oceny kryteriów oraz powiązane ustalenia i ich aktualne rozstrzygnięcia | Sprzeczność `pass` z otwartym ustaleniem: odmowa | P; potrzebne jednoznaczne powiązanie ustaleń, nie tylko deklaracja „brak” |
| Wynik pozostaje aktualny przy zapisie | Oczekiwana rewizja stanu i oceniana podstawa porównane podczas zapisu | Zmiana w międzyczasie: brak starego W02 | P; kontrola tylko przed zapisem pozostawia wyścig |
| Wynik i stan przetrwają przerwanie | Odczyt po wznowieniu wskazuje zgodną parę stan–wynik | Awaria: bez częściowego sukcesu, ponowienie bez duplikacji | P; kopia stanu w pamięci nie daje trwałości |
| Przegląd nie udaje odbioru | W04 osobno od W02; actor U, stan reviewed | W02 kończy się bez odbioru | M w modelu; symulowane U/cytat nie są rzeczywistą zgodą |

## Kontrprzykłady autora i minimalne doprecyzowania

| Przypadek | Dlaczego dotychczasowy opis nie wystarcza | Minimalne doprecyzowanie | Koszt i ocena efektu |
| --- | --- | --- | --- |
| Raport ocenia C1, C2; wymagany zestaw zmieniono na C1, C2, C3 | Same ID kryteriów albo ich liczba nie wiążą oceny z obowiązującą treścią | Zlecenie wskazuje wersję kryteriów, a wynik odnosi się do niej; zmiana wymaga oceny wpływu | Jeden odnośnik do istniejącej wersji; przyszła próba odrzuca stary raport |
| Raport deklaruje `pass`, lecz powiązane ustalenie jest ponownie otwarte | Pole wyniku może być sprzeczne z rejestrem ustaleń | Sprawdzić stan ustaleń należących do tej oceny; nie przyjmować deklaracji zbiorczej bez odniesień | Powiązanie istniejącego ustalenia; przyszły test sprzeczności |
| Zapisano sam raport i zmienił się commit repozytorium | Porównanie całego HEAD może odrzucić przegląd niezmienionego produktu | Porównywać określony zakres oceny, nie automatycznie całe repo | Dobór istniejącej reprezentacji zakresu; test braku fałszywej blokady |

To doprecyzowania proponowanego adaptera. Nie wdrażają manifestu, mechanizmu zgód ani nie zmieniają ostrzegawczego W5. Jakość samego osądu, kompletność wiedzy domenowej i rzeczywista niezależność nie wynikają z poprawności tych powiązań.

## Osobna recenzja i sprawdzenia

### Rzeczywiście uruchomiona diagnostyka modelu

Wynik: [transition-diagnostic.json](transition-diagnostic.json). [Skrypt odtworzenia](check-transition-example.py) kopiuje źródła, model i fixture WIT1 do nowego katalogu tymczasowego i wykonuje tam diagnostykę; repo źródłowe pozostaje tylko do odczytu. Log zachowuje SHA-256 odczytanych plików, datę UTC i wersję Pythona. Nie wymaga zachowania katalogu tymczasowego.

Z korzenia iso-template-agent, z już istniejącym środowiskiem modelu, bez instalacji:

```sh
../iso-model-state/.venv/bin/python -B reference/process-map/check-transition-example.py ../iso-model-state
```

27 kroków fixture WIT1 prowadzi do ready. Każda próba poniżej startuje niezależnie z tego samego osiągniętego stanu; dwie ostatnie dodają P00 przed W02. Nie wstrzykiwano stanu ready. Wszystkie siedem prób z asercjami wyników i nienaruszenia stanu wejściowego przeszło; polecenie zakończyło się kodem 0. Pięć pierwszych wykonano przed otrzymaniem recenzji, dwie ostatnie dodano na jej podstawie.

| Próba | Zaobserwowany wynik |
| --- | --- |
| W02, R, bez pola evidence i bez raportu | reviewed, acceptance = null |
| W02, A | Odmowa actor; wejście bez zmian |
| W04, U, przed W02 | Odmowa state; wejście bez zmian |
| W03, R, findings = [q1] | in_preparation; q1 open, blocking = true |
| W02, R, aktualne wejście tests_ok = false po wcześniejszym W01 | reviewed; ta operacja nie ponawia warunku tests_ok |
| P00 tworzy otwarte pytanie blokujące po W01, następnie W02 | reviewed mimo nowej blokady |
| P00 tworzy pytanie nieblokujące po W01, następnie W02 | reviewed; samo pytanie nie zatrzymuje operacji |

**Korekta potwierdzonego błędu opisu:** poprzedni przykład wyciągnął z zaległej informacji o pokryciu W03 w STAN.md zbyt mocny wniosek o braku wykonania. Odczytany kod obsługuje W03 i wykonana próba to potwierdza. Nie dowodzi to pełnego pokrycia W03 ani kompletnego procesu naprawy w repozytorium.

**Nowa luka specyfikacji adaptera:** samo „wydanie nadal ready” nie dowodzi aktualności wszystkich przesłanek W01. Konkretny przykład: po przygotowaniu wydania pojawia się negatywny wynik testów dla tego samego materiału. Piąta próba przekazuje takie wejście; model nadal dopuszcza W02. Trzeba wskazać, które nowe wyniki i blokady unieważniają gotowość oraz skąd adapter je odczytuje. Minimalnie: ponowna ocena obowiązujących przesłanek gotowości na aktualnych wynikach przy przejściu, bez zmiany istniejącego YAML w ramach tej pracy. To brak w propozycji połączenia z repozytorium, nie automatycznie defekt abstrakcyjnego W02 względem jego aktualnej specyfikacji.

To diagnostyka zachowania istniejącego modelu, nie RED/GREEN implementacji, pełna regresja ani wykonanie rzeczywistego przeglądu wydania. Pozostałe próby adaptera (stary raport, zmiana kryteriów, wyścig zapisu, awaria trwałości) są analizą, bo adapter nie istnieje.

### Osobny recenzent

Recenzję wykonał subagent `/root/review_transition`, uruchomiony bez historii autora. Dostał przedmiot, źródła i kryteria; nie otrzymał powyższej tabeli ani wyników diagnostyki przed własną oceną. [Oceniana treść przed korektami](evidence/worked-transition-before-review.md), SHA-256: `d5db4a20c457566f0f5ce70778a557744146067517ab460426fbdcdd636eab20`. To archiwalna kopia bajt w bajt: względne odnośniki w niej należy interpretować z pierwotnego katalogu process-map/, nie z evidence/.

[Pełna odpowiedź recenzenta](evidence/reviewer-response.md) została zapisana bez zmiany treści. Numery linii dotyczą kopii przed korektami. Recenzent wykonał tylko odczyt; diagnostykę uruchamiał prowadzący. Osobny kontekst nie zapewnia niezależności poznawczej ani braku wspólnych błędów modelu AI.

| Uwaga recenzenta | Rozstrzygnięcie autora | Dowód / skutek |
| --- | --- | --- |
| 1. Błędny opis braku obsługi W03 | Przyjęta; skorygowano §3, §7 i status wykonania | Kod, test źródłowy test_release_findings.py i rzeczywista próba W03 potwierdzają obsługę symulacyjną |
| 2. Nowa blokada po W01 | Przyjęta jako brak specyfikacji adaptera; dopisano ponowną ocenę gotowości i parę prób blokujące/nieblokujące w §5 i §8 | Dwie dodatkowe próby modelu potwierdzają, że obecne W02 dopuszcza oba przypadki; przyszły adapter nie jest testowany |
| 3. Wersja kryteriów | Przyjęta; doprecyzowano podstawę oceny i wpływ zmiany treści przy zachowanym ID | Poprawka opisu i przyszły przypadek testowy; brak implementacji porównania |
| 4. Każda usterka kontra tylko blokująca | Przyjęta; ujednolicono §7 z tabelą §5 | Ustalenie dopuszczone przez obowiązujące kryteria samo nie blokuje; nie daje agentowi prawa przyjęcia ryzyka |

Wartość osobnej recenzji w tej próbie: autor również wykrył W03 i wersję kryteriów, lecz nie zapisał sprzeczności „każda usterka” i nie podał konkretnej sekwencji P00 po W01. Recenzja dostarczyła tych dwóch nowych punktów. Nie wyliczamy z tego ogólnej skuteczności agentów ani kompletności przeglądu.

Ten sam recenzent odczytał następnie poprawiony przykład i potwierdził zamknięcie wszystkich czterech uwag: [odpowiedź z kontroli zamknięcia](evidence/reviewer-closure.md). Nie oceniał całej specyfikacji adaptera ani raportu prowadzącego. Nie zastępujemy tego wyniku własnym stwierdzeniem autora o niezależnym zatwierdzeniu.

Kontrola dokumentacji: `make check` zakończone kodem 0; [log](evidence/transition-document-check.log). Kontrola dotyczy repozytorium szablonu, nie potwierdza funkcjonalności proponowanego adaptera. Odnośniki w reference/ sprawdzane osobno, ponieważ są poza główną kontrolą śladu.

Końcowe sprawdzenie: 66 lokalnych odnośników bez braków; zachowana kopia zgadza się ze wskazanym SHA-256; źródła modelu nadal odpowiadają skrótom z diagnostyki. Zapis: `evidence/transition-links-check.txt`. `git diff --check` bez błędów. `make check`: 248 elementów, 0 błędów, 4 znane ostrzeżenia (MIG-01/MIG-02 bez AT, D-81/D-82 bez wzmianki w commicie).

## Wynik i dalsze sprawy

Prześledzenie zakończone; cztery uwagi rozliczono w opisie. Reguły powiązań i odmowy można mechanizować, lecz istniejący model nie dowodzi wykonania rzeczywistej recenzji. Dokument nadaje się do dalszego objaśniania i przygotowania specyfikacji adaptera; nie jest jeszcze kompletną specyfikacją jego implementacji.

| Sprawa pozostająca otwarta | Właściciel | Kiedy i następny krok |
| --- | --- | --- |
| Wiążące źródła materiału, kryteriów, wyników i blokad | Agent | Przed propozycją implementacji rozpoznać istniejące zapisy projektu i wskazać jeden spójny sposób odczytu |
| Trwałość, konflikt zmian i powiązanie uruchomień z rolami | Agent | Przed implementacją wybrać minimalny mechanizm oraz przygotować testy awarii i odmowy; bez uruchamiania nowej infrastruktury teraz |
| Polityka nowych blokad i kryteriów wyniku pozytywnego | Agent → użytkownik, jeśli zmienia przyjęte reguły | Zestawić propozycję z mandatem i istniejącymi kryteriami; nie uznawać poprawki edukacyjnej za zatwierdzenie nowej polityki |

Nie zmieniono template/, iso-model-state ani Kitchen; nie implementowano adaptera, manifestów ani mechanizmu zgód. Bez commita i pushu.

## Decyzje agenta i punkt wznowienia

- 2026-10-26, decyzja agenta: osobna ocena w reference/process-map/; nie tworzyć VER/ACC dla fikcyjnego wydania. Powód: przeglądamy propozycję edukacyjną, nie produkt objęty rejestrem formalnych odbiorów.
- 2026-10-26, decyzja agenta: recenzent bez historii rozmowy, tylko odczyt źródeł i własny raport; bez wglądu w powyższą analizę przed sformułowaniem własnych uwag. Powód: ograniczenie sugerowania wniosków autora.
- 2026-10-26, decyzja agenta: diagnostyka istniejącego modelu na kopii w katalogu tymczasowym, z trwałym skryptem i logiem w tym repozytorium. Powód: rozstrzygnąć różnicę między opisem a kodem bez zmiany źródłowego projektu i bez zależności od zachowania katalogu tymczasowego.
- Właściciel: agent; następny krok edukacyjny: pokazać użytkownikowi różnicę między „jest ID”, „jest raport” i „raport nadal ma zastosowanie”. Zmiana modelu, kodu produkcyjnego i mechanizmów procesu poza zakresem tego zadania.
