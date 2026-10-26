# Nasze podejście — materiał ujawniany dopiero w rundzie 4

Stan odczytany 2026-10-26, po zakończeniu rund 1–3. To opis do krytycznej oceny, nie sugestia oczekiwanej odpowiedzi.

## Cel i zakres

Jeden człowiek i agenci mają dostarczać działające przyrosty bez odtwarzania ustaleń z pamięci i całej historii rozmów. Cel nie obejmuje certyfikacji. Człowiek rozstrzyga zmianę zakresu, przyjęcie ryzyka, odbiór przyrostu i wydanie; agent dobiera technikę w uzgodnionym zakresie. Koszt procesu i zdolność wznowienia mają być sprawdzane w pilocie, bez przyjętych z góry wyników pomiarów.

## Co istnieje w formalizowanym modelu iso-model-state

Obowiązujący model YAML ma wersję 0.7; wykonawca Python stosuje deklarowane stany, role, warunki i skutki do instancji symulacyjnej.

- Produkty: PLAN, REQ, AT (scenariusz akceptacyjny), DES, CODE. Każdy element ma ID, wersję, stan, zależności depends_on, opcjonalnego poprzednika historycznego oraz flagę suspect. PLAN/REQ/AT wymagają zatwierdzenia U; DES/CODE mają inną ścieżkę i mogą być podważone przez U.
- Stany produktów: draft, verified, approved, baselined, deferred, superseded, withdrawn; none oznacza brak elementu. Baseline to operacja U z dowodem demonstracyjnym commit/tag na jego polecenie, nie autonomiczny commit agenta.
- T01 (A) weryfikuje element na podstawie checks_ok, dojrzałych zależności i braku suspect. T02 (U) zatwierdza wymagające tego typy. T04 (U) tworzy baseline. Etykiety A/R/U nie są uwierzytelnianiem rzeczywistej osoby.
- Zmiana zaakceptowanego elementu wymaga wskazanej zgody na konkretny element, wersję i operację; zgoda nie jest używana ponownie. Zmiana oznacza zależne produkty jako suspect. Przegląd bez wpływu może usunąć flagę przy spełnionych warunkach; ocena treści nie jest automatyczna.
- Pytania mają stany i informację blocking; pytanie o zmianę zawiera cel i rozstrzygnięcie. Kolejka ogranicza jednocześnie zadawane pytania. Nie oznacza to rozumienia tekstu użytkownika przez wykonawcę.
- Wydanie przechodzi in_preparation → ready (A, przesłanki zakresu, tests_ok, brak otwartych blokad) → reviewed (R) → accepted (U, bez otwartych blokad). W03/W05 obsługują ustalenia i odmowę. Zmiana po odbiorze nie nadpisuje odebranego wydania: wymaga następnego rekordu, wcześniejsza migawka zostaje.
- W02 ma nadal guard true i nie wymaga rzeczywistego raportu. checks_ok/tests_ok oraz dowody w scenariuszach są danymi wejściowymi symulacji. Ich wartości nie pochodzą automatycznie z testów produktu lub autentycznych decyzji człowieka.

Istnieją WIT1–WIT5, testy warunków, generowane sekwencje Hypothesis oraz próby celowo zepsutych reguł. Nie jest to pełne przeszukanie wszystkich stanów. E3/TLA+/TLC jeszcze nie wykonano. Według STAN dostawa E2 jest gotowa do decyzji użytkownika; nie przedstawiamy jej jako odebranej. Nie wykonywaliśmy teraz ponownie regresji tego repozytorium.

## Co jest obecnie tylko propozycją praktycznego zastosowania

- Mapa projektu: wykonane, pozostałe, zależności, niewiadome, blokady; karta bieżącego przyrostu: cel, granice, wymagania, plan, moduły, kontrole, wyniki i decyzje. Widoki odsyłają do istniejących źródeł zamiast dublować treść.
- Rozdzielenie pojęć zadanie → wykonanie → ocena. Przegląd ma wskazywać konkretny materiał i wersję kryteriów. Sam ID albo pole pass nie wystarcza do potwierdzenia aktualności wyniku.
- Połączenie modelu z repozytorium, które odczytuje raporty, wykrywa brak lub nieaktualność podstawy oceny i pokazuje powód odmowy oraz następny krok. Nie jest zaimplementowanym adapterem. Nie rozstrzygnięto jeszcze formatu wszystkich tych zapisów.
- Osobny recenzent bez historii tworzenia przy wybranych kontrolach. To ograniczenie wpływu autora, nie gwarancja niezależności rozumowania. Osobna recenzja nie zastępuje demonstracji i odbioru człowieka.

W szablonie iso-template-agent działają już m.in. kontrola ID i śladu, generowane raporty, sprawdzenie indeksu przed commitem oraz ostrzeżenie W5 dotyczące zmian po weryfikacji. Są to kontrole określonych własności dokumentacji; nie egzekwują całego powyższego obiegu. W5 pozostaje ostrzeżeniem. Nie wdrażamy obecnie manifestów wejść ani nowego mechanizmu zgód w szablonie.

## Źródła dostępne prowadzącemu

- iso-model-state/model/process.yaml, docs/STAN.md, docs/KARTA-CELU-I-ZAKRESU.md, PLAN.md.
- iso-template-agent/reference/KITCHEN-MINIMAL-PROCESS.md, reference/process-map/worked-transition.md i static-model.md.

Rozmówca nie ma dostępu narzędziowego do tych repozytoriów: ocenia powyższy opis. Gdy szczegółu brakuje, powinien wskazać brak informacji, a nie przypisywać modelowi wymyśloną własność. Pochodzenie i skróty źródeł zapisuje prowadzący osobno.
