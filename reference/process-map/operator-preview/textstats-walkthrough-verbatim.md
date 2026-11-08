# Karta TextStats — zapis rozmowy verbatim

Zapis 2026-11-07 na wyraźne polecenie użytkownika. Sekcje 1–5 zawierają pełne, dosłowne odpowiedzi asystenta dotyczące propozycji karty i przejścia przez nią, od powrotu do karty po wyjaśnienie PASS/FAIL. Nagłówki sekcji i ten wstęp są metadanymi archiwum. Zachowano Markdown oraz znacznik niedostępnej wizualizacji; działająca treść makiety jest osobno w [textstats-card.html](textstats-card.html).

To materiał edukacyjny, nie nowe wymagania, zlecenia wykonania ani decyzje odbioru. Cytowane polecenia są przykładami wiadomości. Fikcyjne wyniki F5 nie dowodzą działania TextStats. Sekcja 6 jest nową kontynuacją, oddzieloną od zapisów wcześniejszych wiadomości.

## 1. Powrót do jednej karty i propozycja widoków — odpowiedź asystenta

**Tak — wracamy do jednej czytelnej karty funkcji TextStats.** Powinna pomagać Ci odpowiedzieć: „co robimy, gdzie jesteśmy, czego brakuje i o co mam poprosić agenta?”.

Proponuję **trzy perspektywy tej samej sprawy**, korzystające z tych samych danych:

- **Co teraz?** — stan pracy, następny krok i ewentualna decyzja dla Ciebie.
- **Na jakiej podstawie?** — wymaganie, test, wynik oraz ograniczenia dowodów.
- **Co się zmieniło?** — historia potrzebna do zrozumienia obecnego stanu.

Poniżej możesz je przełączać. Przyciski przygotowują edytowalny szkic wiadomości. To propozycja na podstawie zapisanej symulacji F5, bez połączenia z silnikiem.

visualize{"path":"/Users/michal/PycharmProjects/iso-template-agent/reference/process-map/operator-preview/textstats-card.html"}

**Ty piszesz o sensie pracy; narzędzie powinno dołączać jej jednoznaczny kontekst.** Przykładowo: „Sprawdź, czy te testy naprawdę potwierdzają tę regułę”. Docelowo agent otrzymywałby wskazaną funkcję, rewizje i podstawę oceny, a przed działaniem sprawdzał aktualność. Nie musiałbyś przepisywać identyfikatorów ani pamiętać historii. Samo pytanie nie oznaczałoby zgody na zmianę lub odbiór.

**Dalej:** zacznij od „Co teraz?” i wybierz „Przygotuj pytanie o odbiór” — zobaczysz, jak stan procesu może pomóc Ci napisać konkretną wiadomość.

## 2. Tekstowy odpowiednik niedostępnej wizualizacji — odpowiedź asystenta

Nie możesz wyświetlić makiety w tym urządzeniu. Poniżej ten sam pomysł w zwykłym tekście.

**TEXTSTATS → Funkcja: liczenie słów**  
Bieżąca zmiana: „myślnik rozdziela słowa”.

| Widok | Co zobaczysz |
|---|---|
| **Co teraz?** | W scenariuszu poprawiono regułę i test. Kontrole zapisano jako pozytywne. Proces oczekuje Twojego odbioru. |
| **Na jakiej podstawie?** | Reguła: myślnik jest separatorem. Przykład: `biało-czerwony → 2`. Wskazana wersja programu i przypisane wyniki. **Wyniki są fikcyjne — F5 nie uruchamiał TextStats.** |
| **Co się zmieniło?** | Wcześniej wykonanie miało PASS, ale przegląd przypadku FAIL. Poprawiono przypadek i program; stare wyniki pozostały w historii. |

Pod tym byłoby pole **„Wiadomość do agenta”**, np.:

> Wyjaśnij, co dokładnie miałbym odebrać. Pokaż przykład działania i odróżnij rzeczywiste dowody od zapisów symulacji. Na razie niczego nie zatwierdzam.

**Najważniejsze:** Ty wskazujesz sprawę i piszesz zwykłym językiem. Docelowy interfejs dołącza identyfikatory i wersje do wiadomości; agent sprawdza aktualny stan. Nie musisz ich pamiętać. To proponowane zachowanie, jeszcze niewdrożone.

**Dalej:** przejdźmy przez tę kartę tekstowo — najpierw ustalimy, co oznacza tutaj „czeka na odbiór” i czego potrzebujesz, żeby świadomie zdecydować.

## 3. Co teraz? — odpowiedź asystenta

**Zaczynamy od „Co teraz?”. Karta mówi: czeka na Twój odbiór — ale w tym przykładzie chodzi o odbiór w symulacji, nie potwierdzenie działania prawdziwego programu.**

Wyobraź sobie, że wracasz do projektu po kilku dniach i widzisz:

> **TextStats — zmiana sposobu liczenia słów**  
> Chcemy, żeby `biało-czerwony` było liczone jako **2 słowa**.  
> Zapisano poprawione wymaganie, przypadek testowy i wersję programu.  
> Kontrole w scenariuszu są pozytywne. **Twojego odbioru jeszcze nie ma.**

To pozwala zorientować się w pracy, ale **jeszcze nie wystarcza do podjęcia decyzji**. Naturalną reakcją operatora jest poproszenie o podstawę oceny:

> **„Pokaż mi, co dokładnie się zmieniło i skąd wiadomo, że teraz działa.”**

Agent powinien odpowiedzieć konkretnie:

| Pytanie | Co wiemy w naszym przykładzie |
|---|---|
| Co miało się zmienić? | Myślnik ma rozdzielać słowa. |
| Jak to sprawdzamy? | Dla `biało-czerwony` oczekujemy wyniku `2`. |
| Czy wykonano sprawdzenie programu? | W próbie F5 **nie** — zapisano fikcyjny wynik PASS. |
| Co zatem możemy ocenić teraz? | Czy rozumiesz regułę oraz sposób przedstawienia podstawy odbioru. Nie poprawność programu. |

**Praktyczna korzyść karty:** nie musisz odtwarzać historii rozmowy. Widzisz zamiar, stan oraz konkretny brak. Możesz zlecić wyjaśnienie lub sprawdzenie, zamiast zgadywać, czy „zielone” oznacza „gotowe”.

**Dalej:** przechodzimy do „Na jakiej podstawie?” — przyjrzymy się, dlaczego samo `biało-czerwony → 2` może być zbyt słabą podstawą do odbioru całej reguły.

## 4. Na jakiej podstawie? — odpowiedź asystenta

**Teraz widok „Na jakiej podstawie?”. Sprawdzamy, czy dowody odpowiadają temu, co obiecaliśmy.**

Nasza reguła brzmi: **„myślnik rozdziela słowa”**. Przypadek `biało-czerwony → 2` pokazuje jedno zastosowanie. Sam nie rozstrzyga pozostałych sytuacji:

| Przykład | Co trzeba ustalić |
|---|---|
| `biało-czerwony` | Oczekiwane `2` — to zapisano w scenariuszu. |
| `biało--czerwony` | Czy kolejne separatory traktujemy jako jeden? |
| `-czerwony` | Czy separator na początku wpływa na wynik? |
| `biało–czerwony` | Czy półpauza `–` ma działać tak samo jak myślnik `-`? |

To **pytania ilustrujące granice reguły**, nie dopisane wymagania ani lista spraw, na które musisz teraz odpowiedzieć.

Jako operator możesz napisać:

> „Sprawdź, które z tych sytuacji rozstrzygają nasze obecne wymagania. Zaproponuj brakujące przykłady. Do mnie skieruj tylko decyzje, których nie da się wyprowadzić z ustaleń.”

Agent powinien najpierw przeczytać istniejące ustalenia. **Nie powinien ani zgadywać znaczenia reguły, ani przerzucać na Ciebie każdego szczegółu testowania.**

W karcie potrzebujemy więc rozdzielić:

- **Co obiecujemy** — treść i granice wymagania.
- **Jak to sprawdzamy** — przypadki z oczekiwanymi wynikami.
- **Co rzeczywiście sprawdzono** — wykonania dla wskazanej wersji programu.

W F5 mamy fikcyjne zapisy tych ocen i wykonań. Pozwalają ćwiczyć proces, ale nie dowodzą działania TextStats.

**Dalej:** zajrzymy do historii: jak wykonanie testu mogło mieć **PASS**, a przegląd tego samego przypadku **FAIL** — i dlaczego to nie jest sprzeczność.

## 5. Co się zmieniło? PASS wykonania i FAIL przeglądu — odpowiedź asystenta

**Teraz „Co się zmieniło?”. Test może przejść, a mimo to sprawdzać niewłaściwą rzecz.**

Załóżmy taki przebieg — to ilustracja mechanizmu, nie odtworzenie szczegółów zapisanych w F5:

| Element | Przed zmianą | Po zmianie wymagania |
|---|---|---|
| Wymaganie | `biało-czerwony` to **1 słowo** | Teraz oczekujemy **2 słów** |
| Przypadek testowy | Oczekuje **1** | Przez przeoczenie nadal oczekuje **1** |
| Program | Zwraca **1** | Jeszcze niezmieniony: zwraca **1** |

Uruchamiamy stary test. Program zwraca `1`, test oczekuje `1` — **PASS**.

Następnie przeglądamy przypadek względem nowego wymagania: oczekuje `1`, chociaż powinien oczekiwać `2` — **FAIL**.

**Obie oceny są prawidłowe, bo odpowiadają na inne pytania:**

- **Wykonanie testu:** czy program zwrócił to, czego oczekiwał test?
- **Przegląd przypadku:** czy test oczekuje tego, co uzgodniliśmy?

W historii F5 rzeczywiście zapisano PASS wykonania i FAIL przeglądu przypadku. Sam zapis nie wystarcza jednak, żeby przypisać mu dokładnie powyższą przyczynę.

Na karcie operatora chcielibyśmy zobaczyć:

> **Nie ma jeszcze podstaw do odbioru.**  
> Wykonanie ma PASS, ale przypadek testowy nie przeszedł przeglądu.  
> **Następny krok agenta:** wyjaśnić zastrzeżenie, poprawić przypadek i ponownie sprawdzić właściwą wersję programu.

Możesz wtedy napisać:

