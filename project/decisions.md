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

### D-74 Ustalenia z wykonania przeniesienia
- status: open
- options: A) przyjąć jak wdrożono · B) przyjąć z poprawkami (wskaż które)
- proposal: A
- notes: lista w reference/layout-map.md, część 8: stare trace.md i progress.md w archive/flat-layout/ (w reports/ są raporty warstwy procesu); korzeń projektu z PROCESS_ROOT albo z gita; check_refs.py w projekcie pomija process/, a w repozytorium szablonu rozwiązuje ścieżki układu projektu względem template/ i wzorców; wyjątek dla przykładowej mapy nawigacji wbudowany w check_leak.py; pary ekranów w mapie projektu (%% key-pair:); init.py dopuszcza nieśledzone pliki; wzorce dokumentów bez odwołań do decyzji szablonu; nowa reguła P-11 w template/process/AGENTS.md (pakiet zmienia się tylko przez make process-update)

### D-75 Kontrola pojęć słownika projektu w plikach procesu
- status: open
- options: A) check_leak.py porównuje tylko angielskie nazwy pojęć (z nawiasu w tytule) i tylko pisane wielką literą, jak E6 w wymaganiach · B) pojęcia wyłączone z kontroli wpisuje projekt w project/check_leak.allow · C) bez zmian
- proposal: A
- notes: test na danych testowych pokazał, że słownik z ogólnymi pojęciami (Element, User) daje zgłoszenia w tekstach procesu, które używają tych słów potocznie; w gtd2 (słownik GTD) make check wyłożyłby się od razu. Do rozstrzygnięcia przed pilotem

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
- notes: zrobione 2026-10-18: Mac zsynchronizowany do f855d51 (drzewo identyczne z kopią), test i make check przechodzą na Pythonie 3.10, tag baseline-01-szablon założony na Macu (D-24). Tagi baseline-00-przed-en i baseline-01-szablon wypchnięte z Maca przez Użytkownika. 2026-10-19: make restore-check RECORD=1 z kopii origin na 7779435, wynik pass (VER-01). Q-10 zamknięta.

### Q-11 Stan projektu wobec aktualizacji (active, frozen, retired)
- notes: z dokumentu Użytkownika o copierze (2026-10-19); bramka aktualizacji odmawia dla frozen i retired. Wróć, gdy z szablonu korzysta więcej niż jeden projekt albo gdy któryś projekt ma przestać przyjmować aktualizacje

### Q-12 Propozycja: warstwy kontekstu i pakiety praktyk
- notes: plik Użytkownika PROPOSAL-CONTEXT-AND-PRACTICE-PACKAGES.md (D-66). Tematy poza D-68 i D-69: krótszy AGENTS.md i ładowanie kontekstu według zadania (K0–K6); minimalny start z profilem ryzyka i definicją ukończenia; zakres szablonu: sama specyfikacja czy cały cykl z kodem i TDD; rejestr aktywacji pakietów praktyk (available, proposed, pilot, active…); pomiar wartości praktyk (słuszna uwaga: kryterium 1 pilota Q-03 jest nierozstrzygające); strona ISO rozdzielająca wsparcie przez szablon, zastosowanie w projekcie, wykonanie i ocenę zgodności; zmiana kontraktu (co agent rozstrzyga sam, commit na spójną zmianę zamiast na odpowiedź). Wróć po wydaniu v1.0.0 albo wcześniej, gdy któryś temat zablokuje pilota

## Rozstrzygnięte

### D-73 Kryteria odbioru w rekordzie postępu
- status: resolved
- options: A) progress.md dostaje sekcję „Kryteria odbioru” z kamieniami i zadaniami, które je mają; sekcja tylko wtedy, gdy są (bez zmiany złotego wzorca) · B) bez zmian: kryteria czyta się w planie
- proposal: A
- choice: A — sekcja „Kryteria odbioru” w reports/progress.md, tylko gdy kamień albo zadanie ma acceptance_criteria; dane złotego wzorca bez kryteriów, a sprawdza je osobny przypadek testu (acceptance-criteria)
- date: 2026-10-22

