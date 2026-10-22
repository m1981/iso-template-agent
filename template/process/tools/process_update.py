"""Bramka aktualizacji procesu w projekcie (szablon D-52, szablon D-47, szablon D-49, szablon D-51).

Aktualizuje pakiet procesu copierem do jawnie podanej wersji i sprawdza wynik. Kod 0 copiera
nie wystarcza: copier potrafi zakończyć update kodem 0 i zostawić konflikt (próba przy szablon D-43).

Kolejno:
  1. odmawia, gdy wersja nie ma postaci vX.Y.Z, gdy nie ma pliku answers, gdy drzewo nie jest
     czyste (także nieśledzone pliki) albo gdy copier ma inną wersję niż przypięta;
  2. uruchamia copier update z --vcs-ref i --conflict inline; pełny log i kod wyjścia zapisuje
     w .git/process-update.log (poza plikami projektu);
  3. sprawdza: brak konfliktów (indeks, znaczniki w zmienionych i nowych plikach, pliki .rej),
     zmiany tylko w process/ i w pliku answers, wersja w answers równa podanej;
  4. uruchamia walidację projektu (make check, make test).
Niczego nie commituje, nie robi stash, nie instaluje hooków. Pakiet zaktualizowany nie znaczy,
że migracja dokumentów jest zakończona (szablon D-51): to osobny krok.

Użycie: python3 tools/process_update.py vX.Y.Z [--defaults]   (albo: make process-update V=vX.Y.Z)
Kod wyjścia: 0 wszystko spełnione; 1 aktualizacja wykonana, ale wynik nie przeszedł kontroli
(zmiany zostają do przeglądu); 2 odmowa przed uruchomieniem copiera (nic nie zmieniono).
"""
import os
import re
import shutil
import subprocess
import sys

COPIER_VERSION = "9.19.1"   # przypięta wersja (szablon D-49); zmiana tylko po teście granicy dystrybucji
ANSWERS = ".copier-answers.process.yml"
PAYLOAD = "process/"
CHECKS = [["make", "check"], ["make", "test"]]
VERSION_RE = re.compile(r"^v\d+\.\d+\.\d+$")
MARKER_RE = re.compile(r"^(<<<<<<<|>>>>>>>)( |$)", re.M)


def run(cmd, cwd):
    return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)


def refuse(msg):
    print(f"process_update: odmowa, nic nie zmieniono: {msg}")
    sys.exit(2)


def changed_paths(root):
    """Ścieżki zmienione, nowe i usunięte względem HEAD (z nieśledzonymi, bez ignorowanych)."""
    out = run(["git", "status", "--porcelain=v1", "-z", "--untracked-files=all"], root).stdout
    items, parts, i = [], out.split("\0"), 0
    while i < len(parts):
        entry = parts[i]
        if not entry:
            i += 1
            continue
        code, path = entry[:2], entry[3:]
        if code[0] in "RC":          # przy zmianie nazwy następny element to stara ścieżka
            items.append((code, parts[i + 1]))
            i += 1
        items.append((code, path))
        i += 1
    return items


def find_conflicts(root, changes):
    """Konflikty: wpisy nierozstrzygnięte w indeksie, pliki .rej, znaczniki <<<<<<< / >>>>>>>
    w zmienionych i nowych plikach (linia ======= sama nie wystarcza: tak podkreśla się nagłówki)."""
    unmerged = run(["git", "ls-files", "-u"], root).stdout.strip()
    found = {line.split("\t", 1)[1] for line in unmerged.splitlines()}
    for _, path in changes:
        full = os.path.join(root, path)
        if path.endswith(".rej"):
            found.add(path)
        elif os.path.isfile(full):
            try:
                text = open(full, encoding="utf-8").read()
            except UnicodeDecodeError:
                continue
            if MARKER_RE.search(text):
                found.add(path)
    return sorted(found)


def answers_commit(root):
    for line in open(os.path.join(root, ANSWERS), encoding="utf-8"):
        m = re.match(r"^_commit:\s*['\"]?([^'\"\s]+)", line)
        if m:
            return m.group(1)
    return None


