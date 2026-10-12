# Ryzyka

Lekka analiza „co pójdzie źle” (w miejsce HARA/FMEA z projektów regulowanych). Dla każdego przypadku użycia 3–10 scenariuszy: co może się nie udać, jaki jest skutek dla Użytkownika i jak system ma się zachować. Każde ryzyko musi dać co najmniej jedno wymaganie (zwykle wzorzec EARS „unwanted”: If …, then System shall …); brak takiego wymagania to błąd B8.

Wdrożenie: skopiuj ten plik do katalogu głównego (`cp moduly/ryzyka/ryzyka.md ryzyka.md`); typ RYZ z narzedzia/id.toml staje się aktywny.

Format:

```
### RYZ-nn Co może pójść źle
- źródło: UC-nn
- skutek: co traci Użytkownik
- prawdopodobieństwo: niskie | średnie | wysokie
- dotkliwość: niska | średnia | wysoka
```

Brak ryzyk.
