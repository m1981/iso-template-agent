"""Ślad dwukierunkowy według modelu tools/id.toml (AGENTS.md, P-03…P-06).

Generuje trace.md (macierz w obie strony) i sprawdza model. Kod wyjścia 1 = błędy.

Błędy (error):
  E1 brak wymaganego pola albo rodzica       E5 tekst niezgodny ze wzorcem EARS / nie jedno „shall”
  E2 nieznane ID (w polu rodzica lub tekście) E6 pojęcie spoza słownika w tekście EARS
  E3 zdublowane ID                            E7 rodzic niedozwolonego typu albo niezgodny z parent_rules
  E4 niedozwolona wartość (status, result,    E8 brak wymaganego pokrycia (poziom „error”)
     pattern, wpis w produces:)
Ostrzeżenia (warning):
  W1 brak oczekiwanego pokrycia (poziom „warning”)
  W2 rozstrzygnięta decyzja bez dzieci i bez wzmianki w commitach (tylko na ekranie)
  W3 produkt w stanie verified/approved bez weryfikacji VER z wynikiem „pass” (D-11, D-15)
  W4 pole spoza znanych pól typu, np. dawna polska nazwa (D-21)
  W5 element albo jego rodzic zmienił się po ostatniej weryfikacji VER z wynikiem „pass” (D-32;
     tylko na ekranie, bo zależy od historii gita)

Użycie: python3 tools/trace.py [plik_wyjściowy=trace.md]
"""
import io
import os
import re
import shutil
import subprocess
import sys
import tarfile
import tempfile
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


def fingerprint(e):
    """Treść elementu bez pola status (zmiana stanu nie jest zmianą treści)."""
    return (e.title, tuple(sorted((k, v) for k, v in e.fields.items() if k != "status")))


