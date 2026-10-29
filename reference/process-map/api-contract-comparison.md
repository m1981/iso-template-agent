# Porównanie dwóch kontraktów API procesu

2026-10-26. Analiza porównawcza na zlecenie użytkownika. **Wspólne rozumienie architektury, różne scenariusze i poziomy konkretyzacji.** Dokumenty mogą się uzupełniać, ale nie można ich połączyć przez samo przemianowanie operacji. Nie zmieniono żadnego z porównywanych kontraktów ani modelu.

## 1. Materiał i granice porównania

| Oznaczenie | Materiał | Wersja odczytana |
| --- | --- | --- |
| A | [Nasz kontrakt odbioru przyrostu](acceptance-contract.md) | Rewizja 2; SHA-256 `b2df3cba3364ef82e52cb1cb94c64d42a43aaf433f0475769ef0a51a8d6b5390` |
| B | [Kontrakt iso-model-state](../../../iso-model-state/informative/architecture-2026-10-26/process-api-contract.md) | SHA-256 `316081b451820af018db4fd7ded87e0dbd37f3dbfe0c512dd9af040faa6ddd93` |
| BR | [Recenzja B](../../../iso-model-state/informative/architecture-2026-10-26/review.md) | SHA-256 `e4e95fd09141eb7874ed73a36d5e5fefb145a7f6f8bed434e3014d8a64b2a654`; R01–R03 zamknięte w dokumencie |
| BV | [Zapis sprawdzenia projekcji B](../../../iso-model-state/informative/architecture-2026-10-26/verification.json) | SHA-256 `88ff884f48bcbd53f6fad4b28c4a7d0745d03b8c51757d9c10bfa06915ada9e8` |
| M | [Model v0.7](../../../iso-model-state/model/process.yaml) | SHA-256 `2d329822e239555c1642d0a5a20aae0eb28fee17a6f2ff13968e48d7f428fc07`, zgodny z B |

Przeczytano oba kontrakty, recenzję B i zapis wyników BV; sprawdzono odpowiednie przejścia M. Nie uruchamiano ponownie projekcji, testów API ani recenzenta. Jest to ocena autora A, nie niezależna recenzja obu prac. Podane niżej miejsca odnoszą się do sekcji tych wersji.

## 2. Punkty wspólne

Oba kontrakty:

- oddzielają wykonawcę od trwałego systemu kontrolującego przejścia;
- pozostawiają decyzje człowiekowi, a tożsamość ustalają poza polem przesłanym przez agenta;
- wiążą ocenę i decyzję z konkretnym materiałem, zachowują historię i nie przenoszą odbioru na nową treść;
- odróżniają oświadczenie agenta od wyniku narzędzia i od oceny człowieka;
- wymagają kontroli ponowień, konkurencji oraz trwałego zapisu;
- przyznają, że poprawne powiązania, zaufany runner i osobny recenzent nie gwarantują poprawności merytorycznej;
- opisują propozycję, a nie działające API. Zakres zgody na opracowanie nie jest zgodą na implementację.

Podstawa: A §1, §3–7; B §1–4, §6–8. Zgodność nie jest dwoma niezależnymi dowodami skuteczności: oba opracowania wynikają z podobnych ustaleń użytkownika i częściowo wspólnych doświadczeń.

## 3. Najważniejsze różnice

| Temat i kategoria | A | B | Znaczenie praktyczne |
| --- | --- | --- | --- |
| **Różnica zakresu: przedmiot odbioru** | §1 i §4: pojedyncze zgłoszenie odbioru przyrostu; accepted nie pozwala wydać lub wdrożyć. | §1 i §5: zmiana zatwierdzonego r1, propagacja suspect i ponowny odbiór wydania przez W04. | Nie wolno automatycznie uznać `decide accept` za W04. Najpierw określić relację przyrostu, kandydata wydania i wydania. B również nie upoważnia do deploy/publikacji. |
| **Różnica punktu wyjścia: model i uprawnienia** | §6: inspect/submit/decide; wcześniejsze uzgodnienie zakresu poza kontraktem. Nie ustanawia osobnego recenzenta dla każdego przyrostu. | §3–5 i §7: zachowuje aktorów v0.7, listę 16 przejść, przydzielonego R przy W02. T02/T04/T05 należą do U. | B konkretyzuje istniejący model; A opisuje potrzeby jednego fragmentu pracy. Nie można z braku wcześniejszych bramek w A wywnioskować, że A je usuwa. Mapa uprawnień musi poprzedzić implementację wspólnego API. |
| **Propozycja wdrożeniowa: źródło prawdy i izolacja** | §3, §5, Q1/Q3/Q4: wymaga rozdziału i zachowanej podstawy, odkłada wybór magazynów oraz technicznego kanału operatora. | §2, §6, DA05: chroniony serwis, importer, niezmienne manifesty; Markdown może być eksportem, Git ma oddzielnego wykonawcę. | B konkretniej odpowiada, jak wymuszać ochronę, ale przeniesienie autorytatywnego stanu do serwisu jest nową decyzją architektoniczną. Istniejący szablon P-01 wskazuje repozytorium. Trzeba określić właściciela każdej informacji i odtwarzanie, zanim powstaną dwa konkurencyjne rejestry. |
| **Świadomy kompromis: jednostka konfliktu i awarie zewnętrzne** | §7: rewizja istotnego kontekstu zgłoszenia; niezwiązana dokumentacja nie blokuje. Brak operacji Git w tym przejściu. | §6 i §8, DA04: rewizja całego projektu, osobna rewizja operacji i rezerwacja mutacji przy T04; jawne rozliczenie skutku Git po awarii. | B lepiej opracowuje skutek poza bazą. Globalna rezerwacja celowo ogranicza równoległość i może powodować dodatkowe odmowy. To kompromis do pomiaru, nie automatyczny defekt. |
| **Luka do doprecyzowania: nowy wynik przed odbiorem** | §4, §7, S07/S19: mający zastosowanie nowy wynik negatywny blokuje odbiór, nawet gdy kod się nie zmienił. | §6 i §7: napływ dowodu nie zmienia process_revision ani flag; potrzebne jego przyjęcie poleceniem. §5 pkt 9 wymienia przy W04 pytania i tożsamość materiału. | B nie określa dostatecznie, co wymusza uwzględnienie nowego niekorzystnego wyniku przed W04. Potrzebny kontrprzykład z §4 poniżej. To luka opisu adaptera, nie wykazany błąd działającego API. |