> „Rozlicz zastrzeżenie do przypadku testowego. Pokaż poprawkę i nowe wyniki. Zachowaj wcześniejsze wyniki w historii; nie wykonuj odbioru za mnie.”

**Dalej:** domkniemy kartę — co agent powinien przynieść po poprawce, żebyś mógł podjąć decyzję bez czytania całej historii.

## 6. Kontynuacja: co agent przynosi do odbioru

**Po poprawce agent powinien przynieść krótką podstawę decyzji, a nie samo „testy zielone”.** Poniżej wzór dla rzeczywistej pracy — nie raport wykonania TextStats:

| Na karcie | Co powinno się znaleźć |
|---|---|
| **Co odbierasz** | Konkretny wycinek: zmieniona reguła liczenia słów, w uzgodnionych granicach. |
| **Co poprawiono** | Zastrzeżenie do przypadku, sposób jego usunięcia i wynik ponownego przeglądu. |
| **Jak działa** | Przykład uruchomiony na wskazanej wersji programu, z oczekiwanym i rzeczywistym wynikiem. |
| **Co sprawdzono poza przykładem** | Wyniki uzgodnionych kontroli i regresji; szczegóły dostępne przez odnośniki. |
| **Co pozostaje niepewne** | Znane ograniczenia oraz nierozstrzygnięte kwestie wpływające na odbiór. |
| **Jaka decyzja jest potrzebna** | Przyjęcie tego zakresu i tej wersji albo wskazanie konkretnego zastrzeżenia. |

Nie musisz osobiście powtarzać całej pracy agenta. Potrzebujesz zrozumieć **co dostajesz, na czym opiera się ocena i jakie są jej granice**. Możesz poprosić o demonstrację lub pogłębienie konkretnego punktu.

Przykładowa wiadomość operatora:

> „Pokaż demonstrację na wersji wskazanej do odbioru i wyjaśnij pozostałe ograniczenia. Potem zdecyduję.”

To nadal prośba o sprawdzenie, nie zgoda. Jeśli po ocenie przyjmujesz wynik, zapis odbioru powinien wskazywać dokładnie ten zakres i wersję. **Późniejsza zmiana nie dziedziczy automatycznie wcześniejszego odbioru.**

W naszym F5 ta karta nadal musi pokazywać: **wyniki są symulowane; rzeczywistego działania TextStats nie sprawdzono**. Nie proponuję więc teraz odbioru programu.

**Dalej:** przejdziemy przez sytuację „po odbiorze chcę zmienić regułę” — zobaczysz, jak karta zachowuje wcześniejszy wynik i pokazuje nową pracę.


## 7. Kontynuacja: zmiana po odbiorze

**Odbiór zamyka konkretny zakres i wersję. Nowy pomysł otwiera nową pracę, ale nie kasuje tego, co wcześniej przyjęto.** To dalszy przykład edukacyjny, nie rzeczywisty odbiór TextStats.

Załóżmy, że przyjęto regułę dla znaku `-`. Później piszesz:

> „Chciałbym, żeby półpauza `–` też rozdzielała słowa. Sprawdź, co trzeba zmienić.”

Karta powinna pokazać dwie rzeczy jednocześnie:

| Dotychczasowy wynik | Nowa propozycja |
|---|---|
| Obsługa `-` przyjęta dla wskazanej wersji. | Rozszerzenie o `–` jest analizowane. |
| Dawne testy, wyniki i odbiór pozostają w historii. | Agent ustala wpływ na wymagania, kod i testy. |
| Poprzedni odbiór nadal opisuje poprzedni zakres. | Zlecenie analizy nie jest jeszcze zgodą na wykonanie rozszerzenia. |

Agent powinien przynieść krótką propozycję: co zmieni, czego dotknie i jak to sprawdzi. Po Twojej zgodzie wykonuje zmianę, zachowuje wcześniejsze dowody i przedstawia nowy wynik do odbioru.

**Na karcie nie cofamy całej funkcji do „niezrobione”.** Pokazujemy: „dotychczasowy zakres odebrany; rozszerzenie w analizie”. Stary wynik testu może pozostać prawdziwy dla starej wersji, ale nie stanowi dowodu obsługi nowego znaku.

**Dalej:** pokażemy mapę kilku funkcji — jak z takich kart zobaczyć cały projekt, zależności i najbliższą możliwą pracę.

## 8. Powiązania przed mapą funkcji — propozycja, nie wdrożony model

2026-11-07. Użytkownik wskazał §9 jako podstawę rozróżnienia informacji, identyfikatorów i sposobu prezentacji. Ponownie odczytano wprowadzenie do rozdziału 9 w lokalnym źródle.

**To dobry moment na ustalenie znaczenia relacji, zanim powstanie mapa wielu funkcji.** Rysunek z jednakowymi strzałkami „powiązane z” nie pozwoli rozpoznać, co grupuje informacje, co blokuje pracę, a co jest podstawą oceny.

### Źródło i nasza propozycja

[ISO §9](../../../../iso-29110-5-1/chapters/09-description-of-work-products.md) dopuszcza łączenie i dzielenie informacji oraz elektroniczne nośniki. Zaleca też pomijanie kodów WP.XX w opisach aktywności i zadań dla czytelności. WP.13 w katalogu wskazuje specyfikację wymagań; nie identyfikuje konkretnego wymagania TextStats. Z tego nie wynika gotowy model bazy danych ani zakaz identyfikatorów elementów projektu.

Nasza propozycja: karta funkcji grupuje widoki informacji przez odnośniki, nie utrzymuje ich kopii. „Funkcja” jest tutaj jednostką organizacji pracy dobraną przez nas; nie dopisujemy nowego obowiązkowego produktu pracy ISO.

### Co łączymy i po co

| Relacja | Znaczenie | Przykład / ograniczenie |
|---|---|---|
| Funkcja → wymagania | Określają jej zachowanie | „Liczenie słów” pokazuje regułę separatorów. Jedno wspólne wymaganie może dotyczyć kilku funkcji. |
| Zmiana → wskazane rewizje wymagań | Proponuje lub realizuje zmianę zakresu | Dodanie półpauzy ma osobną propozycję; sama przynależność do odebranej funkcji nie nadaje mu odbioru. |
| Zadanie → wynik pracy | Określa, co ma powstać lub zostać zmienione | Zadanie „popraw przypadek” prowadzi do nowej rewizji przypadku. Zamknięcie zadania nie dowodzi jego poprawności. |
| Przypadek testowy → rewizje wymagań | Deklaruje, jakie zachowanie ma sprawdzać | AT-01@3 odnosi się do CAP-01@2. To deklaracja śladu, której sens wymaga oceny. |
| Przegląd → badane rewizje i podstawa oceny | Zapisuje ocenę konkretnych informacji | FAIL dla AT-01@2 nie staje się automatycznie oceną AT-01@3. |
| Wykonanie → rewizja testu i wersja programu | Wiąże zaobserwowany wynik z tym, co uruchomiono | W rzeczywistym projekcie również dane wejściowe i istotne środowisko. W F5 wykonania są fikcyjne. |
| Odbiór → ustalony zakres, wersja i wskazane dowody | Zachowuje przedmiot decyzji operatora | Nowe rewizje nie są dopisywane po cichu do wcześniejszego odbioru. |
| Zadanie → warunek rozpoczęcia lub zakończenia | Określa rzeczywistą zależność pracy | „Do integracji potrzebny uzgodniony kontrakt wejścia”; to nie musi blokować analizy lub pracy ze stubem. |

To relacje o różnych znaczeniach; nie narzucamy relacji jeden-do-jednego. Wspólny moduł lub reguła mogą dotyczyć wielu funkcji. Sama wspólna zależność nie oznacza, że funkcje muszą być realizowane kolejno.

### ID, rewizja i nośnik

- Nazwa dla człowieka: „Myślnik rozdziela słowa”.
- ID elementu: CAP-01, zachowane mimo zmiany nazwy lub pliku.
- Rewizja: CAP-01@2, konkretna treść stanowiąca podstawę oceny.
- Nośnik: plik, rekord narzędzia lub sekcja; jeden nośnik może zawierać kilka elementów.

Do nawigacji karta może pokazywać bieżącą rewizję. Rekord wyniku lub odbioru wskazuje dokładnie badaną podstawę, nie ruchome „najnowsze”. Powiązanie zapisujemy raz w źródle, a widok w drugą stronę wyliczamy. To propozycja dla karty; bez migracji istniejącego schematu.

### Co dzięki temu zobaczy operator

Na mapie nie będzie jednego statusu „funkcja zrobiona”, który ukrywa nowe zmiany. Dla jednej funkcji pokażemy osobno **zakres odebrany**, **bieżącą zmianę** i **następny krok / konkretny warunek**. Agent może mechanicznie odszukać powiązane elementy, brakujące referencje lub inną rewizję podstawy. Nie wywnioskuje z samych strzałek kompletności wymagań ani poprawności testu.

Nie nazywamy informacji „blokadą” tylko dlatego, że istnieje krawędź. Blokada wymaga jawnego warunku i ustalonego stanu; brak danych pokazujemy jako „nieustalone”, a nie „gotowe”. Przegląd znaczenia i ustalenie zakresu wpływu pozostają pracą człowieka/agenta. Nie tworzymy teraz uniwersalnego silnika reguł ani pełnego schematu danych.

Następny krok edukacyjny: mapa kilku wyraźnie oznaczonych przykładowych funkcji TextStats, z oddzieleniem powiązań informacyjnych od warunków kolejności; bez przypisywania fikcyjnych postępów rzeczywistemu projektowi.

## 9. Mapa kilku funkcji — przykład edukacyjny

2026-11-07. To propozycja widoku i fikcyjny zakres do objaśnienia relacji, nie odczyt backlogu TextStats ani zgoda na implementację. Nie przypisujemy funkcjom rzeczywistych statusów wykonania.

**Mapa projektu powinna pokazywać zdolności programu oraz to, co pozwala nad nimi pracować.** Weźmy trzy przykładowe funkcje:

