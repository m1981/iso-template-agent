"""Sprawdzenie odtworzenia repozytorium z kopii zapasowej (szablon D-35; ISO/IEC 29110 PM.02.07).

Klonuje remote „origin” do katalogu tymczasowego i sprawdza punkty listy REPO z process/checklist.md:
  REPO.1 klon bieżącej gałęzi ma ten sam ostatni commit co repozytorium lokalne (HEAD),
  REPO.2 klon ma te same tagi,
  REPO.3 w klonie process/tools/trace.py przechodzi bez błędów.
Niczego nie zmienia w repozytorium, chyba że podano --record: wtedy dopisuje do records/verification.md
rekord VER z subject: repository (zacommituj go jak każdą zmianę).

Użycie: python3 process/tools/restore_check.py [--record] [--remote origin]
        make restore-check            make restore-check RECORD=1
Kod wyjścia: 0 gdy wszystkie punkty spełnione, 1 gdy nie, 2 gdy nie da się sklonować.
"""
import datetime
import os
import re
import subprocess
import sys
import tempfile

TOOLS_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, TOOLS_DIR)
import model as M  # noqa: E402

ROOT = M.ROOT
VERIFICATION = os.path.join("records", "verification.md")


def git(*args, cwd=ROOT):
    return subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True)


def next_ver_id(fpath):
    used = [int(n) for n in re.findall(r"^#{2,4}\s+VER-(\d{2})\b", open(fpath, encoding="utf-8").read(), re.M)]
    return f"VER-{max(used, default=0) + 1:02d}"


def main(argv):
    record = "--record" in argv
    remote = argv[argv.index("--remote") + 1] if "--remote" in argv else "origin"
    url = git("remote", "get-url", remote).stdout.strip()
    if not url:
        print(f"restore_check: brak remote „{remote}”; ustaw kopię zapasową (README.md, Start).")
        return 2
    local_head = git("rev-parse", "HEAD").stdout.strip()
    branch = git("rev-parse", "--abbrev-ref", "HEAD").stdout.strip()
    local_tags = set(git("tag").stdout.split())
    dirty = bool(git("status", "--porcelain").stdout.strip())
    failed, notes = [], []
    with tempfile.TemporaryDirectory() as tmp:
        clone = os.path.join(tmp, "klon")
        r = git("clone", "--quiet", "--branch", branch, url, clone, cwd=tmp)
        if r.returncode != 0:
            print(f"restore_check: nie udało się sklonować gałęzi {branch} z {url}:\n{r.stderr.strip()}")
            return 2
        clone_head = git("rev-parse", "HEAD", cwd=clone).stdout.strip()
        clone_tags = set(git("tag", cwd=clone).stdout.split())
        if clone_head != local_head:
            failed.append("REPO.1")
            notes.append(f"HEAD lokalnie {local_head[:12]}, w kopii {clone_head[:12]} (niewypchnięte commity?)")
        if clone_tags != local_tags:
            failed.append("REPO.2")
            missing = sorted(local_tags - clone_tags)
            extra = sorted(clone_tags - local_tags)
            notes.append("tagi " + "; ".join(x for x in (
                f"brak w kopii: {', '.join(missing)}" if missing else "",
                f"tylko w kopii: {', '.join(extra)}" if extra else "") if x))
        r = subprocess.run([sys.executable, "-B", os.path.join(os.path.relpath(TOOLS_DIR, ROOT), "trace.py"), os.devnull],
                           cwd=clone, capture_output=True, text=True, env=dict(os.environ, PROCESS_ROOT=clone))
        if r.returncode != 0:
            failed.append("REPO.3")
            notes.append("ślad w klonie ma błędy: " + "; ".join(l for l in r.stdout.splitlines() if l.startswith("E"))[:300])
    result = "fail" if failed else "pass"
    summary = f"kopia {url}, HEAD {clone_head[:12]}, tagi {len(clone_tags)}"
    if dirty:
        notes.append("w repozytorium lokalnym były niezacommitowane zmiany (nie trafiają do kopii)")
    print(f"restore_check: {result} — {summary}")
    for n in notes:
        print("  " + n)
    if record:
        fpath = os.path.join(ROOT, VERIFICATION)
        ident = next_ver_id(fpath)
        block = (f"\n### {ident} Odtworzenie repozytorium z kopii zapasowej\n"
                 f"- subject: repository\n- date: {datetime.date.today().isoformat()}\n"
                 f"- by: make restore-check\n- checklist: REPO\n- result: {result}\n"
                 + (f"- failed: {', '.join(failed)}\n" if failed else "")
                 + f"- notes: {summary}" + ("; " + "; ".join(notes) if notes else "") + "\n")
        text = open(fpath, encoding="utf-8").read()
        text = text.replace("\nBrak weryfikacji.\n", "\n") if "\nBrak weryfikacji.\n" in text else text
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(text.rstrip("\n") + "\n" + block)
        print(f"restore_check: dopisano {ident} do {VERIFICATION}; odśwież ślad (make check) i zacommituj.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