### D-72 Commity przeniesienia
- status: resolved
- options: A) dwa commity w jednej odpowiedzi: najpierw wyłącznie git mv, potem zmiany ścieżek i narzędzi; wyjątek od P-07 · B) jeden commit (D-54)
- proposal: A
- choice: A — przy przeniesieniu (zadanie przeniesienia w project/plan.md) dwa commity w jednej odpowiedzi; wyjątek od zasady jednego commita na odpowiedź dotyczy tylko tego zadania
- date: 2026-10-22
- notes: git rozpoznaje przeniesienie po podobieństwie treści; commit z samym git mv daje pewną historię (K-4)

### D-71 Kryteria odbioru zadań
- status: resolved
- options: A) opcjonalne pole acceptance_criteria w typie TSK (id.toml) i kryteria K-1…K-11 w zadaniu przeniesienia · B) kryteria w notes zadania · C) tylko w mapie
- proposal: A
- choice: A — pole acceptance_criteria w TSK (id.toml, wzór w plan.md, fixture testu); K-1…K-11 w zadaniu przeniesienia w project/plan.md
- date: 2026-10-22
- notes: uzasadnienie propozycji mówiło, że rekord postępu pokaże kryteria; to nieprawda, progress.py nie pokazuje ich nawet dla kamieni (D-73)

### D-70 Commit 7779435 bez ID w opisie
- status: resolved
- options: A) zostawić i zapisać tutaj jako znany wyjątek: przepisanie wymagałoby zmiany 8 opublikowanych commitów (7779435 i 7 kolejnych) i wymuszonego pushu, a jedyne naruszenie to brak ID w opisie (ślad i pliki generowane były aktualne) · B) przepisać historię i wymusić push (wszystkie klony trzeba potem wyrównać)
- proposal: A
- choice: A — 7779435 zostaje; znany wyjątek od reguły ID w opisie commita (powstał bez hooków); historii nie przepisujemy (D-46)
- date: 2026-10-22

### D-69 Na czym działa pre-commit: katalog roboczy czy indeks
- status: resolved
- options: A) kontrole śladu i aktualności w pre-commit czytają zawartość indeksu (to, co wchodzi do commita), jak już robi check_separation.py; test z częściowo dodanymi zmianami · B) zostaje katalog roboczy, a ograniczenie zapisane w AGENTS.md
- proposal: A
- choice: A — .githooks/pre-commit sprawdza migawkę indeksu (git checkout-index) z GIT_DIR prawdziwego repozytorium; przypadek precommit-index w test_tools.py (błąd tylko w indeksie odrzucony, błąd tylko w katalogu roboczym przepuszczony), stary hook nie przechodzi tego testu; wymaganie HKS-05 z testem w spec/tests/process-kit.feature
- date: 2026-10-22
- notes: z propozycji Użytkownika (D-66), sekcja 10: dziś trace.py, progress.py i iso_map.py w pre-commit czytają katalog roboczy, więc commit z częściowo dodanymi zmianami może przejść kontrolę na plikach, których nie zawiera

### D-68 Miejsce pakietów praktyk w układzie po przeniesieniu
- status: resolved
- options: A) zarezerwować w mapie (doc/layout-map.md) process/practices/ na pakiety praktyk (wzorowane na załączniku E) i evidence/ w projekcie na dowody; bez treści, tylko miejsce, żeby nie przenosić drugi raz · B) nie rezerwować; wrócić po przeniesieniu
- proposal: A
- choice: A — process/practices/ i evidence/ zarezerwowane w doc/layout-map.md, bez plików
- date: 2026-10-22
- notes: z propozycji Użytkownika (D-66), sekcje 7 i 9; propozycja zakłada płaski układ, bo nie zna D-42 i D-54

