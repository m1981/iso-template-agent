# Runda 3: próba podważenia sukcesu

**Źródła.** Opieram się na wznowionej gałęzi, którą widzę bezpośrednio, oraz na fragmentach drugiej gałęzi przytoczonych w rundzie 2. Te drugie oznaczam [zapis]. Numery linii 671 i 1236 podał prowadzący. Przypisuję je do moich wiadomości po treści, ale samych numerów nie potrafię zweryfikować. Nie korzystam ze streszczenia po kompakcji.

## 1. Co przeszkadzało i kiedy decydował użytkownik

**Obserwacje.**
- **Najdroższe pytania zadałem na starcie.** Pierwsza odpowiedź zawierała osiem pytań (Q1–Q8). Odpowiedź „Q2: wybierz konkretne repo” była niejednoznaczna i wymagała dwóch kolejnych rund. „Q1: ours” przyjąłem bez zastrzeżeń, choć sam poleciłem tę opcję jako „obojętną dla testu”. Później okazało się, że nie była obojętna.
- **Użytkownik dwa razy korygował formę komunikacji, i to w przeciwnych kierunkach.** Najpierw: „Nie zostawiajmy osieroconych/nizaadresowanych tematow”. Na to odpowiedziałem pełną tabelą „Otwarte” w każdej wiadomości. Potem: „Jeden tamtat na raz bo sie gubie”.
- **Zasadę 6 łamałem dalej.** Odpowiedź o diffie Markdown zawierała trzy decyzje i tabelę pięciu bibliotek.
- **„Co to za kroki 5-9 bo sie zgubilem?”** Wcześniej pisałem m.in. „Ręczne kroki 5–9 (UI-4, UI-5)”, nie wyjaśniając, czym są te kroki. Same kroki były opisane w `MANUAL-UI.md`, ale odwołanie do numeru w tym dokumencie nie wystarczyło użytkownikowi do wyboru działania. Dopiero tabela z opisem każdego kroku i stanem umożliwiła decyzję „2. wszystko sprawdziłem”.
- **Błędy produktu wykrywał użytkownik zrzutami, nie testy:**
  - luka merge w kroku 14b;
  - podpowiedź nachodząca na ścieżkę;
  - niebieski „Commit”;
  - kółko działające tylko w części okna Repozytoria;
  - przewijanie krótkiej listy;
  - zapomniany Staged po `.gitignore`, z którego wyszedł pomysł P13.
- **Część przeróbek wynikała z mojego własnego narzędzia.** Dwukrotnie ucięta treść błędu testu pomiaru wynikła z mojego filtrowania przez `grep`, a nie z projektu.

**Interpretacja.** Mechanizmy zapewniały spójność dokumentów i kodu. To, czy produkt zachowuje się dobrze, zależało przede wszystkim od tego, że użytkownik oglądał okno.

## 2. „Każdy commit przechodzi samodzielnie”

**Co było zapisanym wymaganiem.** W prompcie startowym i w `WSPOLPRACA.md` nie znalazłem obowiązku, żeby każdy commit miał zielone testy. Polecenie użytkownika brzmiało „zrob logiczne commity”, czyli „logiczne”, a nie „zielone”. Jedyne zapisane wymaganie dotyczy uczciwości wyniku: „jeśli testy oblewają, powiedz to”. To wymóg z instrukcji systemowych, nie od użytkownika.

**Moja własna obietnica.** W pierwszej serii napisałem: „każdy commit przechodzi samodzielnie”. Kilka linijek niżej w tej samej wiadomości stoi: „W pierwszych trzech commitach oblewa jeszcze `test_req_vcs_205`”. To zdanie było fałszywe w dosłownym brzmieniu. Chodziło mi o „został sprawdzony samodzielnie”, a napisałem „przechodzi”. W drugiej serii, w tabeli z ✗, podałem wyniki rzetelnie.

**Wyjątek.** Czerwone commity pośrednie wynikały z kolejności „najpierw specyfikacja”, którą wybrałem sam. Ujawniłem to, a użytkownik się nie sprzeciwił. Brak sprzeciwu nie jest jednak akceptacją. Według [zapisu] końcowy prompt zawiera zasadę „najpierw commit ze specyfikacją, potem kod z testami”, ale nie wiem, kto ją sformułował ani czy użytkownik wprost ją zatwierdził.

