# Jakie plany, kiedy i jak je czytać

Przygotowano: 2026-10-22. Zapis w nowym układzie: 2026-10-23. Status: materiał dydaktyczny do [PROPOSAL](../PROPOSAL-CONTEXT-AND-PRACTICE-PACKAGES.md), bez aktywacji nowych praktyk.

## 1. Co jest wzorcem, a co propozycją

Opis WP.10 w lokalnej kopii ISO/IEC 29110 daje podstawę treści planu projektu. Nie narzuca Markdown, nazw plików ani identyfikatorów. Nie przejrzeliśmy w tej rozmowie wypełnionego planu z rzeczywistego projektu wraz z dowodem jego odbioru. Poniższe przykłady są autorską propozycją, a nie oficjalnym wzorem ISO ani dowodem zgodności.

Źródła:

- [Rozdział 9, WP.10 i zasady organizacji produktów pracy](../../../iso-29110-5-1/chapters/09-description-of-work-products.md): cel, zakres, cykl, produkty, zadania, czas, zasoby, zespół, harmonogram, nakład, koszty, ryzyka, wersjonowanie, dostarczenie i zatwierdzenie planu.
- [PM.01 — planowanie](../../../iso-29110-5-1/chapters/06-project-management-pm-process.md): przygotowanie, przegląd i uzgodnienie planu.
- [Załącznik B, B.11](../../../iso-29110-5-1/chapters/annex-b-additional-testing-tasks.md): informacyjny opis planu testów. Nie utożsamiać go z całym planem V&V.
- [Załącznik E](../../../iso-29110-5-1/chapters/annex-e-deployment-packages.md): informacyjne podejście pakietowe, zawierające szablony, przykłady i checklisty. Sam załącznik nie dostarcza wypełnionego planu.

Ścieżki do normy zakładają repozytoria sąsiadujące na dysku. Przy dystrybucji szablonu trzeba zapewnić legalnie dostępne źródło albo bibliografię zastępującą lokalne linki.

## 2. Zestaw planów i moment ich przygotowania

| Plan | Kiedy | Co rozstrzyga | Przykład |
|---|---|---|---|
| Projektu | Na początku; aktualizacja przy zmianie celu, zakresu, zasobów lub zobowiązań | Co dostarczamy, za ile, kiedy, kto odpowiada, jak odbieramy | [project-plan.md](project-plan.md) |
| Przyrostu | Przed najbliższym przyrostem; szczegóły dalekich przyrostów później | Najbliższy wynik, kolejność prac, RED/GREEN, dowody i granice | [increment-plan.md](increment-plan.md) |
| Weryfikacji i walidacji | Lekka strategia od początku; szczegóły przed realizacją objętego zakresu | Co sprawdzamy, na jakim poziomie, względem czego i kto ocenia | [verification-validation-plan.md](verification-validation-plan.md) |
| Wydania | Przed dostarczeniem odbiorcy | Skład wydania, warunki dopuszczenia, dostawa i odbiór | [delivery-migration-operations.md](delivery-migration-operations.md) |
| Migracji | Przed zmianą formatu istniejących danych | Próba, kopia, kontrola kompletności, przełączenie i wycofanie | Ten sam plik, osobny plan migracji |
| Utrzymania i odtworzenia | Przed użyciem na wartościowych danych | Odpowiedzialność, obsługa awarii, odtworzenie i granice wsparcia | Ten sam plik, osobny plan utrzymania |
| Pilota praktyki | Przed eksperymentalnym włączeniem kontroli | Hipoteza, koszt, próba, kryteria oceny i decyzja po pilocie | [practice-pilot-plan.md](practice-pilot-plan.md) |

Osobny plik jest potrzebny, gdy plan ma własny cykl zmian, odbiorcę lub zbyt duży zakres. Początkowo kilka planów może być sekcjami jednego dokumentu. Liczba plików nie mierzy dojrzałości.

## 3. Wspólny projekt demonstracyjny

