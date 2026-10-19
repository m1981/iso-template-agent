# Macierz śladu

Plik generowany przez tools/trace.py według tools/id.toml; nie edytuj ręcznie (P-04).

Elementy: SC 1 · IO 2 · D 1 · Q 0 · DP 1 · G 4 · UC 1 · RSK 1 · REQ 3 · E 5 · AT 1 · OBJ 1 · MS 1 · TSK 1 · PRK 1 · COR 1 · VER 2 · VAL 1 · ACC 1

Błędy: 0 · ostrzeżenia: 2

## W górę: element → rodzice

| Element | Typ | Rodzice |
| --- | --- | --- |
| DP-01 | DP | D-01 |
| G-AKT-01 | G | — |
| G-ELM-01 | G | D-01 |
| G-ELM-02 | G | — |
| G-AKT-02 | G | — |
| UC-01 | UC | SC-01, IO-01 |
| RSK-01 | RSK | UC-01 |
| CAP-01 | REQ | UC-01 |
| CAP-02 | REQ | RSK-01 |
| OUT-01 | REQ | IO-02, DP-01 |
| E-01 | E | UC-01 |
| E-02 | E | UC-01 |
| E-03 | E | UC-01 |
| E-04 | E | UC-01 |
| E-05 | E | UC-01 |
| AT-01 | AT | CAP-01 |
| MS-01 | MS | OBJ-01 |
| TSK-01 | TSK | MS-01 |
| PRK-01 | PRK | MS-01 |
| COR-01 | COR | VER-02 |
| VER-01 | VER | UC-01 |
| VER-02 | VER | CAP-02 |
| VAL-01 | VAL | SC-01 |
| ACC-01 | ACC | MS-01 |

## W dół: element → dzieci

| Element | Typ | Dzieci |
| --- | --- | --- |
| SC-01 | SC | UC-01, VAL-01 |
| IO-01 | IO | UC-01 |
| IO-02 | IO | OUT-01 |
| D-01 | D | DP-01, G-ELM-01 |
| DP-01 | DP | OUT-01 |
| UC-01 | UC | RSK-01, CAP-01, E-01, E-02, E-03, E-04, E-05, VER-01 |
| RSK-01 | RSK | CAP-02 |
| CAP-01 | REQ | AT-01 |
| CAP-02 | REQ | VER-02 |
| OUT-01 | REQ | — |
| OBJ-01 | OBJ | MS-01 |
| MS-01 | MS | TSK-01, PRK-01, ACC-01 |
| VER-01 | VER | — |
| VER-02 | VER | COR-01 |
| VAL-01 | VAL | — |
| ACC-01 | ACC | — |

## Plan → produkty (produces:, wyjątek od P-03)

| Zadanie | Produkuje | Elementy |
| --- | --- | --- |
| TSK-01 | UC, CAP-01 | UC-01, CAP-01 |

## Charakterystyki jakości (REQ, WP.13)

Wymagania niefunkcjonalne według charakterystyk; 0 to pytanie, czy czegoś nie pominięto.

| Charakterystyka | Liczba | Wymagania |
| --- | --- | --- |
| functional | 0 | — |
| performance | 0 | — |
| compatibility | 0 | — |
| usability | 0 | — |
| reliability | 0 | — |
| security | 0 | — |
| maintainability | 0 | — |
| portability | 0 | — |
| constraint | 0 | — |
| legal | 0 | — |

## Produkty pracy ISO/IEC 29110-5-1-2

| Produkt | Typ | Elementy |
| --- | --- | --- |
| WP.02 | SC Scenka użytkownika | 1 |
| WP.02 | IO Pozycja zakresu In/Out | 2 |
| WP.03, WP.07 | D Decyzja | 1 |
| WP.13 | G Pojęcie słownika | 4 |
| WP.13 | UC Przypadek użycia | 1 |
| WP.13 | REQ Wymaganie EARS | 3 |
| WP.16 | E Ekran | 5 |
| WP.19 | AT Test akceptacyjny | 1 |
| WP.10 | OBJ Cel projektu | 1 |
| WP.10 | MS Kamień milowy | 1 |
| WP.10 | TSK Zadanie | 1 |
| WP.10 | PRK Ryzyko projektu | 1 |
| WP.04 | COR Korekta | 1 |
| WP.23 | VER Weryfikacja | 2 |
| WP.22 | VAL Walidacja | 1 |
| WP.01 | ACC Akceptacja | 1 |
| WP.05 | AGENTS.md | — |
| WP.09 | progress.md | — |
| WP.11 | repozytorium git | — |
| WP.12 | drugi remote (kopia zapasowa) | — |
| WP.21 | trace.md | — |

## Błędy i ostrzeżenia

- W1 CAP-02: brak dzieci typu AT (Test akceptacyjny)
- W1 OUT-01: brak dzieci typu AT (Test akceptacyjny)
