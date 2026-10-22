# Wymagania szablonu (warstwa procesu)

Wymagania wobec samego szablonu procesu (D-59), w składni EARS, z podmiotem „Process kit” (ustawienie system warstwy procesu). Każde wymaganie wskazuje decyzję, z której wynika (`source:`); test akceptacyjny, który je sprawdza, jest w spec/tests/process-kit.feature (D-60). Wymaganie bez testu to luka widoczna w macierzy śladu (W1), a nie przeoczenie.

Do przeniesienia (D-54) plik leży w docelowym miejscu warstwy procesu, a ślad liczy dla niego `make process-kit` (widok tymczasowy, tools/process_kit_view.py). Wymagania o układzie i migracjach (LAY, MIG) opisują stan po przeniesieniu; dziś nie mają testów.

Obszary: TRC ślad · HKS hooki · SEP rozdział autora i weryfikatora · PLN plan i postęp · REC rekordy i listy kontrolne · REP repozytorium i kopia · ISO zgodność z normą · INI start projektu · DST dystrybucja · UPD bramka aktualizacji · MIG migracje · LAY układ i własność plików · LEK przeciek domeny · TST katalog testów · LNG język.

## TRC Ślad

### TRC-01
- pattern: ubiquitous
- text: Process kit shall read every ID schema, Parent field, coverage rule and state only from the Traceability Model.
- source: D-05, D-06
- quality: maintainability
- status: initiated

### TRC-02
- pattern: event
- text: When an Element lacks a required field or a Parent, Process kit shall report an error.
- source: D-06, D-14
- quality: functional
- status: initiated

### TRC-03
- pattern: event
- text: When an Element refers to an ID that does not exist, Process kit shall report an error.
- source: D-06, D-26
- quality: functional
- status: initiated

### TRC-04
- pattern: event
- text: When two Elements share one ID, Process kit shall report an error.
- source: D-05
- quality: functional
- status: initiated

### TRC-05
- pattern: event
- text: When a field holds a value outside the values that the Traceability Model allows, Process kit shall report an error.
- source: D-11, D-14, D-33
- quality: functional
- status: initiated

### TRC-06
- pattern: event
- text: When a Requirement text breaks its EARS pattern or does not contain exactly one "shall", Process kit shall report an error.
- source: D-01
- quality: functional
- status: initiated

### TRC-07
- pattern: event
- text: When a Requirement text contains a capitalized term that is missing from the Glossary, Process kit shall report an error.
- source: D-01
- quality: functional
- status: initiated

### TRC-08
- pattern: event
- text: When a Parent has a type that the Traceability Model does not allow for that field, Process kit shall report an error.
- source: D-28
- quality: functional
- status: initiated

### TRC-09
- pattern: event
- text: When an Element lacks the children that a coverage rule of level error demands, Process kit shall report an error.
- source: D-06
- quality: functional
- status: initiated

### TRC-10
- pattern: ubiquitous
- text: Process kit shall generate the Trace Matrix in both directions from the Parent fields alone.
- source: D-06, D-09
- quality: functional
- status: initiated

### TRC-11
- pattern: event
- text: When an Element has a field that the Traceability Model does not know, Process kit shall report a warning.
- source: D-21
- quality: maintainability
- status: initiated

### TRC-12
- pattern: event
- text: When a Work Product is in state verified or approved without a passing Verification Record, Process kit shall report a warning.
- source: D-15
- quality: functional
- status: initiated

### TRC-13
- pattern: event
- text: When an Element or its Parent changed after the Commit that added its last passing Verification Record, Process kit shall report a warning.
- source: D-32, D-39
- quality: functional
- status: initiated

### TRC-14
- pattern: ubiquitous
- text: Process kit shall read the Traceability Model with the same result on every supported interpreter version.
- source: D-26
- quality: portability
- status: initiated

### TRC-15
- pattern: event
- text: When a word that looks like an ID stands inside a longer token or belongs to an area that does not exist yet, Process kit shall not treat it as a reference.
- source: D-26
- quality: functional
- status: initiated

### TRC-16
- pattern: event
- text: When a heading puts a colon after the ID, Process kit shall report the colon.
- source: D-26
- quality: usability
- status: initiated

