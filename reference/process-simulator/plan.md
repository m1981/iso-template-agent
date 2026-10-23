# Plan symulatora edukacyjnego procesu

Data: 2026-10-23. Rewizja: 1. Status: propozycja realizacji.

Użytkownik zlecił utworzenie folderu, zapisanie planu, sposobu wykonania technicznego i rejestru postępów (D-77). Ten zapis nie oznacza jeszcze zamówienia implementacji ani odbioru symulatora.

Symulator ma pomóc operatorowi zrozumieć, jak powstaje przyrost: jakie czynności tworzą produkty pracy, jak wiążą je identyfikatory i na jakiej podstawie można kontynuować pracę. Użytkownik wykonuje kroki i obserwuje konsekwencje, także po błędzie lub zmianie wymagania.

- [Plan techniczny](technical-plan.md) opisuje model, silnik, widoki i sprawdzanie implementacji.
- [Rejestr postępu](progress.md) zawiera bieżący stan, dowody, historię i punkt wznowienia.
- [Pierwszy przyrost](increment-01.md) konkretyzuje proponowany zakres pierwszej działającej lekcji; propozycja do decyzji D-79.
- [Kontrakt współpracy](collaboration.md) utrwala instrukcje Użytkownika przekazane przy omawianiu przyrostu.

## Zakres pierwszej wersji

Jedna lekcja o fikcyjnym przyroście, od potrzeby przez wymagania, plan, projekt rozwiązania, kod i testy do demonstracji oraz odbioru. Proponowany materiał to TextStats z [historii repozytorium](../repository-evolution/README.md): domena jest mała, a istniejące zdjęcia pokazują treści produktów pracy i chronologię planowania. S1 ma ustalić wycinek lekcji i mapowanie jego identyfikatorów; nie zakładamy zgodności identyfikatorów przykładu ze schematem szablonu.

W pierwszej wersji wykonanie prac nad przykładowym produktem będzie symulowane. Kod, test i raport będą miały czytelną treść, lecz kliknięcie „wykonaj test” odtworzy wynik scenariusza, a nie uruchomi dowolny kod. Interfejs i eksport oznaczą te wyniki jako symulowane. Rzeczywiste testy samego symulatora będą miały osobne logi.

To osobna lekcja, nie wybór funkcji pilota Kitchen CAD/CAM. Nie zmieniamy pakietu `template/process/`, zasad W5, manifestów wejść ani mechanizmu zgód projektu. Nie tworzymy systemu zarządzania projektami, harmonogramowania ani sterowania agentami.

## Co użytkownik powinien zrozumieć

| Pytanie edukacyjne | Zachowanie symulatora | Sposób sprawdzenia z użytkownikiem |
| --- | --- | --- |
| Czynność czy produkt pracy? | Krok pokazuje wejścia, działanie i powstałe lub zmienione informacje. | Użytkownik wskazuje różnicę między przeglądem a jego zapisem. |
| Typ produktu czy konkretny element? | Osobno pokazujemy WP.13, plik specyfikacji, ID wymagania i jego rewizję. | Użytkownik znajduje wymaganie i wyjaśnia, czym jest jego ID. |
| Plan czy wykonanie? | Plan poprzedza pracę; zaplanowany test nie daje wyniku. | Użytkownik rozpoznaje brak wykonania mimo istniejącego testu. |
| Co uzasadnia następny krok? | Dostępne działania pokazują spełnione warunki; niedostępne podają konkretną przyczynę. | Użytkownik przewiduje następny krok przed jego odsłonięciem. |
| Co zmienia nowe wymaganie? | Widać nową rewizję, zależności i zakres wcześniejszego wyniku. | Użytkownik wskazuje, czego stary wynik nie potwierdza. |
| Sprawdzenie czy odbiór? | Wynik testu, ocena przydatności i decyzja odbiorcza pozostają osobnymi faktami. | Użytkownik wyjaśnia, dlaczego zielony wynik nie zamyka przyrostu sam. |

## Widoki jednego stanu

1. **Przebieg:** czynności PM/SI, bieżący krok, wykonawca i warunki kontynuacji. To przepływ informacji z możliwością powrotu i poprawki, a nie kaskada dla całego projektu.
2. **Produkty pracy:** graf zależności oraz karta wybranego elementu z treścią, identyfikatorem, rewizją, miejscem zapisu i odniesieniem do normy. Macierz powiązań jest tabelarycznym widokiem tych samych danych.
3. **Historia:** zdarzenia, zmiany treści i relacji, wyniki oraz ich aktualność. Planowane działanie nie pojawia się jako wykonane.

Każdy krok odpowiada na pytania: co się wydarzyło, co powstało, dlaczego jest potrzebne, co można zrobić dalej. Nie pokazujemy od razu całego grafu możliwych stanów; domyślnie widoczny jest fragment dotyczący wybranego przyrostu lub elementu.

## Kolejność realizacji

Identyfikatory S0–S5 dotyczą prac nad symulatorem; nie są identyfikatorami fikcyjnego projektu w lekcji. Statusy utrzymujemy tylko w rejestrze postępu.

