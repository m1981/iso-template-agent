# Testy akceptacyjne

Scenariusze Gherkin, po jednym lub kilku na wymaganie. Test wskazuje weryfikowane wymaganie komentarzem `# verifies:` (P-03) i ma stan `# status:`; reports/trace.md pokazuje pokrycie, a wymaganie bez testu daje ostrzeżenie W1. Gdy testów przybędzie, można podnieść poziom w process/tools/id.toml (`coverage = "AT:error"` dla typu REQ).

Pliki: `spec/tests/<obszar>.feature`. Format:

```
Feature: Przechwytywanie

  @AT-nn
  # verifies: OBS-nn
  # status: initiated
  Scenario: Zapis przechwyconego elementu
    Given …
    When …
    Then …
```

Testy są pisane na etapie specyfikacji jako kryteria akceptacji; ich uruchamianie przychodzi z kodem.

Test automatyczny wskazuje swój przypadek komentarzem `# runner: plik::przypadek` (kilka po przecinku); skrypt testów wypisuje wiersz `CASE przypadek: pass|fail`. `make test-report` uruchamia wskazane skrypty i zapisuje raport testów (WP.20): test przechodzi tylko wtedy, gdy przeszły wszystkie jego przypadki. Test bez `runner:` jest ręczny i ocenia go przegląd.
