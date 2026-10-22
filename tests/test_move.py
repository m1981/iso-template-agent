"""Test przeniesienia na trzy warstwy (TSK-05 w project/plan.md; D-54, D-71, D-72).

Sprawdza kryteria odbioru K-1…K-10 zadania przeniesienia na podstawie gita: stan sprzed przeniesienia
to commit BASE, stan po nim to HEAD (z katalogiem roboczym dla kontroli uruchamianych). K-7 (droga
projektu na prawdziwym szablonie) sprawdza tests/test_distribution.py, a K-11 (Mac, Python 3.10) to
przebieg tego testu na drugim systemie.

Listy MOVES, EDITED i NEW są specyfikacją przeniesienia wyprowadzoną z reference/layout-map.md:
  MOVES   każdy plik z BASE → jego miejsce po przeniesieniu (pierwszy commit: sam git mv, D-72),
  EDITED  pliki po przeniesieniu, których treść wolno zmienić (ścieżki, narzędzia, D-56, D-73),
  NEW     pliki, które przeniesienie dodaje.
Każdy plik spoza EDITED musi mieć treść identyczną z BASE (K-3).

Test napisany przed przeniesieniem (TDD): na układzie BASE musi się wyłożyć.

Użycie: python3 tests/test_move.py   (wypisuje CASE k-n: pass|fail; kod 1 = porażka)
"""
import os
import re
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "ad47c56e2a95d3fced3a6ffa5597a49c9ae52000"   # ostatni commit przed przeniesieniem
PROC = "template/process"
TPL = PROC + "/templates"

MOVES = {
    ".githooks/commit-msg": PROC + "/hooks/commit-msg",
    ".githooks/pre-commit": PROC + "/hooks/pre-commit",
    ".gitignore": ".gitignore",
    "AGENTS.md": PROC + "/AGENTS.md",
    "CLAUDE.md": "CLAUDE.md",
    "Makefile": PROC + "/process.mk",
    "README.md": TPL + "/root/README.md",
    "acceptance.md": "records/acceptance.md",
    "checklist.md": PROC + "/checklist.md",
    "corrections.md": "records/corrections.md",
    "decisions.md": "project/decisions.md",
    "doc/PROPOSAL-CONTEXT-AND-PRACTICE-PACKAGES.md": "reference/PROPOSAL-CONTEXT-AND-PRACTICE-PACKAGES.md",
    "doc/layout-map.md": "reference/layout-map.md",
    "doc/sessions/REF-GTD_system_modeling_with_EARS.md": "reference/sessions/REF-GTD_system_modeling_with_EARS.md",
    "glossary.md": TPL + "/spec/glossary.md",
    "iso-map.html": "reports/iso-map.html",
    "kontrakt-decyzji.md": PROC + "/kontrakt-decyzji.md",
    "modules/navigation/README.md": PROC + "/modules/navigation/README.md",
    "modules/navigation/build.py": PROC + "/modules/navigation/build.py",
    "modules/navigation/check.py": PROC + "/modules/navigation/check.py",
    "modules/navigation/navigation-map.html": TPL + "/spec/navigation/navigation-map.html",
    "modules/navigation/screens.mmd": TPL + "/spec/navigation/screens.mmd",
    "modules/navigation/template.html": PROC + "/modules/navigation/template.html",
    "modules/risks/risks.md": TPL + "/spec/risks.md",
    "modules/state-model/README.md": PROC + "/modules/state-model/README.md",
    "plan.md": TPL + "/project/plan.md",
    "principles.md": TPL + "/spec/principles.md",
    "progress.md": "archive/flat-layout/progress.md",
    "requirements.md": TPL + "/spec/requirements.md",
    "roles/README.md": PROC + "/roles/README.md",
    "roles/verifier.md": PROC + "/roles/verifier.md",
    "scenarios.md": TPL + "/spec/scenarios.md",
    "scope.md": TPL + "/spec/scope.md",
    "tests/README.md": TPL + "/spec/tests/README.md",
    "tools/check_commit.py": PROC + "/tools/check_commit.py",
    "tools/check_leak.allow": "project/check_leak.allow",
    "tools/check_leak.py": PROC + "/tools/check_leak.py",
    "tools/check_refs.allow": "project/check_refs.allow",
    "tools/check_refs.py": PROC + "/tools/check_refs.py",
    "tools/check_separation.py": PROC + "/tools/check_separation.py",
    "tools/golden_master.py": "tests/golden_master.py",
    "tools/id.toml": PROC + "/tools/id.toml",
    "tools/iso29110.toml": PROC + "/tools/iso29110.toml",
    "tools/iso_map.py": PROC + "/tools/iso_map.py",
    "tools/model.py": PROC + "/tools/model.py",
    "tools/new_project.py": PROC + "/tools/init.py",
    "tools/process_kit_view.py": "archive/tools/process_kit_view.py",
    "tools/process_update.py": PROC + "/tools/process_update.py",
    "tools/progress.py": PROC + "/tools/progress.py",
    "tools/restore_check.py": PROC + "/tools/restore_check.py",
    "tools/test_distribution.py": "tests/test_distribution.py",
    "tools/test_report.py": PROC + "/tools/test_report.py",
    "tools/test_tools.py": PROC + "/tools/test_tools.py",
    "tools/trace.py": PROC + "/tools/trace.py",
    "trace.md": "archive/flat-layout/trace.md",
    "use-cases.md": TPL + "/spec/use-cases.md",
    "validation.md": "records/validation.md",
    "verification.md": "records/verification.md",
}
# pliki, które zostają na miejscu (spec/, project/plan.md, reports/, reference/golden/)
STAY_PREFIXES = ("spec/", "project/plan.md", "reports/", "reference/golden/")