### D-67 Gdzie trzymać dwa pliki Użytkownika
- status: resolved
- options: A) propozycja do doc/ (po przeniesieniu reference/) jako materiał wejściowy, z tematem w kolejce (Q-12); eksport strony ISO zostaje poza gitem, bo źródłem jest iso-map.html · B) oba pliki do doc/ · C) oba poza gitem
- proposal: A
- choice: A — propozycja w doc/PROPOSAL-CONTEXT-AND-PRACTICE-PACKAGES.md (treść identyczna z plikiem z laptopa, ten sam hash bfbecfa); eksport strony ISO zostaje na laptopie poza gitem
- date: 2026-10-22
- notes: na laptopie propozycja jest dodana do indeksu w katalogu głównym; check_refs.py zgłasza w niej przyszłe katalogi (practices/, evidence/, src/), a w doc/ ich nie sprawdza

### D-64 Założenia przy wykonaniu D-59…D-63
- status: resolved
- options: A) przyjąć jak wdrożono · B) przyjąć z poprawkami (wskaż które)
- proposal: A
- choice: A — założenia przyjęte jak wdrożono
- date: 2026-10-22
- notes: (1) katalog testów jako plik Gherkin spec/tests/process-kit.feature zamiast catalog.md: typ AT zostaje jednym formatem; (2) pliki warstwy procesu (spec/, project/plan.md, reports/, reference/golden/) od razu w docelowych miejscach; do przeniesienia ślad liczy przejściowy tools/process_kit_view.py (make process-kit), a reports/ nie sprawdza pre-commit; (3) check_refs.py pomija rejestr decyzji, doc/, reference/, archive/, pliki generowane, .gitignore i kod testów; sama nazwa pliku wystarcza, gdy taki plik istnieje; 16 wyjątków z powodem w tools/check_refs.allow; (4) check_leak.py pomija D-nn i Q-nn (decyzje szablonu, D-56) i kod testów; ID wymagań liczy tylko w obszarach, które projekt ma; wyjątek dla przykładowej mapy modułu nawigacji (2 pliki, test używa jej jako danych); lista plików procesu w Makefile do przeniesienia; (5) termin kamienia „Wydanie v1.0.0”: 2026-11-30; (6) poprawione przykłady z konkretnymi ID na „nn” w roles/verifier.md i komentarzu tools/model.py; (7) złoty wzorzec ze stałym rejestrem z jedną decyzją, żeby nie zależał od rejestru szablonu; (8) bez testu zostają LAY-01, LAY-02, MIG-01, MIG-02 (powstaną z przeniesieniem i migracjami) oraz ręczne TRC-01 i LNG-01 do przeglądu

### D-66 Dwa nowe pliki Użytkownika na laptopie
- status: resolved
- options: A) do repozytorium jako materiały wejściowe · B) zostają poza gitem · C) najpierw przeczytać i ocenić wpływ na szablon, miejsce później
- proposal: C
- choice: C — przeczytane 2026-10-22; miejsce przechowania: D-67
- date: 2026-10-22
- notes: PROPOSAL-CONTEXT-AND-PRACTICE-PACKAGES.md (propozycja z 2026-10-22, napisana na stanie 7779435, bez wiedzy o D-41…D-64): warstwy kontekstu K0–K6, minimalny start (Day 1), pakiety praktyk wzorowane na załączniku E z rejestrem aktywacji, pomiar wartości praktyk, podział odpowiedzialności człowiek–agent, kontrole wiązane z wersją wejść. „ISO 29110 a nasz model śladu.md”: eksport opublikowanej strony z 2026-10-19, kopia tego, co generuje iso-map.html

