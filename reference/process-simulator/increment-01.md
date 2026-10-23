# Pierwszy przyrost symulatora

Data: 2026-10-23. Status: propozycja do decyzji D-79; w rozmowie D1. Wynik ma być używalną lekcją w przeglądarce, przechodzącą przez scenariusz, silnik i widoki. Nie kończymy przyrostu na samym modelu Python ani zestawie dokumentów.

## Wynik dla operatora

Operator przechodzi pierwszy przyrost fikcyjnego TextStats: liczenie słów w poprawnym pliku. Wykonuje czynności, ogląda powstające informacje i widzi, dlaczego zaplanowanie testu, jego wykonanie oraz odbiór to różne fakty. Po nieudanym teście może poprawić implementację w fabule, ponowić próbę i doprowadzić przyrost do demonstracji oraz decyzji odbiorczej.

Treści oprzemy na [istniejącej lekcji TextStats](../repository-evolution/README.md), zachowując rozdzielenie przyrostu i wydania. Kwestia zachowania przy błędzie odczytu pozostaje otwarta w fabule: można odebrać uzgodniony przyrost, ale nie otrzymuje on automatycznie zgody na wydanie produktu. Nowy rekord odbioru w lekcji będzie jawnie fikcyjny, bez dopisywania go do materiału źródłowego.

## Przebieg ćwiczenia

| Czynność operatora w lekcji | Widoczny rezultat | Czego uczy |
| --- | --- | --- |
| Otwórz potrzebę i uzgodnij zakres w fabule | Potrzeba, definicja słowa, wymagania R1/R1a/R2 oraz otwarte Q1 | Znaczenie i granice poprzedzają implementację. |
| Przygotuj plan i projekt rozwiązania, przejrzyj wymagania | Plan przyrostu, kontrakty C1/C2 i zapis przeglądu | Czynność wytwarza informację, a powiązanie prowadzi do jej źródła. |
| Przygotuj testy | T1–T4 dla obliczenia i zaplanowany T5 dla integracji; brak wyników | Przypadek testowy nie jest wykonaniem. |
| Uruchom próbę na szkielecie | Symulowany wynik RED powiązany z rewizją kodu i testem | Błąd jest obserwacją, a nie samym kolorem statusu. |
| Zaimplementuj obliczenie, połącz adapter i ponów testy | Nowa rewizja kodu, osobne wykonania testów, symulowany GREEN | Poprawka nie nadpisuje wcześniejszego wyniku; integracja ma własne sprawdzenie. |
| Przeprowadź demonstrację | Instrukcja, wynik przykładowego użycia i ocena przydatności | Poprawność według testów i użyteczność to różne oceny. |
| Odbierz przyrost albo zgłoś potrzebę korekty | Jawna decyzja w lekcji; otwarte sprawy pozostają widoczne | Zielone testy nie podejmują decyzji za operatora. |

Kolejność w tabeli jest prowadzonym przykładem. Silnik sprawdza konkretne zależności działań, a nie wyłącznie numer slajdu. Próba pominięcia sprawdzenia lub odbioru pokazuje brakującą podstawę; nieznane i powtórzone polecenie nie uszkadza stanu. Odrzucenie przyrostu zachowuje powód i umożliwia korektę oraz nową demonstrację.

## Zakres interfejsu

Jeden ekran: po lewej przebieg i dostępne działania; pośrodku mały graf produktów; po prawej karta zaznaczonego elementu; poniżej historia. Karta pokazuje treść, lokalne ID, rewizję, przykładowy plik, typ WP, relacje i powód powstania. Nie wymagamy znajomości kodów ISO, aby wykonać następny krok.

Graf i historia powstają z tego samego stanu. Każdy wynik fabuły ma oznaczenie „symulacja”. Przegląd wcześniejszego kroku jest tylko do odczytu; aby kontynuować, wracamy do bieżącego końca historii. Eksport i import pozwalają przenieść ćwiczenie przez restart. Nie zapisujemy sesji automatycznie; operator ma widoczną informację o potrzebie eksportu.

## Granica przyrostu i dalsza kolejność

I1 obejmuje jedną pełną lekcję, ścieżkę nieudanego testu i korekty, trzy widoki, inspekcję historii oraz zapis i wznowienie sesji. Odnosi się do etapów S1–S4 planu głównego, lecz nie oznacza zakończenia wszystkich ich szerszych kryteriów.

Proponuję następnym przyrostem objąć zmianę wymagania po GREEN i tworzenie alternatywnej gałęzi historii. Są zapisane w planie całej pierwszej wersji, ale odłożenie ich poza I1 wymaga decyzji D-79. Nie oznaczamy ich jako wykonanych ani usuniętych z celu. Alloy/TLC pozostają opcjonalnym S5. Kuchnia, rzeczywiste wydania, manifesty i mechanizm zgód projektu pozostają poza zakresem tej lekcji.

## Wykonanie w Pythonie

