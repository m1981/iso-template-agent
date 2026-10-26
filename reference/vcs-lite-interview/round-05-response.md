# Runda 5: rekomendacje do sprawdzenia

**Źródła:** wznowiona gałąź, którą widzę bezpośrednio, i fragmenty drugiej gałęzi przytoczone przez prowadzącego, oznaczone [zapis]. Numery linii pochodzą od prowadzącego i ich nie weryfikuję. Nie korzystam ze streszczenia po kompakcji.

## R1. Raport z serii commitów podaje wynik każdego commita, bez zdania podsumowującego

1. **Zdarzenie:** w pierwszej serii napisałem „każdy commit przechodzi samodzielnie”, a w tej samej wiadomości, że w trzech commitach oblewa `test_req_vcs_205` (linia 671 według prowadzącego). W drugiej serii tabela z ✗ była spójna. Przy `d5d12d4` zrobiłem commit mimo jednorazowej porażki AT-VCS-016.
2. **Problem:** wynik sprawdzenia był rzetelny, ale moje podsumowanie przeinaczało go. Żaden mechanizm nie porównuje raportu z logiem. W02 ma warunek `true`. Wyjątek „czerwone commity pośrednie przy kolejności specyfikacja → kod” nigdy nie został wprost zaakceptowany przez użytkownika.
3. **Najmniejsza zmiana:** stały format tabeli z drugiej serii. Każdy wiersz ma commit, liczbę przechodzących i oblewających testów na stanie indeksu (`checkout-index`, praktyka już opisana w końcowym prompcie [zapis]) oraz ID każdego oblanego testu z przyczyną. Bez zdań typu „wszystko przechodzi”, które mają streszczać tabelę.
4. **Hipoteza i koszt:**
   - **Hipoteza:** znikają sprzeczne podsumowania, a każdy wyjątek jest jawny i można go przypisać do konkretnego commita.
   - **Koszt:** jedna tabela na serię. Logi już są zapisywane do pliku.
   - **Warunek:** dotyczy serii więcej niż jednego commita.
5. **Eksperyment:** przy następnej serii porównać każde twierdzenie raportu z zapisanym logiem i policzyć niezgodności.
   - **Dane bazowe:** obie historyczne serie. W pierwszej jest jedno sprzeczne zdanie, w drugiej żadnego.
   - **Obalenie hipotezy:** niezgodność pojawia się mimo formatu tabeli.
6. **Samodzielnie** mogę zmienić format raportu. **Decyzji człowieka wymaga** polityka: czy czerwone commity pośrednie są dopuszczalne i czy commit z niestabilnym testem jest dopuszczalny.

## R2. Zapisany dowód, że nowy test oblał z właściwego powodu

1. **Zdarzenie:**
   - test krótkich list przeszedł przed poprawką, potem po poprawieniu testu oblał z `assert 10.0 == 0`, na końcu było 302 passed (linie 1003, 1008, 1016);
   - test długiej ścieżki P12 oblał z niewłaściwego powodu, bo ścieżka była za krótka;
   - test grubości czcionki porównywał nazwę czcionki („font3”) zamiast jej grubości.
2. **Problem:** zasada TDD istnieje tylko w tekście. Wynik `pass` nie mówi, czy test w ogóle chroni zachowanie. Według opisu modelu `checks_ok` przyjęłoby pierwszy przebieg. Wszystkie trzy przypadki wychwyciła moja dyscyplina, nie kontrola.
3. **Najmniejsza zmiana:** w raporcie przyrostu przy każdym nowym teście zachowania wpisać linię asercji z pierwszego czerwonego przebiegu i jedno zdanie, czy ta przyczyna odpowiada zgłoszonemu błędowi. Źródłem jest pełny log, który już zapisujemy do pliku. Nowy rejestr nie jest potrzebny.
4. **Hipoteza i koszt:**
   - **Hipoteza:** recenzent albo człowiek może sprawdzić jakość testu bez powtarzania mojej pracy.
   - **Koszt:** jedna linia na test.
   - **Warunek:** nowe zachowanie albo naprawa błędu. Nie dotyczy refaktoryzacji.
