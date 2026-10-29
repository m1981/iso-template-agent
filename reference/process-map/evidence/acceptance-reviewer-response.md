Ocena rewizji 1: **dwie usterki doprecyzowania kontraktu, obie średniej wagi**. Nie wykazałem możliwości samodzielnego odbioru przez agenta przy przestrzeganiu całego dokumentu.

Oceniony plik: `reference/process-map/acceptance-contract.md`, SHA-256 `af57fe8527375da03263bcbe3dccd79787c99a0bc15531f094774bd620f8c3fc`.

1. **R1 — końcowy poprzednik przy istniejącym aktywnym zgłoszeniu. §4 i §6, linie 106–110.**

   Ślad: S1 jest `rejected` → agent tworzy S2 jako następcę S1 → S2 jest `submitted` → agent, z aktualnym tokenem i spełnionym G, zgłasza S3, ponownie wskazując S1 jako poprzednika.

   Tabela operacji przewiduje utworzenie S3 i pozostawienie końcowego S1 bez zmian. Wyraźna odmowa przy istniejącym aktywnym zgłoszeniu dotyczy tylko żądania **bez** poprzednika. Lokalne reguły operacji prowadzą więc do dwóch aktywnych zgłoszeń, sprzecznie z §4. Ogólne ograniczenie w §4 zakazuje wyniku, ale kontrakt nie rozstrzyga tego wejścia.

   **Minimalna poprawka:** jeżeli istnieje aktywne zgłoszenie, poprzednik musi wskazywać właśnie je; każda inna wartość, również ID końcowe, daje `CONFLICT`. Sprawdzenie obejmuje cały przyrost i jest atomowe z utworzeniem następcy. Dopisać scenariusz powyżej oraz dwa równoczesne pierwsze zgłoszenia przyrostu.

2. **R2 — równoczesne identyczne ponowienia mają sprzeczne reguły odpowiedzi. §7, linie 118–122.**

   Ślad: S1 jest `submitted` → dwa identyczne żądania `accept`, z tym samym kluczem, treścią i tokenem, docierają równocześnie → oba odczytują brak zapisanego wyniku ponowienia → pierwsze utrwala odbiór → drugie według ostatniego akapitu dostaje konflikt.

   Reguła ponowień wymaga jednego historycznego wyniku dla tego klucza; reguła konkurencji nakazuje drugiemu zapisowi konflikt. Dodatkowo odmowa dziedzinowa zużywa klucz, więc nie wiadomo, jak zachować konflikt bez przypisania temu samemu kluczowi drugiego wyniku. S09 obejmuje ponowienie po zakończonym zapisie, nie ten wyścig.

   **Minimalna poprawka:** rozróżnić konkurujące **różne** żądania od identycznych żądań o wspólnym kluczu. Te drugie współdzielą jedno wykonanie i wynik; podczas wykonania mogą dostać jawny wynik przejściowy wymagający ponowienia, który nie utrwala odmowy dziedzinowej. Kontrola klucza i zapisu wyniku musi obejmować równoczesne wywołania. Dopisać scenariusz z utratą pierwszej odpowiedzi i ponowieniem przed zakończeniem pierwszego wywołania.

Pozostałe wymagane granice są zapisane poprawnie:

- **Odrzucenie mimo braków:** §6 nie wymaga G dla `reject`. Warto rozszerzyć S14 o `unknown` spowodowane niedostępnością źródła; odczyt powinien nadal umożliwiać odrzucenie zachowanego zgłoszenia z aktualnym tokenem.
- **Nowa wersja bez dziedziczenia odbioru:** §4, §7 i S18 wiążą odbiór z konkretną podstawą i przewidują nowe zgłoszenie.
- **Historia a aktualna gotowość:** §7 wyraźnie rozdziela historyczne `accepted`, bieżące ustalenia i historyczny wynik ponowienia.
- **Role i milczenie:** §4–5 wymagają jawnej decyzji operatora, a pochodzenie uprawnień ustala system.
- **Źródła normatywne:** lokalne PM.04.01 i WP.01 uzasadniają odniesienie do odbioru, lecz nie narzucają tego API. §1 prawidłowo oznacza adaptację i fakultatywny charakter listy cech WP.01. Przywołanie kontroli uprawnień po stronie systemu odpowiada [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html).

Granice oceny: wyłącznie odczyt i analiza dokumentu oraz przywołanych źródeł; bez zmian, testów API, VER/ACC i delegowania. Q1–Q4 są jawnie odłożonymi wyborami źródeł, technologii i modelu zagrożeń — nie traktuję ich jako usterek tej propozycji. R1–R2 dotyczą semantyki niezależnej od tych wyborów. Osobny kontekst recenzenta nie dowodzi niezależności poznawczej ani kompletności przeglądu.
