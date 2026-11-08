# Jedna karta TextStats → istniejące dane F5

2026-11-08 · A-09 · analiza wykonana na zlecenie U „Dajel”.

**Wniosek:** dane wystarczają do czytelnego, generowanego raportu edukacyjnego dla trzech stanów. Nie wystarczają do automatycznego odtworzenia całego ręcznie napisanego meldunku: uzasadnienia merytoryczne i zalecenia agenta nie są faktami wyliczanymi przez silnik. Najmniejszy następny krok to raport tylko do odczytu, z jawnymi brakami. Nie potrzeba teraz nowego schematu danych.

Wykryta granica: przy nowej propozycji silnik czeka na **operatora**, podczas gdy przyjęty wzorzec komunikacji zaleca najpierw **analizę przez agenta**. Można ją wykonać doradczo poza workflow, ale F5 nie rejestruje jej jako osobnego etapu przed zgodą. Ukrycie tej różnicy w etykiecie karty byłoby błędem. Automatyczna obsługa takiego etapu wymagałaby osobnej zmiany procesu; nie jest zlecona.

## 1. Przedmiot i źródła

Mapujemy [przyjętą koncepcję](textstats-walkthrough-verbatim.md) (§14, §18–21), nie wszystkie przyszłe typy kart GUI/bazy/CNC. Wcześniejsze opisy pozostają historią rozmowy; poniższe ustalenia doprecyzowują granice ich automatycznego odtwarzania.

| Źródło | Co jest wiążące dla mapowania |
|---|---|
| [ChangeState](../flowable-trial/src/main/java/org/example/processlab/workflow/ChangeState.java) | Stan sprawy, zakres przez ID, propozycja, aktualny snapshot, historia poleceń i odbiór |
| [ProjectSnapshot](../flowable-trial/src/main/java/org/example/processlab/rules/ProjectSnapshot.java) | Rewizje, bieżące referencje, zależności, oceny i deklarowane wykonania |
| [WorkflowChecks](../flowable-trial/src/main/java/org/example/processlab/workflow/WorkflowChecks.java), [Rules](../flowable-trial/src/main/java/org/example/processlab/rules/Rules.java) | Aktualność i agregacja trzech kontroli; kandydaci wpływu, nie kompletna analiza znaczenia |
| [ChangeProcess](../flowable-trial/src/main/java/org/example/processlab/workflow/ChangeProcess.java): execute, state, tasks, report | Dozwolone operacje, aktywne zadania i istniejący raport; upoważnienie zostaje zużyte przy ApplyChange |
| [05-fail](../flowable-trial/evidence/f5-restart/05-fail.json), [07-show](../flowable-trial/evidence/f5-restart/07-show.json), [10-show](../flowable-trial/evidence/f5-restart/10-show.json) | Zachowane dane rzeczywistego uruchomienia symulatora. Oceny produktu i decyzje wewnątrz scenariusza są fikcyjne |

## 2. Mapa pól — wszystkie tylko do odczytu

Klucze w pierwszej kolumnie to **proponowane nazwy projekcji widoku**, nie nowe pola utrwalanego modelu ani wdrożony kontrakt API. `s` oznacza ChangeState, `p` jego snapshot. Referencja zawsze obejmuje ID i rewizję. Etykieta dla człowieka nie zastępuje klucza ani referencji.

