# iso-template-agent

Szablon procesu do prowadzenia projektu przez człowieka z agentem LLM. Bierze z praktyk projektów regulowanych (ISO/IEC 29110-5-1-2 Basic jako podstawa, do tego DO-178C, ASPICE) mechanizmy, czyli identyfikatory, ślad dwukierunkowy, kontrolę zmian i bramki, a pomija ceremonię dla audytora.

To repozytorium jest warstwą procesu (D-43): rozwija szablon i samo pracuje według niego (D-48). Projekty powstają z niego przez copier i dostają poprawki procesu w kolejnych wydaniach.

## Trzy warstwy

| Warstwa | Gdzie | Co |
| --- | --- | --- |
| proces | to repozytorium: project/, spec/, records/, reports/, reference/, tests/ | rejestr decyzji szablonu, wymagania szablonu i ich testy, plan wydań |
| szablon | template/ (copier.yml) | pakiet process/: reguły, narzędzia, hooki, moduły, wzorce dokumentów |
| projekt | osobne repozytorium, np. gtd2 | process/ z copiera i dokumenty projektu założone przez init.py |

## Nowy projekt

    copier copy --vcs-ref vX.Y.Z https://github.com/m1981/iso-template-agent nowy-projekt
    cd nowy-projekt && git init
    python3 process/tools/init.py
    make hooks
    git add -A && git commit -m "Start projektu (D-01)"

Dalej według README.md projektu (kolejność: umowa, plan, zatwierdzenie i baseline, środowisko, specyfikacja). Aktualizacja procesu w projekcie: `make process-update V=vX.Y.Z` (D-52); migracje dokumentów opisuje template/process/MIGRATIONS.md (D-51).

## Praca nad szablonem

Zasady: AGENTS.md (warstwa procesu) i template/process/AGENTS.md (proces, który dostają projekty).

    make hooks              # raz, w nowym klonie (hooki z template/process/hooks)
    make check              # ślad warstwy procesu, odwołania, przeciek dziedziny
    make test               # test narzędzi procesu
    make test-distribution  # granica dystrybucji: copier na małym i na prawdziwym szablonie
    make golden             # wyjścia narzędzi wobec złotego wzorca
    make test-move          # kryteria odbioru przeniesienia na trzy warstwy
    make test-report        # raport testów akceptacyjnych szablonu (reports/test-report.md)

Wydanie: tag vX.Y.Z na przetestowanym commicie, nigdy na tym samym commicie co tag baseline-nn (D-49); opis zmian w CHANGELOG.md.

Wymagany jest `python3` (3.8+) i `git`; do testów dystrybucji copier w przypiętej wersji (template/process/tools/process_update.py).
