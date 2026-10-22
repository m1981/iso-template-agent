# Walidacje

Rekord walidacji (ISO/IEC 29110-5-1-2 WP.22, validation record): czy produkt służy temu, do czego jest przeznaczony. Ocenia Użytkownik albo odbiorca, np. przechodząc scenki. Rekord wskazuje ocenione elementy w polu `items:` (P-03). Wynik `fail` oczekuje korekty w corrections.md.

Format:

```
### VAL-nn Walidacja czego
- items: SC-nn, UC-nn …
- date: RRRR-MM-DD
- by: Użytkownik
- checklist: SC, UC (opcjonalnie)
- result: pass | fail
- failed: UC.3 (przy wyniku fail)
- notes: co nie służy celowi
```

Brak walidacji.
