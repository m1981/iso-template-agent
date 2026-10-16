# Weryfikacje

Rekord weryfikacji (ISO/IEC 29110-5-1-2 WP.23, verification record): czy produkt pracy spełnia swoje wymagania i reguły (przegląd, test). Rekord wskazuje sprawdzone elementy w polu `items:` (P-03); trace.md pokazuje, co już ma weryfikację. Rekordów nie poprawia się wstecz: nowy przegląd to nowy rekord.

Hooki sprawdzają ślad przy każdym commicie, ale to nie zastępuje weryfikacji: rekord VER zapisuje przegląd treści, którego skrypt nie zrobi (sens, mierzalność, kompletność). Produkt pracy w stanie `verified` albo `approved` bez rekordu VER z wynikiem `pass` daje ostrzeżenie W3. Wynik `fail` oczekuje korekty w corrections.md.

Przegląd prowadzi się według list kontrolnych z checklist.md: pole `checklist:` wskazuje użyte listy, a `failed:` niespełnione punkty (wynik `pass` nie może ich mieć). Rekord sprawdzenia kopii zapasowej (`make restore-check RECORD=1`) ma `subject: repository` zamiast `items:`, bo dotyczy repozytorium, a nie elementu.

Format:

```
### VER-nn Przegląd czego
- items: UC-nn, OBS-nn …
- date: RRRR-MM-DD
- by: Użytkownik | agent (niezależny) | …
- checklist: UC, REQ
- result: pass | fail
- failed: REQ.3 (przy wyniku fail)
- notes: znalezione usterki
```

Brak weryfikacji.