Wszystkie przykłady dotyczą fikcyjnego narzędzia **Release Ledger**: lokalnego CLI, które sprawdza powiązania wymagań i planu, wiąże dowody z wersją wejść oraz przygotowuje manifest wydania. To inny projekt niż archiwizator sesji i obecne narzędzia szablonu.

Daty, osoby, koszty, progi i nazwy poleceń są założeniami demonstracyjnymi. Nie są odpowiedziami Michała ani ofertą lub zobowiązaniem. Żaden etap nie został wykonany. Identyfikatory `DEMO/...` są lokalne dla przykładów; nie dodajemy ich do `template/process/tools/id.toml`, aktywnego planu ani rejestru decyzji. Nazwy przyszłych plików kodu i poleceń zapisujemy w backtickach, ponieważ nie istnieją w tym repozytorium.

## 4. Mapa treści WP.10 na przykład

| Element | Gdzie w przykładzie projektu |
|---|---|
| Opis produktu, potrzeby klienta, zakres, cele | §1–2 |
| Cykl wytwarzania i produkty dostawy | §3 |
| Zadania, weryfikacja, walidacja i przeglądy | §5 oraz plan V&V |
| Czas trwania, daty i zależności | §5; kalendarz w §4 |
| Zasoby, szkolenie, skład zespołu | §4 |
| Nakład i koszt | §5–6 |
| Ryzyka | §7 |
| Repozytorium, dostęp, wersje, baseline, kopie, odtwarzanie, archiwizacja | §8 |
| Instrukcje dostarczenia, skład i wersje, kolejność, media, odzyskiwanie | §9 oraz plan wydania |
| Zatwierdzenie przez klienta i kierownika projektu | §10; jawnie niewykonane |

To mapa treści, nie automatyczny werdykt zgodności. Termin i nakład muszą być uzasadnione pomiarem lub estymacją z jawną niepewnością.

## 5. Checklista przeglądu planu

- Czy każde zobowiązanie ma produkt, zadanie, odpowiedzialność i kryterium odbioru?
- Czy zadania obejmują przegląd, integrację, poprawki, dostawę i odbiór?
- Czy pracochłonność jest odróżniona od czasu kalendarzowego i oczekiwania?
- Czy dostępność i zależności pozwalają zmieścić zadania w harmonogramie?
- Czy budżet obejmuje role poza programistą, narzędzia i rezerwę?
- Czy ryzyka mają sygnał uruchamiający działanie i właściciela?
- Czy wymagania i kryteria sprawdzenia są jednoznaczne, a otwarte sprawy jawne?
- Czy wiadomo, kto zatwierdza plan i kto może zmienić jego zobowiązania?
- Czy plan wskazuje wersje wejść, dowody oraz sposób dostarczenia i odtworzenia?
- Czy wynik modelu wykonalności ma zapisane założenia, zakres i status rozstrzygnięcia?

Plan to przewidywania i zobowiązania. Rejestr postępu to fakty wykonania. Raport testu to dowód na konkretnych wejściach. Zmiana planu nie może nadpisywać historycznego wyniku ani ukrywać odchylenia.

## 6. Jak wdrożyć przykłady do rzeczywistego projektu

Najpierw uzgodnić cel, zobowiązania i stosowalność sekcji. Potem zastąpić dane demonstracyjne rzeczywistymi, określić brakujące informacje i uzgodnić baseline. Nie kopiować fikcyjnych podpisów — w przykładach ich nie ma. Nie tworzyć nowego parsera tylko dla tych tabel. Ewentualne rozszerzenie obecnego schematu planu jest osobnym przyrostem z migracją i testami.

Opis formalizacji i przejścia do kodu: [primer modeli formalnych](../FORMAL-MODELS-REQUIREMENTS-AND-PROCESS.md). Dosłowny zapis odpowiedzi, która rozpoczęła ten temat: [zapis rozmowy](../FORMAL-FEASIBILITY-CONVERSATION.md).