Utrzymujemy [proponowaną architekturę](technical-plan.md): biblioteka standardowa Pythona, lokalne HTTP, HTML/CSS/JavaScript i SVG. Szczegóły implementacji agent dobiera w granicach zatwierdzonego zakresu i zapisuje istotne decyzje w rejestrze postępu.

| Zasada | Konkretne zastosowanie | Unikany problem |
| --- | --- | --- |
| Czysty rdzeń i adaptery | Typowane rekordy stanu, polecenia i wyniki; przejście nie czyta plików ani zegara. HTTP i zapis są adapterami. | Ukryte efekty uboczne i testy zależne od środowiska. |
| Jedno miejsce reguł | Dostępność działania i jego wykonanie korzystają z tej samej oceny warunków. | Inne zasady w interfejsie i backendzie. |
| Małe jawne odpowiedzialności | Funkcje i rekordy danych; kompozycja. Osobno silnik, projekcje i transport. | Rozbudowane hierarchie klas, uniwersalny workflow engine i klasa zarządzająca wszystkim. |
| Stan wynika z faktów | Historia i rewizje; powiązania odwrotne oraz gotowość są wyliczane. | Kilka ręcznie synchronizowanych statusów i grafów. |
| Dane lekcji poza logiką przejść | Treści produktów i objaśnienia jako jawne dane; warunki jako testowane funkcje. | Zaszycie całej lekcji w instrukcjach warunkowych albo budowa własnego języka skryptowego. |
| Atomowa odmowa | Najpierw walidacja całego polecenia, potem nowy stan; błędy mają konkretne przyczyny. | Częściowa mutacja i maskowanie błędów ogólnym wyjątkiem. |
| Jawna symulacja | Wynik prób produktu pochodzi z ustalonego wariantu scenariusza, nie z deklaracji `pass` przesłanej przez UI. | Animacja mylona z wykonaniem testów lub zatwierdzeniem produktu. |

Treść karty nie jest kopią stanu utrzymywaną ręcznie. UI nie posiada drugiego silnika. Nie wprowadzamy ogólnego systemu wtyczek, asynchroniczności ani wielu usług bez wykazanej potrzeby. Determinizm i jawne zależności są ważniejsze niż liczba abstrakcji.

## Kolejność pracy i dowody

1. Utrwalić obiekty, relacje, zdarzenia i oczekiwane skutki wycinka lekcji, mapując źródłowe ID TextStats bez udawania, że są ID normy.
2. Napisać test jednego pełnego przebiegu i krytycznych odmów, uzyskać RED, zbudować minimalny silnik, uzyskać GREEN.
3. Wcześnie połączyć silnik z prostym ekranem: potrzeba → wymaganie → test → wynik. Rozwinąć ten sam pionowy przekrój o resztę uzgodnionej lekcji.
4. Dodać zapis i wznowienie, inspekcję historii, korektę po błędzie i po odmowie odbioru. Sprawdzić uszkodzony import i nieobsługiwaną wersję.
5. Wykonać pełny scenariusz w przeglądarce, porównać karty i graf z historią, zapisać dowody oraz instrukcję startu. Dopiero wtedy przekazać aplikację operatorowi do oceny edukacyjnej.

Testy mają obserwować zachowanie i niezmienniki, nie prywatne funkcje. Oczekiwany przebieg zapisujemy niezależnie od implementacji; generator dostępnych akcji nie może być jedyną wyrocznią własnych testów. Przynajmniej jedna kontrolowana mutacja reguły ma zostać wykryta. Rzeczywisty RED/GREEN silnika i symulowany RED/GREEN TextStats mają osobne oznaczenia i miejsca zapisu.

## Kryteria gotowości do próby użytkownika

- Aplikacja uruchamia się lokalnie według sprawdzonej instrukcji i pozwala przejść całą lekcję.
- Kliknięcie elementu wyjaśnia różnicę między typem WP, produktem, lokalnym ID i rewizją oraz prowadzi do zależności.
- Przypadek testowy bez wykonania nie ma wyniku; poprawka zachowuje wcześniejszy raport; odbiór nie pojawia się automatycznie.
- Odmowa niedozwolonego działania podaje przyczynę i pozostawia stan bez zmian; poprawna ścieżka pozostaje osiągalna.
- Eksport/import odtwarza tę samą historię, stan i relacje; wadliwy import nie zastępuje bieżącej sesji.
- Testy silnika i próba przeglądarkowa mają trwały zapis wyników; symulowane wyniki produktu są jednoznacznie oznaczone.
- Punkt wznowienia opisuje wynik, ograniczenia i pracę pozostającą poza I1. Nie ma deklaracji odbioru Użytkownika przed jego odpowiedzią.

Próba edukacyjna: operator wskazuje, co powstało po czynności, co pozostaje tylko planem, dlaczego następny krok jest dostępny lub nie i dlaczego GREEN nie oznacza wydania. Zapisujemy jego odpowiedzi i potrzebne podpowiedzi, nie zgadujemy progu sukcesu.
