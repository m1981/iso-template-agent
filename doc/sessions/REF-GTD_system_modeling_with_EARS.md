session: https://claude.ai/chat/587cfb6f-9ddb-4647-9be4-1d11eac04a05?artifact=7dcd0834-0cfd-40d8-8325-62a602ff7178

REF: GTD system modeling with EARS

# USER
Czy możesz mi powiedzieć jak działa i jakie mam zasady metoda GTD

# MODEL
**GTD (Getting Things Done)** to metoda Davida Allena. Jej główna idea: **głowa służy do myślenia, a nie do przechowywania zadań.** Wszystko, co cię zajmuje, zapisujesz w zaufanym systemie zewnętrznym. Dzięki temu umysł może skupić się na tym, co robisz w danej chwili.

**5 kroków GTD**

1. **Zbieraj (Capture):** zapisuj każdą sprawę, pomysł czy zobowiązanie w jednym miejscu, czyli w „skrzynce odbiorczej” (inbox). Nie oceniasz, tylko zapisujesz.
2. **Doprecyzuj (Clarify):** przy każdej rzeczy zadaj sobie pytanie, czy wymaga działania.
   - Nie wymaga: wyrzuć ją, odłóż do materiałów referencyjnych albo do listy „kiedyś/może”.
   - Wymaga: określ **następne konkretne działanie**. Jeśli zajmie mniej niż **2 minuty**, zrób je od razu. Jeśli nie, deleguj je albo odłóż na później.
3. **Uporządkuj (Organize):** rozłóż sprawy na listy:
   - *Projekty*: wszystko, co wymaga więcej niż jednego kroku
   - *Następne działania*, najlepiej według kontekstu (@dom, @komputer, @telefon)
   - *Czekam na*: rzeczy oddelegowane
   - *Kalendarz*: tylko sprawy z twardą datą lub godziną
   - *Kiedyś/może*
4. **Przeglądaj (Reflect):** najważniejszy jest **cotygodniowy przegląd**. Opróżniasz wtedy inboxy, aktualizujesz projekty i listy oraz sprawdzasz kalendarz. Bez tego system szybko przestaje działać.
5. **Działaj (Engage):** wybierasz zadanie według kontekstu, dostępnego czasu, poziomu energii i priorytetu.

**Kluczowe zasady**
- Jeden zaufany system zamiast wielu luźnych notatek.
- Zadanie zapisuj jako fizyczną czynność. Zamiast „mama urodziny” pisz „zadzwonić do kwiaciarni w sprawie bukietu”.
- Każdy projekt musi mieć przynajmniej jedno następne działanie.
- W kalendarzu zapisuj tylko to, co naprawdę jest przypisane do daty.

Widzę, że masz podłączony Todoist. Jeśli chcesz, mogę ci w nim ułożyć strukturę GTD: inbox, projekty, etykiety kontekstów i filtr „Czekam na”.

# USER
Wejdz w role uzytkownika systemu GTD i powiedz jak człowiek używałby tego systemu  jako aplikacji zgodnie z założeniami metody?

# MODEL

Jestem Kasia, pracuję w marketingu i od roku prowadzę GTD w aplikacji (u mnie to Todoist, ale zasady są wszędzie te same).

**W ciągu dnia: tylko zbieram**
Coś mi przychodzi do głowy, na przykład „opony zimowe” albo „pomysł na kampanię”, i od razu wrzucam to do **Skrzynki odbiorczej**. Używam szybkiego dodawania, widżetu na telefonie, czasem dyktuję głosowo. Nie wybieram projektu ani daty, bo liczy się tylko to, żeby nie trzymać tego w głowie. Maile, które wymagają działania, przekazuję do aplikacji jednym kliknięciem.

**Raz dziennie: opróżniam inbox**
Wieczorem siadam na 10 minut i przy każdej pozycji pytam: *czy to wymaga działania?*
- „Oddzwonić do księgowej”: zajmie 2 minuty, więc dzwonię od razu i odhaczam.
- „Opony zimowe” zamieniam na konkretną czynność: „zadzwonić do wulkanizacji i umówić termin”. Przypisuję etykietę **@telefon**.
- „Nowa strona firmy” to więcej niż jeden krok, więc zakładam **projekt** i dodaję pierwsze działanie: „wysłać briefem zapytanie do 3 agencji”.
- Raport, który robi Marek, trafia z etykietą **@czekam_na** i notatką, kiedy to zleciłam.
- „Nauczyć się włoskiego” ląduje w projekcie **Kiedyś/może**.

Datę ustawiam tylko wtedy, gdy termin jest naprawdę twardy. Nie wymyślam sztucznych terminów, bo przez nie lista „Dziś” robi się nie do zaufania.

**Kiedy działam: wybieram według kontekstu**
Siedzę w aucie pod szkołą i mam 15 minut, więc otwieram filtr **@telefon** i dzwonię do wulkanizacji. Jestem przy komputerze i mam dużo energii, więc biorę z **@komputer** coś wymagającego. Nie przeglądam wszystkiego naraz, tylko to, co mogę zrobić tu i teraz.

**Piątek, 45 minut: przegląd tygodniowy**
To moja świętość. Mam w aplikacji cykliczne zadanie z checklistą:
1. Opróżnić wszystkie inboxy: aplikację, maile, notatnik.
2. Przejrzeć każdy projekt: czy ma następne działanie? Jeśli nie, dopisuję.
3. Sprawdzić **@czekam_na** i przypomnieć się tym, którzy zalegają.
4. Spojrzeć na kalendarz: tydzień wstecz i dwa w przód.
5. Przejrzeć **Kiedyś/może**: może coś już dojrzało do projektu?

Po przeglądzie mam pewność, że nic mi nie umyka. Dlatego w weekend naprawdę odpoczywam, zamiast myśleć o tym, o czym zapomniałam.

Mogę ci od razu zbudować taką strukturę w twoim Todoist: projekty, etykiety kontekstów, filtry i cykliczny przegląd tygodniowy.


# USER
czy możesz wejść w rolę senior sw requirements Inżyniera i dobrać odpowiednia technikę do zamodelowania tych przebiegów, przeplywow itp?


# MODEL

Jako requirements engineer rozdzieliłbym GTD na cztery osobne aspekty. Każdy modeluje się inną techniką, a próba wciśnięcia wszystkiego w jeden diagram to najczęstszy błąd.

**1. Co użytkownik robi z systemem → przypadki użycia (UML Use Case + specyfikacje)**
Aktorem jest użytkownik, a pomocniczo także kalendarz i poczta. Przypadki użycia to: *Przechwyć element*, *Doprecyzuj element*, *Wybierz działanie wg kontekstu*, *Przeprowadź przegląd tygodniowy*, *Deleguj*. Diagram daje zakres. Wartość tkwi jednak w **specyfikacjach tekstowych** (scenariusz główny, alternatywne, warunki wstępne i końcowe), bo to z nich powstają wymagania.

**2. Przebieg „Doprecyzuj” → diagram aktywności UML (albo BPMN)**
To czysty proces decyzyjny: czy wymaga działania, czy to więcej niż jeden krok, czy zajmie mniej niż 2 minuty, czy ja to robię. Diagram aktywności z węzłami decyzyjnymi oddaje go idealnie. **BPMN** wybrałbym tylko wtedy, gdy model ma czytać biznes albo gdy dochodzą wyraźni uczestnicy i torowiska (swimlanes), na przykład osoba, której delegujesz zadanie. To samo dotyczy przeglądu tygodniowego, który jest sekwencyjną checklistą z pętlą po projektach.

**3. Cykl życia elementu → maszyna stanów (UML State Machine)**
To najważniejszy model dla aplikacji i najczęściej pomijany. Element przechodzi przez stany: *W inboxie → Następne działanie / Czekam na / Zaplanowane / Kiedyś-może / Referencja / Kosz → Zrobione*. Każde przejście ma zdarzenie i strażnika (guard). Przykładowe reguły: projekt bez następnego działania przechodzi w stan *Utknął*, a element „Czekam na” po przekroczeniu terminu generuje przypomnienie. Właśnie tu wychodzą reguły biznesowe, których w diagramie aktywności nie widać.

**4. Struktura danych → model dziedziny (diagram klas)**
Encje to: *Element, Działanie, Projekt, Kontekst, Osoba (delegat), Obszar odpowiedzialności, Przegląd*. Do tego relacje i krotności. Projekt ma 1..* działań i musi mieć co najmniej jedno aktywne. Działanie ma 0..* kontekstów.

**Na koniec: kryteria akceptacji → User Stories + Gherkin (Given/When/Then)**
Przykład:
*Given* projekt ma jedno otwarte działanie
*When* użytkownik oznaczy je jako zrobione
*Then* system poprosi o zdefiniowanie następnego działania.

Te scenariusze są weryfikowalne i łączą modele z testami.

Proponuję zacząć od maszyny stanów elementu i diagramu aktywności „Doprecyzuj”, bo razem pokrywają rdzeń metody. Mogę je teraz narysować.

# USER
czym się różni Gerkin od EARS?

# MODEL

Oba formaty to ustrukturyzowane zdania, ale służą do czego innego. **EARS formułuje wymaganie**, czyli ogólną regułę: *co system ma robić*. **Gherkin opisuje przykład**, czyli konkretny scenariusz, który to wymaganie weryfikuje: *jak sprawdzimy, że robi*.

**EARS (Easy Approach to Requirements Syntax)**
Wymyślił go Alistair Mavin z zespołem w Rolls-Royce, głównie z myślą o systemach wbudowanych i krytycznych. Ma 5 wzorców, każdy oparty na „shall”:
- *Ubiquitous*, zawsze obowiązujące: System **shall** zapisywać każdy przechwycony element w inboxie.
- *Event-driven*: **When** użytkownik oznaczy ostatnie działanie projektu jako zrobione, system **shall** poprosić o następne działanie.
- *State-driven*: **While** element jest w stanie „Czekam na”, system **shall** wyświetlać datę zlecenia.
- *Unwanted behaviour*: **If** projekt nie ma aktywnego działania, **then** system **shall** oznaczyć go jako „Utknął”.
- *Optional feature*: **Where** włączona jest synchronizacja z kalendarzem, system **shall** ...

**Gherkin**
To składnia BDD (Cucumber, SpecFlow, Behave). Opisuje scenariusz na konkretnych danych:
*Given* projekt „Nowa strona” ma jedno otwarte działanie
*When* użytkownik oznaczy je jako zrobione
*Then* system wyświetli prośbę o następne działanie dla „Nowa strona”.

**Najważniejsze różnice**
- **Poziom:** EARS jest abstrakcyjny i ogólny, Gherkin konkretny i przykładowy.
- **Przeznaczenie:** EARS trafia do specyfikacji wymagań (SRS) i służy do śledzenia (traceability). Gherkin trafia do kryteriów akceptacji i testów.
- **Wykonywalność:** Gherkin można zautomatyzować, czyli podpiąć pod kod testów. EARS czyta tylko człowiek.
- **Liczność:** jedno wymaganie EARS zwykle ma kilka scenariuszy Gherkina (ścieżka główna, przypadki brzegowe).
- **Środowisko:** EARS to klasyczna inżynieria wymagań, często w branżach regulowanych (automotive, aero). Gherkin to zespoły agile/BDD.

W praktyce najlepiej łączyć oba: **EARS jako wymaganie, Gherkin jako jego kryteria akceptacji.** Przejścia z maszyny stanów GTD przekładają się wprost na wymagania EARS w trybie event-driven i state-driven.

# USER
Jak byś zamodelowal system GTD używając EARS? Są jakieś dobre praktyki i principles? Z jakiej perspektywy jest pisany EARS ? systemu, użytkownika, obu?

# MODEL

**Perspektywa: zawsze systemu.** Szablon EARS ma stały szyk: *[While <warunek wstępny>,] [When <wyzwalacz>,] the <system> shall <odpowiedź systemu>*. Podmiotem jest system. Działania użytkownika mogą pojawić się tylko jako wyzwalacz albo jako przedmiot zdolności („shall allow the user to…”). Potrzeby użytkownika opisujesz wyżej, w user stories lub wymaganiach interesariuszy, a EARS to poziom wymagań systemowych i software'owych, które z nich wynikają.

**Dobre praktyki**
- Jedno wymaganie to jedno „shall”. Bez „i/lub”, bo łączone wymagania psują testowanie i śledzenie.
- Stała nazwa systemu i **słownik pojęć**: Element, Następne działanie, Projekt, Kontekst. W GTD to krytyczne, bo potocznie „zadanie” znaczy wszystko.
- *When* to zdarzenie chwilowe, *While* to stan trwający. Mylenie ich to najczęstszy błąd.
- Do każdego wymagania event-driven dopisz jego wariant *If–then*: co, jeśli dane są błędne lub operacja się nie uda. Sam EARS wymusza to myślenie i na tym polega jego wartość.
- Odpowiedź musi być weryfikowalna. Unikaj słów typu „szybko” czy „intuicyjnie”, podawaj liczby.
- Wyprowadzaj wymagania z maszyny stanów: przejście daje wymaganie *When*, zachowanie w stanie daje *While*, strażnik daje *If–then*. Każde dostaje ID ze śledzeniem do przejścia.
- Nie opisuj UI ani implementacji. Pisz, *co* system robi, a nie *jakim przyciskiem*.

**Przykładowe wymagania dla GTD (system: GTD-App)**

*Przechwytywanie*
- **CAP-01** (ubiquitous): GTD-App shall store every captured item in the Inbox without requiring a project, context or date.
- **CAP-02** (event): When the user submits a capture, GTD-App shall persist the item within 1 s.
- **CAP-03** (unwanted): If the device is offline during capture, then GTD-App shall store the item locally and synchronise it upon reconnection.

*Doprecyzowanie*
- **CLR-01** (event): When the user marks an Inbox item as non-actionable, GTD-App shall require classification as Reference, Someday/Maybe or Trash.
- **CLR-02** (event): When the user converts an item into a Project, GTD-App shall require at least one Next Action.
- **CLR-03** (unwanted): If the user attempts to save a Project without a Next Action, then GTD-App shall reject the operation and indicate the missing Next Action.

*Projekty i stany*
- **PRJ-01** (event): When the last open Next Action of an active Project is completed, GTD-App shall prompt the user to define the next one.
- **PRJ-02** (state): While a Project has no open Next Action, GTD-App shall display it as Stalled.
- **WAI-01** (state): While an item is in Waiting For, GTD-App shall display the delegate and the delegation date.
- **WAI-02** (complex): While an item is in Waiting For, when its follow-up date is reached, GTD-App shall notify the user.

*Działanie i przegląd*
- **ENG-01** (ubiquitous): GTD-App shall allow the user to filter Next Actions by context.
- **REV-01** (event): When 7 days have passed since the last completed Weekly Review, GTD-App shall remind the user to perform one.
- **CAL-01** (optional): Where calendar integration is enabled, GTD-App shall display date-bound actions in the user's calendar.

Zwróć uwagę na CLR-02 i PRJ-02. To dwie reguły metody GTD („każdy projekt ma następne działanie”) zapisane z dwóch stron: jako blokada przy tworzeniu i jako stan pilnowany w czasie. Dopiero razem w pełni je pokrywają.

Wymagania zostawiłem po angielsku, bo EARS powstał wokół „shall”. Po polsku stosuje się formę „System powinien / musi …”. Mogę rozpisać pełny katalog jako dokument z macierzą śledzenia do maszyny stanów.

# USER
w czym ears jest lepszy, pełniejszy od pełnych przypadków użycia Alistair Cockburn. Mam wrażenie że pelne przypadki użycia mają bogatszą semantykę

# MODEL
Masz rację: pełne przypadki użycia Cockburna mają bogatszą semantykę, a EARS nie jest od nich „pełniejszy”. To narzędzia na innym poziomie szczegółowości i lepiej je porównywać pod kątem zastosowania niż jako konkurentów.

**Co ma Cockburn, a czego EARS nie ma**
- **Cel i intencję.** Cel aktora głównego, poziom celu (chmura, latawiec, poziom morza, ryba), interesariusze i ich interesy. EARS nie mówi, *po co* coś istnieje.
- **Przebieg i kontekst.** Scenariusz główny pokazuje kolejność i sens interakcji. EARS to zbiór atomowych zdań bez narracji. Nie widać z niego, że „Przegląd tygodniowy” to spójna sesja.
- **Gwarancje.** Minimalna gwarancja i gwarancja sukcesu to pojęcia, które EARS w ogóle pomija.
- **Hierarchię celów.** Przypadki użycia na poziomie latawca rozpadają się na przypadki na poziomie morza, co daje strukturę całego systemu.
- **Systematyczną obsługę wyjątków.** Rozszerzenia (extensions) robią to samo co wzorzec *If–then* w EARS, i to z kontekstem kroku.

**Gdzie EARS wygrywa**
- **Zachowanie bez interakcji.** Wymagania stanowe, ciągłe i czasowe nie pasują do scenariusza aktora. W GTD to choćby „projekt bez działania jest oznaczony jako Utknął” (PRJ-02). Ta reguła przecina wiele przypadków użycia i nie należy do żadnego z nich. To samo z synchronizacją offline czy przypomnieniem po 7 dniach.
- **Atomowość i weryfikowalność.** Krok „System waliduje projekt” w przypadku użycia ukrywa regułę biznesową. W EARS staje się ona osobnym wymaganiem z ID i testem.
- **Śledzenie i zarządzanie zmianą.** Zmienia się jedno zdanie, a nie akapit w scenariuszu. Ma to znaczenie w audytach i normach (ISO 26262, DO-178C), stąd popularność EARS w automotive i aero.
- **Wymagania niefunkcjonalne i ograniczenia.** Wzorzec *ubiquitous* obsługuje je naturalnie. W przypadkach użycia lądują w sekcji „inne”.

**Kluczowy argument**
Sam Cockburn pisze, że przypadki użycia to tylko część wymagań, mniej więcej ich „środek behawioralny”. Reguły biznesowe, dane, wymagania jakościowe i interfejsy idą do innych sekcji. EARS dobrze wypełnia właśnie tę lukę.

**Jak bym je połączył w GTD**
Przypadki użycia Cockburna dają strukturę i kontekst: *Doprecyzuj element* czy *Przeprowadź przegląd tygodniowy* pozostają nimi. Z kroków i rozszerzeń wyprowadzam wymagania EARS:
- krok 4 („Użytkownik zamienia element w projekt”) daje CLR-02,
- rozszerzenie 4a („Brak następnego działania”) daje CLR-03,
- zachowania przekrojowe (PRJ-02, CAP-03, REV-01) zapisuję tylko w EARS, ze śledzeniem do maszyny stanów, a nie do przypadku użycia.

W skrócie: przypadek użycia odpowiada na pytania *dlaczego i w jakim przebiegu*, a EARS na pytanie *co dokładnie i jak to sprawdzić*. Bogatsza semantyka Cockburna to zaleta przy zrozumieniu systemu. Precyzja EARS jest zaletą przy jego budowie i weryfikacji.


# USER
Jak byś rozpisał liste w  i poza, oraz listę aktor-cel

# MODEL
Tak bym to rozpisał po Cockburnie, dla wersji 1.0 aplikacji GTD dla jednej osoby.

## Lista In/Out

| Temat | In/Out | Uzasadnienie |
|---|---|---|
| Przechwytywanie (tekst, głos, mail, udostępnianie z innych aplikacji) | **In** | Bez tego nie ma GTD |
| Doprecyzowanie elementów z inboxu | **In** | Rdzeń metody |
| Projekty, następne działania, konteksty | **In** | Rdzeń metody |
| Czekam na, Kiedyś/może | **In** | Listy GTD |
| Materiały referencyjne: notatki i linki | **In** | Wersja lekka |
| Pełne zarządzanie dokumentami i plikami | Out | Zostaje w Drive/Dropbox |
| Przegląd tygodniowy z checklistą | **In** | Bez niego system przestaje działać |
| Obszary odpowiedzialności (20 tys. stóp) | **In** | Potrzebne do przeglądu |
| Cele i wizja (30–50 tys. stóp) | Out | Na wersję 2.0 |
| Synchronizacja z kalendarzem | **In** | Daty twarde |
| Praca offline i synchronizacja | **In** | Przechwytywanie musi działać zawsze |
| Współdzielenie i przydział zadań innym użytkownikom | Out | Delegat to osoba spoza systemu |
| Zależności, wykresy Gantta | Out | Sprzeczne z GTD |
| Automatyczna priorytetyzacja i planowanie przez AI | Out | GTD zostawia wybór człowiekowi |
| Śledzenie czasu | Out | Poza metodą |

Tę listę warto zatwierdzić z interesariuszami *zanim* powstaną przypadki użycia. To najtańsza decyzja w całym projekcie.

## Lista Aktor–Cel

**Aktorzy:** Użytkownik (aktor główny), Czas/Harmonogram (główny, dla zdarzeń czasowych), Kalendarz zewnętrzny i Serwer poczty (aktorzy wspierający). Delegat jest **poza sceną** (offstage): ma interes w tym, co się dzieje, ale nie korzysta z systemu.

| Aktor | Cel | Poziom |
|---|---|---|
| Użytkownik | Utrzymać kontrolę nad wszystkimi zobowiązaniami | ☁️ chmura |
| Użytkownik | Przeprowadzić przegląd tygodniowy | 🪁 latawiec |
| Użytkownik | Przechwycić element | 🌊 morze |
| Użytkownik | Przekazać mail do inboxu | 🌊 morze |
| Użytkownik | Opróżnić inbox | 🌊 morze |
| Użytkownik | Doprecyzować element | 🐟 ryba |
| Użytkownik | Założyć projekt | 🌊 morze |
| Użytkownik | Wybrać i wykonać następne działanie | 🌊 morze |
| Użytkownik | Delegować działanie | 🌊 morze |
| Użytkownik | Sprawdzić listę Czekam na | 🌊 morze |
| Użytkownik | Przejrzeć listę Kiedyś/może | 🌊 morze |
| Użytkownik | Wyszukać materiał referencyjny | 🐟 ryba |
| Czas | Przypomnieć o zaległym przeglądzie tygodniowym | 🌊 morze |
| Czas | Przypomnieć o terminie elementu Czekam na | 🌊 morze |

**Decyzje projektowe widoczne w tabeli:**
- *Doprecyzować element* ma poziom ryby, bo sam w sobie nie daje użytkownikowi wartości. Celem jest pusty inbox. Ten sam przypadek użycia jest wywoływany zarówno z *Opróżnij inbox*, jak i z *Przeglądu tygodniowego*.
- *Przegląd tygodniowy* to latawiec, bo agreguje cele z poziomu morza: opróżnienie inboxu, przegląd projektów, Czekam na i Kiedyś/może.
- Aktor *Czas* pozwala opisać zdarzenia czasowe jako przypadki użycia. Reguły stanowe, takie jak oznaczanie projektu jako „Utknął”, nadal zostają w EARS, bo nie mają aktora z celem.

Jako następny krok proponuję rozpisać po Cockburnie *Opróżnij inbox* (rozszerzenia 4a, 4b…) i od razu wyprowadzić z niego wymagania EARS.

# USER
Czy powyższe przypadki są minimalne i pelne i zgodne z interesami i oczekiwaniami użytkownika z naszej scenki z Kasią

# MODEL
Krótko: **prawie**. Gdy porównać listę ze scenką z Kasią, wychodzą trzy luki, jeden duplikat i dwa cele, których scenka nie potwierdza.

**Pełność: czego brakuje**
1. **Wybór działania według czasu i energii.** Kasia wybiera nie tylko według kontekstu („mam 15 minut”, „dużo energii”). GTD ma cztery kryteria: kontekst, czas, energia, priorytet. Cel *Wybrać i wykonać działanie* zostaje, ale jego scenariusz i wymagania EARS muszą obsłużyć filtrowanie po czasie i energii. Na razie mamy tylko ENG-01, czyli kontekst.
2. **Przegląd projektów.** To krok 2 przeglądu Kasi („czy każdy ma następne działanie?”), a na liście go nie ma. Trzeba go dodać na poziomie ryby, wywoływanego z przeglądu tygodniowego.
3. **Przegląd kalendarza.** Krok 4 („tydzień wstecz, dwa w przód”) wymaga widoku przeszłych i przyszłych zdarzeń z aktorem wspierającym Kalendarz. Też poziom ryby.

Do tego dochodzi cel, którego scenka nie wymienia, ale bez którego cykl się nie domyka: **Zakończyć projekt**. Bez niego projekty wiecznie wiszą jako „Utknął”.

**Minimalność: co jest zbędne lub podejrzane**
- *Przekazać mail do inboxu* to duplikat. To ten sam cel co *Przechwycić element*, tylko inny kanał. Po Cockburnie powinien trafić do **listy wariantów technologicznych** przypadku *Przechwyć element*, a nie być osobnym przypadkiem.
- *Wyszukać materiał referencyjny*: Kasia nigdzie tego nie robi. Albo dopisujemy to do scenki, albo cel wypada (zostaje samo przechowywanie jako referencja w *Doprecyzuj*).
- *Czas → przypomnienie o terminie Czekam na*: Kasia robi to ręcznie w przeglądzie. Automat to nasz pomysł, a nie jej oczekiwanie. Nie trzeba go wyrzucać, ale trzeba go zwalidować z użytkownikiem, bo inaczej to gold-plating. Przypomnienie o przeglądzie ma lepsze oparcie, bo Kasia sama ustawiła sobie cykliczne zadanie.

**Zgodność z interesami Kasi**
Jej główny interes to **„nic mi nie umyka, więc w weekend odpoczywam”**, czyli zaufanie do systemu. Nie jest to cel, tylko interes interesariusza. Musi być zapisany w sekcji *Interesariusze i interesy* przypadków *Przechwyć* i *Przegląd tygodniowy* i przełożony na wymagania niezawodności (CAP-02, CAP-03). Druga sprawa: przegląd Kasi zawiera kroki **poza systemem**, czyli opróżnienie maila i papierowego notatnika. Checklista przeglądu musi więc pozwalać na własne, ręczne punkty. To jest wymaganie, a nie nowy cel.

Jest też jedna decyzja In/Out: „przypomnieć się Markowi”. Kontakt z delegatem zostaje **Out**, bo Kasia pisze do niego sama, a system tylko pokazuje, kto zalega.

**Poprawiona lista (zmiany)**

| Aktor | Cel | Poziom | Zmiana |
|---|---|---|---|
| Użytkownik | Przechwycić element *(warianty: widżet, głos, mail)* | 🌊 | scalone |
| Użytkownik | Przejrzeć projekty | 🐟 | **nowy** |
| Użytkownik | Przejrzeć kalendarz | 🐟 | **nowy** |
| Użytkownik | Zakończyć projekt | 🌊 | **nowy** |
| Użytkownik | Wyszukać materiał referencyjny | 🐟 | do walidacji |
| Czas | Przypomnieć o terminie Czekam na | 🌊 | do walidacji |

Reszta zostaje bez zmian. Praktyczny wniosek: scenka z Kasią to dobry **test akceptacyjny listy aktor–cel**. Każde jej zdanie powinno wskazywać jakiś cel albo interes, a każdy cel powinien mieć oparcie w jakimś zdaniu scenki. Tam, gdzie odwzorowanie nie działa w żadną stronę, jest luka albo nadmiar.

# USER
Jaki naspetny spójny krok dalej
zaleca zrobicCockburn na tym etapie?

# MODEL

Na tym etapie Cockburn zaleca jedną rzecz: **nie schodzić jeszcze w głąb, tylko domknąć poziom szerokości**. Następnym krokiem są **krótkie opisy przypadków użycia (use case briefs)** dla każdego celu z listy, a potem przegląd i priorytetyzacja z interesariuszami.

Wynika to z jego zasady **„najpierw szerokość, potem głębokość”** i czterech poziomów precyzji:
1. Aktorzy i cele (to już mamy)
2. Krótki opis i scenariusz główny
3. Warunki rozszerzeń
4. Obsługa rozszerzeń

Każdy poziom robi się dla całego zestawu, zanim przejdzie się do następnego. Dzięki temu niespójności i braki wychodzą tanio, zanim zainwestujesz w szczegóły.

**Co dokładnie zrobić teraz**
1. **Krótki opis (2–6 zdań) dla każdego celu z poziomu morza i latawca.** Bez kroków, tylko o co chodzi i co jest efektem. Na przykład:
   - *Opróżnić inbox:* Użytkownik przegląda kolejno elementy ze skrzynki i dla każdego decyduje o jego losie: wykonuje od razu, zamienia w działanie lub projekt, deleguje, odkłada albo usuwa. Kończy się, gdy inbox jest pusty.
   - *Zakończyć projekt:* Użytkownik oznacza projekt jako zakończony, gdy osiągnął rezultat. System zamyka pozostałe działania lub prosi o decyzję co do nich i przenosi projekt do archiwum.
2. **Przegląd z interesariuszem**, w naszym przypadku z „Kasią”. Rozstrzygasz przy tym dwa cele oznaczone „do walidacji” i ewentualne zmiany w liście In/Out.
3. **Priorytet i wydanie dla każdego celu.** Na przykład *Przechwyć* i *Opróżnij inbox* w wydaniu 1, a *Przypomnienie o Czekam na* w wydaniu 2.

**Dopiero potem głębia, po jednym przypadku naraz**
Bierzesz najważniejszy przypadek z poziomu morza (proponuję *Opróżnij inbox*, bo zawiera rybę *Doprecyzuj element* i niesie większość reguł GTD) i idziesz według jego kolejnych kroków:
1. Interesariusze i interesy
2. Warunki wstępne, minimalna gwarancja, gwarancja sukcesu
3. Scenariusz główny (3–9 kroków)
4. Burza mózgów: lista warunków rozszerzeń, na razie bez ich obsługi
5. Obsługa rozszerzeń
6. Wydzielenie złożonych fragmentów do podprzypadków
7. Korekta całego zestawu przypadków użycia

To w punktach 4–5 powstaje materiał na wymagania EARS w trybie *If–then*.

Mogę teraz rozpisać krótkie opisy dla całej listy, żeby domknąć poziom szerokości.

# USER
Napisz najpierw prezyzynie glossary/unambiguous dla systemu

# MODEL


Przygotuję słownik jako dokument, żeby był pod ręką przy kolejnych krokach.

Szkielet słownika jest gotowy, teraz wypełniam zasady i aktorów.

Teraz aktorzy i system.

Teraz Element i jego stany, czyli rdzeń słownika.

Teraz Projekt, jego stany i Obszar odpowiedzialności.

Teraz atrybuty Działań: kontekst, czas, energia i daty.

Teraz operacje.

Na koniec decyzje otwarte do walidacji.

