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

SLOWA_EARS = {"When", "While", "If", "Where", "Then", "The", "A", "An", "Each", "Every"}


def wzorzec_ears(system):
    return {
        "ubiquitous": lambda t: t.startswith(f"{system} shall"),
        "event": lambda t: t.startswith("When "),
        "state": lambda t: t.startswith("While "),
        "unwanted": lambda t: t.startswith("If ") and ", then " in t,
        "optional": lambda t: t.startswith("Where "),
        "complex": lambda t: t.startswith("While ") and " when " in t,
    }


def pojecia(m):
    """Angielskie nazwy pojęć ze słownika: nawias na końcu tytułu, synonimy po średniku."""
    zbior = set()
    for e in m.elementy:
        if not m.typy[e.typ].get("terms"):
            continue
        n = re.search(r"\(([^()]*)\)\s*$", e.tytul)
        if n:
            for p in n.group(1).split(";"):
                if p.strip():
                    zbior.add(p.strip().lower())
    return zbior


def nieznane_pojecia(tekst, znane, system):
    bez_cytatow = re.sub(r'"[^"]*"|“[^”]*”|„[^”]*”', " ", tekst)
    bez_cytatow = bez_cytatow.replace(system, " ")
    brak = []
    for ciag in re.findall(r"[A-Z][\w/'-]*(?:\s+[A-Z][\w/'-]*)*", bez_cytatow):
        slowa = ciag.split()
        i = 0
        while i < len(slowa):
            if slowa[i] in SLOWA_EARS:
                i += 1
                continue
            dopas = 0
            for j in range(len(slowa), i, -1):
                fraza = " ".join(slowa[i:j]).lower()
                if fraza in znane or (fraza.endswith("s") and fraza[:-1] in znane):
                    dopas = j
                    break
            if dopas:
                i = dopas
            else:
                brak.append(slowa[i])
                i += 1
    return brak


def wzmianki_w_commitach(m):
    try:
        log = subprocess.run(["git", "log", "--format=%B"], cwd=m.korzen,
                             capture_output=True, text=True, check=True).stdout
    except Exception:
        return set()
    return set(m.ids_w(log))


