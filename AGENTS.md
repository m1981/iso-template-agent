# AGENTS.md — jak pracujemy

Przeczytaj na start każdej sesji, w tej kolejności: kontrakt-decyzji.md (obowiązuje zawsze), ten plik, plan.md, progress.md, decisions.md.

Ten plik opisuje proces: ślad, zmiany, rolę agenta (ISO/IEC 29110 WP.05 i część WP.10). Co powstaje, po co i kiedy, jest w plan.md (D-08).

Język (D-17): warstwa maszynowa po angielsku (kody ID, nazwy pól, stany, nazwy plików i skryptów, kody błędów), treść i rozmowa po polsku. Tłumaczenie terminów normy: glossary.md, „Terminy procesu”.

Odwołania D-nn w tym pliku, README.md i tools/ wskazują decyzje szablonu; po `make new-project` są w archive/template/decisions.md.

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
| Rekordy walidacji (WP.22) | validation.md | VAL-nn |
| Rekordy akceptacji (WP.01) | acceptance.md | ACC-nn |
| Zasady projektowe | principles.md | DP-nn |
| Słownik pojęć i terminy normy | glossary.md | G-GRP-nn |
| Scenki użytkownika | scenarios.md | SC-nn |
| Zakres In/Out, aktorzy i cele | scope.md | IO-nn |
| Przypadki użycia | use-cases.md | UC-nn |
| Wymagania EARS | requirements.md | OBS-nn |
| Testy akceptacyjne | tests/*.feature | AT-nn |
| Macierz śladu, generowana (WP.21) | trace.md | — |
| Zgodność z ISO/IEC 29110, generowana | iso-map.html | — |
| Moduły opcjonalne | modules/ (kopiowane do katalogu głównego) | E-nn, RSK-nn |

P-02 ID są niezmienne i nigdy nie są używane ponownie. Schematy ID, pola rodziców, reguły pokrycia, stany i odpowiedniki w ISO/IEC 29110 są tylko w tools/id.toml (model śledzalności); ten plik do niego odsyła.

## Ślad
P-03 Dziecko podaje tylko rodzica (pola z id.toml, np. `source:`, `scenarios:`, `verifies:`). Nigdzie nie wypisuje się dzieci. Jedyny wyjątek: zadanie planu wskazuje w `produces:`, co wytwarza (D-09).
P-04 Macierz w obie strony generuje tools/trace.py do trace.md, rekord postępu tools/progress.py do progress.md, a stronę zgodności z normą tools/iso_map.py do iso-map.html (z id.toml i tools/iso29110.toml); nie edytuje się ich ręcznie.
P-05 Pre-commit odrzuca: błędy E1–E8, nieaktualny trace.md, progress.md lub iso-map.html oraz, gdy wdrożono moduł nawigacji, łamanie jego reguł i nieaktualną mapę. Ostrzeżenia nie blokują.

## Stany i gotowość (P-06)
Produkty pracy (typy z `product = true`) mają obowiązkowe pole `status` ze stanami normy (D-11, D-14): `initiated` → `verified` (jest rekord VER z wynikiem `pass` w verification.md; bez niego ostrzeżenie W3, D-15) → `approved` (dla wymagań decyzja D-nn, P-08). Decyzje, zadania, ryzyka projektu i rekordy mają własne statusy. Baseline nie jest stanem: wynika z tagu.

Wymaganie: jeden wzorzec EARS · tekst zaczyna się zgodnie ze wzorcem · dokładnie jedno „shall” · podmiotem jest system · słowa pisane wielką literą są pojęciami ze słownika · ma źródło · status jest jednym ze stanów produktów pracy. Wszystko to sprawdza trace.py; mierzalność i sens ocenia przegląd.
Przypadek użycia: ma rodzica (scenkę albo zakres In), poziom celu i gwarancje.

## Zmiana
P-07 Każda zmiana: edycja → `git diff` → `make check` → jeden commit na odpowiedź Użytkownika. Opis commita wskazuje co najmniej jedno istniejące ID (hook commit-msg).
P-08 Zatwierdzenie lub zmiana zatwierdzonego wymagania wymaga decyzji D-nn w rejestrze.
P-09 Zamknięty etap = tag `baseline-nn-nazwa` (`make baseline N=…`), wpisany w pole `tag:` kamienia milowego w plan.md. Po tagu odśwież progress.md (`make progress`) i dołącz go do następnego commita. Po każdej sesji push na GitHuba (WP.12, D-13); tagi idą razem z nim.

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
    make test        # po każdej zmianie tools/ lub id.toml
