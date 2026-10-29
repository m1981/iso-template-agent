# Sprawdzenie karty zmiany wymagania

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
