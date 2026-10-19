"""Test granicy dystrybucji procesu copierem (D-50 krok 1; D-43, D-47, D-49, D-52).

Buduje w katalogu tymczasowym mały szablon (copier.yml, template/process/…, w nim prawdziwa
bramka tools/process_update.py) z wydaniami v1.0.0…v1.3.0 i projekty z niego, po czym sprawdza:
  copy        payload i answers powstają, nic spoza process/ nie trafia do projektu
  update      v1.0.0→v1.1.0: nowa funkcja działa, pliki projektu bajt w bajt bez zmian
  repeat      drugi update do tej samej wersji nie zmienia drzewa
  version     wersja inna niż vX.Y.Z (1.1.0, v1.1, latest, HEAD): odmowa na czystym drzewie
  markers     znaczniki konfliktu w nowym pliku i pliki .rej są wykrywane bez wpisu w indeksie;
              podkreślenie nagłówka ======= nie jest konfliktem
  binary      konflikt pliku binarnego wykrywa indeks gita (znaczników nie da się przeczytać)
  missing     nieistniejące wydanie: copier kończy się błędem, bramka go zgłasza
  conflict    lokalna zmiana w process/ w miejscu zmienionym w wydaniu: copier kod 0, bramka kod 1
  dirty       brudne drzewo: bramka odmawia przed copierem (kod 2), drzewo bez zmian
  tags        tag baseline na commicie wydania: bramka przechodzi tylko, gdy answers ma vX.Y.Z
  jump        skok v1.0.0→v1.2.0 (najstarsza wspierana wersja) daje zmiany obu wydań
  scope       wydanie zmieniające plik poza process/: bramka kod 1
  validation  stary dokument łamie nową regułę: bramka kod 1, nic nie zacommitowano
  hooks       make hooks nie nadpisuje core.hooksPath ustawionego przez inny menedżer
  isolation   każde polecenie git działa we własnym repozytorium fixture; repozytorium,
              z którego uruchomiono test, nie zmienia się
Każda mutacja jest sprawdzana, zanim test oceni kontrolę (zasiew musi się udać).

Użycie: python3 tools/test_distribution.py   (albo: make test-distribution)
Kod wyjścia: 0 wszystko przeszło, 1 błąd, 2 NIE URUCHOMIONO (brak copiera w przypiętej wersji).
"""
import hashlib
import os
import shutil
import subprocess
import sys
import tempfile

TOOLS_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(TOOLS_DIR)
sys.path.insert(0, TOOLS_DIR)
import process_update as PU  # noqa: E402

ANSWERS = PU.ANSWERS
failures = []


def check(cond, msg):
    if not cond:
        failures.append(msg)
        print("  BŁĄD: " + msg)


def git(repo, *args, expect_ok=True):
    """Git tylko we własnym repozytorium fixture: przed poleceniem sprawdza, gdzie jest."""
    if args[0] != "init":
        top = subprocess.run(["git", "rev-parse", "--show-toplevel"], cwd=repo, capture_output=True, text=True)
        if top.returncode != 0 or os.path.realpath(top.stdout.strip()) != os.path.realpath(repo):
            raise SystemExit(f"test_distribution: przerwano, git nie jest w repozytorium fixture {repo}: {top.stdout.strip()}")
    r = subprocess.run(["git", *args], cwd=repo, capture_output=True, text=True)
    if expect_ok and r.returncode != 0:
        raise SystemExit(f"test_distribution: git {' '.join(args)} w {repo}: {r.stderr.strip()}")
    return r


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def mutate(path, old, new):
    """Zasiew zmiany z asercją, że się wykonał."""
    text = open(path, encoding="utf-8").read()
    if old not in text:
        raise SystemExit(f"test_distribution: zasiew nieudany, brak „{old}” w {path}")
    write(path, text.replace(old, new, 1))
    if open(path, encoding="utf-8").read() == text:
        raise SystemExit(f"test_distribution: zasiew nie zmienił {path}")


def init_repo(repo):
    os.makedirs(repo, exist_ok=True)
    git(repo, "init", "-q")
    git(repo, "config", "user.email", "test@example.invalid")
    git(repo, "config", "user.name", "test")
    git(repo, "config", "commit.gpgsign", "false")


def commit_all(repo, msg):
    git(repo, "add", "-A")
    git(repo, "commit", "-q", "-m", msg)


CHECK_V1 = 'print("check v1.0")\n'
CHECK_V11 = '''import os, sys
# v1.1: nowa reguła dla dokumentów projektu (jak zmiana reguły w trace.py, D-51)
if os.path.exists("spec/old-format.md"):
    print("check v1.1: spec/old-format.md ma stary format, wymagana migracja M-01")
    sys.exit(1)
print("check v1.1")
'''


