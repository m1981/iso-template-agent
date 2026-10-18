# Rejestr decyzji

Pamięć projektu między sesjami (kontrakt-decyzji.md). Agent aktualizuje rejestr po każdej odpowiedzi Użytkownika. ID są niezmienne. Artefakty wskazują decyzję w swoich polach (`source:`, `established_by:`, `changed_by:`); rejestr nie wylicza swoich dzieci, robi to trace.md. Treść po polsku, nazwy pól i stanów po angielsku (D-17). Wpisy rozstrzygnięte przed D-17 zachowują dawne nazwy plików w treści: to zapis historii.

Format:

```
### D-nn Tytuł zwykłymi słowami
- status: open | resolved | deferred
- options: A) … · B) …
- proposal: A
- choice: A — co dokładnie postanowiono
- date: RRRR-MM-DD

### Q-nn Temat w kolejce
- notes: skąd się wziął
```

## Otwarte

### D-40 Adres origin na Macu
- status: open
- options: A) przełączyć na HTTPS: git remote set-url origin https://github.com/m1981/iso-template-agent (logowanie przez przeglądarkę albo token) · B) zostawić SSH git@github.com:m1981/iso-template-agent.git (wymaga klucza SSH dodanego w GitHubie)
- proposal: A, jeśli push z Maca przez SSH nie działa; B, jeśli działa
- notes: oba adresy to to samo repozytorium; kopia agenta w chmurze używa HTTPS; dotyczy Q-10 (push tagów z Maca)

## W kolejce

### Q-01 Strona „ISO 29110 a nasz model śladu” po rozszerzeniu
- notes: kolory pokrycia na stronie pokazują stan sprzed D-08…D-19; odświeżyć. Zrobione w D-25 (2026-10-16).

### Q-02 Przeniesienie zmian szablonu do gtd2
- notes: w gtd2 ID zostają (D-17); migrują nazwy pól, stanów i plików; 28 wymagań przechodzi z draft na initiated (D-11); każdy produkt dostaje status (D-14)

### Q-03 Pilot ról na gtd2 (D-36)
- notes: przy Q-02; weryfikator w osobnej sesji według roles/verifier.md przegląda 10 wymagań uznanych za gotowe; kryteria: co najmniej jedna potwierdzona usterka, najwyżej 1 na 3 zgłoszenia odrzucone, zero zmian w plikach produktów, najwyżej dwa pytania o kontekst; zapis w gtd2 jako kamień milowy z acceptance_criteria i rekord ACC, w szablonie decyzja zamykająca

### Q-04 Karta sesji autora
- notes: odłożone w D-37; wróć, gdy pilot pokaże powtarzalne usterki tego samego rodzaju (np. rozwiązanie w wymaganiu) albo sesja autora zacznie mieszać role; opis w roles/README.md

### Q-05 Sesje programisty i testera
- notes: odłożone w D-36; tester czarnej skrzynki pisze testy z wymagań bez wglądu w kod, raport testów WP.20; wróć na początku etapu kodu; opis w roles/README.md

### Q-06 Rola w opisie commita i uprawnienia do plików
- notes: odłożone w D-38; linia „Role: verifier” i kontrola, że commit roli zmienia tylko dozwolone pliki; wróć, gdy w pilocie weryfikator zmieni plik produktu albo E9 okaże się za słabe; opis w roles/README.md

### Q-07 Pełna tabela ról i odpowiedzialności
- notes: odłożone w D-36; wszystkie role normy (CUS, PJM, TL, AN, DES, PR, TES, WT) przypisane do zadań PM i SI; wróć, gdy dołączy druga osoba albo zewnętrzny klient

### Q-08 Elementy normy świadomie pominięte
- notes: z przeglądu normy 2026-10-16; studium wykonalności (5.2), instrukcje dostarczenia (PM.01.02), czas trwania, pracochłonność i koszt (PM.01.04, PM.01.08), plan testów (załącznik B), proces wsparcia po dostarczeniu (załącznik A), przykładowe wypełnione artefakty (załącznik E); wróć, gdy pojawi się zewnętrzny klient, budżet albo etap kodu

