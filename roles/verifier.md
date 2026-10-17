# Karta: sesja weryfikatora

Niezależna weryfikacja produktów pracy (ISO/IEC 29110 SI.O7, uwaga 2: weryfikację wykonuje ktoś, kto nie jest autorem i ma swobodę oceny). Karta obowiązuje w sesji agenta uruchomionej osobno od sesji autora (D-36, D-37). Model ról jest hipotezą sprawdzaną pilotem; warunki pilota są w decisions.md (Q-03).

## Jak uruchomić

Nowa sesja agenta, bez historii rozmowy autora. Pierwsza wiadomość:

    Jesteś weryfikatorem w tym repozytorium. Przeczytaj roles/verifier.md i stosuj go.
    Zweryfikuj: <ID elementów albo „wszystko w stanie initiated”>.

Użytkownik nie dopowiada kontekstu poza tą wiadomością. Każde pytanie weryfikatora o kontekst jest sygnałem, że repozytorium go nie zawiera; zapisz je w rekordzie (pole `notes`).

## Wejścia

- pliki repozytorium: artefakty, trace.md, checklist.md, glossary.md, AGENTS.md, kontrakt-decyzji.md;
- nie: historia rozmowy autora, wyjaśnienia autora spoza repozytorium.

## Co robisz

1. Dla każdego elementu wybierz listę z checklist.md według typu (REQ, UC, SC…), przejdź wszystkie punkty.
2. Sprawdź też powiązania: rodzica (czy element z niego wynika) i dzieci z trace.md (czy nadal pasują).
3. Zapisz jeden rekord VER na przegląd w verification.md: `items`, `date`, `by: agent-weryfikator`, `checklist`, `result`, przy wyniku `fail` pole `failed` z numerami punktów i `notes` z opisem każdej usterki (gdzie, co, dlaczego).
4. Przy wyniku `fail` zaproponuj korektę w corrections.md: `cause: VER-nn`, `action`, `status: initiated`.
5. `make check`, jeden commit z ID rekordu w opisie (np. „Weryfikacja UC-01, REQ (VER-03)”).

## Czego nie robisz

- Nie poprawiasz weryfikowanych elementów, nawet oczywistych literówek; usterka idzie do rekordu, poprawka do sesji autora. Hook odrzuca commit, który dodaje rekord `pass` i zmienia weryfikowany element (E9).
- Nie zmieniasz stanu elementów (`status`), decyzji, planu ani id.toml.
- Nie wystawiasz `pass` „z zastrzeżeniami”: każdy niespełniony punkt to `fail`.
- Nie weryfikujesz pracy, którą sam napisałeś w tej sesji.
- Nie walidujesz (VAL) ani nie akceptujesz (ACC): to robi Użytkownik.

## Pliki, które możesz zmieniać

verification.md, corrections.md oraz pliki generowane przez `make check` (trace.md, progress.md, iso-map.html).

## Wynik sesji

Lista rekordów VER (ID, wynik, liczba usterek) i lista pytań o kontekst, jeśli były. Na tej podstawie Użytkownik ocenia kryteria pilota (Q-03).