def build_template(tdir):
    init_repo(tdir)
    write(os.path.join(tdir, "copier.yml"),
          '_min_copier_version: "9.17.1"\n_subdirectory: template\n'
          f'_answers_file: {ANSWERS}\n_templates_suffix: .jinja\n'
          'project_name:\n  type: str\n  default: Projekt\n')
    write(os.path.join(tdir, "README.md"), "Szablon (poza payloadem)\n")
    write(os.path.join(tdir, "template", ANSWERS + ".jinja"), "{{ _copier_answers | to_nice_yaml -}}\n")
    write(os.path.join(tdir, "template", "process", "AGENTS.md"), "Proces wersja 1\nlinia druga\n")
    write(os.path.join(tdir, "template", "process", "tools", "check.py"), CHECK_V1)
    shutil.copy(os.path.join(TOOLS_DIR, "process_update.py"),
                os.path.join(tdir, "template", "process", "tools", "process_update.py"))
    commit_all(tdir, "v1.0.0")
    git(tdir, "tag", "v1.0.0")
    # v1.1.0: zmiana reguły (check.py) i pierwszej linii AGENTS.md
    write(os.path.join(tdir, "template", "process", "tools", "check.py"), CHECK_V11)
    mutate(os.path.join(tdir, "template", "process", "AGENTS.md"), "Proces wersja 1", "Proces wersja 1.1")
    commit_all(tdir, "v1.1.0")
    git(tdir, "tag", "v1.1.0")
    # v1.2.0: nowy plik reguł
    write(os.path.join(tdir, "template", "process", "rules", "nowa.md"), "Nowa reguła\n")
    commit_all(tdir, "v1.2.0")
    git(tdir, "tag", "v1.2.0")
    # v1.3.0: wydanie wadliwe, dodaje plik poza process/
    write(os.path.join(tdir, "template", "README.md"), "README projektu nadpisany przez szablon\n")
    commit_all(tdir, "v1.3.0")
    git(tdir, "tag", "v1.3.0")


def make_client(tdir, cdir, version="v1.0.0"):
    r = subprocess.run(["copier", "copy", "--defaults", "--vcs-ref", version, tdir, cdir],
                       capture_output=True, text=True)
    if r.returncode != 0:
        raise SystemExit(f"test_distribution: copier copy: {r.stderr.strip()}")
    init_repo(cdir)
    write(os.path.join(cdir, "Makefile"),
          "check:\n\tpython3 -B process/tools/check.py\ntest:\n\t@echo test projektu\n")
    write(os.path.join(cdir, "README.md"), "README projektu\n")
    write(os.path.join(cdir, "project", "plan.md"), "Plan projektu\n")
    write(os.path.join(cdir, ".gitignore"), "data/\n")
    write(os.path.join(cdir, "data", "local.db"), "dane trwałe\n")
    commit_all(cdir, "projekt z szablonu " + version)


def snapshot(repo, include_payload=False):
    """Skróty wszystkich plików (także ignorowanych) poza .git; domyślnie bez process/ i answers."""
    out = {}
    for base, dirs, files in os.walk(repo):
        dirs[:] = [d for d in dirs if d != ".git"]
        for name in files:
            rel = os.path.relpath(os.path.join(base, name), repo)
            if not include_payload and (rel.startswith(PU.PAYLOAD) or rel == ANSWERS):
                continue
            out[rel] = hashlib.sha256(open(os.path.join(base, name), "rb").read()).hexdigest()
    return out


def gate(cdir, version):
    r = subprocess.run([sys.executable, "-B", "process/tools/process_update.py", version, "--defaults"],
                       cwd=cdir, capture_output=True, text=True)
    return r.returncode, r.stdout + r.stderr


def copier_rc_from_log(cdir):
    text = open(os.path.join(cdir, ".git", "process-update.log"), encoding="utf-8").read()
    return text.rsplit("[kod wyjścia copiera: ", 1)[-1].split("]")[0]


def root_state():
    def g(*a):
        return subprocess.run(["git", *a], cwd=ROOT, capture_output=True, text=True).stdout
    return g("rev-parse", "HEAD"), g("status", "--porcelain=v1", "--untracked-files=all"), \
        g("config", "--local", "--list"), g("tag")