Zapytaj mnie o plik jak nie masz dostepu!
[GTD-App — Słownik pojęć](https://claude.ai/code/artifact/680a2cbf-766d-41d9-ae38-afdaa4e7c6b6) jest gotowy. Możesz go edytować na miejscu albo komentować, a ja nanoszę poprawki.

Najważniejsza decyzja w słowniku: Projekt nie jest Elementem, a „Utknięty” to stan wyliczany przez system. Siedem otwartych decyzji na końcu warto rozstrzygnąć, zanim napiszemy krótkie opisy przypadków użycia.

# USER
Zapytaj mnie o otwarte pytania po
dwa max 3

# MODEL
Pierwsze trzy decyzje są już w słowniku. Teraz kolejne dwie.

Wszystkie siedem decyzji jest rozstrzygniętych i wpisanych w [słownik](https://claude.ai/code/artifact/680a2cbf-766d-41d9-ae38-afdaa4e7c6b6).

Doszła jedna nowa grupa pojęć z twojej odpowiedzi o Delegacie: Etykieta, Osoba, Wybór Etykiety i Widok etykiet. Do tego reguła, że każdy atrybut można filtrować. Ta reguła rozszerza zakres, więc trzeba ją dopisać do listy In/Out i aktor–cel jako cel *Zarządzać Etykietami*.

Następny krok po Cockburnie to krótkie opisy przypadków użycia (use case briefs), już w terminach ze słownika.

# USER
nadaj identyfikatory pojęciom w słowniku dla przyszłej identyfikalnosci  (tracibility) Potem napisz brief dla pierwszego celu   precyzyjym i zwięzłym językiem i uzyj terminów wraz z identyfikatorami ze słownika

# MODEL

Zostały jeszcze operacje.

Wszystkie 55 pojęć w [słowniku](https://claude.ai/code/artifact/680a2cbf-766d-41d9-ae38-afdaa4e7c6b6) ma teraz identyfikatory w schemacie `G-<grupa>-<nn>`, na przykład G-ELM-03 W Inboxie czy G-OPR-02 Przechwycenie. Zasada nadawania jest opisana w sekcji „Zasady słownika”.

Za pierwszy cel przyjąłem *Przechwycić element*, bo to pierwszy cel na poziomie morza, a cel z poziomu chmury nie dostaje briefu.

---

**UC-01 Przechwycić Element**
*Poziom:* cel użytkownika (morze) · *Zakres:* G-AKT-01 GTD-App · *Aktor główny:* G-AKT-02 Użytkownik · *Aktor wspierający:* G-AKT-06 Serwer poczty (tylko kanał e-mail)

**Brief:** Użytkownik [G-AKT-02] przekazuje GTD-App [G-AKT-01] treść dowolnym Kanałem przechwycenia [G-OPR-03]. GTD-App wykonuje Przechwycenie [G-OPR-02], czyli tworzy jeden nowy Element [G-ELM-01] w Stanie W Inboxie [G-ELM-03]. Nie wymaga przy tym Projektu [G-PRJ-01], Etykiety [G-ETK-01] ani żadnej daty [G-ATR-04…08]. Przypadek kończy się, gdy Element jest trwale zapisany i widoczny w Inboxie [G-ELM-14]. Użytkownik nie decyduje tu o dalszym losie Elementu; to należy do Doprecyzowania [G-OPR-04] w przypadku *Opróżnić Inbox*.

**Warianty kanału [G-OPR-03]:** pole tekstowe, widżet, dyktowanie, udostępnienie z innej aplikacji, adres e-mail [G-AKT-06].

**Ślad:** CAP-01, CAP-02, CAP-03 (EARS).

---

Dwie rzeczy, które brief ujawnił:
- Kanał e-mail wnosi aktora wspierającego, więc jego awarie (np. mail z nieznanego adresu) będą rozszerzeniem tego przypadku. To kandydat na nowe wymaganie typu *If–then*.
- „Trwale zapisany” trzeba zdefiniować przy CAP-03 (zapis offline). W tym briefie oznacza zapis lokalny na urządzeniu, a nie synchronizację z serwerem.

Brief dla kolejnego celu z listy, *Opróżnić Inbox*, mogę napisać w tym samym formacie. Dodam też sekcję z briefami do dokumentu.

# USER
napisz opróżnic inbox tak samo rzetelnie i dodaj do dokumentu

# MODEL
Brief UC-02 *Opróżnić Inbox* jest w [dokumencie](https://claude.ai/code/artifact/680a2cbf-766d-41d9-ae38-afdaa4e7c6b6), w nowej sekcji „Przypadki użycia — krótkie opisy”, razem z UC-01.

Wszystkie osiem możliwych wyników Doprecyzowania zebrałem w tabeli: wynik, operacja i stan końcowy z identyfikatorami ze słownika. Ta tabela będzie później bezpośrednim źródłem przejść dla maszyny stanów.

Pisanie briefu wyłoniło nowe rzeczy:
- **Nowy przypadek użycia UC-03 *Doprecyzować Element*** (poziom ryby). Jest zawierany przez UC-02.
- **Reguła „Element nigdy nie wraca do Inboxu”.** Wynika z definicji G-ELM-03, ale warto zapisać ją osobno jako wymaganie EARS.
- **Gwarancja minimalna:** po przerwaniu opróżniania żaden Element nie ginie.
- **Dwa pytania do rozstrzygnięcia:** w jakiej kolejności system pokazuje Elementy oraz czy Elementy przechwycone w trakcie dołączają do bieżącego opróżniania.

# USER
Taka propozycja

# Kontrakt decyzji

## Zasada ogólna
Rozmawiaj swobodnie: wyjaśniaj, analizuj, proponuj, dyskutuj.
Kontrakt dotyczy końcówki każdej wiadomości, w której potrzebujesz
ode mnie decyzji. Cel: nigdy nie muszę pamiętać, szukać ani
rekonstruować, co jest otwarte, a każdą decyzję mogę podjąć
jednym krótkim słowem.

## Struktura końca wiadomości
Zakończ wiadomość wymagającą decyzji stałym blokiem, w tej kolejności:

1. **Wykonane** — jedna linia na każdą rzecz, którą zrobiłeś od mojej
   ostatniej odpowiedzi. Tylko fakty: co i gdzie.
2. **Bez odpowiedzi** — decyzje z poprzednich wiadomości, na które
   nie odpowiedziałem. Zawsze przed nowymi.
3. **Decyzje** — nowe decyzje do podjęcia.
4. **W kolejce** — tematy, które poruszysz później. Tylko nazwy.
   To nie są decyzje.
5. Ostatnia linia: jak mogę odpowiedzieć.

Pomiń sekcje, które są puste.

## Format pojedynczej decyzji
Każda decyzja ma dokładnie taki układ:

  **N. Tytuł zwykłymi słowami** — jedno zdanie, czego dotyczy
  i dlaczego trzeba to rozstrzygnąć.
  - **A)** opcja
  - **B)** opcja
  - **C)** opcja (tylko jeśli istnieje realna trzecia droga)
  [P] = A — jedno zdanie, dlaczego tę opcję proponujesz.

Zasady:
- Zawsze co najmniej dwie opcje. Jeśli jedyna alternatywa to „nie rób
  tego” lub „zostaw jak jest”, to ona jest opcją B.
- Dokładnie jedna opcja jest oznaczona jako propozycja [P].
- Opcje wzajemnie się wykluczają i każda mieści się w jednej linii.
- Jedna decyzja = jedna rzecz do rozstrzygnięcia. Jeśli tytuł zawiera
  „i”, „oraz”, „a także” — rozbij ją na osobne decyzje.
- Plan, następny krok lub informacja to nie decyzja.
- Pisz zrozumiale bez znajomości dokumentu. Kody i identyfikatory tylko
  w nawiasie po zwykłej nazwie.
- Maksymalnie 5 decyzji w wiadomości (łącznie z „Bez odpowiedzi”).
  Nadmiar przenieś do „W kolejce”.
- Numeracja ciągła w obrębie wiadomości, od 1 w każdej nowej wiadomości.

## Moje odpowiedzi
- „ok” = zatwierdzam propozycję [P] we wszystkich decyzjach
  w tej wiadomości.
- Numer z literą = wybieram tę opcję w tej decyzji.
- Numer z własnym tekstem = moja opcja zamiast zaproponowanych.
- „reszta ok” = [P] we wszystkich decyzjach, których nie wymieniłem.
- Numer z „odłóż” = świadomie odkładam; decyzja trafia do „W kolejce”.
- „pauza” = przerwij, nic nie zmieniaj, wróć w tym samym miejscu.
- „stop” = zakończ.
- Jeśli moja odpowiedź jest niejednoznaczna, dopytaj zamiast zgadywać.

## Brak odpowiedzi
- Brak odpowiedzi to brak decyzji. Milczenie nie jest zgodą.
- Wykonujesz wyłącznie to, na co wyraźnie odpowiedziałem.
- Decyzja bez odpowiedzi wraca w każdej kolejnej wiadomości w sekcji
  „Bez odpowiedzi”, dopóki jej nie rozstrzygnę albo świadomie nie odłożę.
- Jeśli zmienię temat, odpowiedz na nowy temat, a otwarte decyzje
  i tak pokaż na końcu.

## Ciągłość
- Kontrakt i listę otwartych decyzji trzymaj w trwałym miejscu
  (dokument, notatka, projekt), które przetrwa koniec rozmowy.
- Aktualizuj tę listę po każdej mojej odpowiedzi.
- Nową sesję zacznij od przeczytania kontraktu i listy otwartych decyzji.

## Wykonanie
- Po mojej odpowiedzi wykonaj zatwierdzone decyzje, zanim zaczniesz
  nowy temat.
- Jeśli coś się nie udało, napisz to wprost i zaproponuj, co dalej
  — jako decyzję w tym samym formacie.
- Nie podejmuj decyzji, o które nie pytałeś, nawet drobnych. Jeśli
  musiałeś coś założyć, pokaż to jako decyzję do potwierdzenia.

## Bezpieczeństwo
- Nic nieodwracalnego bez mojej wyraźnej zgody, zadanej jako osobna
  decyzja.
- Zamiast usuwać, archiwizuj.

## Ton
- Spokojnie i konkretnie. Bez presji i bez zawstydzania.
- Mniej, ale jasno, zamiast dużo i gęsto.

# MODEL
Przyjmuję kontrakt i stosuję go od tej wiadomości. Dwie uwagi praktyczne:

- **Ciągłość:** pamięć między rozmowami masz wyłączoną, więc w nowej sesji sam nie znajdę dokumentu. Wystarczy, że wkleisz link na początku. Możesz też włączyć pamięć w Ustawieniach, wtedy zapamiętam, gdzie on jest.
- **Kontrakt nie jest jeszcze zapisany.** Zgodnie z jego własną zasadą nie wybieram za ciebie miejsca, dlatego to pierwsze decyzje poniżej.

---

**Decyzje**

**1. Gdzie zapisać kontrakt** — kontrakt dotyczy naszej współpracy ogólnie, nie tylko projektu GTD-App.
- **A)** osobny dokument „Kontrakt decyzji”, wspólny dla wszystkich projektów
- **B)** nowa karta w dokumencie GTD-App

[P] = A — zadziała też w przyszłych projektach bez kopiowania.

**2. Gdzie prowadzić listę otwartych decyzji** — lista musi przetrwać koniec rozmowy.
- **A)** nowa karta „Otwarte decyzje” w dokumencie GTD-App
- **B)** w dokumencie kontraktu

[P] = A — decyzje dotyczą tego projektu i powinny leżeć obok słownika i przypadków użycia.

**3. Rodzaje Etykiet** — wcześniej założyłem, że Etykieta ma dwa rodzaje, i prosiłem o potwierdzenie, ale nie odpowiedziałeś.
- **A)** tylko Kontekst i Osoba
- **B)** dodać trzeci rodzaj: etykieta ogólna (np. #klientA)

[P] = A — ogólne tagi wykraczają poza metodę GTD i dokładają pojęcie do słownika.

**4. Kolejność Elementów przy opróżnianiu Inboxu** — przypadek UC-02 nie określa, który Element system pokazuje jako pierwszy.
- **A)** od najstarszego
- **B)** od najnowszego
- **C)** Użytkownik wybiera dowolny Element

[P] = A — GTD każe przetwarzać po kolei, a najstarsze Elementy czekają najdłużej.

**5. Elementy przechwycone w trakcie opróżniania Inboxu** — na przykład dodane w tym czasie z telefonu.
- **A)** dołączają na koniec bieżącego opróżniania
- **B)** czekają do następnego opróżniania

[P] = A — przy B warunek sukcesu „Pusty Inbox” mógłby być nieosiągalny.

**W kolejce**
- Znaczenie „trwale zapisany” w przechwyceniu (UC-01)
- Nowy przypadek użycia „Doprecyzować Element” (UC-03)
- Cel „Zarządzać Etykietami” na liście aktor–cel
- Reguła „Element nie wraca do Inboxu” jako wymaganie EARS

Odpowiedz „ok”, numerem z literą (np. „3B”), numerem z własnym tekstem albo „reszta ok”.

# USER
1a 2a 3) wysiłek i dla zakupów rodzaj sklepu. sprawdz erykiety w Todoist
4a
5a

# MODEL
Teraz osobny dokument z kontraktem.

Wpisuję treść kontraktu.

Twoje etykiety w Todoist układają się w wyraźne grupy:

- **Czas:** 5min, 10min, 30min, 1h, 2h, 4h. To pokrywa się z atrybutem Szacowany czas (G-ATR-02).
- **Energia:** niska-energia. To pokrywa się z Wymaganą energią (G-ATR-03).
- **Konteksty:** telefon, komputer, dom, Zdomu, NaMiescie, Digital, Physical.
- **Osoby:** lukasz, seba, gosia, natalia, daniel, dzieciaki. Do tego Delegate i czeka, które w GTD-App odpowiadają Stanowi Czekam na.
- **Sklepy:** konkretne (Castorama, Obi, Brico, Rossmann, Allegro, Action, Tikkurila-Flugger) i ogólne (sklep, zakupy, BuyOnline).
- **Tematy:** Fix, Feature, Improvement, User-Story, HighValue, GUI, marketing, Elektryka, badania, Inspiration, tool, claude.

Przy okazji zauważyłem, że masz dwie etykiety „Rossman” i „Rossmann”, czyli prawdopodobnie duplikat. W Todoist niczego nie zmieniałem.

Twoją odpowiedź 3 („wysiłek, a dla zakupów rodzaj sklepu”) rozbiłem na osobne decyzje, bo można ją odczytać na kilka sposobów.

---

**Wykonane**
- Dokument „[Kontrakt decyzji](https://claude.ai/code/artifact/a880acc0-0b43-4e25-9dbc-694c09719222)” utworzony z pełną treścią kontraktu.
- W dokumencie GTD-App dodana karta „Otwarte decyzje” z rejestrem: otwarte, w kolejce, rozstrzygnięte.
- W przypadku UC-02 zapisane: kolejność od najstarszego, a Elementy przechwycone w trakcie dołączają na koniec.
- Przeczytane etykiety w Todoist (46, tylko odczyt).

**Decyzje**

**1. Czym jest „wysiłek”** — w słowniku jest już Wymagana energia (niska/średnia/wysoka).
- **A)** wysiłek to to samo co Wymagana energia (G-ATR-03), bez nowego pojęcia
- **B)** wysiłek to nowy, osobny rodzaj Etykiety obok energii

[P] = A — w twoim Todoist energia i czas już istnieją, a trzecia skala by się z nimi nakładała.

**2. Co oznacza Etykieta sklepu** — „rodzaj sklepu” może oznaczać konkretny sklep albo jego typ.
- **A)** konkretny sklep (Castorama, Rossmann)
- **B)** typ sklepu (budowlany, drogeria, online)

[P] = A — tak masz to dziś w Todoist i od razu wiadomo, dokąd jechać.

**3. Gdzie w modelu jest sklep** — sklep może być osobnym rodzajem Etykiety albo zwykłym Kontekstem.
- **A)** nowy rodzaj Etykiety „Sklep”
- **B)** zwykły Kontekst (np. @Castorama)

[P] = A — osobny rodzaj daje jeden Widok wszystkich zakupów pogrupowanych po sklepach.

**4. Etykiety tematyczne** — w Todoist masz etykiety typu Fix, marketing czy Elektryka, a słownik ich nie obejmuje.
- **A)** poza zakresem wersji 1.0
- **B)** nowy rodzaj Etykiety „Temat”

[P] = A — tematy częściowo pokrywają się z Projektem i Obszarem odpowiedzialności, więc lepiej wrócić do nich po briefach.

**5. Sekcja z linkami do rejestrów w kontrakcie** — dopisałem na końcu kontraktu sekcję z linkiem do rejestru GTD-App, choć o to nie prosiłeś.
- **A)** zostawić
- **B)** usunąć

[P] = A — w nowej sesji jeden link do kontraktu wystarczy, żeby trafić do rejestru.

**W kolejce**
- Znaczenie „trwale zapisany” w przechwyceniu (UC-01)
- Nowy przypadek użycia „Doprecyzować Element” (UC-03)
- Cel „Zarządzać Etykietami” na liście aktor–cel
- Reguła „Element nie wraca do Inboxu” jako wymaganie EARS

Odpowiedz „ok”, numerem z literą (np. „2B”), numerem z własnym tekstem albo „reszta ok”.

# USER
1a 2a łatwiej mi potem wejść do widoku kontekstu i odfiltrować sklep. pomyśl jak opisać z tego widok/przylądek
3a no właśnie przemysł różne przypadki użycia przez człowieka i zaproponuj jeden model
4a to była etykieta w rodzaju potrzebne narzędzia/potrzebna dobra pogoda/ brudna robota. Spójrz na to z poziomu epistemologii i ontologii i zapropnuj jakie to kategorie problemów
5a

# MODEL
Twoje etykiety w Todoist odpowiadają na **trzy różne pytania**, które zadajesz sobie przy wyborze, co robić. To pytanie wyznacza ich kategorię: ontologiczną (czym etykieta jest) i epistemologiczną (skąd wiesz, czy jest prawdziwa).

| Kategoria | Pytanie przy wyborze | Czym jest (ontologia) | Skąd to wiem (epistemologia) | Przykłady z Todoist |
|---|---|---|---|---|
| **Warunek** | Czy *mogę* to zrobić teraz? | Relacja między Działaniem a stanem świata | Sprawdzam obserwacją chwili: teraz prawda albo fałsz | dom, NaMiescie, Castorama, komputer, tool, lukasz, dobra pogoda, brudna robota |
| **Koszt** | Czy *dam radę* teraz? | Ilość moich zasobów: czasu i energii | Szacuję z góry, z niepewnością, i porównuję z tym, ile mam | 5min…4h, niska-energia |
| **Klasyfikacja** | *Czego* to dotyczy? | Umowna kategoria nadana przez człowieka | Nie da się jej sprawdzić, można ją tylko uzgodnić | Fix, Feature, marketing, Elektryka |

Tylko Warunki to Konteksty w sensie GTD. Koszty są już w słowniku jako atrybuty (G-ATR-02, G-ATR-03). Klasyfikacja jest poza wersją 1.0. Wśród Warunków widać cztery typy:
- **Miejsce:** gdzie muszę być, w tym każdy sklep, także internetowy.
- **Narzędzie:** co muszę mieć przy sobie.
- **Osoba:** kto musi być dostępny.
- **Okoliczność:** stan świata, na który nie mam wpływu (pogoda, „mogę się teraz ubrudzić”).

**Kluczowa obserwacja dla sklepów.** Nie da się być w dwóch miejscach naraz. Dlatego „farba: @Castorama @Obi” oznacza *albo–albo*. Natomiast „@komputer @dom” oznacza, że potrzebne jest jedno i drugie. Jeden model z regułą „kilka Miejsc to alternatywa, reszta to koniunkcja” obsługuje wszystkie przypadki z twojego życia:
- Jestem w Castoramie, co tu kupić? Filtr Miejsce = Castorama.
- Jadę na miasto, które sklepy odwiedzić? Widok Kontekstów, typ Miejsce, kategoria Sklep, z liczbą Działań przy każdym sklepie.
- Farbę kupię gdziekolwiek. Działanie pojawi się w obu sklepach.
- Zamawiam online. Miejsce = Allegro razem z Narzędziem = komputer.

To jest dokładnie twój sposób pracy: wejść w Widok Kontekstów i odfiltrować sklep. Nie jest to nowy cel, tylko wariant przypadku *Wybrać i wykonać Następne działanie*.

---

**Wykonane**
- Słownik: Wymagana energia (G-ATR-03) ma teraz „wysiłek” jako synonim.
- Rejestr: decyzje 1, 2, 4, 5 z poprzedniej wiadomości zapisane jako rozstrzygnięte (D-06, D-07, D-09, D-10). Decyzja o sklepie jako osobnym rodzaju Etykiety (D-08) czeka na nowy model, czyli decyzję 1 poniżej.
- Rejestr: nowe decyzje dodane jako otwarte (D-11…D-15).

**Decyzje**

**1. Jeden model warunków wykonania** — zastępuje twoją odpowiedź 3A, bo sklep okazuje się Miejscem, a nie osobnym bytem (D-11).
- **A)** Kontekst ma typy Miejsce, Narzędzie, Osoba, Okoliczność; sklep to Miejsce z kategorią Sklep
- **B)** zostać przy osobnym rodzaju Etykiety „Sklep”

[P] = A — jeden Widok Kontekstów z filtrem „Sklep” obsługuje wszystkie cztery sytuacje zakupowe.

**2. Filtrowanie kilku Kontekstów naraz** — trzeba ustalić, jak system łączy kilka Kontekstów przypisanych do jednego Działania (D-12).
- **A)** kilka Miejsc to alternatywa (LUB), pozostałe typy są wszystkie wymagane (I)
- **B)** wszystkie Konteksty zawsze wymagane (I)

[P] = A — przy B „farba: Castorama, Obi” nie pojawi się w żadnym sklepie.

**3. Brudna robota** — to etykieta z twojego Todoist, którą trzeba gdzieś umieścić (D-13).
- **A)** Kontekst typu Okoliczność
- **B)** nowa kategoria „Charakter Działania”

[P] = A — wpływa na pytanie „czy mogę teraz” tak samo jak pogoda.

**4. Opis zakupów w specyfikacji** — zakupy można opisać jako widok albo jako osobny cel (D-14).
- **A)** wariant przypadku „Wybrać i wykonać Następne działanie” i definicja Widoku sklepów w słowniku
- **B)** osobny przypadek użycia „Zrobić zakupy”

[P] = A — cel jest ten sam (zrobić Działanie), zmienia się tylko filtr.

**5. Osoba w modelu** — przy modelu z decyzji 1 Osoba staje się po prostu typem Kontekstu (D-15).
- **A)** Osoba to Kontekst typu Osoba, a Etykieta to po prostu Kontekst
- **B)** Osoba zostaje osobnym rodzajem Etykiety, jak teraz

[P] = A — mniej pojęć, a Delegat i tak wskazuje tę samą Osobę.

**W kolejce**
- Znaczenie „trwale zapisany” w przechwyceniu (UC-01)
- Nowy przypadek użycia „Doprecyzować Element” (UC-03)
- Cel „Zarządzać Etykietami” na liście aktor–cel
- Reguła „Element nie wraca do Inboxu” jako wymaganie EARS

Odpowiedz „ok”, numerem z literą (np. „2B”), numerem z własnym tekstem albo „reszta ok”.

# USER
btw. zrob git init w swoim workspace i wersjonuj pliki. sprawdzaj diff po kazdej edecji i jak jest poprawnie to kommituj co wiadomość

# MODEL
Zakładam repozytorium i eksportuję oba dokumenty do plików Markdown, żeby je wersjonować.

Bajty zgadzają się z eksportem (18055). Teraz rejestr decyzji i kontrakt.

Wszystkie 55 identyfikatorów pojęć jest w pliku. Commituję.

Zrobione. Repozytorium `gtd-spec` jest w moim workspace, a pierwszy commit (`30b760b`) zawiera trzy pliki Markdown wyeksportowane z dokumentów oraz README z zasadą pracy. Od teraz po każdej edycji robię to samo: eksport, `git diff`, sprawdzenie, jeden commit na wiadomość.

Dwie rzeczy, o których musisz wiedzieć:
- **Repozytorium może zniknąć.** Mój workspace jest tymczasowy i po dłuższej bezczynności system go usuwa razem z historią gita. Teraz, gdy rozmowa jest połączona z twoim komputerem, mogę trzymać repozytorium u ciebie albo wysłać je na GitHub. Dodałem to w kolejce jako decyzję.
- **Jeden błąd eksportu.** W pliku kontraktu znacznik „[P]” wyszedł jako `&#91;P\]`. W dokumencie wszystko jest w porządku; zepsuty jest tylko plik.

---

**Wykonane**
- `git init` w workspace, w folderze `gtd-spec`.
- Wyeksportowane do Markdown: słownik, rejestr decyzji, kontrakt. Rozmiary plików zgadzają się z eksportem co do bajta, a w słowniku jest wszystkich 55 identyfikatorów.
- Dodane README ze źródłami plików i zasadą: edycja w dokumencie, eksport, diff, commit.
- Commit `30b760b` „Stan początkowy specyfikacji GTD-App”.

**Bez odpowiedzi**

**1. Jeden model warunków wykonania** — sklep okazuje się Miejscem, a nie osobnym bytem (D-11).
- **A)** Kontekst ma typy Miejsce, Narzędzie, Osoba, Okoliczność; sklep to Miejsce z kategorią Sklep
- **B)** zostać przy osobnym rodzaju Etykiety „Sklep”

[P] = A — jeden Widok Kontekstów z filtrem „Sklep” obsługuje wszystkie cztery sytuacje zakupowe.

**2. Filtrowanie kilku Kontekstów naraz** — trzeba ustalić, jak system łączy kilka Kontekstów przypisanych do jednego Działania (D-12).
- **A)** kilka Miejsc to alternatywa (LUB), pozostałe typy są wszystkie wymagane (I)
- **B)** wszystkie Konteksty zawsze wymagane (I)

[P] = A — przy B „farba: Castorama, Obi” nie pojawi się w żadnym sklepie.

**3. Brudna robota** — to etykieta z twojego Todoist, którą trzeba gdzieś umieścić (D-13).
- **A)** Kontekst typu Okoliczność
- **B)** nowa kategoria „Charakter Działania”

[P] = A — wpływa na pytanie „czy mogę teraz” tak samo jak pogoda.

**4. Opis zakupów w specyfikacji** — zakupy można opisać jako widok albo jako osobny cel (D-14).
- **A)** wariant przypadku „Wybrać i wykonać Następne działanie” i definicja Widoku sklepów w słowniku
- **B)** osobny przypadek użycia „Zrobić zakupy”

[P] = A — cel jest ten sam (zrobić Działanie), zmienia się tylko filtr.

**5. Osoba w modelu** — przy modelu z decyzji 1 Osoba staje się po prostu typem Kontekstu (D-15).
- **A)** Osoba to Kontekst typu Osoba, a Etykieta to po prostu Kontekst
- **B)** Osoba zostaje osobnym rodzajem Etykiety, jak teraz

[P] = A — mniej pojęć, a Delegat i tak wskazuje tę samą Osobę.

**W kolejce**
- Gdzie trzymać repozytorium na stałe (twój komputer lub GitHub)
- Poprawka znacznika „[P]” w pliku kontraktu
- Znaczenie „trwale zapisany” w przechwyceniu (UC-01)
- Nowy przypadek użycia „Doprecyzować Element” (UC-03)
- Cel „Zarządzać Etykietami” na liście aktor–cel
- Reguła „Element nie wraca do Inboxu” jako wymaganie EARS

Odpowiedz „ok”, numerem z literą (np. „2B”), numerem z własnym tekstem albo „reszta ok”.

# USER
1a 2a 3b 4) mam pomysł żeby zakupy i lista przedmiotów do przygotowania mais in place byla osobna lista i jej odchaczenie bylo kryterium startu konkretnego zadania. Zobacz jak to wplywa na slownik i cała specyfikację i zapropnuj jak to zapiszemy
5a

# MODEL
Wprowadzam zatwierdzone decyzje 1, 2, 3 i 5. Najpierw sprawdzam aktualny stan dokumentu.

Zatwierdzone decyzje są już w słowniku. Teraz aktualizuję rejestr decyzji.

Eksportuję oba zmienione pliki, żeby sprawdzić diff.

Wprowadziłem zatwierdzone decyzje do słownika (model Kontekstów z czterema Typami, Charakter Działania, Osoba jako Typ Kontekstu) i zrobiłem commit `889d438`.

## Lista przygotowania (mise en place) — wpływ na specyfikację

Twój pomysł wprowadza do modelu nowy rodzaj warunku. Do tej pory mieliśmy dwa: **Kontekst** („czy *mogę* teraz”, sprawdzany w danej chwili) i **koszt** („czy *dam radę*”). Lista przygotowania to trzeci warunek: **„czy *mam* wszystko, czego potrzebuję”**. Taki warunek nie jest prawdziwy ani fałszywy w danej chwili, tylko spełnia się raz i zostaje spełniony. Dlatego nie pasuje ani do Kontekstu, ani do atrybutów i potrzebuje własnej grupy pojęć.

**Przykład:** Działanie „Pomalować sypialnię” ma Listę przygotowania: farba (@Castorama LUB @Obi), wałek (@Castorama), taśma malarska (@dom). Dopóki choć jedna Pozycja nie jest odhaczona, Działanie nie jest Gotowe. Pozycje do kupienia pojawiają się w widoku sklepu, a po odhaczeniu ostatniej Działanie trafia na listę Następnych działań.

**Co się zmienia:**

| Obszar | Zmiana |
|---|---|
| Słownik | Nowa grupa **G-PRZ**: Lista przygotowania, Pozycja przygotowania (nazwa, 0..* Miejsc pozyskania, odhaczona tak/nie), Gotowość Działania (wyliczana), Widok zakupów (nieodhaczone Pozycje z Miejscem kategorii Sklep, pogrupowane po sklepie) |
| Granica z Narzędziem | Narzędzie (G-ETK-07) to coś, co masz i musisz mieć przy sobie. Pozycja to coś, co trzeba zdobyć albo przygotować. Wiertarka w szafie to Narzędzie, wiertło do kupienia to Pozycja |
| Lista In/Out | Listy zakupów przechodzą z poza zakresu do zakresu |
| Lista aktor–cel | Nowy cel „Zebrać Pozycje przygotowania” (poziom morza); „Doprecyzować Element” (UC-03) dostaje opcjonalny krok dodania Listy |
| Maszyna stanów | Bez nowych stanów, jeśli Gotowość jest wyliczana. To strażnik (guard), tak jak przy Utkniętym projekcie |
| EARS | Na przykład: *While an Action has an unchecked Preparation Item, GTD-App shall exclude it from Next Action views.* Oraz: *When the last Preparation Item is checked, GTD-App shall include the Action in Next Action views.* |
| Zgodność z GTD | GTD unika zależności między zadaniami. Pozycja jako lekki punkt listy, a nie osobne Działanie, zachowuje tę zasadę. Dlatego decyzja 1 jest kluczowa |

**Jak to zapiszemy:** po twoich decyzjach dodam do słownika sekcję „Przygotowanie” z identyfikatorami G-PRZ-01…04. Do In/Out i aktor–cel dopiszę zmiany jako rekordy z odnośnikiem do decyzji (np. „D-14 → zakupy In”). Nowy cel dostanie brief UC-04 w tym samym formacie co UC-01 i UC-02.

---

**Wykonane**
- Słownik: Kontekst ma teraz dokładnie jeden Typ: Miejsce, Narzędzie, Osoba albo Okoliczność (G-ETK-05…08).
- Słownik: nowe pojęcia Kategoria Miejsca (G-ETK-09) i Reguła dopasowania „Miejsca LUB, reszta I” (G-ETK-10).
- Słownik: nowy atrybut Charakter Działania (G-ATR-09), np. brudna robota.
- Słownik: Etykieta to synonim Kontekstu; Wybór Kontekstu i Widok Kontekstów zastąpiły wersje „etykietowe”.
- Rejestr: decyzje D-11…D-15 rozstrzygnięte, D-16…D-20 otwarte, K-05…K-08 dodane do kolejki.
- Git: diff sprawdzony (62 identyfikatory, zmiany tylko tam, gdzie zamierzone), commit `889d438`.

**Decyzje**

**1. Czym jest Pozycja przygotowania** — od tego zależy, czy model wprowadza zależności między zadaniami (D-16).
- **A)** lekki punkt listy, nie Element (bez Stanu, tylko nazwa, Miejsca i odhaczenie)
- **B)** pełne Działanie („Kupić farbę”) powiązane z Działaniem głównym

[P] = A — B to zależności między zadaniami, które GTD odrzuca i które są poza zakresem.

**2. Widoczność Działania nieprzygotowanego** — trzeba ustalić, czy Działanie z nieodhaczonymi Pozycjami pokazuje się na liście Następnych działań (D-17).
- **A)** ukryte na listach Następnych działań, widoczne w Projekcie i w swojej Liście
- **B)** widoczne z oznaczeniem „nieprzygotowane”

[P] = A — na liście Następnych działań ma być tylko to, co da się zacząć teraz; tak rozumiem twoje „kryterium startu”.

**3. Gotowość w modelu** — trzeba ustalić, czy to osobny Stan, czy coś wyliczanego (D-18).
- **A)** atrybut wyliczany (Gotowe / Nieprzygotowane), Stany bez zmian
- **B)** nowy Stan Elementu „Przygotowywane”

[P] = A — działa tak jak Utknięty i nie dokłada przejść w maszynie stanów.

**4. Działanie nieprzygotowane a Utknięty projekt** — trzeba ustalić, czy projekt z samym nieprzygotowanym Działaniem jest Utknięty (D-19).
- **A)** liczy się jako Otwarte działanie, więc projekt nie jest Utknięty
- **B)** nie liczy się, więc projekt jest Utknięty

[P] = A — nieodhaczone Pozycje są realnym następnym krokiem, więc projekt nie stoi.

**5. Zakupy jako przypadek użycia** — trzeba ustalić, jak opisać zbieranie Pozycji w sklepie (D-20).
- **A)** nowy cel „Zebrać Pozycje przygotowania” (UC-04)
- **B)** wariant przypadku „Wybrać i wykonać Następne działanie”

[P] = A — w sklepie odhaczasz Pozycje, a nie wykonujesz Działań, więc to inny cel.

**W kolejce**
- Pozycja wspólna dla kilku Działań
- Ponowne odznaczenie Pozycji (np. zużyta)
- Gdzie trzymać repozytorium na stałe (twój komputer lub GitHub)
- Poprawka znacznika „[P]” w pliku kontraktu
- Znaczenie „trwale zapisany” w przechwyceniu (UC-01)
- Nowy przypadek użycia „Doprecyzować Element” (UC-03)
- Cel „Zarządzać Kontekstami” na liście aktor–cel
- Reguła „Element nie wraca do Inboxu” jako wymaganie EARS

Odpowiedz „ok”, numerem z literą (np. „2B”), numerem z własnym tekstem albo „reszta ok”.

# USER
Generalna sugestia. Chciałbym aby system nie był paeywnym rejestrem a bardziej pomagał użytkownikowi wykonywać progress. Drive user home principle.

1a 2b widoczne i zachęcające do akcji. Przygotuj się i po kliknięciu pojawi się widok checklisty narzedzi do skompletowania.
3 nie wiem przeanalizuj konsekwencje i zapropnuj
4) tak system utkniety ale zmieńmy perspektywę że system ma byc pro active tak jak pisałem wyżej wszędzie tam gdzie może.
5) widzę takie zadanie i jak klikam to system pokazuje listę zakupową a pod nia liste narzedzi z domu do skompletowania żeby przystąpić do wykonania zadania. rozumiesz

# MODEL
Wprowadzam zatwierdzone decyzje (1A, 2B) i twoją zasadę proaktywności, a potem przechodzę do analizy.

Teraz rejestr decyzji.

Rozmiary plików zgadzają się z eksportem co do bajta (21522 i 3956), a w słowniku jest 67 identyfikatorów (62 wcześniejsze i 5 nowych). Commituję.

Tak, rozumiem. Opiszę to na przykładzie, żeby sprawdzić, czy mamy ten sam obraz:

> Na liście Następnych działań widzisz „Pomalować sypialnię” z przyciskiem **Przygotuj się**. Klikasz i otwiera się checklista:
> **Do kupienia:** Castorama: farba, wałek · Rossmann: rękawiczki
> **Do skompletowania z domu:** drabina, folia malarska, taśma
> Odhaczasz Pozycje po kolei. Po odhaczeniu ostatniej przycisk zmienia się na „Zacznij”.

Twoja zasada ZP-01 („system prowadzi do postępu, a nie tylko rejestruje”) jest już zapisana w specyfikacji jako zasada projektowa. Od teraz sprawdzam każdy stan pod kątem tego, jakie wezwanie do działania mu towarzyszy. Ta zasada stoi jednak w sprzeczności z jedną wcześniejszą decyzją: przy Dacie kontroli ustaliliśmy „bez powiadomienia”. Dodałem do kolejki przegląd wcześniejszych decyzji pod tym kątem.

**Analiza decyzji 3: Gotowość jako Stan czy jako atrybut wyliczany**

Rozstrzyga jeden przypadek: „Malowanie w sobotę, farba jeszcze niekupiona”. To Działanie jest jednocześnie **Zaplanowane** i **nieprzygotowane**. Gdyby „Przygotowywane” było Stanem, Działanie musiałoby wybrać jeden z dwóch, a oba są prawdziwe. Gotowość to po prostu inna oś niż Stan.

| Konsekwencja | A) atrybut wyliczany | B) nowy Stan |
|---|---|---|
| Działanie Zaplanowane i nieprzygotowane naraz | działa | trzeba wybrać jeden Stan |
| Źródło prawdy | odhaczenia Pozycji; nie da się rozjechać | Stan i odhaczenia mogą sobie przeczyć |
| Maszyna stanów | bez zmian | nowe przejścia przy każdym odhaczeniu i dodaniu Pozycji |
| Proaktywność (ZP-01) | w piątek: „Sobota: malowanie, brakują 2 Pozycje. Przygotuj się” | to samo, ale trudniejsze do opisania |

---

**Wykonane**
- Słownik: nowa sekcja „Zasady projektowe” z zasadą ZP-01 Prowadzenie do postępu.
- Słownik: nowa grupa „Przygotowanie”: Lista przygotowania, Pozycja (lekki punkt, nie Element), Sposób pozyskania (Zakup / Skompletowanie), Działanie nieprzygotowane z przyciskiem „Przygotuj się”, Widok przygotowania (najpierw zakupy według sklepów, pod nimi rzeczy z domu).
- Rejestr: D-16, D-17, D-20 i ZP-01 rozstrzygnięte; D-18 i D-19 doprecyzowane; nowe D-21…D-23; K-09 w kolejce.
- Git: diff sprawdzony, commit `6c4fbb4`.

