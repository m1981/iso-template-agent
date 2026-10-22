"""Przeciek domeny do procesu (D-62, D-57): pliki procesu nie zawierają treści projektu.

Sprawdza pliki procesu (w projekcie z copiera: katalog process/; w tym repozytorium przed
przeniesieniem: lista z Makefile) na dwa sposoby:
  1. konkretne ID elementów projektu (np. przypadek użycia z numerem) są błędem; dozwolone są
     tylko ID zastępcze z „nn” (UC-nn, REQ-nn). ID wymagań (obszar w ID) liczą się tylko w obszarach,
     które projekt już ma, jak przy E2 w trace.py („UTF-16” to nie wymaganie). Nie dotyczy decyzji i kolejki (D-nn, Q-nn): pliki
     procesu powołują się na decyzje szablonu (D-56);
  2. z --glossary PLIK: pojęcie ze słownika projektu (nazwa polska i angielskie z nawiasu)
     w pliku procesu jest błędem.
Pomija kod testów (dane fixture są syntetyczne; sprawdza je uruchomienie testów).

Wyjątki (tools/check_leak.allow): ścieżka pliku # powód. Zbędny wpis to błąd.

Użycie: python3 tools/check_leak.py [--glossary spec/glossary.md] ŚCIEŻKA...
Kod wyjścia: 0 brak przecieku, 1 przeciek.
"""
import os
import re
import sys

TOOLS_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, TOOLS_DIR)
import model as M  # noqa: E402

SKIP_CODES = {"D", "Q"}


def load_allow(path):
    allow = {}
    if os.path.exists(path):
        for n, line in enumerate(open(path, encoding="utf-8"), 1):
            entry, _, reason = line.partition(" # ")
            entry = entry.strip()
            if entry and not entry.startswith("#"):
                allow[entry] = (n, reason.strip())
    return allow


def files_under(root, paths):
    out = []
    for p in paths:
        full = os.path.join(root, p)
        if os.path.isdir(full):
            for base, dirs, names in os.walk(full):
                dirs[:] = [d for d in dirs if d not in ("__pycache__", ".git")]
                out += [os.path.relpath(os.path.join(base, n), root) for n in names]
        elif os.path.isfile(full):
            out.append(p)
    return sorted(set(out))


def glossary_terms(path):
    terms = set()
    for line in open(path, encoding="utf-8"):
        m = re.match(r"^#{2,4}\s+G-[A-Z]{3}-\d{2}\s+(.*?)\s*(?:\(([^()]*)\))?\s*$", line)
        if m:
            names = [m.group(1)] + (m.group(2).split(";") if m.group(2) else [])
            terms |= {n.strip() for n in names if len(n.strip()) >= 4}
    return terms


def main(argv):
    root = M.ROOT
    glossary = None
    if "--glossary" in argv:
        i = argv.index("--glossary")
        glossary = argv[i + 1]
        argv = argv[:i] + argv[i + 2:]
    if "--root" in argv:
        i = argv.index("--root")
        root = os.path.abspath(argv[i + 1])
        argv = argv[:i] + argv[i + 2:]
    m = M.Model(root)
    patterns = [(code, re.compile(r"(?<![\w-])(?:" + t["pattern"] + r")(?![\w-])"))
                for code, t in m.types.items() if code not in SKIP_CODES]
    # typy z obszarem w ID (wymagania): liczą się tylko obszary, które projekt ma (jak E2 w trace.py, D-26),
    # bo „UTF-16” w tekście nie jest wymaganiem
    areas = {code: {e.id.split("-")[0] for e in m.elements if e.type == code}
             for code, t in m.types.items() if t.get("area_prefix")}
    terms = glossary_terms(os.path.join(root, glossary)) if glossary else set()
    term_res = [(t, re.compile(r"(?<!\w)" + re.escape(t) + r"(?!\w)", re.I)) for t in sorted(terms)]
    allow_path = os.path.join(TOOLS_DIR, "check_leak.allow")
    allow = load_allow(allow_path)
    errors, used = [], set()
    for rel in files_under(root, argv or ["process"]):
        if os.path.basename(rel).startswith("test_") or rel.endswith((".allow", ".pyc")):
            continue
        try:
            text = open(os.path.join(root, rel), encoding="utf-8").read()
        except UnicodeDecodeError:
            continue
        found = []
        for lineno, line in enumerate(text.splitlines(), 1):
            for code, rx in patterns:
                found += [f"{rel}:{lineno}: konkretne ID {x.group(0)} ({code}); w procesie tylko ID zastępcze z „nn”"
                          for x in rx.finditer(line)
                          if code not in areas or x.group(0).split("-")[0] in areas[code]]
            for term, rx in term_res:
                if rx.search(line):
                    found.append(f"{rel}:{lineno}: pojęcie projektu „{term}” ze słownika {glossary}")
        if found and rel in allow:
            used.add(rel)
            continue
        errors += found
    for rel, (n, reason) in sorted(allow.items()):
        if not reason:
            errors.append(f"tools/check_leak.allow:{n}: wyjątek „{rel}” bez powodu")
        elif rel not in used and (not argv or any(rel == a or rel.startswith(a.rstrip("/") + "/") for a in argv)):
            errors.append(f"tools/check_leak.allow:{n}: zbędny wyjątek „{rel}”")
    for e in errors:
        print(e)
    print(f"check_leak: {len(errors)} błędów, wyjątków użytych {len(used)}" + (f", pojęć ze słownika {len(terms)}" if glossary else ""))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