def main():
    copier = shutil.which("copier")
    if not copier:
        print(f"test_distribution: NIE URUCHOMIONO: brak copiera (pip install copier=={PU.COPIER_VERSION})")
        return 2
    got = subprocess.run([copier, "--version"], capture_output=True, text=True).stdout.split()[-1:]
    if got != [PU.COPIER_VERSION]:
        print(f"test_distribution: NIE URUCHOMIONO: copier {' '.join(got)}, przypięta wersja {PU.COPIER_VERSION}")
        return 2

    before_root = root_state()
    with tempfile.TemporaryDirectory() as tmp:
        tdir = os.path.join(tmp, "szablon")
        build_template(tdir)

        print("copy")
        c = os.path.join(tmp, "copy")
        make_client(tdir, c)
        check(PU.answers_commit(c) == "v1.0.0", f"copy: answers {PU.answers_commit(c)} zamiast v1.0.0")
        payload = sorted(p for p in snapshot(c, include_payload=True) if p.startswith(PU.PAYLOAD) or p == ANSWERS)
        check(payload == [ANSWERS, "process/AGENTS.md", "process/tools/check.py", "process/tools/process_update.py"],
              f"copy: nieoczekiwany payload {payload}")
        check(not os.path.exists(os.path.join(c, "copier.yml")), "copy: copier.yml trafił do projektu")

        print("update")
        before = snapshot(c)
        rc, out = gate(c, "v1.1.0")
        check(rc == 0, f"update: bramka kod {rc}\n{out}")
        check(snapshot(c) == before, "update: zmieniły się pliki poza process/")
        r = subprocess.run([sys.executable, "-B", "process/tools/check.py"], cwd=c, capture_output=True, text=True)
        check("check v1.1" in r.stdout, f"update: nowa funkcja nie działa: {r.stdout.strip()}")
        check(open(os.path.join(c, "process", "AGENTS.md"), encoding="utf-8").read().startswith("Proces wersja 1.1"),
              "update: AGENTS.md procesu bez zmiany z wydania")
        commit_all(c, "aktualizacja procesu v1.1.0")

        print("missing")
        rc, out = gate(c, "v9.9.9")
        check(rc == 1 and "copier zakończył się kodem" in out,
              f"missing: brak zgłoszenia błędu copiera dla nieistniejącego wydania (kod {rc})\n{out}")
        git(c, "checkout", "-q", "--", ".")
        git(c, "clean", "-q", "-fd")
        check(git(c, "status", "--porcelain=v1", "--untracked-files=all").stdout == "", "missing: drzewo nie wróciło do stanu po commicie")

        print("repeat")
        rc, out = gate(c, "v1.1.0")
        check(rc == 0, f"repeat: bramka kod {rc}\n{out}")
        check(git(c, "status", "--porcelain=v1", "--untracked-files=all").stdout == "", "repeat: drzewo zmienione")

        print("version")
        for bad in ("1.1.0", "v1.1", "latest", "HEAD"):
            rc, out = gate(c, bad)
            check(rc == 2 and "vX.Y.Z" in out, f"version: wersja „{bad}” przyjęta (kod {rc})")
        check(git(c, "status", "--porcelain=v1", "--untracked-files=all").stdout == "", "version: drzewo zmienione")

        print("markers")
        m = os.path.join(tmp, "markers")
        init_repo(m)
        write(os.path.join(m, "a.md"), "start\n")
        commit_all(m, "start")
        write(os.path.join(m, "process", "nowy.md"), "<<<<<<< before updating\nx\n=======\ny\n>>>>>>> after updating\n")
        write(os.path.join(m, "a.md"), "Nagłówek\n=======\n")
        write(os.path.join(m, "process", "plik.rej"), "odrzucony fragment\n")
        found = PU.find_conflicts(m, PU.changed_paths(m))
        check(found == ["process/nowy.md", "process/plik.rej"],
              f"markers: wykryte {found}; oczekiwane znaczniki w nowym pliku i .rej, bez nagłówka =======")

        print("binary")
        b = os.path.join(tmp, "binary")
        init_repo(b)
        with open(os.path.join(b, "logo.bin"), "wb") as f:
            f.write(b"\xff\x00wersja-bazowa")
        commit_all(b, "baza")
        git(b, "checkout", "-q", "-b", "inna")
        with open(os.path.join(b, "logo.bin"), "wb") as f:
            f.write(b"\xff\x00wersja-inna")
        commit_all(b, "inna")
        git(b, "checkout", "-q", "-")
        with open(os.path.join(b, "logo.bin"), "wb") as f:
            f.write(b"\xff\x00wersja-glowna")
        commit_all(b, "glowna")
        merge = git(b, "merge", "-q", "inna", expect_ok=False)
        check(merge.returncode != 0, "binary: zasiew nieudany, merge bez konfliktu")
        found = PU.find_conflicts(b, PU.changed_paths(b))
        check(found == ["logo.bin"], f"binary: konflikt pliku binarnego niewykryty (wykryte {found})")

        print("conflict")
        c2 = os.path.join(tmp, "conflict")
        make_client(tdir, c2)
        mutate(os.path.join(c2, "process", "AGENTS.md"), "Proces wersja 1", "Proces wersja 1 z lokalną zmianą")
        commit_all(c2, "lokalna zmiana pliku procesu")
        rc, out = gate(c2, "v1.1.0")
        check(rc == 1 and "konflikty do rozstrzygnięcia" in out and "process/AGENTS.md" in out,
              f"conflict: bramka nie wykryła konfliktu (kod {rc})\n{out}")
        print(f"  copier zakończył się kodem {copier_rc_from_log(c2)} mimo konfliktu")

        print("dirty")
        c3 = os.path.join(tmp, "dirty")
        make_client(tdir, c3)
        mutate(os.path.join(c3, "project", "plan.md"), "Plan projektu", "Plan projektu w toku")
        before = snapshot(c3, include_payload=True)
        rc, out = gate(c3, "v1.1.0")
        check(rc == 2 and "niezacommitowane" in out, f"dirty: oczekiwana odmowa (kod {rc})\n{out}")
        check(snapshot(c3, include_payload=True) == before, "dirty: odmowa zmieniła pliki")

        print("tags")
        t2 = os.path.join(tmp, "szablon-tagi")
        shutil.copytree(tdir, t2)
        git(t2, "tag", "baseline-02-proces", "v1.1.0")
        c4 = os.path.join(tmp, "tags")
        make_client(t2, c4)
        rc, out = gate(c4, "v1.1.0")
        recorded = PU.answers_commit(c4)
        check((rc == 0) == (recorded == "v1.1.0"),
              f"tags: answers {recorded}, bramka kod {rc}: bramka musi przechodzić tylko przy v1.1.0\n{out}")
        print(f"  answers zapisał {recorded}; bramka kod {rc}")

        print("jump")
        c5 = os.path.join(tmp, "jump")
        make_client(tdir, c5)
        rc, out = gate(c5, "v1.2.0")
        check(rc == 0, f"jump: bramka kod {rc}\n{out}")
        check(os.path.exists(os.path.join(c5, "process", "rules", "nowa.md")), "jump: brak pliku z v1.2.0")
        r = subprocess.run([sys.executable, "-B", "process/tools/check.py"], cwd=c5, capture_output=True, text=True)
        check("check v1.1" in r.stdout, "jump: brak zmiany z v1.1.0")
        commit_all(c5, "aktualizacja procesu v1.2.0")

        print("scope")
        before = open(os.path.join(c5, "README.md"), encoding="utf-8").read()
        rc, out = gate(c5, "v1.3.0")
        check(rc == 1 and "poza zakresem" in out and "README.md" in out,
              f"scope: bramka nie wykryła zmiany poza process/ (kod {rc})\n{out}")
        print("  README projektu " + ("zmieniony przez wydanie, bramka zgłosiła"
                                      if open(os.path.join(c5, "README.md"), encoding="utf-8").read() != before
                                      else "bez zmian w treści"))

        print("validation")
        c6 = os.path.join(tmp, "validation")
        make_client(tdir, c6)
        write(os.path.join(c6, "spec", "old-format.md"), "dokument w starym formacie\n")
        commit_all(c6, "dokument projektu")
        head = git(c6, "rev-parse", "HEAD").stdout
        rc, out = gate(c6, "v1.1.0")
        check(rc == 1 and "make check: kod" in out and "M-01" in out,
              f"validation: bramka nie zgłosiła reguły łamanej przez stary dokument (kod {rc})\n{out}")
        check(git(c6, "rev-parse", "HEAD").stdout == head, "validation: bramka coś zacommitowała")
        check("pakiet zaktualizowany" not in out, "validation: bramka ogłosiła sukces")

        print("hooks")
        h = os.path.join(tmp, "hooks")
        init_repo(h)
        shutil.copy(os.path.join(ROOT, "Makefile"), h)
        git(h, "config", "core.hooksPath", ".husky")
        r = subprocess.run(["make", "hooks"], cwd=h, capture_output=True, text=True)
        check(r.returncode != 0 and git(h, "config", "--get", "core.hooksPath").stdout.strip() == ".husky",
              f"hooks: make hooks nadpisał inny menedżer hooków (kod {r.returncode})")
        git(h, "config", "--unset", "core.hooksPath")
        r = subprocess.run(["make", "hooks"], cwd=h, capture_output=True, text=True)
        check(r.returncode == 0 and git(h, "config", "--get", "core.hooksPath").stdout.strip() == ".githooks",
              f"hooks: make hooks nie ustawił .githooks (kod {r.returncode}) {r.stdout}{r.stderr}")

    print("isolation")
    check(root_state() == before_root, "isolation: test zmienił repozytorium, z którego go uruchomiono")

    if failures:
        print(f"test_distribution: {len(failures)} błędów")
        return 1
    print("test_distribution: copy, update, repeat, version, markers, binary, missing, conflict, dirty, tags, jump, scope, validation, hooks, isolation — OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