EDITED = {
    # narzędzia i hooki: nowe ścieżki (model śladu, raporty, korzeń projektu), D-56, D-73
    *(PROC + "/tools/" + n for n in ("check_commit.py", "check_leak.py", "check_refs.py", "check_separation.py",
                                     "id.toml", "init.py", "iso29110.toml", "iso_map.py", "model.py", "process_update.py",
                                     "progress.py", "restore_check.py", "test_report.py", "test_tools.py", "trace.py")),
    PROC + "/hooks/commit-msg", PROC + "/hooks/pre-commit",
    PROC + "/modules/navigation/README.md", PROC + "/modules/navigation/build.py",
    PROC + "/modules/navigation/check.py", PROC + "/modules/state-model/README.md",
    # reguły procesu: ścieżki i D-56
    PROC + "/AGENTS.md", PROC + "/process.mk", PROC + "/checklist.md", PROC + "/kontrakt-decyzji.md",
    PROC + "/roles/README.md", PROC + "/roles/verifier.md",
    # wzorce: bez tabeli terminów (D-57), umowa w planie (D-41), start według D-44, nowe ścieżki
    TPL + "/root/README.md", TPL + "/spec/glossary.md", TPL + "/project/plan.md",
    TPL + "/spec/requirements.md", TPL + "/spec/scenarios.md", TPL + "/spec/scope.md",
    TPL + "/spec/use-cases.md", TPL + "/spec/principles.md", TPL + "/spec/tests/README.md",
    TPL + "/spec/risks.md", TPL + "/spec/navigation/screens.mmd", TPL + "/spec/navigation/navigation-map.html",
    # warstwa procesu: wpięcie, rejestr, plan, wyjątki, testy, raporty generowane
    "CLAUDE.md", ".gitignore", "project/decisions.md", "project/plan.md",
    "project/check_refs.allow", "project/check_leak.allow",
    "spec/requirements.md", "spec/tests/process-kit.feature",
    "tests/golden_master.py", "tests/test_distribution.py", "archive/tools/process_kit_view.py",
    "reports/trace.md", "reports/progress.md", "reports/iso-map.html", "reports/test-report.md",
    "reference/layout-map.md",
}

NEW = {
    "README.md", "AGENTS.md", "Makefile", "copier.yml", "CHANGELOG.md", "project/settings.toml",
    "tests/test_move.py", "reference/tdd/test_move-red.txt",
    "template/.copier-answers.process.yml.jinja",
    PROC + "/MIGRATIONS.md", PROC + "/terms.md",
    TPL + "/root/AGENTS.md", TPL + "/root/CLAUDE.md", TPL + "/root/Makefile", TPL + "/root/.gitignore",
    TPL + "/project/agreement.md", TPL + "/project/decisions.md", TPL + "/project/settings.toml",
    TPL + "/project/check_refs.allow", TPL + "/project/check_leak.allow",
    TPL + "/records/acceptance.md", TPL + "/records/corrections.md",
    TPL + "/records/validation.md", TPL + "/records/verification.md",
}

