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
- quality: functional | performance | compatibility | usability | reliability | security | maintainability | portability | constraint | legal
- notes: opcjonalnie
```

Pole `quality` przypisuje wymaganie do charakterystyki jakości z ISO/IEC 29110 WP.13 (za ISO/IEC 25010): funkcjonalność, wydajność, zgodność, użyteczność (w tym dostępność), niezawodność, bezpieczeństwo, utrzymywalność, przenośność oraz ograniczenia projektowe i wymogi prawne. Pole jest opcjonalne; trace.md pokazuje, które charakterystyki nie mają jeszcze żadnego wymagania, żeby żadnej nie pominąć przez przeoczenie.

Brak wymagań.
