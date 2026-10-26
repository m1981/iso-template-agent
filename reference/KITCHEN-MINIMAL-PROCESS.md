# Kitchen CAD/CAM — codzienny sposób pracy

2026-10-24. Kierunek przyjęty w [D-81](../project/decisions.md). Opis do sprawdzenia w pilocie; wdrożenie w Kitchen CAD/CAM jeszcze niewykonane.

**Cel:** dostarczać małe, działające przyrosty. Repozytorium ma pozwalać Tobie i nowemu agentowi wznowić pracę bez odtwarzania historii z pamięci.

## Dwa widoki

- **Mapa projektu:** wyniki do dostarczenia, rzeczywisty stan, zależności, niewiadome, blokady i następny możliwy przyrost. Uzupełnia listę tasków o przyczyny kolejności prac.
- **Karta bieżącego przyrostu:** cel, granice, wymagania, plan kroków, dotknięte moduły, sprawdzenia, dowody i decyzje. Rozróżnia „kod napisany”, „sprawdzone” i „odebrane”.

Agent utrzymuje widoki. Wymagania, decyzje i dowody mają wskazane źródła w repozytorium; widoki do nich odsyłają. Stabilne ID łączą informacje bez kopiowania treści. Po rozpoznaniu projektu najpierw wykorzystamy istniejące pliki.

## Jeden obieg przyrostu

| Krok | Odpowiedzialność | Warunek przejścia dalej |
| --- | --- | --- |
| **1. Wznowienie** | Agent czyta instrukcje, mapę, kartę i decyzje; porównuje z kodem i dowodami. | Zna stan i następny krok. Sprzeczności ustaleń wyjaśnia z Tobą. |
| **2. Przed kodem** | Agent opisuje wynik, wymagania, zależności i sprawdzenia. Ty rozstrzygasz brakujące decyzje o zakresie i ryzyku. | Są granice, obserwowalne kryteria i plan poprzedzający wykonanie. |
| **3. Wykonanie** | Agent dobiera rozwiązanie techniczne, wykonuje RED → implementację → GREEN i porządkuje kod. | Kod oraz testy realizują uzgodniony zakres; odstępstwa są jawne. |
| **4. Sprawdzenie** | Narzędzia wykonują testy; agent ocenia wyniki, zapisuje sprawdzone wersje i luki. | Sprawdzono dotknięte kontrakty, jednostki i przepływ między modułami. Oczekiwane wyniki obliczeń uzasadniono niezależnie od badanego kodu. |
| **5. Demonstracja** | Agent dostarcza uruchamialny wynik, instrukcję i ograniczenia. Ty odbierasz przyrost albo wskazujesz korektę. | Jest jawna decyzja dotycząca konkretnego wyniku. Korekta wraca do sprawdzeń; wydanie wymaga osobnej zgody. |
| **6. Koniec sesji** | Agent aktualizuje stan i punkt wznowienia: wykonanie, dowody, następny krok, blokady i właścicieli spraw. | Kolejna sesja ma trwały kontekst. Commit na Twoje wyraźne żądanie. |

**Zmiana:** agent wskazuje wpływ na wymagania, plan, moduły i testy oraz granice ważności wcześniejszych dowodów. Zachowuje historię. Zmiana zaakceptowanych ustaleń, przyjęcie ryzyka oraz wybór techniczny zmieniający koszt lub zobowiązania trafiają do Ciebie. Cisza nie jest zgodą. Kontrola struktury dokumentów nie dowodzi poprawności produktu; drugi agent sam nie zapewnia niezależności oceny.

## Sprawdzenie procesu w praktyce

Po rozpoznaniu modułów wybierzemy jeden pełny przyrost z przekazaniem pracy nowej sesji agenta. Zmierzymy czas wznowienia, przeoczone decyzje, nieaktualne dowody i czas utrzymania dokumentacji. Pierwsza próba dostarczy wartości bazowych; potem uzgodnimy kryteria sukcesu. Koszt procesu to aktualizacja informacji przy zmianie i zamknięciu sesji; zbędne kopie i kontrole bez efektu upraszczamy po ocenie pilota.

**Następny krok — agent:** rozpoznać moduły, źródła ustaleń i uruchomienia przed propozycją funkcji. WIT5/WIT3 i dalsze narzędzia wrócą przy wykazanej potrzebie. Przed rzeczywistą produkcją trzeba ustalić integrację CNC, skutki fizyczne oraz obowiązki dotyczące danych i dostawy. Pilot nie upoważnia do uruchomienia maszyny.

Podstawa: ustalenia Użytkownika i adaptacja [konspektu operacyjnego, §3–4](OPERATIONAL-CONTEXT-AND-PRACTICE-ROLLOUT.md). To propozycja do pilota, nie deklaracja zgodności z normą.
