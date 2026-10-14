# Weryfikacje

Rekord weryfikacji (ISO/IEC 29110-5-1-2 WP.23, verification record): czy produkt pracy spełnia swoje wymagania i reguły (przegląd, test). Rekord wskazuje sprawdzone elementy w polu `items:` (P-03); trace.md pokazuje, co już ma weryfikację. Rekordów nie poprawia się wstecz: nowy przegląd to nowy rekord.

Hooki sprawdzają ślad przy każdym commicie, ale to nie zastępuje weryfikacji: rekord VER zapisuje przegląd treści, którego skrypt nie zrobi (sens, mierzalność, kompletność). Produkt pracy w stanie `verified` albo `approved` bez rekordu VER z wynikiem `pass` daje ostrzeżenie W3 (D-15). Wynik `fail` oczekuje korekty w corrections.md.

Format:

```
### VER-nn Przegląd czego
- items: UC-nn, OBS-nn …
- date: RRRR-MM-DD
- by: Użytkownik | agent (niezależny) | …
- result: pass | fail
- notes: znalezione usterki
```

Brak weryfikacji.