Pozostałe różnice nie świadczą o sprzeczności:

- A rozdziela stan zgłoszenia od gotowości i pozwala odrzucić `submitted` również przy `blocked/unknown`. B stosuje W05 z `reviewed` do `in_preparation` oraz tworzy pytanie blokujące. Inny przedmiot i skutki wymagają jawnego mapowania; nie jest to tylko zmiana nazw statusów.
- B rozdziela niezmienne bajty produktu od nowego `AssessmentContext` po zmianie zależności. To przydatne doprecyzowanie obszaru pozostawionego w Q1 naszego kontraktu. Brak wpływu na AT/DES/CODE jest założeniem scenariusza B; nie dowodzi typowego kosztu rzeczywistej zmiany.
- B opisuje 3 czynności operatora realizujące 5 przejść U. A nie analizuje całej zmiany wymagania, więc nie można porównywać tej liczby z jednym odbiorem A ani twierdzić, że A jest pięć razy prostszy. Jawne grupowanie poleceń w B ogranicza liczbę pytań bez oddawania agentowi uprawnień U.
- A dopuszcza przejściowe `IN_PROGRESS` dla równoczesnego retry; B AC35 wymaga identycznego końcowego wyniku. Da się to pogodzić po rozdzieleniu odpowiedzi przejściowej od wyniku końcowego. Przed wyborem transportu trzeba doprecyzować moment odpowiedzi i regułę zapamiętywania odmów.

## 4. Jeden kontrprzykład wymagający wspólnej odpowiedzi

Przypadek porównawczy, nie uruchomiony test:

1. Zaufany runner zwraca wynik pozytywny dla materiału M i właściwego planu; wydanie przechodzi W01/W02.
2. Operator ogląda widok odbioru na rewizji r.
3. Ten sam uprawniony runner dostarcza nowy, mający zastosowanie negatywny wynik dla M i właściwego planu. Może to być ujawnienie niestabilnego testu; materiał nie zmienił się.
4. Według B §6/§7 dowód trafia do magazynu, lecz nie zmienia r ani aktywnych flag. Nikt jeszcze nie przyjął go poleceniem procesowym; nie powstało pytanie blocking.
5. Operator wysyła W04 z widoku r. Materiał i recenzja nadal mają właściwe ID; modelowy guard W04 sprawdza pytania, nie zbiór nowych wyników.

**Nieustalone w B:** czy adapter odmówi, sprawdzając także nowe dowody poza aktywnymi powiązaniami, czy użyje starego pozytywnego zestawu? Ogólne „aktualność dowodów” nie ustala kompletności tego odczytu, a lista AC nie zawiera tego przypadku. Nie twierdzę, że autor zamierza dopuścić odbiór — dwie implementacje mogą różnie zinterpretować opis.

**Minimalna propozycja:** przed W04 adapter uzgadnia wszystkie znane, mające zastosowanie wyniki z wiążącego źródła dla ocenianej podstawy, także jeszcze niepodpięte do procesu. Negatywny lub nierozstrzygnięty konflikt blokuje; nieustalona kompletność daje brak gotowości. Sprawdzenie i zapis decyzji muszą uwzględniać konkurencyjny napływ takiego wyniku. Sposób techniczny należy dobrać do magazynu; nie trzeba automatycznie zwiększać globalnej rewizji od każdego callbacku niezwiązanego z przedmiotem.

