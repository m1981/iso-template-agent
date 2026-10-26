# Mechaniczne wsparcie procesu — przegląd sesji

Data: 2026-10-24. Status: ocena i propozycje, nie wdrożenie nowych reguł.

Podstawa: rozmowa, trwałe zapisy przebiegu i odczyt aktualnych narzędzi. W tej ocenie nie uruchamiano ponownie testów produktu; przywołane wyniki pochodzą z zapisanych wcześniejszych wykonań. To ocena naszego rozwiązania, nie interpretacja wymagań normy ani potwierdzenie zgodności.

## Wniosek

Mamy działające kontrole struktury dokumentacji i części dowodów oraz mechanicznie sterowaną lekcję. Nie mamy jeszcze mechanicznie prowadzonego codziennego procesu Kitchen CAD/CAM. Punkt wznowienia i kontrakt pomagają pamięci, lecz ich przeczytanie, aktualizowanie i stosowanie nadal zależy od agenta. Nie można obiecać wyeliminowania błędów człowieka i agenta; można uniemożliwić konkretne błędne operacje i ujawniać konkretne braki.

## Co pokazała sesja

1. Recenzja szablonu wykazała dwa defekty narzędzi: raport uznawał wynik za pozytywny mimo niezerowego kodu runnera, a hook ukrywał ostrzeżenie W5. Naprawy mają dowody RED/GREEN w [raporcie TDD](tdd/control-results/report.txt). To rzeczywista poprawa kontroli, nie deklaracja procesu.
2. Powstał symulator, testy i [dowody wykonania](process-simulator/evidence/README.md). Usunięcie warunku przeglądu wykrył test mutacyjny; próba przeglądarkowa ujawniła błędny komunikat odbioru przy wyczerpaniu limitu. Sam zielony zestaw wcześniejszych testów nie wystarczył.
3. Użytkownik przeszedł odbiór w fikcyjnej lekcji. Nie stanowi to odbioru symulatora ani produktu Kitchen. Scenariusze zmiany wymagania i następnego wydania nie zostały zaimplementowane.
4. Po utracie procesu serwera zniknął stan lekcji. Odtworzono tylko trzy potwierdzone czynności z rozmowy; to rekonstrukcja, nie odzyskanie oryginalnych danych. [Zapis incydentu](process-simulator/progress.md), sekcja „Incydent podczas próby”.
5. Użytkownik musiał zgłosić rozmycie celu. D-81 uporządkowała kierunek, ale nie zrobił tego mechanizm kontrolny. [Minimalny proces Kitchen](KITCHEN-MINIMAL-PROCESS.md) jest opisem do pilota; nie dowodzi wdrożenia w Kitchen.

## Pięć najważniejszych ustaleń

| Kategoria i problem | Mechanizm i dowód | Granica ochrony / skutek | Najmniejsza odpowiedź |
| --- | --- | --- | --- |
| **Brak: kontrola śladu nie obejmuje całej pracy** | [id.toml](../template/process/tools/id.toml) określa kontrolowane typy i pliki; [check_refs.py](../template/process/tools/check_refs.py) pomija `reference/`. | Kontrola szablonu nie obejmuje automatycznie treści planu symulatora ani proponowanych widoków Kitchen. Poprawne ID i EARS nie dowodzą sensu wymagania. | Przy wyniku kontroli wskazywać jej zakres; po rozpoznaniu Kitchen przypisać istniejące źródła do jednego przyrostu, bez kopiowania wszystkiego do nowego rejestru. |
| **Brak: realna kolejność pracy nie jest egzekwowana jak w lekcji** | [engine.py](process-simulator/app/engine.py), `reason` i `current_run`, blokuje niedozwolone przejścia fikcyjnej lekcji. [pre-commit](../template/process/hooks/pre-commit) kontroluje migawkę indeksu. | Hook uruchamia się przy commicie, nie przed rozpoczęciem implementacji. Nie potwierdza chronologii TDD ani rzeczywistego wykonania przeglądu. | Dla pilota przygotować jawny wynik kontroli gotowości oparty na istniejących danych; nie nazywać go egzekwowaniem całego procesu. |
| **Brak: ograniczona kontrola aktualności dowodów** | [trace.py](../template/process/tools/trace.py), `impact`, porównuje element i jego bezpośrednich rodziców z commitem dodającym VER. Bez historii Git lub przy niezacommitowanym rekordzie nie ma takiej kontroli. [test_report.py](../template/process/tools/test_report.py) respektuje kod runnera. | W5 nie bada całego wpływu zmiany kodu i środowiska. Raport wskazuje HEAD oraz obecność niezacommitowanych zmian, bez dokładnej identyfikacji ich zawartości. | W5 pozostaje ostrzeżeniem. Przed odbiorem pilota ponownie wykonać odpowiednie sprawdzenia i jawnie nazwać ograniczenia dowodu. Manifesty wejść pozostają poza zakresem. |
| **Brak: rozdzielenie commitów nie zapewnia niezależnego osądu ani zgody** | [check_separation.py](../template/process/tools/check_separation.py), `violations`, odrzuca nowy VER/VAL pass razem ze zmianą ocenianego elementu. | Ten sam agent może utworzyć dwa commity. Kontrola nie identyfikuje osoby; nie obejmuje ACC. Tekst `resolved` lub `accepted` nie uwierzytelnia decyzji człowieka. | Opisywać E9 jako rozdzielenie zmian. Dla istotnych reguł domenowych stosować oczekiwane wyniki z niezależnie uzasadnionej podstawy; rzeczywiste decyzje nadal przypisywać do wypowiedzi użytkownika. Nie wdrażać teraz mechanizmu zgód. |
| **Brak: ciągłość wymaga pamiętania o zapisie i właściwym kontekście** | [server.py](process-simulator/app/server.py), `SessionStore`, utrzymuje stan w pamięci; [session.py](process-simulator/app/session.py) sprawdza i odtwarza ręczny eksport. Dziennik postępu utrzymuje agent. | Awaria ujawniła utratę stanu. Dokumenty pozwalają wznowić pracę, ale nie gwarantują, że agent przeczyta aktualny zamiar i nie pominie decyzji. | W procesie Kitchen najpierw sprawdzić wznowienie z repozytorium na jednym przyroście. Automatyczny trwały zapis lekcji rozważyć tylko przed dalszym użyciem symulatora. |