def main(argv):
    args = [a for a in argv if not a.startswith("--")]
    defaults = "--defaults" in argv
    if len(args) != 1 or not VERSION_RE.match(args[0]):
        refuse("podaj wersję postaci vX.Y.Z, np. make process-update V=v1.2.0")
    version = args[0]

    top = run(["git", "rev-parse", "--show-toplevel"], os.getcwd())
    if top.returncode != 0:
        refuse("katalog nie jest repozytorium gita")
    root = top.stdout.strip()
    if os.path.realpath(root) != os.path.realpath(os.getcwd()):
        refuse(f"uruchom w katalogu głównym repozytorium ({root})")
    if not os.path.isfile(os.path.join(root, ANSWERS)):
        refuse(f"brak {ANSWERS}: projekt nie powstał z szablonu przez copier copy")
    dirty = changed_paths(root)
    if dirty:
        refuse("niezacommitowane zmiany lub nieśledzone pliki: " + ", ".join(p for _, p in dirty[:5]))
    copier = shutil.which("copier")
    if not copier:
        refuse(f"brak copiera; zainstaluj copier=={COPIER_VERSION}")
    got = run([copier, "--version"], root).stdout.strip().split()[-1:]
    if got != [COPIER_VERSION]:
        refuse(f"copier {' '.join(got) or '?'}, przypięta wersja to {COPIER_VERSION}")

    before = answers_commit(root)
    cmd = [copier, "update", "--answers-file", ANSWERS, "--vcs-ref", version, "--conflict", "inline"]
    if defaults:
        cmd.append("--defaults")
    log_path = run(["git", "rev-parse", "--git-path", "process-update.log"], root).stdout.strip()
    log_path = os.path.join(root, log_path)
    with open(log_path, "w", encoding="utf-8") as log:
        log.write("$ " + " ".join(cmd) + "\n")
        log.flush()
        if defaults:
            # bez pytań: całe wyjście do logu
            proc = subprocess.run(cmd, cwd=root, stdout=log, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL)
        else:
            # nowe pytania wydania odpowiada człowiek, więc wyjście idzie na ekran; log ma polecenie i kod
            log.write("[tryb z pytaniami: wyjście copiera na ekranie]\n")
            log.flush()
            proc = subprocess.run(cmd, cwd=root)
        log.write(f"\n[kod wyjścia copiera: {proc.returncode}]\n")

    problems = []
    print(f"process_update: {before} → {version}; log: {os.path.relpath(log_path, root)}")
    print(f"  1. copier update: kod {proc.returncode}")
    if proc.returncode != 0:
        problems.append(f"copier zakończył się kodem {proc.returncode} (szczegóły w logu)")

    changes = changed_paths(root)
    conflicted = find_conflicts(root, changes)
    print("  2. konflikty: " + (", ".join(conflicted) if conflicted else "brak"))
    if conflicted:
        problems.append("konflikty do rozstrzygnięcia: " + ", ".join(conflicted))

    outside = sorted({p for _, p in changes if not (p.startswith(PAYLOAD) or p == ANSWERS)})
    print(f"  3. zakres (tylko {PAYLOAD} i {ANSWERS}): " + (", ".join(outside) if outside else "spełniony"))
    if outside:
        problems.append("zmiany poza zakresem pakietu: " + ", ".join(outside))

    after = answers_commit(root)
    print(f"  4. wersja w {ANSWERS}: {after}")
    if after != version:
        problems.append(f"{ANSWERS} wskazuje {after} zamiast {version} (szablon D-49: tag wydania nie może dzielić commita z innym tagiem)")

    if not problems:
        results = []
        for check in CHECKS:
            r = run(check, root)
            results.append((" ".join(check), r.returncode))
            if r.returncode != 0:
                tail = (r.stdout + r.stderr).strip().splitlines()[-15:]
                problems.append(f"{' '.join(check)}: kod {r.returncode}\n      " + "\n      ".join(tail))
        print("  5. walidacja: " + ", ".join(f"{c} kod {rc}" for c, rc in results))
    else:
        print("  5. walidacja: nie uruchomiona, bo wcześniejsze punkty nie przeszły")

    if problems:
        print("process_update: NIE PRZESZŁO. Zmiany zostały w katalogu roboczym do przeglądu; nic nie zacommitowano.")
        for p in problems:
            print("  - " + p)
        return 1
    print(f"process_update: pakiet zaktualizowany do {version} i sprawdzony; nic nie zacommitowano.")
    print("  Przejrzyj git diff i zacommituj. Migracja istniejących dokumentów to osobny krok (szablon D-51).")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