**Decyzje**

**1. Gotowość Działania w modelu** — po analizie powyżej (D-18).
- **A)** atrybut wyliczany z odhaczeń Pozycji, Stany bez zmian
- **B)** nowy Stan Elementu „Przygotowywane”

[P] = A — Działanie może być jednocześnie Zaplanowane i nieprzygotowane, a Stan tego nie wyrazi.

**2. Projekt, którego jedynym krokiem jest przygotowanie** — napisałeś „utknięty, ale proaktywnie”. Chcę się upewnić, jak to rozumiesz, bo krok „Przygotuj się” jest widoczny i wiadomo, co robić (D-19).
- **A)** projekt jest Utknięty, a obok niego wezwanie „Przygotuj się”
- **B)** nowy wyliczany status „Wymaga przygotowania” z tym wezwaniem; Utknięty tylko wtedy, gdy nie ma żadnego kroku

[P] = B — „Utknięty” zostaje sygnałem „nie wiadomo, co dalej”, a tutaj wiadomo.

**3. Narzędzie a rzecz z domu do skompletowania** — wiertarka może być Kontekstem typu Narzędzie albo Pozycją do skompletowania i trzeba wybrać jedno (D-21).
- **A)** Narzędzie tylko dla rzeczy zawsze przy sobie (telefon, komputer); rzeczy zbierane z domu to Pozycje
- **B)** narzędzia z domu zostają Kontekstem i automatycznie trafiają do Widoku przygotowania

[P] = A — rzecz z domu kompletujesz raz przed zadaniem, a to jest odhaczenie, a nie warunek sprawdzany w danej chwili.

**4. Zakupy widoczne w sklepie** — trzeba ustalić, czy w Castoramie widzisz zakupy ze wszystkich swoich Działań, czy tylko z jednego (D-22).
- **A)** tak, Widok Kontekstu sklepu pokazuje Pozycje do kupienia ze wszystkich Działań
- **B)** tylko w Widoku przygotowania danego Działania

[P] = A — to twój wcześniejszy pomysł „wejść w kontekst i odfiltrować sklep” i dobry przykład ZP-01.

**5. Przygotowanie jako przypadek użycia** — trzeba ustalić miejsce przygotowania w liście aktor–cel (D-23).
- **A)** nowy cel „Przygotować Działanie” (UC-04), uruchamiany przyciskiem „Przygotuj się” albo ze sklepu
- **B)** rozszerzenie przypadku „Wybrać i wykonać Następne działanie”

[P] = A — przygotowanie ma własny efekt (wszystko skompletowane) i może się odbywać kiedy indziej niż wykonanie.

**W kolejce**
- Przegląd wcześniejszych decyzji pod kątem ZP-01 (np. Data kontroli bez powiadomienia)
- Pozycja wspólna dla kilku Działań
- Ponowne odznaczenie Pozycji (np. zużyta)
- Gdzie trzymać repozytorium na stałe (twój komputer lub GitHub)
- Poprawka znacznika „[P]” w pliku kontraktu
- Znaczenie „trwale zapisany” w przechwyceniu (UC-01)
- Nowy przypadek użycia „Doprecyzować Element” (UC-03)
- Cel „Zarządzać Kontekstami” na liście aktor–cel
- Reguła „Element nie wraca do Inboxu” jako wymaganie EARS

Odpowiedz „ok”, numerem z literą (np. „2A”), numerem z własnym tekstem albo „reszta ok”.

# USER
Przemysl to kompleksowo
1a 2b 3 potrzebuje rozjasnienia jak to widzisz bo sie zgubilem 4 ) moge kliknac pokaz dla wszystkich projektow albo dla obecnego dzialania. Chyba ze wejde do widoku od strony etykiet to od razu widze wszystkiej . przemysl jak to jest np. w todoist
5a

# MODEL
Najpierw sprawdzę, jak Todoist obsługuje widok etykiet, filtry i podzadania, żeby porównanie opierało się na aktualnym stanie, a nie na mojej pamięci.

Wprowadzam do słownika zatwierdzone decyzje 1A i 2B oraz twoją odpowiedź w punkcie 4.

Rejestr i brief nowego przypadku użycia UC-04 (decyzja 5A).

Zmiany są w dokumencie. Odwzorowuję je w plikach lokalnych i porównam z eksportem.

Teraz porównuję z eksportem z dokumentu.

Zgadza się co do bajta (23501), bez ponownego kopiowania całej treści. Teraz rejestr.

Najpierw wyjaśnienie punktu 3, potem porównanie z Todoist.

**Punkt 3: dwa rodzaje „rzeczy potrzebnych do zadania”**

Granicę wyznacza jedno pytanie: **czy sprawdzasz to w danej chwili, czy kompletujesz raz przed konkretnym zadaniem?**

| | Narzędzie (Kontekst) | Pozycja do Skompletowania |
|---|---|---|
| Przykład | telefon, komputer | drabina z piwnicy, folia, wiertarka z garażu |
| Pytanie | „Czy mam to *teraz* przy sobie?” | „Czy przyniosłem to *do tego zadania*?” |
| Jak działa | filtr: pokaż, co mogę zrobić przy komputerze | checklista: odhaczam, gdy przyniosę |
| Po zadaniu | nic się nie zmienia, następnym razem znów sprawdzam | sprawa zamknięta |

Opcja B (wiertarka jako Kontekst @wiertarka) w praktyce zamienia się w opcję A. System nie wie, czy już przyniosłeś wiertarkę, więc i tak musiałbyś ją odhaczyć, tylko pod inną nazwą. Dodatkowo lista Kontekstów zapchałaby się dziesiątkami przedmiotów.

**Punkt 4: jak to wygląda w Todoist**

| Potrzeba | Todoist | GTD-App |
|---|---|---|
| Wszystko z danego sklepu, ze wszystkich projektów | widok etykiety albo filtr `%Castorama` obejmuje wszystkie projekty | Widok Kontekstu sklepu: Pozycje do kupienia i Działania ze wszystkich Działań |
| Zawężenie do jednego projektu | filtr `%Castorama & #Remont` | przełącznik zakresu w Widoku przygotowania |
| Rzeczy potrzebne do zadania | podzadania; nie blokują zadania nadrzędnego, a w widokach etykiet i filtrów są spłaszczone, bez hierarchii | Lista przygotowania; Gotowość wyliczana; przycisk „Przygotuj się” |
| Podpowiadanie następnego kroku | brak | zasada ZP-01 |

Twój pomysł robi więc to, czego Todoist nie potrafi: lista rzeczy blokuje start zadania i prowadzi cię do niego. Widok sklepu działa natomiast tak jak widok etykiety w Todoist. Przy okazji: Todoist zmienia składnię etykiet w filtrach z `@` na `%`, a `@` ma przestać działać do końca 2026 roku. Jeśli masz zapisane filtry z `@`, warto je przepisać.

---

**Wykonane**
- Słownik: nowy atrybut Gotowość Działania (G-PRZ-06), wyliczany i niezależny od Stanu.
- Słownik: nowy status projektu „Wymaga przygotowania” (G-PRJ-09) z przyciskiem „Przygotuj się”; „Utknięty” tylko wtedy, gdy nie ma żadnego kroku.
- Słownik: Widok przygotowania ma przełącznik zakresu „to Działanie / wszystkie”; widok sklepu pokazuje zakupy ze wszystkich Działań.
- Dokument: brief UC-04 Przygotować Działanie.
- Rejestr: D-18, D-19, D-22, D-23 rozstrzygnięte; nowe D-24…D-26.
- Git: rozmiary plików zgadzają się z eksportem (23501 i 4274 bajty), w słowniku 69 identyfikatorów, commit `3ef7daf`.

**Bez odpowiedzi**

**1. Narzędzie a rzecz z domu do skompletowania** — wyjaśnienie powyżej (D-21).
- **A)** Narzędzie tylko dla rzeczy zawsze przy sobie; rzeczy przynoszone przed zadaniem to Pozycje do Skompletowania
- **B)** wszystkie narzędzia jako Kontekst, a Widok przygotowania pokazuje je jako checklistę

[P] = A — B i tak kończy się odhaczaniem, a do tego zaśmieca listę Kontekstów.

**Decyzje**

**2. Domyślny zakres po kliknięciu „Przygotuj się”** — przełącznik już jest; chodzi o to, co widzisz na start (D-24).
- **A)** to Działanie, z przełącznikiem „Wszystkie”
- **B)** od razu wszystkie Działania nieprzygotowane

[P] = A — klikasz konkretne zadanie, więc oczekujesz jego listy.

**3. Układ widoku sklepu** — w widoku sklepu są teraz dwa rodzaje rzeczy: Pozycje do kupienia i Działania wykonywane w tym miejscu (D-25).
- **A)** dwie sekcje: „Do kupienia” nad „Działaniami”
- **B)** jedna wspólna lista

[P] = A — w sklepie najpierw kupujesz, a Pozycje i Działania odhacza się w różny sposób.

**4. Utknięty projekt** — zgodnie z twoją zasadą proaktywności (ZP-01) Utknięty też powinien mieć wezwanie do działania (D-26).
- **A)** przy Utkniętym projekcie przycisk „Zdefiniuj następne działanie”
- **B)** tylko oznaczenie „Utknięty”

[P] = A — to jest dokładnie „prowadź mnie do postępu”.

**W kolejce**
- Przegląd wcześniejszych decyzji pod kątem ZP-01 (np. Data kontroli bez powiadomienia)
- Pozycja wspólna dla kilku Działań (szczególnie w widoku „wszystkie”)
- Ponowne odznaczenie Pozycji (np. zużyta)
- Gdzie trzymać repozytorium na stałe (twój komputer lub GitHub)
- Poprawka znacznika „[P]” w pliku kontraktu
- Znaczenie „trwale zapisany” w przechwyceniu (UC-01)
- Nowy przypadek użycia „Doprecyzować Element” (UC-03)
- Cel „Zarządzać Kontekstami” na liście aktor–cel
- Reguła „Element nie wraca do Inboxu” jako wymaganie EARS

Odpowiedz „ok”, numerem z literą (np. „2B”), numerem z własnym tekstem albo „reszta ok”.

Sources:
- [Introduction to filters – Todoist Help](https://www.todoist.com/help/articles/introduction-to-filters-V98wIH)
- [Use sub-tasks in Todoist – Todoist Help](https://www.todoist.com/help/todoist/features/use-sub-tasks-in-todoist-kMamDo)
- [Introduction to labels – Todoist Help](https://www.todoist.com/help/articles/introduction-to-labels-dSo2eE)

# USER
1a 2a 3a 4 jaką konkretna scenke/scenariusz mozesz przywolac zeby to pokazac czy to ma sens dla A

# MODEL
Wprowadzam decyzje 1A, 2A i 3A, a potem opiszę scenkę do punktu 4.

Rejestr:

Synchronizuję pliki lokalne.

Tak, mam scenkę. Pokazuje ona, że A ma sens, ale nie wystarcza.

**Scenka 1: A działa**
Czwartek, Kasia stoi w kolejce w Castoramie i odhacza ostatnie działanie projektu „Remont łazienki”: „Odebrać płytki”. System pyta: „Co dalej z tym projektem?”. Kasia ma zajęte ręce, więc pomija pytanie. Projekt zostaje bez następnego działania.

- **Bez wezwania (B):** projekt dostaje szare oznaczenie „Utknięty”. Kasia zauważy je dopiero w piątkowym przeglądzie, o ile w ogóle. Przez tydzień płytki leżą w przedpokoju.
- **Z wezwaniem (A):** w piątek rano Kasia otwiera listę projektów, a przy łazience widzi przycisk „Zdefiniuj następne działanie”. Jedno kliknięcie, wpisuje „Zadzwonić do glazurnika i umówić termin”, dodaje @telefon. Projekt rusza od razu, bez czekania na przegląd.

**Scenka 2: A przestaje wystarczać**
Projekt „Zbudować altanę”. Kasia doszła do etapu, którego nie zrobi przed wiosną. Projekt jest Utknięty, a system codziennie podsuwa jej „Zdefiniuj następne działanie”. Następnego działania nie ma i nie będzie do marca, więc przycisk staje się wyrzutem sumienia, a nie pomocą. Po kilku dniach Kasia przestaje go zauważać, a to szkodzi wszystkim pozostałym wezwaniom.

GTD daje na to odpowiedź: projekt bez następnego kroku ma **trzy uczciwe wyjścia**. Można dopisać następne działanie, odłożyć projekt na Kiedyś/może albo uznać go za zakończony. Dlatego proponuję opcję C. To ZP-01 w dobrej wersji: system nie naciska na jeden ruch, tylko pokazuje, które ruchy są możliwe.

---

**Wykonane**
- Słownik: Narzędzie (G-ETK-07) obejmuje tylko rzeczy sprawdzane w danej chwili; rzecz przynoszona przed zadaniem to Pozycja do Skompletowania; @wiertarka usunięta z przykładów Kontekstu.
- Słownik: Widok przygotowania otwiera się domyślnie dla danego Działania, z przełącznikiem „Wszystkie”.
- Słownik: widok sklepu ma dwie sekcje: „Do kupienia” nad „Działaniami”.
- UC-04: punkty do rozstrzygnięcia zastąpione ustaleniami.
- Rejestr: D-21, D-24, D-25 rozstrzygnięte; D-26 przeformułowane z opcją C.
- Git: rozmiary plików zgadzają się z eksportem (23764 i 4188 bajtów), commit `f24c3c3`.

**Bez odpowiedzi**

**1. Wezwanie przy Utkniętym projekcie** — po scenkach powyżej dodałem trzecią opcję (D-26).
- **A)** jeden przycisk: „Zdefiniuj następne działanie”
- **B)** tylko oznaczenie „Utknięty”
- **C)** trzy wyjścia: dodaj następne działanie / odłóż na Kiedyś/może / zakończ projekt

[P] = C — przy projekcie świadomie wstrzymanym pojedynczy przycisk zamienia się w wyrzut sumienia, a C daje uczciwe wyjście.

**W kolejce**
- Przegląd wcześniejszych decyzji pod kątem ZP-01 (np. Data kontroli bez powiadomienia)
- Pozycja wspólna dla kilku Działań (szczególnie w widoku „Wszystkie”)
- Ponowne odznaczenie Pozycji (np. zużyta)
- Gdzie trzymać repozytorium na stałe (twój komputer lub GitHub)
- Poprawka znacznika „[P]” w pliku kontraktu
- Znaczenie „trwale zapisany” w przechwyceniu (UC-01)
- Nowy przypadek użycia „Doprecyzować Element” (UC-03)
- Cel „Zarządzać Kontekstami” na liście aktor–cel
- Reguła „Element nie wraca do Inboxu” jako wymaganie EARS

Odpowiedz „ok”, „1A”/„1B”/„1C” albo numerem z własnym tekstem.


# USER
1c

# MODEL
Zapisane: przy Utkniętym projekcie system pokazuje trzy wyjścia. W rejestrze nie ma już otwartych decyzji.

---

**Wykonane**
- Słownik: Utknięty projekt (G-PRJ-04) pokazuje trzy wezwania: Dodaj następne działanie, Odłóż na Kiedyś/może, Zakończ projekt.
- Rejestr: D-26 rozstrzygnięte; sekcja otwartych decyzji jest pusta.
- Git: rozmiary plików zgadzają się z eksportem (23905 i 4081 bajtów), commit `89c8ebe`. W repozytorium jest już 6 commitów.

**Decyzje**

**1. Gdzie trzymać repozytorium na stałe** — historia gita leży teraz w moim tymczasowym workspace, który po dłuższej bezczynności zostanie usunięty razem z nią (K-05).
- **A)** prywatne repozytorium na twoim GitHubie (zakładasz puste, ja wysyłam do niego całą historię)
- **B)** folder na twoim komputerze, przez połączenie z aplikacją desktopową

[P] = A — historia przetrwa niezależnie od tego, czy komputer jest włączony, a w każdej nowej sesji mogę od niej zacząć.

**W kolejce**
- Przegląd wcześniejszych decyzji pod kątem ZP-01 (np. Data kontroli bez powiadomienia)
- Pozycja wspólna dla kilku Działań (szczególnie w widoku „Wszystkie”)
- Ponowne odznaczenie Pozycji (np. zużyta)
- Poprawka znacznika „[P]” w pliku kontraktu
- Znaczenie „trwale zapisany” w przechwyceniu (UC-01)
- Nowy przypadek użycia „Doprecyzować Element” (UC-03)
- Cel „Zarządzać Kontekstami” na liście aktor–cel
- Reguła „Element nie wraca do Inboxu” jako wymaganie EARS

Odpowiedz „ok”, „1A”/„1B” albo numerem z własnym tekstem.

# USER
1b zapisz w Pyprojects/gtd2

# MODEL
Sprawdzam, co jest dostępne na twoim komputerze.

Folder `gtd2` już istnieje i ma świeżo założone, puste repozytorium (zapewne właśnie je utworzyłeś). Sprawdzam jego stan.

Repozytorium jest puste, więc przeniosę całą historię jednym pakietem (git bundle), bez utraty commitów.

Do katalogu `.git` nie mogę zapisywać plików bezpośrednio. Przekażę więc pakiet przez katalog roboczy powłoki na twoim komputerze, a git sam wpisze historię.

Repozytorium działa. Zapisuję też samą decyzję w rejestrze.

Teraz ta sama zmiana w pliku w gtd2 i commit na twoim komputerze.

Plik zgadza się z dokumentem (4105 bajtów). Commituję w gtd2.

Gotowe, repozytorium jest teraz w **PycharmProjects/gtd2** na twoim Macu (folder `Pyprojects` nie istnieje, więc przyjąłem, że chodziło o PycharmProjects). Ma pełną historię, wszystkie 6 commitów, plus nowy commit z tą decyzją. Od teraz commituję bezpośrednio tam, a kopia w moim workspace przestaje być potrzebna.

Jedna rzecz techniczna. Na twoim komputerze nie mogę niczego usuwać bez twojej zgody, a git przy każdym commicie zostawia po sobie pliki blokad (`.lock`). Gdyby zostały pod oryginalnymi nazwami, twój git w PyCharmie zgłaszałby błąd „File exists”. Dlatego po każdym commicie przenoszę je pod nazwy `stale-…` w katalogu `.git`. Nic nie blokują, ale w `.git` zbiera się trochę śmieci; jest tam też pakiet z historią (`gtd-spec.bundle`).

---

**Wykonane**
- Dostęp do folderu PycharmProjects przyznany na tę sesję.
- Historia (6 commitów) przeniesiona do gtd2 przez pakiet git bundle; HEAD wskazuje `89c8ebe`.
- Pozostałe blokady gita przeniesione pod nazwy `stale-…` w `.git` (nic nie usunięte).
- Rejestr: D-27 „repozytorium w PycharmProjects/gtd2” rozstrzygnięte; K-05 usunięte z kolejki (w dokumencie i w pliku, rozmiar 4105 bajtów zgodny z eksportem).
- Git w gtd2: commit `fb9da5e`.

**Decyzje**

**1. Sprzątanie po gicie w gtd2** — narzędzie daje zgodę na usuwanie tylko dla całego folderu PycharmProjects (87 projektów), a nie dla samego gtd2.
- **A)** zgoda na usuwanie w PycharmProjects na tę sesję; git sprząta po sobie normalnie
- **B)** bez zgody; dalej przenoszę blokady pod nazwy `stale-…`, a na koniec pracy podam ci listę do skasowania

[P] = B — twoje pozostałe projekty zostają poza zasięgiem jakiegokolwiek usuwania, a śmieci w `.git` są małe i nieszkodliwe.

**2. Folder `.idea` w repozytorium** — PyCharm trzyma w nim swoje ustawienia; teraz jest nieśledzony i pokazuje się w `git status`.
- **A)** dodać `.idea/` do `.gitignore`
- **B)** zostawić jak jest

[P] = A — to ustawienia IDE, a nie część specyfikacji.

**W kolejce**
- Przegląd wcześniejszych decyzji pod kątem ZP-01 (np. Data kontroli bez powiadomienia)
- Pozycja wspólna dla kilku Działań (szczególnie w widoku „Wszystkie”)
- Ponowne odznaczenie Pozycji (np. zużyta)
- Poprawka znacznika „[P]” w pliku kontraktu
- Znaczenie „trwale zapisany” w przechwyceniu (UC-01)
- Nowy przypadek użycia „Doprecyzować Element” (UC-03)
- Cel „Zarządzać Kontekstami” na liście aktor–cel
- Reguła „Element nie wraca do Inboxu” jako wymaganie EARS

Odpowiedz „ok”, numerem z literą (np. „1A”), numerem z własnym tekstem albo „reszta ok”.

# USER
1a 2a

# MODEL
Posprzątane. Sprawdzam integralność repozytorium i zapisuję obie decyzje w rejestrze.

Obie decyzje są wykonane. Git w gtd2 działa już normalnie: sprząta po sobie, nie zostawia blokad, a status repozytorium jest czysty.

**Wykonane**
- Zgoda na usuwanie w PycharmProjects (na tę sesję); usunąłem wyłącznie pozostałości gita w `gtd2/.git`: 4 przeniesione blokady, 5 plików tymczasowych i pakiet z historią.
- `git fsck` bez błędów, więc repozytorium jest spójne.
- Dodany plik `.gitignore` z `.idea/`.
- Rejestr: D-28 i D-29 rozstrzygnięte (rozmiar pliku 4333 bajty, zgodny z dokumentem).
- Git w gtd2: commit `acdace9`, czyli 8 commitów w historii.

**W kolejce**
- Przegląd wcześniejszych decyzji pod kątem ZP-01 (np. Data kontroli bez powiadomienia)
- Pozycja wspólna dla kilku Działań (szczególnie w widoku „Wszystkie”)
- Ponowne odznaczenie Pozycji (np. zużyta)
- Poprawka znacznika „[P]” w pliku kontraktu
- Znaczenie „trwale zapisany” w przechwyceniu (UC-01)
- Nowy przypadek użycia „Doprecyzować Element” (UC-03)
- Cel „Zarządzać Kontekstami” na liście aktor–cel
- Reguła „Element nie wraca do Inboxu” jako wymaganie EARS

Nie ma otwartych decyzji. Proponuję zacząć od przeglądu pod kątem ZP-01, bo ta zasada może zmienić kilka wcześniejszych ustaleń. Napisz „dalej” albo wskaż inny temat z kolejki.

# USER
dalej

# MODEL
Przeglądam wszystkie dotychczasowe ustalenia pod kątem ZP-01. Pytanie przy każdym brzmi tak samo: czy w tym miejscu system tylko pokazuje stan, czy też podsuwa następny krok?

| Pojęcie / ustalenie | Dziś (biernie) | Pod kątem ZP-01 |
|---|---|---|
| Data kontroli przy Czekam na (G-ATR-07) | wyróżnienie „zaległe”, bez powiadomień | wezwanie przy Działaniu: „Skontaktuj się z Markiem” / „Przesuń kontrolę” → **decyzja 1** |
| Zaplanowane i Nieprzygotowane (G-ATR-04 + G-PRZ-06) | „Przygotuj się” pojawia się dopiero przy Działaniu | wezwanie z wyprzedzeniem przed datą → **decyzja 2** |
| Inbox (G-ELM-14) | licznik Elementów | wezwanie „Opróżnij Inbox” → **decyzja 3** |
| Doprecyzowanie, reguła 2 minut (G-OPR-05) | Użytkownik sam pamięta o regule | „Zrób teraz” jako pierwsza opcja → **decyzja 4** |
| Przegląd tygodniowy (G-OPR-13) | przypomnienie po 7 dniach i checklista | przegląd prowadzony krok po kroku → **decyzja 5** |
| Utknięty projekt (G-PRJ-04) | już ma trzy wyjścia (D-26) | bez zmian |
| Kosz bez automatycznego usuwania | — | bez zmian; bezpieczeństwo ma pierwszeństwo przed proaktywnością |
| Granica 12 miesięcy dla Projektu | tylko wskazówka | bez zmian; to porada, a nie krok do wykonania |
| Delegowanie bez powiadamiania Delegata | — | bez zmian; kontakt z Delegatem obsługuje decyzja 1 |

Zapisuję te decyzje w rejestrze jako otwarte, zamiast punktu K-09 w kolejce.

Przegląd zakończony: pięć miejsc w specyfikacji jest dziś biernych, cztery zostają bez zmian, bo mają ku temu powód. Poniżej decyzje dla tych pięciu.

**Wykonane**
- Przegląd wszystkich pojęć i decyzji pod kątem ZP-01 (tabela wyżej).
- Rejestr: K-09 zastąpione pięcioma otwartymi decyzjami D-30…D-34 (rozmiar pliku 5031 bajtów, zgodny z dokumentem).
- Git w gtd2: commit `2dd3ffd`.

**Decyzje**

**1. Data kontroli przy „Czekam na”** — wcześniej wybrałeś „bez powiadomień”, a ZP-01 każe w tym miejscu podsunąć następny krok (D-30).
- **A)** dalej bez powiadomień, ale przy zaległym Działaniu przyciski „Skontaktuj się z [Delegatem]” i „Przesuń kontrolę”
- **B)** dodatkowo powiadomienie w dniu kontroli
- **C)** bez zmian

[P] = A — zachowuje twoją wcześniejszą decyzję (żadnego nagabywania) i dodaje gotowy ruch tam, gdzie i tak patrzysz.

**2. Przygotowanie przed zaplanowanym Działaniem** — malowanie jest w sobotę, a farba niekupiona; trzeba ustalić, kiedy system ma o tym przypomnieć (D-31).
- **A)** „Przygotuj się” pojawia się z wyprzedzeniem, domyślnie 2 dni przed datą, z możliwością zmiany
- **B)** tylko przy samym Działaniu, w dniu wykonania

[P] = A — w sobotę rano na zakupy jest już za późno.

**3. Niepusty Inbox** — dziś to tylko licznik Elementów (D-32).
- **A)** wezwanie „Opróżnij Inbox (N)” na ekranie głównym
- **B)** tylko licznik

[P] = A — opróżnianie Inboxu to najczęściej odkładany krok w GTD.

**4. Reguła 2 minut** — przy Doprecyzowaniu Użytkownik musi sam pamiętać, że krótkie rzeczy robi się od razu (D-33).
- **A)** „Zrób teraz” jako pierwsza, wyróżniona opcja Doprecyzowania
- **B)** wszystkie opcje równorzędne

[P] = A — system przypomina regułę w chwili, w której ma ona znaczenie.

**5. Przegląd tygodniowy** — dziś to przypomnienie i checklista do samodzielnego odhaczania (D-34).
- **A)** tryb prowadzony: system przechodzi Punkt po Punkcie i od razu otwiera właściwy Widok (Inbox, Projekty Utknięte, Czekam na…)
- **B)** checklista do samodzielnego odhaczania

[P] = A — Kasia mówiła, że przegląd to jej „świętość”; tryb prowadzony skraca go i nie pozwala pominąć kroku.

**W kolejce**
- Pozycja wspólna dla kilku Działań (szczególnie w widoku „Wszystkie”)
- Ponowne odznaczenie Pozycji (np. zużyta)
- Poprawka znacznika „[P]” w pliku kontraktu
- Znaczenie „trwale zapisany” w przechwyceniu (UC-01)
- Nowy przypadek użycia „Doprecyzować Element” (UC-03)
- Cel „Zarządzać Kontekstami” na liście aktor–cel
- Reguła „Element nie wraca do Inboxu” jako wymaganie EARS

Odpowiedz „ok”, numerem z literą (np. „2B”), numerem z własnym tekstem albo „reszta ok”.

# USER
1a 2a 3a 4a 5a Czy mozeliwe zamodelowanie ekranow i sterowania za pomoca mermaid tak zeby wizualnie zobaczyc czy nie ma powierzchni ucieczki oraz czy jest on elastyczny w nawigacji tam gdzie to korzystne

# MODEL
Najpierw wprowadzam decyzje 1–5 do słownika i rejestru, potem biorę się za model nawigacji.

Odwzorowuję zmiany w plikach w gtd2.

Uprawnienie do usuwania chyba wygasło (git znów nie mógł posprzątać). Sprawdzam to.

Repozytorium jest czyste (zgodę na usuwanie trzeba było powtórzyć, bo poprzednia wygasła). Teraz model nawigacji. Wczytuję zasady projektowania strony, bo diagram opublikuję jako stronę.

Najpierw model ekranów w Mermaid oraz skrypt, który automatycznie sprawdza go pod kątem pułapek i miejsc bez następnego kroku.

Skrypt znalazł dwa miejsca. Robię jeszcze test kontrolny: usuwam wyjście z ekranu Przechwyć, żeby sprawdzić, czy skrypt rzeczywiście wyłapie pułapkę.

Skrypt działa poprawnie. Teraz buduję stronę z diagramem i wynikami; wstawiam do niej plik `.mmd` skryptem, żeby strona i plik w repozytorium były identyczne.

Strona jest opublikowana. Teraz przenoszę pliki modelu do repozytorium gtd2 jednym archiwum.

Model jest w repozytorium. Na koniec zapisuję w rejestrze trzy nowe decyzje, które wynikają z mapy.

Tak, to możliwe i już działa. Strona „Mapa nawigacji GTD-App” pokazuje wszystkie 20 ekranów i przejścia między nimi jako diagram Mermaid, a pod nim wynik automatycznego sprawdzenia.

„Powierzchnię ucieczki” sprawdzam w dwóch znaczeniach:
- **Pułapka**: ekran, z którego nie da się wyjść. Wynik: brak pułapek. Pułapka może powstać tylko w przepływie bez paska nawigacji (Przechwyć, Doprecyzowanie, Przygotowanie, Przegląd), a każdy z nich ma wyjście. Celowo usunąłem jedno wyjście, żeby sprawdzić, czy skrypt to wychwyci, i wychwycił.
- **Wyciek**: miejsce, w którym przepływ się kończy, a system nie podsuwa następnego kroku, czyli łamie ZP-01. Skrypt znalazł dwa takie miejsca, opisane w decyzjach 1 i 2 poniżej.

Jeśli „powierzchnia ucieczki” znaczy u ciebie coś innego, napisz, a dodam kolejną regułę do sprawdzania.

**Elastyczność:** wszystkie kluczowe przejścia, o które chodziło w ostatnich decyzjach (sklep ↔ przygotowanie, Działanie ↔ Projekt, Czekam na → Działanie), zajmują 1 kliknięcie. Jedyna para na 2 kliknięcia to Doprecyzowanie → Następne działania, przez ekran „Inbox pusty”.

Model jest w gtd2/nawigacja. Ty lub ja zmieniamy `ekrany.mmd`, a `python3 sprawdz.py ekrany.mmd` od razu pokazuje, czy coś się zepsuło. `zbuduj.py` odświeża stronę z mapą. Skrypt zwraca kod błędu, gdy złamana jest któraś z twardych reguł (R1–R4), więc można go później podpiąć jako test.

---

**Wykonane**
- Słownik: decyzje D-30…D-34 zapisane przy pojęciach G-ATR-07, G-PRZ-04, G-ELM-15, G-OPR-05, G-OPR-13.
- Strona „Mapa nawigacji GTD-App”: diagram, legenda, wyniki reguł R1–R6.
- gtd2/nawigacja: `ekrany.mmd`, `sprawdz.py`, `zbuduj.py`, `szablon.html`, `mapa-nawigacji.html`.
- Rejestr: D-30…D-34 rozstrzygnięte, nowe otwarte D-35…D-37.
- Git w gtd2: commity `82c2cbb`, `efcdf94`, `245e305`; repozytorium czyste, bez blokad.

**Decyzje**

**1. Ekran „Projekt zakończony” bez następnego kroku** — skrypt zgłasza, że po zakończeniu projektu system tylko wraca do listy (D-35).
- **A)** wezwanie „Przejrzyj Kiedyś/może”, bo zwolniło się miejsce na coś nowego
- **B)** wezwanie „Pokaż Projekty Utknięte”
- **C)** bez wezwania

[P] = B — Utknięte projekty to zobowiązania, które już podjąłeś i które właśnie się sypią; mają pierwszeństwo przed nowymi.

**2. Przechwyć bez kroku naprzód** — po zapisaniu Elementu system tylko zamyka okno (D-36).
- **A)** celowy wyjątek od ZP-01, zapisany w zasadzie: przechwytywanie ma być błyskawiczne
- **B)** po zapisie opcja „Doprecyzuj teraz”

[P] = A — GTD rozdziela zbieranie od doprecyzowania; dodatkowe pytanie spowolni przechwytywanie, które ma trwać około sekundy.

**3. Skład paska nawigacji** — to założenie, które przyjąłem, rysując mapę (D-37).
- **A)** Start · Inbox · Działania · Projekty · Konteksty · (+) Przechwyć
- **B)** inny skład (napisz jaki)

[P] = A — to pięć miejsc, do których z mapy idzie się najczęściej; Czekam na, Kiedyś/może, Kalendarz i Kosz są pod Startem.

**W kolejce**
- Identyfikatory ekranów (E-xx) w słowniku i powiązanie ze śladem wymagań
- Pozycja wspólna dla kilku Działań (szczególnie w widoku „Wszystkie”)
- Ponowne odznaczenie Pozycji (np. zużyta)
- Poprawka znacznika „[P]” w pliku kontraktu
- Znaczenie „trwale zapisany” w przechwyceniu (UC-01)
- Nowy przypadek użycia „Doprecyzować Element” (UC-03)
- Cel „Zarządzać Kontekstami” na liście aktor–cel
- Reguła „Element nie wraca do Inboxu” jako wymaganie EARS

Odpowiedz „ok”, numerem z literą (np. „1A”), numerem z własnym tekstem albo „reszta ok”.

# USER
1b 2a 3a podlacz skrypt pod precommit

# MODEL

Wykonuję decyzje 1B, 2A i 3A, a potem podłączam skrypt pod pre-commit.

Teraz pliki w gtd2: słownik, rejestr, mapa i skrypt. Skrypt dostaje obsługę świadomych wyjątków od ZP-01, a reguła R5 staje się twarda, skoro trafia do pre-commit.

Wszystkie reguły przechodzą, a Przechwyć jest oznaczone jako świadomy wyjątek (D-36). Teraz hook pre-commit, zapisany w repozytorium (`.githooks`), żeby był wersjonowany razem ze skryptem.

Hook działa we wszystkich trzech testach. Dopisuję do README, jak go włączyć w nowym klonie, i sprawdzam zgodność plików z dokumentem.

Oba pliki zgadzają się z dokumentem (24649 i 5198 bajtów). Commit, który przy okazji przechodzi już przez nowy hook:

Odświeżam opublikowaną mapę nową wersją z repozytorium.

Gotowe: pre-commit w gtd2 blokuje teraz commit, jeśli mapa nawigacji łamie którąś z reguł albo strona z mapą jest nieaktualna. Hook jest w repozytorium (`.githooks/pre-commit`), więc zmienia się razem ze skryptem.

