# Słownik pojęć szablonu (warstwa procesu)

Pojęcia, których używają wymagania szablonu (spec/requirements.md, D-59). Dziedziną warstwy procesu jest sam proces, więc są tu pojęcia procesu; pojęcia produktu klienta należą do słownika projektu (D-57). Tytuł podaje w nawiasie angielską nazwę z wymagań EARS (E6).

## Pojęcia

### G-ART-01 Element (Element)
- definition: zapis w pliku artefaktu z ID według schematu typu w modelu śledzalności; ma pola i co najwyżej wskazuje rodziców
- changed_by: D-06
- status: initiated

### G-ART-02 Rodzic (Parent)
- definition: element wskazany przez dziecko w polu rodzica określonym w modelu śledzalności (P-03)
- distinct_from: G-ART-01
- changed_by: D-06
- status: initiated

### G-ART-03 Identyfikator (ID)
- definition: niezmienny znacznik elementu zgodny ze wzorcem typu, nigdy nieużywany ponownie
- changed_by: D-05
- status: initiated

### G-ART-04 Wymaganie (Requirement)
- definition: element typu REQ: jedno zdanie EARS z dokładnie jednym „shall” i źródłem
- changed_by: D-01
- status: initiated

### G-ART-05 EARS (EARS)
- definition: składnia wymagań z sześcioma wzorcami (ubiquitous, event, state, unwanted, optional, complex)
- changed_by: D-01
- status: initiated

### G-ART-06 Słownik (Glossary)
- definition: plik pojęć, którego nazwy angielskie są jedynymi dozwolonymi słowami pisanymi wielką literą w wymaganiach
- changed_by: D-01
- status: initiated

### G-ART-07 Produkt pracy (Work Product)
- definition: element typu oznaczonego jako produkt; ma obowiązkowy stan initiated, verified albo approved
- changed_by: D-11
- status: initiated

### G-ART-08 Rekord weryfikacji (Verification Record)
- definition: element typu VER z datą, wynikiem pass albo fail i weryfikowanymi elementami albo przedmiotem
- changed_by: D-12
- status: initiated

### G-ART-09 Test akceptacyjny (Acceptance Test)
- definition: element typu AT: scenariusz z tagiem, polem verifies i opcjonalnym runner do testu automatycznego
- changed_by: D-60
- status: initiated

### G-ART-10 Lista kontrolna (Checklist)
- definition: sekcja checklist.md z ponumerowanymi punktami przeglądu; rekord weryfikacji wskazuje listę i niespełnione punkty
- changed_by: D-31
- status: initiated

### G-ART-11 Kamień milowy (Milestone)
- definition: element planu typu MS z terminem i opcjonalnym tagiem, który oznacza osiągnięcie
- changed_by: D-16
- status: initiated

### G-ART-12 Decyzja (Decision)
- definition: element typu D w rejestrze decyzji z opcjami, propozycją i wyborem Użytkownika
- changed_by: D-01
- status: initiated

### G-ART-13 Rejestr decyzji (Decision Register)
- definition: plik decyzji i kolejki tematów, pamięć projektu między sesjami
- changed_by: D-01
- status: initiated

### G-NAR-01 Model śledzalności (Traceability Model)
- definition: plik reguł z typami, schematami ID, polami rodziców, pokryciem i stanami, z którego czytają wszystkie narzędzia
- changed_by: D-06
- status: initiated

### G-NAR-02 Macierz śladu (Trace Matrix)
- definition: plik generowany z pól rodziców, pokazujący powiązania w górę i w dół
- changed_by: D-06
- status: initiated

### G-NAR-03 Rekord postępu (Progress Record)
- definition: plik generowany z planu, rekordów i tagów, pokazujący stan kamieni, zadań i produktów
- changed_by: D-10
- status: initiated

### G-NAR-04 Strona zgodności (Compliance Page)
- definition: plik generowany z modelu śledzalności i danych normy, pokazujący pokrycie produktów pracy ISO/IEC 29110
- changed_by: D-25
- status: initiated

### G-REP-01 Commit (Commit)
- definition: zapis zmiany w repozytorium git; jeden na odpowiedź Użytkownika
- changed_by: D-01
- status: initiated

### G-REP-02 Opis commita (Commit Message)
- definition: tekst commita, który wskazuje co najmniej jedno istniejące ID
- distinct_from: G-REP-01
- changed_by: D-26
- status: initiated

### G-REP-03 Kopia zapasowa (Backup Remote)
- definition: drugie repozytorium git, do którego idą commity i tagi i z którego da się odtworzyć repozytorium
- changed_by: D-13
- status: initiated

### G-DST-01 Pakiet procesu (Process Package)
- definition: katalog process/ dostarczany i aktualizowany przez copier: reguły, narzędzia, hooki, moduły, wzorce dokumentów
- changed_by: D-47
- status: initiated

### G-DST-02 Projekt (Project)
- definition: repozytorium utworzone z szablonu, które ma własne dokumenty, rejestr i rekordy
- distinct_from: G-DST-01
- changed_by: D-43
- status: initiated

### G-DST-03 Plik copiera (Answers File)
- definition: plik zapisany przez copier w projekcie z wersją szablonu i odpowiedziami
- changed_by: D-53
- status: initiated

### G-DST-04 Tag wydania (Release Tag)
- definition: nieprzesuwany tag postaci vX.Y.Z na przetestowanym commicie szablonu
- changed_by: D-49
- status: initiated

### G-DST-05 Wzorzec dokumentu (Document Template)
- definition: pusty plik w pakiecie procesu, z którego powstaje dokument projektu; nowa wersja wzorca nie zmienia wcześniejszych kopii
- changed_by: D-47
- status: initiated

### G-DST-06 Migracja (Migration)
- definition: opisany w wydaniu krok dostosowania istniejących dokumentów projektu do zmienionych reguł, wykonywany osobno od aktualizacji pakietu
- changed_by: D-51
- status: initiated
