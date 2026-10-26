# Runda 4: model wobec zdarzeń sesji

**Źródła:**
- **Sesja:** wznowiona gałąź, którą widzę bezpośrednio, oraz fragmenty drugiej gałęzi z rundy 2, oznaczone [zapis].
- **Linie 1003, 1008, 1016 i 1065:** to dowody podane przez prowadzącego. Treść pasuje do tego, co widzę, ale numerów linii nie weryfikuję.
- **Model:** znam go wyłącznie z opisu powyżej, oznaczam go [opis]. Nie mam dostępu do `process.yaml`.

## 1. Sens modelu własnymi słowami

**Działający model:**
- To maszyna stanów produktów (PLAN, REQ, AT, DES, CODE) z wersjami, zależnościami i flagą „podejrzany” (suspect).
- Przejścia zależą od roli: agent weryfikuje, a człowiek zatwierdza, tworzy baseline i odbiera wydanie.
- Działa na danych symulacyjnych: `checks_ok` i `tests_ok` to dane wejściowe, a nie odczyty z prawdziwego repo.

**Proponowane zastosowanie** (jeszcze niewdrożone):
- mapa projektu i karta przyrostu, które odsyłają do istniejących źródeł;
- rozdzielenie oceny od wykonania, z oceną przypiętą do konkretnej wersji materiału;
- adapter czytający raporty z repo;
- osobny recenzent.

Model nie ocenia, czy raport jest prawdziwy ani czy ludzka decyzja jest trafna.

## 2. Trzy zdarzenia w języku modelu

**a) Merge z wynikiem równym HEAD (krok 14b, OBS-VCS-010).**
- **Produkty:**
  - REQ-VCS-024, zatwierdzony;
  - nowy REQ-VCS-027;
  - DES-VCS-046;
  - zmieniony DEC-VCS-048 (zmieniły go DEC-VCS-065 i 069);
  - CODE: `status.py`, `repo.py`, `model.py`, `sidebar.py`.
- **Zmiana:** zaakceptowana reguła „bez wykrywania merge” przestała obowiązywać.
- **Decyzja człowieka:** „Q9: a”, potem „P11a i P11b tak 11c tak”.
- **Co trzeba by zapisać:** zgodę na konkretny element, wersję i operację, a do tego flagi suspect na zależnych modułach.
- **Co model by wykrył:** moduły zależne od zmienionego DEC lub REQ. Ręcznie dopisywałem „Zmienione przez DEC-VCS-065” i aktualizowałem linie `Trace:`. Model zrobiłby to systematycznie.
- **Co zostaje poza modelem:**
  - samo odkrycie luki, które przyszło ze zrzutu użytkownika;
  - to, że lukę odsłoniła moja słaba rekomendacja „ours”.
- **Brak informacji:**
  - DEC nie jest typem produktu w [opisie], więc nie wiem, gdzie trafiają decyzje z cytatem;
  - nie wiem, gdzie trafiają `UI-REFERENCE.md`, makiety HTML i `MANUAL-UI.md`.

**b) Fałszywie uspokajający test krótkich list (linie 1003, 1008, 1016).**
- **Produkt:** CODE `file_list.py` i `sidebar.py` oraz test DES-VCS-023.
- **Wynik sprawdzenia:**
  - linia 1003: błędny test przechodzi;
  - linia 1008: poprawiony test oblewa z `assert 10.0 == 0`;
  - linia 1016: pełny zestaw daje 302 passed.
- **W modelu:** gdybym podał `checks_ok=true` po pierwszym przebiegu, T01 zweryfikowałby CODE.
- **Wniosek:** model tego nie wykrywa. Proponowane „ocena przypięta do materiału i wersji kryteriów” pomoże tylko wtedy, gdy kryterium będzie obejmować dowód porażki przed poprawką. Tego [opis] nie mówi. Ten błąd złapała reguła tekstowa TDD i moja dyscyplina.

**c) Commity na polecenie i moja fałszywa formuła.**
- **Zdarzenie:** „zrob logiczne commity na moje polecenie teraz”.
- **W modelu:** to T04, czyli baseline robiony przez człowieka z commitem jako dowodem. Polecenie użytkownika do tego pasuje.
- **Czego model nie obejmuje:**
  - moje zdanie „każdy commit przechodzi samodzielnie” w tej samej wiadomości co „oblewa `test_req_vcs_205`”;
  - `git reset -q` na indeksie.

  W02 ma warunek `true`, więc raport nie byłby sprawdzony.
