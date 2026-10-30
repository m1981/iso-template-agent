# Kryteria odbioru i DoD wykonywalnego modelu procesu

2026-10-29 · D-83 · propozycja kryteriów całej pracy, nie raport ich spełnienia. Zakres opisuje [brief](brief.md), odpowiedzialność — [karta](work-card.md).

**Odczyt po audycie 2026-10-30:** [mapowanie każdego AC](coverage-map.md#85-rozliczenie-naszych-ac-bez-tworzenia-drugiej-specyfikacji) rozdziela odsyłacze do przyjętego DoD od konkretyzacji i proponowanych rozszerzeń. Ten dokument nie jest samodzielną bramką E3. Sformułowania o wymaganym dowodzie i zmianie kryterium niżej opisują proponowany kontrakt odbioru; nie czynią nieprzyjętych AC obowiązkowymi.

## Zasada odbioru

Techniczny DoD oznacza **gotowość do odbioru**. Odbiór wymaga osobnej, rzeczywistej decyzji operatora odnoszącej się do określonej wersji i zakresu. Recenzent może rekomendować odbiór; agent ani zielona bramka nie mogą podjąć go za człowieka.

Kompletność oceniamy względem zatwierdzonego wykazu pojęć, operacji, relacji, własności i scenariuszy. Wyłączenia oraz założenia są jawne. Nie używamy określenia „wszystkie ścieżki” bez podania zakresu przestrzeni stanów i metody badania.

## Warunki techniczne i dowody

| ID | Warunek zakończenia | Dowód wymagany przy zgłoszeniu odbioru |
| --- | --- | --- |
| AC-01 | Granica modelu i kryteria są uzgodnione; każda reguła ma źródło lub jawnie przyjętą interpretację | Wersjonowana mapa zakresu; decyzje o różnicach względem wcześniejszego DoD; lista wyłączeń bez ukrytych braków |
| AC-02 | Każdy typ i relacja w zakresie ma jednoznaczną tożsamość, znaczenie wersji, stany i reguły historii | Słownik/model encji zgodny z wykonawcą; przykłady rewizji, zastąpienia i zachowania wcześniejszego odbioru |
| AC-03 | Każda operacja ma aktora, wejścia, warunki, efekt, odmowę oraz określony skutek niepowodzenia | Kontrakty i testy wykonania/odmowy; brak niezamierzonej częściowej zmiany przy błędzie; wznowienie/ponowienie dla operacji trwałych |
| AC-04 | Zmiana poprawnie wpływa na zależności, gotowość i aktualność dowodów; relacje dają się przejść w obu kierunkach | Testy zmiany i zastąpienia wymagania, naprawy zależności, starego planu i późnego negatywnego wyniku; raport wskazuje konkretny element i powód |
| AC-05 | Badanie struktury i własności rozlicza osiągalność, niedozwolone przejścia, zakleszczenia, niezmienniki i postęp w uzgodnionym zakresie | Wersje wejść/narzędzi, polecenia, granice, założenia sprawiedliwości i wyniki; jawna lista własności jeszcze nieudowodnionych; awaria/timeout nie jest PASS |
| AC-06 | Kontrole są czułe na błędy, a model i wykonawca realizują tę samą semantykę | Oczekiwania ze źródeł i rzeczywistych przypadków; mutacje według przyjętego DoD; porównanie przebiegów modelu i wykonawcy; RED/GREEN/regresja dla zmienionego zachowania |
| AC-07 | Każdy wymagany scenariusz ma sprawdzony wynik i rozliczone odchylenia | WIT1–WIT5 oraz przypadki negatywne z tabeli niżej; trwałe wejścia, historia i wyniki pozwalające powtórzyć próbę bez `/private/tmp` |
| AC-08 | Deklaracja, symulacja, rzeczywiste wykonanie kontroli i decyzja człowieka są rozróżnione | Próba, w której sama flaga sukcesu nie wystarcza w uzgodnionym operacyjnym przekroju; wynik powiązany z badaną wersją; zgoda nieprzenoszona na inny zakres |
| AC-09 | Operator widzi stan, przyczyny blokad, następny dozwolony krok i własną decyzję; nowa sesja odtwarza stan z zapisów | Próba użytkownika i osobna sesja wznowienia: odpowiedzi porównane z historią i oczekiwanym stanem; brak konieczności odtwarzania ustaleń z pamięci operatora |
| AC-10 | Wyniki można odtworzyć, a ustalenia recenzji są rozliczone | Instrukcja uruchomienia, spójna wersja modelu i dowodów, raport osobnego recenzenta; brak otwartej usterki naruszającej przyjęte kryterium |

Nie uznajemy kryterium za spełnione wyłącznie dlatego, że istnieje dokument o odpowiedniej nazwie. Przy każdym AC zapisujemy: spełnione / niespełnione / niebadane, wersję i odnośnik do dowodu. Usunięcie kryterium z zakresu wymaga decyzji, nie wpisu „nie dotyczy” nadanego przez autora. Przyjęcie ryzyka nie zamienia nieudanego testu w udany.

## Minimalny zestaw zachowań do rozliczenia

| Przebieg | Co wynik ma wykazać |
| --- | --- |
| WIT1: od planu do odbioru | Plan przed wykonaniem, wymagane produkty i kontrole, rzeczywista decyzja właściwego aktora w granicy wybranego trybu |
| WIT2: odrzucenie i poprawka | Odmowa z powodem, poprawka i ponowna ocena; brak obejścia blokady |
| WIT3: zastąpienie wymagania | Zależności nie przechodzą bez oceny na nową wersję; naprawa przywraca gotowość |
| WIT4: pytania i decyzje | Brak albo niejednoznaczność odpowiedzi nie staje się zgodą; zakres odpowiedzi jest sprawdzany |
| WIT5: zmiana po odbiorze i następne wydanie | Nowy cykl nie zmienia treści historycznego odbioru i nie dziedziczy go jako zgody na nowy zakres |
| Błąd po zielonym wyniku | Nowy negatywny fakt przed decyzją odbiera gotowość lub wymaga jawnego rozstrzygnięcia według przyjętej reguły |
| Nieaktualny plan / sprzeczny kontekst | System wskazuje wykrywalny konflikt i właściwe źródło; agent nie wybiera arbitralnie wygodnej wersji |
| Przerwanie / błędne polecenie / ponowienie | Brak cichego uszkodzenia stanu i podwojenia decyzji; zapisane zasady odzyskania dla obsługiwanych operacji |
| Zmiana roli lub próba przyjęcia przez autora | Model odmawia niedozwolonej operacji; test symbolicznej roli nie jest dowodem bezpieczeństwa tożsamości |

WIT1–WIT5 już istnieją w `iso-model-state`; najpierw sprawdzamy adekwatność i wykorzystujemy ich dowody. Tabela nie nakazuje odtworzenia scenariuszy w edukacyjnym interfejsie L1. Współbieżność, uwierzytelnianie i awarie sieci dochodzą tylko wtedy, gdy w zakresie znajdzie się obsługująca je implementacja.

## Zgodność z wcześniejszym DoD

[PLAN.md `iso-model-state`](../../../iso-model-state/PLAN.md) zawiera własny DoD. Poniższe mapowanie jest wstępne i nie zmienia jego zobowiązań:

| Istniejące kryteria | Odpowiedniki tutaj |
| --- | --- |
| Zamknięty słownik, źródła/interpretacje, pokrycie celów PM/SI | AC-01, AC-02; zakres pokrycia pozostaje do rozliczenia, nie jest certyfikacją |
| Struktura, bezpieczeństwo S1–S15 (w tym S7a/S7b), żywotność L1–L5 i F1–F3 | AC-03–AC-05; nie pomijamy własności, które są trudniejsze do sprawdzenia |
| TLC, granice i obserwacje; wrażliwość każdej własności na mutację | AC-05, AC-06; nie zastępujemy pełnego zobowiązania kilkoma wygodnymi testami |
| WIT1–WIT5 i odtworzenie rzeczywistych zdarzeń z tego samego modelu | AC-07, AC-08; obecne wyniki mogą być użyte po sprawdzeniu wersji i zakresu |
| Osobna recenzja i odbiór użytkownika | AC-09, AC-10 oraz decyzja końcowa poniżej |

AC-08 i AC-09 wymagają szczególnego porównania z istniejącą próbą operacyjną: część dowodów już powstała, a część właściwości pozostaje abstrakcją modelu. Nie uznajemy ich ani za nowe automatycznie zaakceptowane wymagania, ani za już spełnione.

## Odbiór przez operatora

Pakiet do decyzji zawiera jedną stronę: wersję i zakres, wyniki AC, najważniejsze ograniczenia, ustalenia recenzenta i rekomendację. Szczegółowe logi są podlinkowane, nie przerzucone na operatora do samodzielnej interpretacji.

Operator sprawdza na reprezentatywnym przebiegu, czy potrafi wskazać aktualny stan, podstawę gotowości, konsekwencję zmiany oraz decyzję należącą do niego. Agent przedstawia błędy i ograniczenia, także gdy wszystkie mechaniczne kontrole przeszły. Wynik: przyjęcie określonego zakresu albo odmowa z potrzebną poprawką. Nie zapisujemy odbioru przed odpowiedzią.

Dowód użyteczności może obejmować przeoczone decyzje, nieaktualne dowody, fałszywe alarmy i zbędne wielokrotne wpisy. Zbieramy konkretne zdarzenia podczas próby, bez wymyślania wartości bazowych i progów. Nie wprowadzamy pomiaru czasu pracy, wydajności ani predykcji harmonogramu.

## Zakończenie bieżącego zlecenia dokumentacyjnego

To odrębne, mniejsze kryterium: karta, brief i propozycja DoD są zapisane, wzajemnie powiązane, mają jawny status, źródła, odpowiedzialności i punkt wznowienia; sprawdzono odnośniki i kontrole dokumentów repozytorium. Zakończenie tego zlecenia nie potwierdza spełnienia AC-01–AC-10.