### Q-09 Skrypt modułu model stanów
- notes: modules/state-model ma konwencję, nie ma skryptu sprawdzającego (stany i przejścia wskazują wymagania, stany nieosiągalne i bez wyjścia)

### Q-10 Zaległe czynności na Macu
- notes: zrobione 2026-10-18: Mac zsynchronizowany do f855d51 (drzewo identyczne z kopią), test i make check przechodzą na Pythonie 3.10, tag baseline-01-szablon założony na Macu (D-24). Czeka: push tagów baseline-00-przed-en i baseline-01-szablon z terminala na Macu (sesja agenta dostaje 403 przy pushu tagów), potem make restore-check RECORD=1

## Rozstrzygnięte

### D-39 Założenia przy D-31, D-32, D-33, D-35
- status: resolved
- options: A) przyjąć jak wdrożono · B) przyjąć z poprawkami (wskaż które)
- proposal: A
- choice: A — założenia przyjęte jak wdrożono
- date: 2026-10-17
- notes: W5 tylko na ekranie, bo zależy od historii gita i w trace.md psułby kontrolę aktualności; rekord odtworzenia kopii ma subject: repository zamiast items (nowy klucz root_if w id.toml); numerów punktów list kontrolnych się nie zmienia ani nie używa ponownie; lista wartości quality obejmuje też constraint i legal (WP.13: ograniczenia i wymogi prawne)

### D-38 Rozdział autora i weryfikatora w commicie
- status: resolved
- options: A) błąd E9: commit, który dodaje rekord VER albo VAL z wynikiem pass, nie może w tym samym commicie zmieniać weryfikowanych elementów · B) ostrzeżenie · C) bez kontroli
- proposal: A
- choice: A — tools/check_separation.py w pre-commit (E9); test tablicą decyzyjną: 4 przypadki MC/DC i 3 brzegowe (nowy element, sama zmiana stanu, rekord kopii); każdy warunek sprawdzony wycofaniem; pierwszy commit repozytorium (import) nie jest sprawdzany
- date: 2026-10-17
- notes: mechaniczny odpowiednik zasady „autor nie zatwierdza sam siebie”, sprawdzalny w hooku; test według tablicy decyzyjnej: nowy rekord, wynik pass, element zmieniony w tym samym commicie — E9 tylko gdy wszystkie trzy, po jednym przypadku na zmianę każdego warunku (MC/DC) zamiast wszystkich kombinacji

### D-37 Karty ról
- status: resolved
- options: A) teraz tylko karta weryfikatora (roles/verifier.md: wejścia, pliki do zapisu, czego nie robi, listy kontrolne, wynik sesji) i tabela ról normy w AGENTS.md; sesja autora działa według AGENTS.md · B) karty dla wszystkich rodzajów sesji od razu · C) tylko tabela
- proposal: A
- choice: A — roles/verifier.md i tabela ról normy w AGENTS.md; karta autora odłożona (Q-04)
- date: 2026-10-17
- notes: zależy od D-36; zawężona 2026-10-17 — karta powstaje dla sesji, której faktycznie użyjemy w pilocie

### D-36 Role normy a sesje agenta
- status: resolved
- options: A) model Użytkownik + sesja autora + sesja weryfikatora przyjęty jako hipoteza i sprawdzony pilotem na gtd2 (przy Q-02) według kryteriów akceptacji kamienia milowego; sesje programisty i testera dopiero z etapem kodu · B) wdrożyć pełny model ról od razu · C) odłożyć
- proposal: A
- choice: A — model Użytkownik + sesja autora + sesja weryfikatora jako hipoteza; pilot na gtd2 według czterech kryteriów (Q-03, roles/README.md); sesje programisty i testera z etapem kodu (Q-05)
- date: 2026-10-17
- notes: zawężona 2026-10-17 po pytaniu Użytkownika o zależności i walidację; D-37 i D-38 zależą od tej decyzji (D-38 działa też bez niej, ale wtedy sprawdza tylko osobne commity, nie osobne sesje); role rozdziału 8 i załącznika B; norma pozwala łączyć role w jednej osobie, ale rozdziela autora i zatwierdzającego (SI.02.04–05, SI.03.08) i wymaga niezależnej weryfikacji (uwaga 2 przy SI.O7)

