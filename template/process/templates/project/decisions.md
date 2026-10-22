# Rejestr decyzji

Pamięć projektu między sesjami (process/kontrakt-decyzji.md). Agent aktualizuje rejestr po każdej odpowiedzi Użytkownika. ID są niezmienne. Artefakty wskazują decyzję w swoich polach (`source:`, `established_by:`, `changed_by:`); rejestr nie wylicza swoich dzieci, robi to reports/trace.md. Treść po polsku, nazwy pól i stanów po angielsku. Pliki procesu powołują się na decyzje szablonu jako „szablon D-nn”; to nie są decyzje tego projektu (ich opis: CHANGELOG.md w repozytorium szablonu).

Format:

```
### D-nn Tytuł zwykłymi słowami
- status: open | resolved | deferred
- options: A) … · B) …
- proposal: A
- choice: A — co dokładnie postanowiono
- date: RRRR-MM-DD

### Q-nn Temat w kolejce
- notes: skąd się wziął
```

## Otwarte

Brak otwartych decyzji.

## W kolejce

Brak tematów w kolejce.

## Rozstrzygnięte

### D-01 Start projektu z szablonu
- status: resolved
- choice: projekt założony z szablonu procesu iso-template-agent{version} (copier copy, process/tools/init.py)
- date: {date}
