# Architektura i dane próby Flowable — F4 z wariantem wznowienia F5

2026-11-05 / aktualizacja 2026-11-06 · D-98/D-99 · dokumentacja istniejącej implementacji. **F5 dodaje wariant plikowej bazy i jawne wznowienie; odbiór użytkowy pozostaje osobny.** Kod źródłowy pozostaje źródłem prawdy; diagramy są jego ręcznie opracowanymi widokami.

Czytaj najpierw **1 → 2 → 3**: otoczenie, wykonanie, odpowiedzialności. Potem wybierz **4** dla zależności kodu, **5** dla śladu produktów albo **6 → 7 → 8** dla danych i poleceń. Strzałki nie określają kolejności pracy, chyba że ich opis mówi o wywołaniu. Przebieg w czasie pokazuje osobno [demo 1–5](evidence/f4-demo.md), a źródłem przejść jest [BPMN](src/main/resources/change.bpmn20.xml).

| Widok | Pytanie |
| --- | --- |
| 1. C4 Context | Kto korzysta z laboratorium i do czego? |
| 2. C4 Container | Co jest wykonywane i gdzie są dane? |
| 3. C4 Component | Który element odpowiada za reguły, zadania i zapis? |
| 4. Zależności kodu | Które pakiety znają inne pakiety/biblioteki? |
| 5. Zależności produktów | Co wiąże wymaganie, przegląd, test i wykonanie? |
| 6. Stan sprawy | Co pamiętamy pomiędzy poleceniami? |
| 7. Migawka produktów | Jak reprezentujemy rewizje i ich dowody? |
| 8. Polecenia | Co wolno przekazać do fasady i jak wskazujemy cel? |

## 1. C4 — kontekst systemu

**Jest jeden operator rzeczywistego laboratorium.** W uruchamianym scenariuszu kod testu podaje fikcyjne role AGENT/OPERATOR i wyniki. Nie ma integracji z sesją LLM ani interaktywnego ekranu decyzji. Testy dotyczą sterowania procesem; nie uruchamiają produktu TextStats.

```mermaid
flowchart LR
    U["Operator laboratorium<br/>[osoba]<br/>Uruchamia scenariusze i czyta raporty"]
    L["Laboratorium procesu<br/>[system]<br/>Lokalna próba zmiany wymagania TextStats"]
    U -->|"Lokalne polecenia i raporty"| L
    classDef person fill:#123e62,color:#fff,stroke:#123e62
    classDef system fill:#216a9e,color:#fff,stroke:#123e62
    class U person
    class L system
```

Źródło: [ChangeProcessTest](src/test/java/org/example/processlab/ChangeProcessTest.java), zwłaszcza F4_09; [instrukcja uruchomienia](README.md).

## 2. C4 — kontenery i miejsca danych

„Kontener” C4 oznacza aplikację albo magazyn danych, nie kontener Docker. H2 pokazano jako osobny magazyn logiczny, **ale jest osadzone w tej samej JVM**. W F4 jest pamięciowe; F5 dodaje bazę plikową, otwieraną kolejno przez nowe JVM. Flowable BPMN i DMN to biblioteki tej aplikacji, nie osobne serwery. Maven uruchamia testową JVM przez Surefire.

```mermaid
flowchart TB
    U["Operator<br/>[osoba]"]
    subgraph LAB["Laboratorium procesu F4/F5 — system"]
        A["Scenariusz i proces<br/>[aplikacja: Java 17 / JUnit / Flowable 8]<br/>Jedna JVM: testy, fasada, BPMN i DMN"]
        H[("Stan silników<br/>[osadzone H2 / JDBC]<br/>F4: pamięć; F5: plik na dysku")]
        F[("Eksporty dowodów<br/>[lokalne pliki evidence]<br/>Raport demo i logi")]
        A -->|"Usługi Flowable / JDBC"| H
        A -->|"Eksport demo: parametr demo.output"| F
    end
    U -->|"verify / Maven Surefire"| A
    U -->|"Czyta raport Markdown"| F
    classDef app fill:#216a9e,color:#fff,stroke:#123e62
    classDef store fill:#e4eff7,color:#173c56,stroke:#216a9e
    class A app
    class H,F store
```