### D-65 Który folder na laptopie jest roboczy
- status: resolved
- options: A) iso-template-agent: aktualizacja do GitHuba przez fast-forward, hooki, tagi; ai-sldc-template zostaje jako archiwum · B) ai-sldc-template · C) nic nie ruszać
- proposal: A
- choice: A — iso-template-agent zaktualizowany do 11ddded (drzewo zgodne z GitHubem, git fsck bez błędów), make hooks, tagi pobrane; pliki Użytkownika nietknięte; make check, make test (60 przypadków) i make golden przechodzą na Pythonie 3.10; test dystrybucji: nie uruchomiono (brak copiera na laptopie)
- date: 2026-10-22
- notes: pierwsza próba aktualizacji się nie udała, bo folder nie pozwalał usuwać plików (git podmienia pliki przez usunięcie): zostały index.lock i 49 nieśledzonych kopii plików z GitHuba. Po zgodzie Użytkownika na usuwanie usunięte tylko pliki sprawdzone jako identyczne z GitHubem i pliki tymczasowe tej próby. Commit 7779435 (zapis sesji GTD) nie ma ID w opisie, bo powstał bez hooków: D-70

### D-63 Kryteria odbioru wydania v1.0.0
- status: resolved
- options: A) kamień milowy w planie warstwy procesu z acceptance_criteria AC-1…AC-9 (lista w odpowiedzi z 2026-10-19), rekordy VAL z pilota gtd2 i rekord ACC Użytkownika; tag v1.0.0 dopiero po ACC · B) v1.0.0 po przejściu testów, bez pilota
- proposal: A
- choice: A — project/plan.md warstwy procesu: cel, kamień milowy „Wydanie v1.0.0” z kryteriami AC-1…AC-9, 10 zadań i 2 ryzyka projektu
- date: 2026-10-19

### D-62 Kontrola przecieku domeny do procesu
- status: resolved
- options: A) automatyczna: w process/ dozwolone są tylko zastępcze ID z „nn” (np. UC-nn), a nie konkretne numery; w projekcie kontrola, że pliki process/ nie zawierają pojęć z jego słownika; w warstwie procesu punkt listy kontrolnej przeglądu rejestru: decyzja dotyczy procesu, nie produktu klienta · B) tylko punkt listy kontrolnej
- proposal: A
- choice: A — tools/check_leak.py w make check (konkretne ID i pojęcia słownika projektu); lista TPL w checklist.md
- date: 2026-10-19
- notes: z D-57: w poprzednim podejściu terminy, decyzje i zadania produktu klienta trafiały do rejestrów procesu

### D-61 Weryfikacja samego przeniesienia
- status: resolved
- options: A) przed przeniesieniem złoty wzorzec wyjść narzędzi (trace.md, progress.md, iso-map.html, komunikaty 21 psuć i 5 ostrzeżeń na fixture); po przeniesieniu wyjścia identyczne poza ścieżkami; do tego niezmienniki: treść przeniesionych dokumentów bajt w bajt, pokrycie mapy 50/50, git log --follow dla każdego pliku, nowe narzędzie check_refs.py w make check (każda ścieżka wspomniana w dokumentach i kodzie procesu istnieje) · B) wystarczą make test i make test-distribution
- proposal: A
- choice: A — tools/golden_master.py i wzorzec w reference/golden/ (31 plików); tools/check_refs.py z listą wyjątków w make check
- date: 2026-10-19
- notes: check_refs.py zostaje na stałe: łapie dokładnie te „małe zależności”, o które pyta Użytkownik, także przy przyszłych zmianach

### D-60 Powiązanie testów w Pythonie z wymaganiami
- status: resolved
- options: A) katalog testów w warstwie procesu (spec/tests/catalog.md): wpisy AT-nn z verifies: REQ i polem runner: plik::przypadek; testy wypisują nazwy przypadków, a kontrola sprawdza, że każdy runner istnieje i przeszedł; nowe pole runner to zmiana reguł id.toml · B) tylko pliki .feature dla scenariuszy ludzkich, testy w Pythonie bez śladu · C) znaczniki „# verifies:” w kodzie testów i nowy format parsera
- proposal: A
- choice: A — pole runner: w typie AT (id.toml) i kontrola E4 w trace.py; katalog jako spec/tests/process-kit.feature (52 testy, 50 z runner:); testy wypisują wiersze CASE; tools/test_report.py (make test-report) zapisuje raport testów
- date: 2026-10-19
- notes: wynik przebiegu z nazwami przypadków to raport testów (WP.20)