- **Brak informacji:**
  - czy T04 wymaga `tests_ok`;
  - czy baseline odpowiada jednemu commitowi, czy całej serii;
  - jak model traktuje celowo czerwone commity pośrednie: śledzenie powiązań oblewa, bo specyfikacja idzie pierwsza.

  Z opisu tego nie rozstrzygnę.

**Zdarzenie, które model może utrudnić: zmiana REQ-VCS-017 dla `.gitignore`.**
- **Co się stało:** jedna odpowiedź „D1 i D2 zgodnie z rekomendacja” objęła trzy rzeczy: nową decyzję o zaznaczaniu, termin trzech etapów i zmianę zaakceptowanego REQ-VCS-017.
- **Co wymagałby model:** zgodę na konkretny element i wersję, której nie używa się ponownie. To oznacza osobne potwierdzenie albo zgodę wymieniającą elementy.
- **Skutek propagacji:** według TRACE.md z REQ-VCS-017 zależą moduły `model.py`, `difftool.py`, `gitcli.py`, `repo.py`, `settings.py` i `settings_dialog.py`. Wszystkie dostałyby flagę suspect i wymagałyby przeglądu „bez wpływu”, choć dopisanie `.gitignore` dotyczy tylko `repo.py` i `model.py`.
- **Przypuszczenie:** przy tempie tej sesji, kilka przyrostów dziennie, to głównie dodatkowe zapisy, a nie dodatkowa kontrola.

## 3. Co rozwiązuje, czego nie obejmuje, ile kosztuje

**Rozwiązuje:**
- **Jeden temat na wiadomość:** kolejka z limitem jednocześnie zadawanych pytań zamienia zasadę 6 z `WSPOLPRACA.md`, którą łamałem, w ograniczenie, które da się sprawdzić.
- **Zmiany zaakceptowanych reguł:** w sesji pilnowałem ich wyłącznie przez dopiski w SPEC.md. W modelu mają ślad przez flagę suspect.
- **Granica commitu:** model ją zapisuje, bo baseline robi tylko człowiek.

**Nie obejmuje:**
- prawdziwości moich raportów;
- jakości testów (zdarzenie b);
- błędów widocznych tylko na ekranie, czyli sześciu wykrytych zrzutami;
- niejednoznacznych odpowiedzi („Q2: wybierz konkretne repo”);
- operacji gita na indeksie;
- niestabilnego testu;
- utraty narzędzi pracy, np. `stage_parts.py`.

**Ryzyko dla problemu „zgubiłem się”:** proponowane widoki „odsyłają do źródeł zamiast dublować treść”. To samo zawiodło przy „kroki 5–9”: numer w dokumencie nie wystarczył użytkownikowi, pomogła dopiero tabela z opisem każdego kroku. Mapa z samymi ID powtórzy ten problem. Czasu pracy nie mam jak oszacować.

## 4. `Trace:` w module a macierz z nazw testów

**Obserwacja.**
- Nazwa testu daje powiązanie test → wymaganie, ale nie test → moduł.
- Kolumna „Moduły” w TRACE.md powstaje, o ile pamiętam działanie programu sprawdzającego, z linii `Trace:`. Tego programu nie czytałem w tej gałęzi, więc to niepewne.

**Zastąpienie informacji** (macierz liczona z czegoś innego):
- **Importy testów albo pokrycie kodu per test:** dają przybliżone powiązanie test → moduł, a przez nazwę testu moduł → wymaganie.
- **Pierwsza wada:** wyniki byłyby zbyt szerokie. Testy okna (`MainWindow`) dotykają prawie wszystkich modułów, więc każdy moduł UI dostałby dziesiątki wymagań.
- **Druga wada:** moduł bez testu nie dostałby żadnego powiązania.

**Świadoma rezygnacja:**
- tracimy kierunek kod → wymaganie;
- traci się też wejście do mechanizmu suspect. W modelu CODE ma `depends_on`. Bez `Trace:` albo równoważnego zapisu nie da się ustalić, które moduły oznaczyć po zmianie REQ.

**Korekta rundy 3.** Wniosek „można zastąpić” był za mocny. W kontekście tego modelu linia `Trace:` jest raczej danymi wejściowymi niż zbędnym kosztem. Brakuje w niej jednak wersji elementów, a model ich wymaga. To nowa luka.

## Czego nie wiem

- Jak model reprezentuje DEC, wzorzec UI i ręczną listę kontrolną.
- Warunków T04.
- Czy kolejka pytań rozróżnia jedną zgodę obejmującą wiele elementów.
- Formatu zapisów dla adaptera.
