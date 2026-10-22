# Mapa ścieżek: przejście na trzy warstwy (D-50, krok 2)

Zatwierdzona (D-54) i wykonana 2026-10-22 (część 8). Plik przeniesiony z doc/ do reference/. Podstawa: D-41 (umowa), D-42 (katalogi według rodzaju dokumentu), D-43 (trzy warstwy, copier), D-44 (kolejność startu), D-47 (copier dostarcza tylko `process/`), D-48 (warstwa procesu sama używa procesu), D-49 (wersje), D-51 (migracje), D-52 i D-53 (bramka).

Stan wyjściowy: commit 01f5c30, 49 śledzonych plików, plus ta mapa (50). Uzupełnienie 2026-10-19 (D-59…D-64): wymagania, testy, plan i raporty warstwy procesu oraz nowe narzędzia; wiersz zakończony „/” obejmuje cały katalog. Tabela w części 3 obejmuje każdy z nich dokładnie raz; sprawdza to polecenie z części 6.

## 1. Trzy warstwy po przeniesieniu

**Repozytorium iso-template-agent (warstwa procesu).** Samo jest projektem według procesu (D-48): ma rejestr, rekordy i raporty, a narzędzia bierze z `template/process/tools/`.

```
README.md  AGENTS.md  CLAUDE.md  Makefile  .gitignore   # dla autora procesu
copier.yml                                              # konfiguracja szablonu
CHANGELOG.md                                            # wydania vX.Y.Z (D-49)
project/decisions.md  project/plan.md  project/settings.toml   # rejestr i plan warstwy procesu
spec/requirements.md  spec/glossary.md  spec/tests/      # wymagania i testy szablonu (D-59, D-60)
records/  reports/  reference/                          # rekordy, raporty generowane, materiały wejściowe (w tym reference/golden/)
tests/test_distribution.py  tests/golden_master.py      # testy warstwy procesu (poza payloadem)
template/                                               # tylko to trafia do projektu
  .copier-answers.process.yml.jinja
  process/                                              # payload copiera (D-47)
```

**Payload `process/` (warstwa szablonu)** aktualizuje copier. W projekcie nikt go nie edytuje; odstępstwa idą do plików projektu.

```
process/
  AGENTS.md  kontrakt-decyzji.md  checklist.md  terms.md   # reguły
  MIGRATIONS.md                                             # migracje dokumentów (D-51)
  process.mk                                                # cele make, wpinane z Makefile projektu
  roles/  hooks/  tools/  modules/
  practices/                                                # zarezerwowane: pakiety praktyk wzorowane na załączniku E (D-68, Q-12)
  templates/                                                # puste wzorce dokumentów projektu
```

**Projekt z szablonu (np. gtd2)** po `copier copy` i `python3 process/tools/init.py`:

```
AGENTS.md  CLAUDE.md  README.md  Makefile  .gitignore   # projektu; powstają ze wzorców raz
.copier-answers.process.yml                             # zapisuje copier, bez ręcznej edycji
process/                                                # copier
project/   agreement.md  plan.md  decisions.md  settings.toml
spec/      glossary.md  principles.md  scenarios.md  scope.md  use-cases.md  requirements.md
           tests/*.feature   [navigation/]  [risks.md]  # moduły, gdy wdrożone
records/   corrections.md  verification.md  validation.md  acceptance.md
reports/   trace.md  progress.md  iso-map.html          # tylko generowane
evidence/                                               # zarezerwowane: wybrane dowody przyrostów i odbioru (D-68, Q-12)
reference/                                              # materiały wejściowe, bez kontroli śladu
```

## 2. Właściciele

| Klasa | Gdzie | Kto zmienia | Jak trafia do projektu |
| --- | --- | --- | --- |
| Reguły, narzędzia, hooki, moduły (kod) | process/ | warstwa procesu | copier copy i update |
| Puste wzorce dokumentów | process/templates/ | warstwa procesu | copier; kopiowane przez init.py, nowe wydanie nie zmienia wcześniejszych kopii |
| Dokumenty projektu | project/, spec/, records/ | projekt | init.py raz, potem tylko projekt; zmiana reguł przez migrację (D-51) |
| Ustawienia projektu | project/settings.toml | projekt | init.py ze wzorca |
| Raporty | reports/ | narzędzia | generowane w projekcie |
| Wpięcie procesu | AGENTS.md, CLAUDE.md, README.md, Makefile, .gitignore w katalogu głównym | projekt | init.py ze wzorca raz; nigdy nie nadpisuje istniejącego |
| Metadane copiera | .copier-answers.process.yml | copier | copier; ręcznie nie edytujemy |
| Materiały wejściowe | reference/ | projekt | ręcznie |

