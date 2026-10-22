# Raport testów

Plik generowany przez tools/test_report.py (ISO/IEC 29110 WP.20, D-60); nie edytuj ręcznie.

Data: 2026-10-22 · commit: 1cef40c (z niezacommitowanymi zmianami) · Python 3.13.16

Testy automatyczne: 51 · przeszły: 51 · nie przeszły: 0 · ręczne: 2

| Test | Weryfikuje | Wynik | Przypadki albo problem |
| --- | --- | --- | --- |
| AT-01 | TRC-02 | pass | tools/test_tools.py::breakage-01, tools/test_tools.py::breakage-02, tools/test_tools.py::breakage-10, tools/test_tools.py::breakage-21 |
| AT-02 | TRC-03 | pass | tools/test_tools.py::breakage-03, tools/test_tools.py::id-in-text |
| AT-03 | TRC-04 | pass | tools/test_tools.py::breakage-04 |
| AT-04 | TRC-05 | pass | tools/test_tools.py::breakage-05, tools/test_tools.py::breakage-12, tools/test_tools.py::breakage-13, tools/test_tools.py::breakage-20 |
| AT-05 | TRC-06 | pass | tools/test_tools.py::breakage-06 |
| AT-06 | TRC-07 | pass | tools/test_tools.py::breakage-07 |
| AT-07 | TRC-08 | pass | tools/test_tools.py::breakage-08, tools/test_tools.py::breakage-14, tools/test_tools.py::breakage-15, tools/test_tools.py::breakage-16 |
| AT-08 | TRC-09 | pass | tools/test_tools.py::breakage-09 |
| AT-09 | TRC-10 | pass | tools/test_tools.py::chain, tools/test_tools.py::chain-no-warnings |
| AT-10 | TRC-11 | pass | tools/test_tools.py::warning-04, tools/test_tools.py::warning-05, tools/test_tools.py::extension-point |
| AT-11 | TRC-12 | pass | tools/test_tools.py::warning-01, tools/test_tools.py::warning-02, tools/test_tools.py::w3-with-record |
| AT-12 | TRC-13 | pass | tools/test_tools.py::w5 |
| AT-13 | TRC-14 | pass | tools/test_tools.py::toml-fallback |
| AT-14 | TRC-15 | pass | tools/test_tools.py::id-in-text |
| AT-15 | TRC-16 | pass | tools/test_tools.py::heading-colon |
| AT-16 | TRC-17 | pass | tools/test_tools.py::feature-untagged |
| AT-17 | TRC-19 | pass | tools/test_tools.py::nav-orphan |
| AT-18 | HKS-01 | pass | tools/test_tools.py::precommit-trace |
| AT-19 | HKS-02 | pass | tools/test_tools.py::commit-msg |
| AT-20 | HKS-03 | pass | tools/test_tools.py::precommit-progress, tools/test_tools.py::precommit-iso-map |
| AT-21 | HKS-04 | pass | tools/test_distribution.py::hooks |
| AT-22 | SEP-01 | pass | tools/test_tools.py::e9-1, tools/test_tools.py::e9-2, tools/test_tools.py::e9-3, tools/test_tools.py::e9-4, tools/test_tools.py::e9-5, tools/test_tools.py::e9-6, tools/test_tools.py::e9-7 |
| AT-23 | SEP-02 | pass | tools/test_tools.py::e9-import |
| AT-24 | PLN-01 | pass | tools/test_tools.py::progress |
| AT-25 | PLN-02 | pass | tools/test_tools.py::precommit-progress |
| AT-26 | PLN-03 | pass | tools/test_tools.py::breakage-11 |
| AT-27 | REC-01 | pass | tools/test_tools.py::breakage-17, tools/test_tools.py::breakage-19 |
| AT-28 | REC-02 | pass | tools/test_tools.py::breakage-18 |
| AT-29 | REP-01 | pass | tools/test_tools.py::restore-check |
| AT-30 | REP-02 | pass | tools/test_tools.py::restore-check |
| AT-31 | ISO-01 | pass | tools/test_tools.py::iso-map |
| AT-32 | INI-01 | pass | tools/test_tools.py::new-project |
| AT-33 | INI-02 | pass | tools/test_tools.py::new-project |
| AT-34 | INI-03 | pass | tools/test_tools.py::template-copy, tools/test_tools.py::first-commit |
| AT-35 | DST-01 | pass | tools/test_distribution.py::copy |
| AT-36 | DST-02 | pass | tools/test_distribution.py::tags |
| AT-37 | UPD-01 | pass | tools/test_distribution.py::version, tools/test_distribution.py::dirty |
| AT-38 | UPD-02 | pass | tools/test_distribution.py::conflict, tools/test_distribution.py::markers, tools/test_distribution.py::binary |
| AT-39 | UPD-03 | pass | tools/test_distribution.py::scope |
| AT-40 | UPD-04 | pass | tools/test_distribution.py::update |
| AT-41 | UPD-05 | pass | tools/test_distribution.py::missing |
| AT-42 | UPD-06 | pass | tools/test_distribution.py::validation |
| AT-43 | UPD-07 | pass | tools/test_distribution.py::repeat |
| AT-44 | UPD-08 | pass | tools/test_distribution.py::jump |
| AT-45 | LAY-03 | pass | tools/test_tools.py::refs |
| AT-46 | LEK-01 | pass | tools/test_tools.py::leak-id |
| AT-47 | LEK-02 | pass | tools/test_tools.py::leak-term |
| AT-48 | TST-01 | pass | tools/test_tools.py::breakage-22 |
| AT-49 | TST-02 | pass | tools/test_tools.py::test-report |
| AT-52 | TRC-18 | pass | tools/test_tools.py::quality-section |
| AT-50 | TRC-01 | ręczny | — |
| AT-51 | LNG-01 | ręczny | — |
| AT-53 | HKS-05 | pass | tools/test_tools.py::precommit-index |

## Przebiegi

| Plik | Kod wyjścia | Przypadki pass | Przypadki fail |
| --- | --- | --- | --- |
| tools/test_distribution.py | 0 | 15 | 0 |
| tools/test_tools.py | 0 | 61 | 0 |
