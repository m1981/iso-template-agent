# Przypadki użycia

Według Cockburna: najpierw szerokość, potem głębokość. Dla wszystkich celów powstają krótkie opisy (brief), dopiero potem pełne przypadki, jeden po drugim: interesariusze i interesy, warunki wstępne, gwarancje, scenariusz główny (3–9 kroków), warunki rozszerzeń, obsługa rozszerzeń. Teksty używają terminów ze słownika (z ID w nawiasie kwadratowym przy pierwszym użyciu).

Każdy przypadek wskazuje rodzica: scenkę (`scenki:`) albo pozycję zakresu In (`zakres:`). Wymagania pochodne i ekrany pokazuje slad.md; nie wypisuje się ich ręcznie.

Format:

```
### UC-nn Cel zwykłymi słowami
- poziom: morze | latawiec | ryba
- scenki: SC-nn
- zakres: IO-nn
- aktor główny: G-AKT-nn
- status: brief | pełny

Krótki opis: 2–6 zdań, co Użytkownik osiąga i kiedy przypadek się kończy.

- Gwarancja minimalna: co jest prawdą nawet przy porażce.
- Gwarancja sukcesu: co jest prawdą po sukcesie.
```

Brak przypadków użycia.
