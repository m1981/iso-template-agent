# Moduł: nawigacja

Model ekranów i sterowania w Mermaid oraz kontrole, które pokazują pułapki, miejsca bez następnego kroku i liczbę kliknięć między ekranami. Dla projektów z interfejsem użytkownika.

## Wdrożenie

1. Skopiuj katalog do katalogu głównego jako `nawigacja/` (`cp -r moduly/nawigacja nawigacja`).
2. Zastąp przykładową mapę w `nawigacja/ekrany.mmd` własną; dla każdego ekranu dodaj komentarz `%% E-nn realizuje: UC-nn`.
3. W `nawigacja/sprawdz.py` uzupełnij listę `KLUCZOWE` (pary ekranów do pomiaru kliknięć).
4. `make nawigacja`, potem `make sprawdz`.

Od tej chwili typ E z `narzedzia/id.toml` jest aktywny: ekrany pojawiają się w slad.md jako dzieci przypadków użycia, a pre-commit sprawdza mapę i aktualność `mapa-nawigacji.html`.

## Reguły

| Reguła | Co sprawdza |
| --- | --- |
| R1 | każdy ekran osiągalny ze Startu (E01) |
| R2 | z każdego ekranu da się wrócić do Startu (brak pułapek) |
| R3 | każdy przepływ bez paska ma wyjście |
| R4 | ekran zakończenia celu ma wezwanie do dalszej pracy |
| R5 | brak miejsc bez kroku naprzód (świadome wyjątki: `%% wyjatek-zp01: Enn (D-nn)`) |
| R6 | liczba kliknięć dla par z `KLUCZOWE` (informacyjnie) |
| R7 | każdy ekran realizuje przypadek użycia |

R4 i R5 realizują zasadę „prowadzenie do postępu”. Jeśli przyjmujesz ją w projekcie, zapisz ją w `zasady.md` z decyzją.