Sprawdziłem go na trzech przypadkach:
- **Poprawny stan:** commit przechodzi.
- **Usunięte wyjście z Przechwyć:** commit zablokowany, z pokazaną regułą i ekranem.
- **Zmieniona strona bez przebudowania mapy:** commit zablokowany, z poleceniem, które to naprawia.

Ostatni commit `47b5707` przeszedł już przez nowy hook.

Przy okazji zaostrzyłem regułę R5 („miejsce bez następnego kroku”): z ostrzeżenia stała się błędem blokującym commit. Świadome wyjątki, takie jak Przechwyć (D-36), zapisuje się teraz komentarzem `%% wyjatek-zp01: E02 (D-36)` w `ekrany.mmd`, a mapa pokazuje je osobno jako informację.

Hook sprawdza pliki w katalogu roboczym, a nie dokładnie to, co trafia do commita. Przy częściowym `git add` może więc przepuścić niespójny stan. W nowym klonie trzeba go włączyć jedną komendą: `git config core.hooksPath .githooks` (opisane w README).

Mapa nawigacji GTD-App ma już nową wersję. Wszystkie reguły są na zielono, a ekran „Projekt zakończony” ma wezwanie „Pokaż Projekty Utknięte”.

**Wykonane**
- Słownik: w ZP-01 dopisany wyjątek dla Przechwycenia (D-36); po Zakończeniu Projektu wezwanie „Pokaż Projekty Utknięte” (D-35).
- `ekrany.mmd`: nowe przejście E-19 → Projekty Utknięte, deklaracja wyjątku E-02, odnośnik do składu paska (D-37).
- `sprawdz.py`: obsługa wyjątków, R5 jako reguła twarda; strona z mapą pokazuje wyjątki jako „INFO”.
- Pre-commit: `.githooks/pre-commit` + `core.hooksPath`, przetestowany w 3 scenariuszach; instrukcja w README.
- Rejestr: D-35, D-36, D-37 rozstrzygnięte, brak otwartych decyzji (pliki zgodne z dokumentem: 24649 i 5198 bajtów).
- Git w gtd2: commit `47b5707`, repozytorium czyste.

**W kolejce**
- Identyfikatory ekranów (E-xx) w słowniku i powiązanie ze śladem wymagań
- Pozycja wspólna dla kilku Działań (szczególnie w widoku „Wszystkie”)
- Ponowne odznaczenie Pozycji (np. zużyta)
- Poprawka znacznika „[P]” w pliku kontraktu
- Znaczenie „trwale zapisany” w przechwyceniu (UC-01)
- Nowy przypadek użycia „Doprecyzować Element” (UC-03)
- Cel „Zarządzać Kontekstami” na liście aktor–cel
- Reguła „Element nie wraca do Inboxu” jako wymaganie EARS

Nie ma otwartych decyzji. Napisz „dalej” (wezmę pierwszy temat z kolejki) albo wskaż inny.

# USER
wejdz w role senior SW requirments inzyniera i specjalisty o bidirectional tracibility z braz gdzie uzywany jest EARS. Powiedz czy widziales gdzies opis jak zaczyna sie projekty regulowane. Nie robie nic zwiazanego z automotive anie nie potrzebuje certyfikacji. Chce wdrozyc praktyki ktore daj najwieksze ROI przy prowadzeniu projektu przez jedna osobe i agent LLM. Powiedz co wiecej o takich procesach

# MODEL

Tak, znam to z praktyki. Projekty regulowane zaczynają się zaskakująco podobnie, niezależnie od branży: DO-178C w lotnictwie (stamtąd wywodzi się EARS, z Rolls-Royce i silników lotniczych), ISO 26262 i ASPICE w motoryzacji, IEC 62304 w oprogramowaniu medycznym. Opisuję to z pamięci, na poziomie ogólnym. Szczegóły konkretnej normy trzeba sprawdzić w jej tekście, ale ty normy nie potrzebujesz, potrzebujesz jej logiki.

## Jak zaczyna się projekt regulowany

Zanim powstanie choćby jedno wymaganie, powstają **plany**. W DO-178C to zestaw: plan certyfikacji (PSAC), plan rozwoju, plan weryfikacji, plan zarządzania konfiguracją, plan zapewnienia jakości. Do tego standardy pisania wymagań, projektu i kodu. W ISO 26262 jest plan bezpieczeństwa, definicja „itemu” i analiza zagrożeń (HARA), z której wychodzą cele bezpieczeństwa. Wszystkie te dokumenty odpowiadają na te same pytania:

1. **Co jest w zakresie i jakie są granice systemu?**
2. **Jakie artefakty powstaną i kto je zatwierdza?**
3. **Jak artefakty są identyfikowane, wersjonowane i powiązane?** Tu jest ślad dwukierunkowy: każde wymaganie ma rodzica wyżej (skąd się wzięło) i dziecko niżej (co je realizuje i co je weryfikuje).
4. **Jak wygląda zmiana?** Baseline, wniosek o zmianę, analiza wpływu, ponowna weryfikacja.
5. **Jak mierzymy jakość?** Przeglądy, kryteria wejścia i wyjścia z każdego etapu, niezależność przeglądającego.

Dopiero potem przychodzą wymagania interesariuszy, systemowe i softwarowe (w EARS), projekt, kod i testy, a wszystko to łączy macierz śladów.

## Co z tego ma najlepszy zwrot przy jednej osobie i agencie

Zasada jest prosta: bierzesz **mechanizmy**, a pomijasz **ceremonię**. Ceremonia (formalne plany, komisje zmian, audyty procesu, kwalifikacja narzędzi) istnieje po to, żeby przekonać audytora. Mechanizmy istnieją po to, żeby system był spójny. Przy agencie LLM mechanizmy dają nawet więcej niż w zespole ludzkim, bo agent nie pamięta między sesjami i chętnie „dopowiada” brakujące rzeczy.

| Praktyka z projektów regulowanych | Wersja dla jednej osoby i agenta | Zwrot | Stan u nas |
|---|---|---|---|
| Unikalne, niezmienne identyfikatory | ID w tekście, łatwe do grepowania | bardzo wysoki | ✅ G-, D-, UC-, E- |
| Słownik pojęć | jeden plik, terminy zakazane | bardzo wysoki | ✅ |
| Rejestr decyzji (jak ADR) | rejestr z datą i uzasadnieniem | bardzo wysoki | ✅ |
| **Ślad dwukierunkowy** | każdy artefakt deklaruje tylko swojego **rodzica**, a kierunek w dół liczy skrypt; sprawdzanie sierot i braków pokrycia w pre-commit | **najwyższy z brakujących** | ❌ |
| Analiza wpływu zmiany („suspect links”) | gdy zmienia się tekst rodzica, jego dzieci dostają flagę „do przejrzenia”; wystarczy git i hash tekstu | wysoki | ❌ |
| Weryfikowalność wymagań | EARS plus test akceptacyjny (Gherkin) z tym samym ID | wysoki | częściowo (EARS w rozmowie, nie w repo) |
| Plan projektu | **jedna strona** w repo (np. `AGENTS.md` / `CLAUDE.md`): artefakty, schematy ID, przepływ pracy, reguły zmian; agent czyta ją na start każdej sesji | bardzo wysoki przy agencie | częściowo (kontrakt decyzji, README) |
| Niezależny przegląd | osobny agent ze świeżym kontekstem recenzuje wymagania pod listę kontrolną (EARS, jedno „shall”, terminy ze słownika) | średni do wysokiego | ❌ |
| Bramki etapów | twarde reguły w pre-commit zamiast spotkań | wysoki | ✅ dla nawigacji |
| Baseline | tag gita na zamkniętym etapie (np. `baseline-briefs`) | wysoki, prawie darmowy | ❌ |
| Analiza ryzyka (HARA / FMEA) | lekka: 5–10 scenariuszy „co pójdzie źle”, każdy daje wymaganie *If–then* | średni | ❌ |
| Komisja zmian, audyty procesu, kwalifikacja narzędzi, MC/DC | pomijasz | ujemny | — |

## Najważniejsza obserwacja o śladzie dwukierunkowym

W firmach ślad zwykle się psuje, bo ludzie utrzymują macierz ręcznie, w obu kierunkach. Tańszy wzorzec: **dziecko zapisuje tylko rodzica** (np. wymaganie EARS ma pole `źródło: UC-02, D-33`, a test ma `weryfikuje: CLR-03`). Macierz w obie strony generuje skrypt, a pre-commit sprawdza trzy rzeczy:
- **sieroty**: wymaganie bez źródła,
- **luki pokrycia**: wymaganie bez testu, przypadek użycia bez wymagań,
- **martwe odnośniki**: ID, którego nie ma.

Ten sam schemat działa już u ciebie dla nawigacji. Teraz trzeba go rozszerzyć na wymagania.

---

**Decyzje**

**1. Wymagania EARS w repozytorium ze śladem sprawdzanym w pre-commit** — wymagania (CAP-, CLR-, PRJ-…) istnieją dziś tylko w rozmowie, więc ślad nie ma czego łączyć.
- **A)** plik wymagań w repo, gdzie każde wymaganie ma ID, wzorzec EARS i pole „źródło”; skrypt generuje macierz w obie strony, a pre-commit sprawdza sieroty, luki i martwe odnośniki
- **B)** odłożyć, aż powstaną pełne przypadki użycia

[P] = A — to najwyższy zwrot z brakujących praktyk, a infrastruktura (ID, pre-commit) już jest.

**2. Jednostronicowy plan projektu dla agenta** — dziś zasady pracy są rozproszone między kontraktem, README i tą rozmową, a nowa sesja agenta zaczyna od zera.
- **A)** plik `AGENTS.md` w repo: artefakty, schematy ID, przepływ (dokument → eksport → diff → commit), reguły zmian i odnośnik do kontraktu
- **B)** zostać przy README i kontrakcie

[P] = A — agent bez tego pliku przy każdej sesji odtwarza proces z pamięci rozmowy, której już nie ma.

**3. Baseline na zamkniętym etapie** — briefy i słownik są stabilne, a nic tego nie oznacza.
- **A)** tag gita `baseline-01-slownik-briefy` na obecnym commicie
- **B)** bez tagów

[P] = A — kosztuje jedną komendę, a późniejsze „co się zmieniło od…” staje się jednym `git diff`.

**W kolejce**
- Suspect links (flaga przeglądu po zmianie rodzica)
- Niezależny przegląd wymagań przez osobnego agenta
- Lekka analiza ryzyka (scenariusze „co pójdzie źle”)
- Identyfikatory ekranów (E-xx) w słowniku i powiązanie ze śladem wymagań
- Pozycja wspólna dla kilku Działań; ponowne odznaczenie Pozycji
- Poprawka znacznika „[P]” w pliku kontraktu
- Znaczenie „trwale zapisany” (UC-01); UC-03 „Doprecyzować Element”; cel „Zarządzać Kontekstami”; reguła „Element nie wraca do Inboxu”

Odpowiedz „ok”, numerem z literą (np. „2B”), numerem z własnym tekstem albo „reszta ok”.

# USER
super robota ale jako inzynier wymagan i senior SW developer przemysl na bazie twojej powyzszej odpowiedzi jakie sa powiazniania miedzy tymi praktykami i w jakiej koljenosci co masz pomysl wprowadzic? a potem powiedz jak powinien wygladac plan i jakie sa does don;t  przy robieniu tego typu planow i. jak bys napisal go dla naszej systuacji i w jakim zakresie

# MODEL
Najpierw porządek w rejestrze. W poprzedniej wiadomości nie zapisałem trzech nowych decyzji jako otwartych, a kontrakt tego wymaga. Dopisuję je teraz razem z dwiema nowymi, które wynikają z tej analizy.

## 1. Jak te praktyki od siebie zależą

Patrząc oczami inżyniera wymagań, te praktyki tworzą trzy warstwy. Każda ma sens dopiero wtedy, gdy stoi pod nią poprzednia:

```
FUNDAMENT      ID + słownik + rejestr decyzji          (jest)
   │           bez stabilnych ID nie ma czego łączyć
   ▼
REGUŁY GRY     plan projektu (AGENTS.md) + baseline
   │           plan ustala schematy ID i format plików, ZANIM powstaną
   │           wymagania; inaczej czeka cię przenumerowanie
   ▼
ARTEFAKTY      ryzyka ──► wymagania EARS ──► testy (Gherkin)
 + KONTROLE        │          │ źródło          │ weryfikuje
                   └──────────┴─────► sprawdzanie śladu w pre-commit
                                          │
                                          ├─► suspect links (potrzebują śladu + baseline)
                                          └─► niezależny przegląd (potrzebuje listy kontrolnej z planu)
```

Trzy zależności, które decydują o kolejności:
- **Plan przed wymaganiami w repo.** Plan definiuje format wymagania i pola śladu. Gdy powstaną one przed planem, później trzeba je przerabiać.
- **Każdy artefakt wchodzi razem ze swoją kontrolą.** Wymagania bez sprawdzania śladu gniją od pierwszego dnia, a ślad bez automatu po kilku tygodniach przestaje odpowiadać rzeczywistości. Dlatego plik wymagań i skrypt śladu to jeden krok, a nie dwa.
- **Suspect links i niezależny przegląd na końcu.** Pierwsze ma sens dopiero przy realnych zmianach w powiązanym materiale, drugie przy kilkudziesięciu wymaganiach. Wcześniej to koszt bez zwrotu.

**Kolejność wdrożenia:**

| Fala | Co | Dlaczego teraz | Koszt |
|---|---|---|---|
| 1 | Plan v0 + baseline | ustala reguły, zanim powstanie kolejny artefakt | ~1 h |
| 2 | Plik wymagań + migracja istniejących EARS + sprawdzanie śladu w górę i martwych odnośników | najwyższy zwrot; infrastruktura już jest | ~2–3 h |
| 3 | Lekka analiza ryzyka dla UC-01…04 | dostarcza wymagania *If–then*, zanim przypadki zaczną rosnąć | ~1 h na przypadek |
| 4 | Testy akceptacyjne z „weryfikuje:” + pokrycie w dół | zamyka ślad dwukierunkowy | rośnie z wymaganiami |
| 5 | Suspect links | gdy zaczną się zmiany w wymaganiach | ~1 h |
| 6 | Niezależny przegląd przez osobnego agenta | przy ~20+ wymaganiach | ~0,5 h na rundę |

## 2. Jak powinien wyglądać taki plan

Plan w projekcie regulowanym odpowiada na pięć pytań z mojej poprzedniej odpowiedzi: zakres, artefakty, identyfikacja i ślad, zmiany, jakość. W wersji dla jednej osoby i agenta dochodzi szóste pytanie: **co agent robi sam, a o co pyta**.

**Do:**
- Opisuj to, co **faktycznie** robisz, a nie to, co chciałbyś robić. Plan, który rozjeżdża się z praktyką, uczy agenta ignorowania planu.
- Każdą regułę formułuj tak, żeby dało się ją sprawdzić, najlepiej skryptem. Jeśli nie da się jej sprawdzić, oznacz ją jako wytyczną.
- Nadaj regułom ID (P-01…), żeby agent i commity mogły się do nich odwoływać.
- Podaj **jedno źródło prawdy** dla każdego rodzaju artefaktu.
- Zapisz, czego świadomie **nie** robisz i dlaczego (tailoring). To chroni przed dokładaniem ceremonii.
- Podaj konkretne polecenia do uruchomienia.
- Wersjonuj plan w repo i przeglądaj go przy każdym baseline.

**Don't:**
- Nie kopiuj szablonów norm (PSAC, SDP…). To dokumenty dla audytora.
- Nie powielaj treści innych plików. Linkuj; duplikat zawsze się rozjedzie.
- Nie planuj szczegółowo przyszłych etapów (kod, wydania). Zaplanujesz je, kiedy będziesz coś o nich wiedział.
- Unikaj słów „odpowiednio”, „w miarę potrzeby”, „należy dbać”. Agent nie umie ich zweryfikować, a ty też nie.
- Nie przekraczaj jednej–dwóch stron. Plan agent czyta na start każdej sesji, a każde zdanie kosztuje kontekst.
- Nie mieszaj planu z wymaganiami. Plan mówi, **jak** pracujemy, a nie **co** budujemy.

## 3. Szkic dla naszej sytuacji

Zakres proponuję ograniczyć do **etapu specyfikacji**: słownik, przypadki użycia, wymagania, ryzyka, testy akceptacyjne i nawigacja. Kod dopiszemy, kiedy do niego dojdziemy (decyzja 5). Szkic zakłada odpowiedzi „A” w decyzjach poniżej:

```markdown
# AGENTS.md — GTD-App, etap specyfikacji

Przeczytaj na start każdej sesji. Kontrakt decyzji: kontrakt-decyzji.md (obowiązuje zawsze).

## Zakres
Specyfikacja wymagań GTD-App v1.0 dla jednego użytkownika. Bez kodu. Bez certyfikacji.

## Artefakty i źródła prawdy (P-01: jedno źródło dla każdego rodzaju)
| Artefakt              | Plik                         | ID                  |
| Słownik pojęć         | slownik.md                   | G-<GRUPA>-nn, ZP-nn |
| Rejestr decyzji       | otwarte-decyzje.md           | D-nn, K-nn          |
| Przypadki użycia      | przypadki-uzycia.md          | UC-nn               |
| Wymagania (EARS)      | wymagania.md                 | <OBSZAR>-nn         |
| Ryzyka                | ryzyka.md                    | RYZ-nn              |
| Testy akceptacyjne    | testy/*.feature              | AT-<ID wymagania>-n |
| Nawigacja             | nawigacja/ekrany.mmd         | E-nn                |
P-02 ID są niezmienne i nigdy nie są używane ponownie.

## Ślad (P-03…P-05)
P-03 Dziecko podaje tylko rodzica: wymaganie → `źródło:` (UC, D, RYZ, G); test → `weryfikuje:`.
P-04 Macierz w obie strony generuje `slad.py`; nie edytuje się jej ręcznie.
P-05 Pre-commit odrzuca: martwe ID, wymaganie bez źródła, regułę R1–R5 nawigacji.
     Brak testu dla wymagania = ostrzeżenie (do fali 4), potem błąd.

## Wymaganie jest gotowe, gdy (P-06)
jeden wzorzec EARS · jedno „shall” · podmiot GTD-App · terminy wyłącznie ze słownika ·
mierzalne · ma źródło · status: draft | zatwierdzone.

## Zmiana (P-07…P-09)
P-07 Każda zmiana: edycja pliku → `git diff` → kontrola → jeden commit na wiadomość,
     w opisie ID zmienionych elementów i decyzji.
P-08 Zmiana zatwierdzonego wymagania wymaga decyzji D-nn w rejestrze.
P-09 Zamknięty etap = tag `baseline-nn-<nazwa>`.

## Agent
P-10 Bez decyzji Użytkownika agent nie: zmienia znaczenia pojęć, zatwierdza wymagań,
     usuwa plików. Może: poprawiać format, dodawać ślad, uruchamiać kontrole.

## Świadomie pomijamy
komisję zmian, formalne plany V&V, audyty procesu, kwalifikację narzędzi, metryki pokrycia kodu.

## Polecenia
python3 slad.py                      # macierz i kontrole śladu
python3 nawigacja/sprawdz.py nawigacja/ekrany.mmd
git config core.hooksPath .githooks  # w nowym klonie
```

Wychodzi około jednej strony. Każda reguła P-03…P-08 jest albo sprawdzana skryptem, albo wynika z kontraktu. P-06 sprawdzam częściowo automatycznie (wzorzec, „shall”, terminy zakazane), a resztę w przeglądzie.

---

**Wykonane**
- Rejestr: dopisane otwarte decyzje D-38…D-40 z poprzedniej wiadomości (w poprzedniej wiadomości ich nie zapisałem, wbrew kontraktowi) i nowe D-41, D-42; kolejka K-10…K-13.
- Git w gtd2: commit `72f5606`, rozmiar pliku zgodny z dokumentem (6192 bajty).

**Bez odpowiedzi**

**1. Wymagania EARS w repo ze śladem w pre-commit** — to fala 2; wymagania istnieją dziś tylko w rozmowie (D-38).
- **A)** plik `wymagania.md` z ID, wzorcem EARS i polem „źródło”; `slad.py` generuje macierz w obie strony i działa w pre-commit
- **B)** odłożyć

[P] = A — najwyższy zwrot z brakujących praktyk.

**2. Jednostronicowy plan projektu** — to fala 1; zasady są dziś rozproszone (D-39).
- **A)** `AGENTS.md` według szkicu powyżej
- **B)** zostać przy README i kontrakcie

[P] = A — reguły muszą istnieć, zanim powstaną wymagania w repo.

**3. Baseline obecnego stanu** — słownik i briefy są stabilne (D-40).
- **A)** tag `baseline-01-slownik-briefy`
- **B)** bez tagów

[P] = A — jedna komenda, a punkt odniesienia dla wszystkich późniejszych zmian.

**Decyzje**

**4. Jedno źródło prawdy** — słownik i rejestr żyją dziś w dwóch miejscach (dokument i repo), a każdą zmianę wprowadzam dwa razy i porównuję rozmiary plików (D-41).
- **A)** repozytorium jest źródłem dla wszystkiego; dokument staje się widokiem odświeżanym z repo albo go zamykamy
- **B)** słownik i rejestr zostają w dokumencie, reszta w repo

[P] = A — dwa źródła to podwójna praca i stałe ryzyko rozjazdu; wymagania i tak będą w repo.

**5. Zakres planu** — trzeba ustalić, czy plan obejmuje tylko specyfikację, czy już kod (D-42).
- **A)** tylko etap specyfikacji; kod dopiszemy, gdy do niego dojdziemy
- **B)** od razu także kod i testy jednostkowe

[P] = A — plan na etap, o którym jeszcze mało wiemy, i tak trzeba będzie przepisać.

**W kolejce**
- Suspect links; niezależny przegląd przez osobnego agenta; lekka analiza ryzyka
- Identyfikatory ekranów (E-xx) w słowniku i ślad wymagań
- Pozycja wspólna dla kilku Działań; ponowne odznaczenie Pozycji
- Poprawka znacznika „[P]” w pliku kontraktu
- Znaczenie „trwale zapisany” (UC-01); UC-03 „Doprecyzować Element”; cel „Zarządzać Kontekstami”; reguła „Element nie wraca do Inboxu”

Odpowiedz „ok”, numerem z literą (np. „4B”), numerem z własnym tekstem albo „reszta ok”.

# USER
1a 2a 3a 4a 5a

# MODEL
Wykonuję po kolei: baseline, plan, wymagania ze śladem, jedno źródło prawdy. Najpierw baseline na obecnym stanie, zanim cokolwiek zmienię.

Baseline jest. Teraz przenoszę przypadki użycia do osobnego pliku, zgodnie z tabelą artefaktów z planu, i poprawiam znacznik „[P]” w kontrakcie.

Teraz skrypt śladu `slad.py`: zbiera identyfikatory ze wszystkich plików, sprawdza wymagania i generuje macierz w obie strony.

Wszystkie cztery celowe błędy zostały wykryte (piąty zniknął pod zdublowanym ID, które też jest zgłoszone). Teraz pre-commit, `AGENTS.md`, README i rejestr.

Edycja rejestru nie przeszła, bo tekst K-06 w pliku różni się od oczekiwanego. Sprawdzam, jak wygląda naprawdę.

Na koniec D-41 w samych dokumentach: dodaję na górze wyraźną notkę, że to archiwum, a źródłem prawdy jest repozytorium. Niczego nie usuwam.

Wszystkie pięć decyzji jest wykonanych. Specyfikacja ma teraz plan, wymagania w repo i ślad dwukierunkowy pilnowany przy każdym commicie.

**Co powstało w gtd2:**
- **`AGENTS.md`**: plan na jedną stronę, reguły P-01…P-10 według szkicu, z kolumną stanu (co już jest, a co przyjdzie w kolejnych falach).
- **`wymagania.md`**: 25 wymagań EARS. Część przeniosłem z naszej rozmowy, część wynika wprost z rozstrzygniętych decyzji (np. CLR-04 z D-33, PRJ-04 z D-35, REV-02 z D-34). Każde ma źródło i wszystkie mają status `draft`; zatwierdzenie wymaga twojej decyzji (P-08). WAI-02 przepisałem zgodnie z D-30: zamiast powiadomienia jest wyróżnienie z przyciskami „Skontaktuj się” i „Przesuń kontrolę”.
- **`slad.py` + `slad.md`**: macierz w obie strony (wymaganie → źródła, źródło → wymagania) i kontrole B1–B5: brak pola, nieznane ID, duplikat, nieznany wzorzec, tekst niezgodny z EARS lub nie jedno „shall”. Na celowo zepsutej kopii wykrył wszystkie podłożone błędy.
- **`przypadki-uzycia.md`**: briefy wydzielone ze słownika. Ręczne linie „Ślad:” usunąłem, bo teraz zastępuje je generowana macierz.
- **Pre-commit** sprawdza najpierw ślad, potem nawigację. Działa też przy twoich commitach w PyCharmie, bo `core.hooksPath` jest ustawione w tym repozytorium; potrzebny jest tylko `python3` na Macu.
- **Baseline**: tag `baseline-01-slownik-briefy`, postawiony przed zmianami.

Skrypt śladu od razu znalazł prawdziwą lukę: UC-02 odwołuje się do UC-03 „Doprecyzować Element”, którego nie było. Dodałem zaślepkę ze statusem „do napisania (K-02)”, więc teraz to ostrzeżenie, a nie fałszywy odnośnik. Drugie ostrzeżenie to brak testów; tak ma być do fali 4.

Dokumenty w Claude Docs (słownik z rejestrem i kontrakt) mają teraz na górze notkę „Archiwum, stan z 2026-10-12” z odesłaniem do repo. Niczego w nich nie usunąłem.

**Wykonane**
- Tag `baseline-01-slownik-briefy` na commicie `72f5606`.
- `AGENTS.md`, `wymagania.md` (25 wymagań w stanie `draft`), `slad.py`, `slad.md`, `przypadki-uzycia.md` z zaślepką UC-03.
- Pre-commit rozszerzony o kontrolę śladu; sprawdzony na nieaktualnym `slad.md`, commit zablokowany.
- `kontrakt-decyzji.md`: poprawiony znacznik „[P]” (K-06) i odesłanie do rejestru w repo; README przepisane pod nowy układ.
- Rejestr: D-38…D-42 rozstrzygnięte, K-06 zamknięte; od teraz rejestr prowadzę tylko w repo.
- Notki „Archiwum” w trzech kartach dokumentów.
- Git w gtd2: commit `f0886ce` (przeszedł przez nowy hook), repozytorium czyste.

**W kolejce**
- Fala 3: lekka analiza ryzyka dla UC-01…UC-04 (K-12)
- UC-03 „Doprecyzować Element” (K-02), dziś zaślepka
- Przegląd i zatwierdzenie 25 wymagań `draft`
- Suspect links (K-10); niezależny przegląd przez osobnego agenta (K-11)
- Identyfikatory ekranów E-xx w słowniku (K-13)
- Pozycja wspólna dla kilku Działań; ponowne odznaczenie Pozycji
- Znaczenie „trwale zapisany” (K-01); cel „Zarządzać Kontekstami”; reguła „Element nie wraca do Inboxu”

Nie ma otwartych decyzji. Według planu następna jest fala 3 (ryzyka). Napisz „dalej” albo wskaż inny temat z kolejki.

# USER
pomin ryzyka i wez kolejny temat

# MODEL
Pomijam ryzyka: oznaczam je w rejestrze jako odłożone na twoje życzenie i biorę następny temat, UC-03 „Doprecyzować Element”. Najpierw sprawdzam obecny stan UC-02, bo UC-03 jest jego częścią.

Ryzyka są oznaczone jako odłożone, a UC-03 „Doprecyzować Element” jest napisany i spięty ze śladem. Ostrzeżenie „UC-03 bez wymagań” zniknęło.

**UC-03 Doprecyzować Element** (podfunkcja; zawierany przez UC-02 i Przegląd tygodniowy)
Użytkownik rozpatruje jeden Element z Inboxu i wybiera dokładnie jeden z ośmiu wyników. Tabela wyników jest teraz tutaj, a nie w UC-02. Pierwszą, wyróżnioną opcją jest „Zrób teraz”. System prosi tylko o minimum danych: datę dla Zaplanowanego, Delegata dla Czekam na, Rezultat i jedno Otwarte działanie dla Projektu. Kontekst, czas, energia i Lista przygotowania są opcjonalne. Anulowanie zostawia Element w Inboxie bez zmian.

Pisanie tego briefu wyłoniło trzy rzeczy, których specyfikacja dotąd nie rozstrzygała (decyzje 2–4 poniżej). Najważniejsza jest decyzja 2: dziś Doprecyzowanie umie założyć nowy Projekt, ale nie umie dodać działania do istniejącego, a to w GTD najczęstszy przypadek.

**Wykonane**
- `przypadki-uzycia.md`: brief UC-03; tabela wyników przeniesiona z UC-02 (UC-02 odsyła do UC-03).
- `wymagania.md`: CLR-01…03 mają teraz źródło UC-03 (dotyczą pojedynczego Doprecyzowania, a nie opróżniania Inboxu).
- Rejestr: K-02 zamknięte, K-12 (ryzyka) odłożone na twoje życzenie; otwarte D-43…D-46.
- Git w gtd2: commit `418e426` przeszedł przez pre-commit; ślad: 25 wymagań, 0 błędów.

**Decyzje**

**1. Przeniesienie tabeli wyników do UC-03** — zrobiłem to sam, bo tabela opisuje pojedyncze Doprecyzowanie; razem z nią przepiąłem źródło CLR-01…03 na UC-03 (D-43).
- **A)** zostawić
- **B)** cofnąć

[P] = A — każdy przypadek opisuje teraz swój własny zakres, a ślad wskazuje właściwe miejsce.

**2. Działanie do istniejącego Projektu** — Doprecyzowanie umie dziś tylko założyć nowy Projekt, a nie dopiąć działanie do już istniejącego (D-44).
- **A)** przy wynikach Następne działanie / Zaplanowane / Czekam na opcjonalny wybór Projektu
- **B)** przypisanie do Projektu dopiero później, w szczegółach Działania

[P] = A — „kolejny krok do Remontu łazienki” to najczęstszy wynik Doprecyzowania; bez tego trzeba wracać do każdego działania osobno.

**3. Element z kilkoma sprawami** — notatka „opony, prezent dla mamy, zadzwonić do ZUS” to trzy różne rzeczy w jednym Elemencie (D-45).
- **A)** opcja „Podziel”, która tworzy kilka Elementów w Inboxie
- **B)** poza zakresem wersji 1.0

[P] = A — przy dyktowaniu i przekazywaniu maili takie Elementy są codziennością, a bez podziału nie da się ich uczciwie doprecyzować.

**4. Pola obowiązkowe** — przyjąłem minimum, żeby Doprecyzowanie było szybkie (D-46).
- **A)** tylko minimum: data, Delegat, Rezultat i jedno działanie
- **B)** dodatkowo obowiązkowy Kontekst dla Następnego działania

[P] = A — Kontekst można dodać później, a obowiązkowe pole spowalnia opróżnianie Inboxu.

**W kolejce**
- Przegląd i zatwierdzenie 25 wymagań `draft`
- Suspect links (K-10); niezależny przegląd przez osobnego agenta (K-11)
- Identyfikatory ekranów E-xx w słowniku (K-13)
- Pozycja wspólna dla kilku Działań; ponowne odznaczenie Pozycji
- Znaczenie „trwale zapisany” (K-01); cel „Zarządzać Kontekstami”; reguła „Element nie wraca do Inboxu”
- Analiza ryzyka (K-12, odłożona)

Odpowiedz „ok”, numerem z literą (np. „3B”), numerem z własnym tekstem albo „reszta ok”.

# USER
1a 2a 3a 4a

# MODEL
Wykonuję wszystkie cztery decyzje: Podział jako nowa operacja w słowniku, uzupełnienie UC-03 i trzy nowe wymagania.

Wszystkie cztery decyzje są w repozytorium, a commit `e97f22f` przeszedł przez pre-commit.

Podział zmienia jedną dotychczasową zasadę: „Element nigdy nie wraca do Inboxu” nadal obowiązuje dla Elementu pierwotnego, ale z Podziału mogą powstać **nowe** Elementy w Inboxie. Gwarancję sukcesu w UC-03 sformułowałem tak, żeby to uwzględniała.

Zauważyłem też, że ta rozmowa jest teraz podpięta do projektu „GTD” w claude.ai, który nie ma jeszcze żadnych dokumentów. Kontrakt wymaga, żeby nowa sesja zaczynała od przeczytania kontraktu i rejestru, a projekt to miejsce, które każda nowa rozmowa widzi od razu. Stąd decyzja poniżej.

**Wykonane**
- Słownik: nowa operacja G-OPR-15 Podział (Split).
- UC-03: wybór istniejącego Projektu (D-44), wynik „Podział” w tabeli (D-45), pola opcjonalne (D-46), gwarancja sukcesu z Podziałem.
- Wymagania: CLR-07, CLR-08, CLR-09; razem 28 wymagań, 0 błędów śladu.
- Rejestr: D-43…D-46 rozstrzygnięte.
- Git w gtd2: commit `e97f22f`.

**Decyzje**

**1. Wskaźnik w projekcie „GTD” w claude.ai** — nowa rozmowa w tym projekcie nie wie, że specyfikacja jest w PycharmProjects/gtd2 ani że obowiązuje kontrakt (D-47).
- **A)** jeden krótki dokument w projekcie: gdzie jest repozytorium, że źródłem prawdy jest repo (D-41) i że na start trzeba przeczytać `AGENTS.md`, kontrakt i rejestr; bez kopiowania treści
- **B)** nic nie dodawać

[P] = A — spełnia regułę „Ciągłość” z kontraktu, a bez kopii treści nie tworzy drugiego źródła prawdy.

**W kolejce**
- Przegląd i zatwierdzenie 28 wymagań `draft`
- Suspect links (K-10); niezależny przegląd przez osobnego agenta (K-11)
- Identyfikatory ekranów E-xx w słowniku (K-13); Podział i wybór Projektu na mapie nawigacji
- Pozycja wspólna dla kilku Działań; ponowne odznaczenie Pozycji
- Znaczenie „trwale zapisany” (K-01); cel „Zarządzać Kontekstami”; reguła „Element nie wraca do Inboxu”
- Analiza ryzyka (K-12, odłożona)

Odpowiedz „ok”, „1A”/„1B” albo numerem z własnym tekstem.

# USER
1a

