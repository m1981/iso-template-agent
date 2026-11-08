# Mapa repozytorium według celu, historii i mocy dokumentów

Audyt A-13 · 2026-11-08 · **migawka `ca8f3367e8184279e2655fb2d8173cfcf79f9f42`**, 49 commitów od pierwszego `716abb6`. To raport informacyjny, nie nowa instrukcja procesu ani decyzja o zmianie zakresu.

## Wniosek dla operatora

Repozytorium urosło z **szablonu procesu** w **szablon + jego własny projekt + laboratorium edukacyjne i techniczne**. Obecny układ nie pokazuje wystarczająco wyraźnie tych granic. Zgubienie się nie oznacza, że operator musi nauczyć się wszystkich dokumentów: większość plików nie służy codziennemu prowadzeniu pracy.

**539 plików śledzonych, w tym 143 Markdown.** W samym eksperymencie Flowable jest 233 plików, z czego 179 w `evidence/`. Liczba plików nie jest liczbą obowiązków operatora. Nie wykazano, że wszystkie są niezbędne; nie znaleziono też podstawy do masowego usuwania. Najpierw należy naprawić orientację i oznaczenia aktualności, zachowując dowody i działające zależności.

- **Teraz przeczytaj:** ten wniosek → [punkt wznowienia](../process-modeling/brief.md#punkt-wznowienia) → tylko §8.7 [planu](../process-modeling/coverage-map.md#87-zalecenia-i-punkt-wznowienia). Reszta jest dobierana do zadania.
- **Wszystkie pliki:** [inventory.tsv](inventory.tsv), jeden wiersz na każdy plik z bazowego commita, z celem, rolą, mocą, oceną aktualności, zaleceniem i historią ścieżki.
- **Bieżące zlecenie:** A-13 w planie; A-12/Kitchen nadal jest propozycją. Ten audyt nie otwiera nowej implementacji.

## 1. Co sprawdzono, a czego ten wynik nie dowodzi

Prześledzono listę zmian wszystkich 49 commitów i drzewa w dziesięciu punktach historii. Odczytano dokumenty sterujące pracą, indeksy celów, wybrane raporty, instrukcje i odbiorców plików (copier, Makefile, testy złotych wzorców i przeniesienia). Przejrzano nazwy i nagłówki pozostałej dokumentacji. **Nie wykonano pełnego semantycznego przeglądu każdego z 539 plików ani ponownej regresji produktu.** Wykaz jawnie odróżnia ocenę punktu wejścia od klasyfikacji według funkcji katalogu i typu pliku.

Git dostarcza dat i zmian, ale nie rozstrzyga, czy treść jest prawdziwa, zatwierdzona lub nadal obowiązuje. Commit zapisuje paczkę pracy, niekoniecznie moment jej wykonania. Wykrycie przeniesienia przez Git jest heurystyką podobieństwa; „pierwszy commit” w wykazie oznacza początek rozpoznanej linii pliku, nie autorstwo idei.

Zakres liczbowy to pliki śledzone na bazowym commicie, **bez nowego pakietu tego audytu**. Poza nim pozostaje nieśledzony eksport użytkownika `ISO 29110 a nasz model śladu.md`. Nie oceniano jego treści ani potrzeby. Lokalne `.runs/`, `.tooling/`, `target/`, `__pycache__/`, `.idea/` i `.DS_Store` są ignorowane przez Git; nie są dodatkowymi dokumentami procesu. `.runs/` może zawierać lokalny stan — nie traktować go automatycznie jak bezpieczny do usunięcia cache.

## 2. Jak powstała obecna struktura

| Punkt historii | Pliki / MD | Co zmieniło cel i strukturę |
| --- | ---: | --- |
| `716abb6`, 12.10 | 30 / 16 | Początkowy szablon: instrukcje, decyzje, produkty pracy, ślad |
| `11ddded`, 19.10 | 95 / 35 | Wymagania i kryteria samego szablonu, dystrybucja, wzorce wyników i testy |
| `12acb1d`, 22.10 | 120 / 49 | Po `b866213` (przeniesienie) dostosowano trzy warstwy: pakiet w template/, jego rozwój w project/spec/records/reports, materiały w reference/ |
| `e63c8da`, 24.10 | 151 / 70 | Naprawy kontroli w TDD, materiały planowania i plan lekcji |
| `5471272`, 24.10 | 197 / 73 | Działający przyrost edukacyjny L1/TextStats |
| `0a988e4`, 26.10 | 271 / 94 | Mapy procesu, przejście W02, wywiad o współpracy vcs-lite |
| `8849a3b`, 30.10 | 302 / 112 | Kontrakty API, modelowanie cyklu wydań, audyt kryteriów; trwałe wznowienie kierowane przez brief/mapę |
| `8fa127b`, 06.11 | 413 / 115 | Osobny eksperyment Java/Flowable F1–F4, testy, dowody i diagramy |
| `16f5ff8`, 07.11 | 515 / 136 | F5: trwałość i wznowienie w kolejnych JVM, wyniki recenzji |
| `ca8f336`, 08.11 | 539 / 143 | Relacja ISO–Scrum, koncepcja i generator kart operatora, ograniczona próba czytelności, roadmapa |

Wniosek: szczególnie późny wzrost wynika z **eksperymentów i dowodów**, nie z rozbudowania obowiązkowej dokumentacji każdego projektu. Copier wybiera `template/`; nie rozsyła całego laboratorium. Istnieją dwa tagi baseline, brak tagu wydania v1.0.0. Zakończenie eksperymentu nie oznacza wydania szablonu.

Przykład znaczenia historii: `template/process/tools/trace.py` leży w obecnym katalogu od `b866213`, ale jego rozpoznana linia sięga `716abb6`. Z kolei `reference/repository-evolution/` to **fikcyjna historia TextStats do nauki**, a nie historia Git tego repozytorium.

## 3. Pliki według celu

Grupy poniżej są rozłączne; sumują się do 539. Wykaz TSV podaje przypisanie każdego pliku.

| Cel | Liczba | Najważniejsze miejsca | Jak traktować |
| --- | ---: | --- | --- |
| G1. Dostarczany pakiet procesu | 56 | [template/process/AGENTS.md](../../template/process/AGENTS.md), tools/, hooks/, templates/, modules/, roles/ | Instrukcje, implementacja i wzorce dla projektów. Wzorzec rekordu nie jest rzeczywistym rekordem |
| G2. Rozwój i sprawdzanie szablonu | 69 | [project/plan.md](../../project/plan.md), decisions.md, spec/, records/, reports/, tests/, reference/golden/, reference/tdd/, layout-map.md, pliki korzenia | Własny projekt produktu „szablon”; osobny zakres od laboratorium |
| G3. Edukacja, propozycje praktyk i tło | 25 | reference/*.md poza layout-map; planning-examples/, repository-evolution/, sessions/ | Propozycje i przykłady. Nie wdrażają same praktyk ani nie zatwierdzają projektu |
| G4. Lekcja L1/TextStats | 52 | [process-simulator/README.md](../process-simulator/README.md), kod, testy, evidence/, collaboration.md, progress.md | Działająca symulacja edukacyjna. Wyjątek: collaboration.md zawiera lokalny kontrakt D-78 |
| G5. Rozumienie, modelowanie i koordynacja | 56 | process-modeling/ oraz process-map/ bez flowable-trial/, w tym operator-preview/ | Diagramy i analizy; **wyjątek: brief i §8.7–8.8 mapy prowadzą bieżącą pracę** |
| G6. Próba mechanizacji Flowable | 233 | [flowable-trial/README.md](../process-map/flowable-trial/README.md), src/, evidence/, architecture.md, f5-report.md, show-card | Oddzielny eksperyment techniczny; nie wybrana platforma produkcyjna Kitchen |
| G7. Wywiad i doświadczenie vcs-lite | 45 | [README](../vcs-lite-interview/README.md), [findings.md](../vcs-lite-interview/findings.md), pytania, odpowiedzi, źródła | Materiał empiryczny z ograniczeniami. Hipoteza korzyści nie jest obowiązkiem procesu |
| G8. Archiwum dawnego układu | 3 | archive/flat-layout/, archive/tools/process_kit_view.py | Historia; poza codzienną mapą czytania. Przeniesienie/usunięcie może naruszyć test dawnej migracji |

## 4. Co jest normatywne, informacyjne, aktualne

W tym audycie **„normatywne” wymaga dopowiedzenia: według ISO czy lokalnie wiążące**. Tych znaczeń nie wolno mieszać.

| Rodzaj | Źródło i granica |
| --- | --- |
| Źródło normy | Lokalne rozdziały w [iso-29110-5-1/chapters](../../../iso-29110-5-1/chapters), poza tym repo. Audyt struktury nie ponawia interpretacji normy. Mapy WP i plik iso29110.toml nie zastępują treści źródłowej |
| Obowiązujące instrukcje lokalne | AGENTS.md + pakiet procesu, z jawnymi odstępstwami i decyzjami użytkownika. D-78 / collaboration.md reguluje bieżącą współpracę; D-87 kieruje wznowienie do briefu i mapy |
| Lokalna specyfikacja produktu | spec/requirements.md i spec/tests/process-kit.feature dotyczą **szablonu**. Kod testów sprawdza wybrane oczekiwania. Istnienie ID, testu lub statusu initiated nie jest zatwierdzeniem treści |
| Plan i upoważnienie | project/plan.md dotyczy produktu-szablonu; mapa §8.7 dotyczy obecnego wątku laboratoryjnego. Decyzje i rzeczywiste polecenia określają upoważnienie. Pozycja `proposed` nie zleca wykonania |
| Dowód wykonania | Raport/log/wynik przypisany do konkretnego przedmiotu i wersji. Rejestr może zawierać sam format. Wyniki fikcyjnego przebiegu nie są odbiorem rzeczywistego produktu |
| Informacja i propozycja | Analizy, diagramy, przykłady, projektowane kryteria. Mogą być przydatne i merytorycznie poprawne, ale nie nakładają zobowiązań przez sam fakt zapisania |
| Widok pochodny | reports/*, rendery, generowane karty. Źródło i data decydują, czego widok dotyczy. `07-show` nie jest żywym stanem projektu |

**Aktualność nie jest własnością całego katalogu ani nawet całego pliku.** Brief ma aktualny punkt wznowienia oraz dawne propozycje. Coverage-map ma aktywny plan/rejestr, datowane analizy i nieaktualny skrót u góry. W TSV oznaczono takie pliki jako mieszane, zamiast przyznawać im zbiorcze „aktualny”.

Nie ustalamy nowej hierarchii przez daty modyfikacji. Przy pozornej sprzeczności trzeba ustalić zakres, status i decyzję zmieniającą poprzednie ustalenie. Jeśli tego nie ma, konflikt pozostaje do rozstrzygnięcia, a nie do zgadnięcia przez agenta.

## 5. Pięć najważniejszych ustaleń

| Kategoria | Problem → plik i dowód | Skutek | Minimalna poprawka — rekomendacja, jeszcze niewykonana |
| --- | --- | --- | --- |
| **Brak** | Główny [README](../../README.md) opisuje trzy warstwy, ale nie prowadzi do bieżącego briefu i nowych rezultatów; indeks process-map także nie obejmuje wszystkich późniejszych dostaw | Użytkownik zaczyna od mapy, która pomija obecny cel | Dodać do README trzy wejścia: prowadzenie bieżącej pracy, rozwój szablonu, nauka/eksperymenty; linki do istniejących źródeł, bez drugiego planu |
| **Potwierdzony defekt** | [coverage-map](../process-modeling/coverage-map.md), początek: „Bieżący wynik… F5 niezlecone”; §8.7 A-06 i D-99 dokumentują późniejsze zakończenie F5 | Pierwszy odczyt podaje nieprawidłowy obecny stan | Oznaczyć dawny skrót jako historyczny i odesłać do §8.7; nie przepisywać dawnych dowodów |
| **Potwierdzony defekt** | [project/plan.md](../../project/plan.md), wstęp: `make process-kit`; `make -n process-kit` kończy się kodem 2, brak celu w Makefile | Instrukcja odtworzenia postępu nie działa | Zastąpić dawną instrukcję aktualnymi `make trace` / `make progress`, po sprawdzeniu właściwego zakresu; zachować historię migracji w Git |
| **Brak** | reference/ wygląda na informacyjne, ale [collaboration.md](../process-simulator/collaboration.md) ma kontrakt D-78, a brief/mapa kierują pracą na mocy D-87. Starszy kontrakt ma inny zakres autonomii i format odpowiedzi | Nowa sesja może zastosować niewłaściwy kontrakt lub pominąć wyjątek | W jednym punkcie wejścia wskazać źródła i zakres odstępstw D-78/D-87; nie zmieniać kontraktu pakietu w ramach porządkowania |
| **Brak** | [reports/test-report.md](../../reports/test-report.md) opisuje `2026-10-22 / b866213 dirty`; reports/progress obejmuje plan szablonu, nie A-01…A-13. Są osobne dowody L1, modelowania i Flowable | Jeden widok „raport” łatwo uznać za ocenę całego aktualnego repo | Mapa czytania ma wskazywać osobno wynik i przedmiot każdej próby; nie łączyć liczników PASS i nie uznawać dawnych raportów za obecną regresję |

Obecne mechanizmy nie wystarczają, ponieważ sprawdzają określony zakres składni, śladu i plików. Nie porównują znaczenia „bieżący” we wszystkich dokumentach. `check_refs.py` świadomie wyłącza reference/ (D-64); zielone `make check` nie potwierdza aktualności tego laboratorium. Nie rekomenduję teraz nowego rozbudowanego skanera: pierwszą poprawką powinny być linki, zakres i usunięcie mylących oznaczeń.

Koszt proponowanego uporządkowania: jednorazowa korekta kilku wejść, potem zmiana linku/opisu przy zmianie celu lub upoważnienia. Efekt sprawdzimy próbą wznowienia: czy nowa sesja wskazuje właściwy cel, plan, wynik i granice zgody, bez czytania całej historii. Nie ustalono progu czasu ani skuteczności. Właściciel przygotowania poprawki: agent; zmiana zakresu/kontraktu lub przeniesienie materiałów wymaga właściwej decyzji operatora.

## 6. Czy wszystkie pliki są potrzebne?

**Do codziennego prowadzenia pracy — nie. Do zachowania historii, testów i odtwarzalności — wiele tak. Dla każdego pliku nie udowodniono jeszcze konieczności przechowywania.** Usuwanie wymaga innego pytania niż czytanie: kto plik konsumuje i jaki dowód albo zdolność odtworzenia zniknie?

| Zbiór | Rekomendacja | Powód i kontrola przed zmianą |
| --- | --- | --- |
| Pakiet, specyfikacja, testy, decyzje | Utrzymać | To produkt i jego podstawa. Zmiany pakietu wpływają na odbiorców copiera |
| 31 plików reference/golden/ | Utrzymać jako czynne dane testowe | tests/golden_master.py rzeczywiście je odczytuje. Stary wzorzec może być aktualnym oczekiwaniem |
| Puste formaty records/* i templates/* | Nie usuwać tylko dlatego, że nie ma wpisów | Są elementami formatu/dystrybucji; oddzielić format od dowodu wykonania |
| Dowody F1–F5, TDD i recenzji | Zachować; schować za indeksem wyników | Duża liczba logów wynika z odtwarzania i wariantów. Redukcja wymaga zachowania źródła, wersji i niezależnych przebiegów |
| Dawne propozycje i zrealizowane plany, np. remaining-rounds.md, findings-round-01.md | Logicznie oznaczyć jako historyczne; czytać końcowe findings.md | Najmniejsza zmiana to etykieta i odsyłacz. Przenoszenie psuje linki, nie daje samo wartości |
| Diagramy źródłowe i rendery | Utrzymać pary lub uzgodnić odtwarzanie | DOT/Mermaid i SVG/PNG służą różnym odbiorcom. Nie są automatycznie zbędną duplikacją |
| Transkrypty i fikcyjne snapshots | Oddzielić w mapie od instrukcji operacyjnych | Zachowują rozumowanie/lekcję. Nie używać ich jako domyślnego kontekstu każdej sesji |
| Archive/ i test historycznej migracji | Osobny kandydat do przeglądu zasad retencji | tests/test_move.py ma zakodowane stare ścieżki i porównania. Usunięcie może zmienić kryterium, nie tylko porządek katalogów |

Porównanie identyfikatorów blobów Git wykazało **11 grup identycznej treści, obejmujących 48 plików**. To nie jest lista do skasowania. Przykłady: `.gitignore` projektu i jego wzorzec mają odrębne funkcje; takie same eksporty mogą potwierdzać odtworzenie przez autora i recenzenta; pięć pustych stderr dokumentuje brak wyjścia błędów. Osobno można rozważyć konsolidację dwóch identycznych zrzutów ekranu L1, po sprawdzeniu odsyłaczy i kontekstu zdarzeń. Nie wykazano równoważności semantycznej różnych dokumentów na podstawie podobnych nagłówków.

## 7. Mapa czytania — zależnie od pracy

### Operator: co i dlaczego robimy teraz

1. [Brief — tylko punkt wznowienia](../process-modeling/brief.md#punkt-wznowienia): ostatni wynik, granice i wskazanie planu.
2. [Coverage-map §8.7](../process-modeling/coverage-map.md#87-zalecenia-i-punkt-wznowienia): status bieżącej pracy i upoważnienie; §8.8 tylko gdy potrzebny dowód zdarzenia.
3. Jeden dokument wskazany przez aktualne zadanie. Dla tego audytu jest nim niniejszy raport. Dla karty: [mapa pól](../process-map/operator-preview/textstats-card-data-map.md) i [wynik generatora](../process-map/flowable-trial/evidence/operator-card/README.md).
4. [Decyzje](../../project/decisions.md) dopiero dla konkretnego rozstrzygnięcia lub sprawy wymagającej operatora. Nie trzeba odczytywać wszystkich 99 wpisów za każdym razem.

Ta ścieżka operatora nie zastępuje obowiązkowego odczytu agenta.

### Agent: obowiązkowy start według AGENTS.md

[Kontrakt decyzji](../../template/process/kontrakt-decyzji.md) → [instrukcja pakietu](../../template/process/AGENTS.md) → [lokalne AGENTS](../../AGENTS.md) → [plan szablonu](../../project/plan.md) → [raport postępu](../../reports/progress.md) → [decyzje](../../project/decisions.md) → [punkt wznowienia](../process-modeling/brief.md#punkt-wznowienia) → wskazany w nim plan §8.7/rejestr §8.8. Przy stosowaniu D-78 odczytać [kontrakt współpracy](../process-simulator/collaboration.md). Obowiązują nowe jawne polecenia i wyjątki w ich zakresie, nie historyczne „dalej”.

### Developer: wybrać jeden produkt, zanim otworzy kod

| Zadanie | Kolejność |
| --- | --- |
| Zmiana pakietu procesu | project/plan + właściwa decyzja → spec/requirements i AT → odpowiedni moduł template/process → testy; dla zmiany dystrybucji także copier.yml/test_distribution i MIGRATIONS |
| Zmiana lekcji L1 | process-simulator/README → specyfikacja i plan tej lekcji → jej kod/testy → jej evidence; symulowane decyzje nie stają się rzeczywistymi odbiorami |
| Zmiana Flowable/karty | flowable-trial/README + f5-report → mapa pól karty (gdy dotyczy) → pom.xml i src/ → testy i wskazany pakiet dowodów. Architecture.md ma opisany zakres F4/F5 |
| Kontynuacja formalnego modelu | brief + mapa §8.5/8.7 → aktualne źródła i upoważnienie w osobnym iso-model-state. Historyczny lokalny raport nie potwierdza jego dzisiejszego stanu |

### Nauka: czytać wybiórczo

Podstawy przyrostu: L1 README i lekcja → process-map/README oraz worked-transition.md → static-model.md dla encji. Relacja ISO i Scrum: iso-and-scrum.md. Planowanie: planning-examples/README. Historia fikcyjnego projektu: repository-evolution/README. Wnioski o współpracy: vcs-lite-interview/findings.md; surowe rozmowy dopiero do sprawdzenia konkretnego wniosku. Propozycje pakietów praktyk i formalizacji czytać po rozpoznaniu potrzeby, nie jako listę obowiązków na start.

## 8. Odtworzenie i kontrola audytu

Z korzenia repo:

```sh
python3 reference/repository-audit/build_inventory.py --output /tmp/iso-template-inventory.tsv
cmp reference/repository-audit/inventory.tsv /tmp/iso-template-inventory.tsv
```

Skrypt czyta przypięty commit, nie niezapisany katalog roboczy; wypisuje liczby, etapy historii i grupy identycznych blobów. Nie uruchamia produktu, nie zmienia Git ani nie potrzebuje sieci. Klasyfikacja jest oceną audytora dla tej migawki — dla nowego zakresu trzeba ją ponownie przejrzeć, nie tylko zmienić SHA.

Kolumny TSV: `path`, `goal`, `role`, `authority`, `currency`, `maintenance`, `basis`, `first_commit`, `first_date`, `origin_path`, `path_since`, `last_commit`, `last_date`. `basis` określa granicę oceny. Generowanie z Git zapobiega ręcznemu pominięciu ścieżek; nie automatyzuje osądu aktualności ani przydatności.

Decyzja agenta, 2026-11-08: audyt zapisano w osobnym `repository-audit/`, a nie w dydaktycznym `repository-evolution/`; jeden generowany wykaz zamiast ręcznie utrzymywanego drugiego rejestru projektu. Powód: oddzielić rzeczywistą historię repozytorium od fikcyjnej historii TextStats. Ten pakiet jest migawką audytu, nie nowym obowiązkiem aktualizowania 539 rekordów przy każdym commicie.

**Wynik wykonanych kontroli:** wykaz 539/539 ścieżek, bez powtórzeń; druga generacja bajtowo identyczna; sumy ośmiu grup zgodne. Porównano trzy linie plików z `git log --follow` (trace.py, project/plan.md, brief.md). 29 lokalnych odnośników raportu wskazuje istniejące pliki/katalogi; nie sprawdzono kotwic. Kontrola końcowych spacji i bloków kodu bez usterek. `make check`: 265 elementów, 0 błędów, wcześniejsze ostrzeżenia W1 MIG-01/02; bez dowodu aktualności semantycznej reference/. Nie ponawiano testów Python/Java ani dawnych eksperymentów.

Kontrole końcowe i zamknięcie: Z-60 w [rejestrze §8.8](../process-modeling/coverage-map.md#88-rejestr-zmian-i-wykonania). Bez usuwania, przenoszenia, zmiany reguł, commita, pracy w Kitchen lub drugim modelu. Rekomendowana następna paczka: tylko korekta punktów wejścia i nieaktualnych instrukcji z §5; dalszy pilot pozostaje w A-12, a zmiana jego kolejności/zakresu nie wynika automatycznie z tego raportu.
