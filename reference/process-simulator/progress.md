# Rejestr postępu symulatora

Aktualizacja: 2026-10-24. Ten plik opisuje rzeczywistą pracę nad symulatorem. Nie jest historią fikcyjnego projektu z lekcji ani generowanym `reports/progress.md` szablonu.

## Stan i punkt wznowienia

Zakres [I1](increment-01.md) zatwierdzono w D-79. Użytkownik następnie zlecił implementację w TDD według opisanych ustaleń technicznych. **I1 jest zaimplementowany i gotowy do próby edukacyjnej:** Python/stdlib, lokalny HTTP, HTML/CSS/JS/SVG, jedna pełna lekcja, karty i ślad rewizji, historia tylko do odczytu, eksport/import. [Uruchomienie](README.md), [dowody](evidence/README.md).

Rzeczywiste wyniki: 23/23 testy symulatora, pełna próba Chrome z restartem serwera, wykryta mutacja reguły oraz 67/67 testów narzędzi szablonu po użyciu kanonicznego TMPDIR. Próba edukacyjna z Użytkownikiem **trwa**: na przesłanym ekranie wykonano uzgodnienie zakresu (krok 1, 7 elementów, 0 wykonań). Odbiór przez Użytkownika **nie został wykonany**. Wyniki TextStats w aplikacji pozostają symulowane. Alloy/TLC i Kitchen CAD/CAM nie były implementowane.

Następny krok: **S4 — Użytkownik** przechodzi lekcję według README; **agent** zbiera jego obserwacje i przygotowuje korekty objaśnień. Nie otwierać ponownie zgody na wykonane I1, nie rozszerzać samodzielnie zakresu o gałęzie lub zmiany wymagań. Decyzje techniczne A3–A10 zapisano niżej. Commit wyłącznie na nowe wyraźne żądanie; poprzednie D-80 wykonano w e63c8da. Obowiązuje [kontrakt](collaboration.md) (D-78).

## Etapy

Statusy: `proposed` — propozycja; `planned` — praca zlecona, nierozpoczęta; `in_progress` — praca rozpoczęta; `blocked` — konkretna przeszkoda; `completed` — rezultat i sprawdzenie zapisane. `completed` nie oznacza odbioru Użytkownika. Identyfikatory i warunki zakończenia są w planie; status wykonania dotyczy zakresu I1.

| Etap | Status | Dowód lub stan wykonania | Przeszkoda |
| --- | --- | --- | --- |
| S0 | completed | Plan, opis techniczny i rejestr zapisane; sprawdzenia dokumentów poniżej. | — |
| S1 | completed | [Kontrakt scenariusza](scenario.md) i dane lekcji; zakres I1, bez zmiany wymagań i gałęzi. | — |
| S2 | completed | [23 testy GREEN](evidence/08-regression-green.log), odtworzenie pierwszego RED i [wykryta mutacja](evidence/mutation-review-red.log). | — |
| S3 | completed | [Próba Chrome](evidence/browser-check.log), graf i karty, historia, korekta, wznowienie po restarcie; zakres I1 bez gałęzi. | — |
| S4 | in_progress | Użytkownik rozpoczął lekcję i pokazał stan po uzgodnieniu zakresu; dalsza próba oraz ocena użyteczności w toku. | — |
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
| 2026-10-24 | S1 | Użytkownik zatwierdził D1/D-79 i polecił najpierw opisać wiedzę techniczną oraz dobór stosu. | Zakres I1 przyjęty; zmiana wymagań i gałęzie pozostają na następny przyrost. |
| 2026-10-24 | S1 | Sprawdzono lokalny Python i dokumentację Python, SVG, Fetch API oraz SimPy; zapisano wybory i ich ograniczenia. | Python 3.14.6; plan techniczny rewizja 2, decyzje agenta A3–A5. Bez instalacji zależności i bez rozpoczęcia kodowania. |
| 2026-10-24 | S1 | Sprawdzono spójność dokumentacji po przyjęciu D-79. | `make check`: kod 0, 246 elementów, 0 błędów, ostrzeżenia W1 dla MIG-01/MIG-02 i W2 dla D-79. 26 lokalnych linków poprawnych; `git diff --check` bez błędów. |

