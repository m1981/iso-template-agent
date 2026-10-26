**Ocena: dokument nadaje się do dyskusji, ale wymaga korekt przed użyciem jako specyfikacja adaptera.** Proponowane warunki wykrywają brak raportu, niewłaściwy materiał i niepełną ocenę. Nie określają jeszcze dostatecznie kontroli nowych blokad ani obowiązującej wersji kryteriów. Jedno zdanie może także blokować poprawny przegląd z uwagami nieblokującymi.

Przegląd wykonano 2026-10-26, tylko przez odczyt. Przeczytano instrukcje repozytorium, `worked-transition.md`, model v0.6, wykonawcę, `tests/test_execution.py`, SI.O7 i WP.23. Dodatkowo odczytano `tests/test_release_findings.py`, aby sprawdzić twierdzenie o W03. Nie czytano `transition-review.md`. Nie uruchamiano testów, nie zmieniano plików ani stanu repozytoriów. To przegląd propozycji, nie formalny VER lub ACC.

1. **Potwierdzony błąd opisu — istniejąca obsługa W03 została przedstawiona jako niedomknięta bez rozróżnienia warstw.**  
   Miejsce: `reference/process-map/worked-transition.md:46` oraz `:107`.

   Kontrprzykład: dla osiągniętego `ready` zdarzenie `W03`, aktor `R`, `findings: ["q1", "q2"]` ma już obsługę w wykonawcy: tworzy pytania blokujące i cofa wydanie do `in_preparation`. Kod rozpoznaje skutek `for each finding` i wykonuje wskazaną regułę tworzenia pytania. Istnieją też testy oczekujące tego zachowania oraz odmowy kolejnego W01 przy otwartych ustaleniach.

   Dowody: `iso-model-state/src/isomodel/execution.py:169`, `:266`; `iso-model-state/tests/test_release_findings.py:28`.

   Minimalne doprecyzowanie: zastąpić ocenę opartą na STAN.md stwierdzeniem: „W03 jest obsługiwane w wykonawcy symulacyjnym; integracja ustaleń z rzeczywistym repozytorium i przebiegiem korekty pozostaje do zaprojektowania”. Nie utożsamiać istnienia tej implementacji z udowodnionym działaniem całej ścieżki naprawy w repozytorium.

2. **Brak specyfikacji — utrzymanie stanu `ready` nie gwarantuje braku nowych blokad.**  
   Miejsce: `reference/process-map/worked-transition.md:73` oraz `:77`.

   Kontrprzykład: W01 ustawia `ready`. Następnie P00 tworzy nowe pytanie z `blocking: true`, niezwiązane z ustaleniami zapisanymi w gotowym raporcie. Materiał i raport pozostają niezmienione. P00 nie cofa stanu wydania; jedyny zadeklarowany obserwator dotyczy zmian po odbiorze. W02 nadal ma warunek `true`. Sprawdzenie aktualnego `ready` i ustaleń samego raportu może więc dopuścić przejście mimo nowej blokady.

   Dowody: `iso-model-state/model/process.yaml:263`, `:353`, `:363`, `:433`; zastosowanie obserwatorów w `src/isomodel/execution.py:494`.

   Minimalne doprecyzowanie: wskazać, czy nowe otwarte pytanie blokujące wyklucza W02. Jeżeli tak, kontrolować aktualny rejestr pytań podczas utrwalania przejścia, a nie wyłącznie raport. Dodać dwie próby: nowe pytanie blokujące po W01 powoduje odmowę; nowe pytanie nieblokujące nie powoduje odmowy.

   Potwierdzona jest luka między znaczeniem `ready` a aktualnością warunków W01. Przepuszczenie przez przyszły adapter pozostaje hipotezą — adapter jeszcze nie istnieje.

3. **Brak specyfikacji — nie ustalono, którą wersję kryteriów porównuje kontrola.**  
   Miejsce: `reference/process-map/worked-transition.md:76` oraz `:132`.

   Kontrprzykład: recenzent ocenił kryterium K1 „czas odpowiedzi poniżej 2 sekund”. Przed W02 treść K1 zmieniono na „poniżej 200 milisekund”, zachowując identyfikator. Materiał wydania nie zmienił się, a raport nadal zawiera ocenę K1. Porównanie samych identyfikatorów nie wykryje nieaktualnej oceny. Odwrotnie, zmiana wyłącznie redakcyjna mogłaby niepotrzebnie wymusić pełny przegląd.

   SI.O7 wymaga oceny według zdefiniowanych kryteriów; WP.23 wskazuje checklistę i wyniki jej pozycji. Źródła te nie wybierają jednak sposobu identyfikacji wersji kryteriów.

   Minimalne doprecyzowanie: zlecenie i wynik wskazują ustaloną wersję treści kryteriów oraz reguł wyniku pozytywnego. Przy zmianie kryteriów określa się wpływ na wcześniejsze oceny; samo zachowanie ID nie wystarcza. Dodać próbę zmiany znaczenia K1 bez zmiany jego ID.

   To potwierdzony brak rozstrzygnięcia w opisie; zachowanie hipotetycznego porównania po ID nie jest wykrytym błędem istniejącego kodu.

4. **Potwierdzony błąd opisu — ogólna odmowa po zgłoszeniu usterek przeczy wcześniejszej regule dopuszczającej ustalenia nieblokujące.**  
   Miejsce: `reference/process-map/worked-transition.md:107`, w zestawieniu z `:57`, `:77` i `:120`.

   Kontrprzykład: recenzent stwierdził drobną usterkę, którą obowiązujące kryteria jawnie dopuszczają przy wyniku pozytywnym. Wszystkie wymagane oceny wykonano, nie ma ustaleń wykluczających pozytywny wynik. Tabela pozwala zakończyć przegląd, ale zdanie „Recenzent zgłosił usterki: nie wykonujemy W02” nakazuje odmowę.

   Minimalne doprecyzowanie: „Recenzent zgłosił ustalenia wykluczające wynik pozytywny: nie wykonujemy W02”. Dodać próbę pozytywnego wyniku z jawnym ustaleniem nieblokującym. Jeżeli zamiarem jest blokowanie przez każdą usterkę, należy zamiast tego ujednolicić wcześniejsze warunki.

**Potwierdzone odczytem:** opis poprawnie oddziela ISO od adaptacji, W02 od odbioru W04, deklarację roli od uwierzytelnienia oraz atomowość w pamięci od trwałego zapisu. W02 rzeczywiście nie wymaga raportu. Testy zawierają odmowę dla aktora A i odmowę W04 przed `reviewed`. WP.23 przedstawia zawartość rekordu jako przykładową, więc dokument słusznie nie przypisuje normie obowiązku konkretnego formatu.

**Granica ustaleń:** nie oceniano jakości rzeczywistej recenzji ani niezależności poznawczej wykonawcy. Różne etykiety ról lub identyfikatory przebiegów nie dowodzą różnych tożsamości. Nie potwierdzono wykonaniem testów zachowania kodu. Ryzyka dotyczące adaptera są kontrprzykładami do specyfikacji, a nie zgłoszeniami błędów wdrożonego mechanizmu.
