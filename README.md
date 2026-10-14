# ai-sldc-template

Szablon repozytorium do prowadzenia specyfikacji przez człowieka z agentem LLM. Bierze z praktyk projektów regulowanych (DO-178C, ASPICE, ISO 26262) mechanizmy, czyli identyfikatory, ślad dwukierunkowy, kontrolę zmian i bramki, a pomija ceremonię dla audytora.

## Start

1. Skopiuj repozytorium pod nową nazwą i uruchom `make hooki`.
2. W `narzedzia/id.toml` ustaw `system` (podmiot wymagań EARS).
3. Uzupełnij `plan.md`: produkt i zakres, cele, kamienie milowe, zadania.
4. Pracuj według `AGENTS.md`: słownik, scenki, zakres, przypadki użycia, wymagania, testy.
5. Moduły z `moduly/` kopiuj do katalogu głównego, gdy projekt ich potrzebuje (instrukcja w każdym module).

Wymagany jest tylko `python3` (3.8+) i `git`; skrypty nie mają zależności.

## Jak działa ślad

`narzedzia/id.toml` opisuje model: rodzaje elementów, ich identyfikatory, pola, w których element wskazuje rodzica, oraz oczekiwane pokrycie. `narzedzia/slad.py` czyta wszystkie artefakty, sprawdza model i generuje `slad.md`, czyli macierz w obie strony. Kierunek w dół nie jest nigdzie zapisany, tylko liczony, więc oba kierunki nie mogą się rozjechać.

Hooki w `.githooks` blokują commit, gdy ślad ma błędy, `slad.md` jest nieaktualny albo opis commita nie wskazuje żadnego istniejącego ID.

Część zarządcza jest wzorowana na ISO/IEC 29110-5-1-2 (profil Basic dla małych zespołów): każdy typ elementu w `id.toml` ma pole `iso` z odpowiadającym mu produktem pracy, a `slad.md` pokazuje to mapowanie. Plan (`plan.md`) i rekordy (`rekordy.md`) mają ID jak specyfikacja, więc `narzedzia/postep.py` generuje z nich rekord postępu (`postep.md`).

## Pliki

| Plik | Po co |
| --- | --- |
| AGENTS.md | jak pracujemy: ślad, zmiany, rola agenta |
| plan.md | cele, kamienie milowe, zadania, ryzyka projektu |
| postep.md | rekord postępu (generowany) |
| rekordy.md | weryfikacje, walidacje, akceptacje, korekty |
| kontrakt-decyzji.md | jak agent prosi o decyzje i jak czytać odpowiedzi |
| decyzje.md | rejestr decyzji i kolejka tematów |
| zasady.md, slownik.md | zasady projektowe i pojęcia |
| scenki.md, zakres.md | skąd biorą się cele: opowieści użytkownika, In/Out, aktorzy i cele |
| przypadki-uzycia.md, wymagania.md, testy/ | specyfikacja i kryteria akceptacji |
| slad.md | macierz śladu (generowana) |
| narzedzia/ | model śladu, skrypty i ich test (`make test`) |
| moduly/ | nawigacja, ryzyka, model stanów |
