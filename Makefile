# Warstwa procesu (iso-template-agent): ten sam proces co w projektach, z narzędziami z template/process (D-48).
# Cele procesu: template/process/process.mk; tu cele własne warstwy procesu.
PROC := template/process
# słownik warstwy procesu (spec/glossary.md) to pojęcia procesu, nie dziedzina klienta: bez kontroli pojęć (D-62)
LEAK_GLOSSARY :=
include template/process/process.mk

# złoty wzorzec zapisano przed przeniesieniem (D-61): porównanie pomija katalogi nowego układu
GOLDEN_STRIP := --strip spec/ --strip project/ --strip records/ --strip reports/ --strip process/

.PHONY: test-distribution golden test-move test-all

test-distribution: ## granica dystrybucji copierem: mały szablon i prawdziwy template/ (wymaga copiera w przypiętej wersji)
	$(PY) tests/test_distribution.py

golden: ## wyjścia narzędzi wobec złotego wzorca w reference/golden/ (D-61); SNAPSHOT=1 zapisuje nowy wzorzec
	$(PY) tests/golden_master.py $(if $(SNAPSHOT),snapshot reference/golden,compare reference/golden $(GOLDEN_STRIP))

test-move: ## kryteria odbioru przeniesienia na trzy warstwy (TSK-05, D-71)
	$(PY) tests/test_move.py

test-all: check test test-distribution golden test-move ## wszystko, co sprawdza warstwę procesu
