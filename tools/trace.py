"""Ślad dwukierunkowy według modelu tools/id.toml (AGENTS.md, P-03…P-06).

Generuje trace.md (macierz w obie strony) i sprawdza model. Kod wyjścia 1 = błędy.

Błędy (error):
  E1 brak wymaganego pola albo rodzica       E5 tekst niezgodny ze wzorcem EARS / nie jedno „shall”
  E2 nieznane ID (w polu rodzica lub tekście) E6 pojęcie spoza słownika w tekście EARS
  E3 zdublowane ID                            E7 rodzic niedozwolonego typu
  E4 niedozwolona wartość (status, result,    E8 brak wymaganego pokrycia (poziom „error”)
     pattern, wpis w produces:)
Ostrzeżenia (warning):
  W1 brak oczekiwanego pokrycia (poziom „warning”)
  W2 rozstrzygnięta decyzja bez dzieci i bez wzmianki w commitach (tylko na ekranie)
  W3 produkt w stanie verified/approved bez weryfikacji VER z wynikiem „pass” (D-11, D-15)
  W4 pole spoza znanych pól typu, np. dawna polska nazwa (D-21)

Użycie: python3 tools/trace.py [plik_wyjściowy=trace.md]
"""
import os
import re
import subprocess
import sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import model as M  # noqa: E402

EARS_WORDS = {"When", "While", "If", "Where", "Then", "The", "A", "An", "Each", "Every"}


def ears_checks(system):
    return {
        "ubiquitous": lambda t: t.startswith(f"{system} shall"),
        "event": lambda t: t.startswith("When "),
        "state": lambda t: t.startswith("While "),
        "unwanted": lambda t: t.startswith("If ") and ", then " in t,
        "optional": lambda t: t.startswith("Where "),
        "complex": lambda t: t.startswith("While ") and " when " in t,
    }


def term_names(m):
    """Angielskie nazwy pojęć ze słownika: nawias na końcu tytułu, synonimy po średniku."""
    names = set()
    for e in m.elements:
        if not m.types[e.type].get("terms"):
            continue
        n = re.search(r"\(([^()]*)\)\s*$", e.title)
        if n:
            for p in n.group(1).split(";"):
                if p.strip():
                    names.add(p.strip().lower())
    return names


def unknown_terms(content, known, system):
    unquoted = re.sub(r'"[^"]*"|“[^”]*”|„[^”]*”', " ", content)
    unquoted = unquoted.replace(system, " ")
    missing = []
    for run_of_words in re.findall(r"[A-Z][\w/'-]*(?:\s+[A-Z][\w/'-]*)*", unquoted):
        words = run_of_words.split()
        i = 0
        while i < len(words):
            if words[i] in EARS_WORDS:
                i += 1
                continue
            matched_end = 0
            for j in range(len(words), i, -1):
                phrase = " ".join(words[i:j]).lower()
                if phrase in known or (phrase.endswith("s") and phrase[:-1] in known):
                    matched_end = j
                    break
            if matched_end:
                i = matched_end
            else:
                missing.append(words[i])
                i += 1
    return missing


def ids_in_commits(m):
    try:
        log = subprocess.run(["git", "log", "--format=%B"], cwd=m.root,
                             capture_output=True, text=True, check=True).stdout
    except Exception:
        return set()
    return set(m.ids_in(log))