## 3. Plik po pliku

Kolumny: obecna ścieżka → ścieżka w repozytorium iso-template-agent po przeniesieniu → co dostaje projekt.

| Obecnie | W iso-template-agent | W projekcie | Uwagi |
| --- | --- | --- | --- |
| `.githooks/commit-msg` | template/process/hooks/commit-msg | process/hooks/commit-msg | ścieżka do check_commit.py; `core.hooksPath = process/hooks` |
| `.githooks/pre-commit` | template/process/hooks/pre-commit | process/hooks/pre-commit | ścieżki do narzędzi i raportów; navigation/ → spec/navigation/ |
| `.gitignore` | .gitignore (warstwa procesu) i kopia jako template/process/templates/root/.gitignore | .gitignore ze wzorca | |
| `AGENTS.md` | treść procesu → template/process/AGENTS.md; AGENTS.md warstwy procesu nowy, krótki | AGENTS.md ze wzorca: „przeczytaj process/AGENTS.md” + sekcja odstępstw projektu | ścieżki w tabeli artefaktów; zdanie o archive/template/ zmienia się według D-56 |
| `CLAUDE.md` | zostaje (warstwa procesu); kopia jako wzorzec template/process/templates/root/CLAUDE.md | CLAUDE.md ze wzorca | |
| `Makefile` | cele procesu → template/process/process.mk; Makefile warstwy procesu nowy (check, test, test-distribution, release) | Makefile ze wzorca: `include process/process.mk` + cele projektu | process.mk aktualizuje copier, Makefile należy do projektu |
| `README.md` | README warstwy procesu: dla autora procesu; część „Start” → wzorzec | README.md ze wzorca, z kolejnością startu z D-44 | Start: copier copy → init.py → umowa → plan → zatwierdzenie i baseline → środowisko → specyfikacja |
| `acceptance.md` | records/acceptance.md (warstwa procesu) i wzorzec template/process/templates/records/acceptance.md | records/acceptance.md | |
| `checklist.md` | template/process/checklist.md | process/checklist.md | czyta go model.py (ścieżka) |
| `corrections.md` | records/corrections.md i wzorzec | records/corrections.md | |
| `decisions.md` | project/decisions.md: rejestr warstwy procesu, bez zmian treści; nagłówek pustego rejestru z new_project.py → wzorzec template/process/templates/project/decisions.md | project/decisions.md ze wzorca, z D-01 „Start projektu” | numeracja D-nn warstwy procesu ciągnie się dalej (D-54…) |
| `doc/layout-map.md` | reference/layout-map.md | — | ta mapa; po przeniesieniu zapis planu przejścia |
| `doc/PROPOSAL-CONTEXT-AND-PRACTICE-PACKAGES.md` | reference/PROPOSAL-CONTEXT-AND-PRACTICE-PACKAGES.md | — | propozycja Użytkownika z 2026-10-22 (D-66, D-67, Q-12) |
| `doc/sessions/REF-GTD_system_modeling_with_EARS.md` | reference/sessions/REF-GTD_system_modeling_with_EARS.md | — | materiał wejściowy warstwy procesu |
| `glossary.md` | tabela „Terminy procesu (ISO/IEC 29110)” → template/process/terms.md; reszta → wzorzec template/process/templates/spec/glossary.md | spec/glossary.md (pojęcia projektu) | D-57 |
| `iso-map.html` | reports/iso-map.html (generowany w warstwie procesu) | reports/iso-map.html (generowany) | |
| `kontrakt-decyzji.md` | template/process/kontrakt-decyzji.md | process/kontrakt-decyzji.md | |
| `modules/navigation/README.md` | template/process/modules/navigation/README.md | process/modules/navigation/README.md | instrukcja wdrożenia: init.py --module navigation zamiast cp -r |
| `modules/navigation/build.py` | template/process/modules/navigation/build.py | process/modules/navigation/build.py | czyta dane z spec/navigation/ (parametr) |
| `modules/navigation/check.py` | template/process/modules/navigation/check.py | process/modules/navigation/check.py | jak wyżej |
| `modules/navigation/navigation-map.html` | wzorzec template/process/templates/spec/navigation/navigation-map.html | spec/navigation/navigation-map.html (generowany), gdy moduł wdrożony | |
| `modules/navigation/screens.mmd` | wzorzec template/process/templates/spec/navigation/screens.mmd | spec/navigation/screens.mmd, gdy moduł wdrożony | dane projektu; id.toml file = "spec/navigation/screens.mmd" |
| `modules/navigation/template.html` | template/process/modules/navigation/template.html | process/modules/navigation/template.html | szablon strony należy do kodu modułu |
| `modules/risks/risks.md` | wzorzec template/process/templates/spec/risks.md | spec/risks.md, gdy moduł wdrożony | ryzyka produktu (RSK); ryzyka projektu (PRK) są w planie |
| `modules/state-model/README.md` | template/process/modules/state-model/README.md | process/modules/state-model/README.md | |
| `plan.md` | wzorzec template/process/templates/project/plan.md; sekcja „Produkt i zakres” odsyła do agreement.md (D-41) | project/plan.md | |
| `principles.md` | wzorzec template/process/templates/spec/principles.md | spec/principles.md | |
| `progress.md` | reports/progress.md (generowany w warstwie procesu) | reports/progress.md (generowany) | |
| `requirements.md` | wzorzec template/process/templates/spec/requirements.md | spec/requirements.md | |
| `roles/README.md` | template/process/roles/README.md | process/roles/README.md | |
| `roles/verifier.md` | template/process/roles/verifier.md | process/roles/verifier.md | lista plików, które weryfikator może zmieniać: nowe ścieżki |
| `scenarios.md` | wzorzec template/process/templates/spec/scenarios.md | spec/scenarios.md | |
| `scope.md` | wzorzec template/process/templates/spec/scope.md | spec/scope.md | |
| `tests/README.md` | wzorzec template/process/templates/spec/tests/README.md | spec/tests/README.md | testy akceptacyjne to specyfikacja (WP.19) |
| `project/plan.md` | zostaje: plan warstwy procesu (D-63) | — | nowy 2026-10-19; do przeniesienia liczy go make process-kit |
| `reference/golden/` | zostaje: złoty wzorzec (D-61), 31 plików | — | porównanie po przeniesieniu: make golden z --strip katalogów |
| `reports/progress.md` | zostaje: rekord postępu warstwy procesu | — | generowany przez make process-kit; po przeniesieniu przez narzędzia z --root . |
| `reports/test-report.md` | zostaje: raport testów warstwy procesu (WP.20) | — | generowany przez make process-kit TESTS=1 |
| `reports/trace.md` | zostaje: macierz śladu warstwy procesu | — | generowany jak wyżej; dzisiejszy trace.md szablonu znika w jego miejsce |
| `spec/glossary.md` | zostaje: słownik pojęć procesu (D-59) | — | pojęcia procesu, nie produktu (D-57) |
| `spec/requirements.md` | zostaje: wymagania szablonu (D-59) | — |  |
| `spec/tests/process-kit.feature` | zostaje: testy akceptacyjne szablonu (D-60) | — | ścieżki w runner: zmieniają się z tools/ na template/process/tools/ i tests/ |
| `tools/check_leak.py` | template/process/tools/check_leak.py | process/tools/check_leak.py | w projekcie domyślnie sprawdza process/ ze słownikiem spec/glossary.md |
| `tools/check_leak.allow` | wyjątki warstwy procesu w katalogu głównym; wzorzec pusty w template/process/templates/ | project/check_leak.allow | wyjątki należą do projektu, nie do pakietu (D-47) |
| `tools/check_refs.py` | template/process/tools/check_refs.py | process/tools/check_refs.py |  |
| `tools/check_refs.allow` | wyjątki warstwy procesu w katalogu głównym; wzorzec pusty w template/process/templates/ | project/check_refs.allow | jak wyżej |
| `tools/golden_master.py` | tests/golden_master.py | — | narzędzie warstwy procesu |
| `tools/process_kit_view.py` | archive/tools/process_kit_view.py | — | przejściowe (D-64): po przeniesieniu narzędzia czytają warstwę procesu wprost |
| `tools/test_report.py` | template/process/tools/test_report.py | process/tools/test_report.py |  |
| `tools/check_commit.py` | template/process/tools/check_commit.py | process/tools/check_commit.py | |
| `tools/check_separation.py` | template/process/tools/check_separation.py | process/tools/check_separation.py | kopiuje id.toml do migawek: nowe ścieżki + settings.toml |
| `tools/id.toml` | reguły → template/process/tools/id.toml; [project] system i ocena zgodności → wzorzec template/process/templates/project/settings.toml | process/tools/id.toml + project/settings.toml | D-55; ścieżki `file` w typach zmieniają się na project/…, spec/…, records/… |
| `tools/iso29110.toml` | template/process/tools/iso29110.toml | process/tools/iso29110.toml | dane normy |
| `tools/iso_map.py` | template/process/tools/iso_map.py | process/tools/iso_map.py | wynik domyślnie reports/iso-map.html |
| `tools/model.py` | template/process/tools/model.py | process/tools/model.py | korzeń projektu z parametru `--root`, domyślnie dwa poziomy nad tools/; reguły z katalogu narzędzi, ustawienia z project/settings.toml |
| `tools/new_project.py` | D-58 B: przerobiony na template/process/tools/init.py; D-58 A: archive/tools/new_project.py | process/tools/init.py | zakłada dokumenty projektu ze wzorców |
| `tools/process_update.py` | template/process/tools/process_update.py | process/tools/process_update.py | |
| `tools/progress.py` | template/process/tools/progress.py | process/tools/progress.py | wynik domyślnie reports/progress.md |
| `tools/restore_check.py` | template/process/tools/restore_check.py | process/tools/restore_check.py | records/verification.md, ścieżka trace.py |
| `tools/test_distribution.py` | tests/test_distribution.py | — | test warstwy procesu; zamiast małego szablonu sprawdza prawdziwy template/ |
| `tools/test_tools.py` | template/process/tools/test_tools.py | process/tools/test_tools.py | fixture tylko z process/ i wzorców, nie z dokumentów projektu (dziś kopiuje decisions.md i checklist.md z katalogu głównego) |
| `tools/trace.py` | template/process/tools/trace.py | process/tools/trace.py | wynik domyślnie reports/trace.md; W5 kopiuje id.toml i settings.toml do migawek |
| `trace.md` | reports/trace.md (generowany w warstwie procesu) | reports/trace.md (generowany) | |
| `use-cases.md` | wzorzec template/process/templates/spec/use-cases.md | spec/use-cases.md | |
| `validation.md` | records/validation.md i wzorzec | records/validation.md | w warstwie procesu: wyniki pilota (Q-03) |
| `verification.md` | records/verification.md (z VER-01) i wzorzec bez VER-01 | records/verification.md | wzorzec z wersji sprzed VER-01 |

