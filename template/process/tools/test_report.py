"""Raport testów (ISO/IEC 29110 WP.20, szablon D-60): testy akceptacyjne z polem runner: i ich wyniki.

Zbiera testy AT z polem `runner: plik::przypadek[, plik::przypadek…]`, uruchamia każdy wskazany plik
raz i czyta z jego wyjścia wiersze `CASE <przypadek>: pass|fail`. Test AT przechodzi tylko wtedy,
gdy przeszły wszystkie jego przypadki. Przypadek, którego plik nie wypisał, jest porażką
(„brak przypadku”); plik zakończony kodem 2 to „nie uruchomiono” (np. brak copiera), nie sukces.
Testy AT bez runner: są ręczne: raport je wypisuje, ale ich nie ocenia.

Użycie: python3 process/tools/test_report.py [plik_wyjściowy=reports/test-report.md] [--root KATALOG] [--scripts-root KATALOG]
        --root: skąd czytać artefakty; --scripts-root: gdzie uruchamiać testy (domyślnie to samo)
Kod wyjścia: 0 wszystkie testy automatyczne przeszły, 1 nie.
"""
import datetime
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import model as M  # noqa: E402

CASE_RE = re.compile(r"^CASE (\S+): (pass|fail)$", re.M)


def run_script(root, path):
    r = subprocess.run([sys.executable, "-B", path], cwd=root, capture_output=True, text=True)
    return r.returncode, dict(CASE_RE.findall(r.stdout)), r.stdout + r.stderr


def main(argv):
    opts = {}
    for name in ("--root", "--scripts-root"):
        if name in argv:
            i = argv.index(name)
            opts[name] = os.path.abspath(argv[i + 1])
            argv = argv[:i] + argv[i + 2:]
    root = opts.get("--root", M.ROOT)
    scripts_root = opts.get("--scripts-root", root)
    output = argv[0] if argv else os.path.join("reports", "test-report.md")
    m = M.Model(root)
    tests = [e for e in m.elements if e.type == "AT"]
    scripts = {}
    for e in tests:
        for x in [w.strip() for w in m.value(e, "runner").split(",") if w.strip()]:
            scripts.setdefault(x.partition("::")[0], None)
    for path in scripts:
        if not os.path.isfile(os.path.join(scripts_root, path)):
            scripts[path] = (None, {}, f"brak pliku {path}")
            continue
        print(f"test_report: uruchamiam {path}")
        scripts[path] = run_script(scripts_root, path)

    rows, failed, manual = [], 0, 0
    for e in tests:
        runners = [w.strip() for w in m.value(e, "runner").split(",") if w.strip()]
        verifies = m.value(e, "verifies") or "—"
        if not runners:
            manual += 1
            rows.append((e.id, verifies, "ręczny", "—"))
            continue
        problems, statuses = [], []
        for x in runners:
            path, _, case = x.partition("::")
            rc, cases, _ = scripts[path]
            if rc is None:
                problems.append(f"{x}: brak pliku")
            elif rc == 2 and case not in cases:
                problems.append(f"{x}: nie uruchomiono")
            elif case not in cases:
                problems.append(f"{x}: brak przypadku")
            elif cases[case] != "pass":
                problems.append(f"{x}: fail")
            statuses.append(x)
        if problems:
            failed += 1
        rows.append((e.id, verifies, "fail" if problems else "pass", "; ".join(problems) or ", ".join(statuses)))

    head = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=scripts_root, capture_output=True, text=True).stdout.strip()
    dirty = subprocess.run(["git", "status", "--porcelain"], cwd=scripts_root, capture_output=True, text=True).stdout.strip()
    lines = ["# Raport testów", "",
             "Plik generowany przez tools/test_report.py (ISO/IEC 29110 WP.20, szablon D-60); nie edytuj ręcznie.", "",
             f"Data: {datetime.date.today().isoformat()} · commit: {head or '—'}{' (z niezacommitowanymi zmianami)' if dirty else ''}"
             f" · Python {sys.version.split()[0]}", "",
             f"Testy automatyczne: {len(tests) - manual} · przeszły: {len(tests) - manual - failed} · nie przeszły: {failed} · ręczne: {manual}", "",
             "| Test | Weryfikuje | Wynik | Przypadki albo problem |", "| --- | --- | --- | --- |"]
    lines += [f"| {a} | {b} | {c} | {d} |" for a, b, c, d in rows]
    lines += ["", "## Przebiegi", "", "| Plik | Kod wyjścia | Przypadki pass | Przypadki fail |", "| --- | --- | --- | --- |"]
    for path, (rc, cases, _) in sorted(scripts.items()):
        lines.append(f"| {path} | {'—' if rc is None else rc} | {sum(1 for v in cases.values() if v == 'pass')} | "
                     f"{sum(1 for v in cases.values() if v != 'pass')} |")
    with open(M.output_path(root, output), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(f"test_report: {len(tests)} testów AT, automatycznych {len(tests) - manual}, nie przeszło {failed}, ręcznych {manual} → {output}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
