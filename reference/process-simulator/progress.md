# Rejestr postępu symulatora

Aktualizacja: 2026-10-24. Ten plik opisuje rzeczywistą pracę nad symulatorem. Nie jest historią fikcyjnego projektu z lekcji ani generowanym `reports/progress.md` szablonu.

## Stan i punkt wznowienia

Przygotowano propozycję [planu](plan.md), [wykonania technicznego](technical-plan.md) i [pierwszego przyrostu](increment-01.md). Nie ma jeszcze kodu symulatora, uruchomionej lekcji ani wyników Alloy/TLC. Obowiązuje [nowy kontrakt współpracy](collaboration.md) przekazany przez Użytkownika (D-78).

Następny krok: Użytkownik rozstrzyga D-79 (w wiadomości D1), czyli rozpoczęcie I1 wraz z proponowaną granicą zakresu. Po zgodzie agent realizuje S1 i kolejne prace potrzebne do dostarczenia I1; nie prosi ponownie o wybór nazw, struktury i zwykłych szczegółów technicznych. Przy odmowie agent aktualizuje propozycję zgodnie z odpowiedzią. Commit wyłącznie na wyraźne żądanie Użytkownika.

## Etapy

Statusy: `proposed` — propozycja; `in_progress` — praca rozpoczęta; `blocked` — konkretna przeszkoda; `completed` — rezultat i sprawdzenie zapisane. `completed` nie oznacza odbioru Użytkownika. Identyfikatory i warunki zakończenia są w planie; nie kopiujemy ich tutaj.

| Etap | Status | Dowód lub stan wykonania | Przeszkoda |
| --- | --- | --- | --- |
| S0 | completed | Plan, opis techniczny i rejestr zapisane; sprawdzenia dokumentów poniżej. | — |
| S1 | proposed | Nie rozpoczęto. | — |
| S2 | proposed | Nie rozpoczęto. | — |
| S3 | proposed | Nie rozpoczęto. | — |
| S4 | proposed | Nie przeprowadzono próby z operatorem. | — |
| S5 | proposed | Opcjonalny; brak wykazanej potrzeby uruchomienia. | — |

## Historia wykonania i zmian planu

| Data | Etap | Wykonane działanie lub zmiana | Wynik i źródło |
| --- | --- | --- | --- |
| 2026-10-23 | S0 | Utworzono folder i trzy dokumenty. Zaproponowano silnik Python, lokalny interfejs i jeden stan dla widoków. | Pliki w tym katalogu; zlecenie dokumentacji zapisane w D-77. |
| 2026-10-23 | S0 | Uruchomiono `make check`, sprawdzono lokalne linki i domknięcie bloków kodu, wykonano `git diff --check`. | Kod 0; ślad: 243 elementy, 0 błędów, 3 ostrzeżenia. 15 lokalnych linków istnieje, bloki kodu domknięte, diff bez błędów białych znaków. |
| 2026-10-23 | S0 | Utrwalono kontrakt współpracy i przygotowano zakres I1, kryteria oraz zasady wykonania w Pythonie. | collaboration.md, increment-01.md; D-78 obowiązuje, D-79 oczekuje na odpowiedź. Implementacja nie rozpoczęta. |
| 2026-10-23 | S0 | Sprawdzono dokumentację po zapisaniu I1 i kontraktu: `make check`, lokalne linki, domknięcie bloków kodu oraz `git diff --check`. | Kod 0; ślad 245 elementów, 0 błędów, 4 ostrzeżenia (W1: MIG-01/MIG-02, W2: D-77/D-78); 26 lokalnych linków bez błędów. Nie uruchamiano testów nieistniejącego jeszcze symulatora. |
| 2026-10-23 | S0 | Użytkownik zlecił commit zmian agenta (D-80); przygotowano dokumentację do zapisu wraz z wcześniejszymi naprawami i ich dowodami. | Zgoda dotyczy commita, nie realizacji I1. D-79 nadal oczekuje na odpowiedź. |
| 2026-10-24 | S0 | Przed commitem powtórzono regresję zmian narzędzi zapisanych razem z dokumentacją. | `make test`: 67/67; `make test-distribution` z Copierem 9.19.1: 18/18. Pierwszą próbę dystrybucji zakłóciło równoległe dodanie plików do indeksu przez agenta; powtórzenie bez zmian repo przeszło także kontrolę izolacji. To wyniki narzędzi szablonu, nie testy symulatora. |