| Pole / sens dla operatora | Źródło lub wyliczenie | Granica i brak |
|---|---|---|
| `context` — która sprawa i z którego momentu | ID instancji, `s.version`; aktywne TaskView.id/key; nazwa eksportu w odczycie archiwalnym | Nie mylić wersji stanu, rewizji artefaktu i wersji definicji BPMN |
| `simulationNotice` — co właściwie oglądam | Stała etykieta tego demonstratora: „Symulacja; TextStats nie uruchomiono” | To kontekst próby, nie uniwersalna flaga jakości każdego ReviewRecord |
| `goal` — co chcemy uzyskać | Treść wymagania wybranego przez `s.scope.requirementId` i `p.current`, odszukana w `p.artifacts` | Brak osobnej potrzeby biznesowej i tytułu funkcji. „TextStats — zmiana liczenia słów” może być stałą etykietą przykładu, nie wywnioskowanym polem projektu |
| `proposal` — co dopiero proponujemy | `s.proposal.ref/content`; porównanie z bieżącą referencją wymagania | Oddzielić od aktualnego zakresu. Równość referencji w tych eksportach oznacza zastosowaną propozycję; brak danych nie oznacza zgody |
| `currentBasis` — na jakich wersjach pracujemy | `p.current` + treści odpowiadających rewizji | Brak rewizji ma być widocznym błędem/brakiem, bez wybierania „ostatniej podobnej” treści |
| `requirementCheck` — ocena opisu zachowania | `WorkflowChecks.checks(s).requirementReview`; szczegóły ReviewRecord: subject, basis, outcome, rationale | Nie dowodzi rzeczywistego przeglądu ani poprawności opisu |
| `testCheck` — ocena oczekiwań testu | `WorkflowChecks.checks(s).testReview` + odpowiednie ReviewRecord i treść przypadku | Powód FAIL w danych to „Ocena testu w fabule”. Wyjaśnienie „1 zamiast 2” pochodzi z analizy treści, nie z algorytmu kontroli |
| `executionCheck` — zapis wyniku testu | `WorkflowChecks.checks(s).testExecution` + TestRunRecord.id/testCase/software/outcome | Brak rzeczywistego wyniku, logu, danych wejścia i środowiska wykonania. Pokazać „fikcyjny zapis PASS”, nie „program działa” |
| `history` — co wykonano wcześniej | `s.receipts`, historia zadań oraz zachowane oceny i rewizje | Zakończenie zadania nie potwierdza jakości. Nie ma osobnego rejestru zastrzeżeń z formalnym zamknięciem; można pokazać dawny FAIL i aktualny PASS dla innych rewizji |
| `authorization` — zgoda na zastosowanie propozycji | `s.authorized`, aktywne zadanie, referencja propozycji; do wyjaśnienia przeszłej zgody receipts i stateHistory | `false` po APPLY nie znaczy „nigdy nie było zgody”. Same receipts nie wiążą zgody z pełną treścią propozycji; dla innych przebiegów potrzebny odczyt odpowiedniego stanu historii |
| `acceptance` — co odebrano | `s.acceptance.commandId/stateVersion/basis/reason`; poprzednia sprawa wskazana przez `s.previousProcessId` | Odbiór odnosi się do zapisanej podstawy. Przy braku poprzedniej sprawy pokazać brak odczytu; nie odtwarzać odbioru z aktualnego snapshotu |
| `pendingWork` — co blokuje i kto ma zadanie | `ChangeProcess.tasks(id)` + trzy bieżące kontrole; odbiór i nowa propozycja pokazane osobno | Lista zadań nie jest roadmapą projektu. Assignee/Role to rola w zaufanym demonstratorze, nie potwierdzona tożsamość człowieka |
| `recommendation` — co agent zaleca i czego chce od operatora | Oddzielna, jawnie doradcza interpretacja powyższych faktów, odnosząca się do tej sprawy i wersji | Brak utrwalonego meldunku i jego uzasadnienia. Szablon komunikatu może kierować do korekty/oceny, lecz nie udawać analizy znaczenia, zgody lub wykonanej pracy |

Treść wejścia i oczekiwany wynik są obecnie tekstem `ArtifactRevision.content`, a nie osobnymi liczbami/polami. Nie proponuję parsera zdań polskich, który miałby z nich odgadywać kontrakt testu. Pokazujemy treść; semantyczne wyjaśnienie oznaczamy jako analizę agenta.

## 3. Trzy znane stany i oczekiwany sens widoku

| Odczyt | Fakty z danych | Uczciwy meldunek / odpowiedzialność |
|---|---|---|
| 05-fail: sprawa 7, stan 4 | CAP-01@2, AT-01@2, CODE-01@2; kontrole PASSED / CORRECTION / PASSED. Aktywne `prepare`, AGENT. Brak odbioru | „Ocena testu wymaga korekty; fikcyjny PASS wykonania tego nie usuwa. Agent przygotowuje poprawkę i nowe oceny w dotychczasowym zakresie. Nowa decyzja operatora nie jest teraz potrzebna.” Treść wymagania i przypadku pozwala agentowi wyjaśnić rozbieżność 2/1 |
| 07-show: sprawa 7, stan 6 | CAP-01@2, AT-01@3, CODE-01@3; trzy PASSED; `accept`, OPERATOR. Brak odbioru; stary FAIL dla AT-01@2 nadal zapisany | „Dla aktualnej podstawy są pozytywne zapisy w fabule; oczekuje decyzja o odbiorze w ćwiczeniu.” Nie mówić „wszystkie problemy zamknięte” ani „przetestowany produkt”. Rekomendacja odbioru wymaga jawnego uzasadnienia i ograniczenia do fabuły |
| 10-show: poprzednia sprawa 7, stan 7; nowa 10007, stan 0 | Poprzednia acceptance wiąże CAP-01@2, AT-01@3, CODE-01@3; brak jej aktywnych zadań. Nowa ma propozycję CAP-01@3, stare current i wyniki, brak zgody; `authorize`, OPERATOR | „Stary zakres odebrany w fabule; nowe rozszerzenie bez zgody i nowych dowodów. Silnik oczekuje decyzji. Rekomendacja agenta: przed decyzją przygotować analizę poza tym workflow.” Nie podpisywać starych PASSED jako kontroli propozycji @3 ani nie przedstawiać analizy jako aktywnego zadania F5 |

