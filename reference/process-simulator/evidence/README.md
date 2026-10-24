# Dowody wykonania I1 — 2026-10-24

To wyniki rzeczywistych testów **symulatora**. Fikcyjne raporty TextStats w lekcji nie są tymi dowodami. Polecenia poniżej wykonujemy z `reference/process-simulator`, jeśli nie zaznaczono inaczej. Logi i skrypty są w repozytorium; nie wymagają zachowania zawartości katalogu tymczasowego.

## Chronologia TDD

| Cykl | RED — rzeczywiście wykonany | GREEN — rzeczywiście wykonany |
| --- | --- | --- |
| Podstawowe przejścia | [01-core-red.log](01-core-red.log): 4 testy, 4 błędy `NotImplementedError` na zamierzonym szkielecie silnika; kod 1 | [02-core-green.log](02-core-green.log): 4/4; kod 0 |
| Pełna lekcja i odtworzenie | [03-lesson-red.log](03-lesson-red.log): 14 testów, 10 błędów niezaimplementowanych działań; kod 1 | [04-lesson-green.log](04-lesson-green.log): 14/14; kod 0 |
| Transport i widoki | [05b-http-red.log](05b-http-red.log): 21 testów, brak handlerów HTTP (501 zamiast 200/400/409) i projekcji; kod 1 | [06-http-green.log](06-http-green.log): 21/21; kod 0 |
| Granica długości sesji | [07-limit-red.log](07-limit-red.log): brak odmowy 201. kroku; kod 1 | [08-regression-green.log](08-regression-green.log): 23/23, w tym test wspólnego limitu silnika i importu; kod 0 |
| Komunikat po osiągnięciu limitu | [09-ui-limit-red.log](09-ui-limit-red.log): przeglądarka wykryła tekst sugerujący odbiór bez ACC1; kod 1 | [browser-check.log](browser-check.log): granica limitu i pełny przebieg PASS; kod 0 |
| Rozmiar poprawnego eksportu | [07b-size-red.log](07b-size-red.log): poprawna długa sesja odrzucona przez HTTP (400 zamiast 200); kod 1 | [08-regression-green.log](08-regression-green.log): 23/23, w tym odtworzenie długiego zapisu; kod 0 |

Polecenia cykli 01–06: `python3 -B -m unittest discover -s tests -v`. Cykl 07 używał dodatkowo `-p test_engine.py`, 07b `-p test_views_http.py`. Testy dopisywano przed odpowiadającą im implementacją. [05-http-red.log](05-http-red.log) dokumentuje nieudaną próbę HTTP w sandboxie: odmowę otwarcia portu. **Nie jest funkcjonalnym RED transportu.** Ponowienie z dostępem do loopback jest w 05b. Pierwsze wywołanie testu limitu z katalogu głównego miało błąd importu `app`; właściwy RED uzyskano po uruchomieniu z folderu symulatora (07).

Nie zachowujemy kompletnej migawki każdego przejściowego kodu. Oryginalne przebiegi mają powyższe logi. Powtarzalny eksperyment odtwarza pierwszy szkielet i osłabienie konkretnej reguły na świeżej kopii bieżących źródeł:

```sh
python3 -B tools/reproduce-tdd.py
```

- [reproduced-core-red.log](reproduced-core-red.log): odtworzenie początkowego szkicu, 4 błędy, oczekiwany kod 1.
- [mutation-review-red.log](mutation-review-red.log): usunięcie warunku „V1 istnieje przed przygotowaniem testów”; test `test_cannot_test_without_review` wykrywa brak odmowy, oczekiwany kod 1.
- [mutation-review-green.log](mutation-review-green.log): ten sam test na niezmienionej kopii przechodzi, kod 0.

Sukces skryptu oznacza wykrycie mutacji, nie zielony wynik celowo uszkodzonego silnika. To jedna celowana kontrola wyroczni, nie pełny mutation score lub dowód kompletności testów.

## Rzeczywista próba interfejsu