### D-34 Role normy w małym zespole
- status: resolved
- options: A) tabela w AGENTS.md: kto pełni role normy (klient, kierownik projektu, analityk, lider techniczny, projektant, weryfikator) — Użytkownik, agent albo niezależny agent — i kto co zatwierdza · B) bez zmian
- proposal: A
- choice: rozbita na D-36, D-37, D-38 (rozstrzygnięte 2026-10-17)
- date: 2026-10-17
- notes: rozdział 8 i role przy każdym zadaniu; dziś P-10 mówi, czego agent nie robi bez decyzji, ale nie przypisuje ról z normy; Użytkownik poprosił 2026-10-17 o zaprojektowanie procesu z rolami normy i rozważenie rozdziału ról między sesje; rozbita na D-36, D-37, D-38

### D-35 Sprawdzenie odtworzenia kopii zapasowej
- status: resolved
- options: A) make restore-check: klon z origin do katalogu tymczasowego i porównanie drzewa z HEAD oraz listy tagów; wynik jako rekord VER dla repozytorium · B) bez zmian
- proposal: A
- choice: A — tools/restore_check.py (make restore-check [RECORD=1]): klon bieżącej gałęzi z origin, punkty REPO.1–REPO.3; rekord VER z subject: repository (root_if w id.toml); pierwsze uruchomienie 2026-10-17 wykryło brak tagu baseline-00-przed-en w kopii
- date: 2026-10-17
- notes: PM.02.07 „Verify the project repository recovery”; raz zrobiliśmy to przy D-17 ręcznie, ale nie ma tego w procesie

### D-33 Charakterystyki jakości w wymaganiach
- status: resolved
- options: A) opcjonalne pole quality w wymaganiu (functional, performance, compatibility, usability, reliability, security, maintainability, portability, constraint, legal) i tabela w trace.md pokazująca charakterystyki bez żadnego wymagania · B) bez zmian
- proposal: A
- choice: A — pole quality (qualities w id.toml), E4 dla nieznanej wartości, sekcja „Charakterystyki jakości” w trace.md, opis w requirements.md
- date: 2026-10-17
- notes: WP.13 wymienia te charakterystyki, a załączniki C (dostępność) i D (bezpieczeństwo) dokładają do nich zadania; EARS daje formę zdania, ale nie przypomina o wymaganiach niefunkcjonalnych

### D-32 Analiza wpływu zmiany (suspect links)
- status: resolved
- options: A) trace.py oznacza dzieci elementu zmienionego po ich ostatniej weryfikacji jako podejrzane (ostrzeżenie W5), na podstawie historii gita · B) bez tej kontroli
- proposal: A
- choice: A — ostrzeżenie W5: element albo jego rodzic zmienił się po commicie, który dodał ostatni rekord VER pass tego elementu; porównanie treści bez pola status; tylko na ekranie (założenie w D-39)
- date: 2026-10-17
- notes: PM.O3 i PM.02.02: zmianę wymagań ocenia się pod kątem wpływu; dziś trace.md pokazuje dzieci, ale nie mówi, które trzeba przejrzeć po zmianie rodzica; w gtd2 ten sam temat czeka jako K-10

