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

Brak otwartych decyzji.

## W kolejce

### Q-01 Strona „ISO 29110 a nasz model śladu” po rozszerzeniu
- notes: kolory pokrycia na stronie pokazują stan sprzed D-08…D-19; odświeżyć. Zrobione w D-25 (2026-10-16).

### Q-02 Przeniesienie zmian szablonu do gtd2
- notes: w gtd2 ID zostają (D-17); migrują nazwy pól, stanów i plików; 28 wymagań przechodzi z draft na initiated (D-11); każdy produkt dostaje status (D-14)

## Rozstrzygnięte

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
