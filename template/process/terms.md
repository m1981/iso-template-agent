# Terminy procesu (ISO/IEC 29110)

Plik pakietu procesu (szablon D-57): terminy normy i ich odpowiedniki w procesie. Pojęcia dziedziny projektu są w spec/glossary.md projektu.

Nazwy w warstwie maszynowej (kody, pola, stany, pliki) są po angielsku i odpowiadają terminom normy ISO/IEC 29110-5-1-2. Ta tabela jest jedynym miejscem tłumaczenia; treść dokumentów i rozmowa są po polsku.

| Termin normy | Po polsku | U nas |
| --- | --- | --- |
| work product | produkt pracy | typ z `product = true` w process/tools/id.toml |
| initiated · verified · approved | rozpoczęty · zweryfikowany · zatwierdzony | pole `status` produktu pracy |
| project plan (WP.10) | plan projektu | project/plan.md: OBJ, MS, TSK, PRK |
| objective · milestone · task | cel · kamień milowy · zadanie | OBJ-nn · MS-nn · TSK-nn |
| progress status record (WP.09) | rekord postępu | reports/progress.md (generowany) |
| change request (WP.03) | wniosek o zmianę | decyzja D-nn w project/decisions.md |
| correction register (WP.04) | rejestr korekt | records/corrections.md: COR-nn |
| verification record (WP.23) | rekord weryfikacji | records/verification.md: VER-nn |
| verification checklist | lista kontrolna przeglądu | process/checklist.md, pole `checklist:` rekordu |
| repository recovery (PM.02.07) | sprawdzenie odtworzenia z kopii | `make restore-check`, rekord VER z `subject: repository` |
| validation record (WP.22) | rekord walidacji | records/validation.md: VAL-nn |
| acceptance record (WP.01) | rekord akceptacji | records/acceptance.md: ACC-nn |
| traceability record (WP.21) | rekord śladu | reports/trace.md (generowany) |
| project repository (WP.11) · backup (WP.12) | repozytorium · kopia zapasowa | git · drugi remote, np. GitHub |
| baseline | linia bazowa | tag `baseline-nn-nazwa` |
| agreement (WP.02) | umowa | project/agreement.md (szablon D-41) |
| requirements specification (WP.13) | specyfikacja wymagań | spec/requirements.md, spec/use-cases.md, spec/glossary.md |
