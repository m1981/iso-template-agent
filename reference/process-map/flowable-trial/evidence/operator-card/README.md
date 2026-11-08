# A-10 — generowana karta operatora

2026-11-08. Zlecenie U „dalej” po mapowaniu A-09. Kod Java 17 korzysta z istniejących Jackson, WorkflowChecks i Rules. Nie zmieniono modelu danych, BPMN, DMN, reguł procesu ani mechanizmu zgód. Nie wykonano commita.

## Rezultat

`show-card` czyta zapisany eksport, wybiera sprawę i drukuje Markdown. Nie otwiera silnika ani bazy. Zapisy pomocnicze kompilacji i uruchomienia pozostają w ignorowanym `target/`; „tylko do odczytu” dotyczy źródłowego eksportu i procesu, nie zakazu tworzenia plików kompilacji.

Gotowe karty: [korekta testu](05-fail.md), [oczekujący odbiór](07-show.md), [nowa propozycja](10-show.md). Karty są wygenerowane, nie redagowane ręcznie. Na górze podają stan archiwalny, ograniczenie do symulacji oraz rekomendację, niżej zakres, kontrole, odbiór i historię. Komunikat doradczy nie stanowi analizy treści ani polecenia API.

## Sprawdzenia wykonane

| Kryterium z mapy §6 | Dowód i wynik |
|---|---|
| K1: negatywna ocena mimo PASS wykonania | OperatorCardTest.failedReviewIsNotHiddenByPassingRun — PASS; karta wyjaśnia, że PASS nie usuwa zastrzeżenia |
| K2: bieżąca podstawa i oczekujący odbiór | currentBasisWaitsForAcceptanceAndOldFailureRemainsHistory — PASS; rekomendacja dotyczy tylko fabuły, dawny FAIL nie znika |
| K3: poprzedni odbiór a propozycja | nextProposalDoesNotInheritAcceptanceOrChecks, acceptedCaseKeepsExactBasisWithoutRequestingAnotherAcceptance — PASS; zadanie operatora jest oddzielone od doradczej analizy agenta |
| K4: brak, konflikt, nieaktualność | missingPreviousCaseIsExplicit, conflictingResultsCannotRecommendAcceptance, missingCurrentArtifactIsUnknownNotPassed, staleDependencyNeedsNewReviewEvenWithPassRecorded — PASS; nie tworzymy drugiego algorytmu ocen |
| K5: zużyte upoważnienie i referencje | consumedAuthorizationIsNotDescribedAsMissingHistoricalConsent i asercje podstawy w pozostałych testach — PASS |
| K6: odczyt i błędne wejścia | repeatedRenderingDoesNotChangeStateOrInput oraz trzy testy ExportCardTest — PASS; źródła zachowują bajty, wyjście jest powtarzalne, nieznana sprawa/brak pliku/niepełny eksport nie tworzą karty |
| K7: uruchomienie i dowody | Trzy rzeczywiste wywołania show-card, przegląd tekstu wyników przez autora; logi TDD i regresji poniżej. Czytelność dla operatora jeszcze nieoceniona |

**RED:** [red.log](red.log): 10 testów, 10 porażek asercji, 0 błędów wykonania — kompilujący się formatter zwracał pusty tekst. **GREEN:** [green.log](green.log): te same początkowe 10 testów przechodzi. Po oględzinach komunikatów dodano dwie asercje: przyczyna korekty na początku oraz gotowa rekomendacja odbioru zamiast otwartego pytania. [red-recommendation.log](red-recommendation.log): 2 porażki asercji, 0 błędów; następnie poprawiono treść komunikatów.

**Końcowa regresja:** [regression.log](regression.log), `./verify -o verify` — **71 testów, 0 porażek, 0 błędów, 0 pominiętych**: wcześniejsze 58 + 10 testów karty + 3 testy odczytu. Obejmuje testy trwałości w osobnych JVM. Obecne w logu wyjątki wstrzyknięte przez testy nie są błędami zakończenia zestawu. Nie uruchamiano rzeczywistego TextStats.

**Odtworzenie RED na kopii:** [red-replay.log](red-replay.log): końcowe 10 testów formattera ponownie odrzuca pusty wynik; 10 porażek asercji, 0 błędów. [replay-red.py](replay-red.py) zawiera cały stub i procedurę; nie trzeba zachowywać katalogu tymczasowego. Źródła robocze pozostają nietknięte.

Pierwszy wariant skryptu startowego używał `dependency:build-classpath`, ale przypięta wtyczka nie była pobrana do lokalnego cache ([zapis](launcher-offline-failure.log)). To błąd uruchomienia, **nie RED funkcjonalny**. Zastąpiono go już stosowaną w tym repo konwencją jawnej komendy przez Surefire, bez instalowania lub pobierania zależności. OperatorCardCommand nie jest liczony jako test regresji ani potwierdzenie kryteriów.