Nie zmieniamy wcześniejszych wpisów, aby ukryć niepowodzenie lub zmianę kierunku. Dopisujemy nowy wpis z przyczyną. Plan opisuje zamiar, tabela etapów aktualny stan, a log wykonania wyniki i ich ograniczenia.

Ostrzeżenia kontroli dokumentów przed commitem: istniejące W1 dla MIG-01 i MIG-02 (brak testów AT) oraz W2 dla nowych decyzji bez dzieci w kontrolowanym śladzie i bez wzmianki w commitach. Materiały w `reference/` nie tworzą dzieci decyzji w tym śladzie. Commit tych materiałów wykonano później jako e63c8da. Kontrola linków była osobna, ponieważ standardowy check_refs pomija `reference/`. Są to sprawdzenia dokumentacji, nie testy ani odbiór symulatora.

## Dziennik decyzji agenta

Wpisy A1–A2 dotyczą przygotowania propozycji. Wpisy A3 i następne opisują dobór środków w zatwierdzonym zakresie D-79; nie zmieniają zakresu ani decyzji Użytkownika.

| ID i data | Decyzja agenta | Uzasadnienie |
| --- | --- | --- |
| A1, 2026-10-23 | I1 opisuję jako pionowy przekrój lekcji z silnikiem, interfejsem i sprawdzeniem; proponowane ograniczenie zakresu przekazuję w D-79. | Sam silnik nie pozwoli operatorowi ocenić użyteczności edukacyjnej. |
| A2, 2026-10-23 | Utrwalam kontrakt w folderze symulatora, wskazując istniejące dokumenty i ich status. | Kolejna sesja potrzebuje trwałych zasad bez zmiany pakietu rozsyłanego do projektów. |
| A3, 2026-10-24 | Silnik jako deterministyczne przejścia na rekordach Python; testy w unittest, scenariusze i zapis w JSON. | I1 bada kolejność i skutki działań, więc nie potrzebuje harmonogramowania czasu, SimPy ani solvera. |
| A4, 2026-10-24 | Lokalny ThreadingHTTPServer z serializacją zmian sesji w adapterze; silnik pozostaje czysty. | Przeglądarka może otwierać wiele połączeń, ale polecenia muszą zmieniać stan atomowo i w ustalonej kolejności. |
| A5, 2026-10-24 | HTML/CSS/JavaScript oraz SVG, jeden stan serwera dla wszystkich widoków. | Jeden ekran, mały graf i eksport sesji uzasadniają prosty stos bez bazy, frameworka frontendowego i dodatkowego procesu budowania. |

## Rejestr pytań i dalszych spraw

| Sprawa | Właściciel | Następny krok |
| --- | --- | --- |
| Próba i odbiór działającego I1 | Użytkownik | Przejść lekcję według README i wskazać, co jest niejasne; wyniki techniczne nie zastępują tej oceny. |
| Czytelność przykładu TextStats | Agent | Podczas próby S4 zebrać obserwacje operatora; proponować zmianę domeny tylko przy wykazanej przeszkodzie. |
| Kryteria użyteczności edukacyjnej | Agent | Zebrać pierwsze obserwacje i przygotować kryteria do uzgodnienia przed powtórzeniem próby. |
| Zmiana wymagania i alternatywna gałąź | Agent | Po próbie I1 zaproponować zakres kolejnego przyrostu, uwzględniając WIT3 opisane przez Użytkownika. Odłożenie przyjęte w D-79; brak zgody na nową implementację. |
| WIT5: praca po odbiorze i następne wydanie | Agent | Po próbie WIT1 zaproponować kontynuację z zachowaniem wcześniejszego odbioru i osobnym wydaniem. Obecny silnik kończy lekcję po ACC1; samo przechowywanie rewizji nie wystarcza. |
| Potrzeba Alloy lub TLC | Agent | Ocenić konkretne interakcje reguł po uruchomieniu lekcji; przygotować eksperyment tylko przy wykazanej potrzebie. |
| D-74 i D-75, poza bieżącym tematem | Użytkownik | Rozstrzygnąć w osobnej rozmowie przy powrocie do przeniesienia szablonu lub kontroli słownika; nie blokują propozycji I1. |

Lista nie ustanawia dodatkowych blokad dla zatwierdzonego I1. Otwarte sprawy D-74 i D-75 pozostają w głównym rejestrze i nie zostały rozstrzygnięte zgodą na symulator.

## Instrukcja wznowienia dla agenta

