"""Start nowego projektu z kopii szablonu (D-22).

Przenosi historię szablonu (decisions.md, trace.md, progress.md) do archive/template/
(archiwizuje, niczego nie usuwa) i zakłada pusty rejestr z jedną decyzją D-01
„Start projektu z szablonu”, żeby pierwszy commit miał ID (hook commit-msg).
Potem odświeża trace.md i progress.md.

Odmawia, gdy archive/template/ już istnieje (projekt był już założony), gdy katalog
nie jest repozytorium gita albo gdy są niezacommitowane zmiany (żeby każdy krok dało
się cofnąć gitem). Projekt zaczyna się od kopii plików bez historii szablonu (README.md, Start).

Użycie: python3 tools/new_project.py   (albo: make new-project)
"""
import datetime
import os
import subprocess
import sys

TOOLS_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(TOOLS_DIR)
ARCHIVE = os.path.join("archive", "template")
MOVED = ["decisions.md", "trace.md", "progress.md"]

HEADER = """# Rejestr decyzji

Pamięć projektu między sesjami (kontrakt-decyzji.md). Agent aktualizuje rejestr po każdej odpowiedzi Użytkownika. ID są niezmienne. Artefakty wskazują decyzję w swoich polach (`source:`, `established_by:`, `changed_by:`); rejestr nie wylicza swoich dzieci, robi to trace.md. Treść po polsku, nazwy pól i stanów po angielsku. Historia szablonu, z którego powstał projekt: archive/template/decisions.md.

Format:

```
### D-nn Tytuł zwykłymi słowami
- status: open | resolved | deferred
- options: A) … · B) …
- proposal: A
- choice: A — co dokładnie postanowiono
- date: RRRR-MM-DD

### Q-nn Temat w kolejce
- notes: skąd się wziął
```

## Otwarte

Brak otwartych decyzji.

## W kolejce

Brak tematów w kolejce.

## Rozstrzygnięte

### D-01 Start projektu z szablonu
- status: resolved
- choice: projekt założony z szablonu ai-sldc-template{version}; historia szablonu w archive/template/
- date: {date}
"""


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)


def main():
    if os.path.exists(os.path.join(ROOT, ARCHIVE)):
        print(f"new_project: {ARCHIVE}/ już istnieje; projekt był już założony, nic nie zmieniam.")
        return 1
    inside = git("rev-parse", "--show-toplevel")
    if inside.returncode != 0 or os.path.realpath(inside.stdout.strip()) != os.path.realpath(ROOT):
        print("new_project: ten katalog nie jest repozytorium gita; najpierw git init i pierwszy commit (README.md, Start).")
        return 1
    status = git("status", "--porcelain")
    if status.stdout.strip():
        print("new_project: w repozytorium są niezacommitowane zmiany; zacommituj je albo odłóż i uruchom ponownie.")
        return 1
    tag = git("describe", "--tags", "--abbrev=0").stdout.strip()
    version = f", wersja {tag}" if tag else ""
    os.makedirs(os.path.join(ROOT, ARCHIVE))
    for name in MOVED:
        src = os.path.join(ROOT, name)
        if os.path.exists(src):
            os.rename(src, os.path.join(ROOT, ARCHIVE, name))
            print(f"przeniesiono {name} -> {ARCHIVE}/{name}")
    with open(os.path.join(ROOT, "decisions.md"), "w", encoding="utf-8") as f:
        f.write(HEADER.format(version=version, date=datetime.date.today().isoformat()))
    print("założono nowy decisions.md z decyzją D-01")
    for script in ("trace.py", "progress.py"):
        subprocess.run([sys.executable, "-B", os.path.join(TOOLS_DIR, script)], cwd=ROOT)
    print()
    print("Dalej: uzupełnij tools/id.toml (system) i plan.md, potem:")
    print('  git add -A && git commit -m "Start projektu (D-01)"')
    print("Jeśli repozytorium jest klonem szablonu, ustaw własny remote: git remote set-url origin <adres>")
    return 0


if __name__ == "__main__":
    sys.exit(main())