### D-31 Listy kontrolne przeglądu
- status: resolved
- options: A) checklist.md z kryteriami przeglądu dla każdego typu produktu (dla wymagań wprost z SI.02.04: poprawne, testowalne, kompletne, jednoznaczne, niesprzeczne); rekord VER wskazuje listę w polu checklist i wypisuje niespełnione punkty · B) bez list
- proposal: A
- choice: A — checklist.md (listy REQ, UC, SC, IO, G, DP, RSK, AT, E, PLAN, REPO z punktami ze źródłem w normie); rekord VER i VAL: pola checklist i failed; E4 dla nieznanej listy lub punktu i dla wyniku pass z niespełnionymi punktami
- date: 2026-10-17
- notes: przegląd normy rozdział po rozdziale 2026-10-16; WP.23 ma „verification checklist”, a nasze rekordy VER nie mówią, według czego sprawdzano

### D-30 Stara strona „Model śledzalności”
- status: resolved
- options: A) usunąć (nieodwracalne) · B) zostawić
- proposal: B
- choice: B — strona zostaje; aktualny model jest w sekcji „Model śladu” strony ISO
- date: 2026-10-16

### D-29 Historia gita w nowym projekcie
- status: resolved
- options: A) kopia plików bez .git i git init; make new-project odmawia poza repozytorium · B) make new-project usuwa tagi szablonu · C) tylko opisać
- proposal: A
- choice: A — README, „Start”: rsync bez .git, git init, commit „Kopia szablonu”, make new-project; new_project.py odmawia poza repozytorium i nie podaje skrótu commita jako wersji szablonu; test na kopii bez historii
- date: 2026-10-16

### D-28 Pole wskazuje typ rodzica
- status: resolved
- options: A) parent_rules w id.toml: pole → dozwolone typy i warunek rodzica · B) bez zmian
- proposal: A
- choice: A — klucz parent_rules; dla UC: scenarios → SC, scope → IO z kind=In; naruszenie to E7; etykiety strzałek w iso-map.html według reguł
- date: 2026-10-16

### D-27 Niespójności i drobiazgi z przeglądu (D-23)
- status: resolved
- options: A) poprawić wszystkie · B) wybrane
- proposal: A
- choice: A — bez numerów D-nn w progress.md; uwaga o odwołaniach do decyzji szablonu obejmuje Makefile i .githooks/; README: pole iso tylko w typach z odpowiednikiem w normie, pełna lista blokad hooków; AGENTS: schemat ID wymagań ABC-nn; angielskie nazwy w kodzie (skipped, PRODUCTS, bad_toml, new_register, {{RULES}}, {{PATHS}}, parametr line); lista czytających id.toml; poziom cloud w formacie przypadku użycia; nagłówek z dwukropkiem po ID ma własny komunikat, a pola to tylko słowa (\w+)
- date: 2026-10-16

### D-26 Błędy z przeglądu (D-23)
- status: resolved
- options: A) poprawić wszystkie z testem na każdy · B) wybrane
- proposal: A
- choice: A — test działa z własnym system; commit-msg ignoruje diff pod nożyczkami i uwzględnia core.commentChar; ID jako osobne słowo, a ID wymagań w tekście ciągłym sprawdzane tylko dla istniejących obszarów (area_prefix); scenariusz bez tagu kończy element AT; reguły mapy widzą ekrany bez krawędzi; parser zastępczy TOML zgodny z tomllib dla ], # i \\ w napisach; każdy test sprawdzony przez wycofanie poprawki
- date: 2026-10-16

### D-25 Zakres odświeżenia strony ISO (Q-01)
- status: resolved
- options: A) strona generowana w repozytorium z tools/id.toml (pole iso) przez skrypt, sprawdzana przez pre-commit jak trace.md, więc nie może się zestarzeć; opublikowana kopia odświeżana z niej · B) ręczna aktualizacja obu opublikowanych stron (ISO i „Model śledzalności”) · C) ręcznie tylko strona ISO, strona „Model śledzalności” do archiwum
- proposal: A
- choice: A — tools/iso29110.toml (dane normy), ocena w id.toml (iso_partial, iso_out_of_scope), tools/iso_map.py → iso-map.html sprawdzana przez pre-commit; opublikowana strona odświeżona; sekcja „Model śladu” zastępuje stronę „Model śledzalności”
- date: 2026-10-16
- notes: obie strony pokazują stan sprzed D-08…D-21 (polskie kody, braki już uzupełnione)