# pozostałości przejściowe, których po przeniesieniu nie może być w wyjątkach check_refs (K-10)
TRANSITIONAL_ALLOW = ("template/", "template/process/", "init.py", "process/")

CASES, CURRENT = {}, [None]


def case(name):
    CURRENT[0] = name
    CASES.setdefault(name, True)


def fail(msg):
    CASES[CURRENT[0]] = False
    print(f"  BŁĄD [{CURRENT[0]}]: {msg}")


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)


def blob(rev, path):
    r = git("rev-parse", f"{rev}:{path}")
    return r.stdout.strip() if r.returncode == 0 else None


def run(*args, env=None):
    e = dict(os.environ, **(env or {}))
    return subprocess.run([sys.executable, "-B", *args], cwd=ROOT, capture_output=True, text=True, env=e)


def target(path):
    if path in MOVES:
        return MOVES[path]
    if path.startswith(STAY_PREFIXES):
        return path
    return None


def main():
    base_files = git("ls-tree", "-r", "--name-only", BASE).stdout.split("\n")
    base_files = [f for f in base_files if f]
    head_files = set(f for f in git("ls-files").stdout.split("\n") if f)

    case("k-2")   # nic nie zginęło: każdy plik z BASE ma miejsce i ono istnieje
    for f in base_files:
        t = target(f)
        if t is None:
            fail(f"{f}: brak w liście przeniesień")
        elif t not in head_files:
            fail(f"{f} → {t}: nie ma pliku po przeniesieniu")

    case("k-1")   # pliki są tam, gdzie mapa, i nic nie leży poza mapą
    expected = {target(f) for f in base_files if target(f)} | NEW
    for f in sorted(head_files - expected):
        fail(f"{f}: plik spoza mapy")
    for f in sorted(expected - head_files):
        fail(f"{f}: brak pliku z mapy")
    for f in sorted(EDITED - head_files):
        fail(f"{f}: na liście zmienionych, ale nie istnieje")

    case("k-3")   # treść bez zmian poza listą EDITED
    compared = 0
    for f in base_files:
        t = target(f)
        if t and t in head_files and t not in EDITED:
            compared += 1
            if blob(BASE, f) != blob("HEAD", t):
                fail(f"{f} → {t}: treść zmieniona, a plik nie jest na liście EDITED")
    if compared < len([f for f in base_files if target(f) not in EDITED]):
        fail(f"porównano {compared} plików, a niezmienionych ma być {len([f for f in base_files if target(f) not in EDITED])}")
    for f in sorted(EDITED & head_files):
        if git("diff", "--quiet", "HEAD", "--", f).returncode != 0:
            fail(f"{f}: niezacommitowane zmiany")

    case("k-4")   # historia sięga sprzed przeniesienia
    ancestors = set(git("rev-list", BASE).stdout.split())
    moved = [f for f in base_files if target(f) and target(f) != f]
    for f in moved:
        t = target(f)
        if t not in head_files:
            fail(f"{t}: brak pliku, historii nie da się sprawdzić ({f})")
            continue
        log = set(git("log", "--follow", "--format=%H", "--", t).stdout.split())
        if not log & ancestors:
            fail(f"{t}: git log --follow nie sięga sprzed przeniesienia ({f})")

    case("k-5")   # wyjścia narzędzi zgodne ze złotym wzorcem
    golden = os.path.join(ROOT, "tests", "golden_master.py")
    if not os.path.exists(golden):
        fail("brak tests/golden_master.py")
    else:
        r = run("tests/golden_master.py", "compare", "reference/golden",
                *[x for p in ("spec/", "project/", "records/", "reports/", "process/") for x in ("--strip", p)])
        if r.returncode != 0:
            fail("złoty wzorzec: różnice\n" + r.stdout[-1500:])

    case("k-6")   # ślad warstwy procesu liczony wprost, bez widoku
    trace = os.path.join(ROOT, PROC, "tools", "trace.py")
    if not os.path.exists(trace):
        fail(f"brak {PROC}/tools/trace.py")
    else:
        out = os.path.join(ROOT, ".test_move_trace.md")
        r = run(f"{PROC}/tools/trace.py", out, env={"PROCESS_ROOT": ROOT})
        if r.returncode != 0:
            fail("ślad warstwy procesu ma błędy:\n" + "\n".join(l for l in r.stdout.splitlines() if l.startswith("E"))[:1500])
        before = git("show", f"{BASE}:reports/trace.md").stdout
        ids_before = set(re.findall(r"^\| ([A-Z][A-Z-]*-\d{2}) \|", before, re.M))
        ids_now = set(re.findall(r"^\| ([A-Z][A-Z-]*-\d{2}) \|", open(out, encoding="utf-8").read(), re.M)) \
            if os.path.exists(out) else set()
        if os.path.exists(out):
            os.remove(out)
        lost = sorted(ids_before - ids_now)
        if lost:
            fail(f"elementy warstwy procesu zniknęły ze śladu: {', '.join(lost[:20])}")
    if "tools/process_kit_view.py" in head_files or "archive/tools/process_kit_view.py" not in head_files:
        fail("process_kit_view.py nie jest w archive/tools/")

    case("k-8")   # LAY-01 i LAY-02 mają testy automatyczne
    feature = os.path.join(ROOT, "spec", "tests", "process-kit.feature")
    text = open(feature, encoding="utf-8").read()
    for req in ("LAY-01", "LAY-02"):
        block = re.search(r"# verifies: " + req + r"\n\s*# runner: (\S.*)", text)
        if not block:
            fail(f"{req}: brak testu z runner:")

    case("k-9")   # w szablonie nic z warstwy procesu, bez przecieku domeny
    for f in sorted(x for x in head_files if x.startswith("template/")):
        try:
            content = open(os.path.join(ROOT, f), encoding="utf-8").read()
        except (UnicodeDecodeError, FileNotFoundError):
            continue
        if re.search(r"^### (VER-01|D-0[2-9]|D-[1-9]\d)\b", content, re.M) and not f.endswith("test_tools.py"):
            fail(f"{f}: zawiera rekord albo decyzję warstwy procesu")
    if not any(f.startswith("template/") for f in head_files):
        fail("brak katalogu template/")
    else:
        r = run(f"{PROC}/tools/check_leak.py", PROC, env={"PROCESS_ROOT": ROOT})
        if r.returncode != 0:
            fail("check_leak na pakiecie:\n" + r.stdout[-800:])

    case("k-10")  # odwołania do ścieżek bez przejściowych wyjątków
    allow = os.path.join(ROOT, "project", "check_refs.allow")
    if not os.path.exists(allow):
        fail("brak project/check_refs.allow")
    else:
        entries = [l.split(" # ")[0].strip() for l in open(allow, encoding="utf-8") if l.strip() and not l.startswith("#")]
        left = [e for e in entries if e in TRANSITIONAL_ALLOW]
        if left:
            fail(f"przejściowe wyjątki zostały: {', '.join(left)}")
        # na świeżym klonie HEAD: resztki w katalogu roboczym (puste katalogi po git mv,
        # ignorowane __pycache__) nie mogą zamaskować brakującej ścieżki
        with tempfile.TemporaryDirectory() as tmp:
            clone = os.path.join(tmp, "clone")
            subprocess.run(["git", "clone", "-q", ROOT, clone], check=True, capture_output=True)
            r = subprocess.run([sys.executable, "-B", os.path.join(clone, PROC, "tools", "check_refs.py")],
                               cwd=clone, capture_output=True, text=True,
                               env=dict(os.environ, PROCESS_ROOT=clone))
        if r.returncode != 0:
            fail("check_refs na klonie HEAD:\n" + r.stdout[-800:])

    for name, ok in CASES.items():
        print(f"CASE {name}: {'pass' if ok else 'fail'}")
    failed = [n for n, ok in CASES.items() if not ok]
    print(f"test_move: {len(CASES)} kryteriów, nie przeszło {len(failed)}" + (f" ({', '.join(failed)})" if failed else ""))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