### D-59 Wymagania szablonu
- status: resolved
- options: A) przed przeniesieniem spisać wymagania szablonu w warstwie procesu (spec/requirements.md, EARS, podmiot „Process kit”), każde ze źródłem w decyzji D-nn; obszary: TRC ślad, HKS hooki, SEP rozdział ról, DST dystrybucja, INI zakładanie projektu, UPD bramka aktualizacji, MIG migracje, LAY układ i własność plików, LNG język, ISO zgodność · B) bez wymagań; decyzje i testy wystarczą
- proposal: A
- choice: A — spec/requirements.md warstwy procesu: 56 wymagań EARS (podmiot „Process kit”) w 15 obszarach, każde ze źródłem w decyzji; słownik 26 pojęć procesu w spec/glossary.md
- date: 2026-10-19
- notes: dziś wymagania szablonu są rozproszone w 58 decyzjach; bez nich nie da się wykazać, że przeniesienie niczego nie zgubiło (każde wymaganie musi mieć test przed i po)

### D-58 new_project.py
- status: resolved
- options: A) do archive/tools/ (archiwum, bez usuwania); nowy init.py zakłada dokumenty ze wzorców · B) przerobić new_project.py na init.py w tym samym pliku (historia zostaje w git log --follow)
- proposal: B
- choice: B — new_project.py przerobiony na init.py w tym samym pliku (git mv)
- date: 2026-10-19
- notes: B zachowuje historię pliku i nie zostawia martwego kodu; A zachowuje plik do wglądu

### D-57 Podział słownika
- status: resolved
- options: A) tabela „Terminy procesu (ISO/IEC 29110)” do process/terms.md (aktualizuje copier); spec/glossary.md tylko z pojęciami projektu · B) cały słownik w projekcie
- proposal: A
- choice: A — terminy normy w process/terms.md, w spec/glossary.md tylko pojęcia projektu. Użytkownik: „ważne, żeby domena nie przeciekała do procesu”; w poprzednim podejściu w rejestrach procesu z czasem pojawiały się terminy, decyzje i zadania z produktu klienta
- date: 2026-10-19

### D-56 Odwołania do decyzji szablonu w plikach procesu
- status: resolved
- options: A) w plikach process/ odwołania do decyzji warstwy procesu piszemy jako „szablon D-nn” i odsyłamy do CHANGELOG.md w repozytorium szablonu; numer D-nn projektu się nie miesza · B) bez odwołań do decyzji w plikach procesu; uzasadnienia tylko w rejestrze warstwy procesu · C) zostawić D-nn bez oznaczenia
- proposal: A
- choice: A — w plikach procesu „szablon D-nn” z odesłaniem do CHANGELOG.md
- date: 2026-10-19
- notes: dziś 16 plików procesu (AGENTS.md, README.md, Makefile, hooki, narzędzia, id.toml, karty ról, moduły) ma 108 odwołań D-nn; w projekcie D-01 to „Start projektu”, więc gołe D-17 wskazywałoby złą decyzję

### D-55 Podział tools/id.toml
- status: resolved
- options: A) reguły modelu (typy, pola, stany, wspólne pola) w process/tools/id.toml; system, ocena zgodności z normą (iso_other, iso_partial, iso_out_of_scope) i migrated_to w project/settings.toml · B) jak A, ale ocena zgodności zostaje w regułach procesu
- proposal: A
- choice: A — reguły w process/tools/id.toml; system, ocena zgodności i migrated_to w project/settings.toml
- date: 2026-10-19
- notes: ocena zależy od etapu projektu (np. WP.14 oprogramowanie poza etapem specyfikacji); wzorzec settings.toml niesie ocenę domyślną

