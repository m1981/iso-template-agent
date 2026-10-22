# Ryzyka produktu

Lekka analiza „co pójdzie źle” (w miejsce HARA/FMEA z projektów regulowanych). Dla każdego przypadku użycia 3–10 scenariuszy: co może się nie udać, jaki jest skutek dla Użytkownika i jak system ma się zachować. Każde ryzyko musi dać co najmniej jedno wymaganie (zwykle wzorzec EARS „unwanted”: If …, then System shall …); brak takiego wymagania to błąd E8.

Wdrożenie: skopiuj ten plik do katalogu głównego (`cp modules/risks/risks.md risks.md`); typ RSK z tools/id.toml staje się aktywny. Ryzyka projektu (termin, zasoby) są w plan.md jako PRK-nn.

Format:

```
### RSK-nn Co może pójść źle
- source: UC-nn
- impact: co traci Użytkownik
- likelihood: low | medium | high
- severity: low | medium | high
- status: initiated
```

Brak ryzyk.
