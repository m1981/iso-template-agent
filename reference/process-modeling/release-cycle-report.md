# Wynik mapowania cyklu wydań

2026-10-29 · D-84 · **mapowanie wykonane i sprawdzone; gotowe do odbioru U, nie odebrane**. [Plan i kryteria](release-cycle-plan.md), [kontrakt](release-cycle.md).

## Wynik dla operatora

Opisano wszystkie W01–W07 i ich związki ze zmianami, pytaniami i ponownym przeglądem. Przebieg dwóch wydań zachowuje cały wcześniejszy odbiór, a nowy odbiór dotyczy nowej migawki. Pokazano także odmowy oraz powroty po uwagach R i odmowie U.

**36/36 oczekiwań autora odtworzonych przez osobnego recenzenta, pięć celowych usterek wykrytych z właściwego powodu, sześć dodatkowych przebiegów recenzenta zgodnych z jego oczekiwaniami.** To sprawdzenie mapowania i wybranych ścieżek. Nie jest dowodem wszystkich kombinacji, żywotności ani zakończeniem E3. Nie zmieniono kodu ani reguł `iso-model-state`.

## Przedmiot dowodu

- SHA-256 pliku `model/process.yaml`: `2d329822e239555c1642d0a5a20aae0eb28fee17a6f2ff13968e48d7f428fc07`.
- SHA-256 [skryptu końcowego](release_cycle_probe.py): `1e1acefd48c1a465f95ae47c44c937285eb460ae25a2f850bbebef51e92272d9`.
- [Wynik autora v4](evidence/release-cycle-author-v4.json.gz) i [odtworzenie R](evidence/release-cycle-reviewer.json.gz): identyczne bajty, SHA-256 `9414e49fe5305e387390dd735e67575f84ac985c38dfabd0582d511174b4887b`.
- [Dodatkowe próby R](evidence/release-cycle-reviewer-extra.json.gz): SHA-256 `c8049b7faba162d67f2103df594fa0103085a6923d15a1450c576cc2284a46e3`.

Wyniki zawierają hashe źródeł, pełne before/after, zdarzenia, kontrole i odmowy; dodatkowe próby R zawierają także komplet modeli/scenariuszy. Model i kod badano na kopii. Dowody przeniesiono z katalogu roboczego R do tego repozytorium; nie wymagają zachowania `/private/tmp`.

## Rozliczenie kryteriów

| Kryterium | Wynik techniczny | Dowód i granica |
| --- | --- | --- |
| RC-01: pełne kontrakty W | Spełnione | Kontrakt §2–3; siedem legalnych W i siedem odmów niewłaściwego aktora; rama oraz pełna snapshot/protokół W04; recenzja źródeł |
| RC-02: dwa wydania | Spełnione | WIT5: identyczny cały rekord v1 na każdym kroku 30–40; q1 zużyte; W06 ma nowy rekord bez odbioru; snapshot a2 v1/v2 rozdzielone |
| RC-03: odmowy i powroty | Spełnione | Dokładne powody actor/state/guard/evidence, input i boundary rozdzielone; W03/W05 tworzą blocker, blokują gotowość i wracają przez P01/P02/W01/W02 do odbioru; stany odmów identyczne przed/po |
| RC-04: zależności i wyzwalacze | Spełnione | WIT3: a1/d1 wskazują r3, scope zachowuje r1 i r3; tabela T/P/obserwatorów. R dodatkowo wykonał T10 w trzech fazach i wpływ T08 spoza scope w dwóch fazach |
| RC-05: granica formalizacji | Spełnione jako mapowanie | Kontrakt §6 rozlicza relację, ramę, S/L/F i bounds; nie wykonano generatora/TLC ani dowodu CTL |
| RC-06: czułość oczekiwań | Spełnione | M01 odbiór bez reviewed, M02 z blockerem, M03 zmiana starego rekordu, M04 pusta snapshot, M05 zły protokół; rzeczywiste wadliwe następniki sprawdzone przez R |
| RC-07: odtworzenie i recenzja | Spełnione technicznie | Skrypt i trwałe wyniki; odtworzenie 36/36, sześć własnych prób R, uwagi poniżej rozliczone; kontrole dokumentów zapisane na końcu |

Spełnienie RC oznacza gotowość do odbioru **tego mapowania**. Nie nadaje odbioru symulatorowi L1, N1–N3, całemu E3 ani rzeczywistemu produktowi.

## Recenzja i korekty

Recenzent: osobna sesja `/root/review_release_cycle`, uruchomiona bez historii rozmowy. Najpierw wyprowadziła przypadki ze źródeł, potem przeczytała kontrakt; przed końcowym odtworzeniem otrzymała wyniki autora i opis korekt. Nie była ślepa na wyniki w całej recenzji. Nie zmieniała źródeł i nie udzielała odbioru za U.

