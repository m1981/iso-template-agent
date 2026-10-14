# AGENTS.md — jak pracujemy

Przeczytaj na start każdej sesji, w tej kolejności: kontrakt-decyzji.md (obowiązuje zawsze), ten plik, plan.md, postep.md, decyzje.md.

Ten plik opisuje proces: ślad, zmiany, rolę agenta (ISO/IEC 29110 WP.05 i część WP.10). Co powstaje, po co i kiedy, jest w plan.md (D-08).

## Artefakty i źródła prawdy
P-01 Repozytorium jest jedynym źródłem prawdy dla wszystkich artefaktów. Kopie w innych narzędziach są widokami albo archiwum.

| Artefakt | Plik | ID |
| --- | --- | --- |
| Kontrakt interakcji człowiek–agent | kontrakt-decyzji.md | — |
| Plan: cele, kamienie milowe, zadania, ryzyka projektu | plan.md | CEL-nn, KM-nn, ZAD-nn, RP-nn |
| Rekord postępu (generowany) | postep.md | — |
| Rejestr decyzji i kolejka tematów | decyzje.md | D-nn, K-nn |
| Rekordy: korekty, weryfikacje, walidacje, akceptacje | rekordy.md | KOR-nn, WER-nn, WAL-nn, AKC-nn |
| Zasady projektowe | zasady.md | ZP-nn |
| Słownik pojęć | slownik.md | G-GRP-nn |
| Scenki użytkownika | scenki.md | SC-nn |
| Zakres In/Out, aktorzy i cele | zakres.md | IO-nn |
| Przypadki użycia | przypadki-uzycia.md | UC-nn |
| Wymagania EARS | wymagania.md | OBS-nn |
| Testy akceptacyjne | testy/*.feature | AT-nn |
| Macierz śladu (generowana) | slad.md | — |
| Moduły opcjonalne | moduly/ (kopiowane do katalogu głównego) | E-nn, RYZ-nn |

P-02 ID są niezmienne i nigdy nie są używane ponownie. Schematy ID, pola rodziców, reguły pokrycia, stany i odpowiedniki w ISO/IEC 29110 są tylko w narzedzia/id.toml (model śledzalności); ten plik do niego odsyła.

## Ślad
P-03 Dziecko podaje tylko rodzica (pola z id.toml, np. `źródło:`, `scenki:`, `weryfikuje:`). Nigdzie nie wypisuje się dzieci. Jedyny wyjątek: zadanie planu wskazuje w `produkuje:`, co wytwarza (D-09).
P-04 Macierz w obie strony generuje narzedzia/slad.py do slad.md, a rekord postępu narzedzia/postep.py do postep.md; nie edytuje się ich ręcznie.
P-05 Pre-commit odrzuca: błędy B1–B8, nieaktualny slad.md lub postep.md oraz, gdy wdrożono moduł nawigacji, łamanie jego reguł i nieaktualną mapę. Ostrzeżenia nie blokują.

## Stany i gotowość (P-06)
Produkty pracy mają wspólne stany (D-11): `rozpoczęty` (także brak pola status) → `zweryfikowany` (jest rekord WER z wynikiem `zgodny` w rekordy.md) → `zatwierdzony` (dla wymagań decyzja D-nn, P-08). Baseline nie jest stanem: wynika z tagu.

Wymaganie: jeden wzorzec EARS · tekst zaczyna się zgodnie ze wzorcem · dokładnie jedno „shall” · podmiotem jest system · słowa pisane wielką literą są pojęciami ze słownika · ma źródło · status jest jednym ze stanów produktów pracy. Wszystko to sprawdza slad.py; mierzalność i sens ocenia przegląd.
Przypadek użycia: ma rodzica (scenkę albo zakres In), poziom celu i gwarancje.

## Zmiana
P-07 Każda zmiana: edycja → `git diff` → `make sprawdz` → jeden commit na odpowiedź Użytkownika. Opis commita wskazuje co najmniej jedno istniejące ID (hook commit-msg).
P-08 Zatwierdzenie lub zmiana zatwierdzonego wymagania wymaga decyzji D-nn w rejestrze.
P-09 Zamknięty etap = tag `baseline-nn-nazwa` (`make baseline N=…`), wpisany w pole `tag:` kamienia milowego w plan.md. Po tagu odśwież postep.md (`make postep`) i dołącz go do następnego commita.

## Agent
P-10 Bez decyzji Użytkownika agent nie: zmienia znaczenia pojęć, zatwierdza wymagań, usuwa plików, zmienia reguł w id.toml. Może: poprawiać format, dodawać ślad, uruchamiać kontrole, sprzątać blokady gita. Przy założeniu, którego nie może sprawdzić, przedstawia je jako decyzję do potwierdzenia.

## Kolejność wdrażania praktyk
1 plan, kontrakt, rejestr, baseline · 2 słownik, scenki, zakres · 3 przypadki użycia (brief) · 4 wymagania ze śladem · 5 testy akceptacyjne (potem pokrycie jako błąd) · 6 moduły według potrzeby · 7 suspect links i niezależny przegląd przez osobnego agenta (gdy jest kilkadziesiąt wymagań).

## Świadomie pomijamy
Komisję zmian, formalne plany V&V, CM i QA jako osobne dokumenty, audyty procesu, kwalifikację narzędzi, metryki pokrycia kodu.

## Polecenia
    make hooki       # raz, w nowym klonie
    make sprawdz     # wszystkie kontrole
    make slad        # odśwież slad.md
    make postep      # odśwież postep.md
    make nawigacja   # odśwież mapę (moduł nawigacji)
    make baseline N=01-nazwa
    make test        # po każdej zmianie narzedzia/ lub id.toml