def main(wyjscie):
    m = M.Model()
    bledy, ostrz, ekran = [], [], []
    typy, po_id = m.typy, m.po_id
    rodzice_el = defaultdict(list)
    dzieci = defaultdict(list)
    znane_poj = pojecia(m)
    ears = wzorzec_ears(m.system)
    f_status, f_result = m.pole.get("status", "status"), m.pole.get("result", "result")

    for e, pierwszy in m.duplikaty:
        bledy.append(f"E3 {e.id}: zdublowane ID ({m.wzgledna(e.plik)}:{e.linia} i {m.wzgledna(pierwszy.plik)}:{pierwszy.linia})")

    for e in m.elementy:
        t = typy[e.typ]
        for pole in t.get("required", []):
            if not e.pola.get(pole):
                bledy.append(f"E1 {e.id}: brak pola „{pole}”")
        for pole in sorted(set(e.pola) - t["znane"]):
            ostrz.append(f"W4 {e.id}: nieznane pole „{pole}” (znane: {', '.join(sorted(t['znane']))})")
        if t.get("statuses") and e.pola.get(f_status) and e.pola[f_status] not in t["statuses"]:
            bledy.append(f"E4 {e.id}: status „{e.pola[f_status]}” spoza {t['statuses']}")
        if t.get("results") and e.pola.get(f_result) and e.pola[f_result] not in t["results"]:
            bledy.append(f"E4 {e.id}: result „{e.pola[f_result]}” spoza {t['results']}")
        if t.get("produces"):
            for x in m.produkty(e)[1]:
                bledy.append(f"E4 {e.id}: „{x}” w produces: nie jest kodem typu ani ID")
        pola = t.get("fields", [])
        if pola:
            ids = []
            for p in pola:
                ids += m.ids_w(e.pola.get(p, ""))
            if not ids and not t.get("root"):
                bledy.append(f"E1 {e.id}: brak rodzica (pola: {', '.join(pola)})")
            for r in ids:
                if r not in po_id:
                    bledy.append(f"E2 {e.id}: nieznany rodzic {r}")
                elif po_id[r].typ not in t.get("parents", []):
                    bledy.append(f"E7 {e.id}: rodzic {r} typu {po_id[r].typ} niedozwolony (dozwolone: {', '.join(t.get('parents', []))})")
                else:
                    rodzice_el[e.id].append(r)
                    dzieci[r].append(e.id)
        tekst, wz = m.p(e, "text"), m.p(e, "pattern")
        if t.get("ears") and tekst and wz:
            if wz not in ears:
                bledy.append(f"E4 {e.id}: nieznany wzorzec EARS „{wz}”")
            elif not ears[wz](tekst):
                bledy.append(f"E5 {e.id}: tekst nie pasuje do wzorca {wz}")
            if tekst.count(" shall ") != 1:
                bledy.append(f"E5 {e.id}: tekst musi mieć dokładnie jedno „shall”")
            if not tekst.startswith(m.system) and f" {m.system} shall" not in tekst:
                bledy.append(f"E5 {e.id}: podmiotem „shall” musi być {m.system}")
            brak = nieznane_pojecia(tekst, znane_poj, m.system)
            if brak:
                bledy.append(f"E6 {e.id}: pojęcia spoza słownika: {', '.join(sorted(set(brak)))}")

    for p in m.pliki_aktywne():
        for nr, l in M._linie_bez_kodu(p):
            for ref in m.ids_w(l):
                if ref not in po_id:
                    bledy.append(f"E2 {m.wzgledna(p)}:{nr}: nieznany odnośnik {ref}")

    commity = None
    for e in m.elementy:
        t = typy[e.typ]
        if not t.get("coverage"):
            continue
        war = t.get("coverage_if")
        if war:
            pole, wart = war.split("=", 1)
            if e.pola.get(pole.strip()) != wart.strip():
                continue
        for regula in t["coverage"].split(","):
            kod, poziom = [x.strip() for x in regula.split(":")]
            if kod == "*":
                if dzieci.get(e.id):
                    continue
                if commity is None:
                    commity = wzmianki_w_commitach(m)
                if e.id not in commity:
                    ekran.append(f"W2 {e.id}: brak dzieci i wzmianki w commitach")
                continue
            if kod not in typy or not typy[kod]["aktywny"]:
                continue
            if not any(po_id[c].typ == kod for c in dzieci.get(e.id, [])):
                wpis = f"{e.id}: brak dzieci typu {kod} ({typy[kod]['name']})"
                if poziom == "error":
                    bledy.append("E8 " + wpis)
                else:
                    ostrz.append("W1 " + wpis)

    if "VER" in typy and typy["VER"]["aktywny"] and len(m.stany) > 1:
        for e in m.elementy:
            if typy[e.typ].get("product") and m.stan(e) in m.stany[1:]:
                if not any(po_id[c].typ == "VER" and m.p(po_id[c], "result") == "pass" for c in dzieci.get(e.id, [])):
                    ostrz.append(f"W3 {e.id}: stan „{m.stan(e)}” bez weryfikacji VER z wynikiem „pass”")

    aktywne = [k for k, t in typy.items() if t["aktywny"]]
    liczby = " · ".join(f"{k} {sum(1 for e in m.elementy if e.typ == k)}" for k in aktywne)
    out = ["# Macierz śladu", "",
           "Plik generowany przez tools/trace.py według tools/id.toml; nie edytuj ręcznie (P-04).", "",
           f"Elementy: {liczby or 'brak'}", "",
           f"Błędy: {len(bledy)} · ostrzeżenia: {len(ostrz)}", "",
           "## W górę: element → rodzice", "",
           "| Element | Typ | Rodzice |", "| --- | --- | --- |"]
    for e in m.elementy:
        if typy[e.typ].get("fields"):
            out.append(f"| {e.id} | {e.typ} | {', '.join(rodzice_el.get(e.id, [])) or '—'} |")
    out += ["", "## W dół: element → dzieci", "", "| Element | Typ | Dzieci |", "| --- | --- | --- |"]
    for e in m.elementy:
        if dzieci.get(e.id) or typy[e.typ].get("coverage"):
            out.append(f"| {e.id} | {e.typ} | {', '.join(dzieci.get(e.id, [])) or '—'} |")
    zadania = [e for e in m.elementy if typy[e.typ].get("produces")]
    if zadania:
        out += ["", "## Plan → produkty (produces:, wyjątek od P-03)", "",
                "| Zadanie | Produkuje | Elementy |", "| --- | --- | --- |"]
        for e in zadania:
            el = m.produkty(e)[0]
            out.append(f"| {e.id} | {m.p(e, 'produces')} | {', '.join(x.id for x in el) or '—'} |")
    out += ["", "## Produkty pracy ISO/IEC 29110-5-1-2", "", "| Produkt | Typ | Elementy |", "| --- | --- | --- |"]
    for k, t in typy.items():
        if t.get("iso"):
            ile = sum(1 for e in m.elementy if e.typ == k) if t["aktywny"] else "nieaktywny"
            out.append(f"| {t['iso']} | {k} {t['name']} | {ile} |")
    for w in m.iso_inne:
        wp, _, gdzie = w.partition(" ")
        out.append(f"| {wp} | {gdzie} | — |")
    if bledy or ostrz:
        out += ["", "## Błędy i ostrzeżenia", ""] + [f"- {x}" for x in bledy + ostrz]
    with open(os.path.join(m.korzen, wyjscie) if not os.path.isabs(wyjscie) else wyjscie, "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")

    for x in bledy + ostrz + ekran:
        print(x)
    print(f"trace.py: {len(m.elementy)} elementów, {len(bledy)} błędów, {len(ostrz) + len(ekran)} ostrzeżeń")
    return 1 if bledy else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "trace.md"))
