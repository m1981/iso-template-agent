# Cele procesu (process/process.mk), wpinane z Makefile projektu: include process/process.mk.
# Plik należy do pakietu procesu i aktualizuje go copier (szablon D-47); cele projektu dopisuj w Makefile.
# PROC: katalog pakietu względem katalogu głównego (w projekcie process, w repozytorium szablonu template/process).
PROC ?= process
export PROCESS_ROOT := $(CURDIR)
PY := python3 -B
T := $(PROC)/tools
# słownik projektu dla kontroli przecieku dziedziny (szablon D-62); pusty, gdy go nie ma
LEAK_GLOSSARY ?= $(if $(wildcard spec/glossary.md),--glossary spec/glossary.md)

.PHONY: check trace progress iso-map navigation hooks baseline test test-report restore-check process-update

check: trace progress iso-map ## wszystkie kontrole (jak pre-commit, bez sprawdzania aktualności) i odwołania oraz przeciek dziedziny
	@if [ -d spec/navigation ]; then $(PY) $(PROC)/modules/navigation/check.py spec/navigation/screens.mmd; fi
	$(PY) $(T)/check_refs.py
	$(PY) $(T)/check_leak.py $(LEAK_GLOSSARY)

trace: ## odśwież reports/trace.md i pokaż błędy śladu
	$(PY) $(T)/trace.py

progress: ## odśwież reports/progress.md (rekord postępu z planu, rekordów i tagów)
	$(PY) $(T)/progress.py

iso-map: ## odśwież reports/iso-map.html (strona zgodności z ISO/IEC 29110)
	$(PY) $(T)/iso_map.py

navigation: ## odśwież spec/navigation/navigation-map.html (gdy moduł jest wdrożony)
	$(PY) $(PROC)/modules/navigation/build.py

test: ## test narzędzi procesu (po aktualizacji pakietu)
	$(PY) $(T)/test_tools.py

test-report: ## raport testów (WP.20): testy AT z runner: i ich wyniki do reports/test-report.md (szablon D-60)
	$(PY) $(T)/test_report.py

restore-check: ## sprawdź odtworzenie z kopii (klon origin: HEAD, tagi, ślad); RECORD=1 dopisuje rekord VER (szablon D-35)
	$(PY) $(T)/restore_check.py $(if $(RECORD),--record)

process-update: ## aktualizacja pakietu procesu do wersji V=vX.Y.Z z kontrolą wyniku (szablon D-52)
	$(PY) $(T)/process_update.py $(V)

hooks: ## włącz hooki z $(PROC)/hooks; push wysyła też tagi baseline; nie nadpisuje innego menedżera hooków
	@cur=$$(git config --get core.hooksPath); if [ -n "$$cur" ] && [ "$$cur" != "$(PROC)/hooks" ] && [ "$$cur" != .githooks ]; then \
	  echo "make hooks: core.hooksPath wskazuje już $$cur (inny menedżer hooków). Nie nadpisuję: wepnij kontrole z $(PROC)/hooks/ do niego albo zmień ustawienie ręcznie."; exit 1; fi
	git config core.hooksPath $(PROC)/hooks
	git config push.followTags true

baseline: ## oznacz zamknięty etap: make baseline N=01-nazwa
	@test -n "$(N)" || (echo "Podaj N, np. make baseline N=01-zakres" && exit 1)
	git tag -a baseline-$(N) -m "Baseline $(N)"
	$(PY) $(T)/progress.py
	@echo "Dołącz reports/progress.md do następnego commita (P-09)."
