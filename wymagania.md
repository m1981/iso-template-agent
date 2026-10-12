# Wymagania (EARS)

Wymagania systemowe w składni EARS, po angielsku, z podmiotem ustawionym w narzedzia/id.toml (`system`). Wymaganie podaje tylko swoje źródło (P-03); pochodne i pokrycie testami pokazuje slad.md. Status `zatwierdzone` wymaga decyzji D-nn (P-08). ID: trzy litery obszaru i numer, np. CAP-nn dla przechwytywania; prefiks RYZ jest zarezerwowany dla ryzyk.

Wzorce EARS i to, co sprawdza slad.py:

| Wzorzec | Początek tekstu | Przykład |
| --- | --- | --- |
| ubiquitous | `System shall` | System shall store every captured Item. |
| event | `When` | When the User submits a capture, System shall persist the Item. |
| state | `While` | While an Item is in the Inbox, System shall display its age. |
| unwanted | `If …, then` | If the device is offline, then System shall store the Item locally. |
| optional | `Where` | Where calendar integration is enabled, System shall … |
| complex | `While … when` | While …, when …, System shall … |

Zawsze dokładnie jedno „shall”, a słowa pisane wielką literą (poza słowami EARS i nazwą systemu) muszą być pojęciami ze słownika (B6). Teksty w cudzysłowie (etykiety ekranu) są pomijane.

Format:

```
### OBS-nn
- wzorzec: event
- tekst: When the User …, System shall …
- źródło: UC-nn, D-nn
- status: draft
- uwagi: opcjonalnie
```

Brak wymagań.
