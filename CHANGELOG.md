# Wydania szablonu procesu

Wydanie to nieprzesuwany tag vX.Y.Z na przetestowanym commicie (D-49). Projekty przechodzą na nie przez `make process-update V=vX.Y.Z` (D-52). Pliki procesu powołują się na decyzje szablonu jako „szablon D-nn” (D-56); ich treść jest w project/decisions.md tego repozytorium.

Każdy wpis podaje: co się zmienia w procesie, ręczne kroki w projekcie, migracje dokumentów (template/process/MIGRATIONS.md, D-51) i wspierane wersje początkowe.

## Niewydane

- Układ trzech warstw (D-43, D-54): pakiet procesu w template/ dla copiera; w projekcie process/, project/, spec/, records/, reports/.
- init.py zakłada dokumenty projektu ze wzorców (D-58); umowa project/agreement.md (D-41); ustawienia projektu w project/settings.toml (D-55); terminy normy w process/terms.md (D-57).
- Pre-commit sprawdza zawartość indeksu (D-69); kontrole odwołań i przecieku dziedziny w make check (D-61, D-62); raport testów (D-60); kryteria odbioru zadań (D-71, D-73).
- Wersje początkowe: brak (pierwsze wydanie v1.0.0 po odbiorze, D-63).