## 4. Nowe pliki

| Plik | Warstwa | Po co |
| --- | --- | --- |
| copier.yml | proces | `_subdirectory: template`, `_answers_file: .copier-answers.process.yml`, `_min_copier_version`; bez `_tasks`, bez `_skip_if_exists` (D-47) |
| CHANGELOG.md | proces | wydania vX.Y.Z: co się zmienia, ręczne kroki, wspierane wersje początkowe |
| template/.copier-answers.process.yml.jinja | szablon | zapis wersji i odpowiedzi |
| template/process/MIGRATIONS.md | szablon | wpisy M-nn: reguła, których dokumentów dotyczy, jak je znaleźć (kody trace.py), kroki, warunek zakończenia (D-51) |
| template/process/tools/init.py | szablon | (D-58) zakłada dokumenty projektu ze wzorców; odmawia przy brudnym drzewie i nigdy nie nadpisuje istniejącego pliku; `--module` wdraża moduł |
| template/process/templates/project/agreement.md | szablon | umowa (WP.02, D-41): produkt i cel, ogólny zakres, co dostarczamy, kto akceptuje, wykonalność; bez nowego typu ID, zatwierdzana decyzją D i objęta pierwszym baseline'em |
| template/process/templates/root/AGENTS.md, CLAUDE.md, README.md, Makefile | szablon | wpięcie procesu w projekt |
| template/process/templates/project/settings.toml | szablon | system, ocena zgodności, `migrated_to` (D-51) |
| project/settings.toml | proces | ustawienia warstwy procesu |
| process/practices/ (zarezerwowany) | szablon | pakiety praktyk: cel, warunki użycia, procedura, dowód, koszt (D-68); treść według Q-12, bez pustych plików do tego czasu |
| evidence/ (zarezerwowany, w projekcie) | projekt | wybrane dowody przyrostów i odbioru (D-68); zakłada go init.py dopiero, gdy pakiet praktyki go potrzebuje |
| reference/ | proces | materiały wejściowe; tu też dokument Użytkownika o copierze, jeśli Użytkownik się zgodzi (kolejka) |