| Karta funkcji | Wartość dla użytkownika | Wspólne informacje / zależności |
|---|---|---|
| Policz wpisany tekst | Wpisuję tekst i widzę liczbę słów. | Korzysta z reguły liczenia słów. |
| Policz tekst z pliku | Wybieram plik i widzę liczbę słów. | Korzysta z tej samej reguły oraz ustaleń dotyczących odczytu pliku. |
| Zapisz wynik | Zachowuję obliczony wynik. | Korzysta z uzgodnionej postaci wyniku oraz ustaleń formatu zapisu. |

Każda karta opisuje efekt użytkowy. Nie utożsamiamy funkcji z modułem kodu; kilka funkcji może używać wspólnego modułu, a jedna funkcja może wymagać zmian w kilku modułach.

### Widok powiązań informacyjnych

```text
[Policz wpisany tekst] ── realizuje ──▶ [Reguła liczenia słów]
[Policz tekst z pliku] ── realizuje ──▶ [ta sama reguła]
[Policz tekst z pliku] ── realizuje ──▶ [Wymagania odczytu pliku]

[Obliczanie wyniku] ── wytwarza dane zgodne z ──▶ [Kontrakt wyniku]
[Zapisz wynik]      ── przyjmuje dane zgodne z ──▶ [ten sam kontrakt]
```

„Reguła” i „kontrakt” występują w danych raz; mapa może pokazywać ich odnośniki przy kilku funkcjach. Rysunek nie ustanawia kolejności realizacji. Kontrakt oznacza tu uzgodnioną postać danych, np. jakie pola zawiera wynik — nie dodatkową umowę z klientem.

### Widok następnej możliwej pracy

| Praca | Co można robić wcześniej | Warunek sprawdzenia całości |
|---|---|---|
| Liczenie słów | Doprecyzować regułę i przygotować przykłady. | Uruchomić uzgodnione przypadki na wskazanej wersji programu. |
| Odczyt pliku | Osobno sprawdzić odczyt tekstu i błędy wejścia. | Zintegrować z liczeniem i sprawdzić drogę plik → wynik. |
| Zapis wyniku | Po uzgodnieniu kontraktu sprawdzić zapis na danych przykładowych. | Sprawdzić zapis rzeczywistego wyniku obliczenia. |

Wpis „można wcześniej” dotyczy technicznej możliwości w zatwierdzonym zakresie, nie upoważnienia do rozpoczęcia prac. Test zapisu na przykładowych danych nie dowodzi poprawności integracji z liczeniem.

**Zależność danych nie oznacza blokady całej funkcji.** Brak działającego licznika może blokować sprawdzenie pełnej drogi, ale nie musi blokować analizy formatu zapisu czy testu zapisu na danych przykładowych. Dlatego warunek przypinamy do konkretnej pracy lub kontroli.

### Co napisze operator po zmianie reguły

> „Rozważamy dodanie półpauzy jako separatora. Pokaż, których funkcji i testów to dotyczy. Oddziel wpływ potwierdzony od miejsc wymagających sprawdzenia. Na razie tylko analiza.”

Powiązania wskażą obie funkcje liczące jako kandydatów. Zapis wyniku również trzeba rozważyć: struktura danych może pozostać bez zmian, lecz testy całej drogi mogą oczekiwać innej liczby słów. Agent ocenia ten wpływ; graf sam nie dowodzi ani potrzeby zmiany kodu, ani braku wpływu.

Mapa pomaga więc odszukać zakres analizy, ale nie zastępuje analizy. W widoku operatora każda karta zachowuje osobno zakres odebrany, bieżącą zmianę i konkretny następny krok. Gdy brakuje danych, stan brzmi „nieustalone”, a nie „gotowe”.

Następny krok edukacyjny: przeprowadzić jedno polecenie operatora z tej mapy do planu pracy agenta, z rozróżnieniem analizy i zgody na wykonanie; bez uruchamiania fikcyjnego zakresu produktu.

## 10. Od wiadomości operatora do propozycji planu

2026-11-07. Kontynuacja edukacyjna; nie wykonano analizy kodu ani testów TextStats. Przykładowa wiadomość operatora brzmi:

> „Rozważamy dodanie półpauzy jako separatora. Pokaż, których funkcji i testów to dotyczy. Oddziel wpływ potwierdzony od miejsc wymagających sprawdzenia. Na razie tylko analiza.”

### 1. Agent ustala granice polecenia

Może czytać wymagania, powiązania, kod i wyniki oraz przygotować propozycję. Nie zmienia zatwierdzonej reguły i nie rozpoczyna implementacji. Sprawdza również, czy półpauza nie jest już objęta istniejącymi ustaleniami — nowa wiadomość nie przesądza, że jest to rozszerzenie zakresu.

### 2. Powiązania wskazują miejsca do zbadania

| Kandydat | Dlaczego go sprawdzamy | Czego nie wiemy bez odczytu |
|---|---|---|
| Reguła separatorów | Pytanie dotyczy znaczenia słowa i separatora. | Czy obecna treść już obejmuje znak `–`. |
| Obie funkcje liczące | W mapie korzystają ze wspólnej reguły. | Czy rzeczywisty kod stosuje ją wspólnie i jednakowo. |
| Przypadki i wyniki testów | Oczekiwana liczba słów może się zmienić. | Które przypadki zawierają ten znak i jakiej wersji dotyczą wyniki. |
| Zapis wyniku | Otrzymuje dane z liczenia. | Czy trzeba zmienić kod, czy jedynie oczekiwany wynik testu całej drogi. |

To lista do zbadania, nie raport potwierdzonego wpływu. W rzeczywistej pracy agent dopisuje ustalenie oraz odnośnik do konkretnego źródła i wersji. Brak relacji nie jest dowodem braku wpływu; potrzebny jest również przegląd faktycznego przepływu w kodzie.

### 3. Agent wraca z krótką propozycją

Dla ćwiczenia załóżmy, że odczyt potwierdził: obecne wymaganie obejmuje tylko `-`, a `–` jest nowym zakresem. Agent proponuje:

> „Rozszerzyć regułę separatora o znak `–`. Przedstawię zmienioną treść wymagania i przykłady, następnie dostosuję implementację oraz sprawdzę obie drogi wejścia i zapis wyniku. Wcześniejszy odbiór zachowam dla poprzedniej wersji.”

Taka propozycja w rzeczywistym projekcie wymagałaby wskazanych źródeł, kosztów lub ryzyk, jeśli są istotne, i jawnych niewiadomych. W ćwiczeniu nie udajemy, że je zbadano. Człowiek decyduje o rozszerzeniu zakresu, a nie o nazwach funkcji w kodzie czy kolejności drobnych zmian.

### 4. Plan wykonania pozostaje warunkowy do uzyskania zgody

| Krok po zgodzie | Rezultat / warunek zakończenia |
|---|---|
| Utrwalić uzgodnioną regułę i przykłady | Jednoznaczna podstawa nowego zakresu. |
| Dodać test nowego zachowania | RED: test nie przechodzi z oczekiwanej przyczyny. Jeśli zachowanie już działa, nie fabrykować RED — wyjaśnić i odpowiednio skorygować plan. |
| Wprowadzić potrzebną zmianę kodu | GREEN dla nowego zachowania oraz wymaganych testów regresji. |
| Sprawdzić drogi wejścia i zapis | Wyniki wskazujące testowane wersje i dane; rozliczone zastrzeżenia. |
| Przedstawić podstawę odbioru | Zakres, wersja, dowody i ograniczenia gotowe do decyzji operatora. |

Zgoda na wykonanie zmiany nie jest późniejszym odbiorem. Jeśli analiza wykaże, że zachowanie już wynikało z zatwierdzonego wymagania, agent rozpatruje naprawę w istniejącym zakresie zamiast automatycznie eskalować rozszerzenie; nadal respektuje ustalone granice ryzyka i zobowiązań.

### 5. Co widzi operator

```text
Dotychczasowy zakres: odbiór zachowany dla poprzedniej wersji
Nowy zakres: propozycja rozszerzenia — czeka na decyzję
Plan: przygotowany, wykonanie nierozpoczęte
Najbliższa decyzja: czy rozszerzyć regułę o półpauzę?
```

Powyższe statusy są założeniem scenki, nie stanem repozytorium. Sens praktyczny: operator otrzymuje ograniczoną propozycję i podstawę decyzji, a agent ma jednoznaczne granice dalszej pracy. Nie wymagamy od operatora pamiętania listy zależności.

Następny krok edukacyjny: rozdzielić, które elementy tego przebiegu kontroluje mechanizm, a które wymagają analizy i decyzji; bez nowego zakresu implementacyjnego.

## 11. Cel i koniec wątku karty — propozycja do uzgodnienia

2026-11-07. Użytkownik zapytał o jasny cel, zakończenie i uzgodnione kryteria odbioru. Przegląd zapisów potwierdza: mamy kryteria technicznej próby F5 oraz ogólny zamiar oceny użyteczności, ale nie uzgodniliśmy osobnych, obserwowalnych kryteriów zakończenia obecnego tekstowego przejścia. Kolejne „Dalej” autoryzowały następne objaśnienia; nie stanowiły odbioru ani zgody na dowolne rozszerzanie lekcji. Agent odpowiada za brak wyraźnego końca tego wątku.

**Proponowany cel:** sprawdzić, czy operator potrafi na podstawie czytelnej karty zorientować się w pracy i przekazać agentowi adekwatne polecenie, bez rekonstruowania historii rozmów. To ocena koncepcji widoku w ograniczonym ćwiczeniu, nie dowód użyteczności całego procesu ani wdrożenie UI.

**Proponowany rezultat:** jedna zwarta karta tekstowa (sens, zakres, stan, podstawa, brak/warunek i następny krok), pokazana w trzech stanach istniejącego ćwiczenia: brak podstaw do odbioru, podstawa przygotowana do decyzji oraz propozycja zmiany po wcześniejszym odbiorze. Każdy stan jawnie oznacza dane symulowane. Nie tworzymy dalszych funkcji, nowego modelu danych, API ani silnika.

**Proponowane kryteria:**

| Kryterium | Obserwowalny sprawdzian |
|---|---|
| Orientacja | Z samej karty operator wskazuje zakres, co już wykonano i co pozostało lub blokuje krok. |
| Podstawa oceny | Operator rozpoznaje, czego dotyczą wyniki, co jest symulacją/brakiem dowodu i czy wynik odnosi się do rozpatrywanej wersji. |
| Polecenie i odpowiedzialność | Operator potrafi napisać następne polecenie i rozróżnić analizę, zgodę na wykonanie zmiany oraz odbiór. |
| Zachowanie historii | W stanie zmiany po odbiorze operator rozróżnia wcześniejszy odebrany zakres od nowej pracy. |

