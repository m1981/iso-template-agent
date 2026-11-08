# Ograniczona próba TLA+ — P3

2026-11-08 · A-24. Plan próby zapisany przed wykonaniem modelu. Źródło: [mapa P3](../p3-formal-map.md), kontrakt w [worked-transition §11](../worked-transition.md#11-p3--zapis-spóźnionego-wyniku-po-zmianie-podstawy).

## Cel i kryteria

1. Jawny model stanu i relacji kroku, od pustych wyników do zapisu/replay; historia zgłoszenia i decyzji chroniona.
2. TLC sprawdza V1–V8 w skończonych konfiguracjach przeplotów. Każda ma dane, horyzont, wynik, liczbę stanów i źródła z SHA-256.
3. T01–T12 rozliczone: oczekiwania symboliczne rzeczywiście uruchomione; ograniczenia E1–E4 zachowane.
4. Osiągalność zapisu starego wyniku i replay po utracie odpowiedzi potwierdzona śladem TLC. Inwariant negujący cel ma zostać naruszony — to oczekiwany świadek, nie awaria specyfikacji.
5. Sześć minimalnych mutacji wymienionych w mapie musi naruszyć właściwą kontrolę. Błąd parsera, środowiska, timeout lub dowolny niezerowy exit nie oznacza wykrycia mutanta.
6. Odtworzenie jednym poleceniem, logi i konfiguracje w repo. Wyniki nie oznaczają odbioru U ani dowodu kodu produktu.

## Granice ustalone przed badaniem

- Jeden projekt, jeden klient, jedno kryterium, dwie wcześniej zarejestrowane próby. Uprawnienia i zaufanie są symbolicznymi wejściami.
- Trzy podstawy: stara, nowa, zmienione same kryteria. Konfiguracja wybiera parę podstaw, a nie wszystkie projekty/grafy.
- Do trzech żądań, z możliwością kolizji klucza; token przy wysłaniu aktualny albo celowo stary. Warianty błędnych danych są jawne w konfiguracjach.
- Najwyżej jedna zmiana bieżącego kontekstu w konfiguracji; zapis wyniku również podnosi token. Horyzont będzie przypięty w konfiguracji (początkowo 8 kroków, dłuższe świadki osobno). To ograniczenie eksploracji, nie reguła odmowy procesu.
- Odpowiedź może być dostarczona lub utracona; ponowienie zachowuje treść i ID. Awaria przed atomowym zapisem nie zmienia trwałego stanu.
- O3 jest atomową akcją. Badanie nie obejmuje częściowych zapisów realnej bazy, autentyczności logów, odtworzenia procesu systemowego, retencji potwierdzeń, wielokryterialnych wykonań lub automatycznego odbioru.
- Bez fairness i dowodu postępu każdego przebiegu. Wyłączenie kontroli deadlock służy skończonemu badaniu; nie jest dowodem braku blokad.
- Limit uruchomienia: 60 s i 512 MiB sterty na proces TLC; timeout daje wynik nierozstrzygnięty. Zmniejszenie konfiguracji należy ujawnić, a nie nazywać pełnym pokryciem większej.

## Narzędzia i metoda

Pakiet tla2tools release 1.7.4 (silnik zgłasza TLC2 2.19), JAR SHA-256 `936a262061c914694dfd669a543be24573c45d5aa0ff20a8b96b23d01e050e88`; istniejący lokalny Temurin 17.0.21+9. Runner nie pobiera narzędzi ani nie modyfikuje drugiego repo. Ścieżki można przekazać argumentami; nie są zależnością od katalogu tymczasowego.

[Dokumentacja TLC](https://docs.tlapl.us/using:tlc:start) opisuje CLI/config; [opis TLA+ autora](https://lamport.azurewebsites.net/tla/high-level-view.html) rozdziela model stanów i poprawność kodu. Własności sprawdzamy odrębnie od relacji wykonawczej; oczekiwania scenariuszy zapisujemy ręcznie. Nie generujemy oczekiwań z wyniku modelu.

## Odtworzenie

Z korzenia repozytorium (katalog wyniku musi być nowy):

```sh
python3 -B -m unittest discover -s reference/process-map/p3-tla -p test_check.py -v
python3 reference/process-map/p3-tla/check.py --output reference/process-map/p3-tla/.runs/recheck-01
```

Runner domyślnie używa JDK z wcześniejszej próby Flowable oraz JAR z lokalnego `iso-model-state`. Można wskazać dowolną istniejącą zgodną instalację przez `--java /ścieżka/bin/java --jar /ścieżka/tla2tools.jar`. Sprawdza sumę JAR przed wykonaniem. Przypięte źródło narzędzia: [release 1.7.4](https://github.com/tlaplus/tlaplus/releases/tag/v1.7.4). Nie wykonuje pobrania ani instalacji. Sandbox może blokować lokalne gniazdo JVM/RMI — taki wynik jest błędem środowiska, nie kontrprzykładem. Nie potrzebujemy serwera procesu/API.

`--only safety-T06,witness-T06,mutant-token_before_replay` ogranicza odtworzenie do wskazanych prób. Pojedynczy TLC ma limit 60 s, jedna JVM maksymalnie 512 MiB sterty. Przestrzeń robocza jest tymczasowa i odtwarzalna; źródła, konfiguracje i dowody nie zależą od zachowania tego katalogu.

Każdy katalog wyniku zawiera:

- `summary.json`: wersja Javy, SHA-256 JAR/źródeł, polecenia, limity/config ID, kody wyjścia, liczby stanów i klasyfikacja;
- `runs.jsonl`: po jednym rekordzie na próbę, z dokładnym tekstem konfiguracji i pełnym logiem TLC; pole `case` wskazuje próbę;
- kopie `P3.tla`, `cases.json`, `check.py`, odpowiadające zapisanym sumom.

Wynik referencyjny i granice: [raport](report.md). Próby osiągalności celowo kończą się `Invariant NotGoal is violated`: ślad jest świadkiem dojścia do celu. Mutant wymaga wskazanego naruszonego niezmiennika, śladu i kodu 12. Błędów parsera/JVM/timeoutu ani przeżycia mutanta nie zaliczamy jako sukcesu. Przejrzenie źródeł modelu jest nadal potrzebne; sam raport runnera nie dowodzi zgodności z zamiarem.

Archiwum `evidence/development.zip` zachowuje wcześniejsze próby, w tym błąd monitorów (`development-05`) i wyniki sprzed doprecyzowania świadków (`full-01`, `full-02`, `full-03`). Nie są końcowym wynikiem. Dla odtworzenia starej próby rozpakować odpowiedni katalog do własnej kopii, uruchomić jego `check.py` z jawnymi `--java` i `--jar`; `development-05` celowo ujawnia cztery niewykryte mutacje. Pierwsze błędy parsowania/środowiska bez kompletu źródeł są tylko diagnostyką, nie odtwarzalnym dowodem własności.