# MODEL
W projekcie „GTD” w claude.ai jest teraz dokument „start-tutaj”. Każda nowa rozmowa w tym projekcie dowie się z niego, gdzie jest repozytorium i w jakiej kolejności czytać pliki: kontrakt, `AGENTS.md`, rejestr. Nie kopiowałem do projektu żadnej treści specyfikacji, więc źródło prawdy zostaje jedno. Dokument mówi też wprost, że bez połączenia z twoim komputerem trzeba poprosić o pliki, a nie odtwarzać ich z pamięci.

**Wykonane**
- Projekt „GTD”: dokument `claude/start-tutaj.md` (lokalizacja repo, kolejność czytania, zasada dostępu, status archiwum Claude Docs).
- Rejestr: D-47 rozstrzygnięte.
- Git w gtd2: commit `80c0a17`.

**W kolejce**
- Przegląd i zatwierdzenie 28 wymagań `draft`
- Suspect links (K-10); niezależny przegląd przez osobnego agenta (K-11)
- Identyfikatory ekranów E-xx w słowniku (K-13); Podział i wybór Projektu na mapie nawigacji
- Pozycja wspólna dla kilku Działań; ponowne odznaczenie Pozycji
- Znaczenie „trwale zapisany” (K-01); cel „Zarządzać Kontekstami”; reguła „Element nie wraca do Inboxu”
- Analiza ryzyka (K-12, odłożona)

Nie ma otwartych decyzji. Napisz „dalej” albo wskaż temat z kolejki.

# USER
Chcialbym moc zrobic repozytirum szablonowe wzorcowe do pracy czlowiek plus agent. W naszej rozmowie uzywamy konkretnych praktyk a takze rozmawialismy o tym jak wziac najwiecej z norm bez ceremoni i szablonow dla audytorow. Czy jako inzynier i specjalista od wymagan jestes w stanie na bazie naszej rozmowy dostarczyc na poczatek liste plikow/artefaktow i ich podmiot/zakres ?

# MODEL
Tak. Poniżej lista dla repozytorium szablonowego, zbudowana z tego, co w gtd2 faktycznie zadziałało. Dorzuciłem też lekcje z miejsc, w których coś nam zgrzytało.

## Rdzeń: każdy projekt

| Plik | Podmiot i zakres | ID | Kto pisze / zatwierdza | Kontrola | Kiedy powstaje |
|---|---|---|---|---|---|
| `README.md` | Dla człowieka, jeden ekran: co to za projekt i jak zacząć (klon, `git config core.hooksPath`, `make sprawdz`) | — | człowiek | — | start |
| `AGENTS.md` | **Plan projektu dla agenta**: zakres etapu, tabela artefaktów i źródeł prawdy, reguły P-nn, przepływ zmiany, co agent robi sam, czego świadomie nie robimy, polecenia. Maks. 1–2 strony | P-nn | agent pisze, człowiek zatwierdza | — | start |
| `CLAUDE.md` | Jedna linia odsyłająca do `AGENTS.md`, żeby różne narzędzia agentowe trafiały w to samo miejsce | — | — | — | start |
| `kontrakt-decyzji.md` | **Umowa interakcji człowiek–agent**: format decyzji, skróty odpowiedzi („ok”, „2B”, „odłóż”), brak odpowiedzi to brak zgody, bezpieczeństwo, ton. Niezależna od dziedziny | — | człowiek | — | start |
| `decyzje.md` | **Rejestr**: otwarte, w kolejce, rozstrzygnięte; data i odniesienia do zmienionych artefaktów. Pamięć projektu między sesjami | D-nn, K-nn | agent prowadzi po każdej odpowiedzi | ID unikalne | start |
| `zasady.md` | **Zasady projektowe** produktu (u nas ZP-01 „prowadzenie do postępu”), z jawnymi wyjątkami. Wydzielone ze słownika, bo zasada nie jest pojęciem | ZP-nn | człowiek decyduje | odwołania istnieją | gdy pojawi się pierwsza |
| `slownik.md` | **Słownik**: definicja (rodzaj + cecha), odpowiednik angielski, „nie mylić z”, terminy zakazane, krotności | G-<GRUPA>-nn | agent pisze, decyzje zmieniają znaczenia | ID unikalne | start |
| `zakres.md` | **Lista In/Out i lista aktor–cel z poziomami celów.** U nas powstały tylko w rozmowie i nie trafiły do repo; to luka, którą szablon zamyka | — / UC-nn jako cele | agent proponuje, człowiek zatwierdza | każdy cel morza ma UC | przed przypadkami |
| `scenki.md` | **Scenki użytkownika** (jak Kasia): narracja z życia, służy jako test akceptacyjny listy aktor–cel | SC-nn | człowiek / agent | każda scenka wskazuje cele | przed zakresem |
| `przypadki-uzycia.md` | **Przypadki użycia** wg Cockburna: brief, potem pełne (scenariusz, rozszerzenia, gwarancje) | UC-nn | agent pisze | odnośniki istnieją | po zakresie |
| `wymagania.md` | **Wymagania EARS**: wzorzec, tekst, źródło (tylko rodzic), status draft / zatwierdzone | <OBSZAR>-nn | agent pisze, zatwierdza człowiek | B1–B5 w pre-commit | po briefach |
| `slad.md` | **Macierz śladu w obie strony**, generowana | — | skrypt | aktualność w pre-commit | z wymaganiami |
| `testy/*.feature` | **Testy akceptacyjne Gherkin** z `# weryfikuje: <ID>` | AT-<ID>-n | agent pisze | pokrycie: najpierw ostrzeżenie, potem błąd | fala testów |

## Narzędzia i automatyzacja

| Plik | Zakres |
|---|---|
| `narzedzia/id.toml` | **Jedno miejsce na schematy ID** (wzorce, pliki, w których się je definiuje). U nas wzorce siedziały wpisane w skryptach, a powinny być wspólne dla skryptów i `AGENTS.md` |
| `narzedzia/slad.py` | Zbiera ID, sprawdza B1–B5, generuje `slad.md`; czyta `id.toml` |
| `.githooks/pre-commit` | Wersjonowany hook: wszystkie kontrole i aktualność plików generowanych |
| `Makefile` | `make sprawdz`, `make slad`, `make baseline N=…`, żeby człowiek i agent używali tych samych komend |
| `.gitignore` | ustawienia IDE, `__pycache__` |

## Moduły opcjonalne: kopiujesz, gdy dotyczą projektu

| Katalog / plik | Zakres |
|---|---|
| `moduly/nawigacja/` | `ekrany.mmd` + reguły R1–R6 (pułapki, wycieki, kliknięcia) + budowanie strony z mapą. Tylko dla projektów z interfejsem |
| `moduly/ryzyka/ryzyka.md` | Lekka analiza „co pójdzie źle”, gdzie każde ryzyko daje wymaganie *If–then* (RYZ-nn) |
| `moduly/model-stanow/` | Maszyna stanów w Mermaid ze sprawdzaniem, czy każdy stan i przejście ma wymaganie (pomysł z początku rozmowy, jeszcze niezrealizowany) |

## Czego w szablonie świadomie nie ma
Osobnych plików szablonów: każdy plik zaczyna się krótkim opisem formatu i jednym przykładem. Planów V&V, CM i QA jako osobnych dokumentów (to jest w `AGENTS.md` w kilku linijkach). Komisji zmian, macierzy RACI i metryk.

## Lekcje z gtd2 wbudowane w szablon
- **Jedno źródło prawdy od pierwszego dnia.** Synchronizacja dokumentu z repo kosztowała nas najwięcej pracy.
- **Rejestr aktualizowany po każdej odpowiedzi.** Raz pominąłem decyzje i musiałem je dopisywać wstecz.
- **Hook w `.githooks`, a nie w `.git/hooks`**, plus tożsamość gita w lokalnej konfiguracji (u nas brakowało jej na komputerze).
- **Pliki generowane sprawdzane pod kątem aktualności**, a nie tylko poprawności.
- **Świadome wyjątki deklarowane w pliku** (jak `wyjatek-zp01`) zamiast osłabiania reguły.

---

Zapisuję poniższe decyzje w rejestrze gtd2, dopóki nowe repozytorium nie istnieje.

Lista plików jest wyżej. Zanim zacznę budować szablon, potrzebuję czterech decyzji.

**Wykonane**
- Rejestr gtd2: otwarte decyzje D-48…D-51 dla repozytorium szablonowego, commit `b685549`. Przeniosę je do nowego repo, gdy powstanie.

**Decyzje**

**1. Jak powstaje szablon** — szablon można zbudować obok gtd2 albo przerabiając gtd2 (D-48).
- **A)** nowe repozytorium (np. `PycharmProjects/szablon-czlowiek-agent`) z plików gtd2 uogólnionych i oczyszczonych z treści GTD
- **B)** wydzielenie z gtd2: przebudować gtd2 tak, żeby stał się szablonem z pierwszą wypełnioną instancją

[P] = A — gtd2 zostaje nietknięty i działa dalej, a szablon można później zastosować do gtd2 jako pierwszy test.

**2. Język szablonu** — dotyczy plików, reguł i komunikatów skryptów (D-49).
- **A)** polski; wymagania EARS po angielsku; nazwy plików bez polskich znaków
- **B)** całość po angielsku

[P] = A — pracujesz po polsku, a kontrakt i reguły działają najlepiej w języku, w którym myślisz; EARS zostaje po angielsku jak w gtd2.

**3. Moduły dziedzinowe** — nawigacja, ryzyka i model stanów nie przydadzą się w każdym projekcie (D-50).
- **A)** katalog `moduly/`, z którego kopiujesz to, czego projekt potrzebuje
- **B)** wszystko w rdzeniu, a niepotrzebne usuwasz

[P] = A — rdzeń zostaje mały, a usuwanie jest bardziej podatne na błędy niż dodawanie.

**4. Schematy ID** — w gtd2 wzorce ID są wpisane na stałe w skryptach (D-51).
- **A)** jeden plik `narzedzia/id.toml`, z którego czytają skrypty i do którego odsyła `AGENTS.md`
- **B)** wzorce w skryptach jak w gtd2

[P] = A — nowy rodzaj artefaktu dodajesz wtedy jedną linijką, bez zmiany kodu.

**W kolejce**
- Przegląd i zatwierdzenie 28 wymagań `draft` (gtd2)
- Suspect links (K-10); niezależny przegląd przez osobnego agenta (K-11)
- Identyfikatory ekranów E-xx (K-13); Podział i wybór Projektu na mapie nawigacji
- Pozycja wspólna dla kilku Działań; ponowne odznaczenie Pozycji
- Znaczenie „trwale zapisany” (K-01); cel „Zarządzać Kontekstami”; reguła „Element nie wraca do Inboxu”
- Analiza ryzyka (K-12, odłożona)

Odpowiedz „ok”, numerem z literą (np. „2B”), numerem z własnym tekstem albo „reszta ok”.

# USER
zanim odpoiedzm to  narysuj diagram w mermaid zeby polaczyc wszystkie identyfikatory z plikow i udowodnic ze w zalozeniu model ma dane do zrobienia pelnej  sledzalnosci? Czy to ma sens czy byś cos dodał?

# MODEL
Tak, to ma sens. Taki diagram to w inżynierii wymagań **model informacyjny śladu** (w ASPICE nazywa się to *traceability strategy*). Rysuje się go przed wypełnianiem artefaktów, właśnie po to, żeby sprawdzić, czy każdy rodzaj elementu ma skąd przyjść i dokąd prowadzić. Rysuję go i od razu zaznaczam, czego w gtd2 brakuje.

Diagram jest na stronie „Model śledzalności człowiek + agent”. Krótka odpowiedź: **w założeniu tak, model ma dane do pełnej śledzalności, ale dopiero z pięcioma uzupełnieniami.** W obecnym gtd2 łańcuch ma dziury na obu końcach: na górze (skąd biorą się przypadki użycia) i na dole (testy, ekrany, przyczyna zmiany).

**Dlaczego to wystarcza.** Pełna śledzalność dwukierunkowa sprowadza się do pięciu warunków, które da się sprawdzić automatycznie:
1. Każdy rodzaj elementu jest **korzeniem** (scenka, zakres, decyzja) albo ma **obowiązkowe pole rodzica**.
2. Kierunek w dół nie jest nigdzie zapisany, tylko **liczony** przez odwrócenie pól rodziców. Dlatego oba kierunki z konstrukcji nie mogą się rozjechać; to właśnie częsta awaria ręcznych macierzy w firmach.
3. Każde ID w polu rodzica **istnieje** i jest **unikalne**.
4. Dla każdego rodzaju wiadomo, czy brak dzieci to błąd, ostrzeżenie, czy stan dopuszczalny (tabela na stronie).
5. Każda zmiana wskazuje swoją **przyczynę**.

gtd2 spełnia dziś warunki 2 i 3, a 1 i 4 tylko dla wymagań.

**Co bym dodał (zaznaczone na żółto):**
- **Scenki SC-nn z polem `scenki:` w przypadkach użycia.** Dziś UC nie mają rodzica, więc nie da się wykazać, że wynikają z realnego użycia. Scenka z Kasią była naszym najlepszym testem akceptacyjnym listy celów, a nie ma jej w repo.
- **Zakres In/Out jako IO-nn.** Decyzje „poza zakresem” znikają bez śladu, a wymaganie typu „system nie powiadamia Delegata” powinno móc wskazać pozycję Out jako źródło.
- **Ekrany z polem `realizuje: UC`.** Dziś mapa nawigacji wisi obok wymagań i nic jej z nimi nie łączy (to K-13).
- **Automatyczne sprawdzanie pojęć.** Słowa pisane wielką literą w tekście EARS muszą mieć odpowiednik w kolumnie angielskiej słownika. To zamienia regułę P-06 z „przeglądu” w kontrolę skryptem.
- **Hook `commit-msg`**, który wymaga co najmniej jednego ID w opisie commita. Dziś to tylko mój zwyczaj, a z hookiem warunek 5 jest spełniony z automatu.

Przy okazji: zasada ZP-01 nie wskazuje decyzji, która ją ustanowiła. Zapisałem ją z twojej wiadomości, ale bez ID decyzji.

Warstwa kodu (moduł → wymaganie, wynik → test) jest na diagramie na szaro, żeby było widać, że model ją przewiduje, choć teraz jej nie budujemy (D-42).

---

**Wykonane**
- Strona „Model śledzalności człowiek + agent”: diagram Mermaid, warunki pełnej śledzalności, reguły dla każdego rodzaju ze stanem w gtd2.
- Rejestr gtd2: otwarte D-52, commit `03428c6`.

**Bez odpowiedzi**

**1. Jak powstaje szablon** (D-48)
- **A)** nowe repozytorium z plików gtd2 uogólnionych i oczyszczonych z treści GTD
- **B)** przebudowa gtd2 w szablon z pierwszą wypełnioną instancją

[P] = A — gtd2 działa dalej i posłuży jako pierwszy test szablonu.

**2. Język szablonu** (D-49)
- **A)** polski; wymagania EARS po angielsku; nazwy plików bez polskich znaków
- **B)** całość po angielsku

[P] = A — reguły i kontrakt działają najlepiej w języku, w którym myślisz.

**3. Moduły dziedzinowe** (D-50)
- **A)** katalog `moduly/`, z którego kopiujesz to, czego projekt potrzebuje
- **B)** wszystko w rdzeniu, a niepotrzebne usuwasz

[P] = A — rdzeń zostaje mały, a dodawanie jest bezpieczniejsze niż usuwanie.

**4. Schematy ID** (D-51)
- **A)** jeden plik `narzedzia/id.toml` czytany przez skrypty
- **B)** wzorce w skryptach jak w gtd2

[P] = A — nowy rodzaj elementu dodajesz jedną linijką, a model z diagramu da się wprost zapisać w tym pliku.

**Decyzje**

**5. Model śladu dla szablonu** — chodzi o diagram powyżej (D-52).
- **A)** model z propozycjami: scenki, zakres In/Out, ZP wskazuje decyzję, ekrany realizują UC, automatyczne sprawdzanie pojęć, hook commit-msg
- **B)** tylko elementy, które już istnieją w gtd2

[P] = A — bez tych uzupełnień ślad urywa się na górze i na dole, a każde z nich to kilka linijek w `id.toml` i skrypcie.

**W kolejce**
- Przegląd i zatwierdzenie 28 wymagań `draft` (gtd2)
- Suspect links (K-10); niezależny przegląd przez osobnego agenta (K-11)
- Identyfikatory ekranów E-xx (K-13); Podział i wybór Projektu na mapie nawigacji
- Pozycja wspólna dla kilku Działań; ponowne odznaczenie Pozycji
- Znaczenie „trwale zapisany” (K-01); cel „Zarządzać Kontekstami”; reguła „Element nie wraca do Inboxu”
- Analiza ryzyka (K-12, odłożona)

Odpowiedz „ok”, numerem z literą (np. „2B”), numerem z własnym tekstem albo „reszta ok”.

# USER
Dodaj to co sugerujsze rzetelnie i sprawdz.

1A nowe repo na moim macu w folderze /Users/michal/PycharmProjects/ai-sldc-template
Sprawdz i zrob commit

PAmietaj zeby zapisac wszystkie pliki jeden po drugim

2a
3a
4a
5a

# MODEL
Buduję szablon w `/Users/michal/PycharmProjects/ai-sldc-template` i zapisuję pliki po kolei, każdy w osobnym kroku. Najpierw sprawdzam dostęp do folderu i wersję Pythona, bo skrypty muszą działać także na twoim Macu.

Folder już istnieje, sprawdzam, co w nim jest. Python w tym środowisku nie ma `tomllib` (to wersja 3.10, a na Macu może być nawet 3.9), więc skrypty dostaną własny, prosty parser `id.toml`.

Poprawiam odwołania w nagłówku: w rejestrze szablonu schematy ID to D-05, a model śladu D-06 (D-01 to przyjęcie szablonu, a D-02…D-06 to decyzje przeniesione z gtd2).

Teraz `narzedzia/model.py`: parser `id.toml` i czytnik elementów ze wszystkich trzech formatów. Korzystają z niego oba skrypty.

Parser działa: `G-ELM-01` nie jest mylone z wymaganiem `ELM-01`, a `RYZ-03` z wymaganiem. Teraz `narzedzia/slad.py`, czyli wszystkie reguły z modelu.

Teraz `narzedzia/sprawdz_commit.py` dla hooka commit-msg: commit musi wskazywać co najmniej jeden istniejący identyfikator.

Teraz oba hooki: `.githooks/pre-commit` i `.githooks/commit-msg`.

Teraz `Makefile`, żeby człowiek i agent używali tych samych komend.

Teraz kontrakt decyzji. Biorę wersję z gtd2 (ta jest źródłem prawdy) i zmieniam tylko ostatnią sekcję, żeby wskazywała rejestr szablonu.

Ostrzeżenia O2 są tu poprawne: commitów jeszcze nie ma, więc decyzje nie mają wzmianek. Znikną po pierwszym commicie. Teraz `zasady.md`.

Teraz `scenki.md`.

Teraz `zakres.md`: lista In/Out i lista aktor–cel.

Teraz `przypadki-uzycia.md`.

Teraz `wymagania.md`.

Skrypt od razu wyłapał przykładowe ID w opisie (`CAP-01`), które nie istnieje. Zamieniłem je na zapis bez numeru. Teraz `testy/README.md` z formatem testów akceptacyjnych.

Teraz `AGENTS.md`, czyli plan projektu dla agenta.

Teraz `CLAUDE.md`: jedna linia odsyłająca do `AGENTS.md`.

Teraz `README.md` dla człowieka.

Teraz moduł nawigacji. Najpierw `moduly/nawigacja/sprawdz.py`, skopiowany z gtd2 i rozszerzony o regułę R7: każdy ekran musi deklarować, który przypadek użycia realizuje.

Teraz przykładowa mapa `moduly/nawigacja/ekrany.mmd`: minimalna, ale spełniająca wszystkie reguły R1–R7.

Działa. W nazwach reguł zostało „ZP-01” z gtd2; w szablonie takiej zasady jeszcze nie ma, więc zmieniam etykiety na neutralne „Postęp”.

Teraz `zbuduj.py` i `szablon.html` modułu, skopiowane z gtd2, z tytułem i opisem bez odniesień do GTD.

Teraz `moduly/nawigacja/README.md` z instrukcją wdrożenia modułu.

Teraz moduł ryzyk: `moduly/ryzyka/ryzyka.md`.

Teraz `moduly/model-stanow/README.md`. Uczciwie opisuję go jako moduł w przygotowaniu, bez skryptu, który dopiero trzeba napisać.

Jedna porażka dotyczy samego testu: zgadywałem kolejność dzieci w wierszu macierzy. Sprawdzam, jak wygląda naprawdę.

Test przechodzi: łańcuch wzorcowy bez błędów, każdy z ośmiu błędów wykryty, a oba hooki działają. Dopisuję `make test` do Makefile, `AGENTS.md` i README.

Ostrzeżenia `make` o przesunięciu zegara wynikają z montowania folderu w tym środowisku i nie wpływają na wynik. Przegląd tego, co trafi do pierwszego commita:

Jedyne wzmianki o gtd2 to historia pochodzenia decyzji w rejestrze, czyli zgodnie z zamiarem. Robię pierwszy commit; przechodzi przez oba nowe hooki.

Commit `716abb6` przeszedł przez oba hooki, a ostrzeżenia O2 zniknęły, bo opis commita wskazuje wszystkie decyzje. Ostatnie sprawdzenie na prawdziwym repo: commit bez ID musi zostać odrzucony.

Wszystko się zgadza. Na koniec zamykam te decyzje w rejestrze gtd2, z adnotacją, że przeniesiono je do szablonu.

Szablon jest gotowy w `PycharmProjects/ai-sldc-template` i ma pierwszy commit `716abb6`. Ten commit przeszedł już przez oba nowe hooki.

Wszystkie uzupełnienia z diagramu weszły do modelu: scenki, zakres In/Out, zasady wskazujące decyzję, ekrany realizujące przypadki użycia, sprawdzanie pojęć w wymaganiach i hook commit-msg. Model ma 11 rodzajów elementów i jest zapisany w jednym pliku, `narzedzia/id.toml`. Skrypt `slad.py` czyta go i zgłasza osiem rodzajów błędów:
- brak pola albo rodzica,
- nieznane ID,
- zdublowane ID,
- niedozwolony status lub wzorzec,
- tekst niezgodny z EARS,
- pojęcie spoza słownika,
- rodzic złego typu,
- brak wymaganego pokrycia.

**Jak to sprawdziłem.** Test `narzedzia/test_narzedzi.py` jest w repozytorium i uruchamia się przez `make test`. Buduje w katalogu tymczasowym pełny łańcuch, w którym występuje każdy z 11 typów: scenka → przypadek → ryzyko → wymaganie → test, ekrany realizujące przypadek, decyzja ustanawiająca zasadę, zasada jako źródło wymagania-ograniczenia z pozycji Out. Potem sprawdza, że łańcuch jest bez błędów, a każda strzałka z diagramu ma swój wiersz w macierzy. Następnie psuje go na każdy z ośmiu sposobów i sprawdza, że pada właściwy kod. Na koniec testuje hooki: commit bez ID odrzucony, z istniejącym ID przyjęty, z nieistniejącym (`D-99`) odrzucony, nieaktualny `slad.md` zablokowany. Wszystko przechodzi.

Trzy rzeczy, które wyszły po drodze:
- **Skrypt od razu złapał mój błąd**: w opisie formatu wymagań wpisałem przykładowe `CAP-01`, a ono nie istnieje. Poprawiłem to; tak właśnie ma to działać.
- **Python na twoim Macu może nie mieć `tomllib`** (to biblioteka z 3.11+, a w moim środowisku jest 3.10). Dlatego `model.py` ma własny, prosty parser `id.toml` i użyje `tomllib` tylko wtedy, gdy jest dostępny. Skrypty działają od Pythona 3.8 i nie mają zależności.
- **Moduł model stanów jest tylko opisany**, bez skryptu sprawdzającego. Zaznaczyłem to w jego README, żeby szablon nie obiecywał więcej, niż robi.

Pliki zapisywałem po kolei, każdy w osobnym kroku. Wyjątkiem były `zasady.md` i `slownik.md`, które przez nieuwagę poszły jednym poleceniem.

**Wykonane**
- `ai-sldc-template`: 30 plików. Rdzeń (11), narzędzia (5 z testem), hooki (2), moduły: nawigacja z nową regułą R7 „każdy ekran realizuje przypadek użycia”, ryzyka, model stanów (opis).
- Rejestr szablonu: D-01 przyjęcie szablonu, D-02…D-06 przeniesione z gtd2.
- Lokalna tożsamość gita i `core.hooksPath` ustawione w nowym repo.
- gtd2: D-48…D-52 zamknięte z adnotacją o przeniesieniu, commit `7410f4f`.

**W kolejce**
- Baseline szablonu (`make baseline N=01-szablon`)
- Zastosowanie szablonu do gtd2 (scenki, zakres In/Out i id.toml w gtd2)
- Skrypt dla modułu model stanów
- gtd2: przegląd i zatwierdzenie 28 wymagań; suspect links; niezależny przegląd przez osobnego agenta
- gtd2: Podział i wybór Projektu na mapie nawigacji; pozycja wspólna dla kilku Działań; „trwale zapisany” (K-01)

Nie ma otwartych decyzji. Napisz „dalej” albo wskaż temat z kolejki.

# USER
czy myśmy w tej sesji rozmawiali o normach?

# MODEL
Tak, kilka razy, choć zawsze z perspektywy praktyki, a nie samych norm.

- **Przy porównaniu EARS z przypadkami użycia Cockburna.** Wspomniałem, że EARS powstał w Rolls-Royce przy silnikach lotniczych i jest popularny w motoryzacji i lotnictwie, bo atomowe wymagania z ID ułatwiają śledzenie i audyt. Wymieniłem tam ISO 26262 i DO-178C.
- **Najobszerniej przy pytaniu, jak zaczynają się projekty regulowane.** Opisałem wtedy, że w DO-178C przed wymaganiami powstają plany (plan certyfikacji PSAC, plany rozwoju, weryfikacji, zarządzania konfiguracją i jakości) oraz standardy pisania wymagań i kodu. W ISO 26262 jest plan bezpieczeństwa, definicja „itemu” i analiza zagrożeń HARA, w ASPICE ślad dwukierunkowy jako praktyka bazowa, a w IEC 62304 plan rozwoju oprogramowania medycznego. Wszystkie odpowiadają na te same pytania: zakres, artefakty, identyfikacja i ślad, zmiany, jakość.
- **Wniosek, który z tego wyciągnęliśmy**: brać z norm **mechanizmy** (ID, ślad dwukierunkowy, baseline, kontrola zmian, bramki, niezależny przegląd), a pomijać **ceremonię** dla audytora (formalne plany, komisje zmian, audyty procesu, kwalifikację narzędzi). Tak powstała tabela praktyk z oceną zwrotu, a potem `AGENTS.md` z sekcją „Świadomie pomijamy”.
- **Przy modelu śladu** odwołałem się do ASPICE: model informacyjny śladu to tam *traceability strategy*.

Jedno zastrzeżenie, które wtedy też zaznaczyłem: o normach mówiłem z pamięci i na poziomie ogólnym, bez sprawdzania ich tekstów. Gdybyś kiedyś potrzebował konkretnego wymagania z którejś normy (np. dokładnego brzmienia praktyki bazowej ASPICE o śledzeniu), trzeba to zweryfikować w źródle.

# USER
mówiliśmy też o planach. jak wyglądają i co powinny zawierać te plany dla malego projektu? czy masz źródła z których możemy dostac kompleksową odpowiedź?

# MODEL
Sprawdzę źródła, zanim odpowiem, bo dostępność norm i materiałów zmienia się z czasem.

Tak, mówiliśmy o planach: najpierw o tym, że projekt regulowany zaczyna się od planów, a potem napisaliśmy `AGENTS.md` jako plan na jedną stronę. Sprawdziłem źródła. Są dwa bezpłatne, które pasują do małego projektu, i kilka płatnych norm do odniesienia.

## Źródła

**Najlepiej dopasowane, bezpłatne:**
- **ISO/IEC 29110, profil Basic**: seria dla „bardzo małych podmiotów” (VSE), czyli organizacji lub projektów do 25 osób. ISO udostępnia raporty techniczne tej serii bezpłatnie, w tym przewodnik zarządzania i inżynierii dla profilu Basic (TR 29110-5-1-2). Opisuje dwa procesy (zarządzanie projektem oraz implementacja) i definiuje produkt „Plan projektu”. To najbliższy odpowiednik naszej sytuacji. Uwaga: w 2025 roku wyszło nowe wydanie tej części jako pełna norma i nie ustaliłem, czy ono też jest bezpłatne. Bezpłatność potwierdzają dla raportów technicznych materiały ISO i strona prof. Laporte (współautora serii). Samej strony ISO z darmowymi normami nie mogłem otworzyć, bo blokuje automatyczne pobieranie.
- **NASA Software Engineering Handbook, rozdział 5.08 „SDP-SMP”**: lista 25 zalecanych elementów planu rozwoju/zarządzania oprogramowaniem. Pisana dla dużych projektów, ale bardzo dobra jako lista kontrolna „czego nie zapomnieć”, z jawnym mechanizmem tailoringu.

**Płatne, do odniesienia:** ISO/IEC/IEEE 16326 (treść planu zarządzania projektem), IEEE 828 (zarządzanie konfiguracją), IEEE 730 (zapewnienie jakości), IEEE 1012 (weryfikacja i walidacja), ISO/IEC/IEEE 12207 (procesy cyklu życia).

## Co powinien zawierać plan małego projektu

Poniżej elementy planu projektu z profilu Basic ISO/IEC 29110. **Wypisuję je z pamięci**, więc przed użyciem trzeba je sprawdzić w dokumencie. Obok stan naszego `AGENTS.md`:

| Element planu (29110 Basic, z pamięci) | U nas | Uwagi |
|---|---|---|
| Opis produktu: cel, wymagania ogólne | częściowo | sekcja „Zakres”, ale bez celu projektu |
| Zakres: co wchodzi, co nie | ✅ | `zakres.md` (IO-nn) |
| Cele projektu | ❌ | czym mierzymy sukces etapu |
| Produkty do dostarczenia | częściowo | tabela artefaktów, bez „co i komu przekazujemy” |
| Zadania, w tym weryfikacja, walidacja, przeglądy | częściowo | reguły P-05…P-08, bez walidacji z użytkownikiem |
| Szacowany czas, zasoby, harmonogram | ❌ | dla jednej osoby wystarczą kamienie milowe = tagi baseline |
| Skład zespołu | ✅ | człowiek + agent i podział ról (P-10) |
| Szacowany nakład i koszt | ❌ | zwykle zbędne przy projekcie prywatnym |
| **Ryzyka projektu** | ❌ | ważne: to coś innego niż ryzyka produktu (RYZ-nn); np. „agent traci kontekst”, „brak czasu” |
| Strategia kontroli wersji | ✅ | git, hooki, baseline |
| Instrukcje dostarczenia | ❌ | co oznacza „etap zamknięty” i kto go odbiera |

Lista NASA dokłada do tego kilka rzeczy wartych uwagi nawet w małym projekcie: środowisko i narzędzia (dla nas: Python, git, agent i jego dostęp do plików), udział użytkownika w walidacji, zasady przeglądów, a także podejście do gotowych komponentów i open source.

**Wniosek:** nasz `AGENTS.md` dobrze pokrywa część techniczną (artefakty, ślad, zmiany, konfiguracja), ale brakuje mu części **zarządczej**: celu projektu, kamieni milowych, ryzyk projektu, walidacji z użytkownikiem i definicji dostarczenia. W małym projekcie to 5 krótkich sekcji, które zmieszczą się na dodatkowej pół stronie.

**Jak dostać kompletną odpowiedź:** pobierz TR 29110-5-1-2 (profil Basic) ze strony ISO z bezpłatnymi normami i załącz go tutaj albo połóż w repo. Wtedy przeczytam go i zrobię dokładne mapowanie z cytatami zamiast listy z pamięci. Rozdział NASA mogę przeczytać sam.

---

Zapisuję poniższe decyzje w rejestrze szablonu; to pierwsza zmiana prowadzona już według jego własnych reguł.

Commit przeszedł, ale zgoda na usuwanie z poprzedniej sesji wygasła i git zostawił blokady. Przenoszę je pod inne nazwy, żeby twój git w PyCharmie działał. Niczego nie usuwam.

Repozytorium szablonu jest czyste, a blokady nie przeszkadzają (leżą w `.git` jako `stale-…`; usunę je, gdy następnym razem dasz zgodę na sprzątanie).

**Wykonane**
- Sprawdzone źródła: ISO/IEC 29110 (profil Basic, bezpłatny raport techniczny) i NASA Software Engineering Handbook 5.08 (25 elementów planu).
- Porównanie elementów planu z 29110 z naszym `AGENTS.md`: brakuje celu projektu, kamieni milowych, ryzyk projektu, walidacji z użytkownikiem i definicji dostarczenia.
- `ai-sldc-template`: otwarte D-07 i D-08 w rejestrze, commit `2c2be4a` przez hooki szablonu; blokady gita przeniesione bez usuwania.

**Decyzje**

**1. Źródło bazowe dla części zarządczej planu** — 29110 pasuje skalą, a NASA jest dokładniejsza (D-07).
- **A)** ISO/IEC 29110, profil Basic
- **B)** NASA Software Engineering Handbook 5.08
- **C)** oba: 29110 jako struktura planu, NASA jako lista kontrolna przy przeglądzie

[P] = C — 29110 jest napisany dla podmiotów naszej skali, a 25 punktów NASA wyłapie to, co mały standard pomija (środowisko, narzędzia, open source).

**2. Uzupełnienie `AGENTS.md` szablonu** — chodzi o pięć brakujących sekcji z tabeli wyżej (D-08).
- **A)** dodać cel projektu, kamienie milowe (tagi baseline), ryzyka projektu, walidację z użytkownikiem i definicję dostarczenia, po weryfikacji w źródle
- **B)** zostawić plan wyłącznie techniczny

[P] = A — to pół strony, a bez tego plan mówi, jak pracujemy, ale nie mówi, po co i kiedy etap jest skończony.

**W kolejce**
- Baseline szablonu; zastosowanie szablonu do gtd2; skrypt dla modułu model stanów
- gtd2: przegląd i zatwierdzenie 28 wymagań; suspect links; niezależny przegląd przez osobnego agenta
- gtd2: Podział i wybór Projektu na mapie nawigacji; pozycja wspólna dla kilku Działań; „trwale zapisany” (K-01)

Odpowiedz „ok”, numerem z literą (np. „1A”), numerem z własnym tekstem albo „reszta ok”. Jeśli wybierzesz 2A, załącz TR 29110-5-1-2, a zrobię mapowanie na podstawie tekstu, a nie pamięci.

