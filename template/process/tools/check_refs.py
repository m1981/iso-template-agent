"""Integralność odwołań do ścieżek (szablon D-61): każda ścieżka wspomniana w dokumentach i kodzie istnieje.

Szuka w plikach słów wyglądających jak ścieżka: nazwa pliku ze znanym rozszerzeniem (np. roles/verifier.md,
trace.py) albo katalog zakończony ukośnikiem (np. tools/, process/roles/). Ścieżkę szuka względem
katalogu głównego i względem katalogu pliku, który o niej wspomina. Pomija: wzorce i miejsca do
uzupełnienia (*, nn, <…>, {…}, …), adresy URL, ścieżki bezwzględne i ścieżki z listy wyjątków.

Lista wyjątków (project/check_refs.allow, należy do projektu): jedna ścieżka na wiersz, po niej „ # ” i powód, np. pliki,
które powstają dopiero w projekcie albo po wdrożeniu modułu. Wpis, który już nie jest potrzebny
(ścieżka istnieje albo nikt o niej nie wspomina), też jest błędem, żeby lista nie rosła bez kontroli.

W projekcie (pakiet w process/) pakiet jest pomijany: sprawdza go repozytorium szablonu.
Sama nazwa pliku bez katalogu (np. „trace.py”) wystarcza, gdy jakiś śledzony plik ma taką nazwę.
Pomijane pliki: rejestr decyzji, doc/ i materiały wejściowe (zapis historii i planów, w tym ścieżek
dawnych i przyszłych), pliki generowane, .gitignore (wzorce), kod testów i scenariusze .feature (ścieżki danych testowych
w katalogu tymczasowym; sprawdza je uruchomienie testów).

Względem korzenia, katalogu pliku, pakietu procesu, katalogu nad pakietem (układ projektu) i wzorców.

Użycie: python3 process/tools/check_refs.py [--root KATALOG] [plik_lub_katalog ...]
        (bez argumentów: wszystkie śledzone przez git pliki tekstowe)
Kod wyjścia: 0 brak błędów, 1 błędy.
"""
import os
import re
import subprocess
import sys

TOOLS_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, TOOLS_DIR)
import model as M  # noqa: E402

ROOT = M.ROOT
ALLOW = os.path.join("project", "check_refs.allow")

EXT = r"(?:md|py|toml|html|feature|mmd|yml|yaml|json|jinja|txt|log|mk|sh)"
PATH_RE = re.compile(r"(?<![\w/.@$\\-])((?:\.{0,2}[\w-]+/)*\.?[\w-]+(?:\.[\w-]+)*\." + EXT + r")(?![\w/-])"
                     r"|(?<![\w/.@$\\-])((?:\.?[\w-]+/)+)(?![\w.*-])")
SKIP_FILES = {"decisions.md", "trace.md", "progress.md", "iso-map.html", "test-report.md", ".gitignore"}
SKIP_DIRS = ("reference/", "archive/")
PLACEHOLDER = re.compile(r"nn|\*|<|>|\{|\}|…|\$|%")


def tracked(root):
    out = subprocess.run(["git", "ls-files"], cwd=root, capture_output=True, text=True).stdout.split("\n")
    return [p for p in out if p]


def scanned(rel):
    return (os.path.basename(rel) not in SKIP_FILES and not rel.startswith(SKIP_DIRS)
            and not os.path.basename(rel).startswith("test_") and not rel.endswith(".feature")
            and not rel.endswith((".allow",)))


def load_allow(path):
    allow = {}
    if os.path.exists(path):
        for n, line in enumerate(open(path, encoding="utf-8"), 1):
            text = line.split(" # ", 1)
            entry = text[0].strip()
            if entry and not entry.startswith("#"):
                allow[entry] = (n, text[1].strip() if len(text) > 1 else "")
    return allow


def refs_in(text):
    for lineno, line in enumerate(text.splitlines(), 1):
        if "://" in line:
            line = re.sub(r"\S+://\S+", " ", line)
        for m in PATH_RE.finditer(line):
            ref = m.group(1) or m.group(2)
            if PLACEHOLDER.search(ref) or ref.startswith("/") or ref in ("./", "../"):
                continue
            yield lineno, ref


def bases(root, rel_file):
    """Katalogi, względem których szukamy ścieżki: korzeń, katalog pliku, katalog pakietu procesu (odwołania
    typu roles/…), katalog nad nim (układ projektu: process/…; w repozytorium szablonu to template/) i wzorce
    w pakiecie (dokumenty projektu po init.py: spec/…, project/…, records/…)."""
    proc = M.PROCESS_DIR
    return [root, os.path.join(root, os.path.dirname(rel_file)), proc, os.path.dirname(proc), os.path.join(proc, "templates")]


def exists(root, rel_file, ref, basenames):
    for base in bases(root, rel_file):
        if os.path.exists(os.path.normpath(os.path.join(base, ref))):
            return True
    # sama nazwa pliku (np. „trace.py”) wskazuje śledzony plik o tej nazwie w dowolnym katalogu
    return "/" not in ref and ref in basenames


def main(argv):
    root = ROOT
    if "--root" in argv:
        i = argv.index("--root")
        root = os.path.abspath(argv[i + 1])
        argv = argv[:i] + argv[i + 2:]
    allow_path = os.path.join(root, ALLOW)
    allow = load_allow(allow_path)
    files = tracked(root)
    if argv:
        files = [f for f in files if any(f == a or f.startswith(a.rstrip("/") + "/") for a in argv)]
    basenames = {os.path.basename(f) for f in files}
    proc = os.path.relpath(M.PROCESS_DIR, root).replace(os.sep, "/")
    # w projekcie (pakiet w process/) pakietu nie sprawdzamy: jego odwołania sprawdza repozytorium szablonu,
    # gdzie pakiet leży w template/process/ i każde odwołanie jest rozwiązane albo ma wyjątek z powodem
    skip_payload = proc == "process"
    errors, used = [], set()
    for rel in files:
        if not scanned(rel) or (skip_payload and rel.startswith(proc + "/")):
            continue
        try:
            text = open(os.path.join(root, rel), encoding="utf-8").read()
        except (UnicodeDecodeError, FileNotFoundError):
            continue
        for lineno, ref in refs_in(text):
            if exists(root, rel, ref, basenames):
                continue
            if ref in allow:
                used.add(ref)
                continue
            errors.append(f"{rel}:{lineno}: brak ścieżki „{ref}”")
    if not argv:
        for ref, (n, reason) in sorted(allow.items()):
            if not reason:
                errors.append(f"{os.path.relpath(allow_path, root)}:{n}: wyjątek „{ref}” bez powodu")
            elif ref not in used:
                errors.append(f"{os.path.relpath(allow_path, root)}:{n}: zbędny wyjątek „{ref}” (ścieżka istnieje albo nikt o niej nie wspomina)")
    for e in errors:
        print(e)
    print(f"check_refs: {len([f for f in files if scanned(f)])} plików, {len(errors)} błędów, wyjątków użytych {len(used)}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