H2 ma w [POM](pom.xml) zakres `test`. Pokazany wariant działa w testach; zbudowany JAR nie jest samodzielną aplikacją z dołączonym sterownikiem. Źródła: [EngineSession](src/main/java/org/example/processlab/engine/EngineSession.java), [ChangeTrial](src/main/java/org/example/processlab/workflow/ChangeTrial.java). F5 używa `createPersistent` i `reopenPersistent`: utworzenie jest jawne, wznowienie wymaga istniejącej bazy, schematu i tej samej pary modeli. Nie wdraża ich ponownie. Dziesięć osobnych JVM sprawdza odtworzenie instancji z pliku, nie z raportu. Instrukcja: [README F5](README.md#f5--jak-odtworzyć-i-obejrzeć-próbę).

## 3. C4 — komponenty aplikacji

To grupy odpowiedzialności wewnątrz jednej JVM. Na rysunku pominięto rozruch: ChangeTrial przy tworzeniu wdraża BPMN/DMN, a przy wznowieniu odczytuje zapisane definicje i kontroluje ich zgodność; łączy obiekty. EngineSession tworzy/zamyka silniki.

```mermaid
flowchart TB
    subgraph APP["Scenariusz i proces — komponenty aplikacji Java, jedna JVM"]
        F["ChangeProcess<br/>[Java]<br/>Polecenia, nowy stan, raport"]
        S["ChangeState + StateCodec<br/>[rekordy / Jackson]<br/>Migawka JSON caseState"]
        R["WorkflowChecks + Rules<br/>[czyste funkcje Java]<br/>Aktualność, kontrole, graf wpływu"]
        B["Flowable BPMN<br/>[biblioteka Java + XML]<br/>Zadania, przejścia, transakcja"]
        Q["QualificationStep + DmnQualifier<br/>[Java]<br/>Wywołanie przypiętej DMN"]
        D["Flowable DMN<br/>[biblioteka Java + tabela]<br/>Kwalifikacja faktów"]
        F -->|"Czyta / koduje"| S
        F -->|"Liczy kontrole i wpływ"| R
        F -->|"Complete i zapytania"| B
        B -->|"Synchroniczny delegat"| Q
        Q -->|"Wylicza fakty"| R
        Q -->|"Publiczne API oceny"| D
        F -->|"DmnQualifier przed odbiorem, bez historii"| Q
    end
    H[("Wspólne H2<br/>[osadzone w JVM; wariant memory lub file]")]
    B -->|"Zadania, caseState, historia"| H
    D -->|"Historia kwalifikacji w transakcji przebiegu"| H
    classDef component fill:#e4eff7,color:#173c56,stroke:#216a9e
    class F,S,R,B,Q,D component
```

**Granica transakcji:** fasada przekazuje nowy JSON i `action` w jednym `TaskService.complete`. Po `Assess` ta sama synchroniczna kontynuacja BPMN uruchamia QualificationStep i zapis historii DMN. Odczyty walidujące przed `complete` nie są dowodem ochrony przed konkurującymi klientami. Próba rollbacku: F4_06 w [testach](src/test/java/org/example/processlab/ChangeProcessTest.java).

Fasada sprawdza symulowaną rolę. Bezpośrednie API silnika nie jest zabezpieczone tą kontrolą. Raport czyta stan i historię z silnika; nie utrzymuje drugiego automatu etapów.

## 4. Diagram zależności kodu

Strzałka **A → B oznacza: A używa B**. Pokazano własne pakiety i biblioteki używane bezpośrednio, nie całe drzewo przechodnich zależności Maven. Kierunek strzałek nie jest przepływem danych ani kolejnością zadań.

```mermaid
flowchart LR
    W["workflow<br/>fasada, scenariusz, stan, codec"] --> E["engine<br/>EngineSession, DmnQualifier"]
    W --> R["rules<br/>ProjectSnapshot, Rules, fakty"]
    W --> D["domain<br/>rewizje, referencje, wyniki"]
    E --> R
    R --> D
    W --> F["Flowable<br/>publiczne uslugi i delegaty"]
    E --> F
    W --> J["Jackson 3<br/>konkretny schemat JSON"]
    E -. "konfiguracja JDBC" .-> H["H2<br/>sterownik w runtime testow"]
    classDef own fill:#e6f0ec,stroke:#28634f,color:#172d25
    class W,E,R,D own
```

Wniosek: dane domenowe nie importują silnika. Rules także nie importuje Flowable; można sprawdzać te reguły bez BPMN. Pakiet `engine` zna typy faktów/kwalifikacji z `rules`, ponieważ zawiera adapter DMN. To nie jest warstwa zupełnie niezależna od domeny. Źródła: [workflow](src/main/java/org/example/processlab/workflow), [engine](src/main/java/org/example/processlab/engine), [rules](src/main/java/org/example/processlab/rules), [domain](src/main/java/org/example/processlab/domain).

## 5. Diagram zależności produktów pracy — konkretny przykład

Inna znaczeniowo strzałka: **podstawa → produkt/wynik, który się na niej opiera**. Linia ciągła między CAP i AT pokazuje krawędź `Dependency`; linie przerywane pokazują referencje w rekordach ocen/wykonania. Te ostatnie nie są dodatkowymi krawędziami wejścia algorytmu BFS.

```mermaid
flowchart LR
    R["CAP-01@2<br/>Myslnik rozdziela slowa"] -->|"Dependency: VERIFIES"| T["AT-01@3<br/>bialo-czerwony daje 2"]
    R -. "subject" .-> VR["ReviewRecord demoPasscap<br/>PASS wymagania; basis puste"]
    R -. "basis" .-> VT["ReviewRecord demoPasstest<br/>PASS testu wobec CAP-01@2"]
    T -. "subject" .-> VT
    T -. "testCase" .-> X["TestRunRecord demoPassrun<br/>PASS wykonania w fabule"]
    C["CODE-01@3<br/>Fikcyjna wersja programu"] -. "software" .-> X
    VR --> K["Rules + DMN<br/>kwalifikacja wybranych kontroli"]
    VT --> K
    X --> K
    K --> U["TO_OPERATOR<br/>oczekiwanie na decyzje"]
```

Strzałki do kwalifikacji pokazują wykorzystanie wyników, nie zapisany ślad `Dependency`. W tym przykładzie nie ma krawędzi Requirement → Software w kolekcji dependencies. Związek z konkretną wersją programu jest w parze TestRunRecord. BFS nie obejmie automatycznie wszystkich powiązań z ocen i wykonań.

Po zmianie na CAP-01@3 stare rekordy pozostają. Nie stają się ocenami nowego wymagania. Źródło przykładu: widoki 3–5 [wykonanego demo](evidence/f4-demo.md); reguły: [Rules](src/main/java/org/example/processlab/rules/Rules.java), dobór: [WorkflowChecks](src/main/java/org/example/processlab/workflow/WorkflowChecks.java).

## 6. Struktury danych — stan sprawy i pamięć poleceń

Rysunek przedstawia rekordy Java oraz logiczne powiązanie z instancją Flowable, **nie tabele SQL**. FlowableInstance to element silnika pokazany poglądowo, nie nasza nowa klasa. Strzałki opisują pola i ich typy. Liczność przy celu oznacza zawartość pola; nie określamy wyłącznej przynależności wartości do jednej migawki. Niezmienne rekordy mogą być współdzielone przez kolejne migawki i instancje.

```mermaid
classDiagram
    class FlowableInstance {
        <<Flowable>>
        String processInstanceId
        String businessKey
    }
    class ChangeState {
        long version
        Scope scope
        ProjectSnapshot snapshot
        ArtifactRevision proposal
        boolean authorized
        String previousProcessId
        List receipts
        Acceptance acceptance
    }
    class Scope {
        String requirementId
        String testId
        String softwareId
    }
    class Receipt {
        String commandId
        String taskId
        long baseVersion
        Role role
        String action
        String reason
    }
    class Acceptance {
        String commandId
        long stateVersion
        Map basis
        String reason
    }
    class ProjectSnapshot
    class ArtifactRevision
    FlowableInstance "1" --> "1" ChangeState : ostatni caseState JSON
    FlowableInstance "0..1" <-- "0..*" ChangeState : previousProcessId
    ChangeState --> "1" Scope : scope
    ChangeState --> "1" ProjectSnapshot : snapshot
    ChangeState --> "1" ArtifactRevision : proposal
    ChangeState --> "0..*" Receipt : receipts
    ChangeState --> "0..1" Acceptance : acceptance
```

- `version` to wersja **stanu sprawy**, zwiększana po poleceniu; nie rewizja wymagania.
- `authorized` dotyczy propozycji zapisanej w tej migawce. Nowa propozycja zeruje upoważnienie; jego historia pozostaje w potwierdzeniach poleceń i historii silnika.
- `Acceptance.basis` to `Map<String, ArtifactRef>`: kopia mapy current w momencie przyjęcia. Zakres wykonanych kontroli określa Scope, nie sama liczba wpisów basis.
- `previousProcessId` może wskazywać poprzednią przyjętą instancję. Kod nie ogranicza jej do jednego następcy.
- Etap BPMN i aktywne taskId nie są polem ChangeState. Pochodzą z usług silnika. Historia FULL może zachować więcej niż jedną historyczną wartość JSON; rysunek wiąże instancję z ostatnią migawką odczytywaną przez fasadę.

Źródła: [ChangeState](src/main/java/org/example/processlab/workflow/ChangeState.java), metody `startNext`, `state`, `execute` w [ChangeProcess](src/main/java/org/example/processlab/workflow/ChangeProcess.java).

## 7. Struktury danych — rewizje, ślad i dowody

```mermaid
classDiagram
    class ProjectSnapshot {
        List artifacts
        Map current
        List dependencies
        List reviews
        List runs
    }
    class ArtifactRevision {
        ArtifactRef ref
        Kind kind
        String content
    }
    class ArtifactRef {
        String id
        int revision
    }
    class Dependency {
        ArtifactRef basis
        ArtifactRef dependent
        Kind kind
    }
    class ReviewRecord {
        String id
        ArtifactRef subject
        List basis
        Outcome outcome
        String rationale
    }
    class TestRunRecord {
        String id
        ArtifactRef testCase
        ArtifactRef software
        Outcome outcome
    }
    ProjectSnapshot --> "0..*" ArtifactRevision : artifacts
    ProjectSnapshot --> "0..*" ArtifactRef : wartosci current
    ProjectSnapshot --> "0..*" Dependency : dependencies
    ProjectSnapshot --> "0..*" ReviewRecord : reviews
    ProjectSnapshot --> "0..*" TestRunRecord : runs
    ArtifactRevision --> "1" ArtifactRef : ref
    Dependency --> ArtifactRef : basis oraz dependent
    ReviewRecord --> ArtifactRef : subject oraz elementy basis
    TestRunRecord --> ArtifactRef : testCase oraz software
```

| Pole/typ | Znaczenie i ograniczenie |
| --- | --- |
| ArtifactRef | Para `(id, revision)`; równość po wartości, nie tożsamość obiektu Java |
| ArtifactRevision.Kind | REQUIREMENT / TEST_CASE / SOFTWARE |
| ProjectSnapshot.current | `Map<String, ArtifactRef>`; jawny wybór bieżącej rewizji. Nie wybieramy automatycznie największej |
| Dependency.Kind | DERIVED_FROM / VERIFIES; kierunek `basis → dependent` |
| ReviewRecord.basis | Lista referencji; przy porównywaniu podstawy Rules traktuje ją jak zbiór |
| ReviewRecord.Outcome | PASS / FAIL; sprzeczne wyniki tej samej podstawy nie są automatycznie rozstrzygane |
| TestRunRecord.Outcome | PASS / FAIL / ERROR; zawsze dla pary test i program |

Odnośnik ArtifactRef sam nie gwarantuje istnienia wskazanej rewizji. Migawka analityczna F3 dopuszcza braki i zwraca UNKNOWN; fasada F4 odmawia przyjęcia wyników z referencjami do nieistniejących rewizji na wejściu start/Assess. Duplikat ID dowodu jest odrzucany; dopisanie nowego tworzy nową migawkę. To zachowanie API, nie zabezpieczenie przed zmianą bazy przez kogoś z bezpośrednim dostępem.

Źródła: [ProjectSnapshot](src/main/java/org/example/processlab/rules/ProjectSnapshot.java) i [rekordy domain](src/main/java/org/example/processlab/domain).

## 8. Struktury danych — polecenie i jego cel

Envelope i Operation to dwa argumenty `execute`, nie jeden rekord zawierający drugą strukturę. Role są danymi z zaufanego lokalnego scenariusza, nie uwierzytelnioną tożsamością.

```mermaid
classDiagram
    class ChangeProcess {
        execute(Envelope command, Operation operation)
    }
    class Envelope {
        String id
        String processId
        String taskId
        long expectedVersion
        Role role
    }
    class Operation {
        <<sealed interface>>
        reason() String
    }
    class Authorize {
        boolean allowed
        String reason
    }
    class ApplyChange {
        String reason
    }
    class Prepare {
        ArtifactRevision test
        ArtifactRevision software
        String reason
    }
    class Assess {
        List reviews
        List runs
        String reason
    }
    class Decide {
        boolean accepted
        String reason
    }
    class Propose {
        ArtifactRevision requirement
        String reason
    }
    class Rework {
        String reason
    }
    ChangeProcess ..> Envelope : argument celu
    ChangeProcess ..> Operation : argument dzialania
    Operation <|.. Authorize
    Operation <|.. ApplyChange
    Operation <|.. Prepare
    Operation <|.. Assess
    Operation <|.. Decide
    Operation <|.. Propose
    Operation <|.. Rework
```

Envelope identyfikuje konkretną instancję, aktywne zadanie i oczekiwaną wersję stanu. ID polecenia jest unikalne wewnątrz instancji; ponowienie po skutecznym zapisie jest odrzucane. Authorize i Decide wymagają OPERATOR; pozostałe operacje AGENT. Dodatkowo każda operacja ma dozwolone etapy — sam prawidłowy typ nie wystarcza. Odrzucona/wycofana transakcja nie zapisuje Receipt, więc po usunięciu awarii można ponowić to samo polecenie.

Źródło: [ChangeCommands](src/main/java/org/example/processlab/workflow/ChangeCommands.java), walidacja i zapis w [ChangeProcess](src/main/java/org/example/processlab/workflow/ChangeProcess.java).

## Notacja, aktualizacja i granice

**Decyzja agenta A15, 2026-11-05:** pokazać poziomy C4 Context/Container/Component przy użyciu Mermaid flowchart z jawnymi typami i granicami, zależności również jako flowchart, a rekordy jako classDiagram. Natywny renderer C4 po próbnej generacji nakładał opisy na węzły; flowchart zachowuje treść poziomów C4 i daje czytelniejsze rozmieszczenie. Nie jest to składnia C4Context/C4Container/C4Component. Rekordy odpowiadają kodowi; nie tworzymy pozornego relacyjnego schematu bazy ani osobnych usług dla bibliotek. Diagramy ilustrują wybrany przekrój F4/F5, nie pełny model ISO. Aktualizacja A16: wariant file zmienia przechowywanie, nie rekordy domeny ani przebieg.

Podstawa notacji: [C4 — poziom kontenerów](https://c4model.com/diagrams/container) i [Mermaid — C4](https://mermaid.js.org/syntax/c4.html). O zgodności z tą implementacją rozstrzygają podane źródła lokalne. Po zmianie typów, zależności albo granic wykonania trzeba zaktualizować odpowiedni widok; nie ma automatycznej synchronizacji z kodem.

F5 obejmuje poprawne zamknięcie JVM i ponowne otwarcie na tym samym buildzie. Nie dowodzi odporności na utratę zasilania, migracji, backupu ani zgodności innego kodu Java przy takich samych XML. Dokument nie zmienia reguł procesu, nie jest nowym planem ani dowodem odbioru.
