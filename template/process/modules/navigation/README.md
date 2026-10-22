# Moduł: nawigacja

Model ekranów i sterowania w Mermaid oraz kontrole, które pokazują pułapki, miejsca bez następnego kroku i liczbę kliknięć między ekranami. Dla projektów z interfejsem użytkownika.

## Wdrożenie

1. `python3 process/tools/init.py --module navigation`: zakłada `spec/navigation/screens.mmd` (przykładowa mapa) i `spec/navigation/navigation-map.html` ze wzorców. Kod modułu zostaje w `process/modules/navigation/` i należy do pakietu procesu (szablon D-47): projekt go nie edytuje.
2. Zastąp przykładową mapę w `spec/navigation/screens.mmd` własną; dla każdego ekranu dodaj komentarze `%% E-nn realizes: UC-nn` i `%% E-nn status: initiated`.
3. Pary ekranów do pomiaru kliknięć zapisz w mapie komentarzami `%% key-pair: E01 E03 opis`.
4. `make navigation`, potem `make check`.

Od tej chwili typ E z `process/tools/id.toml` jest aktywny: ekrany pojawiają się w reports/trace.md jako dzieci przypadków użycia, a pre-commit sprawdza mapę i aktualność `spec/navigation/navigation-map.html`.

## Reguły

| Reguła | Co sprawdza |
| --- | --- |
| R1 | każdy ekran osiągalny ze Startu (E01) |
| R2 | z każdego ekranu da się wrócić do Startu (brak pułapek) |
| R3 | każdy przepływ bez paska ma wyjście |
| R4 | ekran zakończenia celu ma wezwanie do dalszej pracy |
| R5 | brak miejsc bez kroku naprzód (świadome wyjątki: `%% exception-dp01: Enn (D-nn)`) |
| R6 | liczba kliknięć dla par z `KEY_PAIRS` (informacyjnie) |
| R7 | każdy ekran realizuje przypadek użycia |

R4 i R5 realizują zasadę „prowadzenie do postępu”. Jeśli przyjmujesz ją w projekcie, zapisz ją w `spec/principles.md` z decyzją.