### D-54 Mapa ścieżek przejścia na trzy warstwy
- status: resolved
- options: A) zatwierdzić doc/layout-map.md w całości: układ trzech warstw, właściciele, każdy z 50 plików z nowym miejscem, nowe pliki, zmiany w narzędziach (w tym ścieżki file w id.toml); przeniesienie jednym commitem przez git mv · B) zatwierdzić z poprawkami (wskaż wiersze)
- proposal: A
- choice: A — mapa doc/layout-map.md zatwierdzona w całości; przeniesienie jednym commitem przez git mv, po przygotowaniu weryfikacji (D-59…D-63)
- date: 2026-10-19
- notes: założenia w mapie: umowa (agreement.md) bez nowego typu ID, zatwierdzana decyzją D; moduły wdraża init.py --module zamiast cp -r; dane modułu nawigacji w spec/navigation/, kod w process/modules/navigation/; ryzyka produktu (RSK) w spec/risks.md; warstwa procesu ma tylko te typy, których pliki istnieją (D, Q, VER, VAL…), bo typ bez pliku jest nieaktywny

### D-53 Założenia przy wykonaniu D-49 i D-52
- status: resolved
- options: A) przyjąć jak wdrożono · B) przyjąć z poprawkami (wskaż które)
- proposal: A
- choice: A — założenia przyjęte jak wdrożono
- date: 2026-10-19
- notes: (1) przypięta wersja copiera 9.19.1, bo na niej przeszedł test granicy dystrybucji; dokument Użytkownika sprawdzał 9.17.1, więc _min_copier_version w szablonie testowym to 9.17.1; (2) plik answers: .copier-answers.process.yml; (3) log bramki w .git/process-update.log; (4) walidacja w bramce: make check i make test; (5) bramka bez --defaults pokazuje pytania copiera na ekranie, a do logu zapisuje tylko polecenie i kod; (6) process_update.py i test_distribution.py leżą na razie w tools/; przy przeniesieniu (D-50) bramka idzie do process/tools/, a test do warstwy procesu poza szablonem; (7) make hooks odmawia, gdy core.hooksPath wskazuje inny katalog niż .githooks

### D-52 Bramka aktualizacji projektu
- status: resolved
- options: A) jedno polecenie make process-update V=vX.Y.Z: odmawia przy brudnym drzewie, wymaga jawnej wersji, używa przypiętej wersji copiera i właściwego pliku answers, zapisuje pełny log i kod wyjścia, wykrywa znaczniki konfliktu także w nowych plikach, uruchamia make check i make test; nie robi stash ani commita · B) instrukcja w README, kroki ręczne
- proposal: A
- choice: A — make process-update V=vX.Y.Z (tools/process_update.py)
- date: 2026-10-19
- notes: copier 9.19.1 w próbie z D-43 zakończył update kodem 0 i zostawił konflikt (UU); dokument Użytkownika potwierdza to samo dla 9.17.1

### D-51 Migracja dokumentów po zmianie procesu
- status: resolved
- options: A) każde wydanie, które zmienia reguły dotyczące istniejących dokumentów, ma wpis w process/MIGRATIONS.md: która reguła, których dokumentów dotyczy (nowe, w toku, zakończone), jak je znaleźć (kody błędów i ostrzeżeń trace.py), kroki i warunek zakończenia; projekt zapisuje zakończenie migracji decyzją D i polem migrated_to w pliku ustawień; trace.py ostrzega, gdy wersja procesu jest nowsza niż migrated_to · B) tylko zasada w tekście, bez kontroli
- proposal: A
- choice: A — process/MIGRATIONS.md przy każdym wydaniu zmieniającym reguły; zakończenie migracji decyzją w projekcie i polem migrated_to; trace.py ostrzega, gdy wersja procesu jest nowsza
- date: 2026-10-19
- notes: zasada Użytkownika (2026-10-19), dosłownie: „Copier aktualizuje narzędzia, normy i wzorce. Dostosowanie istniejących dokumentów wymaga jawnie opisanej migracji i osobnego kroku. Aktualizacja pakietu nie oznacza automatycznie zakończenia migracji dokumentów.” Opcje dotyczą tylko tego, jak ją wykonać. Przykład z naszej historii: D-17 zmieniła nazwy pól i stanów, a gtd2 wymaga migracji (Q-02)

