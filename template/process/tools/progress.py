"""Rekord postępu (szablon D-10; ISO/IEC 29110-5-1-2 WP.09, zadanie PM.03.01).

Generuje reports/progress.md z project/plan.md (OBJ, MS, TSK, PRK), rekordów (COR, ACC), stanów
produktów pracy i tagów git. Plik jest deterministyczny: nie zależy od dzisiejszej
daty, tylko od repozytorium, więc pre-commit może sprawdzać jego aktualność.
Planowane i rzeczywiste: pole due a pole completed zadania, due kamienia
a data jego tagu baseline.

Kryteria odbioru kamieni i zadań (pole acceptance_criteria) pokazuje osobna sekcja, tylko gdy są (szablon D-73).

Użycie: python3 process/tools/progress.py [plik_wyjściowy=reports/progress.md]
"""
import os
import subprocess
import sys
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import model as M  # noqa: E402


def tags(root):
    try:
        out = subprocess.run(["git", "for-each-ref", "--format=%(refname:short) %(creatordate:short)", "refs/tags"],
                             cwd=root, capture_output=True, text=True, check=True).stdout
    except Exception:
        return {}
    return dict(l.split(" ", 1) for l in out.splitlines() if " " in l)


def main(output):
    m = M.Model()
    if not m.types.get("TSK", {}).get("active"):
        print("progress.py: brak project/plan.md, pomijam")
        return 0
    of_type = lambda code: [e for e in m.elements if e.type == code]  # noqa: E731
    v = lambda e, *role: [m.value(e, r) or "—" for r in role]  # noqa: E731
    t = tags(m.root)
    acceptances = {}
    for a in of_type("ACC"):
        for k in m.ids_in(m.value(a, "milestone")):
            acceptances.setdefault(k, []).append(f"{a.id} {m.value(a, 'result')}")

    out = ["# Rekord postępu", "",
           "Plik generowany przez process/tools/progress.py z project/plan.md, rekordów, stanów produktów i tagów git; "
           "nie edytuj ręcznie (ISO/IEC 29110 WP.09).", ""]

    tasks = of_type("TSK")
    counts = Counter(m.value(e, "status") for e in tasks)
    out += [f"Zadania: {len(tasks)} · " + " · ".join(f"{s} {counts.get(s, 0)}" for s in m.types["TSK"]["statuses"]), ""]

    out += ["## Kamienie milowe", "", "| Kamień | Cel | Termin | Tag | Osiągnięty | Akceptacja |",
            "| --- | --- | --- | --- | --- | --- |"]
    for e in of_type("MS"):
        tag = m.value(e, "tag")
        reached = f"tak, {t[tag]}" if tag in t else "nie"
        objective, due = v(e, "objective", "due")
        out.append(f"| {e.id} {e.title} | {objective} | {due} | {tag or '—'} | {reached} | {', '.join(acceptances.get(e.id, [])) or '—'} |")

    out += ["", "## Zadania: planowane i rzeczywiste", "",
            "| Zadanie | Kamień | Status | Termin | Zakończono | Produkuje | Produkty według stanu |",
            "| --- | --- | --- | --- | --- | --- | --- |"]
    for e in tasks:
        elem = m.products(e)[0]
        state_counts = Counter(m.state(x) for x in elem)
        state_summary = " · ".join(f"{s} {state_counts[s]}" for s in m.states if state_counts.get(s)) or "brak elementów"
        ms, status, due, done, prods = v(e, "milestone", "status", "due", "completed", "produces")
        out.append(f"| {e.id} {e.title} | {ms} | {status} | {due} | {done} | {prods} | {state_summary} |")

    out += ["", "## Ryzyka projektu", "", "| Ryzyko | Status | Dotyczy | Działanie |", "| --- | --- | --- | --- |"]
    for e in of_type("PRK"):
        out.append(f"| {e.id} {e.title} | " + " | ".join(v(e, "status", "concerns", "mitigation")) + " |")

    open_corrections = [e for e in of_type("COR") if m.value(e, "status") != "completed"]
    out += ["", "## Korekty niezakończone (WP.04)", "", "| Korekta | Status | Przyczyna | Działanie |",
            "| --- | --- | --- | --- |"]
    for e in open_corrections:
        out.append(f"| {e.id} {e.title} | " + " | ".join(v(e, "status", "cause", "action")) + " |")

    out += ["", "## Stan produktów pracy", "", "| Typ | ISO | " + " | ".join(m.states) + " |",
            "| --- | --- | " + " | ".join("---" for _ in m.states) + " |"]
    for k, type_def in m.types.items():
        if type_def.get("product") and type_def["active"]:
            state_counts = Counter(m.state(e) for e in of_type(k))
            out.append(f"| {k} {type_def['name']} | {type_def.get('iso', '—')} | " + " | ".join(str(state_counts.get(s, 0)) for s in m.states) + " |")

    criteria = [e for e in of_type("MS") + tasks if m.value(e, "acceptance_criteria")]
    if criteria:  # szablon D-73: sekcja tylko wtedy, gdy kryteria są
        out += ["", "## Kryteria odbioru", "", "| Element | Kryteria |", "| --- | --- |"]
        for e in criteria:
            out.append(f"| {e.id} {e.title} | {m.value(e, 'acceptance_criteria')} |")
    fpath = M.output_path(m.root, output)
    with open(fpath, "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")
    print(f"progress.py: {len(tasks)} zadań, {len(of_type('MS'))} kamieni, {len(open_corrections)} korekt niezakończonych")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else os.path.join("reports", "progress.md")))
