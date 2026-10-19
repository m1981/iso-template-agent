Feature: Szablon procesu (Process kit)

  Testy akceptacyjne wymagań szablonu (spec/requirements.md, D-59, D-60). Pole runner: wskazuje
  przypadek testu automatycznego (plik::przypadek); make test-report uruchamia go i zapisuje wynik.
  Testy bez runner: są ręczne i ocenia je przegląd (rekord VER).

  @AT-01
  # verifies: TRC-02
  # runner: tools/test_tools.py::breakage-01, tools/test_tools.py::breakage-02, tools/test_tools.py::breakage-10, tools/test_tools.py::breakage-21
  # status: initiated
  Scenario: Brak pola albo rodzica
    Given plik z elementem bez wymaganego pola, np. przypadek użycia bez scenarios: i scope:
    When trace.py sprawdza ślad
    Then wynik ma błąd E1 i kod wyjścia 1

  @AT-02
  # verifies: TRC-03
  # runner: tools/test_tools.py::breakage-03, tools/test_tools.py::id-in-text
  # status: initiated
  Scenario: Nieznany rodzic i nieznane ID w tekście
    Given wymaganie, którego source: wskazuje nieistniejący przypadek użycia, i tekst z nieistniejącym wymaganiem z istniejącego obszaru
    When trace.py sprawdza ślad
    Then wynik ma błąd E2 dla obu odwołań

  @AT-03
  # verifies: TRC-04
  # runner: tools/test_tools.py::breakage-04
  # status: initiated
  Scenario: Zdublowane ID
    Given dwie pozycje zakresu z tym samym ID
    When trace.py sprawdza ślad
    Then wynik ma błąd E3 z obiema lokalizacjami

  @AT-04
  # verifies: TRC-05
  # runner: tools/test_tools.py::breakage-05, tools/test_tools.py::breakage-12, tools/test_tools.py::breakage-13, tools/test_tools.py::breakage-20
  # status: initiated
  Scenario: Wartość spoza dozwolonych
    Given status draft, result ok, status brief i quality speed
    When trace.py sprawdza ślad
    Then każda wartość daje błąd E4

  @AT-05
  # verifies: TRC-06
  # runner: tools/test_tools.py::breakage-06
  # status: initiated
  Scenario: Składnia EARS
    Given wymaganie z dwoma „shall”
    When trace.py sprawdza ślad
    Then wynik ma błąd E5

  @AT-06
  # verifies: TRC-07
  # runner: tools/test_tools.py::breakage-07
  # status: initiated
  Scenario: Pojęcie spoza słownika
    Given wymaganie ze słowem Archive, którego nie ma w słowniku
    When trace.py sprawdza ślad
    Then wynik ma błąd E6

  @AT-07
  # verifies: TRC-08
  # runner: tools/test_tools.py::breakage-08, tools/test_tools.py::breakage-14, tools/test_tools.py::breakage-15, tools/test_tools.py::breakage-16
  # status: initiated
  Scenario: Rodzic niedozwolonego typu
    Given wymaganie z rodzicem typu scenka, korekta z przyczyną typu przypadek użycia, przypadek użycia z pozycją zakresu w scenarios: i z pozycją Out w scope:
    When trace.py sprawdza ślad
    Then każdy przypadek daje błąd E7

  @AT-08
  # verifies: TRC-09
  # runner: tools/test_tools.py::breakage-09
  # status: initiated
  Scenario: Brak wymaganego pokrycia
    Given ryzyko bez wymagania przy pokryciu na poziomie error
    When trace.py sprawdza ślad
    Then wynik ma błąd E8

  @AT-09
  # verifies: TRC-10
  # runner: tools/test_tools.py::chain, tools/test_tools.py::chain-no-warnings
  # status: initiated
  Scenario: Macierz w obie strony
    Given łańcuch wszystkich typów, w którym tylko dzieci wskazują rodziców
    When trace.py generuje trace.md
    Then trace.md pokazuje wymaganie z rodzicem (przypadkiem użycia) w tabeli w górę i z dzieckiem (testem) w tabeli w dół

  @AT-10
  # verifies: TRC-11
  # runner: tools/test_tools.py::warning-04, tools/test_tools.py::warning-05, tools/test_tools.py::extension-point
  # status: initiated
  Scenario: Nieznane pole
    Given ryzyko z polem źródło: i ryzyko projektu z polem działanie:
    When trace.py sprawdza ślad
    Then wynik ma ostrzeżenie W4, a punkt rozszerzenia „3a.” nie jest polem

  @AT-11
  # verifies: TRC-12
  # runner: tools/test_tools.py::warning-01, tools/test_tools.py::warning-02, tools/test_tools.py::w3-with-record
  # status: initiated
  Scenario: Stan verified bez rekordu
    Given wymaganie w stanie verified bez rekordu VER pass
    When trace.py sprawdza ślad
    Then wynik ma ostrzeżenie W3, a dla przypadku użycia z rekordem VER pass go nie ma

  @AT-12
  # verifies: TRC-13
  # runner: tools/test_tools.py::w5
  # status: initiated
  Scenario: Zmiana rodzica po weryfikacji
    Given przypadek użycia zweryfikowany rekordem VER pass i późniejsza zmiana treści jego scenki
    When trace.py sprawdza ślad
    Then wynik ma ostrzeżenie W5 dla przypadku użycia, a sama zmiana stanu scenki go nie daje

  @AT-13
  # verifies: TRC-14
  # runner: tools/test_tools.py::toml-fallback
  # status: initiated
  Scenario: Parser zastępczy TOML
    Given id.toml, iso29110.toml i plik z napisami zawierającymi \\, # i ]
    When parser zastępczy i tomllib czytają te pliki
    Then wyniki są równe, a błąd podaje numer linii

  @AT-14
  # verifies: TRC-15
  # runner: tools/test_tools.py::id-in-text
  # status: initiated
  Scenario: Tekst w kształcie ID
    Given tekst z nazwą algorytmu i kodowania, liczbą trzycyfrową po kodzie typu i kodem typu w środku słowa
    When trace.py sprawdza ślad
    Then nie ma błędu

  @AT-15
  # verifies: TRC-16
  # runner: tools/test_tools.py::heading-colon
  # status: initiated
  Scenario: Dwukropek po ID w nagłówku
    Given nagłówek „### UC-nn: Tytuł”
    When trace.py sprawdza ślad
    Then komunikat wskazuje dwukropek

  @AT-16
  # verifies: TRC-17
  # runner: tools/test_tools.py::feature-untagged
  # status: initiated
  Scenario: Scenariusz bez tagu
    Given scenariusz bez tagu po teście z tagiem, z własnymi komentarzami pól
    When trace.py sprawdza ślad
    Then pola testu z tagiem się nie zmieniają

  @AT-17
  # verifies: TRC-19
  # runner: tools/test_tools.py::nav-orphan
  # status: initiated
  Scenario: Ekran bez krawędzi
    Given nowy ekran bez żadnej krawędzi na mapie nawigacji
    When reguły mapy sprawdzają mapę
    Then wynik wymienia ten ekran i ma kod różny od 0

  @AT-18
  # verifies: HKS-01
  # runner: tools/test_tools.py::precommit-trace
  # status: initiated
  Scenario: Nieaktualna macierz blokuje commit
    Given trace.md zmieniony ręcznie
    When Użytkownik robi commit
    Then pre-commit odrzuca commit

  @AT-19
  # verifies: HKS-02
  # runner: tools/test_tools.py::commit-msg
  # status: initiated
  Scenario: Opis commita bez ID
    Given opis „bez identyfikatora” oraz opis, w którym istniejące ID jest tylko pod linią nożyczek
    When Użytkownik robi commit
    Then commit-msg odrzuca oba, a przyjmuje opis z istniejącym ID przy core.commentChar „;”

  @AT-20
  # verifies: HKS-03
  # runner: tools/test_tools.py::precommit-progress, tools/test_tools.py::precommit-iso-map
  # status: initiated
  Scenario: Nieaktualny postęp albo strona zgodności
    Given nowy tag baseline bez odświeżonego progress.md albo ręcznie zmieniony iso-map.html
    When Użytkownik robi commit
    Then pre-commit odrzuca commit

  @AT-21
  # verifies: HKS-04
  # runner: tools/test_distribution.py::hooks
  # status: initiated
  Scenario: Inny menedżer hooków
    Given core.hooksPath ustawiony na .husky
    When Użytkownik uruchamia make hooks
    Then polecenie kończy się błędem, a core.hooksPath zostaje .husky

  @AT-22
  # verifies: SEP-01
  # runner: tools/test_tools.py::e9-1, tools/test_tools.py::e9-2, tools/test_tools.py::e9-3, tools/test_tools.py::e9-4, tools/test_tools.py::e9-5, tools/test_tools.py::e9-6, tools/test_tools.py::e9-7
  # status: initiated
  Scenario: Autor nie weryfikuje sam siebie
    Given tablica decyzyjna: rekord nowy albo stary, wynik pass albo fail, element zmieniony albo nie, nowy element, sama zmiana stanu, rekord kopii
    When Użytkownik robi commit
    Then commit jest odrzucony z E9 tylko w przypadkach 1 i 5

  @AT-23
  # verifies: SEP-02
  # runner: tools/test_tools.py::e9-import
  # status: initiated
  Scenario: Pierwszy commit repozytorium
    Given repozytorium bez historii z rekordami VER pass
    When Użytkownik robi pierwszy commit
    Then commit przechodzi

  @AT-24
  # verifies: PLN-01
  # runner: tools/test_tools.py::progress
  # status: initiated
  Scenario: Rekord postępu
    Given plan z kamieniem i zadaniem, korekta i odbiór kamienia
    When progress.py generuje progress.md
    Then progress.md ma wiersze kamienia, zadania, korekty i stanów produktów

  @AT-25
  # verifies: PLN-02
  # runner: tools/test_tools.py::precommit-progress
  # status: initiated
  Scenario: Osiągnięty kamień
    Given tag baseline z pola tag: kamienia
    When progress.py generuje progress.md
    Then kamień jest oznaczony jako osiągnięty

  @AT-26
  # verifies: PLN-03
  # runner: tools/test_tools.py::breakage-11
  # status: initiated
  Scenario: Wpis produces:
    Given zadanie z produces: „przypadki”
    When trace.py sprawdza ślad
    Then wynik ma błąd E4

  @AT-27
  # verifies: REC-01
  # runner: tools/test_tools.py::breakage-17, tools/test_tools.py::breakage-19
  # status: initiated
  Scenario: Nieznana lista albo punkt
    Given rekord VER z checklist: XYZ albo failed: REQ.99
    When trace.py sprawdza ślad
    Then wynik ma błąd E4

  @AT-28
  # verifies: REC-02
  # runner: tools/test_tools.py::breakage-18
  # status: initiated
  Scenario: Wynik pass z niespełnionym punktem
    Given rekord VER z result: pass i failed: UC.3
    When trace.py sprawdza ślad
    Then wynik ma błąd E4

  @AT-29
  # verifies: REP-01
  # runner: tools/test_tools.py::restore-check
  # status: initiated
  Scenario: Odtworzenie z kopii
    Given lokalne repozytorium wypchnięte do kopii i tag tylko lokalny
    When restore_check.py sprawdza kopię
    Then na świeżej kopii wynik pass, a tag tylko lokalny daje fail REPO.2

  @AT-30
  # verifies: REP-02
  # runner: tools/test_tools.py::restore-check
  # status: initiated
  Scenario: Rekord odtworzenia
    Given restore_check.py z opcją --record
    When sprawdzenie się kończy
    Then verification.md ma rekord VER z subject: repository bez błędów śladu

  @AT-31
  # verifies: ISO-01
  # runner: tools/test_tools.py::iso-map
  # status: initiated
  Scenario: Strona zgodności
    Given model śledzalności z polami iso i dane normy
    When iso_map.py generuje iso-map.html
    Then strona ma wiersz WP.10 Project plan i etykiety reguł śladu

  @AT-32
  # verifies: INI-01
  # runner: tools/test_tools.py::new-project
  # status: initiated
  Scenario: Odmowa startu projektu
    Given niezacommitowana zmiana albo projekt już założony
    When Użytkownik uruchamia make new-project
    Then polecenie odmawia

  @AT-33
  # verifies: INI-02
  # runner: tools/test_tools.py::new-project
  # status: initiated
  Scenario: Start projektu
    Given czyste repozytorium z kopii szablonu
    When Użytkownik uruchamia make new-project
    Then decisions.md, trace.md i progress.md są w archive/template/, a nowy rejestr ma tylko decyzję startu

  @AT-34
  # verifies: INI-03
  # runner: tools/test_tools.py::template-copy, tools/test_tools.py::first-commit
  # status: initiated
  Scenario: Pierwszy commit kopii
    Given kopia szablonu bez historii gita
    When Użytkownik robi pierwszy commit i start projektu
    Then oba commity przechodzą przez hooki, a kopia nie ma tagów szablonu

  @AT-35
  # verifies: DST-01
  # runner: tools/test_distribution.py::copy
  # status: initiated
  Scenario: Copier dostarcza tylko pakiet
    Given szablon z copier.yml i katalogiem template/process/
    When copier copy tworzy projekt
    Then projekt ma tylko process/ i plik copiera, bez copier.yml

  @AT-36
  # verifies: DST-02
  # runner: tools/test_distribution.py::tags
  # status: initiated
  Scenario: Wersja w pliku copiera
    Given tag baseline-02-proces na commicie wydania v1.1.0
    When bramka aktualizuje projekt do v1.1.0
    Then bramka przechodzi tylko, gdy plik copiera wskazuje v1.1.0

  @AT-37
  # verifies: UPD-01
  # runner: tools/test_distribution.py::version, tools/test_distribution.py::dirty
  # status: initiated
  Scenario: Odmowa przed copierem
    Given wersje 1.1.0, v1.1, latest, HEAD albo niezacommitowana zmiana planu
    When Użytkownik uruchamia make process-update
    Then bramka kończy się kodem 2 i drzewo się nie zmienia

  @AT-38
  # verifies: UPD-02
  # runner: tools/test_distribution.py::conflict, tools/test_distribution.py::markers, tools/test_distribution.py::binary
  # status: initiated
  Scenario: Konflikt mimo kodu 0
    Given lokalna zmiana process/AGENTS.md w linii zmienionej w v1.1.0
    When bramka aktualizuje projekt
    Then copier kończy się kodem 0, a bramka kodem 1 z nazwą pliku w konflikcie

  @AT-39
  # verifies: UPD-03
  # runner: tools/test_distribution.py::scope
  # status: initiated
  Scenario: Zmiana poza pakietem
    Given wydanie v1.3.0, które zmienia README.md projektu
    When bramka aktualizuje projekt
    Then bramka kończy się kodem 1 i wymienia README.md

  @AT-40
  # verifies: UPD-04
  # runner: tools/test_distribution.py::update
  # status: initiated
  Scenario: Pliki projektu bez zmian
    Given projekt z planem, README i ignorowanymi danymi
    When bramka aktualizuje projekt z v1.0.0 do v1.1.0
    Then skróty wszystkich plików poza process/ są takie same, a nowa funkcja działa

  @AT-41
  # verifies: UPD-05
  # runner: tools/test_distribution.py::missing
  # status: initiated
  Scenario: Błąd copiera
    Given wydanie v9.9.9, którego nie ma
    When bramka aktualizuje projekt
    Then bramka zgłasza błąd copiera i kończy się kodem 1

  @AT-42
  # verifies: UPD-06
  # runner: tools/test_distribution.py::validation
  # status: initiated
  Scenario: Walidacja po aktualizacji
    Given dokument w starym formacie, który łamie regułę z v1.1.0
    When bramka aktualizuje projekt
    Then bramka kończy się kodem 1 z odwołaniem do migracji i nic nie commituje

  @AT-43
  # verifies: UPD-07
  # runner: tools/test_distribution.py::repeat
  # status: initiated
  Scenario: Powtórna aktualizacja
    Given projekt już na v1.1.0
    When bramka aktualizuje go do v1.1.0
    Then drzewo się nie zmienia

  @AT-44
  # verifies: UPD-08
  # runner: tools/test_distribution.py::jump
  # status: initiated
  Scenario: Pominięte wydania
    Given projekt na v1.0.0
    When bramka aktualizuje go do v1.2.0
    Then projekt ma zmiany z v1.1.0 i z v1.2.0

  @AT-45
  # verifies: LAY-03
  # runner: tools/test_tools.py::refs
  # status: initiated
  Scenario: Odwołania do ścieżek
    Given dokument z brak/plik.md, wzorcem spec/*.md i wyjątkiem, o którym nikt już nie wspomina
    When check_refs.py sprawdza repozytorium
    Then błąd dla brak/plik.md i dla zbędnego wyjątku, bez błędu dla wzorca

  @AT-46
  # verifies: LEK-01
  # runner: tools/test_tools.py::leak-id
  # status: initiated
  Scenario: Konkretne ID w procesie
    Given plik procesu z numerowanym ID przypadku użycia albo wymagania z obszaru, który projekt ma
    When check_leak.py sprawdza pakiet
    Then błąd dla obu, a nie dla ID zastępczego z „nn”, decyzji szablonu ani nazwy kodowania

  @AT-47
  # verifies: LEK-02
  # runner: tools/test_tools.py::leak-term
  # status: initiated
  Scenario: Pojęcie projektu w procesie
    Given słownik projektu z pojęciem Element (Item) i plik procesu z „Item” albo „element”
    When check_leak.py sprawdza pakiet ze słownikiem
    Then błąd wskazuje pojęcie

  @AT-48
  # verifies: TST-01
  # runner: tools/test_tools.py::breakage-22
  # status: initiated
  Scenario: Runner bez pliku
    Given test AT z runner: tools/brak.py::chain
    When trace.py sprawdza ślad
    Then wynik ma błąd E4

  @AT-49
  # verifies: TST-02
  # runner: tools/test_tools.py::test-report
  # status: initiated
  Scenario: Raport testów
    Given testy z przypadkiem pass, fail, brakującym, z kodem 2 i test ręczny
    When test_report.py tworzy raport
    Then tylko test z samymi przypadkami pass ma wynik pass, a raport kończy się kodem 1

  @AT-52
  # verifies: TRC-18
  # runner: tools/test_tools.py::quality-section
  # status: initiated
  Scenario: Charakterystyki bez wymagań
    Given jedno wymaganie z quality: reliability
    When trace.py generuje trace.md
    Then sekcja charakterystyk ma reliability z liczbą 1 i tym wymaganiem, a security z liczbą 0

  @AT-50
  # verifies: TRC-01
  # status: initiated
  Scenario: Reguły tylko w modelu (przegląd)
    Given narzędzia procesu
    When przegląd kodu szuka schematów ID, pól rodziców i stanów zapisanych poza tools/id.toml
    Then nie ma takich miejsc poza nazwami ról z sekcji [fields]

  @AT-51
  # verifies: LNG-01
  # status: initiated
  Scenario: Warstwa maszynowa po angielsku (przegląd)
    Given kody typów, pola, stany, nazwy plików i kody błędów
    When przegląd według glossary.md, „Terminy procesu”
    Then wszystkie są po angielsku