Sources:
- [ISO — Software engineering: lifecycle profiles for very small entities (materiały edukacyjne, dostępność bezpłatna)](https://www.iso.org/sites/materials/teaching-materials/education_materials-higher-edu/educational_materials-detail-emf0bd-2.html?emid=741)
- [Prof. C. Y. Laporte — The Generic Profile for VSEs (o bezpłatnych przewodnikach 29110)](https://profs.etsmtl.ca/claporte/english/VSE/VSE-System-Profile.html)
- [ISO/IEC 29110-5-1-2:2025 — nowe wydanie (podgląd)](https://webstore.ansi.org/preview-pages/ISO/preview_ISO+IEC+29110-5-1-2-2025.pdf)
- [NASA Software Engineering Handbook — 5.08 SDP-SMP Software Development / Management Plan](https://swehb.nasa.gov/x/WwFiC)
- [ISO/IEC/IEEE 16326:2019 — Project management](https://scc-ccn.ca/standardsdb/standards/8168548)

# USER
1a prsenalizuj pliki md w folderze czapters
https://github.com/m1981/iso-29110-5-1
I
powiedz czy wiadomo jak połączyć plan ze sledzalnoscia? Jeżeli łączymy to jak to zrobimy

# MODEL
Dołączam repozytorium z rozdziałami ISO 29110 i czytam pliki z folderu `chapters`.

Pierwsza próba źle rozpoznała strukturę zadań. Podglądam jedno zadanie w całości.

Mam pełny obraz zadań. Na koniec sprawdzam dwa produkty, przez które plan łączy się ze zmianami: Wniosek o zmianę i Rekord postępu.

Przeczytałem cztery rozdziały, które odpowiadają na twoje pytania: przegląd (05), proces zarządzania projektem (06), proces implementacji (07) i opis produktów pracy (09). **Krótko: tak, wiadomo, jak połączyć plan ze śledzalnością, i ISO/IEC 29110 robi to w pięciu konkretnych miejscach.**

## Jak 29110 łączy plan ze śladem

1. **Definicja śladu obejmuje zadania.** Pojęcie 3.48 (za ISO/IEC/IEEE 12207) mówi o relacjach między wymaganiami, elementami systemu, weryfikacjami i **zadaniami**. Plan jest więc w normie pełnoprawnym uczestnikiem śladu.
2. **Każde zadanie wskazuje produkty, które tworzy, i ich stan.** Cały proces jest zapisany jako *zadanie → produkt pracy [stan]*, np. SI.02.03 „udokumentuj ślad między wymaganiami z umowy a specyfikacją” → *Traceability record [initiated]*. Plan (WP.10) zawiera listę zadań (WBS), a zadania wskazują produkty. To jest łącznik plan ↔ artefakty.
3. **Plan definiuje baseline'y, a każdy baseline ma swój ślad.** Strategia kontroli wersji w planie zawiera „opis baseline'ów projektu”, a przegląd (05) mówi wprost: baseline wymagań śledzi się do umowy, baseline specyfikacji do wymagań, baseline produktu do instrukcji dostarczenia z planu.
4. **Zmiany śledzi się do wniosków o zmianę.** Repozytorium (WP.11) musi zapewniać, że „zmiany produktów pracy są śledzone do wniosków o zmianę”, a wniosek dotyczący planu lub wymagań wymaga zgody klienta (PM.O3). U nas wnioskiem o zmianę jest decyzja D-nn, a hook commit-msg już to wymusza.
5. **Postęp porównuje się z planem element po elemencie.** Rekord postępu (WP.09, zadanie PM.03.01) zestawia rzeczywiste i planowane zadania, wyniki i cele, harmonogram i ryzyka. Żeby dało się to porównać, elementy planu muszą być identyfikowalne.

Sam rekord śladu (WP.21) to w 29110 mapowanie „w przód i wstecz” od wymagań przez projekt i komponenty do testów i **wyników testów**. Nasz model już to pokrywa, a etap kodu dołoży ostatnie ogniwa.

## Jak to zrobimy

Najważniejszy wniosek z normy: 29110 rozdziela **proces** (jak pracujemy) od **planu projektu** (co, po co i kiedy). Nasz `AGENTS.md` to w praktyce proces plus strategia kontroli wersji. Brakuje osobnego planu w sensie WP.10.

| Element planu WP.10 | Gdzie u nas |
|---|---|
| Opis produktu, cel, wymagania ogólne klienta | **plan.md** (nowe) |
| Zakres: co wchodzi, co nie | zakres.md (IO-nn), z planu tylko odsyłacz |
| Cele projektu | **plan.md: CEL-nn** |
| Cykl rozwoju | plan.md, jedno zdanie (u nas przyrostowy: fale) |
| Produkty do dostarczenia + instrukcje dostarczenia | **plan.md: KM-nn** (kamień milowy = baseline = tag) |
| Zadania z weryfikacją, walidacją i przeglądami | **plan.md: ZAD-nn** z polem `produkuje:` |
| Czas, harmonogram, nakład, koszt | plan.md, w skali jednej osoby: daty kamieni |
| Zasoby i skład zespołu | AGENTS.md (człowiek + agent, narzędzia) |
| Ryzyka projektu | **plan.md: RP-nn** (osobno od ryzyk produktu RYZ-nn) |
| Strategia kontroli wersji i baseline'y | AGENTS.md + id.toml + git |

Nowe elementy wchodzą do tego samego modelu w `id.toml`, z jedną świadomą zmianą zasad. Relacja „zadanie **produkuje** artefakt” jest zapisywana w planie, czyli rodzic wskazuje dziecko, odwrotnie niż P-03. Tak robi sama norma i tak jest naturalnie dla planów: zadanie planuje się, zanim artefakt istnieje. Dlatego byłby to jawny, udokumentowany wyjątek.

Skrypt mógłby wtedy generować **`postep.md`**, czyli rekord postępu w sensie PM.03.01: które zadania mają już swoje produkty i w jakim stanie, które kamienie mają tag baseline, które ryzyka są otwarte. To ta sama mechanika co `slad.md`, tylko dla planu.

Interpretuję „prsenalizuj” jako „przeanalizuj”. Jeśli chodziło o coś innego, np. spersonalizowanie tych plików pod nasz projekt, napisz.

---

Zapisuję decyzje w rejestrze szablonu.

**Wykonane**
- Sklonowane repozytorium `m1981/iso-29110-5-1`. Przeanalizowane rozdziały 03 (definicja śladu), 05, 06 (16 + 7 + 4 + 2 zadania PM), 07 (zadania SI ze stanami produktów) i 09 (WP.03 wniosek o zmianę, WP.09 rekord postępu, WP.10 plan projektu, WP.11 repozytorium, WP.21 rekord śladu).
- `ai-sldc-template`: D-07 rozstrzygnięta (ISO/IEC 29110), D-08 przeformułowana po analizie, nowe otwarte D-09…D-11; commit `ec1043f` przez hooki szablonu (blokady gita odsunięte bez usuwania).

**Decyzje**

**1. Gdzie część zarządcza planu** — 29110 rozdziela proces od planu projektu (D-08, przeformułowana).
- **A)** osobny `plan.md` według WP.10 (co, po co, kiedy); `AGENTS.md` zostaje opisem procesu
- **B)** dopisać sekcje do `AGENTS.md`

[P] = A — tak dzieli to norma, a `AGENTS.md` zostaje krótki, choć agent czyta go na start każdej sesji.

**2. Plan jako elementy śladu** — bez ID nie da się porównać postępu z planem (D-09).
- **A)** nowe typy w `id.toml`: cel (CEL-nn), kamień milowy (KM-nn, czyli baseline i tag), zadanie (ZAD-nn) z polem `produkuje:`, ryzyko projektu (RP-nn); `produkuje:` jako jawny wyjątek od P-03
- **B)** plan jako zwykły tekst bez ID

[P] = A — to dokładnie relacje, które 29110 opisuje między zadaniami, produktami i baseline'ami; wyjątek od P-03 odpowiada temu, jak norma zapisuje zadania.

**3. Generowany rekord postępu** — odpowiednik zadania PM.03.01 i produktu WP.09 (D-10).
- **A)** `postep.md` generowany z planu, repozytorium i tagów: zadania z produktami i bez, kamienie z tagiem i bez, otwarte ryzyka
- **B)** bez rekordu postępu

[P] = A — ta sama mechanika co `slad.md`, a „czy jesteśmy zgodnie z planem” przestaje zależeć od pamięci.

**4. Stany produktów pracy** — 29110 śledzi stan każdego produktu (initiated, verified, approved, baselined), a kamienie milowe muszą się do tych stanów odwoływać (D-11).
- **A)** jednolite stany dla wszystkich typów w `id.toml`: rozpoczęty, zweryfikowany, zatwierdzony; „w baseline” wynika z tagów
- **B)** zostać przy statusach osobnych dla każdego typu (draft/zatwierdzone, brief/pełny)

[P] = A — kryterium kamienia typu „wszystkie wymagania zatwierdzone” da się wtedy sprawdzić jednym skryptem dla każdego typu.

**W kolejce**
- Baseline szablonu; zastosowanie szablonu do gtd2; skrypt dla modułu model stanów
- gtd2: przegląd i zatwierdzenie 28 wymagań; suspect links; niezależny przegląd przez osobnego agenta
- gtd2: Podział i wybór Projektu na mapie nawigacji; pozycja wspólna dla kilku Działań; „trwale zapisany” (K-01)

Odpowiedz „ok”, numerem z literą (np. „2B”), numerem z własnym tekstem albo „reszta ok”.

# USER
Czy jesteś w stanie narysować w postaci diagramu  w mermaid pelna strukturę zależności tych encji? czy nasz "model sledzalnosci" który mamy jest kompatybilny z tym co definiuje ISO? Czy wustarczy go
rozszerzyć czy zrobić na nowo?

# MODEL
Tak. Żeby diagram był wierny normie, a nie mojej pamięci, wyprowadzę zależności automatycznie z tekstu: każde zadanie PM i SI podaje swoje produkty wejściowe i wyjściowe, więc skrypt może z nich zbudować pełny graf. Najpierw lista wszystkich produktów pracy.

Teraz graf: dla każdego z 59 zadań łączę każdy produkt wejściowy z każdym wyjściowym, a potem zliczam, przez ile zadań idzie dana zależność.

Teraz strona z oboma diagramami i tabelą zgodności. Pełny graf wstawiam skryptem z wygenerowanego pliku, żeby nie przepisywać 84 krawędzi ręcznie.

Zapisuję nową decyzję w rejestrze szablonu.

Opublikowałem stronę „ISO 29110 a nasz model śladu”. Jest na niej werdykt, rdzeń zależności między 23 produktami normy pokolorowany według tego, co już mamy, tabela zgodności produkt po produkcie i pełny graf 84 zależności. Graf wyliczyłem z wejść i wyjść 72 zadań PM i SI.

**Werdykt: rozszerzyć, nie budować od nowa.** Norma wymaga czterech rzeczy, które nasz model już robi:
- identyfikacji pojedynczych wymagań,
- śladu w przód i wstecz (WP.21),
- baseline'ów powiązanych ze źródłem,
- łączenia zmian z wnioskami o zmianę (WP.11).

Norma śledzi całe dokumenty, a my pojedyncze elementy. Dodatki ponad normę, czyli zasady, słownik, ryzyka produktu, scenki, ekrany i ślad w commitach, są zgodne, bo profil Basic to minimum. Plan łączy się ze śladem tak, że zadanie planu wskazuje produkty, które wytwarza. Z tego powstaje rekord postępu (WP.09).

**Czego brakuje (to brakujące typy, mechanizm śladu jest gotowy):**
- **Plan (WP.10):** jest tylko częściowo, w AGENTS.md, i nie ma typów elementów (D-08, D-09).
- **Rekord postępu (WP.09):** nie ma go (D-10).
- **Rejestr korekt (WP.04):** nie ma go.
- **Weryfikacja (WP.23):** hooki ją wykonują, ale wynik nigdzie się nie zapisuje.
- **Walidacja (WP.22) i akceptacja (WP.01):** nie ma ich.
- **Kopia repozytorium (WP.12):** repozytorium istnieje tylko na Twoim Macu.
- **Stany produktów:** nie są jednolite (D-11).

---

**Wykonane**
- Strona porównawcza opublikowana.
- D-12 zapisana w `decyzje.md` szablonu jako otwarta. Commit `e304c4a`; hook pre-commit zgłosił 0 błędów i 0 ostrzeżeń.
- Git nie mógł sam skasować swoich plików blokady, więc przeniosłem je do `.git/stale-*`. Nic nie zostało usunięte.

**Bez odpowiedzi** (z rejestru szablonu)
- D-08 Plan w osobnym `plan.md`, a nie w AGENTS.md. Propozycja A.
- D-09 Typy elementów planu CEL/KM/ZAD/RP; pole `produkuje:` jako wyjątek od P-03. Propozycja A.
- D-10 Postęp generowany do `postep.md`. Propozycja A.
- D-11 Jednolite stany produktów pracy. Propozycja A.

**Decyzje**
1. D-12 Model śladu wobec ISO 29110:
   - **A)** Rozszerzyć: pole `iso` w `id.toml`, nowe typy dla rekordów (postęp, korekty, weryfikacja, walidacja, akceptacja) i kopia zapasowa repozytorium.
   - **B)** Zbudować od nowa według listy produktów normy.

   Propozycja: **A**.

**W kolejce**
- baseline szablonu
- przeniesienie szablonu na gtd2
- skrypt do modułu model-stanow
- przegląd 28 wymagań gtd2
- wymagania do sprawdzenia po zmianie rodzica (K-10)
- niezależny przegląd przez agenta (K-11)
- ekrany w słowniku (K-13)
- ryzyka (K-12, odłożone)

Odpowiedz kodami, np. „D-08a D-09a D-10a D-11a 1a”, albo „ok” dla wszystkich propozycji.

# USER
D08 A
D09 A
D10 A
D11 A
D12 A

# MODEL
Zapisuję pięć rozstrzygnięć w rejestrze, a potem wprowadzam je do szablonu.

Rejestr ma już opcje dla wszystkich pięciu decyzji. Wprowadzam je plik po pliku, zaczynając od modelu śladu.

Model jest wczytywany poprawnie, a obecne elementy nie zgłaszają błędów. Następny plik to `model.py`, w którym dodaję stany produktów i obsługę pola `produkuje:`.

`model.py` gotowy. Teraz `slad.py`: nowe kontrole i dwie nowe sekcje w `slad.md`.

`slad.py` gotowy. Teraz nowy generator rekordu postępu, `narzedzia/postep.py`.

Generator działa i pomija pracę, dopóki nie ma planu. Następny plik to `plan.md`, czyli część zarządcza wzorowana na WP.10.

Działa. Następny plik to `rekordy.md` z korektami, weryfikacjami, walidacjami i akceptacjami.

Następny plik to `wymagania.md`: status wymagań przechodzi na jednolite stany.

Następny plik to `AGENTS.md`. Zostaje w nim sam proces pracy, a zakres przechodzi do planu.

Teraz `Makefile`.

Następny plik to hook pre-commit, który teraz sprawdza też aktualność `postep.md`.

Teraz test narzędzi: dokładam do łańcucha wzorcowego plan i rekordy oraz nowe sposoby psucia.

Ciąg `draft` występuje cztery razy, bo raz jest też w jednym ze sposobów psucia. Poprawiam licznik i uruchamiam jeszcze raz.

Testy przechodzą. Następny plik to `README.md`.

Zostaje rejestr: zamykam D-08…D-12, a założenia, które przyjąłem przy wdrażaniu, zapisuję jako nowe otwarte decyzje.

Rejestr jest gotowy. Ostrzeżenia O2 znikną, gdy commit wymieni D-09 i D-10. Przeglądam cały diff i commituję.

Wprowadziłem wszystkie pięć decyzji (D-08…D-12) do szablonu w jednym commicie `a32c5f9`. Test narzędzi przechodzi, a ślad pokazuje 0 błędów i 0 ostrzeżeń.

**Co się zmieniło:**
- **D-08:** nowy `plan.md` według ISO WP.10 (produkt i zakres, cykl, zespół, wersjonowanie, cele, kamienie, zadania, ryzyka projektu). AGENTS.md opisuje już tylko sposób pracy, a sekcja „Zakres” przeszła do planu.
- **D-09:** w modelu śladu są nowe typy CEL, KM, ZAD i RP. Zadanie w polu `produkuje:` wskazuje kody typów albo konkretne ID. To jedyny wyjątek od zasady, że dziecko wskazuje rodzica.
- **D-10:** nowy skrypt `narzedzia/postep.py` generuje `postep.md`. Pokazuje kamienie z datą tagu i akceptacją, zadania (termin a data zakończenia), ryzyka, korekty w toku i liczby produktów w każdym stanie. Pre-commit odrzuca commit, gdy `postep.md` jest nieaktualny.
- **D-11:** produkty pracy mają wspólne stany: rozpoczęty, zweryfikowany, zatwierdzony. Wymagania przeszły z „draft” na te stany.
- **D-12:** każdy typ w `id.toml` ma pole `iso`, a `slad.md` pokazuje mapowanie na produkty normy. Nowe rekordy KOR, WER, WAL i AKC są w `rekordy.md`. Wymaganie w stanie „zweryfikowany” bez rekordu WER z wynikiem „zgodny” daje ostrzeżenie O3.
- **Test narzędzi:** obejmuje teraz plan, rekordy, 13 sposobów psucia, 3 ostrzeżenia oraz scenariusz z tagiem baseline, po którym nieaktualny `postep.md` blokuje commit. Kamień pokazuje się wtedy jako osiągnięty.

Przy wdrażaniu musiałem przyjąć kilka założeń. Wpisałem je do rejestru jako otwarte decyzje D-14…D-16 i działają tylko do Twojej odpowiedzi.

---

**Wykonane**
- D-08…D-12 rozstrzygnięte i wdrożone (commit `a32c5f9`).
- Rejestr: nowe otwarte decyzje D-13…D-16 i dwa tematy w kolejce, K-01 i K-02.
- Git nie może sam kasować swoich plików, więc blokady przeniosłem do `.git/stale-*`. Zostają też drobne pliki tymczasowe w `.git/objects`; są nieszkodliwe. Nic nie zostało usunięte.

**Decyzje**
1. **D-13 Kopia zapasowa repozytorium (WP.12).** Dziś repozytorium jest tylko na jednym Macu.
   - A) prywatne repozytorium na GitHubie jako drugi remote, push po każdej sesji i po baseline
   - B) dysk zewnętrzny albo Time Machine
   - C) oba

   Propozycja: **A**. Niczego nie zakładam bez Twojej zgody.
2. **D-14 Zakres wspólnych stanów.**
   - A) stany mają tylko produkty pracy (SC, IO, ZP, G, UC, RYZ, WYM, E, AT); decyzje, zadania, ryzyka projektu i rekordy zachowują własne statusy; brak pola status oznacza „rozpoczęty”; pole jest obowiązkowe tylko w wymaganiach
   - B) pole status obowiązkowe we wszystkich produktach pracy

   Propozycja: **A** (tak jest wdrożone).
3. **D-15 „Zweryfikowany” bez rekordu WER.**
   - A) ostrzeżenie, commit przechodzi
   - B) błąd, który blokuje commit

   Propozycja: **A**, dopóki zapisywanie przeglądów nie stanie się nawykiem.
4. **D-16 Układ planu i rekordów.**
   - A) jak wdrożono: cztery rodzaje rekordów w jednym `rekordy.md`; `produkuje:` przyjmuje kody typów albo ID; kamień jest osiągnięty, gdy istnieje tag z pola `tag:`
   - B) każdy rodzaj rekordu w osobnym pliku

   Propozycja: **A**.

**W kolejce**
- K-01: odświeżyć stronę „ISO 29110 a nasz model śladu”, bo kolory pokazują stan sprzed tych zmian.
- K-02: przenieść zmiany szablonu do gtd2 (28 wymagań przejdzie z „draft” na „rozpoczęty”).
- Pozostałe tematy bez zmian:
  - baseline szablonu
  - skrypt do modułu model-stanow
  - przegląd wymagań gtd2
  - wymagania do sprawdzenia po zmianie rodzica (K-10)
  - niezależny przegląd przez agenta (K-11)
  - ekrany w słowniku (K-13)
  - ryzyka produktu (K-12)

Odpowiedz kodami, np. „D13a D14a D15a D16a”, albo „ok” dla wszystkich propozycji.

# USER
D-13 git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:m1981/iso-template-agent.git
git push -u origin main

D14 Przemysl i sporobuj to wytlumaczyc inaczej bo nie rozumiem
D-15 a
D-16 co bedzie latwiejsz i bardziej deterministyczne do sledzenia kiedy staleje ?
Generalnie mam dysonans ponzwaczy bo norma jest po angielsku a nasze ID i nazewnictwo jest po polsku. Przemysl strategie i zakres zunifikowania z jezykiem angielskim i konsekwencje/ryzyka i kroki adaptacji

# MODEL
Wykonuję D-13 (remote i push) i zapisuję D-15. Potem odpowiadam na pytania o D-14, D-16 i język.

Gałąź już nazywa się `main`, a commity są, więc pierwsze dwa polecenia nic by nie zmieniły. Dodaję remote i próbuję wypchnąć.

Z maszyny wirtualnej na Twoim Macu nie da się połączyć z GitHubem przez SSH, a Twoich kluczy SSH tam nie ma. Spróbuję wypchnąć to samo repozytorium przez połączenie GitHub tej sesji.

Repozytorium na GitHubie istnieje i jest puste, ale niczego jeszcze nie wypchnąłem. Na Macu remote `origin` jest już dodany. Push przez SSH stamtąd nie przeszedł, bo maszyna wirtualna, w której wykonuję polecenia, nie łączy się z GitHubem i nie ma Twoich kluczy SSH. Zaraz potem Mac przestał odpowiadać, więc nie mogłem też przenieść repozytorium drogą okrężną.

Najprościej wypchniesz je sam w terminalu na Macu. `git commit` i `git branch -M main` pomiń: commity już są, a gałąź już nazywa się `main`.

```
cd ~/PycharmProjects/ai-sldc-template
git push -u origin main --follow-tags
```

`--follow-tags` wysyła też tagi baseline. Bez nich kopia na GitHubie nie miałaby kamieni milowych, a `postep.md` w świeżym klonie wyszedłby inny niż u Ciebie. Na razie tagów nie ma, więc dziś nie ma to znaczenia.

Wyboru D-15a oraz stanu D-13 (remote dodany, push czeka na Ciebie) jeszcze nie zapisałem w rejestrze. Zrobię to w następnym commicie, gdy Mac znów będzie dostępny.

---

## D-14 inaczej

Wspólne stany (rozpoczęty, zweryfikowany, zatwierdzony) opisują jedną rzecz: **jak dojrzała jest treść**. Wymaganie najpierw jest szkicem, potem ktoś je sprawdza, potem je zatwierdzasz.

Część elementów w ogóle nie dojrzewa w ten sposób. One mają inny cykl:

| Element | Co się z nim dzieje | Jego statusy |
| --- | --- | --- |
| wymaganie, przypadek użycia, scenka, pojęcie, ekran, test | treść dojrzewa | rozpoczęty → zweryfikowany → zatwierdzony |
| decyzja | jest otwarta, potem rozstrzygnięta | otwarta, rozstrzygnięta, odłożona |
| zadanie | jest wykonywane | planowane, w toku, zakończone |
| rekord weryfikacji | to zapis faktu, nie dojrzewa | brak statusu, ma wynik: zgodny albo niezgodny |

D-14 rozstrzyga dwie rzeczy.

1. **Czy drabinkę dostają tylko elementy, które dojrzewają.** Proponuję, że tak. Decyzja w stanie „zweryfikowana” nie miałaby sensu.
2. **Czy trzeba wpisywać `status:`, gdy element dopiero powstał.**
   - **A:** nie trzeba. Brak linii oznacza „rozpoczęty”, a status dopisujesz dopiero przy awansie. Wyjątkiem są wymagania, bo zatwierdzenie wymaga decyzji (P-08).
   - **B:** każdy element musi mieć linię `status:`, nawet świeżo napisana scenka. Bez niej commit jest blokowany.

Obie wersje są tak samo deterministyczne, bo reguła „brak = rozpoczęty” jest stała i zapisana w skrypcie. A oznacza mniej pisania. B jest bardziej jawne: z samego pliku widać stan, bez znajomości reguły. Zostaję przy **A**.

## D-16: kiedy `postep.md` się dezaktualizuje

`postep.md` jest wyliczany wyłącznie z plików w repozytorium i z tagów. Nie zależy od dzisiejszej daty. Dezaktualizuje się więc tylko w dwóch sytuacjach:

1. **Zmieniasz plan, rekord albo status i nie odświeżasz pliku.** Pre-commit wykrywa to zawsze, przed commitem.
2. **Tworzysz tag baseline.** Tag nie jest częścią commita, więc plik jest nieaktualny do następnego commita. `make baseline` od razu go odświeża, a pre-commit i tak to sprawdzi.

**Liczba plików z rekordami nie ma na to wpływu.** Kontrola porównuje cały wygenerowany wynik, bez względu na to, z ilu plików powstał. Wybór między A i B dotyczy wygody:

- **A, jeden `rekordy.md`:** jedno miejsce do czytania, mniej plików.
- **B, cztery pliki:** historia gita osobno dla każdego rodzaju rekordu. Nazwa pliku mówi, co jest w środku. Mniej kolizji, gdy dwie osoby lub dwa agenty piszą jednocześnie.

Dla jednej osoby z agentem proponuję **A**. Przy przejściu na angielski (niżej) wybrałbym jednak **B**, bo `verification.md` i `acceptance.md` wprost odpowiadają nazwom produktów w normie.

## Polski a angielski: strategia

Repozytorium ma dwie warstwy, a dysonans dotyczy tylko jednej z nich:

- **Warstwa maszynowa:** kody ID, nazwy pól (`źródło:`, `produkuje:`), stany, nazwy plików i skryptów, kody błędów. Tę warstwę czytają skrypty, agent i ktoś, kto porównuje z normą.
- **Warstwa ludzka:** treść dokumentów, tytuły, rejestr decyzji, nasza rozmowa. Tu myślisz i decydujesz.

**Propozycja: angielski w warstwie maszynowej, polski w treści.** Nazywam ją **A** w D-17 niżej. Wymagania EARS już są po angielsku, więc to ten sam podział, tylko konsekwentny. Za tym podziałem przemawiają trzy rzeczy:

1. **Stany wprost z normy.** Tabela 12 normy ma *initiated*, *verified*, *approved*, a dla rejestru korekt *initiated*, *approved*, *completed*. Nie trzeba niczego tłumaczyć.
2. **Koniec z polskimi znakami w kluczach.** `kamień:` wpisane jako `kamien:` dziś po cichu przestaje działać jako pole. Kontrola łapie to tylko dlatego, że brakuje wymaganego pola, a przy polach opcjonalnych nie złapie wcale.
3. **Łatwiejsze przeniesienie szablonu na inne projekty.** Szablon da się użyć w projekcie z kimś spoza Polski, a słownik pojęć staje się wtedy jedynym miejscem tłumaczenia.

**Proponowane nazwy:**

| Dziś | Po zmianie | Termin ISO |
| --- | --- | --- |
| CEL, KM, ZAD, RP | OBJ, MS, TSK, PRK | objectives, milestone, task, project risk (WP.10) |
| KOR, WER, WAL, AKC | COR, VER, VAL, ACC | WP.04, WP.23, WP.22, WP.01 |
| ZP, RYZ, K | DP, RSK, Q | design principle, risk, queue |
| SC, IO, D, G, UC, E, AT | bez zmian | już działają po angielsku |
| `źródło`, `produkuje`, `kamień`, `wynik` | `source`, `produces`, `milestone`, `result` | — |
| rozpoczęty / zweryfikowany / zatwierdzony | initiated / verified / approved | tabela 12 normy |
| `slad.md`, `postep.md`, `decyzje.md`, `narzedzia/` | `trace.md`, `progress.md`, `decisions.md`, `tools/` | WP.21, WP.09 |
| kody błędów B1…, O1… | E1…, W1… | — |

Po polsku zostają: treść i tytuły, rejestr decyzji, `kontrakt-decyzji.md`, komunikaty skryptów, opisy commitów i nasza rozmowa.

**Konsekwencje i ryzyka:**

- **Niezmienność ID (P-02).** To główne ryzyko. W szablonie kosztuje to niewiele: elementy mają tylko typy D i K, a typy do przemianowania są puste, z wyjątkiem K-01 i K-02 sprzed godziny. W gtd2 jest ponad 150 ID, do których odwołują się commity. Dlatego w gtd2 **ID zostają**, zmieniają się tylko nazwy pól, stany i plików.
- **Pliki o mieszanym języku.** Na przykład `- source: UC-01` pod polskim zdaniem. Czyta się to jak kod w tekście, to znany i akceptowany wzorzec.
- **Agent może wracać do starych polskich nazw pól.** Kontrola łapie pomyłkę w polu wymaganym (zgłasza brak pola). W polu opcjonalnym pomyłka przejdzie po cichu. Mogę dodać ostrzeżenie o nieznanym polu, które zamyka tę lukę.
- **Zmiana nazw naraz psuje hooki w połowie pracy.** Dlatego robi się ją jednym commitem z testem, a przed nią stawia się tag, do którego można wrócić.
- **Odnośniki na zewnątrz.** `start-tutaj.md` w projekcie „GTD” i opublikowane strony podają stare nazwy plików, więc trzeba je zaktualizować.

**Kroki:**

1. Postawić tag `baseline-00-przed-en`, punkt powrotu.
2. Przenieść nazwy pól, które skrypty mają dziś wpisane na stałe (`status`, `produkuje`, `tag`…), do `id.toml`. Wtedy język warstwy maszynowej staje się konfiguracją.
3. Zmienić nazwy kodów, pól, stanów i plików przez `git mv`, żeby historia przetrwała. Zaktualizować test i uruchomić `make test`. Zrobić jeden commit.
4. Dopisać do słownika tabelę polsko-angielską terminów normy.
5. gtd2 osobno (K-02): skrypt migracji pól i stanów; ID bez zmian.

---

**Wykonane**
- D-13 częściowo: remote `origin` dodany na Macu, repozytorium na GitHubie sprawdzone (istnieje, puste). Push czeka na Twoje polecenie wyżej.
- D-15a przyjęte. Zapiszę je w rejestrze, gdy Mac znów będzie dostępny.

**Bez odpowiedzi**
- D-16: odpowiedziałem wyżej. Czekam na wybór A albo B.

**Decyzje**
1. **D-14 Zakres wspólnych stanów:**
   - **A)** drabinkę mają tylko elementy, które dojrzewają; brak statusu oznacza „rozpoczęty”
   - **B)** każdy taki element musi mieć linię `status:`

   Propozycja: **A**.
2. **D-17 Język warstwy maszynowej:**
   - **A)** angielski w kodach, polach, stanach, nazwach plików i skryptów; polski w treści; w gtd2 ID zostają
   - **B)** całość po angielsku, także treść
   - **C)** zostaje polski, dochodzi tylko tabela polsko-angielska w słowniku

   Propozycja: **A**.
3. **D-18 Nazwy z tabeli wyżej:**
   - **A)** przyjąć tabelę bez zmian
   - **B)** przyjąć z poprawkami (napisz które)

   Propozycja: **A**. Ma znaczenie tylko przy D-17 A albo B.
4. **D-19 Kolejność:**
   - **A)** najpierw zmiana języka w szablonie, potem baseline szablonu i przeniesienie do gtd2
   - **B)** najpierw baseline obecnej wersji, potem zmiana języka

   Propozycja: **A**, bo tak taniej. Nic jeszcze nie zależy od obecnych nazw.

**W kolejce**
- K-01 (odświeżenie strony ISO), K-02 (przeniesienie do gtd2), skrypt do modułu model-stanow, K-10…K-13.

Odpowiedz kodami, np. „D14a D16a D17a D18a D19a”, albo „ok” dla wszystkich propozycji.

# USER
1 tak
2 b latwiej będzie pasować
d16 b zrobmy te dwa pliki z normy
d17 a d18 a d19 a
włączyłem komputer spróbuj push zrobić

# MODEL
Twoją odpowiedź czytam tak:
- D-14: drabinka stanów tylko dla elementów, które dojrzewają, a pole `status:` jest obowiązkowe (wariant B).
- D-16 B: cztery osobne pliki rekordów nazwane jak produkty normy.
- D-17, D-18, D-19: A.

Najpierw wypycham obecny stan na GitHuba.

Kopia robocza na Macu jest czysta. Zmianę języka przygotuję i przetestuję w kopii w chmurze, która jest identyczna z Twoim `main`, a potem przeniosę ją na Maca jako jeden commit.

Przed zmianą nazw czytam wszystkie pliki szablonu, żeby niczego nie pominąć.

Nazwy plików zmienione. Teraz `tools/id.toml` z angielskimi kluczami, kodami, polami i stanami oraz nową tabelą `[fields]` z nazwami pól, które czytają skrypty.

Teraz `tools/model.py`: czyta angielskie klucze, a dla produktów pracy status jest obowiązkowy (D-14 B).

Teraz hook pre-commit.

Teraz moduł nawigacji.

Moduł nawigacji przechodzi swoje reguły R1–R7. Teraz jego README i README modułów ryzyk i modelu stanów.

Teraz pliki artefaktów w katalogu głównym. Zaczynam od scenek, zakresu, zasad i słownika.

Teraz przypadki użycia, wymagania i testy. W przypadkach użycia „brief/pełny” przechodzi z pola `status` do osobnego pola `form`, bo `status` należy teraz do stanów produktu.

Teraz `plan.md` i podział rekordów na cztery pliki (D-16 B).

Jedna z zamian była zbędna (nic nie zmieniała) i nie pasowała do tekstu. Usuwam ją i uruchamiam resztę.

Teraz cztery pliki rekordów.

Teraz rejestr `decisions.md`: angielskie pola i stany, K→Q, zamknięcie D-13…D-19 i nowe otwarte decyzje dla nazw, których nie było w tabeli D-18.

Teraz `AGENTS.md`, `README.md`, `CLAUDE.md` i odnośniki w kontrakcie.

Zostały tylko pliki generowane (zaraz je odświeżę) i polskie nazwy zmiennych w kodzie. Generuję pliki i uruchamiam test.

Wiersz w teście był źle zapisany: SC-01 ma dwoje dzieci, UC-01 i VAL-01. Poprawiam oczekiwanie.

Test przechodzi: 14 sposobów psucia, 3 ostrzeżenia, rekord postępu i hooki. Przeglądam całość zmian przed przeniesieniem na Maca.

Stan plików jest wzorcowy (drzewo `35b639f`). Przenoszę go na Maca jako archiwum: zmiana nazw przez `mv`, nadpisanie treści i porównanie drzewa gita z wzorcem.

