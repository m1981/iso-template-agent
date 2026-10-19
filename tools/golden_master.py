"""Złoty wzorzec wyjść narzędzi (D-61): zapis przed przeniesieniem, porównanie po nim.

Buduje fixture z tools/test_tools.py (łańcuch wszystkich typów, moduły nawigacji i ryzyk) ze stałym
rejestrem z jedną decyzją D-01 (wzorzec nie zależy od rejestru szablonu) i zapisuje:
  reference/golden/chain/trace.md, reference/golden/chain/progress.md, reference/golden/chain/iso-map.html
      pliki generowane z łańcucha wzorcowego,
  reference/golden/chain/trace.out   wyjście trace.py na łańcuchu,
  breakage-NN.out, warning-NN.out    wyjście trace.py po każdym psuciu i ostrzeżeniu (w reference/golden/).
Porównanie buduje to samo i zgłasza każdą różnicę. Po przeniesieniu ścieżki plików w komunikatach się
zmieniają (np. spec/requirements.md zamiast requirements.md), więc --strip PREFIKS usuwa podane
katalogi z obu stron przed porównaniem; reszta musi być identyczna.

Użycie: python3 tools/golden_master.py snapshot reference/golden
        python3 tools/golden_master.py compare reference/golden [--strip spec/ --strip project/ ...]
Kod wyjścia: 0 zgodne (albo zapisane), 1 różnice.
"""
import difflib
import os
import re
import shutil
import sys
import tempfile

TOOLS_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, TOOLS_DIR)
import test_tools as T  # noqa: E402

GENERATED = ["trace.md", "progress.md", "iso-map.html"]
REGISTER = ("# Rejestr decyzji\n\n## Rozstrzygnięte\n\n### D-01 Start projektu\n- status: resolved\n"
            "- options: A) start\n- proposal: A\n- choice: A\n- date: 2026-10-19\n")


def produce():
    """{nazwa pliku wzorca: treść} dla bieżących narzędzi."""
    out = {}
    with tempfile.TemporaryDirectory() as tmpdir:
        T.prepare(tmpdir)
        # stały rejestr: wzorzec nie może zależeć od tego, ile decyzji ma rejestr szablonu
        open(os.path.join(tmpdir, "decisions.md"), "w", encoding="utf-8").write(REGISTER)
        r = T.run_py(tmpdir, "tools/trace.py")
        out["chain/trace.out"] = r.stdout + f"[kod {r.returncode}]\n"
        T.run_py(tmpdir, "tools/progress.py")
        T.run_py(tmpdir, "tools/iso_map.py")
        for name in GENERATED:
            out["chain/" + name] = open(os.path.join(tmpdir, name), encoding="utf-8").read()
        for kind, items in (("breakage", [(f, a, b) for _, f, a, b in T.BREAKAGES]),
                            ("warning", [(f, a, b) for _, f, a, b, _ in T.WARNINGS])):
            for i, (fname, a, b) in enumerate(items, 1):
                fpath = os.path.join(tmpdir, fname)
                original = open(fpath, encoding="utf-8").read()
                if a not in original:
                    raise SystemExit(f"golden_master: zasiew nieudany ({kind}-{i:02d}: brak tekstu w {fname})")
                open(fpath, "w", encoding="utf-8").write(original.replace(a, b, 1))
                r = T.run_py(tmpdir, "tools/trace.py", os.devnull)
                open(fpath, "w", encoding="utf-8").write(original)
                out[f"{kind}-{i:02d}.out"] = r.stdout + f"[kod {r.returncode}]\n"
    return out


def normalize(text, strips):
    for prefix in strips:
        text = re.sub(r"(?<![\w/.-])" + re.escape(prefix), "", text)
    return text


def main(argv):
    if len(argv) < 2 or argv[0] not in ("snapshot", "compare"):
        print(__doc__)
        return 2
    mode, target = argv[0], argv[1]
    strips = [argv[i + 1] for i, a in enumerate(argv) if a == "--strip"]
    current = produce()
    if mode == "snapshot":
        if os.path.exists(target):
            shutil.rmtree(target)
        for name, text in current.items():
            path = os.path.join(target, name)
            os.makedirs(os.path.dirname(path), exist_ok=True)
            open(path, "w", encoding="utf-8").write(text)
        print(f"golden_master: zapisano {len(current)} plików wzorca w {target}")
        return 0
    stored = {}
    for base, _, names in os.walk(target):
        for n in names:
            path = os.path.join(base, n)
            stored[os.path.relpath(path, target).replace(os.sep, "/")] = open(path, encoding="utf-8").read()
    diffs = []
    for name in sorted(set(stored) | set(current)):
        if name not in current or name not in stored:
            diffs.append(f"{name}: {'brak w bieżących wynikach' if name not in current else 'brak we wzorcu'}")
            continue
        a, b = normalize(stored[name], strips), normalize(current[name], strips)
        if a != b:
            diffs.append(name + ":\n" + "".join(difflib.unified_diff(a.splitlines(True), b.splitlines(True), "wzorzec", "teraz", n=1)))
    for d in diffs:
        print(d)
    print(f"golden_master: {len(stored)} plików wzorca, różnic {len(diffs)}")
    return 1 if diffs else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
