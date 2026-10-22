# AGENTS.md — warstwa procesu (iso-template-agent)

To repozytorium rozwija szablon procesu i samo pracuje według niego (D-48). Proces jest w template/process/AGENTS.md i obowiązuje tutaj w całości, z różnicami opisanymi niżej.

Przeczytaj na start każdej sesji, w tej kolejności: template/process/kontrakt-decyzji.md (obowiązuje zawsze), template/process/AGENTS.md, ten plik, project/plan.md, reports/progress.md, project/decisions.md.

## Różnice wobec projektu

- Pakiet procesu leży w template/process/ (w projekcie: process/). Polecenia make są te same; Makefile ustawia PROC na template/process.
- Wymagania i testy dotyczą samego szablonu (podmiot „Process kit”, spec/requirements.md, spec/tests/process-kit.feature). Pojęcia w spec/glossary.md to pojęcia procesu, więc kontrola przecieku działa bez słownika.
- Rejestr (project/decisions.md) zawiera decyzje szablonu. W plikach pakietu powołujemy się na nie jako „szablon D-nn” (D-56); w dokumentach warstwy procesu zwyczajnie, jako D-nn.
- Przy przeglądzie rejestru stosuj listę TPL z template/process/checklist.md: decyzje dotyczą procesu, nie produktu klienta (D-57, D-62).
- Każda zmiana w template/ zmienia to, co dostaną projekty: `make test` i `make test-distribution` przed commitem; zmiana reguł dla istniejących dokumentów wymaga wpisu w template/process/MIGRATIONS.md (D-51).
- Wydania: tag vX.Y.Z na przetestowanym commicie, wpis w CHANGELOG.md (D-49). Tagi baseline-nn oznaczają etapy pracy nad szablonem.

## Polecenia

    make test-all   # check, test, test-distribution, golden, test-move
