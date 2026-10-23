# Przykładowy plan weryfikacji i walidacji

Status: **demonstracyjny, niewykonany**, wersja 0.1. Projekt: [Release Ledger](project-plan.md). Treści testowe inspirowane informacyjnym B.11; podział dokumentu i progi są naszą propozycją, nie wymaganiem normy.

## 1. Cel, przedmiot i zakres

Weryfikacja: czy wymagania, relacje, kod i dowody spełniają zdefiniowane reguły. Walidacja: czy opiekun potrafi użyć raportu i podjąć prawidłową decyzję o wydaniu. Przedmiot: kandydat CLI, jego manifest, dokumentacja i procedura migracji. Numer wersji kandydata zostanie zapisany po jego utworzeniu; obecnie nie istnieje.

Objęte ryzyka: pominięte wymaganie, fałszywie aktualny pass, zmiana wejść podczas dopuszczenia wydania, utrata danych migracji. Poza zakresem: złośliwy administrator, kryptograficzna autentyczność dowodów, usługi sieciowe, wydajność dla milionów elementów. Zmiana profilu ryzyka wymaga aktualizacji planu.

## 2. Strategia i metody

| Obszar | Poziom / technika | Kryterium i wynik |
|---|---|---|
| Wymagania i plan | Przegląd przykładów i przypadków brzegowych | Jednoznaczne pojęcia, jawne wyłączenia, zadania i kryteria dla zakresu |
| Parser i relacje | Testy jednostkowe: klasy równoważności i granice | Poprawne, puste, zdublowane i nieznane ID dają uzgodniony wynik |
| Decyzja o wydaniu | Tablica decyzyjna | Brak dowodu, fail, nieaktualny dowód, brak zgody i poprawny komplet |
| Współpraca CLI, plików i polityki | Testy integracyjne | Rzeczywiste pliki, kody wyjścia, awarie odczytu/zapisu, brak częściowego manifestu |
| Wyścig sprawdzenie–publikacja | Test z kontrolowaną barierą między krokami | Zmiana wejścia w tym oknie powoduje odmowę albo wydanie dokładnie zamrożonego sprawdzonego snapshotu |
| Migracja | Test systemowy na kopii i wstrzyknięcie awarii | Oryginał bez zmian; po wznowieniu brak ubytku i duplikacji |
| Przydatność raportu | Demonstracja dla OWN | Odbiorca rozpoznaje powód blokady w trzech przygotowanych przypadkach i wskazuje działanie |
| Model formalny | Opcjonalny pilot Alloy/TLA+ | Własności i kontrprzykłady; osobny raport, nie zastępstwo testów kodu |

Próg demonstracji to świadomie mała próbka edukacyjna. Nie daje statystycznej miary użyteczności całego produktu.

## 3. Dane, środowisko i wyrocznie

Dane syntetyczne: poprawny projekt, wymaganie bez zadania, bez testu, nieznane ID, duplikat, pusty zakres, różne rewizje, archiwalny pass, częściowy zapis migracji. Oczekiwane wyniki zapisujemy przed implementacją, na podstawie wymagań, a nie przez skopiowanie aktualnego raportu programu.

Środowisko: przypięta wersja Pythona i zależności, lokalny system plików, tymczasowe katalogi, brak prawdziwych danych. Przed odbiorem drugie czyste środowisko. Raport zapisuje wersję OS, interpretera, zależności, commit i skróty zmiennych wejść. Testy czasu i kolejności używają kontrolowanych zdarzeń, nie arbitralnych sleep.

## 4. Harmonogram i obsada

Testy jednostkowe i integracyjne powstają w T/2 i T/3; nie dodajemy drugi raz ich kosztu do planu. T/4: 8 h DEV na integrację, awarie i raport; REV 2 h i OWN 1 h na ocenę. T/5 obejmuje próbę instalacji i migracji z REV 2 h. T/6 obejmuje poprawki, ponowne wykonanie dotkniętych testów i końcową decyzję OWN. Szczegółowe daty i cała dostępność są w planie projektu.

DEV wykonuje testy i przygotowuje dowody. REV ocenia kompletność i interpretację. OWN waliduje przydatność i podejmuje decyzję odbiorczą. Oddzielny commit nie jest dowodem niezależnej tożsamości recenzenta.

## 5. Wejście, zatrzymanie i zakończenie

Wejście do sprawdzania kandydata: znany zakres, wersje, środowisko i kryteria. Testy wcześniejsze mogą działać na niepełnym przyroście z odpowiednim oznaczeniem.

Przerwać ocenę gotowości przy uszkodzonym środowisku, niekompletnym odczycie, nieznanym zakresie albo naruszeniu integralności danych. Zapisać błąd i wznowić po naprawie; nie oznaczać niewykonanych testów jako pass.

Zakończenie: wszystkie wymagane przypadki wykonane na kandydacie, wyniki aktualne, brak otwartych usterek blokujących, odstępstwa ocenione przez upoważnioną rolę, raport i instrukcja gotowe. Brak wyniku jest luką. Sam zielony runner nie jest odbiorem.

## 6. Dowody, miary i obsługa usterek

Dowód: polecenie, czas, wersje, zakres, wynik, log i identyfikator wejść. Oddzielać wynik scenariusza od statusu wymagania i akceptacji. Zmiana kodu, testów, wymagań lub konfiguracji uruchamia analizę wpływu i ponowne sprawdzenie zależnych dowodów.

Miary: wykonane / planowane przypadki, nieobjęte wymagania, potwierdzone usterki według skutku, czas testów, czas analizy, liczba nieaktualnych dowodów. Pokrycie kodu można dodać po ustaleniu zakresu; nie przyjmujemy arbitralnie progu 100%.

Usterka zawiera kroki odtworzenia, oczekiwany i rzeczywisty wynik, wersję, skutek, właściciela oraz test regresyjny. Utrata danych i fałszywe dopuszczenie wydania blokują dostawę w tym przykładzie. Wynik końcowy i akceptacja: **niewykonane**.
