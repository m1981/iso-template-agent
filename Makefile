# Te same komendy dla człowieka i agenta (AGENTS.md, sekcja Polecenia).
.PHONY: check trace progress iso-map navigation hooks baseline test test-distribution new-project restore-check process-update

check: trace progress iso-map ## wszystkie kontrole (to samo co pre-commit, bez sprawdzania aktualności)
	@if [ -d navigation ]; then cd navigation && python3 -B check.py screens.mmd; fi

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