| Uwaga R | Rozstrzygnięcie |
| --- | --- |
| Oddzielić UnsupportedSemantics od InputError | Dopisano do wspólnego kontraktu |
| Ujawnić dojrzałość następcy i warunek scope w T14 | Dopisano do tabeli wpływu |
| **Luka wyroczni W04:** expected.snapshot i expected.acceptance kopiowane z post mogą przepuścić błędną zawartość | Poprawiono: snapshot z pełnych pre.items dla pre.scope, protokół z numeru pre i cytatu wejścia. M04/M05 wykonują błędny skutek i są wykrywane. R potwierdził i zamknął uwagę |

Końcowy wniosek R: „brak otwartych blokerów technicznego zakończenia mapowania”. Oddzielna sesja i własne oczekiwania ograniczają wspólne błędy, ale nie gwarantują niezależności poznawczej. Podczas rzeczywistej recenzji znaleziono i naprawiono błąd testu diagnostycznego, nie reguły modelu.

## Historia prób — bez zastępowania niepowodzeń sukcesem

1. Pierwszy wariant M03 zakończył raportowanie błędem serializacji zbioru. [Zapis](evidence/release-cycle-initial-error.txt); nie liczono jako wykrycia mutanta.
2. [Pierwszy zapisany raport](evidence/release-cycle-author.json.gz): 33/34. M03 zmieniał już nowe current, więc nie naruszał v1; kontrola prawidłowo nie zaliczyła wykrycia.
3. [Wariant v2](evidence/release-cycle-author-v2.json.gz): 34/34 po przesunięciu skutku M03 przed zmianę current_release. Później R znalazł lukę wyroczni W04.
4. Po poprawie wyroczni i dodaniu M04/M05 pojawił się nieobsługiwany literał quote w M05. Pierwsze raportowanie zakładało gotowy następnik i również zawiodło; po korekcie uprzęży zapisano [v3: 35/36](evidence/release-cycle-author-v3.json.gz). Błąd DSL nie został zaliczony jako wykrycie.
5. Wariant v4: 36/36, legalnie wykonane mutanty; osobne odtworzenie R potwierdziło wynik. Sześć dodatkowych prób R ma osobny raport.

Nie opisujemy tej historii jako TDD naprawy produktu. Jest sprawdzeniem istniejących reguł oraz poprawianiem czułości diagnostyki. Nie wykonano pełnej regresji niezmienionego `iso-model-state`.

## Odtworzenie

Z korzenia `iso-template-agent`, w istniejącym środowisku bez instalacji:

```sh
/Users/michal/PycharmProjects/iso-model-state/.venv/bin/python -B reference/process-modeling/release_cycle_probe.py --source ../iso-model-state --output reference/process-modeling/evidence/release-cycle-rerun.json.gz
```

Skrypt odmawia nadpisania wyniku. Źródła kopiuje do nowego katalogu tymczasowego; hashe trzeba porównać z raportem. Przy zmianie źródeł będzie to nowe badanie, nie identyczne odtworzenie. Dodatkowe próby R można odtworzyć przez `replay(case['model'], case['scenario'])` dla każdego wpisu `results` z ich JSON i porównać pełny wynik po serializacji do JSON; nazwy kontroli wskazują oczekiwania recenzenta. Zmieniony scope i limit wydań to jawne osobne instancje.

## Stan i następny krok

- Agent zakończył kroki 1–5 planu mapowania; wynik gotowy do decyzji U, bez automatycznej akceptacji.
- U: odbiór tego ograniczonego pakietu albo wskazanie korekty. Nie jest potrzebna ponowna decyzja o już wykonanym zleceniu.
- Agent po odbiorze: wykorzystać kontrakt w dalszym istniejącym E3 — uszczegółowić mapowanie do generatora, jego instancję, granice i oczekiwania przed zmianą kodu. Nie rozpoczynać nowego API ani ponownie E1/E2. Pozostałe T/P oraz pełne S/L/F nadal należą do otwartego E3.
- Nie wykonano commita ani pusha. D-83 i wcześniejsze analizy zachowują historię; niniejszy raport jest bieżącym punktem wznowienia tego pakietu.

**Aktualizacja 2026-10-30:** U polecił zapis pakietu w commicie i proste wyjaśnienie mapowania. Przygotowano do zapisu kontrakty, diagnostykę, wyniki autora/R oraz zachowane niepowodzenia. Powyższy brak commita opisuje chwilę dostawy; polecenie zapisu w Git nie jest odbiorem D-85. Bez zmian modelu i bez pushu.

## Kontrola dokumentacji

`make check`: kod 0, 251 elementów, 0 błędów; ostrzeżenia W1 MIG-01/MIG-02 oraz W2 D-84 bez wzmianki w commicie. Osobno: dziewięć dokumentów, 143 lokalne odnośniki do istniejących plików/katalogów, domknięte bloki kodu, brak błędów; kotwic nie sprawdzano. Potwierdzono identyczność końcowych plików autora/R, zgodność hasha skryptu i odczyt 36+6 wyników. `git diff --check` bez błędów. Są to kontrole dokumentacji i dowodów, nie pełna regresja produktu.