### TRC-17
- pattern: event
- text: When a scenario without a tag follows an Acceptance Test, Process kit shall end that Acceptance Test before the scenario.
- source: D-26
- quality: functional
- status: initiated

### TRC-18
- pattern: ubiquitous
- text: Process kit shall show in the Trace Matrix every quality characteristic that has no Requirement.
- source: D-33
- quality: functional
- status: initiated

### TRC-19
- pattern: event
- text: When a screen in the navigation map has no edge, Process kit shall report the screen.
- source: D-26
- quality: functional
- status: initiated

## HKS Hooki

### HKS-01
- pattern: event
- text: When a Commit is attempted while the Trace Matrix has errors or is stale, Process kit shall reject the Commit.
- source: D-06, D-25
- quality: functional
- status: initiated

### HKS-02
- pattern: event
- text: When a Commit Message names no existing ID, Process kit shall reject the Commit.
- source: D-06, D-26
- quality: functional
- status: initiated

### HKS-03
- pattern: event
- text: When a Commit is attempted while the Progress Record or the Compliance Page is stale, Process kit shall reject the Commit.
- source: D-10, D-16, D-25
- quality: functional
- status: initiated

### HKS-04
- pattern: unwanted
- text: If another hook manager already set the hooks path, then Process kit shall leave the hooks path unchanged.
- source: D-53
- quality: compatibility
- status: initiated

### HKS-05
- pattern: event
- text: When a Commit is attempted, Process kit shall check the content staged for that Commit and not the working tree.
- source: D-69
- quality: reliability
- status: initiated

## SEP Rozdział autora i weryfikatora

### SEP-01
- pattern: event
- text: When a Commit adds a passing Verification Record and changes or creates an Element that the record verifies, Process kit shall reject the Commit.
- source: D-38
- quality: functional
- status: initiated

### SEP-02
- pattern: ubiquitous
- text: Process kit shall exempt the first Commit of a repository from the separation check.
- source: D-38
- quality: usability
- status: initiated

## PLN Plan i postęp

### PLN-01
- pattern: ubiquitous
- text: Process kit shall generate the Progress Record from the plan, the records and the tags.
- source: D-10, D-16
- quality: functional
- status: initiated

### PLN-02
- pattern: event
- text: When the tag of a Milestone exists, Process kit shall show the Milestone as reached in the Progress Record.
- source: D-16
- quality: functional
- status: initiated

### PLN-03
- pattern: event
- text: When a task lists what it produces, Process kit shall accept only type codes and IDs.
- source: D-09, D-16
- quality: functional
- status: initiated

## REC Rekordy i listy kontrolne

### REC-01
- pattern: event
- text: When a Verification Record names a Checklist or an item that does not exist, Process kit shall report an error.
- source: D-31
- quality: functional
- status: initiated

### REC-02
- pattern: event
- text: When a Verification Record has result pass and lists failed items, Process kit shall report an error.
- source: D-31
- quality: functional
- status: initiated

## REP Repozytorium i kopia zapasowa

### REP-01
- pattern: event
- text: When the restore check runs, Process kit shall compare the head commit, the tags and the trace of a fresh clone of the Backup Remote with the local repository.
- source: D-35
- quality: reliability
- status: initiated

### REP-02
- pattern: optional
- text: Where the record option is given, Process kit shall append the result of the restore check as a Verification Record.
- source: D-35
- quality: functional
- status: initiated

## ISO Zgodność z normą

### ISO-01
- pattern: ubiquitous
- text: Process kit shall generate the Compliance Page from the Traceability Model and the data of the norm.
- source: D-12, D-25
- quality: functional
- status: initiated

## INI Start projektu

### INI-01
- pattern: unwanted
- text: If the working tree has uncommitted changes or the Project was already started, then Process kit shall refuse to start the Project.
- source: D-22
- quality: reliability
- status: initiated

### INI-02
- pattern: event
- text: When a Project starts, Process kit shall archive the template history and create a Decision Register with one start Decision.
- source: D-22, D-58
- quality: functional
- status: initiated