### D-50 Kolejność wykonania D-41, D-42, D-44
- status: resolved
- options: A) najpierw D-43 (szablon do template/), potem D-41, D-42 i D-44 w szablonie, na końcu przejście gtd2 na copier (zamiast Q-02) · B) najpierw D-41, D-42, D-44 w obecnym płaskim układzie, copier później
- proposal: A
- choice: A — najpierw testy granicy dystrybucji na małym szablonie, potem template/ z D-41, D-42, D-44, na końcu gtd2 (zamiast Q-02)
- date: 2026-10-19
- notes: przy B pliki przenosi się dwa razy

### D-49 Wersje szablonu
- status: resolved
- options: A) wydania szablonu jako tagi vX.Y.Z (dla copiera), tagi baseline-nn zostają dla kamieni pracy nad procesem i nie stoją na tym samym commicie co wydanie · B) jeden rodzaj tagów
- proposal: A
- choice: A — wydania jako nieprzesuwane tagi vX.Y.Z z przetestowanego commita, jawna wersja przy copy i update, copier przypięty, baseline-nn nigdy na commicie wydania
- date: 2026-10-19
- notes: copier szuka wersji w tagach vX.Y.Z; gdy na commicie stoi też baseline-nn, w .copier-answers.yml ląduje nazwa baseline'u

### D-48 Czy praca nad procesem sama używa procesu
- status: resolved
- options: A) tak: katalog główny ma własny rejestr, rekordy i materiały wejściowe, a narzędzia z template/tools/ działają na nim przez parametr katalogu i osobny model śladu dla warstwy procesu · B) tylko rejestr i git, bez kontroli śladu w warstwie procesu
- proposal: A
- choice: A — warstwa procesu sama używa procesu: własny rejestr i rekordy, narzędzia z template/ przez parametr katalogu
- date: 2026-10-19
- notes: dziś szablon sprawdza sam siebie hookami (D-01…D-46, VER-01); w warstwie procesu klientem są projekty, więc wyniki pilota z GTD (Q-03) stają się tu rekordami walidacji

### D-47 Co dostarcza copier, a co należy do projektu
- status: resolved
- options: A) copier dostarcza i aktualizuje tylko katalog process/: narzędzia, reguły (AGENTS procesu, kontrakt, listy kontrolne, role, reguły id.toml), puste wzorce dokumentów, hooki, opis migracji; dokumenty projektu (project/, spec/, records/) powstają ze wzorców jawnym poleceniem make init i są poza zbiorem copiera; AGENTS.md, CLAUDE.md, README.md i Makefile w katalogu głównym należą do projektu i wpinają proces jedną linią; ustawienia projektu (system, prefiksy obszarów, moduły, ocena zgodności) w jednym pliku lokalnym · B) copier zarządza całym drzewem, dokumenty projektu zakłada raz przez _skip_if_exists, konflikty rozwiązywane ręcznie
- proposal: A
- choice: A — copier dostarcza tylko process/; dokumenty projektu przez make init, poza zbiorem copiera; AGENTS.md, CLAUDE.md, README.md, Makefile w katalogu głównym należą do projektu; ustawienia projektu w jednym pliku
- date: 2026-10-19
- notes: przeformułowana 2026-10-19 po dokumencie Użytkownika „Copier: konfiguracja i proces pracy dla nowego zastosowania” (historia truth-ledger → kuchnie): _skip_if_exists odtwarza usunięty plik przy update; własność musi być ustalona dla każdej ścieżki; główny AGENTS.md należy do projektu; przestrzeń nazw od pierwszego wydania. Poprzednie brzmienie: pliki procesu aktualizowane, pliki projektu przez _skip_if_exists, dostosowanie w project/tailoring.md

