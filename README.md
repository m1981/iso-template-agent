# ai-sldc-template

Szablon repozytorium do prowadzenia specyfikacji przez człowieka z agentem LLM. Bierze z praktyk projektów regulowanych (DO-178C, ASPICE, ISO 26262) mechanizmy, czyli identyfikatory, ślad dwukierunkowy, kontrolę zmian i bramki, a pomija ceremonię dla audytora.

## Start

1. Skopiuj repozytorium pod nową nazwą i uruchom `make hooks`.
2. W `tools/id.toml` ustaw `system` (podmiot wymagań EARS).
3. Uzupełnij `plan.md`: produkt i zakres, cele, kamienie milowe, zadania.
4. Pracuj według `AGENTS.md`: słownik, scenki, zakres, przypadki użycia, wymagania, testy.
5. Moduły z `modules/` kopiuj do katalogu głównego, gdy projekt ich potrzebuje (instrukcja w każdym module).

Wymagany jest tylko `python3` (3.8+) i `git`; skrypty nie mają zależności.

## Jak działa ślad

`tools/id.toml` opisuje model: rodzaje elementów, ich identyfikatory, pola, w których element wskazuje rodzica, oraz oczekiwane pokrycie. `tools/trace.py` czyta wszystkie artefakty, sprawdza model i generuje `trace.md`, czyli macierz w obie strony. Kierunek w dół nie jest nigdzie zapisany, tylko liczony, więc oba kierunki nie mogą się rozjechać.

Hooki w `.githooks` blokują commit, gdy ślad ma błędy, `trace.md` lub `progress.md` jest nieaktualny albo opis commita nie wskazuje żadnego istniejącego ID.

Część zarządcza jest wzorowana na ISO/IEC 29110-5-1-2 (profil Basic dla małych zespołów): każdy typ elementu w `id.toml` ma pole `iso` z odpowiadającym mu produktem pracy, a `trace.md` pokazuje to mapowanie. Plan (`plan.md`) i rekordy (`corrections.md`, `verification.md`, `validation.md`, `acceptance.md`) mają ID jak specyfikacja, więc `tools/progress.py` generuje z nich rekord postępu (`progress.md`).

Język: nazwy w warstwie maszynowej (kody, pola, stany, pliki) są po angielsku i odpowiadają terminom normy; treść jest po polsku. Tabela tłumaczeń jest w `glossary.md`.

## Pliki

| Plik | Po co |
| --- | --- |
| AGENTS.md | jak pracujemy: ślad, zmiany, rola agenta |
| plan.md | cele, kamienie milowe, zadania, ryzyka projektu |
| progress.md | rekord postępu (generowany) |
| corrections.md, verification.md, validation.md, acceptance.md | rekordy: korekty, weryfikacje, walidacje, akceptacje |
| kontrakt-decyzji.md | jak agent prosi o decyzje i jak czytać odpowiedzi |
| decisions.md | rejestr decyzji i kolejka tematów |
| principles.md, glossary.md | zasady projektowe i pojęcia |
| scenarios.md, scope.md | skąd biorą się cele: opowieści użytkownika, In/Out, aktorzy i cele |
| use-cases.md, requirements.md, tests/ | specyfikacja i kryteria akceptacji |
| trace.md | macierz śladu (generowana) |
| tools/ | model śladu, skrypty i ich test (`make test`) |
| modules/ | nawigacja, ryzyka, model stanów |
