# Kontrakt pełnego cyklu wydań — model v0.7

2026-10-29 · D-84 · realizacja [planu i kryteriów RC-01–07](release-cycle-plan.md). Kontrakt opisuje istniejący model. Oczekiwania poniżej zapisano przed wykonaniem nowych prób; późniejsze korekty oznaczono. Wyniki są w osobnym raporcie.

## 1. Co jest przedmiotem procesu

**Produkt roboczy** ma ID, wersję, stan i zależności. **Wydanie** ma własny numer, zakres ID, stan, migawkę i zapis odbioru. Zmiana produktu po odbiorze nie zmienia zapisanej migawki. Wskaźnik `current_release` wskazuje najnowsze wydanie; globalne `next_release_required` wymusza jego otwarcie po zmianie objętej regułą.

To trzy odrębne rzeczy: zmiana produktu, otwarcie rekordu następnego wydania i jego odbiór. W06 jest technicznym krokiem agenta; nie zatwierdza zmiany ani odbioru.

Źródło: [model](../../../iso-model-state/model/process.yaml), `release_variables`, `release_control_variables`, `release_semantics`; [własności](../../../iso-model-state/docs/WLASCIWOSCI.md), „Semantyka wielu wydań”. Numery i nazwy niżej są identyfikatorami przyjętej interpretacji, nie etapami nakazanymi wprost przez ISO.

## 2. Wspólny kontrakt wykonania

`execute_step(model, state, event, inputs)` zwraca kopię before/after i rekordy albo wyjątek. Nie zmienia argumentów. Źródło: [wykonawca](../../../iso-model-state/src/isomodel/execution.py), `execute_step`, `_check_evidence`, `_check_bounds`.

- Każda operacja sprawdza schemat wejścia, obsługiwane wyrażenia i pola; potem aktora, priorytet W06, przedmiot/argumenty, stan, guard i wymagany dowód. Dopiero później stosuje skutki i obserwatory do kopii oraz sprawdza granice badania.
- `next_release_required=true` blokuje każdy krok poza W06, również pytania i przeglądy. Powód odmowy to `pending_release`, niezależnie od guard konkretnej operacji.
- Błędny aktor / stan / guard / dowód daje `StepRejected` z odpowiednim kodem; niepoprawne dane dają `InputError`; przekroczenie bounds daje `ExplorationBoundary`. Ostatnich dwóch nie liczymy jako odmowy wynikającej z polityki procesu.
- Nieobsługiwana semantyka lub składnia modelu jest osobnym `UnsupportedSemantics`, a nie wykrytym naruszeniem reguły procesu.
- Pola niewymienione w skutkach pozostają bez zmian; skutki zagnieżdżonych P00 i obserwatorów należą do tego samego kroku. Błąd nie zostawia częściowej zmiany ani zużytej zgody.
- Dowód symulacyjny wymaga `simulation: true`. W04 wymaga niepustego `quote`, W07 — `decision` i `quote`. To kontrola danych demonstracyjnych, nie autentyczności zgody.
- `tests_ok`, `checks_ok`, jednoznaczność i wynik odpowiedzi są wejściami abstrakcyjnymi. Model nie uruchamia testów i nie interpretuje naturalnego języka cytatu.

## 3. Siedem kontraktów W

Wszystkie W poza W06 dotyczą wyłącznie `releases[current_release]`. „Bez zmian” uwzględnia wspólny kontrakt powyżej.

| ID / aktor | Stan i wejścia | Warunek dodatkowy | Skutek i rama | Istotna odmowa |
| --- | --- | --- | --- | --- |
| W01 / A | in_preparation; `tests_ok` | Każdy element zakresu: baselined/deferred/superseded/withdrawn, a baselined bez suspect; tests_ok; brak open/asked blocking w całej kolejce | state=ready; produkty, pytania, zakres, migawki i historia bez zmian | Niedokończony zakres, suspect, false test lub blocker → guard; również pusty zakres wymaga testów i braku blokad |
| W02 / R | ready; brak dodatkowych argumentów | true | state=reviewed; pozostałe pola bez zmian | A zamiast R → actor; in_preparation → state. Nie wymaga osobnego raportu recenzji w obecnym YAML |
| W03 / R | ready; `findings`: lista nowych ID pytań | true; poprawne dane i reguła zagnieżdżonego P00 | state=in_preparation; dla każdego ID nowe open/general/blocking, age zgodnie z kolejnością; produkty i scope bez zmian | Błędny typ/duplikat/istniejące ID → input; nieuprawniony aktor → actor; za dużo pytań → boundary. Pusta lista jest legalna i nie tworzy pytań |
| W04 / U | reviewed; dowód symulacyjny z quote | Brak open/asked blocking w całej kolejce | state=accepted; własna snapshot zakresu, acceptance z numerem i cytatem; produkty i inne wydania bez zmian | Późne blocking → guard; brak quote → evidence; ready → state; A → actor. Nie odczytuje ponownie tests_ok |
| W05 / U | reviewed; `question`: nowe ID | true; reguła zagnieżdżonego P00 | state=in_preparation; jedno nowe open/general/blocking; pozostałe produkty i scope bez zmian | A → actor; ready → state; niepoprawne/ponowne ID → input |
| W06 / A | accepted; target=new_release | next_release_required | Nowy numer n+1, state=in_preparation, osobna kopia scope, snapshot/acceptance=none; current_release=n+1; pending=false. Cały stary rekord identyczny | Bez zmiany wymagającej wydania → guard; U → actor; limit wydań → boundary, nie błąd procesu |
| W07 / U | in_preparation; `item`=następca; decision+quote | Następca poza scope, baselined bez suspect; predecessor istnieje, superseded i jest w scope; wszystkie deps następcy w scope | scope powiększone wyłącznie o ID następcy; poprzednik pozostaje w zbiorze; pozostałe pola bez zmian | Niedojrzały następca / brak właściwego poprzednika → guard; A → actor; reviewed/accepted → state |