### D-24 Nazwa i miejsce baseline'u szablonu
- status: resolved
- options: A) tag baseline-01-szablon na commicie po D-22 i D-23, tworzony na Macu i wypychany stamtąd · B) inna nazwa (wskaż)
- proposal: A
- choice: A — wykonanie po rozstrzygnięciu usterek z przeglądu (D-23), na Macu
- date: 2026-10-16
- notes: ta sesja nie może wypychać tagów na GitHuba (HTTP 403), więc tag powstaje na Macu; baseline-00-przed-en też czeka tam na push

### D-23 Przegląd szablonu przed baseline
- status: resolved
- options: A) niezależny przegląd przez osobnego agenta bez kontekstu tej rozmowy: spójność plików, nazw, poleceń i README; usterki jako lista do decyzji · B) bez przeglądu
- proposal: A
- choice: A — przegląd przez osobnego agenta 2026-10-16; usterki jako osobne decyzje
- date: 2026-10-16
- notes: AGENTS.md, kolejność wdrażania, punkt 7; po dwóch dużych zmianach nazw (D-17, D-20) ryzyko pominiętych odwołań w tekście

### D-22 Historia szablonu przy starcie nowego projektu
- status: resolved
- options: A) polecenie make new-project: przenosi rejestr szablonu (D-01…), trace.md i progress.md do archive/template/ i zostawia pusty rejestr z samym formatem · B) instrukcja w README, czyszczenie ręczne · C) bez zmian, nowy projekt dziedziczy historię szablonu
- proposal: A
- choice: A — tools/new_project.py (make new-project): przenosi decisions.md, trace.md, progress.md do archive/template/, zakłada rejestr z D-01; odmawia przy niezacommitowanych zmianach i przy drugim uruchomieniu; artefakty szablonu nie powołują się już na decyzje szablonu; test na kopii całego szablonu
- date: 2026-10-16
- notes: dziś kopia szablonu przenosi do nowego projektu nasze decyzje D-01…D-21 jako jego własne; dotyczy baseline'u szablonu

### D-20 Nazwy spoza tabeli D-18
- status: resolved
- options: A) przyjąć jak wdrożono · B) przyjąć z poprawkami (wskaż które) · C) jak A, ale nazwy w kodzie Pythona też po angielsku (przed zmianą po polsku: 20 z 30 funkcji i metod, atrybuty klas Element i Model, zmienne lokalne)
- proposal: A
- choice: C — nazwy spoza tabeli przyjęte jak wdrożono; identyfikatory w kodzie (tools/, modules/navigation/) po angielsku; zmiana po tokenach, równoważność drzew składni, wynik skryptów identyczny z wzorcem sprzed zmiany w 23 przypadkach; komunikaty i opisy zostają po polsku
- date: 2026-10-16
- notes: założenia przyjęte przy wdrażaniu D-17: kod typu wymagań REQ (dawniej WYM); klucze w tools/id.toml po angielsku (code, pattern, file, fields, parents, required, statuses, coverage z poziomami error | warning…); pola artefaktów: source, scenarios, scope, established_by, changed_by, realizes, verifies, kind, rationale, release, person, interests, content, definition, distinct_from, exceptions, level, primary_actor, form, minimal_guarantee, success_guarantee, pattern, text, notes, measure, objective, due, tag, acceptance_criteria, milestone, produces, completed, deviation, concerns, mitigation, items, date, by, result, open_issues, cause, action, opened, impact, likelihood, severity; wartości: poziomy celu sea | kite | fish, zadania planned | in_progress | completed, ryzyka projektu open | closed, decyzje open | resolved | deferred, wyniki pass | fail i accepted | rejected, ryzyka produktu low | medium | high; w przypadku użycia brief | full w nowym polu form, bo status należy do stanów produktu; moduł nawigacji: klasy screen, modal, success, external i komentarz exception-dp01; kontrakt-decyzji.md zostaje pod polską nazwą

