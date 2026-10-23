# Przykładowy plan pilota — modele relacji i procesu

Status: **propozycja demonstracyjna, niewykonana**. Pilot jest osobny od budżetu i harmonogramu budowy [Release Ledger](project-plan.md). Nie aktywuje Alloy, TLA+ ani nowych bramek w boilerplate.

## Cel i hipotezy

H1: model relacji pomaga ujawnić brak zadania lub testu w zakresie wydania przed implementacją. H2: model procesu pomaga ujawnić użycie nieaktualnej zgody lub dowodu po zmianie wejść. Interesuje nas dodatkowa wartość wobec istniejących testów, a nie sama liczba znalezionych kontrprzykładów.

## Próba i harmonogram

Pilot po I2, w osobnym uzgodnionym oknie. Limit: DEV 8 h × 150 PLN + REV 2 h × 180 PLN = 1560 PLN; OWN 1 h × 200 PLN na ocenę; razem 1760 PLN. Dostępność i daty wymagają uzgodnienia przed wykonaniem, nie są ukrytym obciążeniem T/2–T/6.

| Czynność | DEV | Wynik |
|---|---:|---|
| Wybrać wymagania, granice i znane naruszenia | 1 h | Lista własności i scenariuszy z ręcznym oczekiwaniem |
| Model relacji Alloy | 2 h | Poprawna instancja, kontrprzykład, jawny zakres analizy |
| Model procesu TLA+ | 3 h | Przebiegi zmiany, weryfikacji, zgody i wydania |
| Powiązać z kodem i zmierzyć koszt | 2 h | Testy regresyjne, raport i luki odwzorowania |

REV 2 h: ocena modelu i granic wnioskowania. OWN 1 h: ocena wartości i decyzja o dalszym stosowaniu.

## Przypadki kontrolne

1. Wymaganie ma zadanie, ale test znajduje się poza zakresem wydania.
2. Pusty zakres przypadkowo spełnia wszystkie kwantyfikowane reguły.
3. Weryfikacja rewizji 1, zmiana do rewizji 2, próba wydania na starym pass.
4. Zmiana wejścia między sprawdzeniem a publikacją.
5. Poprawny przebieg kończy się wydaniem; reguły nie blokują wszystkiego.

Przypadki celowo wadliwe raportujemy jako mutacje kontrolne, oddzielnie od rzeczywistych defektów znalezionych w produkcie.

## Kryteria i pomiar

Kryteria techniczne: znane naruszenia wykrywane w zadanym modelu; poprawny przebieg istnieje; błąd parsera, timeout i niepełna analiza nie są sukcesem; co najmniej jeden kontrprzykład ma odpowiadający test kodu. Brak defektu naturalnego nie oznacza nieskuteczności praktyki.

Pomiar: aktywny czas autora i recenzenta, czas narzędzia, czas tłumaczenia kontrprzykładu, potwierdzone nowe defekty, odrzucone zgłoszenia, liczba rozbieżności model–kod, koszt zmiany jednego wymagania. Przed pilotem zapisać koszt istniejącej kontroli tych samych przypadków.

Po limicie przedstawić wyniki, brakujące zakresy i wariant: utrzymać mały model, uprościć, rozszerzyć próbę lub odłożyć. Nie instalować automatycznie nowej obowiązkowej bramki. Zero kontrprzykładów w ograniczonym modelu nie jest dowodem poprawności implementacji.

## Rejestr pilota

| Etap | Stan | Dowód |
|---|---|---|
| Plan | Przykład zapisany | Ten dokument |
| Narzędzia i modele | Niewdrożone | Instruktaż w [primerze](../FORMAL-MODELS-REQUIREMENTS-AND-PROCESS.md) |
| Uruchomienia | Niewykonane | Brak raportów solvera |
| Ocena wartości | Niewykonana | Wymaga rzeczywistych pomiarów |