Nie zmieniamy wcześniejszych wpisów, aby ukryć niepowodzenie lub zmianę kierunku. Dopisujemy nowy wpis z przyczyną. Plan opisuje zamiar, tabela etapów aktualny stan, a log wykonania wyniki i ich ograniczenia.

Ostrzeżenia kontroli dokumentów: istniejące W1 dla MIG-01 i MIG-02 (brak testów AT) oraz W2 dla D-77 (brak dzieci w kontrolowanym śladzie i wzmianki w commitach). Materiały w `reference/` nie tworzą dzieci decyzji w tym śladzie; nie wykonano commita. Kontrola linków została wykonana osobno, ponieważ standardowy check_refs pomija `reference/`. Są to sprawdzenia dokumentacji, nie testy ani odbiór symulatora.

## Dziennik decyzji agenta

Wpisy dotyczą sposobu przygotowania propozycji; nie zastępują zgody na implementację.

| ID i data | Decyzja agenta | Uzasadnienie |
| --- | --- | --- |
| A1, 2026-10-23 | I1 opisuję jako pionowy przekrój lekcji z silnikiem, interfejsem i sprawdzeniem; proponowane ograniczenie zakresu przekazuję w D-79. | Sam silnik nie pozwoli operatorowi ocenić użyteczności edukacyjnej. |
| A2, 2026-10-23 | Utrwalam kontrakt w folderze symulatora, wskazując istniejące dokumenty i ich status. | Kolejna sesja potrzebuje trwałych zasad bez zmiany pakietu rozsyłanego do projektów. |

## Rejestr pytań i dalszych spraw

| Sprawa | Właściciel | Następny krok |
| --- | --- | --- |
| D-79: rozpoczęcie I1 i jego granica | Użytkownik | Odpowiedzieć na D1: pełna lekcja TextStats z błędem i korektą; zmiana wymagania i gałęzie w kolejnym przyroście. |
| Czytelność przykładu TextStats | Agent | Podczas próby S4 zebrać obserwacje operatora; proponować zmianę domeny tylko przy wykazanej przeszkodzie. |
| Kryteria użyteczności edukacyjnej | Agent | Zebrać pierwsze obserwacje i przygotować kryteria do uzgodnienia przed powtórzeniem próby. |
| Zmiana wymagania i alternatywna gałąź | Agent | Zachować zakres pierwszej wersji; po I1 przygotować kolejny przyrost. Odłożenie czeka na D-79. |
| Potrzeba Alloy lub TLC | Agent | Ocenić konkretne interakcje reguł po uruchomieniu lekcji; przygotować eksperyment tylko przy wykazanej potrzebie. |
| D-74 i D-75, poza bieżącym tematem | Użytkownik | Rozstrzygnąć w osobnej rozmowie przy powrocie do przeniesienia szablonu lub kontroli słownika; nie blokują propozycji I1. |

Nie są to otrzymane zgody ani dodatkowe blokady dla już zleconego przygotowania dokumentacji. Otwarte sprawy D-74 i D-75 pozostają w głównym rejestrze i nie zostały rozstrzygnięte tym planem.

## Instrukcja wznowienia dla agenta

1. Przeczytaj instrukcje repozytorium, collaboration.md, ten rejestr, plan, plan techniczny i increment-01.md. Sprawdź D-77, D-78, D-79 oraz późniejsze polecenia Użytkownika. Pierwszeństwo ma aktualny kontrakt Użytkownika; nie przywracaj sprzecznych dawnych zasad komunikacji.
2. Sprawdź stan plików i rzeczywiste dowody ostatniego etapu; nie zakładaj, że kod istnieje dlatego, że jest w proponowanym drzewie.
3. Przed wykonaniem następnego kroku zapisz jego zakres i oczekiwany wynik. Aktualizuj plan, jeśli zmieniły się przesłanki; zachowaj przyczynę zmiany w historii.
4. Po pracy dopisz polecenie, wynik, odnośnik do trwałego logu, ograniczenia sprawdzenia i następny krok. Nie zapisuj `pass` po samym przeglądzie opisu planowanych testów.
5. Oddzielaj dowody działania symulatora od fikcyjnych raportów wyświetlanych w lekcji. Nie twórz rekordów odbioru lub niezależnej weryfikacji w imieniu człowieka.