Ocena na podstawie odpowiedzi operatora w trzech scenkach; zapis rzeczywistych odpowiedzi i konkretnych niejasności. Jeśli potrzebna będzie podpowiedź wyjaśniająca brak na karcie, odnotować ją jako problem widoku, poprawić ten sam materiał i ponownie sprawdzić dotknięty przypadek. Brak progów czasu, procentów i domniemania akceptacji na podstawie uprzejmego potwierdzenia.

**Dwa pozostałe kroki po uzgodnieniu:** (1) agent przygotowuje kompletną, zwartą kartę i jej trzy stany, uwzględniając krótkie rozróżnienie mechanizm/analiza/decyzja; (2) wspólna próba odczytu, zapis wyniku i jawna decyzja operatora, czy karta wystarcza, czy wymaga wskazanej poprawki. Zamykamy wątek po spełnieniu uzgodnionych kryteriów i przyjęciu koncepcji przez operatora; szerszy pilot wymaga osobnego zakresu.

**Decyzja oczekująca:** czy przyjąć powyższy cel, granicę i sprawdzian. Rekomendacja agenta: przyjąć. Powód: zamienia serię objaśnień w ograniczoną próbę użyteczności. Alternatywa: zmienić oczekiwany rezultat przed dalszą lekcją. Właściciel decyzji: użytkownik; agent nie traktuje braku odpowiedzi jako zgody. Właściciel przygotowania karty po decyzji: agent. Nie dopisywać nowych tematów automatycznie.

## 12. Przyjęcie kryteriów i materiał do próby odczytu

**Decyzja użytkownika, 2026-11-07: „1a”.** Przyjęto wariant A z odpowiedzi po §11: jedna karta, trzy sytuacje oraz sprawdzenie użyteczności według czterech kryteriów z §11. Historyczna propozycja pozostaje zachowana. To zgoda na przygotowanie i przeprowadzenie ćwiczenia, nie odbiór karty, zmiana reguł TextStats ani zlecenie implementacji/pushu/commita.

**Plan ograniczony:** materiał dla trzech stanów przygotowany poniżej; odczyt użytkownika trwa od stanu 1. Po zapisaniu odpowiedzi dla wszystkich stanów agent rozlicza kryteria i przedstawia wynik do jawnej oceny operatora. W razie niejasności poprawia tę samą kartę i ponawia dotknięty przypadek. Nie dodaje kolejnej lekcji lub funkcji.

### Zasady próby

Operator otrzymuje jeden stan naraz. Prosimy o krótkie określenie sytuacji oraz wiadomość do agenta. Nie wymagamy pamiętania ID, historii rozmowy ani nomenklatury ISO. Odpowiedź „nie wiem, bo na karcie brakuje…” jest użyteczną obserwacją, nie błędem użytkownika.

Każda karta jest opracowaniem historycznego zapisu symulacji F5. Żadna nie potwierdza uruchomienia TextStats. Stan 3 korzysta z rzeczywistej propozycji fabuły F5 (spacja nierozdzielająca), a nie z wcześniejszej hipotetycznej półpauzy. Wszelkie odpowiedzi w próbie dotyczą ćwiczenia, nie wykonują poleceń w silniku.

### Stan 1 z 3 — korekta przed odbiorem

**TextStats · Liczenie słów · Symulacja**

| Pole karty | Treść |
|---|---|
| Cel zmiany | Myślnik rozdziela słowa: `biało-czerwony` ma dać `2`. |
| Co przygotowano | Nową regułę, przypadek testowy i oznaczoną wersję programu. Zgoda na wykonanie tej zmiany została wcześniej udzielona w fabule. |
| Przegląd reguły | PASS dla reguły w rewizji 2. |
| Przegląd przypadku | FAIL: przypadek w rewizji 2 nadal oczekuje `1`. Wymaga korekty wobec nowej reguły. |
| Zapis wykonania | PASS dla przypadku 2 i programu 2. To fikcyjny zapis; TextStats nie uruchomiono. |
| Odbiór | Brak. Nierozliczone zastrzeżenie do przypadku. |
| Następny krok / właściciel | Agent: rozliczyć zastrzeżenie, przygotować potrzebną poprawkę i nowe sprawdzenia w uzgodnionym zakresie. |

Podstawa autora: [05-fail](../flowable-trial/evidence/f5-restart/05-fail.json.md), sprawa 7, stan 4: CAP-01@2, AT-01@2, CODE-01@2, oczekujące prepare. Nazwy dla operatora zastępują konieczność czytania ID, ale zachowano dokładne referencje do źródła.

**Pytanie do operatora:** patrząc tylko na tę kartę, co jest już przygotowane, czego brakuje do odbioru i jaką wiadomość napisałbyś teraz do agenta? Wystarczą 2–3 zdania. Jeżeli karta czegoś nie wyjaśnia, wskaż ten brak.

### Stan 2 z 3 — podstawa przygotowana do decyzji w fabule

**TextStats · Liczenie słów · Symulacja**

| Pole karty | Treść |
|---|---|
| Cel zmiany | Myślnik rozdziela słowa: `biało-czerwony` ma dać `2`. |
| Co przygotowano | Regułę w rewizji 2, poprawiony przypadek i program w rewizji 3. |
| Przeglądy | PASS reguły 2 i przypadku 3; poprawiony przypadek oczekuje `2`. Wcześniejszy FAIL przypadku 2 pozostaje historyczny. |
| Zapis wykonania | PASS dla przypadku 3 i programu 3. To fikcyjny zapis; TextStats nie uruchomiono. |
| Odbiór | Jeszcze nie nastąpił. Pozytywne kontrole nie są decyzją operatora. |
| Następny krok / właściciel | Operator: ocena podstawy i decyzja o odbiorze tego zakresu i wersji w fabule albo wskazanie zastrzeżenia. Agent może wyjaśnić zapis. |
| Granica dowodu | Karta pozwala ćwiczyć decyzję procesową; nie pozwala potwierdzić działania rzeczywistego programu. |

Podstawa autora: [07-show](../flowable-trial/evidence/f5-restart/07-show.json.md), sprawa 7, stan 6: CAP-01@2, AT-01@3, CODE-01@3, oczekujące accept.

**Pytanie do operatora:** co zmieniło się w podstawie oceny, co nadal pozostaje Twoją decyzją i czego nie wolno uznać za dowiedzione? Napisz wiadomość, którą skierowałbyś teraz do agenta. To ćwiczenie, nie rzeczywisty odbiór produktu.

### Stan 3 z 3 — propozycja po wcześniejszym odbiorze

**TextStats · Liczenie słów · Symulacja**

| Pole karty | Treść |
|---|---|
| Dotychczasowy zakres | Myślnik rozdziela słowa. Przyjęto w fabule regułę 2, przypadek 3 i program 3. |
| Nowa propozycja | Także spacja nierozdzielająca ma rozdzielać słowa; propozycja reguły w rewizji 3. |
| Co pozostaje aktualne historycznie | Wcześniejszy odbiór i wyniki dotyczą poprzedniego zestawu, nie nowej propozycji. |
| Stan nowej pracy | Nowa sprawa powiązana z poprzednią. Brak zgody na zastosowanie nowej propozycji; wykonanie nie rozpoczęło się. |
| Podstawa oceny nowego zachowania | Nie przedstawiono nowych testów ani wykonań potwierdzających obsługę spacji nierozdzielającej. Widoczne PASS odnoszą się do starej podstawy i są symulowane. |
| Następny krok / właściciel | Operator rozstrzyga zakres. Agent może wcześniej analizować wpływ i przygotować propozycję; nie może uznać poprzedniego odbioru za zgodę na rozszerzenie. |

Podstawa autora: [10-show](../flowable-trial/evidence/f5-restart/10-show.json.md), zakończona sprawa 7 i nowa 10007 / stan 0. Propozycja CAP-01@3 nie zastępuje jeszcze bieżącego CAP-01@2.

**Pytanie do operatora:** co pozostaje odebrane, czego nie obejmuje poprzedni odbiór i co teraz zlecisz agentowi? Wskaż, czy Twoja wiadomość zleca analizę, czy pozwala wykonać zmianę.

### Granice mechanizmu w tych kartach

Prototyp F5 wykazał wybrane zachowania: powiązanie ocen z rewizjami, zadania oczekujące, zachowanie historii i przejście do kolejnej sprawy. Treści ocen, wyniki wykonań i role są fikcyjne. Analiza sensu reguł i testów nie wynika z silnika; rzeczywista decyzja operatora nie powstaje przez zapisanie pola PASS. Karty są redakcją agenta na podstawie eksportów, nie nowym automatycznie generowanym widokiem.

### Rejestr obserwacji próby

| Stan | Odpowiedź użytkownika | Dopowiedzenia / korekty karty | Wynik kryteriów |
|---|---|---|---|
| 1 | Wersja 1: niejasne pola (§13). Po wersji 2, 2026-11-08: „Ja napisalbym: kontynuuj i napraw test” | Zmieniono prezentację (§14); po drugim pokazaniu U podał adekwatne polecenie | Wykazano wybór następnej pracy i poprawne polecenie. Pełnego rozumienia podstawy dowodowej nie wnioskujemy z tej krótkiej odpowiedzi; odbiór koncepcji pozostaje otwarty |
| 2 | Najpierw U: „Slabo wiem co mam zrobic w tyj sytucacji.” (§17); po ponowieniu z rekomendacją U: „1a” (§19) | Dodano konkretny wniosek i rekomendację z ograniczeniem do fabuły | U podjął decyzję w ćwiczeniu. Nie wnioskujemy pełnego rozumienia wszystkich kryteriów z samej zgody |
| 3 | U: „tak jasne”, 2026-11-08, w odpowiedzi na pytanie o zachowany odbiór i brak potrzebnej teraz zgody na rozszerzenie | Bez dalszej korekty | U potwierdził czytelność tego rozróżnienia; końcowa decyzja o koncepcji osobno w §20 |