Trzy kontrole nie są trzema fazami całego SDLC. `Rules` ocenia spójność zapisów i aktualność podstawy. Generator powinien używać tych funkcji, nie odtwarzać ich w osobnym zestawie warunków i nie wybierać najnowszego PASS zamiast sprawdzania konfliktów.

Tłumaczenia zachowujące rozróżnienia: PASSED — „pozytywne zapisy dla tej podstawy”; CORRECTION — „negatywna ocena, potrzebna korekta”; CONFLICT — „sprzeczne wyniki”; REVIEW_REQUIRED — „potrzebna aktualna ocena”; UNKNOWN — „brak wystarczającej podstawy do ustalenia”. Żaden z nich sam nie jest odbiorem produktu.

## 4. Wpływ i najmniejszy dalszy zakres

| Ustalenie / kategoria | Dlaczego obecny mechanizm nie wystarcza | Minimalna odpowiedź; koszt i sprawdzenie |
|---|---|---|
| **Brak prezentacji:** techniczny raport miesza orientację z detalami | U nie rozumiał 07-show; same ID i PASSED nie mówią, co dalej | Propozycja: raport tylko do odczytu, ze znaczeniem pracy na pierwszym planie i referencjami w szczegółach. Koszt: mały formatter i testy trzech stanów; ocena: operator wskazuje stan oraz następne działanie |
| **Brak danych:** rzeczywiste dowody i szczegółowe uzasadnienia | Istnieją tylko fikcyjne wyniki i ogólne rationale; zmiana etykiety nie odtworzy pracy | Teraz jawny brak, bez rozbudowy modelu. Koszt: utrzymanie etykiet ograniczeń. Sprawdzenie: raport nie wymyśla logu, wyniku ani recenzenta |
| **Brak etapu w ograniczonym workflow:** analiza przed zgodą | `authorize` poprzedza `impact`; w stanie 0 nie ma operacji AGENT zapisującej taką analizę | Teraz oddzielić zadanie silnika od doradczej rekomendacji. Zmianę kolejności i dowodu analizy odłożyć do osobnej decyzji. Koszt teraz: jedna jawna informacja; sprawdzenie: raport nie przypisuje tego zadania silnikowi |

Nie stwierdzono na tej podstawie nowego defektu silnika względem jego przyjętego F1–F5. Wykazano niepełne pokrycie późniejszej koncepcji karty. Nie zmieniamy odbioru koncepcji na odbiór implementacji.

**Proponowany następny krok, niezlecony:** wygenerować raport tekstowy dla tych trzech stanów w istniejącym projekcie Java, z wykorzystaniem obecnych reguł; bez UI, REST, nowej bazy lub migracji. Zakończenie: treści powstają z danych, pokazują braki i różnicę zadanie/rekomendacja, zachowują historyczny odbiór; testy obejmują też mylące stare PASS i `authorized=false` po zastosowaniu zmiany. Sam odczyt nie może wykonać polecenia procesu. Następnie warunkowo jedna próba czytelności po wznowieniu.

Każda przyszła komenda musi nadal odnosić się do właściwej sprawy, aktywnego zadania i oczekiwanej wersji, jak obecny Envelope; wyświetlony raport nie upoważnia do działania na późniejszym stanie. Nie dokładamy manifestów wejść ani mechanizmu zgód.

Sprawy odłożone: agent przygotuje kontrakt rzeczywistych dowodów dopiero przed operacyjnym użyciem; operator rozstrzygnie ewentualną zmianę workflow po przedstawieniu wpływu przez agenta. Nie blokują bieżącej analizy ani proponowanego raportu z jawnymi brakami.

## 5. Sprawdzenie i odtworzenie

Wykonano odczyt kodu i trzech zachowanych eksportów, porównanie referencji, zadań, odbioru i powiązania ocen. Nie uruchamiano ponownie silnika ani TextStats. Wyniki PASS w tabeli §3 pochodzą z istniejących raportów `.json.md`, sprawdzonych względem rekordów i kodu reguł; nie są wynikiem nowych testów Java.

