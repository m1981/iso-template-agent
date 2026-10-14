# Słownik pojęć

Każdy termin ma jedno znaczenie w całej specyfikacji. Termin spoza słownika nie może wystąpić w wymaganiu: tools/trace.py sprawdza, czy słowa pisane wielką literą w tekście EARS mają odpowiednik w nawiasie w tytule pojęcia (błąd E6).

- Definicja ma postać: rodzaj nadrzędny + cecha odróżniająca. Ograniczenia i krotności są częścią definicji.
- Nawias na końcu tytułu to angielska nazwa używana w wymaganiach EARS; synonimy rozdziela średnik.
- Pole `distinct_from` („nie mylić z”) wskazuje pojęcie najbliższe, z którym termin bywa mylony.
- Grupy (trzy litery w ID) dobierasz do dziedziny, np. AKT aktorzy, ELM elementy, OPR operacje.

Format:

```
### G-GRP-nn Nazwa pojęcia (English Name; Synonym)
- definition: rodzaj nadrzędny + cecha odróżniająca
- distinct_from: G-GRP-nn
- changed_by: D-nn
- status: initiated
```

## Terminy zakazane

| Termin zakazany | Dlaczego | Użyj zamiast |
| --- | --- | --- |
| (uzupełnij) | (wieloznaczny, bo…) | (pojęcie ze słownika) |

## Terminy procesu (ISO/IEC 29110)

Nazwy w warstwie maszynowej (kody, pola, stany, pliki) są po angielsku i odpowiadają terminom normy ISO/IEC 29110-5-1-2 (D-17, D-18). Ta tabela jest jedynym miejscem tłumaczenia; treść dokumentów i rozmowa są po polsku.

| Termin normy | Po polsku | U nas |
| --- | --- | --- |
| work product | produkt pracy | typ z `product = true` w tools/id.toml |
| initiated · verified · approved | rozpoczęty · zweryfikowany · zatwierdzony | pole `status` produktu pracy |
| project plan (WP.10) | plan projektu | plan.md: OBJ, MS, TSK, PRK |
| objective · milestone · task | cel · kamień milowy · zadanie | OBJ-nn · MS-nn · TSK-nn |
| progress status record (WP.09) | rekord postępu | progress.md (generowany) |
| change request (WP.03) | wniosek o zmianę | decyzja D-nn w decisions.md |
| correction register (WP.04) | rejestr korekt | corrections.md: COR-nn |
| verification record (WP.23) | rekord weryfikacji | verification.md: VER-nn |
| validation record (WP.22) | rekord walidacji | validation.md: VAL-nn |
| acceptance record (WP.01) | rekord akceptacji | acceptance.md: ACC-nn |
| traceability record (WP.21) | rekord śladu | trace.md (generowany) |
| project repository (WP.11) · backup (WP.12) | repozytorium · kopia zapasowa | git · GitHub (D-13) |
| baseline | linia bazowa | tag `baseline-nn-nazwa` |
| requirements specification (WP.13) | specyfikacja wymagań | requirements.md, use-cases.md, glossary.md |

## Pojęcia

Brak pojęć.