Powyższe braki nie są nowo wykrytymi defektami implementacji. Dwa wcześniej potwierdzone defekty raportowania zostały już naprawione. Nie przypisujemy brakującej funkcji produktu do niespełnionego wymagania, jeśli takiego wymagania nie przyjęto.

## Co można przenieść z pamięci do narzędzi

| Potrzeba / propozycja | Dlaczego obecne mechanizmy nie wystarczają | Dowód działania i koszt | Decyzja operatora |
| --- | --- | --- | --- |
| Jeden widok wznowienia: cel, aktywny przyrost, następny krok, blokery i decyzje | `progress.py` generuje postęp z zadeklarowanych pól; nie wybiera właściwego kontekstu rozmowy. Osobny ręczny dziennik może się rozjechać. | Nowa sesja odtwarza stan z repo bez historii rozmów; mierzymy czas i pominięcia. Koszt: mapowanie istniejących źródeł i mała projekcja, nie drugi komplet danych. | Widoki są już przyjętym kierunkiem D-81; konkretny zakres wdrożenia dopiero po rozpoznaniu Kitchen. |
| Jedno uruchomienie kontroli przyrostu z rozdzieleniem: struktura, testy, kwestie wymagające osądu | Zielone `make check` nie oznacza zielonych testów produktu, a brak runnera oznacza kontrolę ręczną. | Próby negatywne: brak odnośnika, błąd testu, brak wyniku ręcznej oceny dają odrębny, prawdziwy stan. Koszt: podpięcie istniejących poleceń; utrzymanie wraz z modułami. | Nie dodawać nowych obowiązkowych bramek bez ustalenia zakresu pilota. |
| Trwały automatyczny zapis lekcji, jeśli wrócimy do symulatora | Poprawny importer nie odzyska danych, których użytkownik nie wyeksportował. | Restart procesu zachowuje ostatnią zakończoną czynność; uszkodzony zapis nie jest udawanym sukcesem. Koszt: zapis, odczyt, obsługa awarii i testy. | Odłożone; nie jest warunkiem rozpoznania Kitchen. |

## Granica automatyzacji

Narzędzie może sprawdzić obecność źródła, wersję, format, wynik polecenia i zadany warunek przejścia. Nie rozstrzyga automatycznie, czy zakres spełnia potrzebę, czy model CNC opisuje właściwą rzeczywistość, czy przyjąć ryzyko i czy wydać produkt. Testy mogą utrwalić ten sam błąd co implementacja, gdy oczekiwany wynik pochodzi z tego samego błędnego rozumowania. Drugi agent sam w sobie tego nie usuwa.

Lokalne hooki i pola autora to pomoc przeciw pomyłkom, nie kontrola tożsamości ani zabezpieczenie przed celową modyfikacją. Dodatkowy model zagrożeń pozostaje otwarty.

## Kolejność dalszej pracy

1. **Agent: rozpoznać Kitchen.** Rezultat: mapa rzeczywistych modułów, poleceń testów, źródeł wymagań i decyzji. Koniec: każdy proponowany element pilota ma wskazane istniejące źródło lub jawny brak.
2. **Agent: dobrać najmniejszą kontrolę i widok dla proponowanego przyrostu.** Rezultat: propozycja oparta na stwierdzonych brakach. Koniec: wiadomo, co narzędzie wykryje, czego nie wykryje i ile miejsc trzeba utrzymywać; zakres przyrostu trafia do użytkownika.
3. **Po uzgodnieniu zakresu: przeprowadzić przyrost i wznowienie przez nową sesję.** Rezultat: działający wynik, rzeczywiste dowody, obserwacje kosztu procesu. Koniec: użytkownik ocenia wynik, a braki wznowienia są zapisane. Zbieramy czas wznowienia, pominięte decyzje, nieaktualne dowody i czas utrzymania dokumentacji; progów nie wymyślamy przed pomiarem.

Nie zmieniono narzędzi, reguł szablonu ani Kitchen CAD/CAM w ramach tej oceny. Właściciel następnego kroku: agent. Brak nowej decyzji wymaganej do samego rozpoznania.