| Etap | Zależność | Rezultat | Warunek zakończenia |
| --- | --- | --- | --- |
| S0 Dokumentacja propozycji | Polecenie Użytkownika | Plan, plan techniczny, rejestr | Pliki istnieją, są powiązane, zakres wykonania jest jawny. |
| S1 Scenariusz i reguły | S0; zlecenie realizacji | Jedna lekcja, słownik obiektów, tabela zdarzeń, pochodzenie reguł | Ręcznie rozpisano poprawny przebieg, nieudany test i zmianę po wyniku; każdy krok ma wejście, skutek i wyjaśnienie. |
| S2 Silnik w TDD | S1 | Deterministyczne przejścia, zależności, historia, eksport i odtworzenie | Testy wykrywają celowo wadliwe przejścia; poprawne przebiegi dochodzą do końca; zapis RED/GREEN jest trwały. |
| S3 Przeglądarkowa lekcja | S2 | Trzy widoki, wybór działania, karta produktu, cofanie i nowa gałąź ćwiczenia | Jeden pełny scenariusz działa w przeglądarce; wszystkie widoki odpowiadają temu samemu stanowi; odmowa wyjaśnia przyczynę. |
| S4 Próba edukacyjna i korekty | S3 | Obserwacje operatora, poprawki objaśnień, instrukcja lokalnego uruchomienia | Sprawdzono pytania edukacyjne; zapisano pomyłki i pomoc agenta; Użytkownik ocenił użyteczność. Nierozstrzygnięty odbiór pozostaje otwarty. |
| S5 Opcjonalny eksperyment formalny | S2; wykazana potrzeba | Mały model Alloy albo TLA+/TLC i odtworzony kontrprzykład | Opisano konfigurację, granice analizy i porównanie z silnikiem. Etap można pominąć bez blokowania S3–S4. |

Nie przypisujemy terminów ani procentów ukończenia. Kolejny etap uszczegóławiamy na podstawie wyników poprzedniego; pierwotny plan i przyczyny zmian pozostają w historii.

## Dlaczego te mechanizmy są potrzebne

| Potrzeba | Dlaczego obecne materiały nie wystarczają | Mechanizm i koszt |
| --- | --- | --- |
| Zrozumienie kolejności i konsekwencji | Zdjęcia repo pokazują wybrane momenty, ale nie reagują na wybór użytkownika. | Mały silnik zdarzeń; utrzymujemy tabelę przejść i testy scenariuszy. |
| Zrozumienie relacji bez pamiętania plików | Macierz śladu nie objaśnia powstania każdego elementu. | Graf i karty wyliczane z jednego stanu; koszt opisów dydaktycznych, bez ręcznej kopii grafu. |
| Zrozumienie granic dowodów | Zielony wynik i samo powiązanie ID nie pokazują automatycznie wpływu każdej zmiany. | Jawne rewizje i zakres symulowanego wyniku; koszt kilku reguł aktualności, nie pełnego mechanizmu manifestów. |
| Wznowienie ćwiczenia | Historia rozmowy nie jest trwałym stanem lekcji. | Eksport i import sesji, odtwarzanie zdarzeń; koszt wersjonowania formatu i testu round-trip. |
| Sprawdzenie nietypowych kolejności | Ręczne scenariusze pokrywają tylko wybrane przebiegi. | Najpierw testy silnika; model formalny dopiero przy interakcjach trudnych do ręcznej oceny. Koszt osobnego modelu i jego zgodności z kodem. |

## Próba edukacyjna

Operator przechodzi lekcję, następnie podobny przebieg z wprowadzoną zmianą i wznowieniem zapisanej sesji. Zapisujemy: czas odnalezienia następnego działania, błędne rozpoznania planu/wyniku/odbioru, pominięte zależności, liczbę podpowiedzi agenta i czas utrzymania treści lekcji. Pierwsza próba ustala obserwacje bazowe; kryteria satysfakcjonującego wyniku uzgadniamy przed kolejną. Nie wpisujemy niezmierzonych wartości ani progów sukcesu.

## Źródła i granice interpretacji

- ISO 29110: [§5.1–5.3](../../../iso-29110-5-1/chapters/05-overview.md), [PM i rysunek 3](../../../iso-29110-5-1/chapters/06-project-management-pm-process.md), [SI i rysunek 4](../../../iso-29110-5-1/chapters/07-software-implementation-si-process.md), [rozdział 9](../../../iso-29110-5-1/chapters/09-description-of-work-products.md). Linki zakładają sąsiednie lokalne repozytorium normy.
- [Model ID szablonu](../../template/process/tools/id.toml), [przykłady planów](../planning-examples/README.md), [primer modeli formalnych](../FORMAL-MODELS-REQUIREMENTS-AND-PROCESS.md).

Schemat szablonu stanowi odniesienie, nie kompletny model symulatora. Każda reguła lekcji otrzyma oznaczenie pochodzenia: źródło ISO z sekcją, adaptacja szablonu albo propozycja dydaktyczna. ISO nie nakazuje użycia symulatora, Alloy ani TLA+. Odbiór w fikcyjnej lekcji nie jest odbiorem rzeczywistego produktu.