def impact(m, parents_of):
    """D-32: dla każdego elementu z rekordem VER „pass” porównuje jego treść i treść jego rodziców
    z wersją z commita, który dodał rekord. Zwraca ostrzeżenia W5. Bez gita: brak ostrzeżeń."""
    def git(*args):
        return subprocess.run(["git", *args], cwd=m.root, capture_output=True)
    if git("rev-parse", "--is-inside-work-tree").returncode != 0:
        return []
    latest = {}  # element → (głębokość commita, VER, commit)
    for v in m.elements:
        if v.type != "VER" or m.value(v, "result") != "pass":
            continue
        log = git("log", "--reverse", "--format=%H", f"-S{v.id}", "--", m.relative(v.file))
        commits = log.stdout.decode().split()
        if not commits:
            continue  # rekord jeszcze niezacommitowany
        commit = commits[0]
        depth = int(git("rev-list", "--count", commit).stdout.decode().strip() or 0)
        for item in m.ids_in(v.fields.get("items", "")):
            if item in m.by_id and (item not in latest or depth >= latest[item][0]):
                latest[item] = (depth, v.id, commit)
    if not latest:
        return []
    old_models, found = {}, []
    tmp = tempfile.mkdtemp()
    try:
        for item, (_, ver, commit) in sorted(latest.items()):
            if commit not in old_models:
                d = os.path.join(tmp, commit)
                archive = git("archive", "--format=tar", commit)
                with tarfile.open(fileobj=io.BytesIO(archive.stdout)) as t:
                    try:
                        t.extractall(d, filter="data")  # Python 3.8.17+, 3.10.12+, 3.11.4+
                    except TypeError:
                        t.extractall(d)
                os.makedirs(os.path.join(d, "tools"), exist_ok=True)
                shutil.copy(os.path.join(m.root, "tools", "id.toml"), os.path.join(d, "tools", "id.toml"))
                old_models[commit] = M.Model(d).by_id
            old = old_models[commit]
            for ident in [item] + parents_of.get(item, []):
                if ident in old and fingerprint(old[ident]) != fingerprint(m.by_id[ident]):
                    who = "zmienił się" if ident == item else f"rodzic {ident} zmienił się"
                    found.append(f"W5 {item}: {who} po weryfikacji {ver}; przejrzyj {item} i zapisz nowy rekord VER")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    return found


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
        if t.get("qualities"):
            for q in [x.strip() for x in m.value(e, "quality").split(",") if x.strip()]:
                if q not in t["qualities"]:
                    errors.append(f"E4 {e.id}: quality „{q}” spoza {t['qualities']}")
        lists = [x.strip() for x in m.value(e, "checklist").split(",") if x.strip()]
        failed = [x.strip() for x in m.value(e, "failed").split(",") if x.strip()]
        for x in lists:
            if x not in m.checklist:
                errors.append(f"E4 {e.id}: lista „{x}” nie istnieje w checklist.md")
        known_items = set().union(*m.checklist.values()) if m.checklist else set()
        for x in failed:
            if x not in known_items:
                errors.append(f"E4 {e.id}: punkt „{x}” nie istnieje w checklist.md")
            elif lists and x.split(".")[0] not in lists:
                errors.append(f"E4 {e.id}: punkt „{x}” spoza wskazanych list ({', '.join(lists)})")
        if failed and m.value(e, "result") == "pass":
            errors.append(f"E4 {e.id}: wynik „pass”, a niespełnione punkty: {', '.join(failed)}")
        if t.get("produces"):
            for x in m.products(e)[1]:
                errors.append(f"E4 {e.id}: „{x}” w produces: nie jest kodem typu ani ID")
        fields = t.get("fields", [])
        if fields:
            refs = [(p, r) for p in fields for r in m.ids_in(e.fields.get(p, ""))]
            root_if = t.get("root_if", "=").split("=", 1)
            if not refs and not t.get("root") and e.fields.get(root_if[0]) != root_if[1]:
                errors.append(f"E1 {e.id}: brak rodzica (pola: {', '.join(fields)})")
            for p, r in refs:
                rule = t["rules"].get(p)
                if r not in by_id:
                    errors.append(f"E2 {e.id}: nieznany rodzic {r}")
                elif by_id[r].type not in t.get("parents", []):
                    errors.append(f"E7 {e.id}: rodzic {r} typu {by_id[r].type} niedozwolony (dozwolone: {', '.join(t.get('parents', []))})")
                elif rule and by_id[r].type not in rule[0]:
                    errors.append(f"E7 {e.id}: pole „{p}” wskazuje {r} typu {by_id[r].type}; dozwolone tu: {', '.join(rule[0])}")
                elif rule and rule[1] and by_id[r].fields.get(rule[1][0]) != rule[1][1]:
                    k, v = rule[1]
                    errors.append(f"E7 {e.id}: pole „{p}” wymaga rodzica z {k}={v}, a {r} ma {k}={by_id[r].fields.get(k) or 'brak'}")
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

    areas = {k: {e.id.split("-")[0] for e in m.elements if e.type == k}
             for k, t in types.items() if t.get("area_prefix")}
    bad = {(p, lineno): ident for p, lineno, ident in m.bad_headings}
    for p, lineno, ident in m.bad_headings:
        errors.append(f"E2 {m.relative(p)}:{lineno}: po ID w nagłówku stoi dwukropek („{ident}:”); zapisz „### {ident} Tytuł”")
    for p in m.active_files():
        for lineno, l in M._lines_outside_code(p):
            for ref in m.ids_in(l):
                if ref in by_id or bad.get((p, lineno)) == ref:
                    continue
                area_type = next((k for k in areas if types[k]["re"].fullmatch(ref)), None)
                if area_type and ref.split("-")[0] not in areas[area_type]:
                    continue  # np. „UTF-16”: kształt ID wymagania, ale obszar nie istnieje
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
    for k, t in types.items():
        if t.get("qualities") and t["active"]:
            out += ["", f"## Charakterystyki jakości ({k}, WP.13)", "",
                    "Wymagania niefunkcjonalne według charakterystyk; 0 to pytanie, czy czegoś nie pominięto.", "",
                    "| Charakterystyka | Liczba | Wymagania |", "| --- | --- | --- |"]
            for q in t["qualities"]:
                ids = [e.id for e in m.elements if e.type == k and q in [x.strip() for x in m.value(e, "quality").split(",")]]
                out.append(f"| {q} | {len(ids)} | {', '.join(ids) or '—'} |")
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

    screen_only += impact(m, parents_of)
    for x in errors + warnings + screen_only:
        print(x)
    print(f"trace.py: {len(m.elements)} elementów, {len(errors)} błędów, {len(warnings) + len(screen_only)} ostrzeżeń")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "trace.md"))
