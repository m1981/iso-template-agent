# AGENTS.md procesu — jak pracujemy

Plik pakietu procesu (process/): dostarcza go i aktualizuje copier, projekt go nie edytuje (szablon D-47). Odstępstwa projektu są w AGENTS.md w katalogu głównym projektu.

Przeczytaj na start każdej sesji, w tej kolejności: process/kontrakt-decyzji.md (obowiązuje zawsze), ten plik, AGENTS.md projektu, project/agreement.md, project/plan.md, reports/progress.md, project/decisions.md.

Ten plik opisuje proces: ślad, zmiany, rolę agenta (ISO/IEC 29110 WP.05 i część WP.10). Co powstaje, po co i kiedy, jest w project/agreement.md i project/plan.md.

Język (szablon D-17): warstwa maszynowa po angielsku (kody ID, nazwy pól, stany, nazwy plików i skryptów, kody błędów), treść i rozmowa po polsku. Tłumaczenie terminów normy: process/terms.md.

Odwołania „szablon D-nn” w plikach procesu wskazują decyzje szablonu procesu, nie decyzje projektu (szablon D-56); ich opis jest w CHANGELOG.md repozytorium szablonu. Decyzje projektu (D-nn bez słowa „szablon”) są w project/decisions.md.

## Układ projektu (szablon D-42, szablon D-47)

| Katalog | Co zawiera | Kto zmienia |
| --- | --- | --- |
| process/ | reguły, narzędzia, hooki, moduły, wzorce dokumentów, opis migracji | copier (aktualizacja: `make process-update V=vX.Y.Z`) |
| project/ | umowa, plan, rejestr decyzji, ustawienia, wyjątki kontroli | projekt |
| spec/ | słownik, zasady, scenki, zakres, przypadki użycia, wymagania, testy akceptacyjne, moduły | projekt |
| records/ | korekty, weryfikacje, walidacje, akceptacje | projekt |
| reports/ | macierz śladu, rekord postępu, strona zgodności, raport testów | tylko narzędzia |
| reference/ | materiały wejściowe bez kontroli śladu | projekt |

## Start projektu (szablon D-44)
1. `copier copy --vcs-ref vX.Y.Z <szablon> <katalog>`, potem w katalogu `git init` i `python3 process/tools/init.py` (dokumenty ze wzorców), `make hooks`, pierwszy commit „Start projektu (szablon D-01)”.
2. Umowa: project/agreement.md (WP.02), ustawienia: project/settings.toml (`system`).
3. Plan: project/plan.md (PM.01): cele, kamienie milowe, zadania, ryzyka; wynika z umowy.
4. Zatwierdzenie umowy i planu decyzją D-nn, potem pierwszy baseline (`make baseline N=01-umowa`).
5. Środowisko (SI.01): ten plik, process/kontrakt-decyzji.md, hooki, kopia zapasowa (drugi remote).
6. Specyfikacja (SI.02) według „Kolejności wdrażania praktyk” niżej.

## Artefakty i źródła prawdy
P-01 Repozytorium jest jedynym źródłem prawdy dla wszystkich artefaktów. Kopie w innych narzędziach są widokami albo archiwum.

