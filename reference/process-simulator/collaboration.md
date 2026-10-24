# Kontrakt współpracy przy symulatorze

Obowiązuje od 2026-10-23. Operacyjny zapis kontraktu przekazanego przez Użytkownika w rozmowie o pierwszym przyroście (D-78). Instrukcja Użytkownika ma pierwszeństwo przed sprzecznymi lokalnymi zasadami komunikacji. Nie zmieniamy kontraktu dystrybuowanego w pakiecie procesu.

## Zamiar i delegowanie

Użytkownik wyznacza cel i granice, agent dobiera środki w zatwierdzonym zakresie i wykonuje pracę do końca. Istotne nieoczywiste wybory zapisuje jako decyzje agenta: data, co wybrano, jednozdaniowe uzasadnienie. Użytkownik może je później podważyć. Propozycja planu nie jest zaakceptowaną decyzją.

Do Użytkownika trafiają wyłącznie: zmiana zaakceptowanego ustalenia; odstępstwo od przyjętego wzorca; luka lub sprzeczność w dokumentach zamiaru; działanie nieodwracalne lub zewnętrzne (w tym publikacja, push, wysyłka, płatność, usunięcie danych, zmiana środowiska albo zależności systemowych); zmiana kolejności lub zakresu; blokada bez znanego obejścia. Niepewność co do granicy zamiaru również wymaga rozstrzygnięcia. Pozostałe szczegóły rozstrzyga agent.

## Komunikacja

Jeden temat na wiadomość. Najpierw 1–3 zdania o wyniku i potrzebie, następnie krótkie „Informacyjnie” z odnośnikami. „Czeka na Ciebie” tylko dla rzeczywistych czynności ręcznych. „Dalej” ma jedną linię. Ostatnia sekcja to „Do decyzji”, wyłącznie gdy potrzebna; bez niej wiadomość kończy się linią „Dalej”. Puste sekcje pomijamy.

Jedna decyzja na wiadomość, maksymalnie trzy dotyczące jednej nierozdzielnej sprawy. Format D1, D2…: konkretna rekomendacja, jedno zdanie dlaczego, jedno zdanie o skutku odmowy, ewentualnie alternatywy w jednej linii. Użytkownik odpowiada np. „D1: tak” lub „D1: nie, wariant B”. Po decyzji nie dopisujemy innych treści. Numery rozmowy mapujemy na trwałe ID rejestru; nie uznajemy milczenia za zgodę.

## Pamięć i zakończenie pracy

Każda sprawa ma właściciela i następny krok. Pozostałe tematy czekają w punkcie wznowienia lub rejestrze pytań. Pełną tabelę pokazujemy tylko na prośbę albo na końcu etapu. Na starcie czytamy dokumenty zamiaru, dziennik decyzji, pytania i punkt wznowienia. Nie zaczynamy od listy pytań, jeśli możliwa jest praca w już ustalonych granicach.

Na końcu aktualizujemy stan, następny krok, sprawy z właścicielami i odnośniki do nowych decyzji agenta. Przed wysłaniem sprawdzamy kompletność propozycji, jeden temat, zgodność z zakresem, umieszczenie decyzji na dole i zapis pozostałych spraw. Szczegóły należą do dokumentów; agent przynosi gotowe rozwiązanie do zatwierdzenia lub odrzucenia.

## Parametry projektu

- Cel zapisany w rozmowie: zrozumienie procesu przez edukacyjny symulator przyrostu, produktów pracy i identyfikatorów.
- Dokumenty zamiaru: [plan](plan.md), [plan techniczny](technical-plan.md), [pierwszy przyrost](increment-01.md). Zakres I1 został zatwierdzony w D-79 dnia 2026-10-24; szczegóły techniczne dobiera agent. Szerszy plan nie oznacza zlecenia wszystkich następnych przyrostów ani S5.
- Wiążące decyzje Użytkownika: [główny rejestr](../../project/decisions.md), w szczególności D-77 i D-78 oraz późniejsze rozstrzygnięcia.
- Dziennik decyzji agenta, pytania i punkt wznowienia: odpowiednie sekcje [rejestru postępu](progress.md).
- Commit wyłącznie na wyraźne żądanie Użytkownika. Zakres symulatora nie obejmuje zmian Kitchen CAD/CAM ani pakietu `template/process/`.

Parametry porządkują istniejące dokumenty; nie ustanawiają nowych zgód na wykonanie.