## 5. Zmiany w narzędziach, bez których przeniesienie nie zadziała

1. **model.py:** korzeń projektu przestaje być „katalog nad tools/”. W projekcie są to dwa poziomy wyżej (process/tools → katalog główny), a w warstwie procesu podaje się `--root .`, bo narzędzia leżą w template/process/tools. Reguły czyta z katalogu narzędzi, ustawienia z project/settings.toml, listy kontrolne z process/checklist.md.
2. **Ścieżki `file` w id.toml** dostają katalogi (project/plan.md, spec/requirements.md, records/verification.md, spec/navigation/screens.mmd). To zmiana reguł, więc obejmuje ją D-54.
3. **Raporty** idą domyślnie do reports/: trace.py, progress.py, iso_map.py, hook pre-commit.
4. **check_separation.py i W5 w trace.py** odtwarzają migawki z gita: kopiują reguły i ustawienia z nowych miejsc. W migawce sprzed przeniesienia pliki leżą pod starymi ścieżkami; pierwszy commit po przeniesieniu musi to obsłużyć (jedno przejście pominięte i opisane albo mapa starych ścieżek). Do sprawdzenia testem.
5. **test_tools.py** buduje fixture tylko z process/ i wzorców. Dziś kopiuje decisions.md i checklist.md z katalogu głównego, a w projekcie to byłyby dokumenty projektu.
6. **init.py** zastępuje new_project.py (D-58).
7. **test_distribution.py** sprawdza prawdziwy template/: copy → init.py → make check → commit → update.