| Artefakt | Plik | ID |
| --- | --- | --- |
| Kontrakt interakcji człowiek–agent | process/kontrakt-decyzji.md | — |
| Umowa (WP.02) | project/agreement.md | — |
| Plan: cele, kamienie milowe, zadania, ryzyka projektu (WP.10) | project/plan.md | OBJ-nn, MS-nn, TSK-nn, PRK-nn |
| Rekord postępu, generowany (WP.09) | reports/progress.md | — |
| Rejestr decyzji i kolejka tematów (WP.03, WP.07) | project/decisions.md | D-nn, Q-nn |
| Ustawienia projektu (podmiot EARS, ocena zgodności) | project/settings.toml | — |
| Rejestr korekt (WP.04) | records/corrections.md | COR-nn |
| Rekordy weryfikacji (WP.23) | records/verification.md | VER-nn |
| Listy kontrolne przeglądu | process/checklist.md | REQ.n, UC.n … |
| Role i karty sesji | process/roles/ | — |
| Rekordy walidacji (WP.22) | records/validation.md | VAL-nn |
| Rekordy akceptacji (WP.01) | records/acceptance.md | ACC-nn |
| Zasady projektowe | spec/principles.md | DP-nn |
| Słownik pojęć | spec/glossary.md | G-GRP-nn |
| Terminy normy | process/terms.md | — |
| Scenki użytkownika | spec/scenarios.md | SC-nn |
| Zakres In/Out, aktorzy i cele | spec/scope.md | IO-nn |
| Przypadki użycia | spec/use-cases.md | UC-nn |
| Wymagania EARS (typ REQ) | spec/requirements.md | ABC-nn: trzy litery obszaru, np. CAP-nn |
| Testy akceptacyjne | spec/tests/*.feature | AT-nn |
| Macierz śladu, generowana (WP.21) | reports/trace.md | — |
| Zgodność z ISO/IEC 29110, generowana | reports/iso-map.html | — |
| Raport testów, generowany (WP.20) | reports/test-report.md | — |
| Moduły opcjonalne | kod w process/modules/, dane w spec/ (`init.py --module`) | E-nn, RSK-nn |

P-02 ID są niezmienne i nigdy nie są używane ponownie. Schematy ID, pola rodziców, reguły pokrycia, stany i odpowiedniki w ISO/IEC 29110 są tylko w process/tools/id.toml (model śledzalności); ten plik do niego odsyła.

## Ślad
P-03 Dziecko podaje tylko rodzica (pola z id.toml, np. `source:`, `scenarios:`, `verifies:`). Nigdzie nie wypisuje się dzieci. Jedyny wyjątek: zadanie planu wskazuje w `produces:`, co wytwarza (szablon D-09).
P-04 Macierz w obie strony generuje process/tools/trace.py do reports/trace.md, rekord postępu process/tools/progress.py do reports/progress.md, a stronę zgodności z normą process/tools/iso_map.py do reports/iso-map.html (z id.toml, process/tools/iso29110.toml i project/settings.toml); nie edytuje się ich ręcznie.
P-05 Pre-commit sprawdza zawartość przygotowaną do commita (indeks), nie katalog roboczy (szablon D-69), i odrzuca: błędy E1–E9, nieaktualny reports/trace.md, reports/progress.md lub reports/iso-map.html oraz, gdy wdrożono moduł nawigacji, łamanie jego reguł i nieaktualną mapę. Ostrzeżenia W1–W5 nie blokują. `make check` sprawdza dodatkowo odwołania do ścieżek (check_refs.py, szablon D-61) i przeciek dziedziny do process/ (check_leak.py, szablon D-62); wyjątki są w project/check_refs.allow i project/check_leak.allow, każdy z powodem.

## Stany i gotowość (P-06)
Produkty pracy (typy z `product = true`) mają obowiązkowe pole `status` ze stanami normy (szablon D-11, szablon D-14): `initiated` → `verified` (jest rekord VER z wynikiem `pass` w records/verification.md; bez niego ostrzeżenie W3, szablon D-15) → `approved` (dla wymagań decyzja D-nn projektu, P-08). Decyzje, zadania, ryzyka projektu i rekordy mają własne statusy. Baseline nie jest stanem: wynika z tagu.

Wymaganie: jeden wzorzec EARS · tekst zaczyna się zgodnie ze wzorcem · dokładnie jedno „shall” · podmiotem jest system z project/settings.toml · słowa pisane wielką literą są pojęciami ze słownika · ma źródło · status jest jednym ze stanów produktów pracy. Wszystko to sprawdza trace.py; mierzalność i sens ocenia przegląd.
Przegląd (rekord VER albo VAL) prowadzi się według list z process/checklist.md (szablon D-31): pole `checklist:` wskazuje listy, `failed:` niespełnione punkty. Wymaganie ma opcjonalne pole `quality:`; reports/trace.md pokazuje charakterystyki jakości bez wymagań (szablon D-33).
Przypadek użycia: ma rodzica (scenkę w `scenarios:` albo pozycję zakresu In w `scope:`; sprawdza to parent_rules w id.toml), poziom celu i gwarancje.
Kamień milowy i zadanie mogą mieć kryteria odbioru (`acceptance_criteria:`, szablon D-71); reports/progress.md zbiera je w osobnej sekcji (szablon D-73).

## Zmiana
P-07 Każda zmiana: edycja → `git diff` → `make check` → jeden commit na odpowiedź Użytkownika. Opis commita wskazuje co najmniej jedno istniejące ID (hook commit-msg).
P-08 Zatwierdzenie lub zmiana zatwierdzonego wymagania wymaga decyzji D-nn w rejestrze. Ostrzeżenie W5 (szablon D-32) po zmianie mówi, które zweryfikowane elementy straciły ważność weryfikacji, bo zmieniły się one same albo ich rodzic: przejrzyj je i zapisz nowy rekord VER.
P-09 Zamknięty etap = tag `baseline-nn-nazwa` (`make baseline N=…`), wpisany w pole `tag:` kamienia milowego w project/plan.md. Po tagu odśwież reports/progress.md (`make progress`) i dołącz go do następnego commita. Po każdej sesji push do kopii zapasowej (WP.12, szablon D-13); tagi idą razem z nim. Przy każdym kamieniu milowym `make restore-check RECORD=1`: sprawdzenie odtworzenia z kopii zapisane jako rekord VER (PM.02.07, szablon D-35).
P-11 Pakiet procesu zmienia się tylko przez `make process-update V=vX.Y.Z` (szablon D-52). Gdy wydanie zmienia reguły dla istniejących dokumentów, process/MIGRATIONS.md opisuje migrację; jej zakończenie zapisuje decyzja projektu i pole `migrated_to` w project/settings.toml (szablon D-51).

## Role i sesje (szablon D-36, szablon D-37)
Role normy rozkładają się na Użytkownika i sesje agenta; szczegóły, warunki pilota i odłożone pomysły: process/roles/README.md.

| Kto | Role ISO/IEC 29110 | Co robi |
| --- | --- | --- |
| Użytkownik | klient, decyzje kierownika projektu | walidacja (VAL), akceptacja (ACC), zatwierdzanie (decyzje D) |
| sesja autora | analityk, lider techniczny, asystent kierownika, projektant ekranów | specyfikacja, plan, rejestr; według tego pliku |
| sesja weryfikatora | niezależny weryfikator (SI.O7) | rekordy VER i propozycje korekt; według process/roles/verifier.md |

Autor nie weryfikuje sam siebie: commit, który dodaje rekord VER albo VAL z wynikiem pass, nie może zmieniać weryfikowanych elementów (E9, process/tools/check_separation.py).

## Agent
P-10 Bez decyzji Użytkownika agent nie: zmienia znaczenia pojęć, zatwierdza wymagań, usuwa plików, zmienia reguł w id.toml ani plików process/. Może: poprawiać format, dodawać ślad, uruchamiać kontrole, sprzątać blokady gita. Przy założeniu, którego nie może sprawdzić, przedstawia je jako decyzję do potwierdzenia.

## Kolejność wdrażania praktyk
1 umowa, plan, kontrakt, rejestr, baseline · 2 słownik, scenki, zakres · 3 przypadki użycia (brief) · 4 wymagania ze śladem · 5 testy akceptacyjne (potem pokrycie jako błąd) · 6 moduły według potrzeby · 7 suspect links i niezależny przegląd przez osobnego agenta (gdy jest kilkadziesiąt wymagań).

## Świadomie pomijamy
Komisję zmian, formalne plany V&V, CM i QA jako osobne dokumenty, audyty procesu, kwalifikację narzędzi, metryki pokrycia kodu.

## Polecenia
    make hooks       # raz, w nowym klonie (hooki z process/hooks i push z tagami)
    make check       # wszystkie kontrole
    make trace       # odśwież reports/trace.md
    make progress    # odśwież reports/progress.md
    make iso-map     # odśwież reports/iso-map.html
    make navigation  # odśwież mapę (moduł nawigacji)
    make baseline N=01-nazwa
    make restore-check [RECORD=1]  # odtworzenie z kopii: klon origin, HEAD, tagi, ślad
    make test        # test narzędzi procesu (po aktualizacji process/)
    make test-report               # raport testów AT z runner: (WP.20, szablon D-60)
    make process-update V=vX.Y.Z   # aktualizacja procesu z kontrolą wyniku (szablon D-52)
    python3 process/tools/init.py [--module navigation|risks]   # start projektu albo wdrożenie modułu
