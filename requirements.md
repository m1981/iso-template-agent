# Wymagania (EARS)

Wymagania systemowe w składni EARS, po angielsku, z podmiotem ustawionym w tools/id.toml (`system`). Wymaganie podaje tylko swoje źródło (P-03); pochodne i pokrycie testami pokazuje trace.md. Status to jeden ze stanów produktów pracy: `initiated`, `verified` (jest rekord VER z wynikiem `pass`), `approved` (wymaga decyzji D-nn, P-08). ID: trzy litery obszaru i numer, np. CAP-nn dla przechwytywania; prefiksy RSK, PRK, OBJ, TSK, COR, VER, VAL i ACC są zarezerwowane dla innych typów (tools/id.toml).

Wzorce EARS i to, co sprawdza trace.py:

| Wzorzec | Początek tekstu | Przykład |
| --- | --- | --- |
| ubiquitous | `System shall` | System shall store every captured Item. |
| event | `When` | When the User submits a capture, System shall persist the Item. |
| state | `While` | While an Item is in the Inbox, System shall display its age. |
| unwanted | `If …, then` | If the device is offline, then System shall store the Item locally. |
| optional | `Where` | Where calendar integration is enabled, System shall … |
| complex | `While … when` | While …, when …, System shall … |

Zawsze dokładnie jedno „shall”, a słowa pisane wielką literą (poza słowami EARS i nazwą systemu) muszą być pojęciami ze słownika (E6). Teksty w cudzysłowie (etykiety ekranu) są pomijane.

Format:

```
### OBS-nn
- pattern: event
- text: When the User …, System shall …
- source: UC-nn, D-nn
- status: initiated
- notes: opcjonalnie
```

Brak wymagań.
