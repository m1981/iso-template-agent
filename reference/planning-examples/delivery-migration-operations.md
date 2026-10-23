# Przykładowe plany wydania, migracji i utrzymania

Status wszystkich planów: **demonstracyjne, niewykonane**. Produkt i budżet: [plan projektu](project-plan.md). Trzy plany są w jednym pliku dla czytelności; mają odrębne wyzwalacze i warunki zakończenia.

## A. Plan wydania

**Wyzwalacz:** dostarczenie kandydata 0.1 odbiorcy. **Odpowiedzialni:** DEV przygotowuje, REV sprawdza dowody, OWN decyduje o odbiorze. **Okno:** T/5–T/6, 12–13.11.2026; koszt już ujęty w planie projektu.

Skład: kod i pakiet CLI, przypięte zależności, instrukcja uruchomienia i ograniczeń, specyfikacja zakresu, raport V&V, manifest zawartości z wersjami i skrótami, procedura migracji i odzyskiwania. Wszystkie odnoszą się do jednej identyfikowalnej wersji; nie wystarcza nazwa katalogu „latest”.

Warunki wejścia: testy zakresu przechodzą, dowody aktualne, brak usterek blokujących, przygotowana kopia i czyste środowisko odbioru. Zgoda na wydanie odnosi się do identyfikatora snapshotu, nie do ruchomej gałęzi.

| Krok | Czynność | Sprawdzenie / reakcja |
|---|---|---|
| 1 | Zamrozić wejścia i wygenerować manifest | Skróty kompletne; nieodczytane wejście blokuje |
| 2 | Wykonać kontrolę i przegląd na snapshotcie | Dowód wskazuje te same wejścia |
| 3 | Uzyskać decyzję dotyczącą tego kandydata | Brak zgody pozostaje brakiem zgody |
| 4 | Zbudować pakiet w katalogu tymczasowym | Sprawdzić zawartość; błąd nie narusza poprzedniego wydania |
| 5 | Zainstalować w czystym środowisku i wykonać smoke test | Sukces i diagnostyka błędnego wejścia |
| 6 | Przekazać pakiet i zapisać odbiór | Odbiorca ma instrukcję i identyfikator wersji |

Przy awarii zachować poprzedni pakiet, log i kandydata do diagnozy. Nowe wejścia wymagają nowej oceny. Stare wydanie nadal odnosi się do starego snapshotu; zmiana gałęzi nie unieważnia historycznego faktu jego poprawnego dopuszczenia.

Wynik/odbiór: **brak wykonania**. Plan nie zawiera fikcyjnego podpisu.

## B. Plan migracji danych v1 → v2

**Wyzwalacz:** v2 dodaje do manifestu dowodu identyfikator zestawu wejść. **Granica:** lokalne dane demonstratora, jedna migracja w danym katalogu, bez równoległego zapisu. **Okno:** próba w T/5 przed dostawą. DEV wykonuje, REV porównuje wynik, OWN zezwala na przełączenie po ocenie próby.

Nie wolno dopisywać fikcyjnego identyfikatora do historycznego pass v1. Po migracji taki rekord zachowuje historię, ale ma nieustaloną aktualność i nie dopuszcza nowego wydania. Nowy pass wymaga rzeczywistego wykonania kontroli.

Procedura:

1. Sprawdzić wersję danych i dostępność miejsca, zatrzymać zapis, wykonać kopię i manifest skrótów oryginału.
2. Przetworzyć kopię do nowego katalogu. Nie edytować oryginału w miejscu.
3. Porównać ID, liczbę rekordów i relacje; raportować pominięte lub nierozpoznane dane jako błąd, a nie sukces częściowej migracji.
4. Sprawdzić, że historyczne pass bez wersji wejść nie stają się aktualnym dowodem.
5. Wstrzyknąć przerwanie po części zapisu i przed przełączeniem. Oryginał ma zachować skróty; ponowienie nie tworzy duplikatów.
6. Po pozytywnym raporcie i zgodzie przełączyć wskaźnik aktywnego katalogu. Zachować poprzedni katalog i raport.

Wycofanie: przed dopuszczeniem nowych zapisów przywrócić wskaźnik poprzedniego katalogu i poprzednią wersję programu. Po nowych zapisach nie wykonywać ślepego rollbacku — zatrzymać pracę i przygotować eksport oraz uzgodnione scalenie zmian. RPO=0 dla samej migracji przy spełnionym zakazie zapisu i zweryfikowanej kopii.

Kryterium zakończenia: kompletność i relacje zachowane, oryginał odtwarzalny, brak fałszywej aktualności, raport przejrzany. **Wyniki prób: nie istnieją.**

## C. Plan utrzymania i odtworzenia

**Wyzwalacz:** pierwsze użycie na wartościowych danych. **Właściciel:** OWN; DEV diagnozuje i przygotowuje poprawkę, REV przegląda zmianę wysokiego ryzyka. **Zakres demonstracyjny:** jedna lokalna instalacja, wsparcie w dni robocze, bez SLA całodobowego.

Założenia do pilota: kopia po każdym dniu zmian; cel RPO do 1 dnia roboczego, RTO do 4 godzin od rozpoczęcia odtworzenia. To cele do pomiaru, nie potwierdzone gwarancje. Dla migracji obowiązuje silniejsza reguła kopii bezpośrednio przed operacją.

| Zdarzenie | Działanie | Dowód |
|---|---|---|
| Podejrzenie uszkodzenia danych | Zatrzymać zapisy, zabezpieczyć kopię stanu i log | ID incydentu, skróty, zakres uszkodzenia |
| Odtworzenie | Przywrócić do osobnego katalogu, sprawdzić integralność, dopiero potem przełączyć | Czas, wersja kopii, wynik kontroli |
| Błąd polityki wydania | Wstrzymać nowe wydania, zidentyfikować dotknięte snapshoty | Lista zakresów i test regresyjny |
| Aktualizacja zależności | Powtórzyć dotknięte testy i odbiór kandydata | Nowy manifest i raport |

Budżet po dostawie: proponowane 2 h DEV miesięcznie na próbę odtworzenia i przegląd zależności, tj. 300 PLN przy stawce z planu. Koszt poza budżetem budowy; awarie przekraczające ten limit wymagają osobnego uzgodnienia. W projekcie rzeczywistym trzeba wskazać czas retencji, lokalizację kopii i osobę zastępującą właściciela; demonstrator przyjmuje 30 dni kopii dziennych oraz zachowanie pakietów wydania do zamknięcia pilota. Usunięcie danych podlega odrębnemu uprawnieniu.

Ocena planu po pierwszej próbie: rzeczywisty czas odtworzenia, utracony zakres danych, ręczne kroki i koszt. Nie uzupełniamy tych miar przed wykonaniem.
