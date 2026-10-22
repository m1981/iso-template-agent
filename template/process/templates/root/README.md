# Projekt

Uzupełnij: nazwa projektu i jedno zdanie, co powstaje. Produkt, cel i zakres opisuje project/agreement.md.

Projekt prowadzi człowiek z agentem LLM według procesu wzorowanego na ISO/IEC 29110-5-1-2 (profil Basic). Proces jest w katalogu process/: dostarcza go copier z szablonu procesu i w projekcie się go nie edytuje.

## Start

Kolejność według normy: umowa → plan → zatwierdzenie i baseline → środowisko → specyfikacja.

1. Projekt z szablonu: `copier copy --vcs-ref vX.Y.Z <adres szablonu> <katalog>`, potem w katalogu `git init`, `python3 process/tools/init.py` (dokumenty ze wzorców), `make hooks` i pierwszy commit „Start projektu (D-01)”.
2. Umowa: uzupełnij project/agreement.md (produkt, cel, zakres, co dostarczamy, kto akceptuje, wykonalność) i `system` w project/settings.toml.
3. Plan: project/plan.md (cele, kamienie milowe, zadania, ryzyka), wynika z umowy.
4. Zatwierdzenie: decyzja w project/decisions.md, potem `make baseline N=01-umowa`.
5. Środowisko: drugi remote jako kopia zapasowa (`git remote add origin <adres>`, push z tagami), `make restore-check RECORD=1`.
6. Specyfikacja według process/AGENTS.md: słownik, scenki, zakres, przypadki użycia, wymagania, testy.

Wymagany jest `python3` (3.8+) i `git`; copier tylko do założenia i aktualizacji projektu.

## Układ

| Katalog | Co zawiera |
| --- | --- |
| process/ | proces: reguły (process/AGENTS.md), narzędzia, hooki, moduły, wzorce; aktualizuje go `make process-update V=vX.Y.Z` |
| project/ | umowa, plan, rejestr decyzji, ustawienia |
| spec/ | słownik, zasady, scenki, zakres, przypadki użycia, wymagania, testy akceptacyjne |
| records/ | korekty, weryfikacje, walidacje, akceptacje |
| reports/ | macierz śladu, rekord postępu, strona zgodności z normą (generowane) |

## Polecenia

    make check     # wszystkie kontrole
    make test      # test narzędzi procesu
    make hooks     # raz, w nowym klonie
    make process-update V=vX.Y.Z   # nowa wersja procesu