## 6. Jak sprawdzić tę mapę

Pokrycie tabeli z części 3 (każdy śledzony plik dokładnie raz):

    python3 - <<'EOF'
    import re, subprocess
    rows = re.findall(r"^\| `([^`]*)`", open("reference/layout-map.md", encoding="utf-8").read(), re.M)
    files = subprocess.run(["git", "ls-files"], capture_output=True, text=True).stdout.split()
    covered = {f: [r for r in rows if f == r or (r.endswith("/") and f.startswith(r))] for f in files}
    print("bez wiersza:", [f for f, r in covered.items() if not r])
    print("w kilku wierszach:", [f for f, r in covered.items() if len(r) > 1])
    print("wiersz bez pliku:", [r for r in rows if not any(f == r or (r.endswith("/") and f.startswith(r)) for f in files)])
    EOF

Po przeniesieniu (osobny commit, `git mv`, bez usuwania):
- `make check` i `make test` w warstwie procesu;
- `make test-distribution` na prawdziwym template/;
- historia każdego pliku przez `git log --follow` sięga sprzed przeniesienia;
- zawartość przeniesionych dokumentów bajt w bajt taka sama (poza zmianami ścieżek opisanymi w części 3).

## 7. Założenia do potwierdzenia

Są w decyzjach D-54…D-58 w project/decisions.md (dziś decisions.md).

## 8. Wykonanie (2026-10-22)

Dwa commity według D-72: najpierw sam `git mv` (56 przeniesień, treść bez zmian), potem zmiany. Kryteria odbioru K-1…K-10 sprawdza `make test-move` (tests/test_move.py: dokładna lista przeniesień, dozwolonych zmian i nowych plików); test napisano przed przeniesieniem, a jego wynik na starym układzie jest w reference/tdd/test_move-red.txt. Tabela w części 3 opisuje stan wejściowy, więc pokrycie z części 6 dotyczy commita sprzed przeniesienia.

Odstępstwa od tabeli i ustalenia z wykonania (do potwierdzenia w rejestrze, D-74):
- `trace.md` i `progress.md` szablonu trafiły do archive/flat-layout/, a nie do reports/, bo tam są już raporty warstwy procesu;
- korzeń projektu narzędzia biorą z PROCESS_ROOT, a bez niej z gita; hooki i process.mk ustawiają PROCESS_ROOT same;
- check_refs.py w projekcie nie sprawdza process/ (pakiet sprawdza repozytorium szablonu); ścieżki z układu projektu w dokumentach warstwy procesu rozwiązuje względem template/ i wzorców;
- wyjątek dla przykładowej mapy nawigacji przeszedł z listy wyjątków do check_leak.py, bo dotyczy każdego projektu;
- pary ekranów do pomiaru kliknięć są w mapie projektu (`%% key-pair:`), nie w check.py pakietu;
- init.py odmawia przy zmianach w śledzonych plikach, a nieśledzone (process/ po copier copy) dopuszcza;
- wzorce dokumentów projektu nie powołują się na decyzje szablonu (wcześniej D-22); pliki pakietu robią to jako „szablon D-nn” (D-56);
- nowa reguła P-11 w process/AGENTS.md: pakiet zmienia się tylko przez make process-update.