### D-21 Ostrzeżenie o nieznanym polu
- status: resolved
- options: A) ostrzeżenie W4 dla pola spoza znanych pól typu · B) bez takiej kontroli
- choice: A — znane pola: fields, required, nowy klucz optional w każdym typie id.toml oraz [project] common_fields (notes); test obejmuje dawne polskie nazwy
- date: 2026-10-16

### D-19 Kolejność: język przed baseline
- status: resolved
- options: A) najpierw zmiana języka w szablonie, potem baseline szablonu i przeniesienie do gtd2 · B) najpierw baseline obecnej wersji
- choice: A — punkt powrotu: tag baseline-00-przed-en na commicie a32c5f9
- date: 2026-10-14

### D-18 Nazwy warstwy maszynowej
- status: resolved
- options: A) tabela z odpowiedzi agenta 2026-10-14 · B) z poprawkami
- choice: A — OBJ, MS, TSK, PRK; COR, VER, VAL, ACC; DP, RSK, Q; SC, IO, D, G, UC, E, AT bez zmian; pola source, produces, milestone, result; stany initiated, verified, approved; pliki trace.md, progress.md, decisions.md, tools/; kody błędów E1…, ostrzeżeń W1…; nazwy spoza tabeli: D-20
- date: 2026-10-14

### D-17 Język warstwy maszynowej
- status: resolved
- options: A) angielski w kodach, polach, stanach, nazwach plików i skryptów; polski w treści; w gtd2 ID zostają · B) całość po angielsku · C) polski z tabelą tłumaczeń
- choice: A — wdrożone w całym szablonie; tabela terminów normy w glossary.md
- date: 2026-10-14

### D-16 Układ planu i rekordów
- status: resolved
- options: A) cztery rodzaje rekordów w jednym pliku · B) każdy rodzaj rekordu w osobnym pliku
- choice: B — corrections.md (WP.04), verification.md (WP.23), validation.md (WP.22), acceptance.md (WP.01); produces: przyjmuje kody typów albo ID; kamień osiągnięty = istnieje tag z pola tag:; pre-commit sprawdza aktualność progress.md
- date: 2026-10-14

### D-15 Stan „verified” bez rekordu weryfikacji
- status: resolved
- options: A) ostrzeżenie, commit przechodzi · B) błąd blokujący commit
- choice: A — ostrzeżenie W3
- date: 2026-10-14

### D-14 Zakres jednolitych stanów
- status: resolved
- options: A) stany tylko dla produktów pracy; brak pola status = initiated · B) status obowiązkowy w każdym produkcie pracy
- choice: stany mają tylko produkty pracy (SC, IO, DP, G, UC, RSK, REQ, E, AT); decyzje, zadania, ryzyka projektu i rekordy mają własne statusy; pole status obowiązkowe w każdym produkcie pracy (B), brak = błąd E1
- date: 2026-10-14

### D-13 Kopia zapasowa repozytorium (ISO/IEC 29110 WP.12)
- status: resolved
- options: A) prywatne repozytorium na GitHubie jako drugi remote · B) dysk zewnętrzny albo Time Machine · C) oba
- choice: A — remote origin git@github.com:m1981/iso-template-agent.git; pierwszy push 2026-10-14; push także z tagami (make hooks ustawia push.followTags)
- date: 2026-10-14

### D-12 Model śladu wobec ISO/IEC 29110: rozszerzyć czy od nowa
- status: resolved
- options: A) rozszerzyć · B) zbudować od nowa według listy produktów normy
- choice: A — pole iso w każdym typie id.toml i tabela mapowania w slad.md; nowe typy KOR (WP.04), WER (WP.23), WAL (WP.22), AKC (WP.01) w rekordy.md; kopia zapasowa (WP.12) osobno: D-13
- date: 2026-10-14

