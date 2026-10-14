# Te same komendy dla człowieka i agenta (AGENTS.md, sekcja Polecenia).
.PHONY: check trace progress navigation hooks baseline test

check: trace progress ## wszystkie kontrole (to samo co pre-commit, bez sprawdzania aktualności)
	@if [ -d navigation ]; then cd navigation && python3 -B check.py screens.mmd; fi

trace: ## odśwież trace.md i pokaż błędy śladu
	python3 -B tools/trace.py

progress: ## odśwież progress.md (rekord postępu z plan.md, rekordów i tagów)
	python3 -B tools/progress.py

navigation: ## odśwież mapę nawigacji (gdy moduł jest wdrożony)
	cd navigation && python3 -B build.py

test: ## test narzędzi śladu i hooków (po zmianie tools/ lub id.toml)
	python3 -B tools/test_tools.py

hooks: ## włącz hooki w nowym klonie; push wysyła też tagi baseline (D-13)
	git config core.hooksPath .githooks
	git config push.followTags true

baseline: ## oznacz zamknięty etap: make baseline N=01-nazwa
	@test -n "$(N)" || (echo "Podaj N, np. make baseline N=01-zakres" && exit 1)
	git tag -a baseline-$(N) -m "Baseline $(N)"
	python3 -B tools/progress.py
	@echo "Dołącz progress.md do następnego commita (P-09)."