1. Przeczytaj instrukcje repozytorium, collaboration.md, ten rejestr, plan, plan techniczny i increment-01.md. Sprawdź D-77, D-78, D-79 oraz późniejsze polecenia Użytkownika. Pierwszeństwo ma aktualny kontrakt Użytkownika; nie przywracaj sprzecznych dawnych zasad komunikacji.
2. Sprawdź stan plików i rzeczywiste dowody ostatniego etapu; nie zakładaj, że kod istnieje dlatego, że jest w proponowanym drzewie.
3. Przed wykonaniem następnego kroku zapisz jego zakres i oczekiwany wynik. Aktualizuj plan, jeśli zmieniły się przesłanki; zachowaj przyczynę zmiany w historii.
4. Po pracy dopisz polecenie, wynik, odnośnik do trwałego logu, ograniczenia sprawdzenia i następny krok. Nie zapisuj `pass` po samym przeglądzie opisu planowanych testów.
5. Oddzielaj dowody działania symulatora od fikcyjnych raportów wyświetlanych w lekcji. Nie twórz rekordów odbioru lub niezależnej weryfikacji w imieniu człowieka.

## Realizacja I1 — 2026-10-24

Użytkownik zlecił wykonanie I1 w TDD według stosu. Plan pozostaje istniejący; scenario.md uszczegóławia S1, nie rozszerza zakresu. Aplikacja i jej dowody są w tym folderze; pakiet szablonu i Kitchen CAD/CAM bez zmian.

- A6 (decyzja agenta): model niezmiennych rekordów i jawne polecenia; treści lekcji w JSON. Korekta po odmowie dotyczy objaśnienia instrukcji, w granicach I1. Powód: umożliwia pełną pętlę poprawki bez wprowadzania odłożonej zmiany wymagań.
- A7 (decyzja agenta): jeden stan sesji na lokalny serwer, numer wersji i blokada przy zmianie; przeszłość tylko do odczytu. Powód: dwie karty nie mogą niejawnie nadpisywać działań. To kontrola pomyłek, nie tożsamości lub rzeczywistych zgód.
- A8 (decyzja agenta): graf grupuje elementy według przykładowego pliku; karty pokazują dokładne ID i rewizje, relacje w obu kierunkach. Powód: graf wszystkich rewizji naraz byłby nieczytelny.
- A9 (decyzja agenta): test przeglądarkowy w osobnym Chrome z tymczasowym profilem, bez nowych zależności. Powód: browser:browser / node_repl dwukrotnie zwrócił błąd środowiska „sandbox-state-meta: missing field sandboxPolicy”, zanim wykonał jakiekolwiek polecenie.

Pierwsze cykle: 4 RED → 4 GREEN; 14 testów (10 błędów brakujących funkcji) → 14 GREEN; HTTP i widoki: RED 21 testów → 21 GREEN. Pierwsza próba HTTP w sandboxie nie otworzyła portów (evidence/05-http-red.log); nie jest dowodem funkcjonalnego RED transportu. Ponowienie z dostępem do loopback (evidence/05b-http-red.log) wykazało brak obsługi HTTP (501) i projekcji. Logi 01–06 dotyczą rzeczywistego symulatora, nie symulowanych wyników TextStats.

### Zakończenie wykonania technicznego

2026-10-24: S1–S3 w zakresie I1 zakończone. Testy graniczne ujawniły dwa problemy nowej implementacji: 201. krok tworzył zapis odrzucany przez importer, a długie poprawne opisy przekraczały limit HTTP. Dopisano testy RED przed poprawkami; końcowa regresja 23/23 (evidence/07, 07b, 08). A10 (decyzja agenta, 2026-10-24): wspólny limit 200 poleceń i HTTP do 2 MiB; uzasadnienie: każda sesja dopuszczona przez UI ma dać się wznowić. Nie jest to manifest wejść ani mechanizm rzeczywistych zgód.

Próba Chrome objęła 15 działań (w tym odmowę, korektę i ponowną demonstrację), ślad do konkretnej rewizji, historię, błędny import, klawiaturę grafu, restart własnego serwera i identyczny zapis po wznowieniu. Zrzuty i log w evidence/. Nie korzystano z profilu przeglądarki Użytkownika ani usług zewnętrznych.

