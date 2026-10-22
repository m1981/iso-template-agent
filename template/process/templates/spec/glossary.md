# Słownik pojęć

Pojęcia dziedziny projektu. Terminy procesu i normy (ISO/IEC 29110) są w process/terms.md, w pakiecie procesu; ten plik ich nie powtarza.

Każdy termin ma jedno znaczenie w całej specyfikacji. Termin spoza słownika nie może wystąpić w wymaganiu: process/tools/trace.py sprawdza, czy słowa pisane wielką literą w tekście EARS mają odpowiednik w nawiasie w tytule pojęcia (błąd E6).

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

## Pojęcia

Brak pojęć.