Koszt: ustalenie zakresu wyników i ich wersji oraz kontrola przy końcowej decyzji. Ocena efektu: dwa przyszłe scenariusze — nowy wynik dla M blokuje, wynik dla innego materiału nie powoduje fałszywej blokady. Inne plany/środowiska wymagają jawnego rozstrzygnięcia zastosowania. Reguła nie ma magicznie wykrywać niezgłoszonych błędów.

## 5. Co warto zaczerpnąć z każdej pracy

| Z B do dalszego doprecyzowania A | Dlaczego A jeszcze nie wystarcza |
| --- | --- |
| Rozdział treści i aktualnej oceny jej zależności | Q1 pozostawia sposób identyfikacji podstawy otwarty. `AssessmentContext` wyjaśnia, jak ponownie ocenić niezmieniony produkt bez przepisywania historii. |
| Lista zasobów i punktów egzekwowania | Sam zakaz akceptacji przez agenta nie określa izolacji środowiska. B wskazuje też sesję przeglądarki operatora i poświadczenia. |
| Rozliczanie skutku zewnętrznego | Atomowy zapis w bazie nie wystarcza, jeśli następne przejście ma tworzyć bazę Git. Zlecenie, potwierdzenie i uzgodnienie skutku to przydatna podstawa dla tego konkretnego zakresu. |

| Z A do dalszego doprecyzowania B | Dlaczego B jeszcze nie wystarcza |
| --- | --- |
| Jawna kontrola nowego negatywnego wyniku przed odbiorem | Rozdział rewizji i przyjmowania dowodów pozostawia przypadek §4 nierozstrzygnięty. |
| Rozdzielenie gotowości od historycznej decyzji w widoku | B przechowuje historię i proponuje widok, lecz nie opisuje tak wyraźnie prezentacji `unknown` i negatywnych nowych informacji po odbiorze. Nie jest to zarzut nadpisywania historii B. |
| Kryteria oceniane przez operatora i odrzucenie mimo niedostępnego źródła | Zaufane kliknięcie poświadcza decyzję, ale samo nie wskazuje, które oceny należało wykonać. A określa ich powiązanie i scenariusz S14; mapowanie na W04/W05 wymaga doprecyzowania bez cichej zmiany modelu. |

To kandydaci do uzgodnienia, nie automatyczne przeniesienie AX01–AX06 do szablonu. Manifesty i mechanizm zgód nadal nie zostały tu wdrożone.

## 6. Dowody i ograniczenia

A zawiera 23 scenariusze oraz osobny przegląd z dwoma zamkniętymi uwagami. Są to oczekiwania i ocena dokumentu, bez wykonania API.

B zawiera 40 scenariuszy oraz osobną recenzję z trzema zamkniętymi uwagami. BV odnotowuje 41 kroków projekcji na istniejący model i 3 oczekiwane odmowy. BR odnotowuje niezależne powtórzenie poprawnej projekcji, nie trzech prób negatywnych. W tej analizie odczytano te zapisy, nie uruchomiono ich ponownie. Hash modelu jest zgodny z deklarowaną podstawą. Wyniki nie obejmują AX01–AX06 ani testów API.

Mocniejszy ślad do istniejącego wykonawcy w B jest zaletą. Nie dowodzi kompletności adaptera, zabezpieczeń ani przewagi kosztowej. Większa liczba scenariuszy odpowiada też szerszemu zakresowi.

## 7. Rekomendacja i punkt wznowienia

Utrzymać wspólny kierunek, ale przed implementacją przygotować jedną mapę semantyczną: **potrzeba operatora → obiekt decyzji → operacja API → przejście modelu → dowód**. Zacząć od ustalenia, czy odbiór przyrostu A ma być odrębną decyzją od W04, czy przyrost zostanie utożsamiony z kandydatem wydania w konkretnym pilocie. Nie utożsamiać automatycznie żadnego z nich z deploy/CNC.

Następnie rozstrzygnąć przypadek nowego wyniku z §4. Dopiero na tej podstawie proponować zakres przejęcia rozwiązań B dotyczących magazynu, poświadczeń i Git. Nie budować dwóch silników ani sumy wszystkich obowiązków obu dokumentów.

Otwarte sprawy tego porównania mają właściciela **agent**: przygotowanie mapowania odbiorów i doprecyzowanie przypadku nowego dowodu. Decyzja operatora będzie potrzebna, jeśli mapowanie zmieni zakres, odpowiedzialność lub źródło prawdy. Na etapie samej analizy nie prosimy o zatwierdzenie całej architektury. Wcześniejsze Q1–Q4 pozostają w A; D-81 pozostaje kierunkiem pilota Kitchen.

Decyzja agenta, 2026-10-26: zachować porównanie obok własnego kontraktu, bez modyfikacji źródeł B i bez przesyłania wiadomości do jego autora. Powód: polecenie obejmuje analizę, nie uzgadnianie zmian między repozytoriami. Bez commita i pushu.
