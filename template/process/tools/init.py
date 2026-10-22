"""Start projektu z pakietu procesu (szablon D-58; zastępuje dawny skrypt new-project, szablon D-22).

Po `copier copy` projekt ma tylko process/ i plik copiera. init.py zakłada dokumenty projektu ze wzorców
z process/templates/ (szablon D-47): pliki wpięcia procesu w katalogu głównym (AGENTS.md, CLAUDE.md, README.md,
Makefile, .gitignore), project/ (umowa, plan, rejestr z D-01, ustawienia, wyjątki kontroli), spec/ i
records/, a potem generuje raporty w reports/. Z --module wdraża moduł (navigation, risks).

Nigdy nie nadpisuje istniejącego pliku (pomija go i mówi o tym). Odmawia, gdy:
  - projekt już założono (jest project/decisions.md), chyba że wdrażasz moduł,
  - katalog nie jest repozytorium gita,
  - śledzone pliki mają niezacommitowane zmiany (każdy krok da się cofnąć gitem; nieśledzone pliki,
    np. process/ zaraz po copier copy, są dozwolone).

Użycie: python3 process/tools/init.py [--module navigation|risks]
"""
import datetime
import os
import re
import shutil
import subprocess
import sys

TOOLS_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, TOOLS_DIR)
import model as M  # noqa: E402

TEMPLATES = os.path.join(M.PROCESS_DIR, "templates")
ANSWERS = ".copier-answers.process.yml"
BASE = {  # wzorzec (względem process/templates/) → plik projektu
    "root/AGENTS.md": "AGENTS.md", "root/CLAUDE.md": "CLAUDE.md", "root/README.md": "README.md",
    "root/Makefile": "Makefile", "root/.gitignore": ".gitignore",
    "project/agreement.md": "project/agreement.md", "project/plan.md": "project/plan.md",
    "project/decisions.md": "project/decisions.md", "project/settings.toml": "project/settings.toml",
    "project/check_refs.allow": "project/check_refs.allow", "project/check_leak.allow": "project/check_leak.allow",
    "spec/glossary.md": "spec/glossary.md", "spec/principles.md": "spec/principles.md",
    "spec/scenarios.md": "spec/scenarios.md", "spec/scope.md": "spec/scope.md",
    "spec/use-cases.md": "spec/use-cases.md", "spec/requirements.md": "spec/requirements.md",
    "spec/tests/README.md": "spec/tests/README.md",
    "records/corrections.md": "records/corrections.md", "records/verification.md": "records/verification.md",
    "records/validation.md": "records/validation.md", "records/acceptance.md": "records/acceptance.md",
}
MODULES = {
    "navigation": {"spec/navigation/screens.mmd": "spec/navigation/screens.mmd",
                   "spec/navigation/navigation-map.html": "spec/navigation/navigation-map.html"},
    "risks": {"spec/risks.md": "spec/risks.md"},
}


def template_version(root):
    """Wersja szablonu z pliku copiera (_commit), jeśli jest."""
    path = os.path.join(root, ANSWERS)
    if os.path.exists(path):
        for line in open(path, encoding="utf-8"):
            m = re.match(r"^_commit:\s*['\"]?([^'\"\s]+)", line)
            if m:
                return m.group(1)
    return ""


def register_text(version="", date=None):
    """Rejestr nowego projektu ze wzorca: D-01 „Start projektu z szablonu”."""
    text = open(os.path.join(TEMPLATES, "project", "decisions.md"), encoding="utf-8").read()
    return (text.replace("{version}", f", wersja {version}" if version else "")
                .replace("{date}", date or datetime.date.today().isoformat()))


def git(root, *args):
    return subprocess.run(["git", *args], cwd=root, capture_output=True, text=True)


def copy_all(root, mapping, version):
    created, skipped = [], []
    for src, dst in mapping.items():
        target = os.path.join(root, dst)
        if os.path.exists(target):
            skipped.append(dst)
            continue
        os.makedirs(os.path.dirname(target) or ".", exist_ok=True)
        if src == "project/decisions.md":
            with open(target, "w", encoding="utf-8") as f:
                f.write(register_text(version))
        else:
            shutil.copy(os.path.join(TEMPLATES, src), target)
        created.append(dst)
    return created, skipped


def main(argv):
    root = M.ROOT
    module = None
    if "--module" in argv:
        i = argv.index("--module")
        module = argv[i + 1] if i + 1 < len(argv) else ""
        if module not in MODULES:
            print(f"init: nieznany moduł „{module}”; dostępne: {', '.join(MODULES)}")
            return 2
    inside = git(root, "rev-parse", "--show-toplevel")
    if inside.returncode != 0 or os.path.realpath(inside.stdout.strip()) != os.path.realpath(root):
        print("init: katalog projektu nie jest repozytorium gita; najpierw git init (README.md, Start).")
        return 1
    if git(root, "rev-parse", "--verify", "-q", "HEAD").returncode == 0 and \
            git(root, "diff", "--quiet", "HEAD", "--").returncode != 0:
        print("init: śledzone pliki mają niezacommitowane zmiany; zacommituj je albo odłóż i uruchom ponownie.")
        return 1
    if module is None and os.path.exists(os.path.join(root, "project", "decisions.md")):
        print("init: projekt już założono (jest project/decisions.md); nic nie zmieniam. Moduł: --module navigation|risks.")
        return 1
    mapping = MODULES[module] if module else BASE
    created, skipped = copy_all(root, mapping, template_version(root))
    for x in created:
        print(f"założono {x}")
    for x in skipped:
        print(f"pominięto {x}: plik już istnieje, nie nadpisuję")
    for script in ("trace.py", "progress.py", "iso_map.py"):
        subprocess.run([sys.executable, "-B", os.path.join(TOOLS_DIR, script)], cwd=root,
                       env=dict(os.environ, PROCESS_ROOT=root))
    if module == "navigation":
        subprocess.run([sys.executable, "-B", os.path.join(M.PROCESS_DIR, "modules", "navigation", "build.py")],
                       cwd=root)
    print()
    if module:
        print(f"Moduł {module} wdrożony. Dalej: make check, potem commit z ID decyzji o wdrożeniu modułu.")
    else:
        print("Dalej (process/AGENTS.md, „Start projektu”): make hooks; uzupełnij project/agreement.md i project/settings.toml")
        print('(system), potem git add -A && git commit -m "Start projektu (D-01)".')
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
