# Moduł: nawigacja

Model ekranów i sterowania w Mermaid oraz kontrole, które pokazują pułapki, miejsca bez następnego kroku i liczbę kliknięć między ekranami. Dla projektów z interfejsem użytkownika.

## Wdrożenie

1. Skopiuj katalog do katalogu głównego jako `navigation/` (`cp -r modules/navigation navigation`).
2. Zastąp przykładową mapę w `navigation/screens.mmd` własną; dla każdego ekranu dodaj komentarze `%% E-nn realizes: UC-nn` i `%% E-nn status: initiated`.
3. W `navigation/check.py` uzupełnij listę `KLUCZOWE` (pary ekranów do pomiaru kliknięć).
4. `make navigation`, potem `make check`.

Od tej chwili typ E z `tools/id.toml` jest aktywny: ekrany pojawiają się w trace.md jako dzieci przypadków użycia, a pre-commit sprawdza mapę i aktualność `navigation-map.html`.

## Reguły

| Reguła | Co sprawdza |
| --- | --- |
| R1 | każdy ekran osiągalny ze Startu (E01) |
| R2 | z każdego ekranu da się wrócić do Startu (brak pułapek) |
| R3 | każdy przepływ bez paska ma wyjście |
| R4 | ekran zakończenia celu ma wezwanie do dalszej pracy |
| R5 | brak miejsc bez kroku naprzód (świadome wyjątki: `%% exception-dp01: Enn (D-nn)`) |
| R6 | liczba kliknięć dla par z `KLUCZOWE` (informacyjnie) |
| R7 | każdy ekran realizuje przypadek użycia |

R4 i R5 realizują zasadę „prowadzenie do postępu”. Jeśli przyjmujesz ją w projekcie, zapisz ją w `principles.md` z decyzją.
