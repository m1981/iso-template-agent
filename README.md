# ai-sldc-template

Szablon repozytorium do prowadzenia specyfikacji przez człowieka z agentem LLM. Bierze z praktyk projektów regulowanych (DO-178C, ASPICE, ISO 26262) mechanizmy, czyli identyfikatory, ślad dwukierunkowy, kontrolę zmian i bramki, a pomija ceremonię dla audytora.

## Start

1. Skopiuj pliki szablonu bez jego historii gita i załóż nowe repozytorium (historia commitów i tagi baseline szablonu nie przechodzą do projektu):

       rsync -a --exclude .git ai-sldc-template/ nowy-projekt/
       cd nowy-projekt && git init && make hooks
       git add -A && git commit -m "Kopia szablonu (D-01)"

2. `make new-project`: rejestr szablonu, `trace.md` i `progress.md` trafiają do `archive/template/`, a nowy rejestr zaczyna się od D-01 „Start projektu”. Polecenie działa tylko w repozytorium gita bez niezacommitowanych zmian. Potem `git add -A && git commit -m "Start projektu (D-01)"` i `git remote add origin <adres>`.
3. W `tools/id.toml` ustaw `system` (podmiot wymagań EARS).
4. Uzupełnij `plan.md`: produkt i zakres, cele, kamienie milowe, zadania.
5. Pracuj według `AGENTS.md`: słownik, scenki, zakres, przypadki użycia, wymagania, testy.
6. Moduły z `modules/` kopiuj do katalogu głównego, gdy projekt ich potrzebuje (instrukcja w każdym module).

Wymagany jest tylko `python3` (3.8+) i `git`; skrypty nie mają zależności.

## Jak działa ślad

`tools/id.toml` opisuje model: rodzaje elementów, ich identyfikatory, pola, w których element wskazuje rodzica, oraz oczekiwane pokrycie. `tools/trace.py` czyta wszystkie artefakty, sprawdza model i generuje `trace.md`, czyli macierz w obie strony. Kierunek w dół nie jest nigdzie zapisany, tylko liczony, więc oba kierunki nie mogą się rozjechać.

Hooki w `.githooks` blokują commit, gdy ślad ma błędy (E1–E8), gdy `trace.md`, `progress.md` lub `iso-map.html` jest nieaktualny, gdy wdrożony moduł nawigacji łamie swoje reguły albo ma nieaktualną mapę, oraz gdy opis commita nie wskazuje żadnego istniejącego ID. Ostrzeżenia (W1–W5) nie blokują; W5 wskazuje zweryfikowane elementy, które zmieniły się same albo przez zmianę rodzica po ostatniej weryfikacji.

Część zarządcza jest wzorowana na ISO/IEC 29110-5-1-2 (profil Basic dla małych zespołów): typy z odpowiednikiem w normie mają w `id.toml` pole `iso` z tym produktem pracy, a `trace.md` pokazuje to mapowanie. Plan (`plan.md`) i rekordy (`corrections.md`, `verification.md`, `validation.md`, `acceptance.md`) mają ID jak specyfikacja, więc `tools/progress.py` generuje z nich rekord postępu (`progress.md`). `tools/iso_map.py` generuje `iso-map.html`: zależności między 23 produktami normy (dane w `tools/iso29110.toml`) i ich pokrycie przez model, z oceną w `id.toml`.

Język: nazwy w warstwie maszynowej (kody, pola, stany, pliki) są po angielsku i odpowiadają terminom normy; treść jest po polsku. Tabela tłumaczeń jest w `glossary.md`.

## Pliki

| Plik | Po co |
| --- | --- |
| AGENTS.md | jak pracujemy: ślad, zmiany, rola agenta |
| plan.md | cele, kamienie milowe, zadania, ryzyka projektu |
| progress.md | rekord postępu (generowany) |
| corrections.md, verification.md, validation.md, acceptance.md | rekordy: korekty, weryfikacje, walidacje, akceptacje |
| checklist.md | listy kontrolne przeglądu (kryteria z normy) |
| kontrakt-decyzji.md | jak agent prosi o decyzje i jak czytać odpowiedzi |
| decisions.md | rejestr decyzji i kolejka tematów |
| principles.md, glossary.md | zasady projektowe i pojęcia |
| scenarios.md, scope.md | skąd biorą się cele: opowieści użytkownika, In/Out, aktorzy i cele |
| use-cases.md, requirements.md, tests/ | specyfikacja i kryteria akceptacji |
| trace.md | macierz śladu (generowana) |
| iso-map.html | zgodność z ISO/IEC 29110 (generowana) |
| tools/ | model śladu, skrypty i ich test (`make test`) |
| modules/ | nawigacja, ryzyka, model stanów |
