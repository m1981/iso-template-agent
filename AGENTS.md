# AGENTS.md — jak pracujemy

Przeczytaj na start każdej sesji, w tej kolejności: kontrakt-decyzji.md (obowiązuje zawsze), ten plik, plan.md, progress.md, decisions.md.

Ten plik opisuje proces: ślad, zmiany, rolę agenta (ISO/IEC 29110 WP.05 i część WP.10). Co powstaje, po co i kiedy, jest w plan.md (D-08).

Język (D-17): warstwa maszynowa po angielsku (kody ID, nazwy pól, stany, nazwy plików i skryptów, kody błędów), treść i rozmowa po polsku. Tłumaczenie terminów normy: glossary.md, „Terminy procesu”.

Odwołania D-nn w tym pliku, README.md, Makefile, .githooks/ i tools/ wskazują decyzje szablonu; po `make new-project` są w archive/template/decisions.md.

## Artefakty i źródła prawdy
P-01 Repozytorium jest jedynym źródłem prawdy dla wszystkich artefaktów. Kopie w innych narzędziach są widokami albo archiwum.

| Artefakt | Plik | ID |
| --- | --- | --- |
| Kontrakt interakcji człowiek–agent | kontrakt-decyzji.md | — |
| Plan: cele, kamienie milowe, zadania, ryzyka projektu (WP.10) | plan.md | OBJ-nn, MS-nn, TSK-nn, PRK-nn |
| Rekord postępu, generowany (WP.09) | progress.md | — |
| Rejestr decyzji i kolejka tematów (WP.03, WP.07) | decisions.md | D-nn, Q-nn |
| Rejestr korekt (WP.04) | corrections.md | COR-nn |
| Rekordy weryfikacji (WP.23) | verification.md | VER-nn |
| Listy kontrolne przeglądu | checklist.md | REQ.n, UC.n … |
| Role i karty sesji | roles/ | — |
| Rekordy walidacji (WP.22) | validation.md | VAL-nn |
| Rekordy akceptacji (WP.01) | acceptance.md | ACC-nn |
| Zasady projektowe | principles.md | DP-nn |
| Słownik pojęć i terminy normy | glossary.md | G-GRP-nn |
| Scenki użytkownika | scenarios.md | SC-nn |
| Zakres In/Out, aktorzy i cele | scope.md | IO-nn |
| Przypadki użycia | use-cases.md | UC-nn |
| Wymagania EARS (typ REQ) | requirements.md | ABC-nn: trzy litery obszaru, np. CAP-nn |
| Testy akceptacyjne | tests/*.feature | AT-nn |
| Macierz śladu, generowana (WP.21) | trace.md | — |
| Zgodność z ISO/IEC 29110, generowana | iso-map.html | — |
| Moduły opcjonalne | modules/ (kopiowane do katalogu głównego) | E-nn, RSK-nn |

P-02 ID są niezmienne i nigdy nie są używane ponownie. Schematy ID, pola rodziców, reguły pokrycia, stany i odpowiedniki w ISO/IEC 29110 są tylko w tools/id.toml (model śledzalności); ten plik do niego odsyła.

## Ślad
P-03 Dziecko podaje tylko rodzica (pola z id.toml, np. `source:`, `scenarios:`, `verifies:`). Nigdzie nie wypisuje się dzieci. Jedyny wyjątek: zadanie planu wskazuje w `produces:`, co wytwarza (D-09).
P-04 Macierz w obie strony generuje tools/trace.py do trace.md, rekord postępu tools/progress.py do progress.md, a stronę zgodności z normą tools/iso_map.py do iso-map.html (z id.toml i tools/iso29110.toml); nie edytuje się ich ręcznie.
P-05 Pre-commit odrzuca: błędy E1–E9, nieaktualny trace.md, progress.md lub iso-map.html oraz, gdy wdrożono moduł nawigacji, łamanie jego reguł i nieaktualną mapę. Ostrzeżenia W1–W5 nie blokują.

## Stany i gotowość (P-06)
Produkty pracy (typy z `product = true`) mają obowiązkowe pole `status` ze stanami normy (D-11, D-14): `initiated` → `verified` (jest rekord VER z wynikiem `pass` w verification.md; bez niego ostrzeżenie W3, D-15) → `approved` (dla wymagań decyzja D-nn, P-08). Decyzje, zadania, ryzyka projektu i rekordy mają własne statusy. Baseline nie jest stanem: wynika z tagu.

Wymaganie: jeden wzorzec EARS · tekst zaczyna się zgodnie ze wzorcem · dokładnie jedno „shall” · podmiotem jest system · słowa pisane wielką literą są pojęciami ze słownika · ma źródło · status jest jednym ze stanów produktów pracy. Wszystko to sprawdza trace.py; mierzalność i sens ocenia przegląd.
Przegląd (rekord VER albo VAL) prowadzi się według list z checklist.md (D-31): pole `checklist:` wskazuje listy, `failed:` niespełnione punkty. Wymaganie ma opcjonalne pole `quality:`; trace.md pokazuje charakterystyki jakości bez wymagań (D-33).
Przypadek użycia: ma rodzica (scenkę w `scenarios:` albo pozycję zakresu In w `scope:`; sprawdza to parent_rules w id.toml), poziom celu i gwarancje.

## Zmiana
P-07 Każda zmiana: edycja → `git diff` → `make check` → jeden commit na odpowiedź Użytkownika. Opis commita wskazuje co najmniej jedno istniejące ID (hook commit-msg).
P-08 Zatwierdzenie lub zmiana zatwierdzonego wymagania wymaga decyzji D-nn w rejestrze. Ostrzeżenie W5 (D-32) po zmianie mówi, które zweryfikowane elementy straciły ważność weryfikacji, bo zmieniły się one same albo ich rodzic: przejrzyj je i zapisz nowy rekord VER.
P-09 Zamknięty etap = tag `baseline-nn-nazwa` (`make baseline N=…`), wpisany w pole `tag:` kamienia milowego w plan.md. Po tagu odśwież progress.md (`make progress`) i dołącz go do następnego commita. Po każdej sesji push na GitHuba (WP.12, D-13); tagi idą razem z nim. Przy każdym kamieniu milowym `make restore-check RECORD=1`: sprawdzenie odtworzenia z kopii zapisane jako rekord VER (PM.02.07, D-35).

## Role i sesje (D-36, D-37)
Role normy rozkładają się na Użytkownika i sesje agenta; szczegóły, warunki pilota i odłożone pomysły: roles/README.md.

| Kto | Role ISO/IEC 29110 | Co robi |
| --- | --- | --- |
| Użytkownik | klient, decyzje kierownika projektu | walidacja (VAL), akceptacja (ACC), zatwierdzanie (decyzje D) |
| sesja autora | analityk, lider techniczny, asystent kierownika, projektant ekranów | specyfikacja, plan, rejestr; według tego pliku |
| sesja weryfikatora | niezależny weryfikator (SI.O7) | rekordy VER i propozycje korekt; według roles/verifier.md |

Autor nie weryfikuje sam siebie: commit, który dodaje rekord VER albo VAL z wynikiem pass, nie może zmieniać weryfikowanych elementów (E9, tools/check_separation.py).

## Agent
P-10 Bez decyzji Użytkownika agent nie: zmienia znaczenia pojęć, zatwierdza wymagań, usuwa plików, zmienia reguł w id.toml. Może: poprawiać format, dodawać ślad, uruchamiać kontrole, sprzątać blokady gita. Przy założeniu, którego nie może sprawdzić, przedstawia je jako decyzję do potwierdzenia.

## Kolejność wdrażania praktyk
1 plan, kontrakt, rejestr, baseline · 2 słownik, scenki, zakres · 3 przypadki użycia (brief) · 4 wymagania ze śladem · 5 testy akceptacyjne (potem pokrycie jako błąd) · 6 moduły według potrzeby · 7 suspect links i niezależny przegląd przez osobnego agenta (gdy jest kilkadziesiąt wymagań).

## Świadomie pomijamy
Komisję zmian, formalne plany V&V, CM i QA jako osobne dokumenty, audyty procesu, kwalifikację narzędzi, metryki pokrycia kodu.

## Polecenia
    make hooks       # raz, w nowym klonie (hooki i push z tagami)
    make check       # wszystkie kontrole
    make trace       # odśwież trace.md
    make progress    # odśwież progress.md
    make iso-map     # odśwież iso-map.html
    make new-project # raz, w kopii szablonu (historia szablonu do archive/template/)
    make navigation  # odśwież mapę (moduł nawigacji)
    make baseline N=01-nazwa
    make restore-check [RECORD=1]  # odtworzenie z kopii: klon origin, HEAD, tagi, ślad
    make test        # po każdej zmianie tools/ lub id.toml
    make test-distribution         # granica dystrybucji copierem (wymaga copiera w przypiętej wersji)
    make process-update V=vX.Y.Z   # w projekcie z copiera: aktualizacja procesu z kontrolą wyniku (D-52)
    make test-report               # raport testów AT z runner: (WP.20, D-60)
    make golden                    # wyjścia narzędzi wobec złotego wzorca (D-61)
    make process-kit [TESTS=1]     # ślad warstwy procesu do czasu przeniesienia (D-64)
