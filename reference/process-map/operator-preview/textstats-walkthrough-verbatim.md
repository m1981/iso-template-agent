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