Poniższa kontrola uruchamiana z korzenia repo nie wymaga `/private/tmp`, zależności ani zapisu. Sprawdza wybrane podstawy mapowania, nie poprawność całego silnika:

```sh
python3 - <<'PY'
import json
from pathlib import Path
root = Path('reference/process-map/flowable-trial/evidence/f5-restart')
data = {n: json.loads((root / (n + '.json')).read_text())['cases']
        for n in ('05-fail', '07-show', '10-show')}
for name, version, task, actor in (
    ('05-fail', 4, 'prepare', 'AGENT'),
    ('07-show', 6, 'accept', 'OPERATOR')):
    case = data[name]['first']; state = case['state']
    assert str(case['id']) == '7' and state['version'] == version
    assert [(t['key'], t['assignee']) for t in case['tasks']] == [(task, actor)]
    assert state['acceptance'] is None and not state['authorized']
    assert any(r['action'] == 'ALLOW' for r in state['receipts'])
    assert any(r['action'] == 'APPLY' for r in state['receipts'])
bad = data['05-fail']['first']['state']['snapshot']
assert any(r['subject'] == bad['current']['AT-01'] and r['outcome'] == 'FAIL'
           for r in bad['reviews'])
assert any(r['testCase'] == bad['current']['AT-01'] and r['outcome'] == 'PASS'
           for r in bad['runs'])
old = data['10-show']['first']; new = data['10-show']['next']
assert not old['tasks'] and old['state']['acceptance'] is not None
assert old['state']['acceptance']['basis'] == old['state']['snapshot']['current']
assert str(new['state']['previousProcessId']) == str(old['id'])
assert new['state']['snapshot']['current'] == old['state']['acceptance']['basis']
assert new['state']['proposal']['ref'] != new['state']['snapshot']['current']['CAP-01']
assert new['state']['acceptance'] is None and not new['state']['authorized']
assert [(t['key'], t['assignee']) for t in new['tasks']] == [('authorize', 'OPERATOR')]
print('PASS: podstawy mapowania trzech eksportów; bez uruchamiania silnika')
PY
```