### D-45 Kopiowanie szablonu bez rsync
- status: resolved
- options: A) git archive HEAD | tar -x -C ../nowy-projekt · B) make new-project DEST=… robi kopię i start jednym poleceniem
- proposal: rozstrzyga D-43: przy D-43 A kopię robi copier copy i D-45 się zamyka
- choice: zamknięta przez D-43 A: kopię robi copier copy (Użytkownik: „patrz d43”)
- date: 2026-10-19
- notes: README obiecuje tylko python3 i git, a krok 1 używa rsync, którego nie ma w kopii agenta

### D-43 Trzy warstwy: praca nad procesem, szablon procesu, projekty z szablonu
- status: resolved
- options: A) to repozytorium jest projektem procesu; szablon dla copiera leży w podkatalogu template/ (copier.yml, _subdirectory); projekty (GTD i kolejne) powstają przez copier copy i dostają poprawki procesu przez copier update · B) jedno repozytorium bez podziału; new-project przenosi do archive/template/ cały zapis pracy nad szablonem (rejestr, rekordy, materiały wejściowe, pliki generowane) · C) bez zmian
- proposal: A
- choice: A — to repozytorium jest projektem procesu; szablon w template/; projekty przez copier copy i update
- date: 2026-10-19
- notes: Użytkownik przy odpowiedzi: proces pracy nad procesem, GTD jako klient i pilot procesu, szablon procesu, copier generuje nowe projekty z meta-szablonu. Próba z copierem 9.19.1 (2026-10-19): pliki z _skip_if_exists zostają nietknięte przy update; lokalna zmiana pliku procesu daje konflikt przy update; copier wybiera wersję po tagach vX.Y.Z, a w _commit zapisuje nazwę z git describe (wybrał baseline-02-x stojący na tym samym commicie co v0.2.0)

### D-46 Autor commitów agenta
- status: resolved
- options: A) bez zmian: autor to Użytkownik, udział agenta w linii Co-Authored-By · B) nowe commity agenta jako Claude (noreply@anthropic.com) · C) jak B i przepisanie 18ab080 z wymuszonym pushem
- proposal: A
- choice: A — autorem commitów zostaje Użytkownik; opublikowanej historii nie przepisujemy
- date: 2026-10-19

### D-44 Kolejność startu w README
- status: resolved
- options: A) kroki według normy: umowa → plan → zatwierdzenie i baseline → środowisko → specyfikacja, każdy krok z wynikiem i commitem · B) obecna kolejność
- proposal: A
- choice: A — wykonanie według D-50
- date: 2026-10-19
- notes: ISO/IEC 29110 5.2 (warunki wejścia), PM.01.01–PM.01.16, SI.01, SI.02

### D-42 Układ katalogów
- status: resolved
- options: A) katalogi według rodzaju dokumentu (ISO/IEC/IEEE 15289): process/, project/, spec/, records/, reports/ (generowane), reference/; w katalogu głównym README.md, AGENTS.md, CLAUDE.md, Makefile · B) tylko reports/ i reference/ · C) płasko
- proposal: A
- choice: A — wykonanie według D-50; przeniesienie przez git mv, bez usuwania
- date: 2026-10-19

### D-41 Umowa projektu (WP.02)
- status: resolved
- options: A) nowy plik agreement.md: produkt, cel, ogólny zakres, co dostarczamy, kto akceptuje, wykonalność; zatwierdzany decyzją D, objęty pierwszym baseline'em; plan.md odsyła do niego · B) sekcja w plan.md
- proposal: A
- choice: A — wykonanie według D-50
- date: 2026-10-19
- notes: WP.02 (tabela 14), PM.01.01 (wejście: Agreement [approved]), WP.11: „requirements baseline (i.e. agreement)”

### D-40 Adres origin na Macu
- status: resolved
- options: A) przełączyć na HTTPS · B) zostawić SSH git@github.com:m1981/iso-template-agent.git
- proposal: B (push z Maca przez SSH zadziałał: commit 7779435)
- choice: B — na Macu zostaje SSH
- date: 2026-10-19

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
