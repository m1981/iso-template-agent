# Sprawdzenie karty zmiany wymagania

Bieżąca karta: [zachowanie zmiany i historia przeglądu](#karta-zachowania--zmiana-wymagania-i-historia-przeglądu), 2026-10-30. Poniżej zachowano wcześniejszą próbę TST-02.

2026-10-27. Próba retrospektywna na rzeczywistej zmianie TST-02 z decyzji D-76. Nie jest nowym odbiorem, wdrożeniem karty ani niezależną recenzją. Nie zmienia kodu produktu lub pakietu procesu.

## Cel i kryteria próby

Ustalone przed ponownym uruchomieniem testów:

| Kryterium | Warunek zaliczenia |
| --- | --- |
| K1 Odtworzenie zmiany | Wskazane rzeczywiste zachowanie przed i po, przyczyna i źródło decyzji. |
| K2 Rozliczenie wpływu | Wskazane wymaganie, zadanie, kod, testy i dowody; brak danych pozostaje jawny. |
| K3 Sprawdzalne dowody | Powtórzenie zapisanej próby RED/GREEN na kopii oraz rozróżnienie nowych wyników od historycznych. |
| K4 Odporność na pochopne zamknięcie | Ręczne próby z brakującą zgodą, wynikiem testu i dowodem chronologii nie prowadzą do stwierdzenia pełnego zamknięcia. |

Sukces tej próby oznacza użyteczność diagnostyczną karty dla jednego przypadku. Nie oznacza, że karta zapobiegła historycznemu błędowi, jest mechanicznie egzekwowana lub sprawdzona w nowej sesji bez kontekstu. Bez pomiarów czasu, wydajności i harmonogramu.

## Plan sprawdzenia

1. Odtworzyć zmianę z decyzji, historii Git, planu, wymagania i testu.
2. Rozliczyć sześć kroków karty oraz dostępne dowody.
3. W kopii wykonać istniejące odtworzenie RED/GREEN; zapisać log i identyfikację wejść.
4. Wykonać ręczne kontrprzykłady, ocenić kryteria i wskazać najmniejszą korektę karty.

Decyzja agenta, 2026-10-27: użyć TST-02, ponieważ ma rzeczywisty defekt, decyzję operatora, diff wymagania i odtwarzalny test. Istniejąca próba obejmuje również sąsiednią poprawkę W5; zachowujemy jej zakres, aby nie przerabiać historycznej procedury.

## Źródła i odtworzenie

- [D-76 i D-80](../../project/decisions.md): autoryzacja naprawy, następnie osobna zgoda na commit.
- [TST-02](../../spec/requirements.md), [AT-49](../../spec/tests/process-kit.feature), [TSK-11](../../project/plan.md), [ślad](../../reports/trace.md).
- [Raport pierwotnej naprawy](../tdd/control-results/report.txt), RED/GREEN, regresja i odtwarzalna łatka w tym samym katalogu.
- `git show e63c8da -- spec/requirements.md spec/tests/process-kit.feature project/plan.md` pokazuje utrwaloną zmianę względem rodzica f24d5ed.
- Karta z rozmowy: opisz różnicę → ustal wpływ → rozstrzygnij → zaktualizuj zamiar → wykonaj i sprawdź → zamknij zmianę.

Powtórzenie testów: uruchomić blok `python3` z sekcji 3 raportu pierwotnej naprawy z katalogu głównego repozytorium. Kopia jest tworzona na nowo; żaden dawny katalog tymczasowy nie jest wymagany.

## Wypełniona karta

| Krok | Fakty i wynik |
| --- | --- |
| 1 Opisz różnicę | Przed: TST-02 wymagało samych wyników pass wskazanych przypadków. Raport mógł być zielony mimo kodu zakończenia runnera 1, 2 lub 7. Po: wszystkie przypadki muszą przejść i każdy użyty runner musi zakończyć się kodem 0. Powód: sprzeczność między zielonym raportem a błędem wykonania. |
| 2 Ustal wpływ | Zmiana TST-02 → AT-49 → przypadki test-report-exit-0/1/2/7 w test_tools.py → warunek oceny w test_report.py. Plan: TSK-11. Raporty śladu odsyłają do wymagania i testu; powiązanie z implementacją ustalono przez diff i odczyt kodu, nie przez pełny automatyczny ślad. |
| 3 Rozstrzygnij | D-76 zawiera polecenie naprawy w TDD, z zachowaniem ostrzegawczego W5 i bez rozszerzenia o manifesty lub zgody. D-80 później dopuszcza commit. Zgoda na naprawę i commit nie jest odbiorem produktu. |
| 4 Zaktualizuj zamiar | W e63c8da zapisano zmienione wymaganie i test oraz TSK-11 już jako completed. Historia Git nie rozstrzyga, czy plan poprzedzał wykonanie. Raport opisuje kolejność RED → poprawka → GREEN; obecne powtórzenie potwierdza czułość testów, ale nie dowodzi historycznej kolejności edycji. |
| 5 Wykonaj i sprawdź | Ponownie uruchomiono procedurę z raportu na kopii: RED 63 pass / 4 fail, kod make 2; GREEN 67 pass / 0 fail, kod 0. To rzeczywiste wyniki z 2026-10-27. |
| 6 Zamknij zmianę | Potwierdzona naprawa techniczna w sprawdzonym zakresie. Nie można na tej podstawie zadeklarować spełnienia wszystkich warunków karty, niezależnej weryfikacji ani odbioru. Nie zmieniono historycznego statusu TSK-11. |

## Rozliczenie wpływu

| Element | Dyspozycja | Dowód lub ograniczenie |
| --- | --- | --- |
| TST-02 i AT-49 | Zmienione | Diff e63c8da; obecna treść zawiera dodatkowy warunek kodu 0. Nadal mają status initiated. |
| test_report.py | Zmieniony i sprawdzony | Sprawdzenie rc != 0 przed uznaniem przypadków za sukces. Nowy RED/GREEN. |
| test_tools.py | Zmieniony i sprawdzony | Istniejące testy sprawdzają wynik AT, wynik procesu raportującego i powód porażki. |
| TSK-11 | Zapis wykonania istnieje; chronologia nieustalona | Plan i poprawka utrwalone razem, brak osobnej wcześniejszej wersji planu w badanym śladzie. Nie oznacza to dowodu, że planu nie było. |
| W5 i pre-commit | Ponownie sprawdzone jako sąsiednia zmiana | Historyczna łatka cofa obie naprawy. Test precommit-w5 daje fail w RED i pass w GREEN; sprawdza widoczność ostrzeżenia i nieblokujący kod 0. |
| Dystrybucja i złoty wzorzec | Odczyt historycznych wyników | Raport pierwotny: 18/18 i 31 plików bez różnic. Nie uruchamiano ich ponownie w tej próbie. |
| Test przeniesienia | Znane historyczne niepowodzenie | 7/9 także przed poprawką. Nie ma podstaw do deklaracji pełnego zielonego test-all. |
| Dawne raporty generowane wadliwym narzędziem | Wpływ nieustalony | Możliwe fałszywe pass wymagają oceny, jeśli mają służyć bieżącej decyzji. Nie wykazano tutaj konkretnego błędnego raportu rzeczywistego projektu ani nie zbadano wszystkich projektów korzystających z szablonu. Właściciel: agent; przed poleganiem na takim raporcie ustalić jego runner, kod wyjścia i potrzebę ponowienia. |
| Przegląd i odbiór | Niepotwierdzone osobnymi rekordami | records/verification.md zawiera VER-01 dotyczący odtworzenia repozytorium, nie TST-02. records/acceptance.md nie zawiera odbioru. Nie wolno wyprowadzać ich z testów ani ze zgody na commit. |

Brak migracji dokumentów uzasadniono niezmienionym formatem danych. Brak zmian w Kitchen wynika z zakresu D-76. Nie oceniano wdrożenia poprawki w projektach korzystających z szablonu.

## Rzeczywiście uruchomione sprawdzenie

[Surowy log](evidence/change-card-replay.log) i [identyfikacja wejść](evidence/change-card-replay.json). HEAD: `0a988e42d7beef6d085b659d6a2c01cd752a89ac`, Python 3.14.6. Metadane zawierają SHA-256 plików pakietu, wymagania, testu, decyzji, planu, instrukcji i łatki. To identyfikacja próby, nie nowy mechanizm manifestów procesu.

RED: fail dla precommit-w5 oraz test-report-exit-1, -2, -7; siedem komunikatów asercji dotyczy czterech przypadków. Przypadek kodu 0 przechodzi w obu fazach. GREEN: 67/67. Cała procedura zakończyła się kodem 0, ponieważ oczekiwany RED został rozpoznany, a GREEN przeszedł.

Przed i po uruchomieniu porównano treść istniejących plików oraz przygotowany do commita diff: bez zmian. Testy tworzyły lokalne repozytoria wyłącznie w kopiach tymczasowych. Nie wykonano commita ani pushu źródłowego repozytorium.

Kontrola dokumentacji po zapisaniu: osiem lokalnych odnośników raportu istnieje; parser logu potwierdził dokładnie cztery oczekiwane porażki RED i 67 sukcesów GREEN. `git diff --check` dla edytowanych README i punktu wznowienia bez błędów. `make check`: kod 0, 248 elementów, zero błędów, dwa istniejące ostrzeżenia W1 dla MIG-01 i MIG-02; odwołania i kontrola przecieku bez błędów. Te kontrole nie oceniają jakości rozumowania w karcie.

## Ręczne kontrprzykłady dla karty

Poniższe to oceny autora według zapisanej karty, nie wykonanie automatycznej bramki. Dokumenty źródłowe pozostały nietknięte; pominięcie oznacza ograniczenie zestawu dowodów rozpatrywanego w danym ćwiczeniu.

| Próba | Rozpatrywane dowody | Oczekiwany wynik i ocena |
| --- | --- | --- |
| Bez decyzji | Diff i GREEN, ale bez D-76 | Nie ustalono uprawnienia do tej zmiany. Krok 3 pozostaje otwarty; zielony test nie zastępuje decyzji. |
| Bez wykonania testu | Sama deklaracja raportu „naprawiono” i kod | Brak podstaw do potwierdzenia działania. Krok 5 pozostaje otwarty. |
| Z wynikiem RED | Log z CASE pass runnera, ale proces runnera kończy się błędem | Sprzeczny wynik wyklucza sukces. Faktyczne testy wykryły tę sytuację. |
| Bez dowodu kolejności | TSK-11 completed i implementacja w jednym commicie | Nie można potwierdzić wykonania kroku 4 przed krokiem 5. Wynik: nieustalone, a nie arbitralnie „plan był po kodzie”. |
| GREEN i zgoda na commit | D-76, D-80 i 67/67 | Potwierdzają uprawnione wykonanie i sprawdzenie techniczne; nie tworzą rekordu odbioru ani niezależnego przeglądu. |

## Ocena karty i minimalna korekta

K1 spełnione. K2 spełnione w zakresie odtworzenia zależności i ujawnienia niewiadomych; nie wykazano kompletności wszystkich zależności. K3 spełnione. K4 spełnione w ręcznej ocenie autora, ale nie zostało niezależnie ani mechanicznie sprawdzone. Wynik: karta przydatna do diagnozy tego przypadku; nie jest jeszcze zwalidowanym mechanizmem prowadzenia nowej zmiany.

Próba wykazała trzy potrzebne doprecyzowania samej propozycji karty:

1. **Przed wykonaniem ustal warunki zamknięcia:** potrzebne testy, przegląd, ewentualny odbiór oraz to, co będzie dowodem każdego z nich. Obecne „potrzebne sprawdzenia” jest zbyt otwarte i może prowadzić do dobierania kryteriów po obejrzeniu wyniku. Koszt: krótka lista w istniejącym zadaniu. Efekt do oceny: czy przy zamknięciu pozostaje spór o wymagany zakres sprawdzenia.
2. **Każda zależność ma dyspozycję i podstawę:** zmieniono, sprawdzono, bez wpływu z uzasadnieniem lub nieustalone z właścicielem. Uwzględnij wcześniejsze wyniki wytworzone wadliwym narzędziem. Sam ślad i W5 nie dowodzą ich wiarygodności. Koszt: wpis tylko dla elementów dotkniętych zmianą. Efekt do oceny: czy zostały nierozliczone zależności.
3. **Podsumowanie oddziela wykonanie, sprawdzenie i odbiór:** odbiór może być niewymagany dla konkretnej czynności, lecz musi to wynikać z ustalonego zakresu, a nie z braku wpisu. TSK completed i zielone testy nie wystarczają do wszystkich trzech ocen. Koszt: trzy krótkie pozycje, bez nowego rejestru. Efekt do oceny: czy nowa sesja potrafi poprawnie ustalić, co jeszcze wymaga decyzji.

To korekty propozycji do następnego użycia, nie aktywacja nowych reguł szablonu. Nie wprowadzamy obowiązku osobnego commita planu ani ponownej akceptacji dawnej naprawy. Nie dodajemy pomiarów czasu, wydajności lub prognoz harmonogramu.

## Punkt wznowienia

Próba zakończona. Następny krok właściciela karty (agent): przy najbliższej zatwierdzonej rzeczywistej zmianie zapisać wejścia i warunki zamknięcia przed wykonaniem, zastosować trzy doprecyzowania, a następnie sprawdzić wznowienie z plików. Użyteczność dla operatora i nowej sesji pozostaje do oceny podczas tego zastosowania; obecna próba autora nie zastępuje takiej obserwacji. Nie wybieramy nowej funkcji Kitchen ani nie rozszerzamy procesu API.

## Karta zachowania — zmiana wymagania i historia przeglądu

2026-10-30 · D-92 · A-04. **Opis obecnego zachowania oraz propozycje, nie nowe wymagania pakietu.** Sekcje powyżej pozostają historyczną próbą TST-02 z 2026-10-27. Ta karta dotyczy tylko `iso-template-agent`; nie zmienia planu Kitchen ani `iso-model-state`.

### 1. Cel, zakres i źródła

Operator ma wiedzieć: co zmieniono, jakie zapisy mogą wymagać ponownego sprawdzenia, co rzeczywiście sprawdzono i co pozostało historycznym wynikiem. Zielony hook odpowiada na pytanie o kontrolowane reguły zapisu, nie o zgodę na zmianę lub poprawność produktu.

| Podstawa | Co z niej wynika | Moc i granica |
| --- | --- | --- |
| [D-92 i D-78](../../project/decisions.md) | Przygotowanie karty; agent dobiera środki w zatwierdzonym zakresie, zgłasza brakujące decyzje | Ustalenia użytkownika. D-92 nie zatwierdza propozycji poniżej |
| [TRC-13, SEP-01/02](../../spec/requirements.md), [AT-12/22/23](../../spec/tests/process-kit.feature) | Nieblokujące W5; E9 dla nowego pass wraz ze zmianą badanego elementu; wyjątek pierwszego commita | Istniejąca specyfikacja szablonu; karta jej nie nadpisuje |
| [AGENTS P-06/P-08 i role](../../template/process/AGENTS.md), [rekordy VER](../../records/verification.md) | Zmiana zatwierdzonego wymagania wymaga decyzji; nowy przegląd to nowy rekord; autor nie recenzuje własnej pracy | Instrukcje. Nie wszystkie są egzekwowane przez narzędzia |
| [trace.impact](../../template/process/tools/trace.py), [E9](../../template/process/tools/check_separation.py), [fingerprint](../../template/process/tools/model.py) | Rzeczywista granica automatyzacji | Dowód implementacji, nie źródło zasadności wymagania |

Nie wyprowadzamy tu nowych obowiązków z ISO. Powiązania normatywne w istniejących instrukcjach nie zastępują decyzji o przyjęciu praktyki w naszym projekcie.

### 2. Dane i odpowiedzialność

Przed zmianą wystarczą odnośniki w istniejącym zadaniu do: wymagania i różnicy treści, podstawy upoważnienia, zależności, planowanych sprawdzeń oraz warunków zamknięcia. To propozycja użycia karty, nie obowiązek dodatkowego formularza.

- **Operator:** rozstrzyga zmianę zakresu, przyjęcie ryzyka, odbiór i wydanie; P-08 wymaga też decyzji dla zmiany zatwierdzonego wymagania. Bez potrzebnej decyzji agent może przygotować analizę i propozycję, nie przedstawiać zmiany jako zatwierdzonej.
- **Agent wykonawca:** aktualizuje zamiar i dotknięte artefakty, zbiera dowody, zgłasza nierozstrzygnięte zależności. Commit tylko na wyraźne zlecenie.
- **Recenzent:** ocenia wskazaną wersję według kryteriów; nowy wynik zapisuje jako nowy VER. Oddzielna sesja ogranicza dzielenie kontekstu autora, ale nie dowodzi niezależności osądu.
- **Narzędzie:** kontroluje strukturę, wybrane różnice i generuje widoki. E9 rozdziela zmiany między commitami, nie uwierzytelnia autora ani recenzenta.

Dla tej karty „zmiana treści” w W5/E9 oznacza zmianę tytułu lub sparsowanych pól poza `status`, zgodnie z `fingerprint`. Nie oznacza porównania całej zawartości pliku, kodu produktu ani wszystkich wejść testu. Migawki porównywane przez E9 to HEAD i indeks. W5 porównuje element i jego bezpośrednich rodziców z commitem dodającym wybrany zapis VER pass.

### 3. Kontrakt przebiegu

| Operacja | Warunek wejścia | Rezultat i zachowane informacje | Obsługa niepowodzenia |
| --- | --- | --- | --- |
| Opisz i zaplanuj zmianę | Znana potrzeba i istniejąca treść; decyzja dostępna, jeśli wymagana | Różnica przed/po i kryteria sprawdzenia zapisane przed wykonaniem; brak domyślnego zatwierdzenia | Niejasność trafia do operatora, jeśli zmienia zakres lub ryzyko; nie blokuje niezależnej analizy |
| Oceń wpływ | Znane ID, relacje i dostępne wersje | Każda rozpatrywana zależność: do zmiany, do sprawdzenia, bez wpływu z powodem albo nieustalone z właścicielem | Brak W5 nie wystarcza do wniosku „bez wpływu”; brakującą podstawę zapisujemy jawnie |
| Zmień i sprawdź | Praca w upoważnionym zakresie; uzgodnione kryteria | Zaktualizowane artefakty i wyniki sprawdzeń; dawny VER pozostaje opisem dawnego przeglądu | Błąd narzędzia lub testu nie staje się pass; poprawka i ponowienie właściwych kontroli |
| Przeprowadź nowy przegląd | Zmiana badanego elementu utrwalona przed nowym pass; wskazany przedmiot i kryteria | Nowy VER z rzeczywistym wynikiem. Recenzent ocenia również sens zależności | Fail prowadzi do korekty; nie przepisujemy go na pass. Kolejny przegląd tworzy kolejny rekord |
| Podsumuj zmianę | Rozliczone kryteria i zależności w przyjętym zakresie | Osobno: wykonanie, sprawdzenie, odbiór wymagany/niewymagany z podstawą. Historyczne wyniki i odbiory zachowane | Nierozstrzygnięty punkt pozostaje otwarty z właścicielem; zielony hook nie zamyka go automatycznie |

To kontrakt pracy do przećwiczenia. Kolejne operacje nie są jednym wdrożonym automatem. Aktualność dowodu oceniamy względem tego, co rzeczywiście badał; sam link i etykieta pass nie potwierdzają poprawności.

### 4. Przykłady i tabela reakcji

**Przykład dydaktyczny**, bez rekordów dopisywanych do projektu: `SC-01 → UC-01 → CAP-01 → AT-01`, gdzie strzałka oznacza podstawę produktu. CAP-01 i AT-01 mają wcześniejsze rekordy VER pass. Nie są to identyfikatory dowodów tej karty; przykładowy graf nie deklaruje rzeczywistego przeglądu naszych wymagań.

Założenia technicznych przypadków: istnieje HEAD, hook jest włączony, raporty są aktualnie wygenerowane i dodane do indeksu, pozostałe kontrole przechodzą. Każdy wiersz to osobny wariant. „Dopuszcza” dotyczy badanej kontroli, nie decyzji człowieka.

| Przypadek | Zdarzenie | Obecna reakcja / podstawa | Oczekiwanie karty lub propozycja |
| --- | --- | --- | --- |
| C1 | Zmiana treści CAP-01, bez nowego VER | W5 dla CAP-01 i AT-01, jeśli spełniają warunki historycznego pass; nie blokuje (TRC-13) | Rozliczyć wpływ; zachować oba dawne wyniki |
| C2 | Zmiana CAP-01 i dodanie nowego VER pass dla niego w tym samym commicie | Odmowa E9 (SEP-01, AT-22) | Rozdzielić wykonanie i przegląd; osobne commity nadal nie dowodzą niezależności recenzenta |
| C3 | Zmiana CAP-01 i nowy VER fail | E9 nie blokuje; W5 może pozostać (AT-22) | Zachować fail, wskazać korektę; nie deklarować zakończenia przeglądu sukcesem |
| C4 | Po commicie zmiany: nowy VER pass dla niezmienionego CAP-01, bez innych zmian | E9 dopuszcza. W5 może być widoczne przed commitem rekordu; po nim nowy pass staje się podstawą porównania | Ponowić trace po zapisie. Nowy VER tylko dla CAP-01 nie odnawia przeglądu AT-01 |
| C5 | Przepisanie starego VER fail na pass wraz ze zmianą CAP-01 | E9 pomija istniejące ID; W5 może ostrzec. Instrukcja VER zabrania przepisywania | **Propozycja P1:** mechaniczna ochrona historii, opisana poniżej |
| C6 | Zmiana SC-01; UC-01 i CAP-01 bez edycji | W5 dla UC-01, jeśli ma historyczny pass; brak przechodniego W5 dla CAP-01 | **Propozycja P2:** lista pośrednio zależnych kandydatów do oceny, nie automatyczne uznanie ich za błędne |
| C7 | Wyłącznie zmiana statusu CAP-01 | Nie wywołuje W5/E9 z tytułu zmiany treści; W3 może ostrzec o braku pass | Nie wyprowadzać zgody ani nowego przeglądu ze zmiany etykiety |
| C8 | Pierwszy commit z nowym elementem i VER pass | E9 ma wyjątek importu (SEP-02, AT-23) | Dopuszczenie importu nie potwierdza historii wykonania |
| C9 | Brak Git lub VER pass jeszcze bez commita | W5 nie ma takiej podstawy porównania i może nie powstać | Ocena aktualności pozostaje nieustalona; nie wnioskujemy „aktualne” z ciszy |
| C10 | Zmiana zatwierdzonego wymagania bez wymaganej decyzji | W5/E9 nie są kontrolą zgody; zapis może przejść | Instrukcja P-08: agent zgłasza brak decyzji. Ta karta nie dodaje mechanizmu zgód |

Odczyt kodu ujawnia dodatkową granicę: W5 wybiera rekordy pass, a późniejszy fail nie jest przez tę funkcję rozstrzygany jako bieżący wynik przeglądu. Ta karta nie definiuje globalnej „gotowości do wydania” na podstawie W5.

### 5. Dwie propozycje wymagające osobnego przyjęcia

| Propozycja / potrzeba | Dlaczego obecny mechanizm nie wystarcza | Minimalny mechanizm i sprawdzenie efektu | Koszt i decyzja |
| --- | --- | --- | --- |
| P1 Zachować historyczny VER | E9 bada nowe rekordy, a instrukcja „nie poprawiać wstecz” nie blokuje nadpisania | Porównanie istniejącego rekordu HEAD–indeks: odmowa zmiany treści lub usunięcia; korekta jako nowy rekord z odnośnikiem do poprzedniego. Test: nadpisanie fail→pass odrzucone, dopisanie kolejnego wyniku dopuszczone; formatowanie bez zmiany treści dopuszczone | Utrzymanie porównania oraz testów; dodatkowy wpis przy korekcie. Operator zatwierdza regułę przed implementacją. Szczegóły reprezentacji treści ustala agent, jawnie uwzględniając ograniczenia parsera |
| P2 Odciążyć ręczne śledzenie dalszych skutków | W5 sprawdza tylko bezpośrednich rodziców | Przejście po grafie zależności z odwiedzonymi węzłami; lista kandydatów bez duplikatów i z drogą od źródła zmiany. Próby: łańcuch, rozgałęzienie, cykl i element niezwiązany; ostrzeżenia nadal nie blokują | Koszt algorytmu/testów i oceny większej listy przez operatora lub agenta. Operator rozstrzyga rozszerzenie zakresu dopiero przed wdrożeniem |

P1 ma pierwszeństwo jako propozycja domknięcia już zapisanej instrukcji. P2 rozszerza istniejące wymaganie; nie jest automatyczną poprawką błędu TRC-13. Obie propozycje pozostają niewdrożone. Żadna nie zapewnia ochrony przed celowym fałszowaniem ani kontroli tożsamości.

### 6. Sprawdzenie karty, dowody i dalsze pytania

Warunki zakończenia tej pracy dokumentacyjnej: (1) każda obecna reakcja ma źródło, (2) propozycje nie są oznaczone jako działające, (3) przykłady obejmują dopuszczenie, ostrzeżenie, odmowę i brak podstawy, (4) ścieżka wznowienia wskazuje zakres i następny krok. Nie są to nowe kryteria odbioru wydania szablonu.

**W tej pracy:** odczyt autora REQ/AT, instrukcji oraz kodu W5/E9; tabela C1–C10 jest analizą, nie logiem nowych uruchomień. Nie wykonano niezależnej recenzji ani próby nowej sesji. Historyczne wykonanie TST-02 jest wyżej; nie zalicza przypadków C1–C10. Kontrole dokumentacji i wynik zakończenia: [rejestr wykonania §8.8](../process-modeling/coverage-map.md#88-rejestr-zmian-i-wykonania).

| Sprawa otwarta | Właściciel | Kiedy i jaki następny krok |
| --- | --- | --- |
| Przyjęcie P1, później ewentualnie P2 | Użytkownik; agent przygotowuje decyzję | Przed implementacją, po omówieniu przykładów. Zgoda na kartę nie jest zgodą na nowe blokady |
| Sposób odniesienia rekordu korygującego do starego i granica porównania treści | Agent | Przed implementacją P1 przedstawić spójny przypadek korekty także błędnego wpisu, bez usuwania historii; nie dodawać teraz pól do schematu |
| Znaczenie późniejszego fail po pass | Agent | Przed użyciem danych VER do automatycznej oceny gotowości zaproponować regułę pierwszeństwa i kontrprzykład; bez domyślnego „zielone” |
| Czy karta pomaga człowiekowi i nowej sesji | Agent, odbiór użytkownika | Przejść C1 → C2 → C4; sprawdzić, czy odróżniają wpływ zmiany, wynik przeglądu i zgodę. To próba zrozumienia, nie dowód działania narzędzia |

**Najbliższy krok:** omówić przykład C1 → C2 → C4. Kod, wymagania pakietu i reguły wydania pozostają bez zmian.

### 7. Przejście dydaktyczne C1 → C2 → C4 — TextStats

2026-11-01, na polecenie U „Wykonajlmy Dalej jak sugerujesz”. To fikcyjny przykład do objaśnienia karty, nie zmiana specyfikacji lub aplikacji TextStats i nie wykonanie testów. Lokalne nazwy CAP-01/AT-01 mają znaczenie jak w §4; nie są dowodami rzeczywistego projektu. Zakładamy w fabule, że decyzja o zmianie została podjęta; nie tworzymy takiej zgody w projekcie.

**Przed:** reguła liczenia traktuje ciąg znaków między białymi znakami jako jedno słowo. Przypadek `biało-czerwony` ma oczekiwany wynik 1. W fabule wymaganie i przypadek testowy miały osobne przeglądy pass, a program przeszedł test.

**Zmiana:** znak `-` ma również rozdzielać słowa, więc dla tego samego wejścia oczekujemy 2. To wyłącznie przykład konkretnej różnicy, nie pełna definicja tokenizacji.

| Przedmiot | Co wiemy po zmianie wymagania, przed nowymi sprawdzeniami |
| --- | --- |
| Dawny przegląd wymagania | Nadal opisuje ocenę starej treści. Nie jest oceną nowego wymagania |
| Przypadek testowy oczekujący 1 | W tym przykładzie jest niezgodny z nową regułą; trzeba zmienić oczekiwanie na 2 i ocenić jego adekwatność |
| Dawny wynik wykonania testu | Pozostaje historycznym sukcesem wobec poprzedniego oczekiwania. Nie przepisujemy go na fail; nowy test wymaga nowego wykonania |
| Kod | Jeśli nadal zwraca 1, nie spełnia nowej reguły dla tego wejścia. Trzeba to sprawdzić i w razie potrzeby poprawić |

**C1 — ostrzeżenie:** przy założeniach §4 W5 wskaże CAP-01 oraz AT-01. Wskazuje zmianę podstawy oceny; nie rozumie znaczenia myślnika i nie wybiera poprawnej liczby. Stary kod i stary test mogą nadal dawać zielony wynik, choć nie sprawdzają nowej reguły. To ocena logiczna przykładu, nie uruchomienie programu. W5 nie zapewnia tutaj automatycznego śladu do kodu i konkretnego wykonania testu.

**C2 — odmowa:** dopisanie nowego VER pass dla CAP-01 w tym samym commicie co jego zmiana zostanie odrzucone przez E9. Oddzielamy utrwalenie zmiany od zapisu pozytywnego przeglądu. Dwa commity same nie dowodzą niezależności recenzenta.

**C4 — ponowny przegląd:** po utrwaleniu zmiany recenzent ocenia nowe wymaganie. Nowy VER pass dla niego może zostać dopisany bez E9, jeżeli badany element się w tym commicie nie zmienia. To jeszcze nie przegląd AT-01 ani wykonanie testu na kodzie. Te czynności mają własne wyniki i mogą wykryć błąd pomimo poprawności wymagania.

W tym przykładzie zamknięcie techniczne wymagałoby rozliczenia nowego wymagania, adekwatności testu oraz nowego wykonania na zmienionym programie w ustalonym zakresie. Odbiór pozostaje odrębną decyzją, gdy jest wymagany. Nie uznajemy go za wykonany w ćwiczeniu.

**Wniosek do zapamiętania:** dowód odpowiada na konkretne pytanie o konkretną wersję. Po zmianie sprawdzamy, na które dzisiejsze pytania dawne dowody nadal odpowiadają. Sam fakt zmiany nie fałszuje historii.

Następny krok edukacyjny: porównać dopisanie nowego wyniku z nadpisaniem starego (C5), na tym samym przykładzie. Właściciel: agent. Zrozumienie i użyteczność dla użytkownika pozostają do oceny; przedstawienie przykładu nie jest ich dowodem.