Polecenie: `node tools/browser-check.mjs`. [Skrypt](../tools/browser-check.mjs), [log](browser-check.log), [eksport próbnej sesji](browser-session.json). Sprawdzono Python 3.14.6, Node 25.2.1, Chrome 156.0.8078.48. Osobny serwer loopback i profil Chrome, wyłącznie dane fikcyjne.

Wykonano przez DOM interfejsu, nie przez bezpośrednie ustawienie stanu aplikacji:

- pełny przebieg do demonstracji, w tym zero wykonań po T1–T5, RED i nowa rewizja kodu;
- osobne GREEN jednostkowe i integracyjne;
- historię tylko do odczytu bez przyszłych wyników i eksport kursora;
- błędny import bez podmiany sesji;
- odmowę, korektę instrukcji, drugą demonstrację oraz jawny odbiór **w fabule**;
- wybór wymagania klawiaturą w grafie i kartę WP.13 z ID/rewizją;
- zatrzymanie własnego serwera, uruchomienie nowego i wznowienie eksportu przez UI; identyczny eksport po odtworzeniu;
- osiągnięcie 200 kroków bez decyzji ACC1: brak komunikatu sugerującego odbiór;
- wąski ekran 390 px bez poziomego przewijania całej strony. Graf ma własne przewijanie.

Zrzuty: [start](browser-00-start.png), [RED](browser-06-red.png), [demonstracja](browser-11-demo.png), [odbiór w fabule](browser-15-accepted.png), [wąski ekran](browser-mobile.png). Zrzut demonstracji został dodatkowo obejrzany przez agenta; automat sam nie ocenia jakości nauczania.

Wbudowany `browser:browser` był niedostępny: dwa wywołania zakończyły się `sandbox-state-meta: missing field sandboxPolicy` przed uruchomieniem kodu. Dlatego użyto zainstalowanego Chrome w odrębnym profilu. Nie instalowano zależności. Skrypt ma własny wąski klient protokołu Chrome, służący jedynie tej próbie; nie jest częścią aplikacji ani zamiennikiem ogólnego frameworka testów.

## Regresja szablonu i ograniczenia

Pierwsze `make test` w repo głównym: 66/67, błąd `restore-check` przy ścieżce `/var/folders/.../T`, rozwiązywanej przez macOS także pod `/private/var/folders/.../T`. To znana w tym repo różnica ścieżek w teście kopii. Ponowienie `TMPDIR=/private/tmp make test`: **67/67, kod 0**; [template-regression.log](template-regression.log). Katalog tymczasowy jest odtwarzany przez testy; żadne wejście dowodowe nie jest przechowywane wyłącznie poza repozytorium. Nie zmieniano narzędzia ani szablonu w ramach I1.

Nie wykonywano wdrożenia, operacji CNC, walidacji Kitchen CAD/CAM, niezależnego przeglądu treści ani odbioru rzeczywistego symulatora w imieniu Użytkownika. Zapis odbioru w `browser-session.json` jest fikcyjnym wejściem testowym. Sprawdzenia techniczne pozwalają rozpocząć próbę edukacyjną, nie stwierdzić jej sukcesu.

Próba dodania ostatniego testu uruchomiona z błędnej ścieżki roboczej nie zmieniła skryptu, a wywołanie Chrome w sandboxie nie mogło otworzyć lokalnego portu; [09a-browser-environment.log](09a-browser-environment.log) dokumentuje błąd środowiska, nie RED funkcji. Właściwy test dodano i wykonano następnie poza sandboxem: 09-ui-limit-red. [Zrzut wykrytego błędnego komunikatu](browser-ui-limit-red.png). Końcowy browser-check.log zawiera udany przebieg po poprawce.

`make check` po uzupełnieniu dokumentacji: kod 0; 246 elementów, 0 błędów, 3 ostrzeżenia (W1 MIG-01/MIG-02, W2 D-79 bez wzmianki w commicie). [Log](document-check.log). Ostrzeżenia nie stanowią dowodu wad działania symulatora. Linki w reference/ sprawdzono osobno, bo główny check ich nie obejmuje.

Przy przygotowaniu commita usunięto końcowe białe znaki w document-check.log i pusty końcowy wiersz local-doc-check.log; treści wyników nie zmieniono.