Końcowa ocena koncepcji: nieprzeprowadzona. Samo przygotowanie materiału nie zamyka ćwiczenia.

## 13. Pierwsza obserwacja użytkownika i korekta konstrukcji kart

2026-11-07. **Wynik próby stanu 1: potrzebna poprawka karty; nie zaliczamy orientacji ani rozumienia podstawy oceny.** Operator zgłosił niejasność etykiet, zamiast otrzymać samowystarczalny widok. Pozostałe kryteria nie zostały ocenione. Nie jest to ocena kompetencji operatora.

Wypowiedź użytkownika, verbatim:

> pierwsze wrazenie mam takie ze pola karty sa dla mnie niejasne. Ja jestem amatorem ty masz dostep do wiedzy treningowej oraz ISO. "Przeglad reguly" co to znaczy? Jaka praca zostaa tu wykonana pod spodem? Tak samoe Przeglad przypadku", Zapis wykonania. Czy jak bedziemy mieli karte projekt GUI czy stworzenie tabeli w bazie danych to pola karty sie zmienia? Czy mozemy mowic na kartach jezykiem developara, testera, PO/PM? Czy znasz jakies wzory kart albo zalecenia jak je tworzyc i czego nie robic? Moze inne normy, workbooki o tym pisza? /Users/michal/PycharmProjects/docs/sources

### 13.1 Diagnoza i znaczenie dotychczasowych pól

Agent pokazał etykiety wewnętrznych ocen zamiast nazw wykonywanych czynności i wniosków. Karta nie wyjaśniała również, czy jest kartą funkcji, zadania czy raportem kontroli. To błąd prezentacji i granulacji. Zamiana FAIL na „niepowodzenie” sama go nie usuwa.

| Dotychczasowa etykieta | Praca, którą powinna oznaczać w rzeczywistym projekcie | Co rzeczywiście wiadomo z F5 |
|---|---|---|
| Przegląd reguły | Analityk/developer sprawdza opis wymagania względem potrzeby i pozostałych ustaleń: czy jest jednoznaczny, spójny, możliwy do sprawdzenia; zapisuje zastrzeżenia i wynik. To analiza treści, nie uruchomienie programu. | Zapisano symulowaną ocenę wymagania. Nie wykazano przeprowadzenia takiego rzeczywistego przeglądu. |
| Przegląd przypadku | Tester/recenzent sprawdza wejście, oczekiwany wynik i kroki testu względem wskazanej wersji wymagania. Np. oczekiwane 1 jest sprzeczne z nową regułą wymagającą 2. | Zapisano fikcyjny FAIL, a treść przypadku w eksporcie faktycznie nadal oczekuje 1. |
| Zapis wykonania | Uruchomienie testu na wskazanej wersji programu i danych, porównanie wyniku rzeczywistego z oczekiwanym; zachowanie logu oraz informacji o istotnym środowisku. | Zapisano fikcyjny PASS. Nie uruchamiano TextStats; nie wolno dopisać domniemanego rzeczywistego wyniku lub logu. |

Nazwy ról opisują kompetencje/perspektywy; nie ustanawiają dodatkowych osób ani niezależności recenzenta. Karta powinna pozwalać rozwinąć zapis: kto, co i na jakiej podstawie sprawdził, dla jakiej wersji, z jakimi ustaleniami oraz gdzie jest wynik. Brak danych ma być widoczny.

### 13.2 Źródła: wzory, wytyczne i ich granice

Odczyt lokalnych źródeł w docs/sources oraz dokumentacji producentów, 2026-11-07. To wybór źródeł do konkretnej korekty, nie pełny przegląd kolekcji. Nie importujemy do małego zespołu pełnego reżimu NASA.