Źródła: model `release_transitions` W01–W07; `release_semantics.frame`; implementacja zagnieżdżonych ustaleń i testy [W03/W05](../../../iso-model-state/tests/test_release_findings.py). W07 nie przepina zależności: robi to późniejsze T14 na szkicu. Niezmienność accepted dotyczy konkretnego numeru, nie zakazu dalszej pracy.

## 4. Wpływ T, P i obserwatorów

| Wyzwalacz | Warunek i skutek istotny dla wydania | Co nie dzieje się automatycznie |
| --- | --- | --- |
| T05 otwarcie zmiany | U, zgoda na dokładne ID/wersję/T05; zużycie zgody, nowa wersja draft, zależni suspect, invalidate_release | P02 z samą zgodą nie zmienia produktu ani wydania |
| T06 podważenie / T07 zastąpienie / T08 wycofanie | T06 tylko typ bez wymogu approval; T07 wymaga własnej zgody; zmiana i zależni suspect; invalidate_release | T07 nie tworzy następcy; T08 nie naprawia jego zależnych |
| T09 odłożenie / T10 wznowienie | U; T09 draft/verified → deferred, T10 deferred → draft; invalidate_release; T10 zachowuje wersję i licznik odrzuceń | Odłożenie nie jest odbiorem, a wznowienie nie dziedziczy gotowości |
| T11 / T12 / T13 | Ocena bez wpływu czyści suspect przy dojrzałych zależnościach; T12 tworzy wniosek; T13 czyści suspect szkicu | T11 nie naprawia zależności do superseded; nie zwalnia z wymuszonego W06 |
| T00 następcy → T01/T02/T04 → W07 → T14 | Następca ma właściwy predecessor; po baseline U włącza go do scope. T14: tylko draft i in_preparation, następca baselined bez suspect, a dla elementu w scope także następca w scope; właściwa krawędź, typy, brak cyklu; zależni z grafu pre stają się suspect | Predecessor nie jest krawędzią budowania; W07 nie usuwa starego ID; T14 nie zwiększa wersji ani nie czyści suspect |
| invalidate_release(e) | Jeśli e w scope: ready/reviewed → in_preparation; accepted → pending=true bez zmiany starego rekordu | Sama zmiana spoza scope nie musi unieważniać wydania |
| Nowe suspect w scope po dowolnym kroku | Obserwator cofa ready/reviewed albo ustawia pending przy accepted; działa także dla wpływu spoza scope | Nie przepisuje historycznej snapshot |
| P00/P01/P02 | Zgłoszenie, jedno pytanie naraz, jednoznaczna decyzja; change wiąże ID/wersję/operację i approved/rejected | Brak odpowiedzi ani rejected nie upoważniają do T05/T07 |
| P03/P04/P05 | Niejednoznaczna odpowiedź wraca do open bez DEC; odłożyć wolno tylko nieblokujące; wznowienie do open | Późne blocking samo nie cofa state=reviewed, lecz W04 odmawia. Stan i możliwość wykonania kroku to różne rzeczy |

Szczegóły źródłowe pozostają w YAML, zamiast drugiej kopii wszystkich guard T/P. Ta tabela określa ich połączenie z W, nie pełne mapowanie wszystkich T/P do TLA+.

## 5. Konkretny przebieg i oczekiwania przed wykonaniem

Wykorzystujemy istniejące WIT1, WIT3, WIT5; nie interpretujemy demonstracyjnych cytatów jako zgód operatora tej sesji.

| Punkt WIT5 | Oczekiwany stan |
| --- | --- |
| Po kroku 29: W04 v1 | current=1, wydanie 1 accepted, snapshot a2.version=1 |
| Po kroku 32: P02 | Zgoda q1 na a2/v1/T05; wydanie 1 nadal identyczne; brak pending |
| Po kroku 33: T05 | a2 draft/v2, q1.consumed=true, pending=true; wydanie 1 identyczne |
| Po kroku 34: W06 | current=2, wydanie 2 in_preparation; scope równy v1, snapshot/acceptance=none; pending=false |
| Po krokach 35–37 | a2 baselined/v2; v1 wciąż zawiera a2/v1 |
| Po krokach 38–40 | W01 → W02 → W04 v2; snapshot a2/v2; obydwa accepted; v1 identyczne na każdym kroku po 29 |