Regresja `make test`: pierwsze wykonanie z niekanonicznym TMPDIR miało 1 błąd restore-check; powtórzenie z kanonicznym TMPDIR: 67/67, kod 0 (evidence/template-regression.log). Bez zmiany narzędzi szablonu. Skrypt `tools/reproduce-tdd.py` wykrył celowo usunięty wymóg V1; na niezmienionej kopii ten sam test przeszedł. Instrukcja i granice interpretacji: evidence/README.md.

Otwarte: S4 po stronie Użytkownika, zbieranie obserwacji po stronie agenta. Nie wykonano commita ani pushu. Nie zmieniano `template/`, Kitchen CAD/CAM ani zastanych zmian w repository-evolution/.

Końcowa próba UI ujawniła błędny tekst przy wyczerpaniu limitu: brak dostępnych działań był opisywany jako odbiór. Dodano asercję przeglądarkową przed poprawką; RED w evidence/09-ui-limit-red.log, GREEN w końcowym evidence/browser-check.log. Tekst odbioru jest teraz wyświetlany wyłącznie dla istniejącego ACC1. Przejrzano zrzut demonstracji; zebrane dowody są techniczne, nie zastępują próby edukacyjnej. `make check`: kod 0, 246 elementów, 0 błędów, 3 znane ostrzeżenia; log evidence/document-check.log.

Na koniec sesji uruchomiono aktualny kod pod http://127.0.0.1:8765 (lokalny proces, sesja narzędzia 1280). Poprzedni serwer zatrzymano po sprawdzeniu, że jego zapis nie zawiera żadnych poleceń. Jeśli serwer już nie działa, odtwórz go poleceniem z README; nie zależymy od utrzymania procesu lub katalogu tymczasowego. Stan demonstracyjny do wczytania: evidence/browser-session.json, jawnie fikcyjna sesja testowa; użytkownik może zacząć od pustej lekcji.

### Wyjaśnienie użytkowania i scenariuszy WIT

Użytkownik zapytał o użytkowanie oraz WIT1 (plan → odbiór), WIT5 (zmiana po odbiorze → następne wydanie) i WIT3 (zastąpienie wymagania → wpływ na zależności). Oznaczenia rozumiemy według jego opisów; nie znaleziono ich definicji w przeszukanych reference/, project/ i spec/. Pytanie nie jest zgodą na rozszerzenie I1.

Obecny odpowiednik WIT1 działa dla jednej ustalonej lekcji do odbioru przyrostu. Role są oznaczeniami fabuły, a testy produktu mają ustalone symulowane wyniki. WIT5 nie działa: ACC1 zamyka wszystkie przejścia, brak modelu kolejnego przyrostu i wydania. WIT3 nie działa: są rewizje kodu i dokładne powiązania, ale brak zastępowania wymagania, przepinania zależności i widoku wpływu zmiany. Historyczność dowodu nie oznacza, że dowód potwierdza nowy zakres.

Rekomendacja edukacyjna: najpierw przejść dostępny WIT1, następnie zaproponować WIT5 jako ciąg dalszy, a WIT3 jako sprawdzenie szczególnego rodzaju zmiany. To propozycja dalszej pracy, nie zmiana zatwierdzonej kolejności lub zakresu. Właściciel przygotowania propozycji: agent; następny krok po obserwacjach z I1. Odbiór I1 przez Użytkownika nadal otwarty.

### Zapis zmian w Git i wznowienie lekcji

2026-10-24: Użytkownik polecił sprawdzić zmiany agenta i wykonać commit(y). Zakres zapisu: folder reference/process-simulator/, rozstrzygnięcie D-79 w project/decisions.md oraz wygenerowany reports/trace.md. Jeden spójny commit obejmuje działającą lekcję, testy, dowody i dokumentację; zastane zmiany repository-evolution/ oraz osobny dokument ISO pozostają poza nim. Polecenie nie obejmuje pushu ani odbioru produktu.

Próba z operatorem rozpoczęta: pierwszy ekran — potrzeba N1; drugi — po uzgodnieniu zakresu, krok 1, 7 elementów, 0 wykonań. Nie wnioskujemy ze zrzutu o zrozumieniu pojęć lub odbiorze. Następny krok Użytkownika: kliknąć R1@1 w karcie potrzeby i przeczytać wymaganie; agent objaśnia jego źródła przed przejściem do planowania. WIT5 i WIT3 nadal poza wykonanym I1.