| Źródło i miejsce | Co rzeczywiście wnosi | Zastosowanie / granica |
|---|---|---|
| [ISO, SI.02.04, SI.03.06–08 i SI.05.04](../../../../iso-29110-5-1/chapters/07-software-implementation-si-process.md); [§9, tabele 32 i 35](../../../../iso-29110-5-1/chapters/09-description-of-work-products.md) | Oddziela sprawdzenie treści wymagań, przygotowanie/weryfikację przypadków oraz wykonanie testów. Opisuje rekordy wyników testów i weryfikacji. | Źródło znaczenia czynności, nie nakaz nazw pól naszego interfejsu. Nie wszystkie wyniki jakości są wynikiem uruchomienia programu. |
| [NASA-STD-8739.8A, lokalny tekst](../../../../docs/sources/nasa-8739-8a.txt), tabela §5.3.2–5.3.3 / SWE-087–088, s. 42; §4.5.2 / SWE-065b,c, s. 35 | Wymagania w kontekście NASA: przeglądy różnych produktów, kryteria wejścia/wyjścia, listy kontrolne, rozliczenie ustaleń; osobno procedury i raporty testów. | Wzorzec treści dowodu i doboru sprawdzenia, nie gotowy formularz feature/task ani obowiązek narzucany temu projektowi. |
| [NASA SWEHB, SWE-087 §3.4](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695472/SWE-087%2B-%2BSoftware%2BPeer%2BReviews%2Band%2BInspections%2Bfor%2BRequirements%2BPlans%2BDesign%2BCode%2Band%2BTest%2BProcedures); [archiwum checklist NASA Langley](https://sw-eng.larc.nasa.gov/supporting-products/archive-of-supporting-materials/) | Wskazówki do organizowania przeglądów oraz dostępne przykłady list kontrolnych. | Checklistę dobieramy do przedmiotu; sama nazwa „review” nie opisuje zakresu pracy. Archiwalnych przykładów nie traktujemy jako aktualnego obowiązku. |
| [Volere-template_pl.pdf](../../../../docs/sources/Volere-template_pl.pdf), wersja 14, s. 5–6, „Karta wymagania”; [strona autorów](https://www.volere.org/templates/) | Konkretny wzór pojedynczego wymagania: opis, uzasadnienie, źródło/właściciel, kryterium spełnienia, powiązania i historia. Obejrzano także grafikę formularza na s. 6. | Pomaga opisać wymaganie; nie zastępuje karty zadania ani raportu testu. Nie kopiujemy wszystkich pól do widoku operatora. |
| [IREB CPRE Foundation syllabus 3.3.0](../../../../docs/sources/cpre_foundationlevel_syllabus_en_v.3.3.0.pdf), §3.1.1–3.1.6 i §3.2, s. 20–23 | Wytyczne edukacyjne: typ produktu pracy i szczegółowość dobrane do celu, odwołania zamiast duplikacji, spójne pojęcia, rozdzielenie poziomów abstrakcji, unikanie niepełnych opisów i niekonkretnych rzeczowników. | Bezpośrednia podstawa do korekty niejasnych etykiet; nie norma zgodności ani gotowa karta wszystkich rodzajów pracy. |
| [Microsoft: typy work items Azure Boards](https://learn.microsoft.com/en-us/azure/devops/boards/work-items/about-work-items?view=azure-devops); [planowanie i śledzenie pracy](https://learn.microsoft.com/en-us/azure/devops/boards/get-started/plan-track-work?view=azure-devops) | Dokumentacja narzędzia rozróżnia poziomy pracy i typy elementów, m.in. wymagania/user stories i tasks. | Znany użytkownikowi wzorzec rozdzielenia funkcji od zadań technicznych. Nie dowodzi skuteczności naszego procesu i nie narzuca terminologii NASA/ISO w UI. |

### 13.3 Minimalna korekta — wspólna struktura, treść odpowiednia do pracy

**Decyzja agenta w granicach uzgodnionej poprawy karty:** zachować stały szkielet, zmienić treść sekcji „Prace i wyniki”. Nie dodawać nowego modelu, narzędzia ani obowiązkowych formularzy. Stałe informacje: rodzaj i nazwa pracy; cel i zakres; co ma powstać i jak poznamy zakończenie; wykonane prace i wyniki; pozostałe prace/blokady; właściciel następnego kroku i potrzebna decyzja. ID i rewizje pozostają w odnośnikach/szczegółach; w podsumowaniu używamy zrozumiałych wersji i nazw.

Karta funkcji pokazuje obiecane zachowanie i podsumowuje powiązane zadania. „Zaprojektuj GUI” oraz „utwórz tabelę” są zazwyczaj zadaniami dostarczającymi wynik potrzebny funkcji. Karty zadania nie udają, że sam ich wynik jest już działającą funkcją. To rozróżnienie widoków tych samych informacji, nie zlecenie budowy nowej hierarchii danych.

| Przedmiot | Wynik pracy | Przykładowa czynność sprawdzająca / dowód |
|---|---|---|
| Projekt GUI | Makieta ekranu i opis jego stanów | Przejście scenariusza użytkownika po makiecie; zapis zauważonych braków i decyzji. Dodatkowe kontrole np. dostępności zależnie od potrzeb. Nie jest to test wdrożonego ekranu. |
| Tabela w bazie | Uzgodniony schemat oraz migracja | Przegląd modelu danych; uruchomienie migracji na bazie testowej, sprawdzenie ograniczeń i wpływu na istniejące dane, jeśli występują; odpowiednie logi/testy. Nie dowodzi działania całej funkcji. |
| Reguła liczenia słów | Implementacja uzgodnionego zachowania | Przegląd przykładów, testy reguły i integracji z wejściami; wyniki powiązane z wersją programu. |

Kontrole są przykładami zależnymi od zakresu i ryzyka, nie nową listą obligatoryjną. PO/PM widzi efekt, zakres, blokady i decyzje; developer — zadania, kontrakty i zmiany; tester — przypadki, środowisko, wykonania i błędy. Wszystkie perspektywy odwołują się do tych samych rekordów, nie utrzymują trzech osobnych prawd.

**Czego unikać:** jednego formularza pełnego N/A; nazw typu „przegląd” bez przedmiotu i wyniku; PASS bez podstawy; mieszania wykonania zadania z odbiorem funkcji; duplikowania statusów i dowodów; przypisywania jakości na podstawie samego istnienia linku. Przegląd całego zbioru materiałów, pełne workflow GUI/bazy i nowe karty projektowe są poza aktualnym ćwiczeniem.

## 14. Karta po korekcie — wersja tekstowa 2

Materiał do ponownego sprawdzenia. Pierwsza wersja i obserwacja pozostają w §12–13. Poniższe trzy stany odnoszą się do tych samych eksportów F5. To zmiana prezentacji, nie nowe wyniki wykonania.

### Stan 1 — test oczekuje niewłaściwego wyniku

**TextStats — zmiana liczenia słów. Symulacja, nie uruchomiony produkt.**

**Chcemy uzyskać:** dla `biało-czerwony` wynik 2. Wykonanie tej zmiany ma zgodę w fabule; odbioru jeszcze nie ma.

| Prace i wyniki | Co wiadomo |
|---|---|
| Sprawdzono opis nowego zachowania | W fabule zapisano pozytywną ocenę opisu. Nie ma dowodu rzeczywistej pracy recenzenta. |
| Sprawdzono, czy test oczekuje wyniku zgodnego z opisem | Przypadek nadal oczekuje 1, chociaż opis mówi 2. Zapisano zastrzeżenie wymagające poprawki. |
| Uruchomienie programu | Nie wykonano w tej próbie. Fikcyjny PASS dotyczy starego oczekiwania w przypadku 2 i programu 2; nie dowodzi poprawnego liczenia słów. |

**Pozostała praca:** agent ma poprawić przypadek, ustalić potrzebną poprawkę programu i przedstawić nowe sprawdzenia. Poprawność rzeczywistego programu pozostaje niewykazana. W fabule nie ma podstaw do odbioru z nierozliczonym zastrzeżeniem.

**Od Ciebie teraz:** możesz zlecić agentowi rozliczenie zastrzeżenia w uzgodnionym zakresie lub poprosić o wyjaśnienie. Nie jest potrzebna ponowna zgoda na ten sam zakres, a odbiór nie został jeszcze dokonany. Podstawa: 05-fail, sprawa 7 / stan 4.

### Stan 2 — poprawiono test; w fabule czekamy na decyzję

**TextStats — zmiana liczenia słów. Symulacja, nie uruchomiony produkt.**

**Chcemy uzyskać:** dla `biało-czerwony` wynik 2.

| Prace i wyniki | Co wiadomo |
|---|---|
| Sprawdzono opis zachowania | W fabule ocena opisu 2 pozostaje pozytywna. |
| Poprawiono i ponownie sprawdzono przypadek testowy | Przypadek 3 oczekuje 2; zapisano pozytywną ocenę. Zastrzeżenie do przypadku 2 zachowano w historii. |
| Uruchomienie programu | Nie wykonano w tej próbie. Zapisano fikcyjny PASS dla przypadku 3 i programu 3. |

**Pozostała praca / decyzja:** w fabule operator ocenia zakres, wersję i zapisane wyniki, a następnie przyjmuje wynik lub wskazuje zastrzeżenie. W rzeczywistym projekcie te fikcyjne oceny nie wystarczają do potwierdzenia działania programu.

**Od Ciebie teraz:** decyzja procesowa w ćwiczeniu lub prośba o wyjaśnienie podstawy; nie rzeczywisty odbiór TextStats. Podstawa: 07-show, sprawa 7 / stan 6.

### Stan 3 — stary zakres przyjęty; nowe zachowanie dopiero proponowane

**TextStats — rozszerzenie liczenia słów. Symulacja, nie uruchomiony produkt.**

**Dotychczas przyjęto w fabule:** obsługę myślnika, opis 2 / przypadek 3 / program 3.

**Nowa propozycja:** także spacja nierozdzielająca ma rozdzielać słowa.

| Prace i wyniki | Co wiadomo |
|---|---|
| Zachowano poprzedni odbiór | Dotyczy obsługi myślnika i poprzedniego zestawu wersji. |
| Zapisano propozycję rozszerzenia | Nie ma zgody na wykonanie nowego zakresu; implementacja nie rozpoczęła się. |
| Sprawdzenie nowego zachowania | Brak nowych testów i wykonań. Dawne pozytywne zapisy go nie obejmują. |

**Pozostała praca / decyzja:** agent może przeanalizować wpływ i przedstawić propozycję; operator rozstrzyga, czy rozszerzyć zakres. Nie przeprowadzamy ponownego odbioru starej pracy tylko dlatego, że pojawił się pomysł.

**Od Ciebie teraz:** zlecenie analizy lub jawna decyzja o rozszerzeniu, z rozróżnieniem obu. Podstawa: 10-show, sprawa 7 zakończona i nowa 10007 / stan 0.

### Ponowna próba

Wersja 2 przygotowana; nie została jeszcze oceniona przez operatora. Nie przechodzimy do stanu 2, dopóki stan 1 nie będzie czytelny. Zwięzła prezentacja w rozmowie powinna zachować sens wykonanej czynności i jawność symulacji. Kryteria z §11 pozostają bez zmian; poprawka nie rozpoczyna nowego projektu.

## 15. Tożsamość pól, model danych i kontrola wpływu zmian

2026-11-07. Użytkownik polecił kontrolować wpływ rozważanych zmian na wcześniejsze ustalenia oraz asertywnie odradzać propozycje niespójne lub o dużym wpływie. Polecenie dotyczy sposobu współpracy; nie jest zgodą na zmianę modelu ani implementacji.

### 15.1 Stan faktyczny po odczycie kodu

Nie zapomniano o identyfikacji danych, ale nie ukończono kontraktu danych nowej karty operatora. §8 opisuje ID i rewizje elementów. Prototyp F5 ma konkretne struktury:

- [ArtifactRef](../flowable-trial/src/main/java/org/example/processlab/domain/ArtifactRef.java): `id`, `revision`.
- [ReviewRecord](../flowable-trial/src/main/java/org/example/processlab/domain/ReviewRecord.java): `id`, `subject`, `basis`, `outcome`, `rationale`.
- [TestRunRecord](../flowable-trial/src/main/java/org/example/processlab/domain/TestRunRecord.java): `id`, `testCase`, `software`, `outcome`.
- [WorkflowChecks](../flowable-trial/src/main/java/org/example/processlab/workflow/WorkflowChecks.java): wyliczane pozycje `requirementReview`, `testReview`, `testExecution`, zwracające CheckStatus. Ich status nie jest tym samym polem co outcome pojedynczego rekordu; agregacja i aktualność należą do reguł.

To model wąskiej próby. TestRunRecord nie przechowuje pełnego logu, środowiska ani danych rzeczywistego wykonania, a ReviewRecord nie ma pełnego opisu metody/checklisty i tożsamości recenzenta. Nie przedstawiamy go jako kompletnego modelu operacyjnych dowodów. Karta tekstowa i makieta nie są z tym modelem zintegrowane.

### 15.2 Cztery odrębne rzeczy

| Warstwa | Przykład | Reguła |
|---|---|---|
| Etykieta dla człowieka | „Wynik sprawdzenia testu” | Może zmieniać brzmienie bez zmiany znaczenia danych. |
| Pole w określonym typie rekordu | `ReviewRecord.outcome` | Ma ustalone znaczenie i typ; nie jest identyfikatorem konkretnego przeglądu. |
| Tożsamość konkretnego zapisu | `ReviewRecord.id` | Rozróżnia jedno sprawdzenie od innego. |
| Referencja do ocenianej treści | `subject = AT-01@2` | Wiąże ocenę z konkretną wersją przedmiotu. |

Nie trzeba przydzielać każdej etykiecie w interfejsie osobnego ID domenowego. Nazwy pól mogą powtarzać się w różnych typach (`id`, `outcome`), jeśli typ i struktura określają ich znaczenie. Stabilne klucze zapisów nie zależą od polskiej etykiety ani od tego, kto ogląda kartę.

Przed implementacją karty potrzeba małego kontraktu jej danych: pole widoku → źródło lub sposób wyliczenia → typ/znaczenie → referencja i zasada aktualności. Osobno określamy pola edytowalne i wyliczane. Pole bez źródła nie może udawać danych z systemu; na karcie pokazujemy brak, a propozycję rozszerzenia modelu analizujemy osobno. Nie planujemy teraz uniwersalnego kreatora formularzy, schematu całego ISO ani migracji F5.

### 15.3 Ocena wpływu bieżącej korekty

- **Zmiana języka karty:** wpływa na prezentację. Powinna zachować tożsamość rekordów, znaczenie wyników i kryteria odbioru. Przepisywanie kluczy danych z powodu zmiany polskich nagłówków byłoby nieuzasadnione.
- **Rozróżnienie funkcji od zadania oraz przykłady GUI/bazy:** pomaga wyjaśnić widok, ale nie oznacza, że prototyp już obsługuje te typy i całe ich workflow.
- **Rzeczywista obsługa nowych rodzajów pracy/dowodów:** potencjalnie zmienia model, reguły, testy, historię i migrację. To duży zakres wymagający osobnego uzasadnienia i zgody; agent odradza włączanie go do obecnej próby czytelności.
- **Obecny zakres i kryteria:** jedna karta TextStats, trzy stany, ocena czytelności; bez zmian. Wersja 2 nadal nieprzyjęta.

Zasada na dalszą pracę: dla rozważanej zmiany agent ustala, czy dotyczy prezentacji, danych, reguł procesu czy zakresu produktu; identyfikuje dotknięte wcześniejsze ustalenia, zależne artefakty i potrzebną kontrolę. Przy nieustalonym wpływie nie zapewnia, że zmiana jest lokalna. Dla sprzeczności lub dużego kosztu przedstawia jasne odradzenie i najmniejszą alternatywę. Nie rozbudowuje automatycznie ćwiczenia ani nie wymaga ponownej zgody na zmianę wyłącznie redakcyjną w już uzgodnionym zakresie poprawy karty.


## 16. Próba odczytu: odpowiedź po poprawieniu stanu 1

2026-11-08. Odpowiedź użytkownika verbatim:

> Ja napisalbym: kontynuuj i napraw test

Odczyt agenta: adekwatne polecenie dalszej pracy w zakresie już zatwierdzonym w fabule. Wskazuje naprawę testu, nie odbiór, nowy zakres ani zgodę na rzeczywistą implementację podczas ćwiczenia. Nie wymagamy od operatora ponownego wypisania identyfikatorów, reguły i technicznych kroków obecnych w karcie. Agent odpowiada za naprawę testu zgodnie z wymaganiem, a nie dopasowanie oczekiwań do błędnego programu, oraz za wskazanie wyników dalszych sprawdzeń.

Ta odpowiedź świadczy o możliwości wyboru sensownej następnej czynności. Sama nie wykazuje jeszcze wszystkich kryteriów: rozumienia wersji i granic dowodów ani zachowania historii po odbiorze. Nie wpisujemy pełnego PASS próby. Kontynuacja: stan 2 w wersji 2, z wyraźnym rozdzieleniem fikcyjnych wyników i decyzji operatora; bez nowych zagadnień i bez zmian kodu.

## 17. Stan 2: brak wskazania działania i analiza protokołu sztabowego

2026-11-08. Obserwacja użytkownika verbatim:

> Slabo wiem co mam zrobic w tyj sytucacji.

Użytkownik przedstawił pełną treść `cabinetry-wisdom/KONTRAKT.md`, wersja 1.2 z 2026-10-19, i poprosił o ocenę przydatności. Analiza dotyczy tekstu przekazanego w rozmowie; nie zmieniono tamtego repozytorium ani nie przyjęto jego uprawnień.

**Diagnoza:** karta stanu 2 zawierała dane i ostrzeżenie o symulacji, ale nie dawała gotowego wniosku oraz jednoznacznej rekomendacji. Pytanie „co napisałbyś teraz do agenta?” przenosiło ciężar opracowania kolejnego kroku na operatora. Dodatkowo odbiór w fabule i rzeczywisty odbiór programu były omawiane razem. Jest to kolejny problem komunikacji, nie dowód braku kompetencji użytkownika. Stan 2 niezaliczony; nie przechodzimy jeszcze do stanu 3.

### 17.1 Zgodność i różnice

| Element przytoczonego kontraktu | Ocena dla tego projektu |
|---|---|
| §2.1 zakończona praca sztabowa | Przydatne: agent przygotowuje uzasadniony następny krok, zamiast żądać od operatora samodzielnego wyprowadzenia go z tabeli. Nie usprawiedliwia ukrywania niewiadomych. |
| §2.2 działanie w granicach zamiaru | Zgodne z zaakceptowanym przez U delegowaniem technicznych środków. Nie trzeba prosić o ponowną zgodę na każdy krok już zleconej pracy. Granice zakresu, ryzyka i zobowiązań nadal obowiązują. |
| §2.3–2.5 wniosek, rekomendacja, jawne zatwierdzenie | Zgodne z potrzebą tej karty i dotychczasowym kontraktem rozmowy. Rekomendacja agenta nie staje się decyzją operatora. |
| §3 do-zbadania / blokujące / decyzja | Pomocne rozróżnienie pracy analitycznej od spraw rzeczywiście wymagających odpowiedzi U. Nie każda niewiadoma jest pytaniem do człowieka. |
| §3 z-domyslna | Nie przenosić automatycznie. Domyślny wybór roboczy może być dopuszczalny tylko w już upoważnionym zakresie; nie daje zgody na zmianę zakresu, akceptację ryzyka lub odbiór. |
| §3 paczki i automatyczne ponawianie | Niepotrzebne w obecnym ćwiczeniu jednej sprawy. Nie importować liczby 4 pytań ani eskalacji po 3 ponowieniach; brak odpowiedzi nie oznacza potrzeby nacisku ani akceptacji. |
| §4 pełny meldunek i liczniki bazy | Użyć krótkiej formy dobranej do decyzji. Liczniki bazy wiedzy nie opisują postępu oprogramowania i nie powinny być kopiowane na kartę. |
| §2.2 i §6 lokalny commit / stała zgoda na push | Uprawnienia konkretnego repozytorium; nie obowiązują tutaj przez przytoczenie dokumentu. |
| §6 ciągłość | Zbieżne z naszymi trwałymi zapisami; nie tworzyć nowej kopii rejestru ani nowego źródła prawdy. |

Istniejący kontrakt rozmowy U już wymagał gotowej rekomendacji i jednej sprawy. Lokalny kontrakt decyzji także wymaga rekomendowanej opcji i uzasadnienia. W tym ćwiczeniu agent zastosował formę odpytywania zamiast pomocy w wykonaniu zadania. Wdrożenie zupełnie nowego kontraktu nie jest konieczne do poprawienia tego zachowania. Sprzecznych lokalnych uprawnień nie rozstrzygamy przez milczące skopiowanie obcego dokumentu.

### 17.2 Rekomendacja: karta jako podstawa, meldunek jako pomoc w działaniu

Jedna odpowiedź operatora powinna mieć przed sobą:

1. Co jest gotowe albo czego brakuje — z odróżnieniem faktu od deklaracji.
2. Co agent rekomenduje zrobić i dlaczego.
3. Czy agent może wykonać to sam w obecnym zakresie, czy potrzebuje konkretnej decyzji.
4. Co oznacza odpowiedź operatora i jaki zakres/wersję obejmuje; brak zgody nie uruchamia zależnej pracy.

Karta nadal przechowuje lub pokazuje podstawę, powiązania i historię. Meldunek jest widokiem tych danych oraz jawnie oznaczoną rekomendacją agenta, nie drugim rejestrem statusów. W przyszłej implementacji rekomendację trzeba powiązać z podstawą i sprawdzać jej aktualność; nie udajemy, że obecna makieta robi to automatycznie.

**Przykład przyszłej prezentacji stanu 2, nie rzeczywiste pytanie decyzyjne w tej analizie:**

> Wniosek: w fabule poprawiono test, zapisane kontrole bieżących wersji są pozytywne; pozostał odbiór operatora.
>
> Rekomendacja: przyjąć w fabule zmianę „myślnik rozdziela słowa” dla reguły 2, przypadku 3 i programu 3. Uzasadnienie: zastrzeżenie do starego przypadku rozliczono, obecne oceny są pozytywne.
>
> Granica: to wyłącznie decyzja w ćwiczeniu; nie dowodzi działania TextStats i nie wykonuje operacji w silniku.
>
> Skutek przyjęcia: w scence ten zakres zostaje odebrany. Alternatywa: pozostawić odbiór otwarty i wskazać zastrzeżenie.
>
> Od Ciebie: „przyjmuję w ćwiczeniu” albo „nie przyjmuję: …”.

W realnym projekcie fikcyjne PASS oznaczałyby brak podstaw do odbioru działania programu. Agent powinien to stwierdzić oraz przygotować potrzebne sprawdzenie w upoważnionym zakresie; jeśli wykonanie wykracza poza niego, przygotować propozycję do decyzji. Nie ma automatycznej zgody na uruchomienie nowego pilota.

### 17.3 Wpływ na przyjęte ustalenia

Rekomendowana korekta mieści się w celu pomocy operatorowi: ta sama karta, trzy stany, te same fakty i kryteria. Zmienia sposób wsparcia: następny krok ma być opracowany przez agenta, a operator ma go rozumieć i rozstrzygać sprawy należące do niego. Krótkiego „zgoda” na podaną rekomendację nie traktować automatycznie jako dowodu rozumienia wszystkich kryteriów; przy końcowej ocenie zapisać, co rzeczywiście zaobserwowano, z uwzględnieniem udzielonej pomocy.

Odradzam wymianę kontraktu, wdrożenie rejestrów cabinetry-wisdom lub budowę nowego modelu danych w odpowiedzi na tę trudność. Koszt jest większy niż potrzebna poprawka. Nie zmieniono template/, uprawnień, schematów, kodu ani kryteriów. Kolejny krok pozostaje ponowną prezentacją stanu 2 z rekomendacją, bez przechodzenia automatycznie do stanu 3.


## 18. Ponowienie stanu 2 — gotowa rekomendacja do decyzji w ćwiczeniu

2026-11-08. Użytkownik zlecił „Dalej” po analizie §17. Przedstawiono poniższy meldunek. Brak odpowiedzi decyzyjnej; sam nakaz kontynuacji nie oznacza odbioru w fabule, odbioru produktu ani akceptacji koncepcji karty.

**Wniosek:** w scenariuszu zmiana jest przygotowana do odbioru. Agent rekomenduje przyjąć zakres „myślnik rozdziela słowa”, ponieważ poprawiony przypadek odpowiada wymaganiu, a zapisane oceny i wykonanie bieżących wersji są pozytywne.

Podstawa: opis wymagania w rewizji 2, przypadek testowy w rewizji 3 oczekujący wyniku 2 dla `biało-czerwony`, program w wersji 3; źródło 07-show. Wcześniejsze zastrzeżenie dotyczyło przypadku w wersji 2 i pozostaje w historii. Wszystkie oceny i wykonanie są symulowane. Nie twierdzimy, że TextStats rzeczywiście uruchomiono.

**Przedmiot decyzji 1 w tej wiadomości:** przyjęcie tej zmiany wyłącznie w fabule ćwiczenia.

- A) Przyjąć opisany zakres i zestaw wersji w ćwiczeniu.
- B) Pozostawić odbiór otwarty i wskazać zastrzeżenie.

Rekomendacja A. Skutek A: w narracji zakres odebrany, można przejść do stanu 3 — nowej propozycji po odbiorze. Skutek B: pozostaje otwarty i omawiamy konkretne zastrzeżenie. Odpowiedź nie wywołuje komendy silnika, nie akceptuje realnego programu ani automatycznie całej koncepcji karty. Od operatora: „1A” lub „1B: …”.

Kontrola wpływu: wyłącznie prezentacja już znanego stanu i jawna rekomendacja; bez nowych dowodów, zmian zakresu/kryteriów/modelu. Kryterium użyteczności nadal wymaga oceny rzeczywistej odpowiedzi i ewentualnych trudności, a krótka zgoda nie dowodzi samodzielnego rozumienia wszystkich aspektów.

## 19. Przyjęcie w fabule i ostatni stan karty

2026-11-08. Użytkownik odpowiedział **„1a”** na decyzję z §18. Przyjęto wyłącznie w ćwiczeniu zakres „myślnik rozdziela słowa”, opis wymagania 2 / przypadek 3 / program 3. Nie uruchomiono komendy ACCEPT, nie zmieniono bazy Flowable, nie odebrano rzeczywistego programu ani koncepcji karty. Odpowiedź zachowuje znaczenie ograniczone w przedstawionym pytaniu.

### Stan 3 z 3 — po odbiorze pojawia się nowa propozycja

**Wniosek:** poprzedni zakres pozostaje odebrany w fabule. Nowy pomysł nie jest jeszcze gotowy do decyzji o wykonaniu; agent powinien najpierw przygotować analizę wpływu i konkretną propozycję.

| Informacja dla operatora | Treść |
|---|---|
| Już odebrane w ćwiczeniu | Myślnik rozdziela słowa; wskazany zestaw wersji 2 / 3 / 3. |
| Nowa propozycja | Także spacja nierozdzielająca ma rozdzielać słowa. |
| Co potwierdzają dawne wyniki | Wyłącznie wcześniejszą podstawę w symulacji. Nie potwierdzają nowego zachowania. |
| Czego brakuje do decyzji o wykonaniu | Rozpoznania wpływu na regułę, przypadki i kod oraz gotowej propozycji zakresu i sprawdzeń. |
| Następna praca agenta | Przeanalizować wpływ i przygotować propozycję; bez wdrażania rozszerzenia ani naruszania poprzedniego odbioru. |

**Rekomendacja:** nie zatwierdzać jeszcze wykonania rozszerzenia. Najpierw agent przygotowuje materiał, który pozwoli świadomie zdecydować. Zwykła analiza w upoważnionych granicach nie wymaga ponownej zgody operatora; zmiana zakresu już jej wymaga. W tym ćwiczeniu opisujemy tę odpowiedzialność, nie rozpoczynamy rzeczywistej analizy kodu ani nowej implementacji.

**Od operatora na tym etapie procesu:** żadna dodatkowa decyzja o produkcie. Nie trzeba wymyślać agentowi planu ani ponownie odbierać starego zakresu. Źródło modelowanego stanu: 10-show (sprawa poprzednia 7 i nowa 10007), z jawną granicą fikcyjnych wyników i decyzji.

### Domknięcie próby koncepcji — propozycja oceny, nie automatyczne zaliczenie

Przedstawiono trzy stany. U zgłosił niejasne etykiety w stanie 1 i brak wskazania działania w stanie 2; obie obserwacje doprowadziły do korekt. Po poprawce stanu 1 U wskazał sensowne polecenie naprawy. Po meldunku stanu 2 U podjął zaproponowaną decyzję w fabule. Nie przeprowadzono niezależnego testu rozumienia wszystkich referencji i wersji; krótka zgoda nie stanowi takiego dowodu. Stan 3 przedstawiono z rozdzieleniem starego zakresu i nowej pracy, ale ocena jego zrozumiałości przez U jeszcze nie nadeszła.

Oczekiwana końcowa informacja od operatora: czy sposób prezentacji (karta z nazwami prac + wniosek + rekomendacja + konkretna decyzja albo „nic od Ciebie”) wystarcza jako koncepcja do dalszego pilota, czy wymaga wskazanej poprawki, szczególnie w stanie 3. Nie deklarować jeszcze pełnego spełnienia kryteriów ani odbioru użyteczności F5. Następny krok pozostaje oceną tej próby, nie implementacją UI, przeprowadzeniem nowej zmiany TextStats lub rozbudową modelu.


## 20. Wynik próby trzech stanów i końcowy wniosek

2026-11-08. Odpowiedź użytkownika na pytanie dotyczące stanu 3, verbatim:

> tak jasne

Dotyczyła zrozumiałości zachowania poprzedniego odbioru oraz tego, dlaczego agent najpierw przygotowuje analizę bez żądania decyzji o wykonaniu rozszerzenia. Nie utożsamiamy jej automatycznie z zatwierdzeniem całej implementacji lub procesu.

| Kryterium §11 | Zebrana obserwacja i granica |
|---|---|
| Orientacja | Pierwsza karta nieczytelna; po zmianie etykiet na czynności U wskazał naprawę testu jako następny krok. To wynik wspomaganej próby na znanym przykładzie. |
| Podstawa oceny | Karty pokazują przedmiot/wersje i jawnie oznaczają fikcyjne wyniki. U zaakceptował decyzję w fabule po gotowej rekomendacji. Brak osobnego dowodu, że sam rozpoznaje wszystkie nieaktualne lub niewystarczające dowody; nie deklarujemy takiego wyniku. |
| Polecenie i odpowiedzialność | U podał polecenie naprawy, następnie „1a” na konkretną rekomendację odbioru w ćwiczeniu. Otwarta forma „co zrobisz?” okazała się niewystarczająca; przygotowana rekomendacja umożliwiła decyzję. |
| Zachowanie historii | U jawnie potwierdził czytelność rozdzielenia odebranego zakresu i nowej propozycji w stanie 3. To potwierdzenie użytkownika, nie niezależny test transferu do nowego projektu. |

**Wniosek agenta:** wspomagane przejście trzech stanów jest wykonane; koncepcję „czytelna karta + wniosek/rekomendacja + konkretna decyzja albo brak potrzebnej decyzji” warto przyjąć do dalszej pracy jako wzorzec komunikacji. Nie stwierdzamy niezależnego wykazania wszystkich umiejętności z kryteriów ani gotowości produkcyjnego narzędzia. Brak takiego dowodu jest jawny przy decyzji; nie zmieniamy po cichu kryteriów na samo istnienie dokumentacji.

**Końcowa decyzja do U (oczekuje):** A — przyjąć poprawioną koncepcję karty i meldunku jako rezultat tego ograniczonego ćwiczenia, z opisanymi granicami obserwacji; B — wskazać konkretną poprawkę przed przyjęciem. Rekomendacja A: pozwoliła wybrać działanie i podjąć decyzję bez samodzielnego projektowania kroków przez operatora. Przedmiotem nie są implementacja UI, model całego ISO, rzeczywisty TextStats ani automatyczne uruchomienie następnego pilota.

Po A: zapisać decyzję i zamknąć wątek oceny koncepcji; zakres następnych prac nie wynika automatycznie z tej zgody. Po B: poprawić wskazany punkt i ponowić dotknięty przypadek. Nie wracać do serii nowych lekcji. Właściciel końcowej decyzji: użytkownik. Właściciel zapisu wyniku: agent.


## 21. Końcowe przyjęcie koncepcji — wątek zamknięty

2026-11-08. Użytkownik odpowiedział verbatim:

> 1a

Odpowiedź dotyczyła końcowej decyzji z §20: **przyjąć poprawioną koncepcję karty i meldunku jako rezultat ograniczonego ćwiczenia, z opisanymi ograniczeniami próby**. Wątek oceny koncepcji jest zamknięty. Historyczne propozycje, pytania i następne kroki w §1–20 pozostają zapisem przebiegu; nie są nadal otwartymi zleceniami.

Przyjęty rezultat:

- Karta przedstawia cel, zakres, konkretne prace i wyniki, podstawę oceny oraz pozostałą pracę.
- Meldunek agenta przedstawia wniosek, uzasadnioną rekomendację i jedną konkretną decyzję albo informację, że od operatora nic teraz nie potrzeba.
- Poprzedni odbiór pozostaje przypisany do poprzedniego zakresu i wersji; nowa propozycja go nie dziedziczy.
- Agent ocenia wpływ rozważanych zmian i odradza niespójne lub nieproporcjonalne rozszerzenia.

Zakres przyjęcia nie obejmuje działania rzeczywistego TextStats, gotowości produkcyjnej Flowable, kompletnego kontraktu danych nowej karty, implementacji UI ani pełnej skuteczności procesu. Przyjęto rezultat wspomaganego ćwiczenia ze znaną granicą obserwacji opisaną w §20; nie dopisujemy nieprzeprowadzonych sprawdzianów. Nie zmieniono uprawnień do commita/pushu ani instrukcji pakietu procesu.

**Dalsza praca:** niezlecona. Właściciel zamkniętego zapisu: agent. Ewentualny pilot lub implementacja wymagają odrębnego ustalenia zakresu i zlecenia. Brak nowego pytania decyzyjnego wynikającego z tego ćwiczenia.

## 22. Zamknięcie etapu z rekomendacją dalszej drogi

2026-11-08. Użytkownik doprecyzował sposób komunikacji: po zakończeniu etapu agent może wskazać kolejkę lub roadmapę, aby nie wymagać osobnej tury na pytanie „co dalej?”. Zachowujemy rozróżnienie rekomendacji od upoważnienia do wykonania. Nie wracamy do automatycznej serii lekcji.

**Przyjęta zasada komunikacji:** na końcu etapu agent podaje najbliższy zalecany krok, jego rezultat i powód; w razie potrzeby najwyżej dwa dalsze kroki z zależnościami. Każdy ma status: wykonany/zlecony/proponowany/warunkowy. Otwarte zadania innych wątków pozostają w swoich rejestrach; nie przestawiamy ich kolejności bez zlecenia.

**Proponowana droga dla przyjętej koncepcji karty (nie nowy plan wykonawczy):**

1. Mapowanie jednej karty na istniejące dane F5 — agent, proponowane. Rezultat: tabela pole → źródło/wyliczenie → brak, dla trzech znanych stanów. Warunek zakończenia: każde pole ma źródło albo jawny brak; decyzja, czy wystarczy poprawka prezentacji. Powód: obecna karta jest redakcją ręczną, a kontrakt danych widoku nie jest kompletny. Bez nowego schematu, UI i zmian silnika.
2. Automatycznie generowany czytelny meldunek — agent, warunkowe i niezlecone. Dopiero jeśli mapowanie wykaże mały zakres, a użytkownik zleci implementację. Rezultat: te same trzy stany z istniejących danych, bez ręcznego przepisywania statusów; brakujące fakty jawne.
3. Krótka próba użycia meldunku po wznowieniu — agent i operator, warunkowe i niezlecone. Po dostarczeniu widoku ocena, czy pomaga odnaleźć stan i podjąć decyzję; nie domyślne przejście do produkcyjnego Kitchen lub ogólnego ALM.

Rekomendacja najbliższa: krok 1. Nie potrzebujemy teraz pełnej bazy danych ani nowej architektury; trzeba najpierw sprawdzić, ile potrzebnego widoku obsługuje istniejący model. Źródłem aktualnego statusu pracy pozostaje mapa §8.7; ta sekcja opisuje propozycję po zakończonym etapie, nie uruchamia jej.
