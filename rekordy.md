# Rekordy

Zapisy tego, co się wydarzyło (D-12), wzorowane na ISO/IEC 29110-5-1-2: korekty (WP.04), weryfikacje (WP.23), walidacje (WP.22) i akceptacje (WP.01). Rekord wskazuje to, czego dotyczy (P-03); slad.md pokazuje, co już ma rekord, a postep.md, co czeka na korektę. Rekordów nie poprawia się wstecz: nowy przegląd to nowy rekord.

Hooki sprawdzają ślad przy każdym commicie, ale to nie zastępuje weryfikacji: rekord WER zapisuje przegląd treści, którego skrypt nie zrobi (sens, mierzalność, kompletność). Produkt pracy w stanie `zweryfikowany` albo `zatwierdzony` bez rekordu WER z wynikiem `zgodny` daje ostrzeżenie O3.

## Weryfikacje
Czy produkt spełnia swoje wymagania i reguły (przegląd, test). Wynik `niezgodny` oczekuje korekty KOR.

```
### WER-nn Przegląd czego
- obiekt: UC-nn, WYM-nn …
- data: RRRR-MM-DD
- kto: Użytkownik | agent (niezależny) | …
- wynik: zgodny | niezgodny
- uwagi: znalezione usterki
```

## Walidacje
Czy produkt służy temu, do czego jest przeznaczony; ocenia Użytkownik albo odbiorca, np. na scenkach.

```
### WAL-nn Walidacja czego
- obiekt: SC-nn, UC-nn …
- data: RRRR-MM-DD
- kto: Użytkownik
- wynik: zgodny | niezgodny
```

## Akceptacje
Przyjęcie dostarczonego kamienia milowego przez odbiorcę. Wynik `odrzucony` oczekuje korekty KOR.

```
### AKC-nn Akceptacja czego
- kamień: KM-nn
- data: RRRR-MM-DD
- kto: odbiorca
- wynik: przyjęty | odrzucony
- otwarte sprawy: opcjonalnie
```

## Korekty
Działania naprawiające odchylenie od planu albo usterkę znalezioną w weryfikacji, walidacji lub akceptacji.

```
### KOR-nn Tytuł problemu
- przyczyna: ZAD-nn, KM-nn, RP-nn, WER-nn, WAL-nn albo AKC-nn
- działanie: co robimy
- kto: kto odpowiada
- otwarto: RRRR-MM-DD
- termin: RRRR-MM-DD
- status: rozpoczęta | zatwierdzona | zakończona
```