def main(output):
    m = M.Model()
    errors, warnings, screen_only = [], [], []
    types, by_id = m.types, m.by_id
    parents_of = defaultdict(list)
    children = defaultdict(list)
    known_terms = term_names(m)
    ears = ears_checks(m.system)
    f_status, f_result = m.field_names.get("status", "status"), m.field_names.get("result", "result")

    for e, first in m.duplicates:
        errors.append(f"E3 {e.id}: zdublowane ID ({m.relative(e.file)}:{e.lineno} i {m.relative(first.file)}:{first.lineno})")

    for e in m.elements:
        t = types[e.type]
        for field in t.get("required", []):
            if not e.fields.get(field):
                errors.append(f"E1 {e.id}: brak pola „{field}”")
        for field in sorted(set(e.fields) - t["known"]):
            warnings.append(f"W4 {e.id}: nieznane pole „{field}” (znane: {', '.join(sorted(t['known']))})")
        if t.get("statuses") and e.fields.get(f_status) and e.fields[f_status] not in t["statuses"]:
            errors.append(f"E4 {e.id}: status „{e.fields[f_status]}” spoza {t['statuses']}")
        if t.get("results") and e.fields.get(f_result) and e.fields[f_result] not in t["results"]:
            errors.append(f"E4 {e.id}: result „{e.fields[f_result]}” spoza {t['results']}")
        if t.get("produces"):
            for x in m.products(e)[1]:
                errors.append(f"E4 {e.id}: „{x}” w produces: nie jest kodem typu ani ID")
        fields = t.get("fields", [])
        if fields:
            ids = []
            for p in fields:
                ids += m.ids_in(e.fields.get(p, ""))
            if not ids and not t.get("root"):
                errors.append(f"E1 {e.id}: brak rodzica (pola: {', '.join(fields)})")
            for r in ids:
                if r not in by_id:
                    errors.append(f"E2 {e.id}: nieznany rodzic {r}")
                elif by_id[r].type not in t.get("parents", []):
                    errors.append(f"E7 {e.id}: rodzic {r} typu {by_id[r].type} niedozwolony (dozwolone: {', '.join(t.get('parents', []))})")
                else:
                    parents_of[e.id].append(r)
                    children[r].append(e.id)
        content, pattern_name = m.value(e, "text"), m.value(e, "pattern")
        if t.get("ears") and content and pattern_name:
            if pattern_name not in ears:
                errors.append(f"E4 {e.id}: nieznany wzorzec EARS „{pattern_name}”")
            elif not ears[pattern_name](content):
                errors.append(f"E5 {e.id}: tekst nie pasuje do wzorca {pattern_name}")
            if content.count(" shall ") != 1:
                errors.append(f"E5 {e.id}: tekst musi mieć dokładnie jedno „shall”")
            if not content.startswith(m.system) and f" {m.system} shall" not in content:
                errors.append(f"E5 {e.id}: podmiotem „shall” musi być {m.system}")
            missing = unknown_terms(content, known_terms, m.system)
            if missing:
                errors.append(f"E6 {e.id}: pojęcia spoza słownika: {', '.join(sorted(set(missing)))}")

    for p in m.active_files():
        for lineno, l in M._lines_outside_code(p):
            for ref in m.ids_in(l):
                if ref not in by_id:
                    errors.append(f"E2 {m.relative(p)}:{lineno}: nieznany odnośnik {ref}")

    commit_ids = None
    for e in m.elements:
        t = types[e.type]
        if not t.get("coverage"):
            continue
        condition = t.get("coverage_if")
        if condition:
            field, expected_value = condition.split("=", 1)
            if e.fields.get(field.strip()) != expected_value.strip():
                continue
        for rule in t["coverage"].split(","):
            code, level = [x.strip() for x in rule.split(":")]
            if code == "*":
                if children.get(e.id):
                    continue
                if commit_ids is None:
                    commit_ids = ids_in_commits(m)
                if e.id not in commit_ids:
                    screen_only.append(f"W2 {e.id}: brak dzieci i wzmianki w commitach")
                continue
            if code not in types or not types[code]["active"]:
                continue
            if not any(by_id[c].type == code for c in children.get(e.id, [])):
                entry = f"{e.id}: brak dzieci typu {code} ({types[code]['name']})"
                if level == "error":
                    errors.append("E8 " + entry)
                else:
                    warnings.append("W1 " + entry)

    if "VER" in types and types["VER"]["active"] and len(m.states) > 1:
        for e in m.elements:
            if types[e.type].get("product") and m.state(e) in m.states[1:]:
                if not any(by_id[c].type == "VER" and m.value(by_id[c], "result") == "pass" for c in children.get(e.id, [])):
                    warnings.append(f"W3 {e.id}: stan „{m.state(e)}” bez weryfikacji VER z wynikiem „pass”")

    active_types = [k for k, t in types.items() if t["active"]]
    counts_line = " · ".join(f"{k} {sum(1 for e in m.elements if e.type == k)}" for k in active_types)
    out = ["# Macierz śladu", "",
           "Plik generowany przez tools/trace.py według tools/id.toml; nie edytuj ręcznie (P-04).", "",
           f"Elementy: {counts_line or 'brak'}", "",
           f"Błędy: {len(errors)} · ostrzeżenia: {len(warnings)}", "",
           "## W górę: element → rodzice", "",
           "| Element | Typ | Rodzice |", "| --- | --- | --- |"]
    for e in m.elements:
        if types[e.type].get("fields"):
            out.append(f"| {e.id} | {e.type} | {', '.join(parents_of.get(e.id, [])) or '—'} |")
    out += ["", "## W dół: element → dzieci", "", "| Element | Typ | Dzieci |", "| --- | --- | --- |"]
    for e in m.elements:
        if children.get(e.id) or types[e.type].get("coverage"):
            out.append(f"| {e.id} | {e.type} | {', '.join(children.get(e.id, [])) or '—'} |")
    task_elems = [e for e in m.elements if types[e.type].get("produces")]
    if task_elems:
        out += ["", "## Plan → produkty (produces:, wyjątek od P-03)", "",
                "| Zadanie | Produkuje | Elementy |", "| --- | --- | --- |"]
        for e in task_elems:
            elem = m.products(e)[0]
            out.append(f"| {e.id} | {m.value(e, 'produces')} | {', '.join(x.id for x in elem) or '—'} |")
    out += ["", "## Produkty pracy ISO/IEC 29110-5-1-2", "", "| Produkt | Typ | Elementy |", "| --- | --- | --- |"]
    for k, t in types.items():
        if t.get("iso"):
            n_elems = sum(1 for e in m.elements if e.type == k) if t["active"] else "nieaktywny"
            out.append(f"| {t['iso']} | {k} {t['name']} | {n_elems} |")
    for w in m.iso_other:
        wp, _, where = w.partition(" ")
        out.append(f"| {wp} | {where} | — |")
    if errors or warnings:
        out += ["", "## Błędy i ostrzeżenia", ""] + [f"- {x}" for x in errors + warnings]
    with open(os.path.join(m.root, output) if not os.path.isabs(output) else output, "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")

    for x in errors + warnings + screen_only:
        print(x)
    print(f"trace.py: {len(m.elements)} elementów, {len(errors)} błędów, {len(warnings) + len(screen_only)} ostrzeżeń")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "trace.md"))