**Macierz prób:** legalne W01–W07 (W07 w WIT3); dla każdego odmowa z niewłaściwym aktorem. Dodatkowo W01 z false test i z blockerem; W04 bez przeglądu, bez cytatu i z późnym blockerem; W06 bez pending, próba pominięcia W06 i granica liczby wydań; W07 przed dojrzałością następcy. W03/W05 tworzą blocker i wracają legalnie do odbioru po P01/P02 i nowym W01/W02. Błędne findings nie zmieniają stanu. Wszystkie prefiksy pochodzą z initial_state; nie wstrzykujemy stanów jako dowodu osiągalności.

**Czułość:** mutacja from W04 dopuszczająca ready ma ujawnić odbiór bez przeglądu; guard W04=true ma dopuścić odbiór z blockerem; dodatkowy skutek W06 zmieniający scope starego wydania ma naruszyć równość rekordu v1. Każdy mutant ma rzeczywiście wykonać wadliwy krok. Błąd parsera/wykonawcy nie liczy się jako wykrycie właściwego naruszenia.

**Korekta uprzęży po pierwszej próbie:** mutant M03 używa `release.state := in_preparation` zamiast pustego zbioru scope. Pierwszy wariant ujawnił błąd serializacji zbioru w skrypcie raportującym; nie zaliczono tego jako wykrycia naruszenia procesu. Nowy wariant zachowuje legalny typ pola i nadal bada tę samą własność niezmienności całego starego rekordu. Pierwotna próba: [zapis błędu](evidence/release-cycle-initial-error.txt).

Druga próba dała 33/34: skutek M03 dodany na końcu W06 zmieniał już nowe current, więc nie naruszał starego rekordu. Kontrola słusznie nie zaliczyła wykrycia; [wynik zachowany](evidence/release-cycle-author.json.gz). Docelowy mutant wstawia ten skutek przed zmianą current_release. To korekta konstrukcji mutanta, nie poprawka procesu.

**Uzupełnienie po recenzji, przed ponowieniem:** oczekiwana pełna snapshot W04 ma powstawać z pre.items dla pre.scope, a acceptance z numeru sprzed kroku i cytatu wejściowego. Nie kopiujemy tych oczekiwań z post. Dwa dodatkowe mutanty mają wykonać pustą snapshot oraz błędny numer/cytat acceptance; wyrocznia ramy W04 musi wykryć obie różnice. Rozszerza to czułość sprawdzenia RC-01/RC-06, nie zakres procesu.

## 6. Kontrakt dalszej formalizacji E3

| Element mapowania | Co trzeba odwzorować i sprawdzić |
| --- | --- |
| Stan | items z wersjami/deps/predecessor/suspect; questions z wiekiem, wiązaniem i consumed; releases/current/pending; historia niezbędna do S2/S3/S8/S15 |
| Wspólna relacja | Allowed = poprawne wejście ∧ actor ∧ priorytet pending ∧ from ∧ guard ∧ wymagane dane dowodowe; efekty, zagnieżdżone P00 i obserwatory jako jeden krok. Błędy wejścia osobno od przejść procesu |
| Rama W | Rozróżnić zmieniany current i chronione wcześniejsze numery; W06 dodaje nowy rekord, nie zmienia stanu starego. W07 dodaje jeden ID do scope |
| S7a/S7b/S8/S10 | Kompletność ready/reviewed, kompletność w chwili W04, wcześniejszy przegląd tego samego numeru, identyczność całego odebranego rekordu |
| S11/S12/S13/S14 | Zgoda związana z wersją i zużyta atomowo; legalna naprawa krawędzi; kontrolowane scope; blocker sprawdzany także przy W04 |
| L1 | Osobno AG EF done: dla każdego osiągalnego stanu istnieje ścieżka zakończenia. Zwykły brak deadlock i pięć świadków nie dowodzą tej formuły CTL |
| L5 i F1–F3 | Postęp konkretnego numeru, obowiązkowe W06, trwały odbiór po ustaniu zmian; jawne założenia działań A/R/U. Nie obiecywać zakończenia przy wiecznej bezczynności operatora |
| Bounds | Limit wersji/pytań/wydań opisuje badanie; nie wolno zamienić odciętego W06 w blokadę procesu ani uznać końca głębokości za done |
| Wyrocznia | Oczekiwane ramy i ścieżki wyprowadzone ze źródeł; porównać pełne następniki i rekordy, nie tylko state. Zgodność dwóch implementacji nie wystarcza |

Całe E3 obejmuje także inne G/S/L i pozostałe T/P, wskazane w [planie projektu](../../../iso-model-state/PLAN.md). Ten pakiet nie obiecuje ich dowodu ani gotowego generatora. Model nadal nie wiąże testów z rzeczywistym kodem; W02 bez raportu i symbolicznym R oraz W04 bez ponownego tests_ok są jawnymi ograniczeniami przyszłego użycia operacyjnego.