5. **Eksperyment:** w następnym przyroście zliczyć nowe testy z zapisaną linią porażki oraz te, w których linia ujawniła złą przyczynę.
   - **Dane bazowe:** trzy przypadki z tej sesji. Z drugiej gałęzi nie mam danych.
   - **Obalenie hipotezy:** zapisane linie nie wykrywają niczego, czego nie wykryłby przegląd samego testu.
6. **Samodzielnie** mogę to zrobić w ramach zatwierdzonego TDD. **Decyzji człowieka wymaga** to, czy recenzent ma ten zapis sprawdzać.

## R3. Odwołania, z których da się wybrać następne działanie

1. **Zdarzenie:** „Co to za kroki 5-9 bo sie zgubilem?” po moim „Ręczne kroki 5–9 (UI-4, UI-5)”. Decyzję („2. wszystko sprawdziłem”) umożliwiła dopiero tabela z opisem każdego kroku. Wcześniej był jeszcze komunikat „Jeden tamtat na raz bo sie gubie”.
2. **Problem, z nowym spostrzeżeniem.** [zapis] Na moją wiadomość z trzema decyzjami o diffie Markdown użytkownik odpowiedział sprawnie: „wersja D1:A tylko bez przekreslen… D2: tak D3: zgodnie z rekomendacja” (linia 1304). Liczba decyzji nie była więc w tym przypadku przyczyną zagubienia. Przyczyną były odwołania do numeru lub ID bez treści. Zasada 6 w `WSPOLPRACA.md` celuje w liczbę tematów, a nie w samowystarczalność odwołań. Proponowane widoki „odsyłają do źródeł” i grożą tym samym.
3. **Najmniejsza zmiana:** każde odwołanie do kroku, ID albo pozycji Punktu wznowienia, które wymaga działania użytkownika, ma w wiadomości jedno zdanie: co to jest i co ma zrobić. Wymaga to dopisania jednego zdania do zasady 4 w istniejącym pliku.
4. **Hipoteza i koszt:**
   - **Hipoteza:** mniej pytań „co to jest”.
   - **Koszt:** dłuższe wiadomości, co działa przeciw celowi „nie przeładować treścią”.
   - **Warunek:** dotyczy tylko odwołań, które wymagają działania, nie odwołań informacyjnych.
5. **Eksperyment:** w kolejnych przyrostach zliczać wypowiedzi użytkownika z pytaniem o znaczenie odwołania albo z sygnałem zagubienia.
   - **Dane bazowe:** dwa takie zdarzenia w widocznej gałęzi. Drugiej gałęzi nie potrafię policzyć.
   - **Obalenie hipotezy:** pytania pojawiają się mimo opisu albo użytkownik zgłasza nadmiar tekstu.
6. **Decyzji człowieka wymaga** zmiana `WSPOLPRACA.md`, bo to jego konwencja. **Samodzielnie** mogę stosować opis odwołań już teraz, bo nie łamie żadnej zasady.

**Świadomie pominąłem:** operacje gita na indeksie (`git reset -q`). Ustaliłem ryzyko, nie stratę, a końcowy prompt [zapis] częściowo to już reguluje.

## Korekty po doprecyzowaniach

- **„Zrób commity” jako T04:** odwzorowanie było moją hipotezą. Zwykły commit nie jest baseline'em. R1 dotyczy więc raportu operacji konfiguracyjnej, a nie przejścia T04.
- **Kolejka a „jeden temat”:** w rundzie 4 twierdziłem, że kolejka zamienia zasadę 6 w egzekwowalne ograniczenie. To było błędne. Kolejka liczy rekordy pytań, a nie tematy w tekście. R3 nie zakłada pomocy modelu.
- **Zgoda grupowa:** napisałem, że model wymagałby osobnych potwierdzeń. Wycofuję to. Jedna wypowiedź może obejmować kilka wskazanych działań, a problemem jest jedynie brak adaptera.
- **Sześć modułów oznaczonych jako suspect:** to była hipoteza z TRACE.md, a nie przebieg modelu.
- **DEC jako produkt:** nie jest produktem. DEC z cytatem to dane dowodowe operacji lub pytania, więc moje pytanie „gdzie trafiają DEC” jest częściowo rozstrzygnięte. Dla UI-REFERENCE i listy ręcznej pozostaje otwarte.
- **Bez zmian:** korekta rundy 4 dotycząca linii `Trace:` (nie „zbędna”, tylko bez wersji).
