# Próba Flowable — środowisko, dane i reguły

Eksperyment edukacyjny, F1–F5 (D-94–D-97/D-99) oraz generator karty (A-10). Jedyny plan i rejestr wykonania: [mapa §8.7–8.8](../../process-modeling/coverage-map.md#87-zalecenia-i-punkt-wznowienia); zakres i granice [F1 §10](../../process-modeling/coverage-map.md#10-f1--dopasowanie-flowable-do-karty-zmiany-wymagania--2026-11-04). To nie narzędzie wydania ani nowy proces produkcyjny.

**Wybierz wynik:** [raport F5 — trwałość i wznowienie](f5-report.md) albo [karty operatora i dowody generatora](evidence/operator-card/README.md). Instrukcja karty jest w [sekcji A-10](#czytelna-karta-operatora--a-10). Karty odczytują archiwalne eksporty; nie pokazują stanu projektu na żywo.

**Wcześniejsza dostawa F4:** [pięć widoków wykonanego scenariusza](evidence/f4-demo.md); opis i dowody w sekcji „Wynik F4”. Poniższe plany F2–F5 i ich przyszły czas zachowują chronologię eksperymentu; aktualne zlecenia są w mapie §8.7. Testy całego tego eksperymentu: `./verify -o clean verify`; nie obejmują pakietu procesu ani lekcji L1.

**Widoki przed F5 (D-98):** [osiem diagramów Mermaid — C4, zależności i struktury danych](architecture.md). Zacznij od widoków 1–3; opisują istniejące F4 i aktualizację przechowywania F5.

**Dostawa F5:** [raport wznowienia, dowody i ocena dopasowania](f5-report.md); [stan do oceny przez operatora](evidence/f5-restart/07-show.json.md).

## F3 — kontrakt reguł przed implementacją

D-96, decyzja agenta A13, 2026-11-04. Wykonujemy czyste funkcje na niezmiennej migawce oraz rzeczywistą tabelę DMN. Nie budujemy jeszcze przebiegu BPMN, magazynu, zgód, UI ani adaptera Git. Reguły poniżej obowiązują eksperyment; nie zmieniają W5/E9 i nie aktywują P1/P2 w szablonie.

| Reguła | Oczekiwanie pozytywne | Odmowa / wynik negatywny i granica |
| --- | --- | --- |
| R1 Tożsamość migawki | Wiele rewizji jednego ID, jawne wskazanie bieżącej; defensywne kopie danych | Duplikat tej samej rewizji, zmiana typu jednego ID lub duplikat ID dowodu → wyjątek, bez zmiany wejścia. Nie wybieramy samowolnie największej rewizji jako bieżącej. Brak wskazanego artefaktu → nieznana podstawa przy ocenie |
| R2 Dopisywanie wyników | Nowy wynik tworzy nową migawkę, stara pozostaje bez zmian | Istniejący ID wyniku, nawet z identyczną treścią → odmowa. Brak operacji nadpisania/usunięcia w tym interfejsie. To kontrola funkcji, nie ochrona bazy ani autoryzacja |
| R3 Kandydaci wpływu | BFS po logicznych ID zależności: łańcuch, rozgałęzienie, cykl; unikalny kandydat z jedną deterministyczną drogą od zmiany | Brak znanego źródła → odmowa; element niezwiązany i samo źródło nie trafiają do wyniku. Rewizje nie maskują zależności do starej podstawy. Lista jest doradcza, nie automatycznym unieważnieniem |
| R4 Aktualność przeglądu | Wskazany bieżący przedmiot, bieżące bezpośrednie podstawy i pass dla dokładnie tego zestawu → PASSED | Brak znanych danych → UNKNOWN; brak pasującej oceny albo zmieniona podstawa → REVIEW_REQUIRED. Fail dla tej samej podstawy → CORRECTION. Pass i fail dla tej samej podstawy → CONFLICT niezależnie od kolejności; F3 nie rozstrzyga konfliktu automatycznie |
| R5 Wynik wykonania testu | Pass dotyczy konkretnej bieżącej rewizji przypadku testowego i programu | Dawny pass nie odnawia nowej pary; znana bieżąca para bez wyniku → REVIEW_REQUIRED. ERROR obok PASS tej samej pary → UNKNOWN. Nieznane dane, niewłaściwe typy lub ERROR wykonania → UNKNOWN; fail → CORRECTION; sprzeczne wyniki tej samej pary → CONFLICT. Przegląd testu i wykonanie testu są oddzielnymi ocenami |
| R6 Kwalifikacja DMN | Fakty z wybranego, niepustego zestawu sprawdzeń; bez braków/konfliktu/fail/oczekiwania → TO_OPERATOR | Kolejność: nieznana podstawa → MISSING_BASIS; konflikt → REVIEW_REQUIRED; fail → CORRECTION; oczekiwanie → REVIEW_REQUIRED. Pusta lista sprawdzeń nie daje gotowości. Brak wyniku DMN, wiele trafień lub nieznany wynik → wyjątek, nigdy TO_OPERATOR |

R4 porównuje zbiór podstaw bez znaczenia kolejności i duplikatów. Zależności migawki opisują aktualny graf logiczny; mogą nadal wskazywać starą rewizję podstawy — wtedy ocena wymaga odnowienia. Stara rewizja zależnego końca krawędzi również wymaga odnowienia. Relacja VERIFIES o typach innych niż wymaganie → przypadek testowy daje UNKNOWN. Sama nowa ocena CAP nie odnawia AT. Dawne sprzeczne wyniki innej rewizji nie blokują nowej, jawnie ocenionej podstawy. Przejście od fail do pass na identycznej podstawie pozostaje konfliktem do osobnego rozstrzygnięcia; to ostrożne założenie próby z F1, nie nowa reguła wydania.

Ocena dotyczy wskazanych przedmiotów; kompletność doboru sprawdzeń i sens zależności nadal wymagają analizy. Nawet TO_OPERATOR oznacza tylko możliwość przedłożenia tych wyników, nie zatwierdzenie zmiany, odbiór ani wydanie. Migawka nie jest dowodem prawdziwości deklaracji pass.

Kolejność wykonania F3: przypadki i testy → kompilujący się RED → minimalny kod/DMN → GREEN → wyłączenia R1–R6 na izolowanej kopii → osobny przegląd. Kryterium: dla każdej reguły przypadki pozytywne i negatywne, dla każdej wybranej mutacji porażka asercji (nie kompilacji/infrastruktury); pełna regresja wraz z F2. Dowody trafią do evidence/. F4 obejmie tożsamość poleceń, przejścia, atomowy zapis i rolę operatora; F5 restart.

## Zakres i kryteria F2

1. Standardowy projekt Maven z przypiętym zestawem, uruchamiany jednym poleceniem po przygotowaniu JDK.
2. Test rzeczywiście tworzy silnik BPMN i dołączony DMN, odpytuje ich usługi i zamyka zasoby; baza testu jest lokalna i odizolowana.
3. Jeden model informacji w Javie, niezależny od Flowable; wyniki przeglądu i wykonania testu mają różne typy, podstawy wskazują rewizje.
4. Zapisane faktyczne wersje, instrukcja oraz wyniki. Brak zależności od katalogów tymczasowych i brak zmiany testów pakietu.

F2 nie zaliczało reguł ani przebiegu. Dostawa F3 i dowody są poniżej; F4 obejmie przebieg zmiany, F5 restart JVM i ocenę widoku.

## Uruchomienie

Z tego katalogu, jednorazowo na macOS arm64:

```sh
./setup-jdk
```

Skrypt pobiera archiwum Eclipse Temurin 17.0.21+9 i sprawdza przypięte SHA-256. Rozpakowuje je do ignorowanego `.tooling/`; nie zmienia instalacji systemowej ani profilu powłoki. Pobranie jest jawne, nie jest ukrytym skutkiem testu. Na innych platformach przygotuj JDK 17 i wskaż `TRIAL_JAVA_HOME`; takich platform tu jeszcze nie sprawdzono.

Testy i pakowanie:

```sh
./verify
```

Wrapper pobierze Maven 3.9.12 i zależności przy pierwszym uruchomieniu. Cache dystrybucji i artefaktów pozostają w `.tooling/`, wyniki w `target/`. Skrypt pomija globalne/użytkowe settings.xml, żeby prywatne repozytoria i profile nie wpływały na próbę. Dla już pobranego zestawu: `./verify -o clean verify`. Enforcer odmawia innej głównej wersji JDK i innej wersji Maven. Import IDE: otworzyć pom.xml, wybrać lokalny JDK 17; powtarzalny punkt odniesienia to skrypt verify.

## Wybory techniczne — decyzja agenta A12, 2026-11-04

| Wybór | Powód / granica |
| --- | --- |
| Java 17, rekordy i enumy; bez Lomboka, Spring Boot i JPA | Wystarczą do małego modelu; brak generowanych getterów, kontenera i mapowania ORM przed wykazaniem potrzeby |
| Maven, standardowe src/main/java i src/test/java, Wrapper 3.3.4 / Maven 3.9.12 | Układ znany narzędziom; wersja wrappera i Maven zgodna z przypiętym repo Flowable. Wrapper skopiowany bez przerabiania z commita 0779d68e5a3385b74d8acb8bc37901ff54513249; zachowana licencja Apache w skryptach oraz [pełny tekst licencji](LICENSE-maven-wrapper.txt) |
| Flowable BOM 8.0.0; JUnit BOM 6.0.1 / Jupiter; H2 2.4.240; SLF4J 2.0.17 | Wersje z flowable-dependencies 8.0.0. „JUnit Jupiter” nie oznacza przypięcia do generacji 5; to wydanie producenta używa 6. Brak zakresów wersji zależności i SNAPSHOT dostawców |
| JUnit do małych testów danych i testu integracyjnego silnika w tym samym verify | Mały projekt nie potrzebuje osobnej infrastruktury Failsafe/serwera. Brak mockowania silnika w teście kompatybilności |
| Jedna konfiguracja BPMN z dołączonym DMN i wspólną bazą | Sprawdzamy rzeczywisty zestaw z F1, bez dwóch niezależnych magazynów. Zamknięcie obu silników jawne |
| H2 memory dla F2/F3 | Nie udaje trwałego projektu; restart i odtwarzanie po zakończeniu JVM dopiero F5 |
| Konstruktor chroni poprawność struktury; reguły procesu poza rekordami | Brak pustych ID/referencji, dodatnia rewizja, kopie kolekcji. Istnienie relacji, aktualność i uprawnienia nie wynikają z samego poprawnego rekordu |

Nie tworzymy ogólnej warstwy repozytoriów, CQRS, frameworka zdarzeń ani drugiego automatu statusów.

## Jeden model danych

Źródło typów: [domain](src/main/java/org/example/processlab/domain). To zwykłe rekordy Javy, bez importów Flowable i bez encji ORM.

| Typ | Co reprezentuje | Czego sam nie potwierdza |
| --- | --- | --- |
| ArtifactRef(id, revision) | Konkretną rewizję elementu, np. CAP-01@2 | Że taki element istnieje; unikalność i przydział rewizji należą do przyszłych operacji |
| ArtifactRevision(ref, kind, content) | Treść wymagania, przypadku testowego lub fikcyjnej wersji programu | Poprawności treści i statusu zatwierdzenia |
| Dependency(basis, dependent, kind) | Typowaną krawędź od podstawy do zależnego produktu | Sensu relacji i jej aktualności; odwrotny indeks ma być wyliczany, nie zapisywany drugi raz |
| ReviewRecord(id, subject, basis, outcome, rationale) | Ocenę wskazanego przedmiotu wobec listy podstaw; lista jest kopiowana defensywnie | Rzeczywistego wykonania przeglądu ani niezależności recenzenta |
| TestRunRecord(id, testCase, software, outcome) | Wynik uruchomienia dla wskazanego testu i wersji programu, oddzielony od oceny testu | Prawdziwości deklarowanego wyniku; w F2 to dane fikcyjne, bez adaptera runnera |

Wszystkie odnośniki są do rewizji, nie tylko ID. Konstruktor sprawdza lokalną strukturę (null, puste teksty, dodatnia rewizja), ale nie przechodzi po grafie. Dopuszczona pusta lista podstaw przeglądu nie oznacza, że każda ocena ma wystarczające podstawy — to późniejsza reguła zależna od rodzaju oceny. Typ końca relacji i istnienie wskazanego elementu też wymagają rozstrzygnięcia w zbiorze danych. W F2 nie ma flagi globalnego „tests_ok”, statusu wydania ani automatycznej zgody.

Niezmienny obiekt w pamięci nie chroni przed nadpisaniem rekordu w bazie. Można nadal utworzyć dwa obiekty o tym samym ID i rewizji, ale różnej treści — integralność zbioru wymaga reguły zbioru; w F3 zapewnia ją ProjectSnapshot, nadal bez magazynu operacyjnego. P1/P2 nadal nie zostały wdrożone. Model jest minimalnym podzbiorem dla tej próby, nie pełnym modelem ISO ani ukończonym kontraktem przyszłej fasady.

## Granica infrastruktury i późniejszego zapisu

[EngineSession](src/main/java/org/example/processlab/engine/EngineSession.java) ma jeden obowiązek: utworzyć i zamknąć BPMN z dołączonym DMN. Konfigurator producenta współdzieli bazę i usługi; nie modyfikujemy tabel Flowable. Włączenie konfiguratorów jest jawne, automatyczne wykrywanie przez ServiceLoader wyłączone; oddzielnie wyłączone są domyślnie wbudowane IDM i Event Registry. Używamy publicznej konfiguracji StandaloneProcessEngineConfiguration, występującej w tutorialu producenta (klasa leży w pakiecie impl.cfg); nie korzystamy z managerów encji ani wewnętrznych komend SQL. Nazwa testowej bazy nie przyjmuje parametrów JDBC. Test generuje unikalną nazwę UUID; dwie sesje z identyczną nazwą nie byłyby izolowane od siebie. Kolejność zamknięcia: BPMN, potem DMN, ponieważ BPMN wykonuje końcowe operacje SQL, a oba silniki współdzielą pulę połączeń.

**Wariant dla F3/F4:** dane fikcyjnej zmiany mają być jednym serializowanym stanem domeny w zmiennej procesu, a przyjęcie wyniku i ukończenie zadania jednym wywołaniem `TaskService.complete(taskId, variables)`. Reguły przygotowują nową wartość bez mutacji starej. To pozwala uniknąć osobnego magazynu obok bazy silnika; nie oznacza jeszcze niezmiennego dziennika. Polecenia pozostają sekwencyjne, zgodnie z F1. Odmowę, ponowienie i błąd podczas zapisu trzeba sprawdzić w F3/F4. F2 nie dowodzi atomowości własnej przyszłej fasady, a kontrola wykonana przed wywołaniem API nie chroni sama przed wyścigiem wielu klientów.

Zależności przechodnie zawierają m.in. Spring Core/Beans, używane przez biblioteki producenta. „Bez Spring Boot” oznacza brak aplikacji/kontenera Boot; nie obietnicę braku jakiegokolwiek JAR-a Spring na classpath. Faktyczny zestaw testu: [test-classpath.txt](evidence/test-classpath.txt).

Źródła: [układ Maven](https://maven.apache.org/guides/introduction/introduction-to-the-standard-directory-layout.html), [Maven Wrapper](https://maven.apache.org/tools/wrapper/), [archiwa Temurin](https://adoptium.net/installation/archives), [wersje zależności Flowable](https://github.com/flowable/flowable-engine/blob/0779d68e5a3385b74d8acb8bc37901ff54513249/modules/flowable-dependencies/pom.xml). Sprawdzenie sumy archiwum nie jest podpisem wydawcy ani audytem zależności.

## Wynik wykonania — 2026-11-04

| Sprawdzenie | Rzeczywisty wynik | Dowód / granica |
| --- | --- | --- |
| RED na kompilujących się szkieletach | 5 testów, 4 porażki asercji, 0 błędów wykonania | [f2-red.log](evidence/f2-red.log): brak silnika, brak walidacji i zmiana podstawy przeglądu przez alias listy. Nie zaliczono awarii pobrania jako RED |
| Pierwsze uruchomienie implementacji | 4 testy danych przeszły; błąd zamykania współdzielonej bazy w teście silnika | [f2-close-order-failure.log](evidence/f2-close-order-failure.log). DMN zamykany przed BPMN usuwał bazę pamięciową za wcześnie; poprawiono kolejność |
| RED ustalenia recenzenta: niezamierzone silniki | 5 testów, 1 porażka: oprócz BPMN/DMN powstawały IDM i Event Registry | [f2-explicit-engines-red.log](evidence/f2-explicit-engines-red.log). Test porównuje różne obiekty konfiguracji, nie liczbę aliasów mapy. Wyłączenie ServiceLoader nie wystarczało; dodano jawne wyłączenia |
| Końcowe GREEN, pełne clean verify offline | 5 testów PASS, JAR zbudowany | [f2-green.log](evidence/f2-green.log). Test silnika potwierdza dokładnie BPMN/DMN i wspólny DataSource, a po zamknięciu brak instancji w ich rejestrach i brak już istniejącej bazy H2 |
| Pierwsze powtórzenie offline, przed korektą recenzenta | 5 testów PASS, clean verify i JAR bez sieci | [f2-offline.log](evidence/f2-offline.log). Końcowe GREEN powyżej także wykonano offline, już z rozszerzonym testem. Nie jest to restart trwałej sprawy ani test innego systemu operacyjnego |
| Wersje środowiska | Maven 3.9.12, Temurin 17.0.21+9, macOS arm64 | [toolchain.txt](evidence/toolchain.txt), [pom.xml](pom.xml), właściwości Wrappera. Maven ZIP sprawdzony z SHA-512 producenta, wyliczone SHA-256 przypięte w Wrapperze |
| Odmowa niewłaściwego JDK | JBR 21.0.10 odrzucony przez RequireJavaVersion przy validate, kod 1 | [f2-jdk-guard.log](evidence/f2-jdk-guard.log); to oczekiwana kontrola środowiska, nie RED reguły domenowej |

Na początku sandbox uniemożliwił pobranie Mavena, później zależności pluginu pakującego. Pobrania ponowiono z właściwym uprawnieniem; nie są to defekty semantyki ani dowody RED. Pomocniczy odczyt XML raportu przez systemowy Python Homebrew nie działał z powodu biblioteki expat; zestaw artefaktów odczytano `/usr/bin/python3`, bez zmian środowiska. Budowanie i testy eksperymentu nie potrzebują Pythona.

### Odtworzenie RED

[f2-implementation.patch](evidence/f2-implementation.patch) zachowuje pełne źródła od kompilujących się szkieletów do końcowego GREEN. Po F4 EngineSession ma dodatkowe API/konfigurację, więc nie stosujemy tej historycznej łaty bezpośrednio do bieżącego źródła. Uruchom `/usr/bin/python3 replay-f2.py`: skrypt rekonstruuje wyłącznie źródła F2 i jego dwa pliki testów na odrębnych kopiach, wykonuje RED (5 testów / 4 porażki / 0 błędów), potem GREEN (5 PASS). [Wynik ponowienia po F4](evidence/f2-compat-replay.json). Zachowano historyczny test silnika; nie uruchamia się na nim testów API dodanego później. Lokalne JDK/cache jak wyżej; żaden dawny katalog tymczasowy ani edycja bieżącego kodu nie są potrzebne.

### Osobna recenzja

Sesja `review_flowable_f2`, bez historii tworzenia implementacji, odczytała kod i dowody oraz opracowała własne przypadki. Zgłosiła jeden bloker: domyślne IDM/Event Registry nie były wyłączone, a test zamknięcia H2 nie wykrywał ich pozostawienia w rejestrach. Po nowym RED, poprawce i końcowym GREEN recenzent ponownie odczytał kod/logi i potwierdził zamknięcie ustalenia — **bez otwartych blokerów F2**. Nie uruchamiał testów samodzielnie.

Pozostałe przypadki recenzenta (parametry JDBC w nazwie, null w basis, sprzeczne treści tej samej rewizji, identyczna nazwa dwóch baz) mają odpowiedź lub jawną granicę wyżej. Wynik F2 nie stanowi odbioru użytkowego, wdrożenia reguł C1–C10 ani zgody na F3–F5. Nie wykonano commita. Lokalny katalog .tooling zajmował po tej próbie około 558 MiB, razem z archiwum JDK i cache; jest wyłączony z Git.

## Wynik F3 — 2026-11-04/05

**Wykonano reguły w izolacji, nie kompletny proces zmiany.** [Rules](src/main/java/org/example/processlab/rules/Rules.java) wylicza wpływ i aktualność; [ProjectSnapshot](src/main/java/org/example/processlab/rules/ProjectSnapshot.java) chroni tożsamość i dopisywanie; [DMN](src/main/resources/qualification.dmn) kwalifikuje fakty przez [DmnQualifier](src/main/java/org/example/processlab/engine/DmnQualifier.java). Wszystkie dane ocen są fikcyjne. Testy rzeczywiście uruchamiają kod Javy i silnik DMN, ale nie wykonują programu TextStats ani Kitchen.

Przykład: CAP-01@2 jest bieżące, lecz przegląd AT-01@2 wskazuje CAP-01@1. Historyczny pass pozostaje zapisany; wynik R4 to REVIEW_REQUIRED. Po dopisaniu przeglądu dokładnie bieżącej podstawy i aktualnego wykonania test/program DMN może zwrócić TO_OPERATOR. To nadal nie odbiór operatora.

| Sprawdzenie | Rzeczywisty wynik | Dowód |
| --- | --- | --- |
| Pierwszy RED przed implementacją Java | 31 testów, 25 porażek asercji, 0 błędów wykonania; kompilacja udana | [f3-red.log](evidence/f3-red.log). Tabela DMN była już zapisana; wykonawca i funkcje były szkieletami |
| GREEN z przypadkami recenzenta, regresją F2 i pakowaniem | 38/38 PASS, 0 błędów; offline clean verify | [f3-green.log](evidence/f3-green.log). 11 testów reguł, 22 wywołania testów DMN (w tym 16 kombinacji czterech faktów), 5 wcześniejszych testów F2 |
| Odtworzenie RED na kopii z końcowym zestawem testów | 38 testów, 32 porażki asercji, 0 błędów wykonania | [f3-red-replay.json](evidence/f3-red-replay.json), [log](evidence/f3-red-replay.log), [zachowane szkielety](evidence/f3-red-sources.json). Siedem testów dodano po recenzjach kontrprzykładów i izolacji wdrożeń; to przyczyna różnicy względem pierwszego RED |
| Celowe uszkodzenia R1–R6 | 14/14 wykrytych, każdorazowo 38 testów, ≥1 porażka asercji, 0 błędów i pominięć | [wyniki i nazwy logów](evidence/f3-mutations.json), [skrypt](verify-mutations.py). To wybrany zestaw usterek, nie pełny mutation score ani dowód wszystkich kombinacji stanu |

Zakres mutacji: przywrócenie fallbacku dla nieznanego rodzica wdrożenia; dopuszczenie duplikatu rewizji; utrata dopisywanego wyniku; brak przechodniego BFS; pomijanie podstawy przeglądu i starej krawędzi; pomijanie rewizji programu i ERROR; gotowość pustego zestawu; zmiana każdego z pięciu rozstrzygnięć DMN. Każda mutacja powstawała na osobnej kopii. Oryginalny katalog źródeł pozostawał bez zmian; współdzielono wyłącznie lokalne narzędzia/cache. Nie modyfikowano wersji zależności.

### Odtworzenie F3

[Historyczne sumy SHA-256 F3](evidence/f3-inputs.sha256) identyfikują stan przed F4. F4 rozszerza konfigurację silnika, API kwalifikatora i POM; zestaw F4 opisuje evidence/f4-inputs.sha256, po F5 historyczny. Nie oczekujemy identyczności tych zmienionych plików ze starymi sumami.

Z katalogu próby, po przygotowaniu JDK/cache zgodnie z „Uruchomienie”:

```sh
./verify -o clean verify
/usr/bin/python3 verify-mutations.py --red
/usr/bin/python3 verify-mutations.py
```

Dwa ostatnie polecenia wymagają Pythona ze standardową biblioteką XML; na tym Macu sprawdzono `/usr/bin/python3`. To pomocniczy odtwarzacz dowodów, nie zależność aplikacji Java. Skrypt tworzy i usuwa własne kopie tymczasowe, zapisuje trwałe logi i JSON w evidence/. Odtwarzacz wybiera wyłącznie cztery klasy testów F2/F3, również po dodaniu F4. Używa szkieletu z importem i sygnaturą konstruktora DmnQualifier dostosowanymi do API DmnEngine; po F4 dodano także pustą metodę evaluateWithoutHistory, żeby aktualne źródła kompilowały się przy odtwarzaniu. Logika szkieletu nadal jest pusta; stan szkieletu sprzed F4 zachowuje evidence/f3-red-sources-before-f4.json. [Pierwotny szkielet](evidence/f3-initial-red-sources.json) zachowuje dokładny stan pierwszego RED, przed zmianą API. Kod 0 skryptu oznacza wykrycie wszystkich wybranych usterek; kod 1 lub wyjątek oznacza nieudaną/infrastrukturalną próbę. Błąd kompilacji bez raportu JUnit oraz błąd wykonania testu nie są uznawane za wykrytą mutację. Nie potrzeba żadnego poprzedniego katalogu w /private/tmp. Ponowienie nadpisuje te same pliki wyników.

Źródła producenta użyte do implementacji: [API DMN](https://www.flowable.com/open-source/docs/dmn/ch03-API/) oraz przypięte do 8.0.0 [ExecuteDecisionBuilder](https://github.com/flowable/flowable-engine/blob/0779d68e5a3385b74d8acb8bc37901ff54513249/modules/flowable-dmn-api/src/main/java/org/flowable/dmn/api/ExecuteDecisionBuilder.java). Dokumentacja WWW miesza nazwy historycznych usług; kompilacja i testy odnoszą się do DmnDecisionService z przypiętych zależności. Kwalifikator wymaga dokładnie jednej definicji pod parentDeploymentId + key, przypina jej ID i wersję, ponownie rozwiązuje ją przed oceną oraz porównuje key/version audytu wykonania. Testy sprawdzają brak przełączenia na późniejszą tabelę oraz odmowę dla nieznanego/usuniętego wdrożenia i ponownie użytego rodzica. To sekwencyjna próba: osobne zapytanie i wykonanie nie zapewniają atomowości przy równoległym redeploy. Błędy wykonawcy propagują się jako wyjątki; brak pojedynczego znanego wyniku nie daje domyślnej kwalifikacji pozytywnej.

### Osobna recenzja F3

Recenzent `review_flowable_f3` najpierw przeczytał F1 i kontrakt, bez historii implementacji, oraz zaproponował osiem kontrprzykładów. Następnie odczytał kod, testy i logi. Sprawdził m.in. oba końce starej krawędzi, brak danych poza ocenianą parą, ERROR obok PASS, kolejność sprzecznych wyników, jawne wskazanie starszej rewizji, stabilną drogę w rombie BFS i kolizje ID różnych rodzajów dowodów.

**Znalazł jeden bloker mimo pierwszego GREEN 36/36:** API DMN mogło wybrać obcą tabelę przy nieznanym rodzicu, a test łapał błąd wcześniej wdrożonej wadliwej tabeli zamiast odmowy braku wdrożenia. Ujawnienie: [log mutacji sprzed poprawki](evidence/f3-deployment-discovery.log); odtworzenie na osobnym silniku: [RED 1/1 failure, 0 errors](evidence/f3-deployment-red.log). Pierwotne [GREEN](evidence/f3-green-before-review.log) nie jest końcową podstawą zamknięcia.

Poprawka: jawne wyszukanie i przypięcie definicji, ponowne sprawdzenie przed oceną, key/version audytu i trzy testy na izolowanych silnikach. Pierwsza próba porównania getDmnDeploymentId wykazała, że to pole audytu w 8.0.0 nie jest wypełniane: [log diagnostyczny](evidence/f3-audit-field-failure.log), 18 błędów wykonania — nie zaliczono ich jako semantycznego RED. Końcowa implementacja nie opiera się na tym polu ani wewnętrznych API. Wybranie obcej tabeli przez publiczny wykonawcę jest widoczne w przypiętym [AbstractExecuteDecisionCmd](https://github.com/flowable/flowable-engine/blob/0779d68e5a3385b74d8acb8bc37901ff54513249/modules/flowable-dmn-engine/src/main/java/org/flowable/dmn/engine/impl/cmd/AbstractExecuteDecisionCmd.java); odczyt źródła wyjaśnia wynik, nie zastępuje próby.

Recenzent potwierdził semantyczne zamknięcie blokera w sekwencyjnej granicy F3 i odczytał GREEN 38/38. Końcowy odczyt całego kompletu (38/38 GREEN, 38/32/0 RED replay, 14/14 mutacji) zakończył recenzję: brak otwartych blokerów F3. Nie uruchamiał testów samodzielnie. Osobny kontekst recenzenta ogranicza część wspólnych błędów, nie dowodzi niezależności rozumowania.

Kontrola zapisu: [make check](evidence/f3-repository-check.log) — kod 0, 262 elementy, 0 błędów, 7 ostrzeżeń (W1 MIG-01/02, W2 D-92–96 bez commitów). [Sprawdzenie dokumentacji](evidence/f3-document-check.json) — 120 lokalnych ścieżek w czterech dokumentach, brak brakujących plików; bez sprawdzania kotwic i prawdziwości treści. `git diff --check` bez błędów. Pakiet template/ nie był zmieniany, więc nie ponawiano jego testów dystrybucji.

### Granica wyniku i dalszy krok

F3 nie ocenia poprawności treści, kompletności wybranych sprawdzeń ani prawdziwości pass. Bezrodzicowy artefakt może być oceniony wobec pustego zbioru podstaw, ale wybór takiej granicy wymaga analizy. Nie ma trwałego dziennika, uprawnień, obsługi komend, transakcji ani działającego workflow. Odmowa duplikatu dotyczy konstrukcji nowej migawki w pamięci; historyczna migawka pozostaje niezmienna. To nie ochrona przed ingerencją w bazę.

Po F3 następnym etapem było użycie tych reguł w przebiegu BPMN. F4 zostało później zlecone D-97 i rozliczone poniżej. F5, UI, REST, P1/P2 operacyjne, W5/E9 i inne repozytoria pozostają poza dostawą. Nie tworzono rekordów VER/VAL/ACC ani commita. Status i właściciele dalszej pracy są wyłącznie w mapie §8.7–8.8, a nie w drugim planie tutaj.


## F4 — kontrakt przed implementacją (A14, 2026-11-05)

D-97. Dotychczasowe funkcje oceniają migawkę, ale nie pamiętają oczekującego zadania ani nie zapisują wyniku razem z przejściem. Dodajemy **jeden BPMN** i małą lokalną fasadę Java; silnik pozostaje jedynym właścicielem stanu zadań. Nie dodajemy ogólnego systemu uprawnień, serwera ani drugiego magazynu.

Przebieg: zgoda na propozycję zmiany → ocena wpływu i zastosowanie → przygotowanie testu/programu → przeglądy i wynik wykonania → kwalifikacja DMN → decyzja operatora. Kwalifikacja CORRECTION wraca do przygotowania, MISSING_BASIS/REVIEW_REQUIRED do ocen; obowiązują priorytety R6, więc fail nie przesłania UNKNOWN/CONFLICT. Odrzucenie odbioru wraca do przygotowania; odmowa zgody kończy sprawę bez zastosowania odrzuconej propozycji; wcześniejsze zastosowane zmiany i wyniki pozostają. Nowa propozycja podczas pracy przekierowuje do nowej zgody, przed zmianą danych wymagania. Nowa zmiana po przyjęciu tworzy nową instancję powiązaną z poprzednią.

| Kontrola F4 | Przypadek i oczekiwanie przed kodem |
| --- | --- |
| F4-01 Kolejność i dwa rodzaje decyzji | Bez zgody operatora nie można zastosować propozycji. Po zgodzie agent wykonuje pracę. Brak odbioru zostawia zadanie oczekujące; przyjęcie wymaga aktualnych ocen i jawnej decyzji operatora |
| F4-02 Negatywny wynik | Zakończenie ocen zapisuje wynik; DMN CORRECTION kieruje do przygotowania. FAIL + UNKNOWN daje MISSING_BASIS, FAIL + CONFLICT daje REVIEW_REQUIRED; żadna z tych kombinacji nie prowadzi do odbioru. Nowe rewizje i nowe wyniki pozwalają kontynuować, dawne wyniki pozostają |
| F4-03 Dokładny cel polecenia | Każde polecenie ma ID, processInstanceId, taskId, oczekiwaną wersję migawki i symulowaną rolę. Zły etap/instancja/wersja/rola lub powtórzone ID → odmowa bez zmiany stanu. ID polecenia jest unikalne w danej instancji. Nie wyszukujemy celu po nazwie zadania |
| F4-04 Zmiana podczas przeglądu/odbioru | Propozycja nie podmienia treści; nowa zgoda i zastosowanie tworzą nową rewizję. Stare taskId/wersja nie kończą nowego zadania; stare wyniki nie odnawiają nowej podstawy |
| F4-05 Historia i następna zmiana | Brak operacji nadpisania wyników; nowe rewizje mają nowe numery większe od dotychczasowych danego ID. Następna sprawa bierze bazę z przyjętej poprzedniej; jej zakończony odbiór i dane pozostają bez zmian |
| F4-06 Atomowy skutek | JSON nowej migawki, rejestr ID wykonanych poleceń i przejście zadania zapisujemy jednym TaskService.complete(taskId, variables). Kontrola negatywna: wyjątek z synchronicznej obsługi zdarzenia po kwalifikacji cofa migawkę, zakończenie zadania i historię DMN; to samo ID można ponowić po usunięciu awarii |
| F4-07 Widok | Odczyt z usług runtime/history: bieżące rewizje, osobne statusy ocen, zadanie i rola, historia zadań i wyników, powiązanie z poprzednią instancją. Widok nie utrzymuje ręcznie drugiej kopii statusu |
| F4-08 Przyjęcie dowodu | Po ustaleniu recenzenta R-F4-02: zarówno migawka wejściowa, jak i nowy batch wyników wymagają istnienia wszystkich rewizji subject/basis/test/software w momencie zapisu. Cały batch odrzucony przed complete przy choć jednej brakującej referencji; istniejące historyczne rewizje pozostają dopuszczalne |

Decyzje techniczne agenta A14: zachowujemy jeden jawny zakres trzech logicznych ID (wymaganie, test, program) w każdej sprawie; oceniamy przegląd wymagania, przegląd testu i wykonanie pary test/program regułami F3. Dobór zakresu i sens ocen pozostają analizą. TekstStats jest fikcyjnym przykładem; zapis PASS nie uruchamia programu produktu.

Dane: niezmienny rekord stanu zawiera migawkę F3, zakres, propozycję, upoważnienie do tej propozycji, wersję stanu, potwierdzenia poleceń i ewentualny odbiór. Bez pola kopiującego etap BPMN. JSON z konkretnych rekordów (bez polimorficznego deserializowania dowolnych klas); Jackson databind 3.0.1 już obecny w cache zestawu Flowable zostanie jawną zależnością Maven. Nie instalujemy nowego środowiska. Historia FULL służy próbie odtworzenia przebiegu; nie jest nieusuwalnym dziennikiem audytowym.

Rola pochodzi z zaufanego harnessa edukacyjnego. Bezpośrednie usługi Flowable i edycja bazy nie są chronione tą fasadą. Polecenia oraz wdrożenia są sekwencyjne, bez konkurujących klientów. Zapis domeny i ukończenie zadania są wspólną transakcją; odczyty walidacyjne przed nią nie dowodzą ochrony przed wyścigiem. Test awarii ma sprawdzić rzeczywisty rollback, nie tylko niezmienność obiektu Java. Start nowej instancji ma osobne ID biznesowe, sprawdzane pod kątem powtórzenia w tej sekwencyjnej granicy.

Kolejność realizacji w A-06: kontrakt i osobny przegląd → testy integracyjne na prawdziwym silniku oraz RED → minimalny kod i BPMN → GREEN, wymuszona awaria i wybrane naruszenia → wygenerowany raport demo, osobny przegląd i aktualizacja pamięci. F5 pozostaje niezlecone; H2 nadal pamięciowe. Odbiór użyteczności przez operatora nie wynika z testów.

Doprecyzowanie A14 po recenzji kontraktu: agent może z zadania ocen jawnie wrócić do przygotowania (`Rework`), np. po ERROR wykonania wymagającym nowej wersji programu. Nie jest to odbiór ani zmiana wymagania. Zapytania widoku i ponowna kwalifikacja przed decyzją nie zapisują historii DMN; właściwa kwalifikacja po ocenach wykonuje się synchronicznie wewnątrz przejścia BPMN.


## Wynik F4 — 2026-11-05

**Działa jeden przebieg BPMN z prawdziwymi zadaniami, historią i kwalifikacją DMN.** Dostępny jest lokalny interfejs Java oraz wygenerowany raport scenariusza. Role operatora i agenta oraz treści ocen są danymi symulacji. Nie wykonywano programu TextStats, nie zatwierdzano rzeczywistego wymagania ani produktu.

Najkrótsza ścieżka oglądania: [raport demo](evidence/f4-demo.md), kolejno widoki 1–5. Widać oczekiwanie na zgodę, fail przeglądu testu mimo pass jego wykonania, poprawkę do nowej rewizji, osobne oczekiwanie na odbiór oraz następną sprawę z zachowanymi starymi wynikami wymagającą nowych ocen. Raport jest odczytem kolejnych stanów silnika, nie ręcznie narysowanymi statusami. To jeszcze nie interaktywny ekran ani test użyteczności z operatorem.

### Kod i granica odpowiedzialności

| Element | Odpowiedzialność |
| --- | --- |
| [change.bpmn20.xml](src/main/resources/change.bpmn20.xml) | Pięć rodzajów zadań oczekujących: authorize, impact, prepare, assess, accept. Drogi po decyzji/kwalifikacji i powroty. Brak domyślnej gałęzi pozytywnej |
| [ChangeProcess](src/main/java/org/example/processlab/workflow/ChangeProcess.java), [polecenia](src/main/java/org/example/processlab/workflow/ChangeCommands.java) | Siedem typów operacji; kontrola roli, etapu, processId/taskId/wersji/commandId, ochrona zapisu rewizji i referencji; jedno complete jako granica zapisu. Stan etapów pochodzi z silnika |
| [ChangeState](src/main/java/org/example/processlab/workflow/ChangeState.java), [StateCodec](src/main/java/org/example/processlab/workflow/StateCodec.java) | Jeden JSON konkretnego typu rekordu w zmiennej caseState; niezmienna migawka, upoważnienie do propozycji, potwierdzenia wykonanych komend i podstawa odbioru. Brak drugiej bazy i natywnej deserializacji Javy |
| [WorkflowChecks](src/main/java/org/example/processlab/workflow/WorkflowChecks.java), [QualificationStep](src/main/java/org/example/processlab/workflow/QualificationStep.java) | Dobór trzech kontroli do zakresu tej sprawy; użycie reguł F3 i DMN w synchronicznej kontynuacji BPMN. Sama kwalifikacja nie akceptuje produktu |
| [ChangeTrial](src/main/java/org/example/processlab/workflow/ChangeTrial.java), [EngineSession](src/main/java/org/example/processlab/engine/EngineSession.java) | Złożenie zależności, przypięcie wdrożeń, jawne beans i historie BPMN/DMN, zamknięcie zasobów. H2 nadal w pamięci |

Fasada kontroluje istnienie referencji dowodów, ponieważ migawka analityczna F3 celowo toleruje brakujące dane i daje UNKNOWN. Bez kontroli na wejściu można było zapisać PASS „na przyszłość” i wykorzystać go po późniejszym utworzeniu rewizji. F4 nie zmienia znaczenia UNKNOWN w F3 — ogranicza przyjmowanie wyników do rzeczywiście istniejącego materiału tej symulacji.

Przygotowanie w tym wąskim modelu tworzy nową rewizję testu i programu, a zależność wybranego testu opisuje wobec bieżącego wybranego wymagania. Nie jest to ogólny edytor dowolnego grafu modułów. Zakres pozostałych zależności i dobór sprawdzeń nadal wymagają analizy; nie przenosić tej operacji bezpośrednio do projektu wielomodułowego.

### Testy i dowody

| Kontrola | Wynik rzeczywisty | Dowód |
| --- | --- | --- |
| Pierwszy RED F4 | 48 testów łącznie: 10 nowych porażek asercji, 38 wcześniejszych PASS, 0 błędów wykonania | [f4-red.log](evidence/f4-red.log), [szkielety i początkowy BPMN](evidence/f4-red-sources.json) |
| Wykryty brak historii DMN | 48 testów, 1 porażka: udane wykonanie nie dopisywało historii DMN | [f4-dmn-history-red.log](evidence/f4-dmn-history-red.log). Włączono historię jawnie; nie przyjęto porównania pustej historii przed/po za wystarczający dowód rollbacku |
| RED ustalenia recenzenta R-F4-02 | 2 testy, 2 porażki asercji, 0 błędów | [f4-future-evidence-red.log](evidence/f4-future-evidence-red.log). Wyniki dla nieistniejącej rewizji przyjmował Assess i import początkowy |
| RED czytelności propozycji | 1 test, 1 porażka; raport nie pokazywał rewizji propozycji przed zgodą | [f4-proposal-view-red.log](evidence/f4-proposal-view-red.log), poprawiony widok w demo |
| GREEN i regresja | 51/51 PASS: 13 testów F4 + 38 F2/F3; offline clean verify i zbudowany JAR | [f4-green.log](evidence/f4-green.log), [ChangeProcessTest](src/test/java/org/example/processlab/ChangeProcessTest.java) |
| RED odtworzony na kopii | 13 testów F4, 13 porażek asercji, 0 błędów | [f4-red-replay.json](evidence/f4-red-replay.json), [log](evidence/f4-red-replay.log). Końcowy zestaw ma trzy dodatkowe testy względem pierwszego RED |
| Wybrane uszkodzenia | 12/12 wykrytych przez asercje, bez błędów wykonania i pominięć | [f4-faults.json](evidence/f4-faults.json) zawiera konkretne nazwy testów, liczby i ścieżki logów. To wybrane błędy, nie dowód wszystkich możliwych stanów |
| Eksport przebiegu | Pięć odczytów po rzeczywistych komendach dwóch instancji, poprzedni odbiór bez zmian | [f4-demo.md](evidence/f4-demo.md), wygenerowany testem F4_09 również w końcowym verify |

Test F4_06 wstrzykuje wyjątek po zakończeniu synchronicznej aktywności qualify. Potem ponownie odpytuje silnik: JSON migawki/potwierdzenia poleceń, aktywne zadania, historyczne zakończenia zadań, szczegóły historii i historię DMN. Wszystko odpowiada stanowi sprzed komendy. Po usunięciu awarii to samo commandId działa jeden raz. Dodatkowy mutant zapisuje migawkę osobną transakcją przed complete — test wykrywa rozdzielenie zapisu. Nie badano awarii zasilania ani konkurujących klientów.

**Granica mutanta task-id:** jego wykrycie wynika z różnicy typu odmowy (IllegalArgumentException fasady wobec FlowableObjectNotFoundException silnika). Silnik nadal odrzuca stare zadanie. Ta próba potwierdza kontrolę fasady, nie wykazanie niewłaściwego skutku domenowego; 12/12 oznacza wykrycie przez asercje, a nie dwanaście naruszeń skutków procesu.

Pozostałe uszkodzenia dotyczą: roli, wersji stanu, commandId, processId, taskId, pominięcia zadania zgody, pozostawienia dawnego upoważnienia po nowej propozycji, skierowania CORRECTION do odbioru, wyłączenia historii DMN oraz dopuszczenia przyszłych referencji przeglądu/wykonania. Każda próba działa na osobnej kopii; źródła robocze pozostają bez zmian.

### Odtworzenie i obejrzenie przebiegu

Z katalogu próby po przygotowaniu środowiska F2:

```sh
./verify -o clean verify
./verify -o -Dtest=ChangeProcessTest#F4_09_exportsExecutedScenario -Ddemo.output=evidence/f4-demo.md test
/usr/bin/python3 verify-workflow.py --red
/usr/bin/python3 verify-workflow.py
```

Drugie polecenie odtwarza scenariusz i zapisuje raport do przeczytania od punktu 1. Pozostałe dwa wykonują negatywne próby na kopiach i zapisują logi/JSON w evidence/. Kod 0 odtwarzacza oznacza wykrycie wybranych usterek; błąd kompilacji/infrastruktury nie jest sukcesem. Dane H2 znikają po zamknięciu silnika; trwały jest eksport oraz kod/testy. Nie wymaga się żadnej dawnej ścieżki tymczasowej. Operacje operatora w testach są fikcyjnymi wejściami scenariusza, nie zgodą właściciela projektu.

Odtwarzanie F3 nadal wybiera jego 38 testów, mimo dodania F4. Dostosowano wyłącznie zgodność szkieletu z rozszerzonym API oraz filtr testów; pierwotne szkielety zachowano. Nie zastąpiono dowodu pierwszego RED nowym uruchomieniem. Po F4 ponowiono odtwarzanie F3 (38 testów / 32 porażki asercji / 0 błędów) i 14/14 wybranych mutacji oraz odtwarzanie pięciu testów F2.

### Przegląd i ograniczenia

Osobny recenzent review_flowable_f4 przeczytał kontrakt przed kodem i zaproponował własne kontrprzykłady. R-F4-01 usunął niejednoznaczność priorytetów fail/UNKNOWN/CONFLICT przed implementacją. R-F4-02 ujawnił przyjmowanie przyszłych dowodów; po RED i poprawce recenzent potwierdził zamknięcie. Poprawiono również maskowany test obcej instancji, tak aby rola i operacja były poprawne, a odmowę powodował sam obcy processId. Recenzent odczytuje kod/logi; nie uruchamiał testów samodzielnie ani nie wystawiał VER/VAL/ACC. Końcowy odczyt eksportu i prób uszkodzeń zakończył recenzję: brak otwartych blokerów F4 w tej granicy.

Silnik przejął prowadzenie zadań, synchroniczne przejścia, transakcję i historię; własny kod nadal utrzymuje znaczenie danych, rewizji, poleceń i zgód w fabule. Koszt tego przekroju to dodatkowy BPMN, fasada, rekord stanu/codec, kompozycja i testy integracyjne. F4 potwierdza wykonalność tego podziału, nie przewagę kosztową nad prostym rdzeniem Python ani przydatność dla operatora. Nie wykonano benchmarku, prognozy prac ani pełnego badania kombinacji.

Źródła: [Flowable — konfiguracja i transakcje standalone](https://www.flowable.com/open-source/docs/bpmn/ch03-Configuration/), [BPMN constructs](https://www.flowable.com/open-source/docs/bpmn/ch07b-BPMN-Constructs/) oraz [TaskService 8.0.0](https://github.com/flowable/flowable-engine/blob/0779d68e5a3385b74d8acb8bc37901ff54513249/modules/flowable-engine/src/main/java/org/flowable/engine/TaskService.java). Dowodem zachowania tego zestawu są testy, nie sama dokumentacja producenta.

Dalsza praca to F5: trwałość po zakończeniu JVM i wznowienie przez nowy proces oraz ocena widoku. Ten etap wymaga osobnego zlecenia. Nie zmieniono template/, W5/E9, Kitchen ani iso-model-state. Nie wykonano commita/pushu.

Historyczne źródła/testy/POM i odtwarzacze F4 identyfikuje [f4-inputs.sha256](evidence/f4-inputs.sha256); sprawdzenie tych sum wymaga stanu commita 8fa127b; F5 zmienia EngineSession/ChangeTrial i odtwarzacz F4. Bieżące sumy są w evidence/f5-inputs.sha256.

Kontrola zapisu F4: [make check](evidence/f4-repository-check.log) — kod 0, 263 elementy, 0 błędów; znane W1 MIG-01/02 i W2 D-92–97 bez commitów. [Kontrola odnośników](evidence/f4-document-check.json): sprawdzono 147 lokalnych ścieżek w pięciu dokumentach, brak brakujących plików. Sprawdzenie sum bieżących wejść i `git diff --check` zakończone bez błędów. Testów dystrybucji nie ponawiano: template/ nie zmieniano.


## F5 — kontrakt przed kodem (D-99, 2026-11-06)

**A16 — decyzja agenta:** rozdzielić jawne utworzenie bazy od ponownego otwarcia. H2 plikowe w katalogu wskazanym dla próby; wznowienie wymaga istniejącego pliku (IFEXISTS), nie wdraża ponownie modeli i nie inicjuje danych. Przy wznowieniu oczekujemy dokładnie jednej definicji BPMN i DMN oraz zgodności zapisanych XML z zasobami tej wersji programu. Reopen używa schemaUpdate=false. Wznowienie dotyczy tego samego przypiętego buildu; zgodność XML nie dowodzi kompatybilności innego kodu Java/codec. Inna/niejednoznaczna konfiguracja daje odmowę, nie wybór latest ani migrację. To ograniczenie jednej próby, nie ogólny katalog wersji. Odczyt nie dopisuje domenowych wyników, poleceń, zadań ani historii DMN; silnik może aktualizować swoje metadane techniczne.

Minimalna zmiana: wspólna konfiguracja EngineSession z wariantem URL i tworzenia schematu; ChangeTrial create/reopen z publicznych usług repozytorium. Bez nowej bazy domenowej, serwera, zależności czy manifestów wejść. Stan sprawy nadal w caseState; etapy w BPMN. Podstawa techniczna: [Flowable Configuration](https://www.flowable.com/open-source/docs/bpmn/ch03-Configuration), [H2: istniejąca baza](https://www.h2database.com/html/features.html#database_only_if_exists); zachowanie sprawdzimy na przypiętym Flowable 8.0.0/H2 2.4.240.

| Próba | Oczekiwanie / dowód |
| --- | --- |
| F5-01 Zamknięcie JVM i nowa JVM | Ta sama instancja, taskId, rewizje, polecenia, historia zadań/DMN i definicje. Każda faza osobnym procesem z potwierdzonym wyjściem; dane tylko z plikowej bazy, nie z przekazanego JSON |
| F5-02 Wznowienie i kontynuacja | Po restarcie negatywny przegląd kieruje do korekty; nowe rewizje i wyniki dają oczekujące zadanie operatora, bez odbioru. Stare dowody pozostają; ponowienie wcześniej skutecznej komendy odrzucone bez zmiany stanu |
| F5-03 Historyczny odbiór i następca | Jawny fikcyjny odbiór, następna sprawa i kolejny restart: poprzedni odbiór niezmieniony, następca wskazuje poprzednika i oczekuje nowej zgody |
| F5-04 Błędny katalog lub model | Reopen nieistniejącej bazy odmawia bez utworzenia pustej; create istniejącej odmawia bez nadpisania. Inna treść modelu lub dodatkowa definicja daje odmowę, nie automatyczną migrację |
| F5-05 Widok z bazy | Raport pokazuje stan, konkretną podstawę, wyniki i oczekującą decyzję bez XML. Dwukrotny odczyt nie tworzy nowych zadań, ocen/odbioru, definicji lub historii DMN |
| F5-06 Odtworzenie i ocena | Osobny recenzent odtwarza próbę z trwałej instrukcji; raport oddziela mechanizmy silnika, własny kod i luki. Ocena zrozumienia/użyteczności przez operatora pozostaje do obserwacji, nie jest zaliczana testami |

Kolejność: kontrakt → osobny przegląd → kompilujący się RED → minimalne GREEN → pełna regresja i wybrane celowe usterki → odtworzenie przez recenzenta → raport i punkt wznowienia. Nie badamy przerwania prądu, awarii dysku, backupu, wielu piszących klientów ani migracji modeli/formatu caseState. Próba restartu oznacza poprawne zamknięcie procesu JVM.

### F5 — jak odtworzyć i obejrzeć próbę

W katalogu tego README, na przygotowanym środowisku F2, bez pobierania nowych zależności:

```sh
./verify -o clean verify -Drestart.output=evidence/f5-restart
python3 verify-persistence.py --red
python3 verify-persistence.py
```

Pierwsze polecenie uruchamia całą regresję. PersistentTrialTest uruchamia **10 osobnych JVM** i czeka na ich wyjście. Następna JVM dostaje jedynie fazę, ścieżkę bazy i ścieżkę eksportu — nie dostaje stanu poprzednika. Eksportowane JSON-y zawierają tożsamości, treść stanu/historii i PID; pliki Markdown pochodzą z usług silnika. Test porównuje pełne zapisane dane przy każdym `show`. Wybrane usterki i RED są uruchamiane na tworzonych przez skrypt kopiach; instrukcja nie zależy od zachowanej ścieżki tymczasowej.

**Demo ręczne — każda linia kończy JVM, następna ją uruchamia od nowa:**

```sh
./resume-demo create moja-proba
./resume-demo show moja-proba
./resume-demo apply moja-proba
./resume-demo fail moja-proba
./resume-demo correct moja-proba
./resume-demo show moja-proba
```

- `create`: tworzy nową bazę i fikcyjną propozycję zmiany; oczekuje zgody w scenariuszu.
- `apply`: odgrywa zgodę w fabule, zastosowanie zmiany i przygotowanie materiałów; oczekuje sprawdzeń.
- `fail`: wpisuje fikcyjny negatywny przegląd testu przy pozytywnym wyniku wykonania; kieruje do korekty.
- `correct`: odgrywa poprawkę i nowe oceny, a także sprawdza odmowę powtórzonego ID polecenia; oczekuje odbioru.
- `show`: odczytuje bieżący stan bez wykonywania powyższych działań. Tutaj zatrzymaj się, żeby ocenić raport.

Otwórz `.runs/moja-proba/show.json.md`. Baza to `.runs/moja-proba/process.mv.db`; raport jej nie zastępuje. Możesz zakończyć terminal i później ponowić `show`. `create` z tą samą nazwą odmawia; nową próbę rozpocznij pod inną nazwą. Skrypt działa lokalnie, na testowym classpath (H2 ma zakres test); nie jest instalowanym CLI do prowadzenia rzeczywistego projektu. JAR nie jest samodzielną aplikacją.

Dodatkowe `./resume-demo accept-next moja-proba` **jawnie odgrywa fikcyjny odbiór** i tworzy następną sprawę. Potem `show` pokaże oba stany. To nie akceptacja procesu przez użytkownika ani rzeczywistego produktu. Nie ma tu automatycznego przypisywania milczeniu zgody.

Podczas oceny raportu operator powinien móc własnymi słowami wskazać: co obecnie czeka, której rewizji dotyczy, co już sprawdzono, kto wykonuje następny krok i czy nastąpił odbiór. Wynik tej obserwacji zapisujemy dopiero po odpowiedzi — nie wynika z 58 zielonych testów. Próg czasu wznowienia ani sukces użytkowy nie są tu z góry zadeklarowane.


Uwaga środowiskowa z odtworzenia 2026-11-06: lokalny Homebrew Python 3.14 ma niespójne libexpat; narzędzia czytające XML uruchomiono przez `/usr/bin/python3` (3.9.6, sprawdzony parser). To nie RED produktu. Nie naprawiano instalacji systemowej. Na innym środowisku wybierz działający Python 3.9+ z modułem ElementTree. Demo korzysta z już dostępnego Surefire i jawnego `-Dtest=DemoCommand`, bez dodatkowego pluginu Maven do budowania classpath. DemoCommand jest wejściem scenariusza, nie asercją zaliczającą regresję; domyślny wzorzec testów go nie wybiera.


Jak czytać upoważnienie po wykonaniu zmiany: „brak aktywnego upoważnienia” oznacza, że nie ma zgody do ponownego wykorzystania. Historyczna zgoda ALLOW i jej wykorzystanie APPLY są w sekcji poleceń. Nie oznacza to, że wcześniej wykonano zmianę bez zgody; późniejszy odbiór nadal jest osobną czynnością.

## Czytelna karta operatora — A-10

Karta powstaje z istniejącego eksportu JSON. Nie otwiera bazy ani nie wykonuje poleceń procesu. To **odczyt archiwalny**, nie widok na żywo. Potrzebne jest to samo lokalne JDK i środowisko Maven co do `./verify`; polecenie działa offline, bez nowych zależności.

Z katalogu `reference/process-map/flowable-trial/`:

```sh
./show-card evidence/f5-restart/05-fail.json first
./show-card evidence/f5-restart/07-show.json first
./show-card evidence/f5-restart/10-show.json next
```

Czytaj od „Teraz”: kto ma pracować i dlaczego, następnie zakres i kontrole. Historia i techniczne ID są niżej. Dla nowej zmiany karta oddziela zadanie zgody w silniku od zalecanej analizy agenta poza workflow. Raport nie zapisuje Twojej odpowiedzi ani odbioru.

Gotowe wyniki: [korekta testu](evidence/operator-card/05-fail.md), [decyzja w ćwiczeniu](evidence/operator-card/07-show.md), [nowa propozycja](evidence/operator-card/10-show.md). [Opis realizacji i dowody](evidence/operator-card/README.md), [mapa pól i kryteria](../operator-preview/textstats-card-data-map.md).

Można również podać istniejący eksport `.runs/NAZWA/show.json` oraz `first` lub `next`. Karta opisuje moment zapisany w tym pliku; samo jej wyświetlenie nie odświeża eksportu. Nie trzeba odgrywać `accept-next`, żeby obejrzeć dostarczone trzy przykłady.

Skrypt używa jawnej komendy `OperatorCardCommand` przez istniejący Surefire, analogicznie do `resume-demo`. Nie jest ona częścią regresji ani dowodem jakości karty. Pliki pomocnicze są w ignorowanym `target/card-*`; standardowe wyjście zawiera sam raport. Parser/formatter są w `src/main/java/.../report/`; reguły pochodzą z niezmienionego `WorkflowChecks`/`Rules`. Nie ma zależności od pamięci rozmowy ani zachowania katalogu tymczasowego.