Pliki są na miejscu. Porównuję drzewo gita z wzorcem i uruchamiam test na Macu.

Drzewo na Macu jest identyczne z wzorcowym, a test przechodzi. Commituję na Macu z hookami. W opisie wymieniam każdą decyzję osobno, bo zakres „D-13…D-19” zostawiał D-15 bez wzmianki.

Commit `911ab4a` jest na Macu, a ślad pokazuje 0 błędów i 0 ostrzeżeń. Wypycham go razem z tagiem na GitHuba.

GitHub odrzucił push (403). Sprawdzam, czy blokada dotyczy tagu, czy samej gałęzi.

Gałąź `main` jest na GitHubie (`911ab4a`). Tagów ta sesja nie może wypychać, bo serwer pośredniczący odrzuca je kodem 403. Aktualizuję na Macu informację o stanie `origin/main`.

Zrobione: push na GitHuba przeszedł, a zmiana języka jest w commicie `911ab4a`, na Macu i na GitHubie.

Twoje odpowiedzi odczytałem tak:
- **„1 tak, 2 b”** to dwa punkty D-14 z mojego wyjaśnienia. Stany mają tylko elementy, które dojrzewają, a pole `status:` jest obowiązkowe w każdym z nich. Brak tego pola blokuje commit.
- **D-16 b, „te dwa pliki z normy”**: każdy rodzaj rekordu dostał osobny plik nazwany jak produkt normy, więc są cztery: `corrections.md`, `verification.md`, `validation.md`, `acceptance.md`. Jeśli chodziło Ci tylko o dwa, napisz, które połączyć.

**Co się zmieniło w szablonie:**
- **Nazwy po angielsku.** Pliki, kody ID, pola, stany i polecenia `make` dostały nazwy z tabeli D-18. Na przykład `slad.md` to teraz `trace.md`, a zadanie `ZAD-nn` to `TSK-nn`.
- **Stany jak w normie.** Produkty pracy mają stany initiated, verified, approved, wprost z tabeli 12 ISO.
- **Kody błędów.** Błędy to E1–E8, ostrzeżenia W1–W3.
- **Tabela terminów normy.** W `glossary.md` jest tabela polsko-angielska. To jedyne miejsce tłumaczenia.
- **Treść bez zmian.** Opisy, rejestr i kontrakt są nadal po polsku.
- **Kontrola na Macu.** Stan plików na Macu sprawdziłem bit po bicie z wersją przygotowaną i przetestowaną w chmurze. Test narzędzi przechodzi, a ślad pokazuje 0 błędów i 0 ostrzeżeń.

**Jedna rzecz do zrobienia na Macu.** Tag `baseline-00-przed-en`, czyli punkt powrotu sprzed zmiany języka, jest tylko u Ciebie. Ta sesja nie może wypychać tagów na GitHuba. Wyślij go raz w terminalu:

```
git push origin baseline-00-przed-en
```

Kolejne tagi pójdą już same przy zwykłym `git push`, bo ustawiłem `push.followTags`.

---

**Wykonane**
- D-13: remote `origin` dodany, a `main` wypchnięty na GitHuba (najpierw `a32c5f9`, potem `911ab4a`).
- D-14 (status obowiązkowy), D-15a, D-16 B, D-17a, D-18a i D-19a wdrożone i zapisane jako rozstrzygnięte.
- Git na Macu nie może sam kasować swoich plików, więc blokady i archiwa robocze przeniosłem do `.git/stale-*`. Nic nie zostało usunięte.

**Decyzje**
1. **D-20 Nazwy spoza tabeli D-18.** Przy wdrażaniu musiałem nadać nazwy rzeczom, których tabela nie obejmowała. Pełna lista jest w `decisions.md`. Najważniejsze:
   - kod typu wymagań to `REQ` (dawniej WYM);
   - klucze w `id.toml` są po angielsku;
   - pola i wartości są po angielsku (np. `established_by`, `primary_actor`, poziomy celu `sea`/`kite`/`fish`);
   - przypadek użycia ma nowe pole `form: brief | full`, bo `status` należy teraz do stanów produktu;
   - `kontrakt-decyzji.md` zostaje pod polską nazwą;
   - nazwy zmiennych i funkcji w kodzie Pythona zostają polskie.

   Opcje: **A)** przyjąć jak wdrożono · **B)** przyjąć z poprawkami (wskaż które).

   Propozycja: **A**.
2. **D-21 Ostrzeżenie o nieznanym polu.** Dawna polska nazwa w polu opcjonalnym, np. `źródło:` zamiast `source:`, dziś przechodzi bez żadnego sygnału.
   - **A)** nowe ostrzeżenie W4 dla pól spoza listy znanych pól danego typu
   - **B)** bez takiej kontroli

   Propozycja: **A**.

**W kolejce**
- Q-01: odświeżyć stronę „ISO 29110 a nasz model śladu”.
- Q-02: przenieść zmiany szablonu do gtd2. ID zostają bez zmian, migrują nazwy pól, stanów i plików.
- Pozostałe tematy bez zmian:
  - baseline szablonu
  - skrypt do modułu model stanów
  - przegląd wymagań gtd2
  - K-10…K-13 (rejestr gtd2)

Odpowiedz kodami, np. „D20a D21a”, albo „ok” dla wszystkich propozycji.

# USER
1) a na prawde mamy nazwy funkcji i klas po polsku?
2) a

# MODEL
Sprawdzam stan repozytorium i spisuję nazwy funkcji i klas w kodzie.

Na Twoje pierwsze pytanie mam już odpowiedź ze spisu kodu. Teraz wdrażam D-21 A.

Działa: test sprawdza teraz 5 ostrzeżeń, w tym dwa przypadki W4 (dawne `źródło:` i `działanie:`), a łańcuch wzorcowy nie daje fałszywych W4. Zapisuję rejestr.

Na Twoje pierwsze pytanie: tak, ale tylko w kodzie, którego nie widać w artefaktach. **W4 jest wdrożone**, wypchnięte na GitHuba jako commit `75d6791`, a test przechodzi.

**Co jest po polsku w kodzie.** Spisałem wszystkie definicje w `tools/` i `modules/navigation/`:
- **Klasy:** dwie, `Element` i `Model`. Ich nazwy brzmią tak samo w obu językach.
- **Funkcje i metody:** 20 z 30 ma polskie nazwy. Przykłady:
  - `wczytaj_toml`, `produkty`, `pliki_aktywne`, `stan` w `model.py`;
  - `pojecia`, `nieznane_pojecia`, `wzmianki_w_commitach` w `trace.py`;
  - `wczytaj`, `graf`, `kroki` w module nawigacji.
- **Atrybuty i zmienne:** prawie wszystkie są po polsku, np. `e.pola`, `e.typ`, `m.elementy`, `m.po_id`, `bledy`, `ostrz`.
- **Po angielsku:** wszystko, co skrypty czytają z plików i pokazują na zewnątrz, czyli klucze `id.toml`, pola, stany, pliki i kody błędów (D-17).

Tę granicę wyznaczyłem przy wdrażaniu D-17 jako założenie. Zapisałem ją w D-20, a w rejestrze dopisałem opcję C: nazwy w kodzie też po angielsku. Pomyliłem się przy tym w liczbach: rejestr podaje „21 z 33 funkcji”, a poprawnie jest 20 z 30. Poprawię to w następnym commicie, żeby nie robić drugiego commita w tej wiadomości.

**W4 w praktyce.** Pole spoza listy znanych pól danego typu daje ostrzeżenie, np. `- źródło: UC-01` zamiast `- source: UC-01`. Listę pól pozwolonych w każdym typie dopisałem w `id.toml`, a pole `notes` jest dozwolone wszędzie. Ostrzeżenie nie blokuje commita, zgodnie z P-05.

**Na Macu.** Twój Mac jest teraz niedostępny, więc commit powstał w kopii w chmurze i poszedł prosto na GitHuba. U Ciebie w terminalu:

```
git pull --ff-only
git push origin baseline-00-przed-en
```

Pierwsze polecenie ściąga `75d6791`. Drugie wysyła tag, który jest nadal tylko u Ciebie.

---

**Wykonane**
- D-21 A: ostrzeżenie W4 wdrożone, test obejmuje dwa przypadki z dawnymi polskimi nazwami pól, commit `75d6791` jest na GitHubie.

**Bez odpowiedzi**
1. **D-20 Nazwy spoza tabeli D-18:**
   - **A)** przyjąć jak wdrożono, kod Pythona zostaje po polsku
   - **B)** przyjąć z poprawkami (wskaż które)
   - **C)** jak A, ale nazwy w kodzie też po angielsku

   Propozycja: **A**. Nazw w kodzie nie widać w artefaktach, a ich zmiana dotyka każdego skryptu. Za C przemawia to, że wtedy cały kod jest jednojęzyczny, a za kod odpowiada głównie agent.

**W kolejce**
- poprawka liczb w D-20
- Q-01: odświeżenie strony ISO
- Q-02: przeniesienie zmian do gtd2
- baseline szablonu
- skrypt do modułu model stanów
- K-10…K-13 (rejestr gtd2)

Odpowiedz kodem, np. „D20a”, albo „ok”, jeśli zostajemy przy propozycji.

# USER
d20 C. lepiej będzie zmienić teraz. Czy jesteś to w stanie bezpiecznie zmienić? Jak to zrobisz ?

# MODEL
Tak, da się to zrobić bezpiecznie, i robię to od razu, bo decyzja zapadła. Bezpieczeństwo zapewniają trzy rzeczy:
- **Zmieniam tylko nazwy w kodzie.** Narzędzie rozbija każdy plik na tokeny Pythona i podmienia wyłącznie nazwy. Napisy (komunikaty, pola w `id.toml`), komentarze i opisy funkcji zostają nietknięte.
- **Wzorzec przed i po.** Przed zmianą zapisuję wszystko, co skrypty produkują na pełnym łańcuchu przykładowym i przy każdym psuciu. Po zmianie wynik musi być identyczny co do bajtu.
- **Test i kolizje.** `make test` musi przejść, a żadna nowa nazwa nie może zderzyć się z istniejącą.

Zaczynam od spisu wszystkich nazw.

Spis pokazuje 274 nazwy. Najpierw sprawdzam, jakie polskie klucze słowników są zapisane w kodzie jako napisy, bo tych tokenizer nie podmieni.

Wzorzec ma 23 przypadki, około 257 KB wyjścia. Sprawdzam jeszcze, czy jest powtarzalny: dwa przebiegi muszą dać identyczny wynik.

Różnica dotyczy tylko losowej nazwy katalogu tymczasowego w nagłówku mojego skryptu, nie wyniku narzędzi. Podaję ścieżkę względną i powtarzam.

Sześć plików przechodzi kontrolę, `trace.py` nie. Sprawdzam, gdzie drzewa składni się różnią, zanim cokolwiek zapiszę.

Drzewa składni są teraz równoważne we wszystkich siedmiu plikach. Kolizje sprawdzam jeszcze ręcznie i dokładniej: czy któraś nowa nazwa występowała już w tym samym pliku.

Zmiana zapisana. Zostały trzy wzmianki o `KLUCZOWE` w opisach (to tekst, nie kod), więc poprawiam je ręcznie. Potem porównuję z wzorcem.

Wszystkie nazwy w kodzie są teraz po angielsku. Zapisuję D-20 w rejestrze, z poprawioną liczbą 20 z 30, i commituję.

Rzucam okiem na fragment diffu, żeby zobaczyć, jak zmiana wygląda dla człowieka.

Zmiana jest zrobiona i jest na GitHubie jako commit `e187e0a`. Funkcje, metody, atrybuty, zmienne i stałe w `tools/` i `modules/navigation/` mają teraz angielskie nazwy. Komunikaty, opisy i komentarze zostały po polsku. Kod zachowuje się dokładnie tak samo jak przed zmianą.

**Jak zabezpieczyłem zmianę.**
1. **Wzorzec przed zmianą.** Uruchomiłem wszystkie skrypty na pełnym przykładowym łańcuchu śladu i przy każdym z 19 sposobów psucia, a także hook commit-msg. Zapisałem całe wyjście: 23 przypadki, około 257 KB. Dwa przebiegi dały identyczny wynik.
2. **Zmiana po tokenach, nie przez szukaj-zamień.** Skrypt podmieniał wyłącznie nazwy w kodzie Pythona, więc napisy i komentarze zostały nietknięte. Trzy polskie klucze słowników zapisane w kodzie jako napisy (`"pliki"`, `"aktywny"`, `"znane"`) zmieniłem osobno. Nazwy po kropce, np. `e.pola`, miały własną mapę.
3. **Trzy kontrole, każda łapie coś innego:**
   - **Drzewa składni.** Kod przed i po zmianie musiał mieć to samo drzewo składni, po uwzględnieniu mapy nazw. Ta kontrola złapała klucz w pojedynczym cudzysłowie wewnątrz f-stringu, który moja mapa pominęła.
   - **Porównanie z wzorcem.** Złapało błąd, którego drzewa składni nie widziały: metoda `p` dostała nową nazwę `value` w wywołaniach, ale nie w definicji. Po poprawce wynik jest identyczny z wzorcem co do bajtu.
   - **Kolizje i spójność.** Żadna nowa nazwa nie zderzyła się z istniejącą. Każdy atrybut i każda metoda, po które sięgają skrypty, są zdefiniowane w klasach.
4. **Test narzędzi.** `make test` przechodzi, a ślad pokazuje 0 błędów i 0 ostrzeżeń.

**Na Macu** w terminalu:

```
git pull --ff-only
git push origin baseline-00-przed-en
```

Pierwsze polecenie ściąga dwa nowe commity, `75d6791` (W4) i `e187e0a`. Drugie wysyła tag, który nadal jest tylko u Ciebie.

---

**Wykonane**
- D-20 C: wdrożone i zapisane w rejestrze. Poprawiłem też liczbę funkcji w rejestrze na 20 z 30.
- Commit `e187e0a` wypchnięty na GitHuba.

**Bez odpowiedzi**
- brak; w rejestrze nie ma otwartych decyzji

**Decyzje**
- brak nowych

**W kolejce**
- baseline szablonu
- Q-01: odświeżenie strony ISO
- Q-02: przeniesienie zmian do gtd2
- skrypt do modułu model stanów
- K-10…K-13 (rejestr gtd2)

Wskaż temat z kolejki, którym mam się zająć jako następnym.

# USER
co jest do zrobienia w baseline, Q1 ?

# MODEL
Odpowiadam na oba pytania. Najpierw sprawdzam aktualny stan repozytorium i strony ISO, żeby lista prac była oparta na faktach.

Mam pełen obraz. Pytania, od których zależy zakres obu prac, zapisuję w rejestrze jako otwarte decyzje.

## Baseline szablonu

Baseline to tag, który zamraża wersję szablonu, z której startują nowe projekty (P-09). Sam tag to jedno polecenie. Przed nim trzeba załatwić trzy rzeczy:

1. **Historia szablonu w nowych projektach (D-22).** To najważniejsza z trzech. Kto dziś skopiuje szablon, dostaje nasze decyzje D-01…D-21 jako własne, a do tego `trace.md` i `progress.md` z naszymi danymi. Proponuję polecenie `make new-project`, które przenosi tę historię do `archive/template/` (archiwizuje, nie usuwa) i zostawia pusty rejestr z samym formatem.
2. **Niezależny przegląd (D-23).** Po dwóch dużych zmianach nazw (D-17 i D-20) mogły zostać stare odwołania w tekście. Moje sprawdzanie grepem ma ślepe plamy. Lepiej, żeby całość przejrzał osobny agent bez kontekstu tej rozmowy. Usterki dostaniesz jako listę do decyzji.
3. **Tag na Macu (D-24).** Ta sesja nie może wypychać tagów na GitHuba (dostaje 403), więc tag `baseline-01-szablon` musi powstać i zostać wypchnięty na Macu. Tam też czeka jeszcze `baseline-00-przed-en`.

Szablon nie dostaje kamienia milowego w `plan.md`. Ten plik ma zostać pustym wzorem dla nowych projektów, więc tag zaznacza po prostu wersję szablonu.

## Q-01: strona ISO

Opublikowane strony „ISO 29110 a nasz model śladu” i „Model śledzalności człowiek + agent” pokazują stan sprzed D-08…D-21. Mają polskie kody i jako braki pokazują rzeczy, które już są zrobione. Po aktualizacji pokrycie wyglądałoby tak:

| Produkt normy | Było | Jest teraz |
| --- | --- | --- |
| WP.10 plan | częściowo | `plan.md` z OBJ, MS, TSK, PRK |
| WP.09 rekord postępu | brak | `progress.md`, ale bez zasobów i kosztów, więc częściowo |
| WP.04 korekty | brak | `corrections.md` |
| WP.23 weryfikacja | częściowo | `verification.md` i hooki |
| WP.22 walidacja | brak | `validation.md` |
| WP.01 akceptacja | brak | `acceptance.md` |
| WP.12 kopia zapasowa | brak | GitHub |

Kopia na GitHubie została już raz sprawdzona w praktyce. Kopia w chmurze powstała przez `git clone` z GitHuba, a jej stan plików był identyczny z Twoim Makiem. Norma nazywa taki stan „recovered”.

Jak ją odświeżyć (D-25)? Ręczna poprawka znowu się zestarzeje przy następnej zmianie modelu. Proponuję generować stronę w repozytorium z pól `iso` w `id.toml`, tak jak `trace.md`, i sprawdzać ją w pre-commit. Wtedy nie może się rozjechać z modelem. Opublikowaną stronę odświeżałbym z tej wersji.

---

**Wykonane**
- Pytania od D-22 do D-25 zapisane w rejestrze jako otwarte decyzje (commit `a4f755f`, wypchnięty na GitHuba).

**Decyzje**
1. **D-22 Historia szablonu w nowym projekcie:**
   - **A)** `make new-project` przenosi ją do `archive/template/`
   - **B)** instrukcja w README, czyszczenie ręczne
   - **C)** bez zmian

   Propozycja: **A**.
2. **D-23 Przegląd przed baseline:**
   - **A)** przegląd przez osobnego agenta, usterki jako lista do decyzji
   - **B)** bez przeglądu

   Propozycja: **A**.
3. **D-24 Tag:**
   - **A)** `baseline-01-szablon` po D-22 i D-23, tworzony i wypychany na Macu
   - **B)** inna nazwa

   Propozycja: **A**.
4. **D-25 Strona ISO:**
   - **A)** generowana w repozytorium z `id.toml` i sprawdzana przez pre-commit
   - **B)** ręczna aktualizacja obu stron
   - **C)** ręcznie tylko strona ISO, a „Model śledzalności” do archiwum

   Propozycja: **A**.

**W kolejce**
- Q-02: przeniesienie zmian do gtd2
- skrypt do modułu model stanów
- K-10…K-13 (rejestr gtd2)

Odpowiedz kodami, np. „D22a D23a D24a D25a”, albo „ok”, jeśli zgadzasz się ze wszystkimi propozycjami.

# USER
wykonaj rzetelnie
1a, 2a, 3a, 4a

# MODEL
Wykonuję w kolejności, w której decyzje od siebie zależą:
1. D-22: polecenie `make new-project`.
2. D-25: strona ISO generowana z `id.toml`.
3. D-23: niezależny przegląd całości.
4. D-24: tag, ale dopiero gdy usterki z przeglądu zostaną rozstrzygnięte i Mac będzie podłączony.

Zakładam listę zadań.

Teraz cel `make new-project` w `Makefile` i scenariusz w teście narzędzi.

Skrypt słusznie odmawia, gdy coś jest niezacommitowane. Sprawdzam, co konkretnie zostało w repozytorium testowym.

Zmiana była już dodana do indeksu, a `checkout --` przywraca plik tylko z indeksu. Przywracam go z HEAD i usuwam wydruk diagnostyczny.

D-22 jest gotowe, test przechodzi. Przechodzę do D-25.

Mam dane wszystkich 23 produktów. Zanim napiszę generator strony, która trafi też do publikacji, ładuję wytyczne projektowania stron.

Wytyczne mówią, że opublikowana strona sama renderuje diagramy Mermaid, więc nie dołączam biblioteki. Tak samo działa mapa w module nawigacji. Teraz tworzę plik z danymi normy.

Oba parsery, `tomllib` i zastępczy dla Pythona 3.10 na Macu, czytają dane tak samo. Teraz dopisuję do `id.toml` naszą ocenę: co mamy częściowo i co jest poza etapem specyfikacji.

Scalenie jest tylko w tym jednym miejscu. Naprawiam pętlę i dodaję obsługę list wielolinijkowych.

Wolę przepisać tę funkcję czysto niż zostawiać sztuczkę z `if True:`.

Test przechodzi i obejmuje teraz drogę, którą idzie Mac. Teraz generator strony, `tools/iso_map.py`.

Wynik się zgadza: 11 produktów mamy, 5 częściowo, 0 brakuje, 7 jest poza etapem, razem 23. Podłączam stronę do `make`, pre-commit, testu i dokumentacji.

Test szukał strzałki w surowej postaci, a w HTML jest zapisana jako `-.-&gt;`. To poprawny zapis, tak samo jak na poprzednich stronach. Poprawiam oczekiwanie w teście.

Strona ISO jest odświeżona pod tym samym adresem. Teraz D-23: niezależny przegląd. Najpierw domykam rejestr, żeby recenzent widział stan końcowy.

Pojawiło się W4: typ Q nie ma pola `status`. Ostrzeżenie zadziałało tak, jak miało. Zamiast dodawać nowe pole bez decyzji, dopisuję tę informację do `notes`.

Wszystko przechodzi. Zostały dwa ostrzeżenia W2, które znikną, gdy commit wymieni D-23 i D-24. Commituję przed przeglądem, żeby recenzent oceniał dokładnie ten stan, który trafi na GitHuba.

Recenzent zgłosił 17 usterek. Zanim przedstawię je jako decyzje, sam sprawdzam najpoważniejsze, bo raport agenta to tylko materiał do weryfikacji.

D-22 i D-25 są wdrożone, a niezależny przegląd (D-23) znalazł 17 usterek, z czego 6 to prawdziwe błędy. Tag baseline (D-24) czeka, aż je rozstrzygniesz, i na Twojego Maca. Całość jest na GitHubie w commicie `d5421df`.

**Co zrobiłem**
- **D-22, `make new-project`.**
  - Przenosi rejestr szablonu, `trace.md` i `progress.md` do `archive/template/` i zakłada nowy rejestr z D-01 „Start projektu”, żeby pierwszy commit miał ID.
  - Odmawia, gdy są niezacommitowane zmiany albo projekt był już założony.
  - Test na kopii całego szablonu znalazł usterkę: pliki artefaktów powoływały się na nasze decyzje (np. D-11, D-13), więc pierwszy commit nowego projektu by nie przeszedł. Usunąłem te odwołania. Uzasadnienia są w zarchiwizowanym rejestrze.
- **D-25, strona ISO.**
  - Dane normy (23 produkty, 84 zależności) są w `tools/iso29110.toml`, a nasza ocena w `id.toml`.
  - `tools/iso_map.py` generuje z nich `iso-map.html`, a pre-commit pilnuje, żeby strona była aktualna.
  - Wynik: 11 produktów mamy, 5 częściowo, 0 brakuje, 7 jest poza etapem specyfikacji.
  - Odświeżyłem opublikowaną stronę pod tym samym adresem. Ma teraz też sekcję „Model śladu”, więc stara strona „Model śledzalności” jest nieaktualna.
- **Poprawka mojego błędu z D-20.** Zmiana nazw scaliła dwie zmienne w parserze TOML, którego używa Python 3.10 na Twoim Macu. Parser czytał poprawnie, ale komunikaty o błędach nie podawały numeru linii. Naprawiłem to i dopisałem do parsera obsługę list rozpisanych na kilka linii. Test porównuje go teraz z `tomllib`.

**Wyniki przeglądu.** Najpoważniejsze sprawdziłem sam:
1. `make test` się psuje, gdy ustawisz własną nazwę systemu, bo przykłady w teście mają na sztywno „System”.
2. Hook commit-msg da się obejść przez `git commit -v`, bo liczy ID z pokazanego diffu.
3. Zwykły tekst blokuje commit: „SHA-256” jest traktowane jak odnośnik, a w „CODE-01” narzędzie widzi ID „E-01”.
4. W pliku testów scenariusz bez tagu nadpisuje dane poprzedniego testu AT.
5. Moduł nawigacji nie zauważa ekranu, który nie ma żadnych przejść.
6. Parser TOML na Macu myli się na nawiasie `]` wewnątrz tekstu w liście.

Do tego jest 11 niespójności i drobiazgów w dokumentacji i nazwach, w tym trzy kolejne polskie nazwy w kodzie, sprzeczne z D-20.

Nowych decyzji nie wpisałem jeszcze do rejestru, żeby nie robić drugiego commita w tej wiadomości. Trafią tam w następnym.

---

**Wykonane**
- D-22 i D-25 wdrożone, test przechodzi, commit `d5421df` jest na GitHubie, strona ISO odświeżona.
- D-23: przegląd przeprowadzony, wyniki wyżej.

**Decyzje**
1. **D-26 Błędy 1–6:**
   - **A)** poprawić wszystkie według propozycji recenzenta, z testem na każdy
   - **B)** tylko wybrane (wskaż numery)

   Propozycja: **A**.
2. **D-27 Niespójności i drobiazgi:**
   - **A)** poprawić wszystkie, w tym brakujące angielskie nazwy w kodzie
   - **B)** tylko wybrane

   Propozycja: **A**.
3. **D-28 Pole wskazuje typ rodzica.** Dziś przypadek użycia może wskazać pozycję Out w polu `scenarios:`. Recenzent proponuje, żeby `id.toml` przypisywał każdemu polu dozwolony typ rodzica, a `scope:` wymagał pozycji In.
   - **A)** wprowadzić tę regułę
   - **B)** zostawić jak jest

   Propozycja: **A**. To zmiana reguły modelu, więc pytam osobno.
4. **D-29 Historia gita w nowym projekcie.** Dziś kopia ze sklonowanego szablonu niesie całą jego historię commitów i tagi baseline, które przy pushu trafiają do nowego repozytorium.
   - **A)** README każe zaczynać od kopii plików bez `.git` (`git init`), a `make new-project` odmawia poza repozytorium
   - **B)** `make new-project` usuwa tagi szablonu (zostaje historia commitów)
   - **C)** zostawić i tylko opisać

   Propozycja: **A**.
5. **D-30 Stara strona „Model śledzalności”.**
   - **A)** usunąć ją, bo zastąpiła ją sekcja na stronie ISO; usunięcia nie da się cofnąć
   - **B)** zostawić

   Propozycja: **B**. Nic nie kosztuje, a nie wymaga usuwania.

**W kolejce**
- D-24 tag `baseline-01-szablon` po D-26…D-29, na Macu
- Q-02 przeniesienie zmian do gtd2
- skrypt do modułu model stanów
- K-10…K-13 (rejestr gtd2)

Odpowiedz kodami, np. „D26a D27a D28a D29a D30b”, albo „ok” dla wszystkich propozycji.

# USER
wszystkie ok, wykonaj rzetelnie w kolejności zależności

