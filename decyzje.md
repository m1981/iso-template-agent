# Rejestr decyzji

Pamięć projektu między sesjami (kontrakt-decyzji.md). Agent aktualizuje rejestr po każdej odpowiedzi Użytkownika. ID są niezmienne. Artefakty wskazują decyzję w swoich polach (`źródło:`, `ustanawia:`, `zmienione przez:`); rejestr nie wylicza swoich dzieci, robi to slad.md.

Format:

```
### D-nn Tytuł zwykłymi słowami
- status: otwarta | rozstrzygnięta | odłożona
- opcje: A) … · B) …
- propozycja: A
- wybór: A — co dokładnie postanowiono
- data: RRRR-MM-DD

### K-nn Temat w kolejce
- uwagi: skąd się wziął
```

## Otwarte

### D-07 Źródło bazowe dla części zarządczej planu
- status: otwarta
- opcje: A) ISO/IEC 29110, profil Basic (plan projektu dla małych podmiotów) · B) NASA Software Engineering Handbook 5.08 · C) oba: 29110 jako struktura, NASA jako lista kontrolna
- propozycja: C

### D-08 Uzupełnienie AGENTS.md o część zarządczą
- status: otwarta
- opcje: A) dodać cel projektu, kamienie milowe (tagi baseline), ryzyka projektu, walidację z użytkownikiem i definicję dostarczenia, po weryfikacji w źródle · B) zostawić plan techniczny
- propozycja: A

## W kolejce

Brak tematów w kolejce.

## Rozstrzygnięte

### D-06 Model śledzalności szablonu
- status: rozstrzygnięta
- opcje: A) model z uzupełnieniami: scenki, zakres In/Out, zasady wskazują decyzję, ekrany realizują przypadki, sprawdzanie pojęć, hook commit-msg · B) tylko elementy istniejące w gtd2
- wybór: A — zapisany w narzedzia/id.toml i sprawdzany przez narzedzia/slad.py
- data: 2026-10-13

### D-05 Schematy ID w jednym pliku
- status: rozstrzygnięta
- opcje: A) narzedzia/id.toml czytany przez skrypty · B) wzorce wpisane w skrypty
- wybór: A
- data: 2026-10-13

### D-04 Moduły dziedzinowe
- status: rozstrzygnięta
- opcje: A) katalog moduly/ kopiowany w razie potrzeby · B) wszystko w rdzeniu
- wybór: A — nawigacja, ryzyka, model stanów
- data: 2026-10-13

### D-03 Język szablonu
- status: rozstrzygnięta
- opcje: A) polski; wymagania EARS po angielsku; nazwy plików bez polskich znaków · B) całość po angielsku
- wybór: A
- data: 2026-10-13

### D-02 Sposób powstania szablonu
- status: rozstrzygnięta
- opcje: A) nowe repozytorium z uogólnionych plików gtd2 · B) przebudowa gtd2
- wybór: A — repozytorium PycharmProjects/ai-sldc-template; decyzje D-02…D-06 przeniesione z rejestru gtd2 (tam numery 48–52)
- data: 2026-10-13

### D-01 Przyjęcie szablonu człowiek + agent
- status: rozstrzygnięta
- wybór: rdzeń (plan, kontrakt, rejestr, zasady, słownik, zakres, scenki, przypadki użycia, wymagania EARS, testy, macierz śladu), narzędzia i hooki, moduły opcjonalne
- data: 2026-10-13