### D-11 Stany produktów pracy
- status: resolved
- options: A) jednolite stany wzorowane na 29110 · B) statusy per typ
- choice: A — rozpoczęty, zweryfikowany, zatwierdzony ([projekt] stany_produktow w id.toml); baseline z tagów; wymagania przechodzą z draft/zatwierdzone na te stany; zakres: D-14
- date: 2026-10-14
- notes: nazwy stanów po angielsku (initiated, verified, approved): D-18

### D-10 Generowany rekord postępu
- status: resolved
- options: A) postep.md generowany z planu, repozytorium i tagów · B) bez rekordu postępu
- choice: A — narzedzia/postep.py, make postep; pre-commit sprawdza aktualność
- date: 2026-10-14

### D-09 Plan jako elementy śladu
- status: resolved
- options: A) typy CEL, KM, ZAD (produkuje:), RP; produkuje: jako jawny wyjątek od P-03 · B) plan jako zwykły tekst
- choice: A — typy w id.toml; P-03 w AGENTS.md opisuje wyjątek
- date: 2026-10-14
- notes: kody po angielsku (OBJ, MS, TSK, PRK, pole produces:): D-18

### D-08 Miejsce części zarządczej planu
- status: resolved
- options: A) osobny plan.md według WP.10, AGENTS.md zostaje procesem · B) sekcje w AGENTS.md
- choice: A — plan.md; sekcja Zakres przeniesiona z AGENTS.md do plan.md
- date: 2026-10-14

### D-07 Źródło bazowe dla części zarządczej planu
- status: resolved
- options: A) ISO/IEC 29110 profil Basic · B) NASA SWEHB 5.08 · C) oba
- choice: A — analiza na podstawie repozytorium m1981/iso-29110-5-1 (rozdziały 05, 06, 07, 09)
- date: 2026-10-14

### D-06 Model śledzalności szablonu
- status: resolved
- options: A) model z uzupełnieniami: scenki, zakres In/Out, zasady wskazują decyzję, ekrany realizują przypadki, sprawdzanie pojęć, hook commit-msg · B) tylko elementy istniejące w gtd2
- choice: A — zapisany w narzedzia/id.toml i sprawdzany przez narzedzia/slad.py
- date: 2026-10-13

### D-05 Schematy ID w jednym pliku
- status: resolved
- options: A) narzedzia/id.toml czytany przez skrypty · B) wzorce wpisane w skrypty
- choice: A
- date: 2026-10-13

### D-04 Moduły dziedzinowe
- status: resolved
- options: A) katalog moduly/ kopiowany w razie potrzeby · B) wszystko w rdzeniu
- choice: A — nawigacja, ryzyka, model stanów
- date: 2026-10-13

### D-03 Język szablonu
- status: resolved
- options: A) polski; wymagania EARS po angielsku; nazwy plików bez polskich znaków · B) całość po angielsku
- choice: A
- date: 2026-10-13
- notes: warstwę maszynową (kody, pola, stany, pliki) zmienia D-17; treść zostaje po polsku

### D-02 Sposób powstania szablonu
- status: resolved
- options: A) nowe repozytorium z uogólnionych plików gtd2 · B) przebudowa gtd2
- choice: A — repozytorium PycharmProjects/ai-sldc-template; decyzje D-02…D-06 przeniesione z rejestru gtd2 (tam numery 48–52)
- date: 2026-10-13

### D-01 Przyjęcie szablonu człowiek + agent
- status: resolved
- choice: rdzeń (plan, kontrakt, rejestr, zasady, słownik, zakres, scenki, przypadki użycia, wymagania EARS, testy, macierz śladu), narzędzia i hooki, moduły opcjonalne
- date: 2026-10-13