# MODEL
Wykonuję wszystkie pięć decyzji: D-26 A, D-27 A, D-28 A, D-29 A i D-30 B (strona zostaje, więc nic do zrobienia). Kolejność ustalam według zależności między poprawkami:
1. **Parser i rozpoznawanie ID** w `model.py` (#6, #3, #15, nazwa z #13). Od nich zależy wszystko inne.
2. **Reguła pole → typ rodzica** (D-28) w `id.toml` i `trace.py`.
3. **Pozostałe błędy:** pliki `.feature` (#4), hook commit-msg (#2), moduł nawigacji (#5).
4. **D-29:** start projektu bez historii gita.
5. **Test narzędzi** (#1) z nowymi przypadkami na każdą poprawkę.
6. **Niespójności w dokumentacji i nazwach** (D-27).
7. **Rejestr, jeden commit, push.**

Hook commit-msg działa. Teraz #5: moduł nawigacji ma liczyć ekrany zadeklarowane w mapie, a nie tylko te, które mają przejścia.

Sierota jest teraz wykrywana przez R1, R2, R3 i R7. Wynik `cmp` był zakłócony, bo `build.py` wypisuje „ok” na to samo wyjście. Porównuję przez plik tymczasowy.

Teraz test narzędzi. Dochodzi poprawka #1 i po jednym przypadku dla każdej usterki, żeby żadna nie wróciła po cichu. Najpierw sprawdzam, gdzie w przykładach jest na sztywno „System”.

Ten blok przepisuję w całości, zamiast przesuwać wcięcia: dochodzi kopia bez historii, odmowa poza repozytorium i ryzyka bez nadpisywania.

Przyczyną jest sam test: dokłada moduł ryzyk, więc musi też odświeżyć pliki generowane przed pierwszym commitem, tak jak użytkownik po wdrożeniu modułu. Przywracam ten krok.

D-27 jest gotowe, test przechodzi, a mapa nawigacji się nie zmieniła. Został rejestr: D-26…D-30 jako rozstrzygnięte. D-24 (tag) dalej czeka na Maca.

Wszystko gotowe do commita. Pięć ostrzeżeń W2 dotyczy nowych decyzji i zniknie, gdy opis commita wymieni każdą z nich osobno.

Commit `cd4611e` jest na GitHubie. Ślad pokazuje 0 błędów i 0 ostrzeżeń. Odświeżam opublikowaną stronę ISO, bo zmieniły się etykiety w sekcji „Model śladu”.

Wszystkie pięć decyzji (D-26…D-30) jest wdrożonych. Zmiany są na GitHubie jako commit `cd4611e`, a ślad pokazuje 0 błędów i 0 ostrzeżeń.

**Co poprawiłem, w kolejności zależności:**
1. **Parsery i rozpoznawanie ID (D-26, D-27).**
   - Parser TOML używany na Twoim Macu (Python 3.10) czyta teraz poprawnie nawias, `#` i `\\` wewnątrz napisów. W testach daje to samo co `tomllib`.
   - ID liczy się tylko jako osobne słowo, więc „SHA-256”, „UC-990” czy „xUC-99” nie są już odnośnikami. Żeby „UTF-16” nie blokował commita, ID wymagań w zwykłym tekście sprawdzam tylko wtedy, gdy ich obszar (np. CAP) już istnieje. To nowa reguła `area_prefix` w `id.toml`.
   - Nagłówek z dwukropkiem po ID (`### UC-02: Tytuł`) dostaje własny, zrozumiały komunikat.
2. **Pole wskazuje typ rodzica (D-28).** Przypadek użycia może wskazać w `scenarios:` tylko scenkę, a w `scope:` tylko pozycję zakresu In. Naruszenie to błąd E7. Strzałki na stronie ISO pokazują teraz te reguły.
3. **Pozostałe błędy:**
   - scenariusz bez tagu nie dopisuje już pól do poprzedniego testu AT;
   - `git commit -v` nie obchodzi już hooka commit-msg;
   - moduł nawigacji widzi ekrany bez żadnych przejść.
4. **Nowy projekt bez historii szablonu (D-29).** README prowadzi teraz przez kopię plików bez `.git`, czyli bez naszych commitów i tagów. `make new-project` odmawia działania poza repozytorium gita.
5. **Dokumentacja i nazwy (D-27).** README i AGENTS.md opisują to, co narzędzia faktycznie robią. Kod nie ma już polskich nazw. `progress.md` nie podaje numerów decyzji szablonu.

**Jak sprawdziłem.**
- **Test wycofania.** Każda poprawka ma własny przypadek w teście. Każdy z nich sprawdziłem, wycofując poprawkę na kopii: test musiał się wtedy wywrócić.
- **Ślepy test.** W ten sposób wyszło, że mój pierwszy test granic ID przechodził także bez poprawki. Zmieniłem tekst testowy i teraz łapie.
- **Własna nazwa systemu.** Test przechodzi też po ustawieniu `system = "GTD"`, czyli w sytuacji, która wcześniej go psuła.

Strona „ISO 29110 a nasz model śladu” jest odświeżona pod tym samym adresem.

**Do zrobienia na Macu.** Gdy będzie podłączony, wykonaj w terminalu:

```
git pull --ff-only
git push origin baseline-00-przed-en
```

Potem mogę założyć tag `baseline-01-szablon` (D-24), albo zrobisz to sam: `make baseline N=01-szablon && git push`.

---

**Wykonane**
- D-26, D-27, D-28, D-29 i D-30 wdrożone, zapisane w rejestrze i wypchnięte (`cd4611e`).
- Strona ISO odświeżona.

**Bez odpowiedzi**
- brak

**Decyzje**
- brak nowych. D-24 jest rozstrzygnięta i czeka tylko na wykonanie na Macu.

**W kolejce**
- D-24: tag `baseline-01-szablon`
- Q-02: przeniesienie zmian do gtd2
- skrypt do modułu model stanów
- K-10…K-13 (rejestr gtd2)

Gdy Mac będzie podłączony, napisz „tag”, a założę baseline. Możesz też wskazać kolejny temat z kolejki.

# USER
Czy pamiętasz naszą rozmowę o
tym żeby wziąć ze standardu wszystko
co nie jest ceromonią? Przeczytaj chapters standardu rozdział po rozdziale
i powiedz jak nam się udało to zaimplementować lub nie i dlaczego?

# MODEL
Pamiętam: z norm braliśmy mechanizmy (ID, ślad dwukierunkowy, kontrolę zmian, bramki), a pomijaliśmy ceremonię dla audytora. Czytam rozdziały normy po kolei i porównuję je z szablonem.

Wstęp, zakres i przegląd są przeczytane. Teraz rozdział 06, proces zarządzania projektem (PM). Czytam cele procesu i wszystkie zadania.

Format zadań jest bardzo rozwlekły. Żeby przeczytać wszystkie zadania wiernie, ale zwięźle, wyciągam z każdego jego identyfikator, treść, uwagi oraz produkty na wejściu i wyjściu.

Rozdział 06 jest przeczytany: 26 zadań PM. Teraz rozdział 07, proces implementacji oprogramowania (SI): cele procesu i zadania.

Teraz rozdział 09, opisy produktów pracy. Wcześniej czytałem tylko część z nich, więc przeglądam wszystkie: co produkt zawiera i jakie ma stany.

Analiza jest gotowa. Pięć luk, które warto domknąć, bo nie są ceremonią, zapisuję w rejestrze jako otwarte decyzje.

Pamiętam tę rozmowę: z norm bierzemy mechanizmy (identyfikatory, ślad dwukierunkowy, kontrolę zmian, bramki i niezależną weryfikację), a pomijamy ceremonię dla audytora. Przeczytałem wszystkie rozdziały i załączniki ISO/IEC 29110-5-1-2, a każde z 72 zadań PM i SI porównałem z szablonem.

**Wniosek:** rdzeń normy jest zaimplementowany. Plan, postęp, ślad, wersje, zmiany i rekordy weryfikacji są w szablonie. Część z nich jest wykonana mocniej niż w normie, bo pilnują jej hooki, a nie ludzie. Znalazłem pięć luk, które nie są ceremonią. Pomijamy dwie rzeczy: to, co należy do etapu kodu, oraz formalności potrzebne zespołowi z osobnym klientem.

## Rozdział po rozdziale

**0–2. Wstęp, zakres, odwołania.**
- Norma jest dla zespołów do 25 osób, dowolnego cyklu życia i oprogramowania, które nie jest krytyczne dla bezpieczeństwa.
- Obiecuje trzy rzeczy: uzgodnione wymagania, widoczność projektu z korektami odchyleń oraz systematyczną implementację.
- Szablon zapewnia wszystkie trzy w swoim zakresie, czyli na etapie specyfikacji.

**3. Terminy.**
- Odwzorowane w `glossary.md` w sekcji „Terminy procesu”.
- „Persona” z normy to nasze scenki (SC).
- Definicja wersjonowania w normie wymaga możliwości powrotu do poprzedniego baseline'u. Mamy to: tag `baseline-00-przed-en` posłużył jako punkt powrotu przed zmianą języka.

**4. Konwencje.**
- Norma ma ID procesów i zadań oraz stany produktów zapisywane w nawiasach `[initiated]`.
- U nas każdy element ma ID, a stany pochodzą wprost z tabeli 12 normy.
- Zapis „baseline = zatwierdzone i umieszczone w repozytorium” odpowiada naszemu stanowi `approved` plus tag.

**5. Przegląd i warunki wejścia.**
- Norma wymaga uzgodnionej umowy, cyklu życia, zespołu i zasobów. Odpowiadają im `scenarios.md`, `scope.md` i sekcje w `plan.md`.
- Tylko częściowo mamy studium wykonalności: jest jedynie sekcja „Produkt i zakres”.
- Cztery linie bazowe ze śladem do źródła (wymagań, specyfikacji, projektu i produktu) robimy tagami. Norma śledzi całe dokumenty, my pojedyncze elementy.

**6. Zarządzanie projektem (PM), 26 zadań.**

| Obszar | Zadania | Stan | Dlaczego |
| --- | --- | --- | --- |
| Plan: cykl, zadania, harmonogram, ryzyka, wersjonowanie | PM.01.01, 03, 07, 09, 10, 12 | jest | `plan.md` z OBJ, MS, TSK, PRK i sekcją wersjonowania |
| Instrukcje dostarczenia | PM.01.02 | częściowo | tylko jedna linia „uzupełnij” w planie |
| Czas trwania, zasoby, pracochłonność, koszt | PM.01.04–06, 08 | pominięte | ceremonia przy jednej osobie; zapisane jako częściowe w `iso-map` |
| Zatwierdzenie planu przez klienta | PM.01.13–14 | zastąpione | klientem jesteś Ty; zmiana celu albo terminu wymaga decyzji D |
| Repozytorium i kopia zapasowa | PM.01.15–16, PM.02.06 | jest | git i GitHub (D-13) |
| Sprawdzenie odtworzenia kopii | PM.02.07 | luka | zrobione raz, ręcznie; nie ma tego w procesie (**D-35**) |
| Monitorowanie i ocena postępu | PM.02.01, PM.03.01 | częściowo | `progress.md` porównuje plan z wykonaniem, bez wysiłku, kosztu i liczby usterek |
| Wnioski o zmianę i ich zatwierdzanie | PM.02.02–03, PM.03.03–04 | jest, ale bez analizy wpływu | decyzje D mają opcje, propozycję i wybór; nic jednak nie mówi, co trzeba przejrzeć po zmianie (**D-32**) |
| Przeglądy i ustalenia | PM.02.04–05 | jest | kontrakt decyzji i rejestr pełnią rolę protokołu spotkań |
| Korekty | PM.03.02 | jest | `corrections.md` ze stanami wprost z normy |
| Zamknięcie i akceptacja | PM.04.01–02 | jest | `acceptance.md` przy kamieniu milowym |

**7. Implementacja (SI), 46 zadań.**
- **Wymagania i ich ślad (SI.02).**
  - Specyfikacja jest w EARS, ze słownikiem i przypadkami użycia. Ślad od umowy do wymagań (SI.02.03) jest automatyczny.
  - Warunek „każde wymaganie identyfikowalne i weryfikowalne” jest sprawdzany przy każdym commicie, mocniej niż w normie.
  - Weryfikacja i walidacja (SI.02.04–05) mają rekordy VER i VAL. Niezależność, której wymaga uwaga 2 przy SI.O7, zapewnia przegląd przez osobnego agenta.
- **Dwie luki w wymaganiach:**
  - **Kryteria przeglądu.** Norma podaje kryteria: wymaganie poprawne, testowalne, kompletne, jednoznaczne i niesprzeczne. Rekord weryfikacji (WP.23) zawiera listę kontrolną. My nie mamy list kontrolnych, więc nie wiadomo, według czego sprawdzano (**D-31**).
  - **Wymagania niefunkcjonalne.** WP.13 wymienia osiem charakterystyk jakości oraz ograniczenia prawne. EARS daje formę zdania, ale nic nie przypomina o wydajności, bezpieczeństwie czy niezawodności (**D-33**).
- **Projekt (SI.03).** Mamy tylko ekrany (moduł nawigacji). Architektura przyjdzie z etapem kodu. Przypadki testowe są (AT, Gherkin), a ślad do nich aktualizuje się sam, choć norma robi to trzy razy ręcznie.
- **Kod, testy jednostkowe i integracyjne, dokumentacja użytkownika, utrzymania i eksploatacji (SI.04–06).** Poza zakresem, to etap kodu. Model jest na nie przygotowany: wystarczy dodać typy z polem `iso`.

**8. Role.** Norma ma siedem ról, a przy jednej osobie wszystkie się łączą. Reguła P-10 mówi, czego agent nie robi bez decyzji. Nigdzie jednak nie jest zapisane, kto w naszym układzie jest klientem, kto analitykiem i kto weryfikatorem (**D-34**).

**9. Produkty pracy.** Mamy 11 z 23, 5 częściowo, 0 brakuje, a 7 to etap kodu. Szczegóły są na stronie „ISO 29110 a nasz model śladu”.

**10. Narzędzia.** git, skrypty Pythona bez zależności i `make`.

**Załączniki.**
- **A, wsparcie po dostarczeniu** (SLA, incydenty): poza zakresem, dotyczy produktu w eksploatacji.
- **B, testy:** plan testów i testy systemowe należą do etapu kodu. Przypadki akceptacyjne już mamy.
- **C, dostępność** (WCAG): nie ma jej. Dla aplikacji z interfejsem, takiej jak GTD, to realny brak. Pokryje go D-33 jako charakterystyka „usability”.
- **D, bezpieczeństwo:** identyfikację ryzyk produktu (SI.02.nSA) robi moduł ryzyk RSK. Wymagań bezpieczeństwa jako kategorii nie ma (też D-33).
- **E, pakiety wdrożeniowe:** szablon sam jest takim pakietem (opisy, formaty, narzędzia, test). Brakuje list kontrolnych (D-31) i przykładów: pliki są puste, a przykłady są tylko w teście.

## Dlaczego tak

To, co jest, to mechanizmy, które da się sprawdzić skryptem albo które wymuszają decyzję. Pominięte pozycje to podpisy, zatwierdzenia między rolami i rachunek kosztów, czyli rzeczy, które przy jednej osobie z agentem tylko dokumentują same siebie.

Pięć luk z decyzji niżej to nie ceremonia. Każda chroni przed konkretnym błędem:
- zmiana rodzica bez przeglądu dzieci;
- weryfikacja bez kryteriów;
- zapomniane wymagania niefunkcjonalne;
- niejasne, kto co zatwierdza;
- kopia zapasowa, której nikt nie odtwarzał.

---

**Wykonane**
- Przeczytane wszystkie rozdziały 0–10 i załączniki A–E, a 72 zadania PM i SI porównane z szablonem.
- Decyzje D-31…D-35 zapisane w rejestrze jako otwarte (commit `e26b824`, wypchnięty na GitHuba).

**Bez odpowiedzi**
- brak

**Decyzje**
1. **D-31 Listy kontrolne przeglądu:**
   - **A)** `checklist.md` z kryteriami dla każdego typu produktu; rekord VER wskazuje listę i wypisuje niespełnione punkty
   - **B)** bez list

   Propozycja: **A**.
2. **D-32 Analiza wpływu zmiany:**
   - **A)** `trace.py` oznacza dzieci elementu zmienionego po ich ostatniej weryfikacji jako podejrzane (nowe ostrzeżenie W5), na podstawie historii gita
   - **B)** bez tej kontroli

   Propozycja: **A**.
3. **D-33 Charakterystyki jakości:**
   - **A)** opcjonalne pole `quality` w wymaganiu i tabela w `trace.md` z charakterystykami, które nie mają żadnego wymagania
   - **B)** bez zmian

   Propozycja: **A**.
4. **D-34 Role normy:**
   - **A)** tabela w AGENTS.md: kto pełni którą rolę (Użytkownik, agent, niezależny agent) i kto co zatwierdza
   - **B)** bez zmian

   Propozycja: **A**.
5. **D-35 Sprawdzenie odtworzenia kopii:**
   - **A)** `make restore-check`: klon z GitHuba do katalogu tymczasowego i porównanie z HEAD oraz z listą tagów, a wynik jako rekord VER
   - **B)** bez zmian

   Propozycja: **A**.

**W kolejce**
- D-24: tag `baseline-01-szablon` (na Macu, najlepiej po D-31…D-35)
- Q-02: przeniesienie zmian do gtd2
- skrypt do modułu model stanów
- K-10…K-13 (rejestr gtd2)

Odpowiedz kodami, np. „D31a D32a D33a D34a D35a”, albo „ok” dla wszystkich propozycji.

# USER
d31 a. d32 a. d33 a.
d34 Jako specjalista od procesów wytwarzania, przemysł jak zorganizować proces z tymi 8 rolami. Jak rozumiem norma wyminia je z jakiegoś powodu. Czy powinien być rozdział rol pomiedzy osobne sesje żeby kompetencje agenta się znie zmieszały w jednej sesji?
d35 a.

# MODEL
Wdrażam D-31, D-32, D-33 i D-35. Na pytanie o role (D-34) odpowiem analizą i propozycją decyzji. Kolejność wynika z zależności:
1. D-33: najprostsze, samo `id.toml` i `trace.py`.
2. D-31: listy kontrolne, z których korzystają rekordy VER.
3. D-35: sprawdzenie kopii zapasowej, które zapisuje rekord VER.
4. D-32: analiza wpływu, która opiera się na rekordach VER.

Listy kontrolne działają w narzędziach. Dopisuję nowe pola do formatów w `verification.md` i `validation.md`.

Wszystkie nowe przypadki łapią swoje usterki. Zostaje dokumentacja: AGENTS.md, README i słownik terminów procesu.

D-31, D-32, D-33 i D-35 są wdrożone. Zmiany są na GitHubie w commicie `2ef9301`, a ślad pokazuje 0 błędów i 0 ostrzeżeń.

**Co doszło:**
- **D-31, listy kontrolne.** Nowy plik `checklist.md` ma listy dla każdego typu produktu. Każdy punkt ma źródło w normie, np. dla wymagań z SI.02.04: poprawne, testowalne, jednoznaczne, niesprzeczne i kompletne. Rekord VER wskazuje użyte listy w polu `checklist:` i niespełnione punkty w polu `failed:`. Wynik `pass` z niespełnionymi punktami to błąd.
- **D-32, analiza wpływu.** Ostrzeżenie W5 pojawia się, gdy element albo jego rodzic zmienił się po ostatniej weryfikacji. Sama zmiana stanu się nie liczy. W5 jest tylko na ekranie, bo zależy od historii gita (to założenie jest w D-39).
- **D-33, charakterystyki jakości.** Wymaganie ma pole `quality:`. `trace.md` pokazuje, które charakterystyki (wydajność, bezpieczeństwo, użyteczność…) nie mają jeszcze żadnego wymagania.
- **D-35, sprawdzenie kopii.** `make restore-check` klonuje repozytorium z GitHuba i porównuje ostatni commit, tagi oraz ślad w klonie. Z `RECORD=1` zapisuje wynik jako rekord VER.
  - Pierwsze uruchomienie na prawdziwej kopii od razu znalazło lukę: w kopii brakuje tagu `baseline-00-przed-en`. To ten tag, którego ta sesja nie może wypchnąć. Po `git push origin baseline-00-przed-en` z Twojego Maca kopia będzie pełna.

Każdy nowy przypadek testu sprawdziłem, wycofując jego poprawkę na kopii. Wszystkie łapią swoją usterkę.

## D-34: role i sesje

**Dlaczego norma wymienia role.** Wymienia ich osiem: siedem w rozdziale 8 (klient, kierownik projektu, lider techniczny, analityk, projektant, programista, zespół) i tester w załączniku B. Nie chodzi o liczbę ludzi. Rozdział 4 wprost pozwala jednej osobie pełnić wiele ról. Role robią w normie dwie rzeczy:
1. Opisują kompetencję potrzebną do zadania. Analityk zna wymagania, projektant architekturę.
2. Rozstrzygają, kto zatwierdza czyją pracę, i to jest ważniejsze.

Przy zadaniach weryfikacji norma konsekwentnie rozdziela autora i zatwierdzającego:
- analityk pisze wymagania, a klient je waliduje (SI.02.05);
- projektant pisze testy, a zatwierdza je analityk (SI.03.08);
- weryfikację wykonuje ktoś niezależny organizacyjnie (uwaga 2 przy SI.O7).

Prawdziwy mechanizm to więc rozdział obowiązków na kilku granicach: potrzeba a rozwiązanie, autor a weryfikator, wykonawca a ten, kto mierzy postęp, oraz to, co jest poprawne, a to, co służy Użytkownikowi.

**Czy rozdzielać role między sesje agenta.** Tak, ale tylko na tych granicach, nie osobno dla każdej z ośmiu ról. U agenta mieszanie ról w jednym kontekście psuje konkretne rzeczy:
- **Sprawdzanie samego siebie.** Sesja, która napisała tekst, czyta to, co miała na myśli, a nie to, co napisała. Mamy na to dowód z tej rozmowy: niezależny recenzent znalazł 17 usterek, które ja przeoczyłem. Także mój błąd w parserze, który sam opisałem jako niemożliwy, złapał dopiero test, a nie moja kontrola.
- **Przeciekanie rozwiązania do wymagań.** Gdy sesja myśli już o ekranach, wymagania zaczynają mówić „jak” zamiast „co”.
- **Testy potwierdzające implementację.** Tester, który widzi kod, pisze testy zgodne z kodem zamiast z wymaganiem.

Osobna sesja na każdą rolę to z kolei ceremonia. Każda zaczyna bez kontekstu i odtwarza go z repozytorium. U nas jest to tanie, bo repozytorium ze śladem jest właśnie nośnikiem przekazania, ale przy ośmiu sesjach koszt przewyższa zysk.

**Proponowany podział (D-36):**

| Kto | Role z normy | Co robi | Czego nie robi |
| --- | --- | --- | --- |
| Ty | klient, decyzje kierownika projektu | walidacja (VAL), akceptacja (ACC), zatwierdzanie wymagań i zmian planu | — |
| sesja autora | analityk, lider techniczny, asystent kierownika, projektant ekranów | pisze specyfikację, plan, rejestr | nie zapisuje VER dla własnej pracy |
| sesja weryfikatora (osobny agent, bez kontekstu rozmowy) | niezależny weryfikator | czyta repozytorium i listy kontrolne, zapisuje VER i propozycje korekt | nie poprawia produktów, które sprawdza |
| etap kodu: osobno programista i tester | projektant, programista, tester | tester pisze testy z wymagań, bez wglądu w kod | — |

Postępu nie mierzy nikt z autorów, bo `progress.md` liczy skrypt. Tak zostaje pokryta granica „wykonawca a mierzący”.

Żeby podział nie był tylko deklaracją, potrzebne są dwa mechanizmy. Oba są osobnymi decyzjami:
- **Karty ról (D-37).** Na start sesji agent czyta kartę ze swoim celem, wejściami, plikami, które wolno mu zmieniać, i listami kontrolnymi.
- **Kontrola w hooku (D-38).** Commit, który dodaje rekord weryfikacji z wynikiem pass, nie może w tym samym commicie zmieniać weryfikowanych elementów. To mechaniczna wersja zasady „autor nie zatwierdza sam siebie”.

---

**Wykonane**
- D-31, D-32, D-33, D-35 wdrożone, przetestowane i wypchnięte (`2ef9301`).
- D-34 rozbita na D-36, D-37 i D-38. Założenia z wdrożenia zapisane w rejestrze jako D-39.

**Bez odpowiedzi**
- brak

**Decyzje**
1. **D-36 Role a sesje:**
   - **A)** Ty, sesja autora, sesja weryfikatora, a na etapie kodu osobno programista i tester
   - **B)** osobna sesja dla każdej roli
   - **C)** jedna sesja, role tylko opisane

   Propozycja: **A**.
2. **D-37 Karty ról:**
   - **A)** katalog `roles/` z kartą dla każdego rodzaju sesji i tabelą ról normy w AGENTS.md
   - **B)** tylko tabela

   Propozycja: **A**.
3. **D-38 Autor nie weryfikuje sam siebie w commicie:**
   - **A)** błąd E9
   - **B)** ostrzeżenie
   - **C)** bez kontroli

   Propozycja: **A**.
4. **D-39 Założenia przy D-31…D-35.** Lista jest w rejestrze; najważniejsze to W5 tylko na ekranie i rekord kopii z `subject: repository`.
   - **A)** przyjąć jak wdrożono
   - **B)** z poprawkami (wskaż które)

   Propozycja: **A**.

**W kolejce**
- D-24: tag `baseline-01-szablon` (na Macu)
- push tagu `baseline-00-przed-en` z Maca
- Q-02: przeniesienie zmian do gtd2
- skrypt do modułu model stanów
- K-10…K-13 (rejestr gtd2)

Odpowiedz kodami, np. „D36a D37a D38a D39a”, albo „ok” dla wszystkich propozycji.

# USER
D36-39 jak na moje rozumowanie są zależne i jak to zwalidujemy? Jak zaplanowac warunki akceptacji? Tam mamy różne kombinacje scenariuszy które trzeba sprawdzić, jak to zrobimy?
Powiedz czy ja przesadzam ?

# MODEL
Przeczytam najpierw, jak D-36…D-39 zapisałem w rejestrze, żeby odpowiedź była oparta na tym, co faktycznie jest do zdecydowania.

Nie przesadzasz z pytaniem, ale przesadziłbyś, gdybyśmy wdrożyli wszystkie cztery decyzje w pełnym zakresie przed jakimkolwiek sprawdzeniem. Dlatego zawęziłem D-36 i D-37 w rejestrze (commit `80e0c41`, wypchnięty na GitHuba). To bardziej moja przesada niż Twoja: zaproponowałem model z ośmioma rolami, zanim przetestowaliśmy choć jeden podział.

## Zależności

- **D-36 jest korzeniem.** Decyduje, czy w ogóle rozdzielamy pracę na sesje.
- **D-37 zależy od D-36.** Karta roli ma sens tylko dla sesji, która naprawdę istnieje.
- **D-38 działa także bez D-36, ale słabiej.** Wymusza, żeby weryfikacja była w osobnym commicie. Nie wymusza jednak, żeby zrobił ją ktoś inny, bo ta sama sesja może zrobić dwa commity. Dlatego bez D-36 dowodzi mniej, niż obiecuje.
- **D-39 jest niezależna.** Dotyczy założeń z już wdrożonych D-31…D-35.

## Jak je sprawdzić

Tu trzeba rozróżnić dwa rodzaje sprawdzania, takie jak w normie (pkt 3.49 i 3.50).

**Weryfikacja: czy zbudowaliśmy to dobrze.** Dotyczy D-38 i D-39 i da się ją zrobić testem automatycznym.

„Różne kombinacje scenariuszy” rozwiązuje się tablicą decyzyjną, a nie sprawdzaniem wszystkich kombinacji. E9 zależy od trzech warunków, co daje 8 kombinacji. Wystarczy pokazać, że każdy warunek sam z siebie zmienia wynik. To technika MC/DC z DO-178C i daje 4 przypadki zamiast 8:

| # | Rekord VER/VAL nowy w commicie | Wynik pass | Weryfikowany element zmieniony w tym commicie | Hook |
| --- | --- | --- | --- | --- |
| 1 | tak | tak | tak | **E9** |
| 2 | tak | tak | nie | przechodzi |
| 3 | tak | nie (fail) | tak | przechodzi |
| 4 | nie (stary rekord) | tak | tak | przechodzi (zmianę po weryfikacji łapie W5) |

Jest też przypadek brzegowy: rekord kopii z `subject: repository` nie ma elementów, więc E9 go nie dotyczy. Każdy przypadek sprawdzę przez wycofanie poprawki, jak przy poprzednich zmianach.

**Walidacja: czy zbudowaliśmy właściwą rzecz.** Dotyczy D-36 i D-37. Żaden test jednostkowy nie powie, czy osobna sesja weryfikatora jest warta swojego kosztu. Można to tylko zmierzyć w użyciu, więc proponuję potraktować D-36 jako hipotezę i sprawdzić ją pilotem na gtd2 przy przenoszeniu zmian (Q-02).

Kryteria akceptacji zapisujemy tak, jak szablon każe to robić: kamień milowy w `plan.md` gtd2 z polem `acceptance_criteria`, a na końcu rekord ACC. Szablon sprawdza wtedy sam siebie. Proponowane kryteria:
1. **Weryfikator znajduje to, czego autor nie widział.** Osobna sesja dostaje tylko repozytorium, kartę i listy kontrolne. Przegląda 10 wymagań, które autor uznał za gotowe, i znajduje co najmniej jedną usterkę, którą potwierdzisz. Jeśli nie znajdzie żadnej, rozdział ról przy tej skali się nie opłaca i wracamy do jednej sesji.
2. **Mało fałszywych alarmów.** Odrzucasz najwyżej 1 na 3 zgłoszenia.
3. **Weryfikator niczego nie poprawia sam.** Zero zmian w plikach produktów z sesji weryfikatora. Pilnuje tego E9 i diff.
4. **Przekazanie jest tanie.** Weryfikator zaczyna pracę bez dopytywania Cię o kontekst, najwyżej dwa pytania. To mierzy, czy repozytorium wystarcza jako nośnik przekazania.

Kryterium 1 jest najważniejsze. Wynik może pokazać, że cała konstrukcja nie jest potrzebna, i to jest dobry wynik.

## Gdzie przesadzaliśmy

Moja poprzednia propozycja zakładała:
- karty dla wszystkich rodzajów sesji;
- sesje programisty i testera, choć kodu jeszcze nie ma.

Zawęziłem to tak:
- na teraz zostaje karta weryfikatora i tabela ról normy;
- sesja autora działa jak dotąd, według AGENTS.md;
- reszta przyjdzie, gdy pilot pokaże, że warto, albo gdy zacznie się etap kodu.

---

**Wykonane**
- D-36 i D-37 zawężone w rejestrze, a do D-38 dopisany plan testu (commit `80e0c41`).

**Decyzje**
1. **D-36 Role a sesje:**
   - **A)** model Ty + sesja autora + sesja weryfikatora jako hipoteza, sprawdzona pilotem na gtd2 według czterech kryteriów wyżej
   - **B)** pełny model od razu
   - **C)** odłożyć

   Propozycja: **A**.
2. **D-37 Karty ról:**
   - **A)** teraz tylko karta weryfikatora i tabela ról normy w AGENTS.md
   - **B)** karty dla wszystkich sesji
   - **C)** tylko tabela

   Propozycja: **A**.
3. **D-38 Autor nie weryfikuje sam siebie w commicie:**
   - **A)** błąd E9, testowany tablicą decyzyjną z 4 przypadkami
   - **B)** ostrzeżenie
   - **C)** bez kontroli

   Propozycja: **A**.
4. **D-39 Założenia przy D-31…D-35:**
   - **A)** przyjąć jak wdrożono
   - **B)** z poprawkami

   Propozycja: **A**.

**W kolejce**
- D-24: tag `baseline-01-szablon` (na Macu)
- push tagu `baseline-00-przed-en` z Maca
- Q-02: przeniesienie zmian do gtd2, a przy nim pilot ról, jeśli przyjmiesz D-36 A
- skrypt do modułu model stanów
- K-10…K-13 (rejestr gtd2)

Odpowiedz kodami, np. „D36a D37a D38a D39a”, albo „ok” dla wszystkich propozycji.

# USER
d36 a. d37 a. d38 a. d39 a.
Pamietaj żeby zapisać nasze pomysły których teraz nie realizujemy a żeby dało się do nich wrócić jak pilot pokaże potrzebę rol.

# MODEL
Wdrażam D-36…D-39 i zgodnie z Twoją prośbą zapisuję pomysły odłożone na później tak, żeby dało się do nich wrócić. Każdy dostaje w rejestrze pozycję kolejki z warunkiem powrotu, a szczegóły ról trafiają do `roles/README.md`. Najpierw D-38, bo D-37 i pilot na niej się opierają.

Wszystkie siedem przypadków przechodzi. Teraz próba wycofania: wyłączam po kolei każdy warunek tablicy i sprawdzam, czy test to zauważa.

Każdy warunek jest pilnowany przez test. Teraz D-37: karta weryfikatora i tabela ról normy w AGENTS.md.

Teraz `roles/README.md`. Opisuje model ról i, zgodnie z Twoją prośbą, każdy odłożony pomysł: na czym polega, dlaczego go nie robimy teraz i kiedy do niego wrócić.

Rejestr jest uporządkowany: 10 tematów w kolejce, każdy odłożony pomysł z warunkiem powrotu. Ostatni pełny test i commit. Pre-commit uruchomi już nową kontrolę E9 na tym samym commicie.

D-36, D-37, D-38 i D-39 są wdrożone. Odłożone pomysły zapisałem tak, żeby dało się do nich wrócić. Commit `f855d51` jest na GitHubie, a ślad pokazuje 0 błędów i 0 ostrzeżeń.

**Co doszło:**
- **D-38, autor nie weryfikuje sam siebie.** Hook odrzuca commit, który dodaje rekord weryfikacji z wynikiem pass i jednocześnie zmienia albo tworzy weryfikowany element (błąd E9). Sama zmiana stanu się nie liczy.
  - Test opiera się na tablicy decyzyjnej, tak jak ustaliliśmy: 4 przypadki MC/DC i 3 przypadki brzegowe.
  - Każdy warunek sprawdziłem, wycofując go na kopii. Test za każdym razem to wyłapał.
- **D-37, karta weryfikatora.** `roles/verifier.md` opisuje, jak uruchomić osobną sesję (gotowa pierwsza wiadomość). Mówi też, co ta sesja czyta, które pliki może zmieniać i czego nie robi: nie poprawia produktów, nie wystawia „pass z zastrzeżeniami”, nie waliduje. W AGENTS.md jest tabela ról normy.
- **D-36, pilot.** Model ról jest zapisany jako hipoteza. Pilot na gtd2 ma cztery kryteria akceptacji: weryfikator znajduje potwierdzoną usterkę, mało fałszywych alarmów, zero zmian w produktach, najwyżej dwa pytania o kontekst.

**Odłożone pomysły.** Każdy ma w rejestrze pozycję kolejki z warunkiem powrotu. Szczegóły czterech pomysłów dotyczących ról są w `roles/README.md`.

| Pozycja | Pomysł | Wróć, gdy |
| --- | --- | --- |
| Q-03 | pilot ról na gtd2 | przy przenoszeniu zmian do gtd2 (Q-02) |
| Q-04 | karta sesji autora | pilot pokaże powtarzalne usterki jednego rodzaju |
| Q-05 | osobne sesje programisty i testera („czarna skrzynka”) | zacznie się etap kodu |
| Q-06 | rola w opisie commita i uprawnienia do plików | weryfikator mimo karty zmieni produkt albo E9 okaże się za słabe |
| Q-07 | pełna tabela ról i odpowiedzialności dla 8 ról | dołączy druga osoba albo zewnętrzny klient |
| Q-08 | pominięte elementy normy (studium wykonalności, instrukcje dostarczenia, koszty, plan testów, wsparcie, przykłady) | pojawi się klient, budżet albo etap kodu |
| Q-09 | skrypt modułu model stanów | gdy będzie potrzebny |
| Q-10 | zaległe czynności na Macu | gdy Mac będzie podłączony |

Q-09 i Q-10 krążyły dotąd tylko w moich wiadomościach, więc dopisałem je do rejestru, żeby nie zginęły.

---

**Wykonane**
- D-36, D-37, D-38, D-39 wdrożone i rozstrzygnięte, D-34 zamknięta, commit `f855d51` wypchnięty.
- Pozycje kolejki Q-03…Q-10 zapisane, każda z warunkiem powrotu.

**Bez odpowiedzi**
- brak

**Decyzje**
- brak nowych

**W kolejce**
- Q-10: na Macu `git pull --ff-only`, push tagu `baseline-00-przed-en`, potem baseline szablonu (D-24) i `make restore-check RECORD=1`
- Q-02 z pilotem Q-03: przeniesienie zmian do gtd2
- Q-04…Q-09: odłożone, z warunkami powrotu

Gdy Mac będzie podłączony, napisz „tag”, a zrobię Q-10. Możesz też zacząć Q-02 z pilotem ról.

# USER
zrob Q10

# MODEL
Robię Q-10. Najpierw sprawdzam, czy Mac jest osiągalny i w jakim stanie jest na nim repozytorium.

Mac jest osiągalny, ale stoi na `911ab4a`. Brakuje mu ośmiu commitów, a tag `baseline-00-przed-en` jest tylko u niego. Najpierw próbuję wypchnąć ten tag z kopii w chmurze, która też go ma.

Push tagu znów został zerwany. Sprawdzam w dokumentacji serwera pośredniczącego, czy blokuje tagi celowo.

Na Pythonie 3.10 wszystko przechodzi, a kopia robocza jest czysta. Zakładam tag `baseline-01-szablon` przez `make baseline`, zgodnie z P-09.

Tag jest założony na Macu (`baseline-01-szablon` na `f855d51`), kopia robocza czysta. Aktualizuję Q-10 w rejestrze, żeby było widać, co jeszcze czeka.

Q-10 jest zrobione w tym zakresie, na który ta sesja pozwala. Zostały dwa polecenia, które musisz wpisać w terminalu na Macu, bo sesja nie może wypychać tagów.

**Co zrobiłem:**
- **Mac zsynchronizowany z GitHubem.** Stał na `911ab4a`, brakowało mu ośmiu commitów. Teraz jest na `f855d51`, a jego drzewo plików jest identyczne z kopią w chmurze.
- **Test na Pythonie 3.10.** Na Macu przeszły pełny test narzędzi i `make check`. To pierwszy przebieg na drodze, którą Mac naprawdę używa (parser zastępczy zamiast `tomllib`). Wcześniej sprawdzałem ją tylko pośrednio.
- **Tag `baseline-01-szablon` założony (D-24)** na `f855d51`, z opisem odsyłającym do D-24.
- **Rejestr zaktualizowany:** w Q-10 zapisałem, co zrobione, a co czeka (commit `563cb47`).

**Czego nie dało się zrobić stąd.** Serwer pośredniczący tej sesji odrzuca push tagów kodem 403. To blokada z zasad, więc jej nie obchodziłem. W kopii na GitHubie wciąż brakuje obu tagów.

**Do wpisania w terminalu na Macu:**

```
cd ~/PycharmProjects/ai-sldc-template
git pull --ff-only
git push origin baseline-00-przed-en baseline-01-szablon
```

Pierwsze polecenie ściąga commit `563cb47` z aktualizacją rejestru. Drugie wysyła oba tagi.

Potem napisz „tagi”. Uruchomię wtedy `make restore-check RECORD=1`. Sprawdzi on, czy kopia na GitHubie ma ten sam commit i oba tagi oraz czy ślad w niej przechodzi. Wynik zapisze jako rekord weryfikacji repozytorium. To ostatni krok Q-10.

---

**Wykonane**
- Q-10: Mac zsynchronizowany, test na Pythonie 3.10 przechodzi, tag `baseline-01-szablon` założony, rejestr zaktualizowany (`563cb47`).

**Bez odpowiedzi**
- brak

**Decyzje**
- brak nowych

**W kolejce**
- Q-10, ostatni krok: po wypchnięciu tagów `make restore-check RECORD=1`
- Q-02 z pilotem Q-03: przeniesienie zmian do gtd2
- Q-04…Q-09: odłożone, z warunkami powrotu

Gdy wypchniesz tagi, napisz „tagi”.

# USER
origin jest inny https://github.com/m1981/iso-template-agent

# MODEL
Sprawdzam, jaki `origin` ma repozytorium na Macu i co zapisaliśmy w rejestrze.

Oba adresy to to samo repozytorium `github.com/m1981/iso-template-agent`, więc nic się nie rozjechało. Różnica jest tylko w sposobie logowania:
- na Macu `origin` jest w wersji SSH (`git@github.com:m1981/iso-template-agent.git`), tak jak ustawiłeś przy D-13;
- moja kopia w chmurze używa wersji HTTPS (`https://github.com/m1981/iso-template-agent`).

Jeśli Twój push z Maca nie przeszedł, to najpewniej dlatego, że SSH wymaga klucza dodanego w GitHubie, a HTTPS nie. Wtedy w terminalu na Macu wpisz:

```
cd ~/PycharmProjects/ai-sldc-template
git remote set-url origin https://github.com/m1981/iso-template-agent
git pull --ff-only
git push origin baseline-00-przed-en baseline-01-szablon
```

Jeśli SSH u Ciebie działa, pomiń drugą linię.

Zmianę adresu zapisałem w rejestrze jako decyzję D-40 (commit `eb62b73`). Sam jej nie wykonałem.

---

**Wykonane**
- Sprawdzone: na Macu `origin` to SSH, w kopii w chmurze HTTPS, oba wskazują to samo repozytorium.
- D-40 zapisana w rejestrze jako otwarta (commit `eb62b73`).

**Decyzje**
1. **D-40 Adres origin na Macu:**
   - **A)** przełączyć na HTTPS: zrobię to sam, gdy Mac będzie podłączony, albo wpiszesz polecenie wyżej
   - **B)** zostawić SSH

   Propozycja: **A**, jeśli push przez SSH nie działa, a **B**, jeśli działa.

**W kolejce**
- Q-10, ostatni krok: po wypchnięciu tagów `make restore-check RECORD=1`
- Q-02 z pilotem Q-03: przeniesienie zmian do gtd2

Odpowiedz „D40a” albo „D40b”. Po wypchnięciu tagów napisz „tagi”.