Nie przeprowadzono niezależnego przeglądu przez subagenta ani odbioru użytkownika. Przegląd autora objął wygenerowane teksty i brak zmian istniejących reguł/modelu/eksportów. Techniczne sprawdzenie nie zastępuje próby użyteczności.

## Odtworzenie

Z katalogu `reference/process-map/flowable-trial/`, z wcześniej przygotowanym środowiskiem `./verify`:

```sh
./verify -o -Dtest=OperatorCardTest,ExportCardTest test
./verify -o verify
python3 evidence/operator-card/replay-red.py
./show-card evidence/f5-restart/05-fail.json first
./show-card evidence/f5-restart/07-show.json first
./show-card evidence/f5-restart/10-show.json next
```

Skrypt odtworzenia używa tymczasowej kopii źródeł i istniejącego cache narzędzi. Karty można zapisać przez przekierowanie standardowego wyjścia; nie nadpisywać nim eksportów wejściowych. Nie należy odpalać kilku buildów jednocześnie w tym samym katalogu target.

**Decyzje agenta:** osobny czysty formatter i adapter eksportu — prostsze testowanie i brak ryzyka zapisów historii przy wyświetlaniu; zachowane techniczne raporty F5 — nie zmieniamy wcześniejszego dowodu; jawny launcher Surefire — wykorzystuje istniejące narzędzia offline. Koszt utrzymania: etykiety, reguły komunikatów doradczych i testy widoku przy zmianie workflow; logika kwalifikacji pozostaje w jednym miejscu.

Mapa pól i kryteria: [A-09/A-10](../../../operator-preview/textstats-card-data-map.md). Aktualny status, wyniki kontroli dokumentacji i dalszy krok: [plan §8.7 i rejestr §8.8](../../../../process-modeling/coverage-map.md). Następna rekomendacja: jedna krótka próba odczytu gotowej karty przez operatora, bez nowej lekcji i bez zmiany procesu.

## Obserwacja operatora i korekta — A-11, 2026-11-08

U po wskazaniu karty napisał: „Nie wiem co zrobic i nie moge odnalezc rekomendacji :(”. **Pierwsza próba nie wykazała użyteczności**: sam raport z instrukcją kolejności czytania nie pozwolił operatorowi odnaleźć rekomendacji i działania. Nie zapisujemy odbioru ani pozytywnej oceny czytelności.

Hipoteza autora: rekomendacja była ukryta w ciągłym akapicie, a zadanie wymagało samodzielnego ułożenia odpowiedzi. Najmniejsza korekta dotyczy tylko prezentacji stanu oczekującego odbioru: osobny nagłówek „Rekomendacja agenta”, wyróżnione zalecenie, gotowa wiadomość do wysłania, powód i alternatywa. Oceny, zakres uprawnień i BPMN pozostają takie same. Samo skopiowanie zdania nie potwierdzi pełnego rozumienia podstawy odbioru.

Test istniejącego stanu 07-show uzupełniono o widoczny nagłówek i gotową wiadomość przed opisem szczegółów. [red-find-recommendation.log](red-find-recommendation.log): 1 porażka asercji, 0 błędów; testy pozostałych stanów przechodzą. Końcowy wynik ponownej regresji w [green-find-recommendation.log](green-find-recommendation.log). Karta 07-show została ponownie wygenerowana po korekcie. Wynik ponownej oceny użytkownika pozostaje otwarty; test tekstu nie jest testem czytelności.


**Odpowiedź po objaśnieniu, 2026-11-08:** U „przyjmuje. Ale powiedz mi czy ISO tez ma taki rodzaj karty lub WP?”. Przyjęcie dotyczy wyniku w ćwiczeniu. Nie wykonano polecenia odbioru w F5 i nie zmieniono eksportów. Próba zakończona z ograniczonym wnioskiem: początkowo raport nie pomógł, po podaniu wyraźnej rekomendacji i gotowej odpowiedzi w rozmowie U podjął decyzję w fabule. Nie ma dowodu ponownego otwarcia karty ani samodzielnego rozumienia. To nie odbiór implementacji czy całego procesu.

**Kontrola przed commitem, 2026-11-08:** asercję obecności sekcji umieszczono przed wycinaniem początku raportu. Dzięki temu pusty formatter nadal powoduje porażkę asercji, a nie wyjątek indeksowania. [precommit-green.log](precommit-green.log): 13/13 testów karty i adaptera; ponowione odtworzenie RED: 10 porażek asercji, 0 błędów w red-replay.log. Kod produktu nie zmienił się od pełnej regresji 71/71 zapisanej w green-find-recommendation.log.
