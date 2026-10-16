# Przypadki użycia

Według Cockburna: najpierw szerokość, potem głębokość. Dla wszystkich celów powstają krótkie opisy (brief), dopiero potem pełne przypadki, jeden po drugim: interesariusze i interesy, warunki wstępne, gwarancje, scenariusz główny (3–9 kroków), warunki rozszerzeń, obsługa rozszerzeń. Teksty używają terminów ze słownika (z ID w nawiasie kwadratowym przy pierwszym użyciu).

Każdy przypadek wskazuje rodzica: scenkę (`scenarios:`) albo pozycję zakresu In (`scope:`). Wymagania pochodne i ekrany pokazuje trace.md; nie wypisuje się ich ręcznie. Pole `form` mówi, jak szczegółowy jest opis (brief albo full); `status` to stan produktu pracy (initiated, verified, approved).

Format:

```
### UC-nn Cel zwykłymi słowami
- level: cloud | kite | sea | fish
- scenarios: SC-nn
- scope: IO-nn
- primary_actor: G-AKT-nn
- form: brief | full
- status: initiated

Krótki opis: 2–6 zdań, co Użytkownik osiąga i kiedy przypadek się kończy.

- minimal_guarantee: co jest prawdą nawet przy porażce.
- success_guarantee: co jest prawdą po sukcesie.
```

Brak przypadków użycia.
