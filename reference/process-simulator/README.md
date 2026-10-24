# Laboratorium procesu — pierwszy przyrost

Działająca lokalna lekcja TextStats: potrzeba → wymagania → plan i projekt → przegląd → przypadki testowe → symulowany RED → poprawka → jednostkowy GREEN → integracja → demonstracja → jawny odbiór w fabule lub korekta instrukcji.

**Status:** I1 zaimplementowany i sprawdzony technicznie. Próba edukacyjna oraz odbiór przez Użytkownika jeszcze niewykonane. Testy TextStats na ekranie są symulowane; rzeczywiste testy aplikacji znajdują się w `tests/` i [dowodach](evidence/README.md).

## Uruchomienie

Z katalogu repozytorium:

```sh
cd reference/process-simulator
python3 -B -m app.server --port 8765
```

Otwórz **http://127.0.0.1:8765**. Zakończenie serwera: Ctrl+C. Gdy port jest zajęty, wybierz inny przez `--port`, np. 8766. Aplikacja wiąże tylko adres loopback; nie jest wdrożeniem sieciowym.

Nie instalujesz pakietów. Runtime: Python i jego biblioteka standardowa oraz przeglądarka z JavaScript/SVG. Sprawdzono Python **3.14.6**, Chrome **156.0.8078.48** na macOS. Składnię dobrano dla Python 3.11+, ale pozostałych wersji i przeglądarek nie testowano.

## Pierwsze ćwiczenie

1. Wybierz „Uzgodnij zakres w fabule”. Otwórz specyfikację w grafie i rozróżnij plik, R1 oraz typ WP.13.
2. Przygotuj plan i projekt, wykonaj przegląd, przygotuj T1–T5. Licznik wykonań nadal wynosi zero. Warunki niedostępnych działań znajdziesz pod „Pozostałe działania i warunki”.
3. Uruchom próbę na szkielecie. W karcie RUN1 zobacz FAIL i powiązanie z CODE1@1. Popraw obliczenie, ponów testy. RUN2 odnosi się do CODE1@2, RUN1 pozostaje niezmieniony.
4. Dołącz adapter, wykonaj integrację i demonstrację. Zdecyduj w fabule o odbiorze albo korekcie objaśnienia; podaj uzasadnienie. Korekta wymaga nowej demonstracji. Zielone testy nie podejmują tej decyzji.
5. Obejrzyj wcześniejszy krok w historii, następnie wróć do bieżącego. Przeszłość jest tylko do odczytu. Wydanie nadal czeka na otwarte Q1.
6. „Zapisz sesję” pokazuje JSON i pozwala pobrać plik. Po restarcie „Wznów sesję” odtwarza zapis. Możesz też wkleić JSON; błędny zapis nie zastąpi sesji.

Jedna instancja serwera ma **jedną sesję w pamięci**, współdzieloną przez karty. Nie ma automatycznego zapisu. Przed zatrzymaniem serwera lub zastąpieniem sesji zachowaj eksport. Limit: 200 kroków, 2000 znaków opisu decyzji/korekty. Import odtwarza legalne polecenia dla konkretnej wersji lekcji; nie przyjmuje gotowych raportów PASS.

## Dokumenty i odpowiedzialność

| Potrzebuję | Wiążący dokument / kod |
| --- | --- |
| Zakres i kryteria I1 | [increment-01.md](increment-01.md), zatwierdzone D-79 |
| Mapa dalszych prac | [plan.md](plan.md) |
| Stos, jego uzasadnienie i granice | [technical-plan.md](technical-plan.md) |
| Stan, historia zmian, decyzje agenta i punkt wznowienia | [progress.md](progress.md) |
| Przejścia i pochodzenie reguł | [scenario.md](scenario.md) |
| Treść kart | [lessons/textstats-i1.json](lessons/textstats-i1.json) |
| Reguły działania | [app/engine.py](app/engine.py) |
| Wyniki rzeczywistych sprawdzeń | [evidence/README.md](evidence/README.md) |

Graf grupuje informacje według przykładowego pliku; karta pokazuje dokładne ID i rewizję. Lista „Opiera się na” prowadzi do podstawy, „Jest podstawą dla” jest wyliczanym śladem odwrotnym. Karty są dydaktycznymi fragmentami produktów pracy, nie pełnymi produktami wymaganymi do zgodności z ISO. Testy symulatora nie potwierdzają poprawności interpretacji całej normy ani skuteczności nauczania.

## Weryfikacja i rozwój

Z folderu `reference/process-simulator`:

```sh
python3 -B -m unittest discover -s tests -v
python3 -B tools/reproduce-tdd.py
node tools/browser-check.mjs
```

Pierwsze polecenie wymaga możliwości otwarcia lokalnych portów HTTP. Drugie odtwarza początkowy RED oraz kontrolowaną mutację na kopiach, bez zmiany źródeł; zapisuje logi w `evidence/`. Trzecie jest pomocniczym testem interfejsu, wymaga Node 22+ i zainstalowanego Chrome. Na innej maszynie ustaw `CHROME_BIN` na plik wykonywalny Chrome, a w razie potrzeby `PYTHON` na interpreter. Tworzy własny serwer i profil tymczasowy, usuwa wyłącznie ten profil po próbie. Node i Chrome nie są zależnościami runtime Pythona ani potrzebnymi instalacjami do zwykłego używania lekcji.

Zmiana wymagania po GREEN, alternatywne gałęzie, model formalny Alloy/TLC, trwała baza i rzeczywiste operacje na projektach pozostają poza I1. Próba Kitchen CAD/CAM nie została tu wybrana ani zrealizowana.

## Próba z operatorem — następny krok

Operator wykonuje lekcję i własnymi słowami odpowiada: co właśnie powstało, co pozostaje planem, co uzasadnia następny krok i dlaczego GREEN nie jest wydaniem. Rejestrujemy czas wznowienia z eksportu, mylone pojęcia i potrzebne podpowiedzi. Zapisujemy rzeczywiste obserwacje i dopiero potem uzgadniamy kryteria użyteczności; nie ma wymyślonych wartości bazowych ani deklaracji odbioru.