Wynik wykonania i kontroli dokumentacji: rejestr [§8.8](../../process-modeling/coverage-map.md#88-rejestr-zmian-i-wykonania). Status i upoważnienie: A-09 w §8.7. Ten dokument nie ustanawia drugiego planu ani nowych wymagań normy.


## 6. Kryteria implementacji raportu — A-10

2026-11-08: U „dalej” zleca rekomendowany raport. Zakres: formatter Java + odczyt eksportu F5, bez bazy, mutacji procesu, UI, nowych zależności i commita. Archiwalny charakter odczytu ma być widoczny. Aktualne statusy tylko w planie §8.7.

- K1: 05-fail pokazuje negatywną ocenę testu mimo PASS wykonania i pracę agenta, bez żądania ponownej zgody.
- K2: 07-show pokazuje podstawę @2/@3/@3 i oczekujący odbiór, nie deklaruje odbioru ani rzeczywistego działania programu; dawny FAIL pozostaje historyczny.
- K3: 10-show rozdziela poprzedni odbiór i nową propozycję. Stare kontrole nie oceniają propozycji; zadanie OPERATOR i doradcza analiza agenta poza workflow są jawnie różne.
- K4: brak danych, sprzeczne wyniki i brak aktualnej oceny zachowują znaczenie istniejących Rules/WorkflowChecks; nie wybierać ostatniego PASS. Brak odczytu poprzednika jest jawny.
- K5: false po zastosowaniu propozycji nie jest opisane jako brak historycznej zgody; wyjście zawiera ID sprawy, wersję stanu, referencje, ID zadania i ograniczenia dowodów.
- K6: powtarzany odczyt jest deterministyczny i nie zmienia źródła ani stanu. Błędne wejście/nieznana sprawa daje błąd, nie pustą zieloną kartę. Do odczytu nie otwieramy silnika.
- K7: jedno opisane polecenie generuje każdą kartę; zachowane przykłady wynikowe, RED/GREEN i pełna regresja projektu Java. Próba czytelności operatora pozostaje osobnym następnym krokiem.

Kolejność wykonania: testy oparte na zachowanych eksportach i przypadkach braków → RED na kompilującym się pustym formatterze → implementacja → GREEN, regresja, uruchomienie polecenia i przegląd wygenerowanych kart. Wyniki oraz odtworzenie w evidence/operator-card/. Nie powstaje nowy schemat domeny ani drugi silnik kwalifikacji.

Wykonanie A-10 i rozliczenie K1–K7: [raport oraz dowody](../flowable-trial/evidence/operator-card/README.md). To zakończenie techniczne, nie wynik próby czytelności operatora.


## 7. Relacja karty do produktów pracy ISO — wyjaśnienie po A-11

2026-11-08. Sprawdzono lokalny [rozdział 9](../../../../iso-29110-5-1/chapters/09-description-of-work-products.md), wprowadzenie oraz tabele 13, 25, 31, 32, 35, i [PM.04.01–02](../../../../iso-29110-5-1/chapters/06-project-management-pm-process.md). Karta operatora z rekomendacją i gotową odpowiedzią jest naszym rozwiązaniem prezentacyjnym, nie formularzem z ISO.

- Opis zachowania odpowiada treści specyfikacji wymagań (WP.13); przypadek testowy — WP.19; zapisy wykonania testów — WP.20; zapisy przeglądów — WP.23. To mapowanie rodzaju informacji, nie twierdzenie, że fikcyjne dane spełniają wszystkie charakterystyki tych produktów pracy.
- WP.01, Acceptance record, dokumentuje przyjęcie dostaw projektu przez klienta. Tabela 13 wymienia możliwe charakterystyki: otrzymanie dostawy i datę, dostarczone elementy, walidację ustalonych kryteriów odbioru, otwarte sprawy i podpisy klienta/kierownika. Nie jest to lista obowiązkowych pól naszego nowego formularza. PM.04.01 opisuje uzyskanie podpisu, a PM.04.02 przechowanie rekordu w repozytorium; tekst zawiera też wyjątek dotyczący odbiorców rynku masowego.
- Rozdział 9 pozwala łączyć i dzielić informacje stosownie do potrzeb oraz przechowywać je w narzędziu elektronicznym. Nie wymaga osobnego pliku na każdy WP. Dlatego karta może prezentować informacje z kilku produktów pracy, a zapis decyzji pozostaje osobno identyfikowalną informacją.
- Wykorzystanie podobnego zapisu do odbioru pojedynczego przyrostu jest naszym dostosowaniem. WP.01 opisano przy odbiorze dostaw projektu, nie jako obowiązkowy formularz każdej funkcji lub zadania. Powiązanie z konkretnymi rewizjami i gotowy tekst wiadomości to nasze mechanizmy, nie nazwana w normie „karta operatora”.

Przed decyzją karta przedstawia podstawę i rekomendację. Po decyzji zapis odbioru wskazuje, co przyjęto; karta może ten zapis wyświetlać. W A-11 utrwalono tylko wypowiedź w ćwiczeniu, nie rzeczywisty WP.01 dostawy TextStats.


## 8. Karta i zapis odbioru — konkretny przykład z istniejących eksportów

2026-11-08, objaśnienie na U „Dalej”. Odczytano istniejące eksporty, bez wykonania nowego polecenia w silniku.

| Informacja | Przed odbiorem: 07-show, sprawa 7 / stan 6 | Po fikcyjnym odbiorze w zapisanym scenariuszu: 10-show, sprawa 7 / stan 7 |
|---|---|---|
| Bieżąca podstawa | CAP-01@2, AT-01@3, CODE-01@3 | Te same rewizje |
| Zapis odbioru | acceptance = null | commandId = accept; stateVersion = 7; basis = ten konkretny zestaw rewizji |
| Powód w zapisie | Brak | „FIKCYJNY odbiór, nie decyzja użytkownika” |
| Oczekujące zadanie | accept, OPERATOR | Brak aktywnych zadań tej sprawy |

Źródła: [07-show.json](../flowable-trial/evidence/f5-restart/07-show.json), [10-show.json](../flowable-trial/evidence/f5-restart/10-show.json), ChangeProcess.execute / gałąź Decide. Ten późniejszy stan pochodzi z wcześniejszego scenariusza F5; nie powstał wskutek dzisiejszej odpowiedzi użytkownika.

Karta jest odczytem tych danych. Decyzja w rozmowie ma osobny zapis Z-55 i nie została przesłana do silnika. Mechanizm wiązania odbioru z wersjami już istnieje: zaakceptowana komenda tworzy Acceptance z podstawą i zapis polecenia. Chroni to przed automatycznym uznaniem nowej rewizji za odebraną. Nie dowodzi merytorycznej poprawności produktu ani tożsamości człowieka; role są symboliczne w tej próbie.

Nie jest potrzebne przepisywanie karty do nowego dokumentu po każdej decyzji: widok powinien pokazać istniejący zapis odbioru. Nie dodano teraz połączenia rozmowy z API ani nowego mechanizmu zgód.