### INI-03
- pattern: event
- text: When a Project starts from a copy without template history, Process kit shall let the first Commit pass every hook.
- source: D-29
- quality: usability
- status: initiated

## DST Dystrybucja

### DST-01
- pattern: event
- text: When a Project is generated, Process kit shall deliver only the Process Package and the Answers File.
- source: D-47
- quality: functional
- status: initiated

### DST-02
- pattern: event
- text: When the Answers File names a version other than the requested Release Tag, Process kit shall report the update as failed.
- source: D-49
- quality: reliability
- status: initiated

## UPD Bramka aktualizacji

### UPD-01
- pattern: unwanted
- text: If the requested version does not have the form "vX.Y.Z" or the working tree is not clean, then Process kit shall refuse the update before it changes any file.
- source: D-52, D-53
- quality: reliability
- status: initiated

### UPD-02
- pattern: event
- text: When an update leaves conflict markers, unmerged entries or rejected hunks, Process kit shall report the update as failed even if copier exits with code 0.
- source: D-52
- quality: reliability
- status: initiated

### UPD-03
- pattern: event
- text: When an update changes a file outside the Process Package other than the Answers File, Process kit shall report the update as failed.
- source: D-47, D-52
- quality: reliability
- status: initiated

### UPD-04
- pattern: event
- text: When an update succeeds, Process kit shall leave every Project file outside the Process Package byte-identical.
- source: D-47
- quality: reliability
- status: initiated

### UPD-05
- pattern: event
- text: When copier exits with an error, Process kit shall report the update as failed.
- source: D-52
- quality: reliability
- status: initiated

### UPD-06
- pattern: event
- text: When the validation of the Project fails after an update, Process kit shall report the update as failed without a Commit.
- source: D-51, D-52
- quality: reliability
- status: initiated

### UPD-07
- pattern: event
- text: When an update to the installed version runs again, Process kit shall leave the working tree unchanged.
- source: D-52
- quality: reliability
- status: initiated

### UPD-08
- pattern: event
- text: When a Project skips releases, Process kit shall apply the changes of every skipped release.
- source: D-49
- quality: functional
- status: initiated

## MIG Migracje dokumentów

### MIG-01
- pattern: event
- text: When a release changes rules for existing documents, Process kit shall describe the Migration in the Process Package.
- source: D-51
- quality: maintainability
- status: initiated

### MIG-02
- pattern: state
- text: While the version of the Process Package is newer than the migrated version of the Project, Process kit shall report a warning.
- source: D-51
- quality: functional
- status: initiated

## LAY Układ i własność plików

### LAY-01
- pattern: ubiquitous
- text: Process kit shall keep every Project document outside the Process Package.
- source: D-47, D-54
- quality: maintainability
- status: initiated

### LAY-02
- pattern: event
- text: When a Document Template changes in a release, Process kit shall leave the documents created from it unchanged.
- source: D-47
- quality: reliability
- status: initiated

### LAY-03
- pattern: event
- text: When a document or a script mentions a path that does not exist and is not listed as an exception with a reason, Process kit shall report an error.
- source: D-61
- quality: maintainability
- status: initiated

## LEK Przeciek domeny

### LEK-01
- pattern: unwanted
- text: If a file of the Process Package contains a concrete ID of a Project Element, then Process kit shall report an error.
- source: D-57, D-62
- quality: maintainability
- status: initiated

### LEK-02
- pattern: unwanted
- text: If a file of the Process Package contains a term from the Glossary of the Project, then Process kit shall report an error.
- source: D-57, D-62
- quality: maintainability
- status: initiated

## TST Katalog testów

### TST-01
- pattern: event
- text: When an Acceptance Test names a runner that does not point to an existing file and case, Process kit shall report an error.
- source: D-60
- quality: functional
- status: initiated

### TST-02
- pattern: event
- text: When the test report runs, Process kit shall mark an Acceptance Test as passed only if every case it names passed.
- source: D-60
- quality: reliability
- status: initiated

## LNG Język

### LNG-01
- pattern: ubiquitous
- text: Process kit shall name every type code, field, state, file and error code in "English".
- source: D-17, D-18, D-20
- quality: maintainability
- status: initiated
