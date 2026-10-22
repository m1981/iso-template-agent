"""Widok warstwy procesu do czasu przeniesienia (D-54, D-59, D-60, D-63). Narzędzie przejściowe.

Pliki warstwy procesu leżą już w docelowych miejscach (spec/requirements.md, spec/glossary.md,
spec/tests/*.feature, project/plan.md), a narzędzia czytają jeszcze płaski układ szablonu. Skrypt
składa w katalogu tymczasowym płaski widok: narzędzia, listy kontrolne, rejestr i rekordy z katalogu
głównego oraz pliki warstwy procesu w miejscach, których oczekuje model; podmiot wymagań to
„Process kit”. Uruchamia na nim trace.py i progress.py, a z --tests także raport testów (testy
idą w tym repozytorium, nie w widoku). Wyniki zapisuje w reports/.

Po przeniesieniu narzędzia czytają te pliki wprost (`--root .`), a ten skrypt idzie do archiwum.

Użycie: python3 tools/process_kit_view.py [--tests]   (albo: make process-kit [TESTS=1])
Kod wyjścia: 0 ślad bez błędów (i testy przeszły), 1 nie.
"""
import os
import shutil
import subprocess
import sys
import tempfile

TOOLS_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(TOOLS_DIR)
SYSTEM = "Process kit"
FROM_ROOT = ["checklist.md", "decisions.md", "verification.md", "corrections.md", "validation.md", "acceptance.md"]
MAPPED = {"spec/requirements.md": "requirements.md", "spec/glossary.md": "glossary.md", "project/plan.md": "plan.md"}


def build(view):
    shutil.copytree(os.path.join(ROOT, "tools"), os.path.join(view, "tools"), ignore=shutil.ignore_patterns("__pycache__"))
    for name in FROM_ROOT:
        shutil.copy(os.path.join(ROOT, name), view)
    for src, dst in MAPPED.items():
        shutil.copy(os.path.join(ROOT, src), os.path.join(view, dst))
    os.makedirs(os.path.join(view, "tests"))
    for name in sorted(os.listdir(os.path.join(ROOT, "spec", "tests"))):
        if name.endswith(".feature"):
            shutil.copy(os.path.join(ROOT, "spec", "tests", name), os.path.join(view, "tests"))
    cfg = os.path.join(view, "tools", "id.toml")
    text = open(cfg, encoding="utf-8").read()
    marker = 'system = "System"'
    if marker not in text:
        raise SystemExit("process_kit_view: w tools/id.toml nie ma wiersza " + marker)
    open(cfg, "w", encoding="utf-8").write(text.replace(marker, f'system = "{SYSTEM}"', 1))


def run(view, *args):
    return subprocess.run([sys.executable, "-B", *args], cwd=view, capture_output=True, text=True)


def main(argv):
    reports = os.path.join(ROOT, "reports")
    os.makedirs(reports, exist_ok=True)
    rc = 0
    with tempfile.TemporaryDirectory() as view:
        build(view)
        r = run(view, "tools/trace.py", os.path.join(reports, "trace.md"))
        print(r.stdout.strip())
        rc |= r.returncode
        r = run(view, "tools/progress.py", os.path.join(reports, "progress.md"))
        print(r.stdout.strip())
        rc |= r.returncode
        if "--tests" in argv:
            r = run(view, "tools/test_report.py", os.path.join(reports, "test-report.md"), "--scripts-root", ROOT)
            print(r.stdout.strip())
            rc |= r.returncode
    print("process_kit_view: " + ("OK" if rc == 0 else "są błędy") + f"; wyniki w {os.path.relpath(reports, ROOT)}/")
    return 1 if rc else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
