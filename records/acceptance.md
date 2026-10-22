# Akceptacje

Rekord akceptacji (ISO/IEC 29110-5-1-2 WP.01, acceptance record): przyjęcie dostarczonego kamienia milowego przez odbiorcę. Rekord wskazuje kamień w polu `milestone:` (P-03); progress.md pokazuje akceptację przy kamieniu. Wynik `rejected` oczekuje korekty w corrections.md.

Format:

```
### ACC-nn Akceptacja czego
- milestone: MS-nn
- date: RRRR-MM-DD
- by: odbiorca
- result: accepted | rejected
- open_issues: opcjonalnie
```

Brak akceptacji.
