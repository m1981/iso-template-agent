# Te same komendy dla człowieka i agenta (AGENTS.md, sekcja Polecenia).
.PHONY: check trace progress iso-map navigation hooks baseline test test-distribution test-report golden process-kit new-project restore-check process-update

# Pliki procesu dla kontroli przecieku domeny (D-62); po przeniesieniu (D-54) wystarczy process/
PROCESS_FILES = .githooks AGENTS.md kontrakt-decyzji.md checklist.md roles tools modules glossary.md principles.md scenarios.md scope.md use-cases.md requirements.md tests plan.md corrections.md validation.md acceptance.md

check: trace progress iso-map ## wszystkie kontrole (to samo co pre-commit, bez sprawdzania aktualności, plus odwołania i przeciek domeny)
	@if [ -d navigation ]; then cd navigation && python3 -B check.py screens.mmd; fi
	python3 -B tools/check_refs.py
	python3 -B tools/check_leak.py $(PROCESS_FILES)

trace: ## odśwież trace.md i pokaż błędy śladu
	python3 -B tools/trace.py

progress: ## odśwież progress.md (rekord postępu z plan.md, rekordów i tagów)
	python3 -B tools/progress.py

iso-map: ## odśwież iso-map.html (strona zgodności z ISO/IEC 29110 z tools/id.toml)
	python3 -B tools/iso_map.py

navigation: ## odśwież mapę nawigacji (gdy moduł jest wdrożony)
	cd navigation && python3 -B build.py

test: ## test narzędzi śladu i hooków (po zmianie tools/ lub id.toml)
	python3 -B tools/test_tools.py

new-project: ## raz, w kopii szablonu: historia szablonu do archive/template/, pusty rejestr z D-01 (D-22)
	python3 -B tools/new_project.py

test-report: ## raport testów (WP.20): testy AT z runner: i ich wyniki do test-report.md (D-60)
	python3 -B tools/test_report.py

process-kit: ## ślad i postęp warstwy procesu do czasu przeniesienia (widok tymczasowy, D-64); TESTS=1 dodaje raport testów
	python3 -B tools/process_kit_view.py $(if $(TESTS),--tests)

golden: ## porównanie wyjść narzędzi ze złotym wzorcem w reference/golden/ (D-61); SNAPSHOT=1 zapisuje nowy wzorzec
	python3 -B tools/golden_master.py $(if $(SNAPSHOT),snapshot,compare) reference/golden

test-distribution: ## test granicy dystrybucji copierem na małym szablonie (D-50); wymaga copiera w przypiętej wersji
	python3 -B tools/test_distribution.py

process-update: ## w projekcie z copiera: aktualizacja procesu do wersji V=vX.Y.Z z kontrolą wyniku (D-52)
	python3 -B tools/process_update.py $(V)

restore-check: ## sprawdź odtworzenie z kopii (klon origin: HEAD, tagi, ślad); RECORD=1 dopisuje rekord VER (D-35)
	python3 -B tools/restore_check.py $(if $(RECORD),--record)

hooks: ## włącz hooki w nowym klonie; push wysyła też tagi baseline (D-13); nie nadpisuje innego menedżera hooków
	@cur=$$(git config --get core.hooksPath); if [ -n "$$cur" ] && [ "$$cur" != .githooks ]; then \
	  echo "make hooks: core.hooksPath wskazuje już $$cur (inny menedżer hooków). Nie nadpisuję: wepnij kontrole z .githooks/ do niego albo zmień ustawienie ręcznie."; exit 1; fi
	git config core.hooksPath .githooks
	git config push.followTags true

baseline: ## oznacz zamknięty etap: make baseline N=01-nazwa
	@test -n "$(N)" || (echo "Podaj N, np. make baseline N=01-zakres" && exit 1)
	git tag -a baseline-$(N) -m "Baseline $(N)"
	python3 -B tools/progress.py
	@echo "Dołącz progress.md do następnego commita (P-09)."
