# iso-template-agent

Szablon procesu do prowadzenia projektu przez człowieka z agentem LLM. Bierze z praktyk projektów regulowanych (ISO/IEC 29110-5-1-2 Basic jako podstawa, do tego DO-178C, ASPICE) mechanizmy, czyli identyfikatory, ślad dwukierunkowy, kontrolę zmian i bramki, a pomija ceremonię dla audytora.

To repozytorium jest warstwą procesu (D-43): rozwija szablon i samo pracuje według niego (D-48). Projekty powstają z niego przez copier i dostają poprawki procesu w kolejnych wydaniach.

## Zacznij od celu

Repozytorium zawiera także laboratorium: lekcję TextStats, mapy i eksperyment Flowable. Nie są one częścią pakietu dostarczanego przez copier.

| Chcę… | Zacznij tutaj | Następnie |
| --- | --- | --- |
| **Wiedzieć, gdzie jesteśmy i co robić dalej** | [Punkt wznowienia — początek briefu](reference/process-modeling/brief.md#punkt-wznowienia) | [Bieżący plan §8.7](reference/process-modeling/coverage-map.md#87-zalecenia-i-punkt-wznowienia); wyniki i zlecenia w §8.8. Planowana czynność nie oznacza zgody na wykonanie |
| **Rozwijać lub sprawdzić szablon procesu** | [Plan produktu-szablonu](project/plan.md) i [wymagania](spec/requirements.md) | [Kryteria testów](spec/tests/process-kit.feature), odpowiedni kod w template/process/ i polecenia poniżej |
| **Zrozumieć proces i eksperymenty** | [Lekcja L1](reference/process-simulator/README.md) albo [indeks map i eksperymentów](reference/process-map/README.md) | Wybrany przykład i jego ograniczenia; nie wszystkie materiały po kolei |

Szczegółowa [mapa celów i czytania](reference/repository-audit/README.md) oraz [wykaz plików](reference/repository-audit/inventory.tsv) opisują migawkę audytu ca8f336. Bieżący stan pracy odczytuj z punktu wznowienia i planu, nie z datowanego wykazu.

### Co obowiązuje i czego dowodzą raporty

- Agent zaczyna według [AGENTS.md](AGENTS.md). Lokalne odstępstwo komunikacji i delegowania określają D-78 w [decyzjach](project/decisions.md) i [kontrakt współpracy](reference/process-simulator/collaboration.md); D-87 wskazuje punkt wznowienia i plan. Umieszczenie tych dokumentów w reference/ nie odbiera im tej roli. Pakiet template/process/ ma własny zakres.
- [Postęp szablonu](reports/progress.md) dotyczy zadań z project/plan.md, a [raport testów szablonu](reports/test-report.md) — wersji i daty wskazanej w nagłówku. Nie przedstawiają całego laboratorium ani wyników wszystkich produktów.
- Wyniki lekcji są opisane w [L1](reference/process-simulator/README.md), próby Flowable w [raporcie F5](reference/process-map/flowable-trial/f5-report.md), a generatora kart w [jego dowodach](reference/process-map/flowable-trial/evidence/operator-card/README.md). To osobne przedmioty oceny; nie sumuj ich wyników jako jakości całego procesu.
- Analiza, przykład i propozycja nie stają się obowiązkiem lub odbiorem przez sam zapis. Kod i mapy tego repo nie zastępują źródłowej normy.

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
