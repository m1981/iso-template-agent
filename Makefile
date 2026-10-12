# Te same komendy dla człowieka i agenta (AGENTS.md, sekcja Polecenia).
.PHONY: sprawdz slad nawigacja hooki baseline test

sprawdz: slad ## wszystkie kontrole (to samo co pre-commit, bez sprawdzania aktualności)
	@if [ -d nawigacja ]; then cd nawigacja && python3 -B sprawdz.py ekrany.mmd; fi

slad: ## odśwież slad.md i pokaż błędy śladu
	python3 -B narzedzia/slad.py

nawigacja: ## odśwież mapę nawigacji (gdy moduł jest wdrożony)
	cd nawigacja && python3 -B zbuduj.py

test: ## test narzędzi śladu i hooków (po zmianie narzedzia/ lub id.toml)
	python3 -B narzedzia/test_narzedzi.py

hooki: ## włącz hooki w nowym klonie
	git config core.hooksPath .githooks

baseline: ## oznacz zamknięty etap: make baseline N=01-nazwa
	@test -n "$(N)" || (echo "Podaj N, np. make baseline N=01-zakres" && exit 1)
	git tag -a baseline-$(N) -m "Baseline $(N)"
