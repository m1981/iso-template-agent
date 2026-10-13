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

### D-08 Miejsce części zarządczej planu
- status: otwarta
- opcje: A) osobny plan.md według ISO/IEC 29110 WP.10 (co, po co, kiedy), AGENTS.md zostaje procesem · B) dopisać sekcje do AGENTS.md
- propozycja: A
- uwagi: przeformułowana 2026-10-14 po analizie ISO/IEC 29110-5-1-2 (rozdziały 05, 06, 07, 09)

### D-09 Plan jako elementy śladu
- status: otwarta
- opcje: A) nowe typy w id.toml: CEL-nn, KM-nn (kamień = baseline = tag), ZAD-nn z polem produkuje:, RP-nn (ryzyko projektu); produkuje: jako jawny wyjątek od P-03 · B) plan jako zwykły tekst bez ID
- propozycja: A

### D-10 Generowany rekord postępu
- status: otwarta
- opcje: A) postep.md generowany z planu, repozytorium i tagów (PM.03.01: planowane i rzeczywiste zadania, kamienie, ryzyka) · B) bez rekordu postępu
- propozycja: A

### D-11 Stany produktów pracy
- status: otwarta
- opcje: A) jednolite stany dla wszystkich typów w id.toml, po polsku, wzorowane na 29110 (rozpoczęty, zweryfikowany, zatwierdzony; baseline z tagów) · B) zostać przy statusach per typ
- propozycja: A

## W kolejce

Brak tematów w kolejce.

## Rozstrzygnięte

### D-07 Źródło bazowe dla części zarządczej planu
- status: rozstrzygnięta
- opcje: A) ISO/IEC 29110 profil Basic · B) NASA SWEHB 5.08 · C) oba
- wybór: A — analiza na podstawie repozytorium m1981/iso-29110-5-1 (rozdziały 05, 06, 07, 09)
- data: 2026-10-14

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
