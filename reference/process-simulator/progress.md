# Rejestr postępu symulatora

Aktualizacja: 2026-10-30. Ten plik opisuje rzeczywistą pracę nad symulatorem i późniejsze analizy procesu. Nie jest historią fikcyjnego projektu z lekcji ani generowanym `reports/progress.md` szablonu.

## Stan i punkt wznowienia

**Bieżące zlecenie — D-86:** wykonano [audyt precyzji i duplikacji wymagań](../process-modeling/coverage-map.md#8-audyt-wymagań-i-kryteriów-2026-10-30). Wynik, granice i kolejne działania są w §8; aktualny [punkt wznowienia](../process-modeling/brief.md) wskazuje właścicieli. E3.5 zostało już wykonane w drugim repozytorium. Dalsze akapity tej sekcji zachowują historię kolejnych dostaw i kierunków; ich instrukcje mapowania generatora nie są bieżącym poleceniem. Nie zmieniono REQ/DoD, kodu ani Kitchen, nie wykonano commita.

**Bieżąca dostawa 2026-10-29 — D-84:** [plan](../process-modeling/release-cycle-plan.md) zapisano przed wykonaniem; [kontrakt pełnego cyklu wydań](../process-modeling/release-cycle.md) i [raport](../process-modeling/release-cycle-report.md) gotowe. 36/36 oczekiwań odtworzył osobny R; sześć dodatkowych własnych przebiegów R zgodnych; błąd wyroczni W04 poprawiony, wcześniejsze niepowodzenia zachowane. RC-01–07 spełnione technicznie, odbiór ograniczonego pakietu czeka na U (D-85). Nie zmieniono modelu v0.7 ani generatora, nie zamknięto E3. Następny krok A po odbiorze: mapowanie do generatora istniejącego E3, nie nowe API. Szczegóły i trwałe dowody w raporcie.

**Kontynuacja D-83, 2026-10-29:** na polecenie „commit(y), a następnie Dalej” zapisano wcześniejszy pakiet w `d6f932d` i wykonano [mapę kryteriów, mechanizmów i braków](../process-modeling/coverage-map.md). Pięć WIT i trzy próby diagnostyczne uruchomiono na kopii; trwałe wyniki i odtworzenie w mapie §5. Potwierdzono rozdział modelu symbolicznego, pełnego badania E3 i przyszłego użycia operacyjnego E4/E5. Następny krok agenta: kontrakty pozostałych przejść E3, od pełnego cyklu wydań, bez zmiany reguł. Osiem prób nie jest pełną regresją ani odbiorem. Karta i DoD pozostają propozycją w zakresie rozszerzeń.

**Bieżące zlecenie 2026-10-29 — D-83:** zapisano [kartę pracy](../process-modeling/work-card.md), [brief](../process-modeling/brief.md) i [propozycję DoD](../process-modeling/acceptance.md) wykonywalnego modelu procesu. Odczytano aktualny model i plan `iso-model-state`: istnieją wykonawca v0.7, WIT1–WIT5, wycinki badań TLC oraz zamknięta z ograniczeniami próba vcs-lite (DEC-PRO-016). Nie powtarzano tam testów ani nie zmieniano plików. Następny krok agenta przed implementacją: mapa istniejącego DoD, zachowań i braków; otwarte sprawy oraz decyzje agenta są w briefie. Dokumentacja nie zatwierdza zmian zakresu, nowego API ani kolejnego pilota. Poprzednie analizy poniżej pozostają historią; lekcja L1 nie otrzymała nowych funkcji.

**Ostatnia próba 2026-10-27:** [sprawdzenie karty zmiany wymagania](../process-map/change-card-check.md) na rzeczywistej naprawie TST-02 zakończone. Ponowione na kopii RED: cztery nieudane przypadki; GREEN: 67/67. Karta ujawniła nieustaloną chronologię planu i granicę między wykonaniem, sprawdzeniem a odbiorem. Trzy doprecyzowania pozostają propozycją, bez aktywacji reguł. Użytkownik wyłączył pomiar czasu, wydajności oraz prognozowanie harmonogramu z potrzeb tego procesu. Następny krok agenta: wykorzystać kartę przy najbliższej zatwierdzonej zmianie i ocenić możliwość wznowienia z plików; szczegóły oraz niewiadome w raporcie. Bez commita, zmian produktu lub wdrożenia API.

**Ostatnia analiza 2026-10-26:** [porównanie kontraktów API](../process-map/api-contract-comparison.md) zakończone. Wspólny kierunek architektury, lecz odbiór przyrostu i W04 wydania wymagają mapowania; obsługa nowego negatywnego wyniku przed W04 wymaga doprecyzowania. Właściciel dalszej propozycji: agent. Nie zmieniono obu kontraktów ani iso-model-state i nie wdrażano API.

**Bieżące zlecenie 2026-10-26 zakończone:** opracowano kontrakt jednego odbioru przyrostu przez API i wykonano osobną recenzję. [Kontrakt](../process-map/acceptance-contract.md), [wynik recenzji](../process-map/acceptance-contract-review.md). To analiza granicy operator–agent–system, nie wdrożenie API ani zmiana zakresu Kitchen. Właściciel dalszego objaśnienia: agent; przejść S01/S03, przed propozycją implementacji przygotować Q1–Q4. D-81 pozostaje kierunkiem późniejszego pilota.

Zakres [I1](increment-01.md) zatwierdzono w D-79. Użytkownik następnie zlecił implementację w TDD według opisanych ustaleń technicznych. **I1 jest zaimplementowany i gotowy do próby edukacyjnej:** Python/stdlib, lokalny HTTP, HTML/CSS/JS/SVG, jedna pełna lekcja, karty i ślad rewizji, historia tylko do odczytu, eksport/import. [Uruchomienie](README.md), [dowody](evidence/README.md).

Rzeczywiste wyniki techniczne: 23/23 testy symulatora, próba Chrome i wykryta mutacja reguły; 67/67 testów narzędzi szablonu po użyciu kanonicznego TMPDIR. Użytkownik w rozmowie potwierdził przejście lekcji do odbioru w fabule. To relacja operatora, nie pobrany końcowy zapis sesji ani odbiór rzeczywistego symulatora. Zgłosił potrzebę przetrawienia pojęć, a następnie rozmywanie celu dalszej pracy.

**Aktualny kierunek — D-81:** minimalny proces prowadzenia Kitchen CAD/CAM, rozpoczynający się od [jednostronicowego opisu](../KITCHEN-MINIMAL-PROCESS.md). Opis zapisany; wdrożenia w projekcie kuchennym jeszcze nie wykonano. Następny krok, właściciel **agent**: rozpoznać istniejące moduły, źródła ustaleń i uruchomienia, następnie zaproponować mały przyrost. Nie wybierać funkcji przed rozpoznaniem. WIT5/WIT3 i dalsza rozbudowa symulatora czekają na wykazaną potrzebę. Nie otwierać ponownie zgody na przyjęty kierunek. Commit wyłącznie na nowe wyraźne żądanie; I1 zapisano w 5471272. Obowiązuje [kontrakt](collaboration.md) (D-78).

## Etapy

Statusy: `proposed` — propozycja; `planned` — praca zlecona, nierozpoczęta; `in_progress` — praca rozpoczęta; `blocked` — konkretna przeszkoda; `completed` — rezultat i sprawdzenie zapisane. `completed` nie oznacza odbioru Użytkownika. Identyfikatory i warunki zakończenia są w planie; status wykonania dotyczy zakresu I1.

| Etap | Status | Dowód lub stan wykonania | Przeszkoda |
| --- | --- | --- | --- |
| S0 | completed | Plan, opis techniczny i rejestr zapisane; sprawdzenia dokumentów poniżej. | — |
| S1 | completed | [Kontrakt scenariusza](scenario.md) i dane lekcji; zakres I1, bez zmiany wymagań i gałęzi. | — |
| S2 | completed | [23 testy GREEN](evidence/08-regression-green.log), odtworzenie pierwszego RED i [wykryta mutacja](evidence/mutation-review-red.log). | — |
| S3 | completed | [Próba Chrome](evidence/browser-check.log), graf i karty, historia, korekta, wznowienie po restarcie; zakres I1 bez gałęzi. | — |
| S4 | in_progress | Użytkownik zgłosił przejście do odbioru w fabule; obserwacje: utrata połączenia, obciążenie pojęciami i rozmywanie celu. D-81 kieruje dalszą pracę ku pilotowi procesu. Ocena edukacyjna nie jest formalnie zamknięta. | — |
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
| Odbiór rzeczywistego symulatora | Użytkownik | Wrócić przy zamykaniu oceny narzędzia; odbiór w fabule nie rozstrzyga tej sprawy i nie blokuje D-81. |
| Przeniesienie nauki na codzienną pracę | Agent | Rozpoznać Kitchen CAD/CAM według D-81, wykorzystać istniejące pliki i zaproponować wycinek pilota. |
| Kryteria użyteczności edukacyjnej | Agent | Zebrać pierwsze obserwacje i przygotować kryteria do uzgodnienia przed powtórzeniem próby. |
| Zmiana wymagania i alternatywna gałąź | Agent | Wrócić po wykazaniu potrzeby w pilocie procesu (D-81), uwzględniając WIT3 opisane przez Użytkownika. Odłożenie przyjęte w D-79; brak zgody na nową implementację. |
| WIT5: praca po odbiorze i następne wydanie | Agent | Wrócić przy potrzebie obsługi kolejnego wydania w pilocie (D-81); zachować wcześniejszy odbiór. Obecny silnik kończy lekcję po ACC1; samo przechowywanie rewizji nie wystarcza. |
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

### Incydent podczas próby: „Failed to fetch”

Użytkownik zgłosił brak połączenia. Przy pierwszym sprawdzeniu API nie odpowiadało, a lsof nie pokazał procesu nasłuchującego na 8765. Przyczyny zakończenia poprzedniego procesu nie ustalono. Uruchomiono serwer jako odrębny proces (start_new_session, PID 18668); sprawdzono HTTP 200 strony oraz odpowiedź API. To uruchomienie operacyjne, bez zmiany kodu aplikacji i bez gwarancji automatycznego restartu.

Nowy serwer miał pustą sesję. Odtworzono wyłącznie trzy czynności potwierdzone w rozmowie: scope, plan, design. To rekonstrukcja potwierdzonego fragmentu, nie odzyskanie oryginalnego zapisu. Nie odtworzono review, testów ani odbioru, bo brak potwierdzenia ich wykonania. Plik do ponownego wznowienia: [recovery-2026-10-24.json](evidence/recovery-2026-10-24.json). API po imporcie: krok 3; dostępne „Przejrzyj wymagania i projekt”. Podczas weryfikacji jedno połączenie z sandboxu zostało zablokowane mimo działającego listenera; ponowienie z dostępem do loopback powiodło się.

Następny krok Użytkownika: kliknąć „Odśwież stan” w aplikacji. Agent kontynuuje prowadzenie od przeglądu. Ograniczenie ujawnione w pilocie: zapis wyłącznie w pamięci wymaga eksportu przed utratą procesu. Właściciel propozycji poprawy odporności i komunikatu błędu: agent; przygotować do uzgodnienia po wznowieniu lekcji. Nie wdrożono automatycznego zapisu ani nie rozszerzono zakresu. Bez kolejnego commita.

### D-81 — skupienie na praktycznym procesie

Użytkownik potwierdził odbiór w fabule, następnie zgłosił nadmiar nowych pojęć i rozmywanie celu rozmowy. Przyjął D1: skupić następny etap na minimalnym procesie prowadzenia Kitchen CAD/CAM, zaczynając od jednostronicowego opisu. Decyzja zapisana jako D-81. Nie potraktowano tego jako odbioru symulatora ani wyboru funkcji kuchennej.

Zapisano reference/KITCHEN-MINIMAL-PROCESS.md: dwa widoki (mapa projektu i karta przyrostu), sześć kroków codziennej pracy, odpowiedzialność za decyzje, obsługa zmiany i sposób oceny kosztu procesu. A11 (decyzja agenta, 2026-10-24): zapis obok istniejącego konspektu w reference/, bez zmiany pakietu template/ lub repozytorium Kitchen; uzasadnienie: ustalenia mają poprzedzić dobór istniejących plików i narzędzi po rozpoznaniu. Podane mechanizmy są opisem do pilota, nie deklaracją działającej automatyzacji.

Następny krok agenta: rozpoznanie modułów, kontraktów, testów i sposobu uruchamiania istniejącego Kitchen CAD/CAM, zanim powstanie propozycja konkretnego przyrostu. Nie ustalono jeszcze funkcji pilota. Po stronie Użytkownika pozostają późniejszy wybór zakresu i ocena działającego wyniku; na tym etapie brak nowej decyzji do podjęcia. Bez kolejnego commita.

Kontrola zapisu D-81: `make check` zakończone kodem 0 (247 elementów, 0 błędów, W1 MIG-01/MIG-02 i W2 D-81 bez wzmianki w commicie). Sprawdzono 22 lokalne odnośniki w nowym opisie, README i rejestrze postępu; bez błędów. `git diff --check` bez błędów. To kontrole dokumentacji; nie uruchamiano ponownie testów niezmienionego kodu.

### Ocena mechanicznego wsparcia procesu

2026-10-24: na prośbę Użytkownika porównano przebieg sesji z aktualnym kodem kontroli. [Raport](../PROCESS-MECHANIZATION-REVIEW.md) rozdziela narzędzia szablonu, fikcyjną lekcję i niewdrożony jeszcze proces Kitchen. Uwzględnia utratę stanu lekcji, rozmycie celu, granice W5 i E9 oraz rzeczywiste naprawy TDD. Nowe usprawnienia pozostają propozycjami; bez zmiany kodu, manifestów wejść, mechanizmu zgód ani commita. Następny krok i właściciel pozostają jak w D-81: agent rozpoznaje Kitchen przed wyborem konkretnego przyrostu. Ewentualny automatyczny zapis symulatora pozostaje odłożony do decyzji o dalszym użyciu lekcji.

### Role i kontekst — odczyt RKD oraz iso-model-state

2026-10-25: na prośbę Użytkownika przeszukano Markdown w RKD i iso-model-state, odczytano instrukcje, stan, propozycje i wybrane mechanizmy. [Synteza](../OPERATOR-AGENT-ROLES-AND-CONTEXT.md) oddziela rolę, mandat, kontekst i uprawnienia narzędzi; przedstawia propozycję pracy PM/PO–developer–przegląd–integracja. Wskazuje Q-04–Q-06, istniejące testy zachowania agentów w RKD oraz granice wykonawcy modelu. Bez uruchamiania innych agentów, zmian w zewnętrznych repozytoriach ani aktywowania nowych kart. Właściciel dalszego rozpoznania: agent. Uwzględnić istniejące DEC i przyrost 1 RKD, zanim powstanie propozycja zakresu pilota; nie traktować ich jako nieistniejących ani automatycznie zatwierdzać nowego zakresu.

Uzupełnienie o niezależności: §10 syntezy zawiera dokładne rozróżnienie SI.O7, objaśniającej uwagi 2 i własnej polityki osobnego recenzenta. Wskazano nadinterpretację źródła w kartach szablonu; korekta opisu do przygotowania przez agenta przy pracy nad rolami, bez osłabiania przyjętego rozdziału. Przypomniane doświadczenie Użytkownika z subagentami uwzględniono w propozycji przeglądów ograniczonych zakresem i ryzykiem. Nie uruchamiano subagentów ani nie wdrażano nowych bramek.

### D-82 — wykonana mapa procesu

2026-10-25: Użytkownik zlecił wykonanie rekomendowanej wizualizacji. Powstał [lokalny przewodnik](../process-map/index.html): trzy widoki, legenda M/I/L/P, przebieg z recenzją i jej pominięciem oraz przykład zmiany po przeglądzie. [README mapy](../process-map/README.md) zawiera plan, źródła, decyzje agenta i wyniki kontroli; SVG/PNG odtwarza istniejący Graphviz przez render.py. Sprawdzono obrazy, lokalne odnośniki i widok Chrome dla 1440/390 px. Bez zmian procesu, nowych zależności, commita lub pusha. Następny krok agenta: poprowadzić użytkownika od widoku 1, potem kontynuować D-81. Ocena czytelności przez Użytkownika pozostaje otwarta; nie jest blokadą wykonanego materiału ani nową prośbą o zatwierdzenie procesu.

Kontynuacja edukacyjna: wyjaśniono śledzalność dwukierunkową (WP.21), analogię do zależności systemu budowania oraz różnicę między produktem, zadaniem i wykonaniem. Na pytanie o ERD przygotowano [statyczny model Mermaid](../process-map/static-model.md): rdzeń, kontekst/role i kontrole/decyzje/wydania. To model pojęciowy, nie zmiana schematu ani reguł procesu. Jawnie wskazano propozycje i ograniczenie: brak lokalnego renderera Mermaid; nie instalowano nowych zależności. Następny krok agenta w objaśnieniu: odczytać relację zadanie → wykonanie → ocena i pokazać, gdzie może brakować wyniku przeglądu. Kierunek pilota D-81 pozostaje bez zmian.

2026-10-26: obejrzano sześć diagramów normy z assets/figures i porównano ich znaczenie z §4.2. [Synteza §14](../OPERATOR-AGENT-ROLES-AND-CONTEXT.md) potwierdza możliwość mechanizacji obiegu po doprecyzowaniu reguł i połączeniu z rzeczywistym repozytorium. Odczytano nowy stan iso-model-state: v0.6, scenariusze WIT1–WIT5; wcześniejsze stwierdzenia o v0.4 są historyczne. Testów tamtego repo nie ponawiano, niczego w nim nie zmieniono. Agent powinien uwzględnić istniejący mechanizm wykonania modelu przy dalszej propozycji pilota, bez rozpoczynania drugiego silnika i bez samodzielnej zmiany planu E2–E5.

Na kolejne zlecenie rozpisano [przykład W02](../process-map/worked-transition.md): podstawa SI.O7/WP.23, obecne ready → reviewed, brak wymagania raportu w tej abstrakcji oraz propozycja kontroli rzeczywistego wyniku. Opisano wejścia, odmowę, skutki, zmianę po przeglądzie, trwałość i przyszłe kryteria TDD. W03 jest deklaracją modelu, nie ukończoną obsługą wykonawcy. To dokumentacja, bez zmian modelu i uruchamiania testów lub recenzentów. Następny krok edukacyjny agenta: przeprowadzić użytkownika przez przykład brakującego raportu i porównać obecny model z proponowanym adapterem. Wdrożenie pozostaje poza tym zleceniem.

### Prześledzenie W02 i osobny recenzent — 2026-10-26

Użytkownik zlecił wejście w zaproponowaną rolę inżyniera weryfikacji procesu i wykonanie analizy z osobnym subagentem. [Wynik](../process-map/transition-review.md): tabela warunek–dowód–wynik–luka, instancja zadanie → wykonanie → raport, cztery uwagi recenzenta i ich rozliczenie. Recenzent `/root/review_transition` nie dostał historii rozmowy, analizy autora ani wyników prób przed własną oceną. Zachowano jego odpowiedź i ocenianą wersję dokumentu. Jest to rzeczywisty przegląd opisu edukacyjnego, nie odbiór procesu ani rzeczywistego wydania.

Prowadzący uruchomił siedem prób istniejącego wykonawcy na kopii źródeł i fixture WIT1: wszystkie oczekiwania diagnostyczne potwierdzone, kod 0. W02 przyjmuje R bez raportu i nie ponawia sprawdzenia nowych blokad/testów; odmawia A; W04 odmawia przed W02. **Korekta powyższego historycznego zapisu:** W03 jest już obsługiwane przez odczytany kod i wykonana próba utworzyła pytanie blokujące oraz cofnęła wydanie do in_preparation. Nie należy używać wcześniejszego wniosku ze STAN.md jako opisu kodu. Skrypt i log są w repo, bez zależności od zachowania katalogu tymczasowego.

Przykład doprecyzowano o aktualność kryteriów, ponowną ocenę gotowości i rozróżnienie ustaleń blokujących/nieblokujących. To propozycje adaptera, nie aktywacja nowych zasad. Otwarte sprawy, właściciele i decyzje agenta są w raporcie. Następny krok agenta: objaśnić na jednym przypadku różnicę między istnieniem powiązań a aktualnością oceny; przed ewentualną implementacją wskazać wiążące źródła danych i sposób utrwalenia. D-81 pozostaje kierunkiem pilota; brak zmian Kitchen, template/ lub iso-model-state, bez commita i pushu.

Zamknięcie etapu: ten sam recenzent ponownie odczytał poprawiony przykład i potwierdził zamknięcie wszystkich czterech uwag w opisie. Nie jest to odbiór adaptera ani deklaracja jego pełnej gotowości. `make check`: 0 błędów, 4 znane ostrzeżenia; 66 odnośników bez braków, zachowana podstawa recenzji zgodna ze skrótem, `git diff --check` czyste. Wyniki i odpowiedź zamykająca są w raporcie powyżej.

### Wywiad z agentem vcs-lite — 2026-10-26

Użytkownik zlecił pięć rund z sesją Claude e5a1e620-442a-4613-9606-6bffe6dfbe04, bez ujawniania naszego modelu przed rundą 4. [Plan, zapis i wznowienie](../vcs-lite-interview/README.md), [wynik częściowy](../vcs-lite-interview/findings.md). Runda 1 wykonana, sprawdzono przytoczone zdarzenia; runda 2 odrzucona przez usługę (HTTP 429, five_hour, reset wskazany 15:50 Europe/Warsaw). Rund 3–5 nie wykonano. Nie zastępować odpowiedzi Claude własną syntezą.

Ustalono, że resume wskazuje wcześniejszą gałąź: późniejsze przyrosty istnieją w tym samym JSONL, ale nie w przodkach ostatniej wiadomości. Dostarczono je jako jawny materiał dodatkowy do oczekującej rundy 2. Prowadzący nie zmieniał źródłowych wiadomości; zaobserwowano techniczne dopiski metadanych, zachowany prefiks pozostał identyczny. Nie zmieniono vcs-lite, modelu procesu ani pakietu template/. Właściciel dalszej pracy: agent; po dostępności usługi wznowić od rundy 2, potem adaptacyjnie rundy 3–5. Rekomendacje końcowe i porównanie z modelem nadal niegotowe. Bez commita i pushu.

### Wywiad vcs-lite — zakończenie po ponowieniu

2026-10-26, użytkownik: „ponow”. Runda 2 ponowiona skutecznie, następnie przeprowadzono adaptacyjnie rundy 3–5. Nasz model pokazano dopiero w rundzie 4; skróty odpowiedzi 1–3 zapisano wcześniej. Rozmówca w każdym przebiegu miał wyłączone narzędzia i MCP. [Końcowa synteza](../vcs-lite-interview/findings.md) odsyła do pięciu niezmienionych odpowiedzi, pytań i dowodów historycznych. Nie wliczamy odrębnego wywiadu zapisanego równolegle w iso-model-state do tych pięciu rund.

Ustalenia: rzeczywiście działała kontrola brakującego testu; dyscyplina TDD wykryła test zielony z niewłaściwego powodu; użytkownik nadal korygował komunikację i użyteczność. Agent wycofał nadmierne twierdzenia o utracie cudzej pracy, zastąpieniu śladu nazwami testów, commicie jako baseline'ie, kolejce jako gwarancji jednego tematu i konieczności osobnych potwierdzeń. Synteza zawiera również korektę prowadzącego: niepełny cytat T04 w pytaniu 5.

Trzy kandydatury do małych prób: raport zgodny z logami, ocena skuteczności testu na znanej usterce, zrozumiały opis następnego działania. Nie są nową polityką ani dowodem przewagi procesu. Właściciel dalszej propozycji: agent; uwzględnić je przy ocenie istniejących widoków/raportów, zanim pojawi się nowy mechanizm. Wywiad zakończony; eksperymentów nie wykonano, D-81 i plan E2–E5 bez zmiany. Bez zmian vcs-lite, iso-model-state i template/, bez commita/pushu.

### Zapis materiałów przeglądu w Git

2026-10-26: użytkownik polecił „zrob commit(y)”. Zakres jednego spójnego zapisu: D-81/D-82, minimalny proces Kitchen, analiza mechanizacji i ról, mapa procesu z recenzją W02 i dowodami, pięć rund wywiadu vcs-lite, aktualny rejestr postępu i zapis odtworzenia lekcji. Powód wspólnego commita: materiały i rejestr mają wzajemne odnośniki. Poza zakresem pozostają zastane zmiany repository-evolution/ i osobny dokument użytkownika o modelu śladu. Kontrole przed zapisem: make check, składnia Python/JSON i diff --check; pakiet procesu oraz kod symulatora bez zmian, więc nie ponawiamy ich regresji. Polecenie nie obejmuje pushu ani odbioru procesu. Dalszy krok merytoryczny pozostaje jak wyżej.

### Kontrakt odbioru przyrostu przez API

2026-10-26: po omówieniu rozdziału operator–agent–system użytkownik zlecił wejście w rolę architekta protokołów/workflow i wykonanie metody opartej na przykładach, niezmiennikach i osobnym recenzencie. [Rezultat](../process-map/acceptance-contract.md): granica jednego odbioru, źródła, uprawnienia, cztery stany zgłoszenia, oddzielna gotowość, operacje inspect/submit/decide, 7 niezmienników i 23 scenariusze do przyszłych testów.

Osobny subagent w kontekście bez historii autora znalazł dwie usterki propozycji: niejednoznaczny poprzednik przy aktywnym zgłoszeniu oraz sprzeczne reguły równoczesnego ponowienia. Poprawiono obie, dodano scenariusze i doprecyzowano odrzucenie przy niedostępnym źródle. Recenzent potwierdził zamknięcie tych uwag; [raport i zachowane odpowiedzi](../process-map/acceptance-contract-review.md). To analiza dokumentu, nie wykonanie testów API ani akceptacja reguł przez operatora.

Decyzje autora A1–A5, źródła, koszt kontroli i pytania Q1–Q4 są przy kontrakcie i recenzji. Nie zmieniono template/, Kitchen, iso-model-state ani kodu symulatora. Nie wdrożono API, manifestów lub mechanizmu zgód. Brak nowego commita i pushu. Właściciel następnego kroku: agent; objaśnić S01/S03, a przed implementacją rozpoznać źródła i przygotować warianty Q1–Q4. Kontrole dotyczą dokumentacji; Mermaid nie był renderowany z powodu braku lokalnego mmdc.

### Porównanie z kontraktem innego agenta

2026-10-26: na prośbę użytkownika odczytano informative/architecture-2026-10-26/process-api-contract.md w iso-model-state wraz z recenzją i zapisanym wynikiem projekcji. [Porównanie](../process-map/api-contract-comparison.md) zachowuje hashe źródeł, wspólne założenia, różnice zakresu oraz kontrprzykład nowego nieprzyjętego wyniku negatywnego przed W04. Nie utożsamiono luki opisu adaptera z defektem nieistniejącego API. Nie powtarzano cudzych prób ani nie uruchamiano kolejnego recenzenta. Właściciel dalszego przygotowania: agent; mapa semantyczna odbioru przyrostu i wydania oraz doprecyzowanie aktualności wyników. Bez zmian porównywanych kontraktów, zewnętrznych repozytoriów, commita i pushu.
