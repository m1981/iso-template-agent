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

### D-13 Kopia zapasowa repozytorium (ISO/IEC 29110 WP.12)
- status: otwarta
- opcje: A) prywatne repozytorium na GitHubie jako drugi remote, push po każdej sesji i po baseline · B) dysk zewnętrzny albo Time Machine · C) oba
- propozycja: A
- uwagi: dziś repozytorium jest tylko na jednym Macu; agent niczego nie zakłada ani nie wysyła bez tej decyzji

### D-14 Zakres jednolitych stanów
- status: otwarta
- opcje: A) stany z D-11 mają produkty pracy (SC, IO, ZP, G, UC, RYZ, WYM, E, AT); decyzje, zadania, ryzyka projektu i rekordy mają własne statusy; brak pola status = rozpoczęty; pole wymagane tylko w wymaganiach · B) pole status obowiązkowe we wszystkich produktach pracy
- propozycja: A
- uwagi: założenie przyjęte przy wdrażaniu D-11 (narzedzia/id.toml, produkt = true)

### D-15 Stan „zweryfikowany” bez rekordu weryfikacji
- status: otwarta
- opcje: A) ostrzeżenie O3, commit przechodzi · B) błąd blokujący commit
- propozycja: A, dopóki przegląd z rekordem WER nie stanie się zwyczajem
- uwagi: założenie przyjęte przy wdrażaniu D-11 i D-12

### D-16 Układ planu i rekordów
- status: otwarta
- opcje: A) jak wdrożono: cztery rodzaje rekordów w jednym rekordy.md; produkuje: przyjmuje kody typów albo ID; zadanie ma status planowane | w toku | zakończone; kamień osiągnięty = istnieje tag z pola tag:; pre-commit sprawdza aktualność postep.md · B) każdy rodzaj rekordu w osobnym pliku (reszta jak w A)
- propozycja: A
- uwagi: założenia przyjęte przy wdrażaniu D-09, D-10 i D-12

## W kolejce

### K-01 Strona „ISO 29110 a nasz model śladu” po rozszerzeniu
- uwagi: kolory pokrycia na stronie pokazują stan sprzed D-08…D-12; odświeżyć po rozstrzygnięciu D-13…D-16

### K-02 Przeniesienie zmian szablonu do gtd2
- uwagi: gtd2 używa statusu draft; po przeniesieniu 28 wymagań przechodzi na stan rozpoczęty (D-11)

## Rozstrzygnięte

### D-12 Model śladu wobec ISO/IEC 29110: rozszerzyć czy od nowa
- status: rozstrzygnięta
- opcje: A) rozszerzyć · B) zbudować od nowa według listy produktów normy
- wybór: A — pole iso w każdym typie id.toml i tabela mapowania w slad.md; nowe typy KOR (WP.04), WER (WP.23), WAL (WP.22), AKC (WP.01) w rekordy.md; kopia zapasowa (WP.12) osobno: D-13
- data: 2026-10-14

### D-11 Stany produktów pracy
- status: rozstrzygnięta
- opcje: A) jednolite stany wzorowane na 29110 · B) statusy per typ
- wybór: A — rozpoczęty, zweryfikowany, zatwierdzony ([projekt] stany_produktow w id.toml); baseline z tagów; wymagania przechodzą z draft/zatwierdzone na te stany; zakres: D-14
- data: 2026-10-14

### D-10 Generowany rekord postępu
- status: rozstrzygnięta
- opcje: A) postep.md generowany z planu, repozytorium i tagów · B) bez rekordu postępu
- wybór: A — narzedzia/postep.py, make postep; pre-commit sprawdza aktualność
- data: 2026-10-14

### D-09 Plan jako elementy śladu
- status: rozstrzygnięta
- opcje: A) typy CEL, KM, ZAD (produkuje:), RP; produkuje: jako jawny wyjątek od P-03 · B) plan jako zwykły tekst
- wybór: A — typy w id.toml; P-03 w AGENTS.md opisuje wyjątek
- data: 2026-10-14

### D-08 Miejsce części zarządczej planu
- status: rozstrzygnięta
- opcje: A) osobny plan.md według WP.10, AGENTS.md zostaje procesem · B) sekcje w AGENTS.md
- wybór: A — plan.md; sekcja Zakres przeniesiona z AGENTS.md do plan.md
- data: 2026-10-14

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