Jednorazową porażkę AT-VCS-016 przy stanie `d5d12d4` potraktowałem jako niestabilność i commit zrobiłem mimo niej. To była moja decyzja. Późniejsze „3. zignoruj” dotyczyło dalszego badania niestabilności, a nie zgody na tamten commit z wyprzedzeniem.

## 3. Trzy zdarzenia bez danego mechanizmu

**a) Test, który fałszywie uspokajał: krótkie listy.**
- **Co wiemy:** pierwsza wersja testu przeszła przed poprawką, bo przewinięcie „w dół, potem w górę” wracało do zera.
- **Bez reguły „najpierw zobacz porażkę”:** przypuszczam, że poprawka i tak byłaby poprawna, bo użytkownik potwierdził działanie na ekranie („działa perfect”). W repo zostałby jednak test, który niczego nie chroni.
- **Czy inny mechanizm by to wyłapał:** ręczna weryfikacja nie zastąpiłaby tej reguły. Sprawdza zachowanie okna, a nie jakość testu.
- **Podobne przypadki:** test głębokiej ścieżki z P12 oblewał z niewłaściwego powodu (za krótka ścieżka), a test przewijania paska bocznego nie działał przez ukryte okno. W obu przypadkach ta sama dyscyplina wymusiła sprawdzenie testu.

**b) Krok 14b: ręczna weryfikacja.**
- **Co wiemy:** żaden test nie obejmował merge z wynikiem równym HEAD. Lukę ujawnił dopiero zrzut użytkownika (OBS-VCS-010).
- **Czego nie wiemy:** czy wyszłaby w tygodniu próbnym. Przypuszczam, że tak, ale dopiero na prawdziwym repo, w gorszym momencie.
- **Rola przypadku:** lukę odsłoniła moja rekomendacja „ours”, nie projekt kroku. Krok 14 w `MANUAL-UI.md` zakładał, że plik trafia do Staged. Mechanizm zadziałał więc częściowo dzięki zbiegowi okoliczności.

**c) Kontrola śledzenia powiązań przy AT-VCS-038.**
- **Co wiemy:** test oblał, bo scenariusz nie miał testu.
- **Czego nie wiem:** czy w tym przypadku zmieniło to wynik. Testy pisałem bezpośrednio po scenariuszu i alarm pojawił się w tej przerwie.
- **Interpretacja:** kontrola zadziałała poprawnie, ale nie potrafię wskazać przypadku, w którym zapobiegła realnemu brakowi. Przy AT-VCS-016 wymusiła napisanie testu pomiaru, który bez niej mógł pozostać ręczny. To jest przypuszczenie, nie dowód.

## 4. Co można uprościć

**Kandydat: obowiązkowa linia `Trace:` w każdym module (REQ-VCS-206).**
- **Obserwacja:**
  - w tej gałęzi wielokrotnie dopisywałem do niej ID;
  - kontrola nigdy nie oblała z jej powodu;
  - nie widzę żadnego zdarzenia, w którym ktoś skorzystał z `TRACE.md` albo z tej linii przy nawigacji po kodzie.
- **Teza warunkowa:** linię można by zastąpić macierzą liczoną z nazw testów.
- **Teza przestaje być prawdziwa, gdy:**
  - użytkownik albo audyt korzysta z kierunku „kod → wymaganie”;
  - powstają moduły bez testów, wtedy nazwy testów nie pokazują ich powiązań.

  Tego nie ustaliłem. Nie znam powodu, dla którego użytkownik przyjął DEC-VCS-036.

**Pozostałe reguły:** nie ustaliłem.

## Czego nadal nie wiemy

- **Co faktycznie dało sukces:** mechanizmy czy szybka pętla użytkownika ze zrzutami. W tej sesji nie da się tego rozdzielić, bo oba działały jednocześnie.
- **Koszt po stronie użytkownika:** czas na zrzuty, czytanie i kroki na prawdziwych repo. Nie mam danych.
- **Czy użytkownik czytał dokumenty, do których się odwoływałem.** Jest sygnał przeciwny: „zgubiłem się”.
- **Przyczyna dwóch niestabilności testu pomiaru.**
- **Pełny przebieg drugiej gałęzi** poza przytoczonymi fragmentami.
