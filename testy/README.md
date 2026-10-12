# Testy akceptacyjne

Scenariusze Gherkin, po jednym lub kilku na wymaganie. Test wskazuje weryfikowane wymaganie komentarzem `# weryfikuje:` (P-03); slad.md pokazuje pokrycie, a wymaganie bez testu daje ostrzeżenie O1. Gdy testów przybędzie, można podnieść poziom w narzedzia/id.toml (`pokrycie = "AT:blad"` dla typu WYM).

Pliki: `testy/<obszar>.feature`. Format:

```
Feature: Przechwytywanie

  @AT-nn
  # weryfikuje: OBS-nn
  Scenario: Zapis przechwyconego elementu
    Given …
    When …
    Then …
```

Testy są pisane na etapie specyfikacji jako kryteria akceptacji; ich uruchamianie przychodzi z kodem.
