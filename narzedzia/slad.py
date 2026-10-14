"""Ślad dwukierunkowy według modelu narzedzia/id.toml (AGENTS.md, P-03…P-06).

Generuje slad.md (macierz w obie strony) i sprawdza model. Kod wyjścia 1 = błędy.

Błędy:
  B1 brak wymaganego pola albo rodzica      B5 tekst niezgodny ze wzorcem EARS / nie jedno „shall”
  B2 nieznane ID (w polu rodzica lub tekście) B6 pojęcie spoza słownika w tekście EARS
  B3 zdublowane ID                           B7 rodzic niedozwolonego typu
  B4 niedozwolona wartość (status, wynik,   B8 brak wymaganego pokrycia (poziom „blad”)
     wzorzec, kod w produkuje:)
Ostrzeżenia:
  O1 brak oczekiwanego pokrycia (poziom „ostrzezenie”)
  O2 rozstrzygnięta decyzja bez dzieci i bez wzmianki w commitach (tylko na ekranie)
  O3 produkt w stanie zweryfikowany/zatwierdzony bez weryfikacji WER z wynikiem „zgodny” (D-11)

Użycie: python3 narzedzia/slad.py [plik_wyjściowy=slad.md]
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
        if not m.typy[e.typ].get("pojecia"):
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

    for e, pierwszy in m.duplikaty:
        bledy.append(f"B3 {e.id}: zdublowane ID ({m.wzgledna(e.plik)}:{e.linia} i {m.wzgledna(pierwszy.plik)}:{pierwszy.linia})")

    for e in m.elementy:
        t = typy[e.typ]
        for pole in t.get("wymagane_pola", []):
            if not e.pola.get(pole):
                bledy.append(f"B1 {e.id}: brak pola „{pole}”")
        if t.get("statusy") and e.pola.get("status") and e.pola["status"] not in t["statusy"]:
            bledy.append(f"B4 {e.id}: status „{e.pola['status']}” spoza {t['statusy']}")
        if t.get("wyniki") and e.pola.get("wynik") and e.pola["wynik"] not in t["wyniki"]:
            bledy.append(f"B4 {e.id}: wynik „{e.pola['wynik']}” spoza {t['wyniki']}")
        if t.get("produkuje"):
            for x in m.produkty(e)[1]:
                bledy.append(f"B4 {e.id}: „{x}” w produkuje: nie jest kodem typu ani ID")
        pola = t.get("pola", [])
        if pola:
            ids = []
            for p in pola:
                ids += m.ids_w(e.pola.get(p, ""))
            if not ids and not t.get("korzen"):
                bledy.append(f"B1 {e.id}: brak rodzica (pola: {', '.join(pola)})")
            for r in ids:
                if r not in po_id:
                    bledy.append(f"B2 {e.id}: nieznany rodzic {r}")
                elif po_id[r].typ not in t.get("rodzice", []):
                    bledy.append(f"B7 {e.id}: rodzic {r} typu {po_id[r].typ} niedozwolony (dozwolone: {', '.join(t.get('rodzice', []))})")
                else:
                    rodzice_el[e.id].append(r)
                    dzieci[r].append(e.id)
        if t.get("ears") and e.pola.get("tekst") and e.pola.get("wzorzec"):
            tekst, wz = e.pola["tekst"], e.pola["wzorzec"]
            if wz not in ears:
                bledy.append(f"B4 {e.id}: nieznany wzorzec EARS „{wz}”")
            elif not ears[wz](tekst):
                bledy.append(f"B5 {e.id}: tekst nie pasuje do wzorca {wz}")
            if tekst.count(" shall ") != 1:
                bledy.append(f"B5 {e.id}: tekst musi mieć dokładnie jedno „shall”")
            if not tekst.startswith(m.system) and f" {m.system} shall" not in tekst:
                bledy.append(f"B5 {e.id}: podmiotem „shall” musi być {m.system}")
            brak = nieznane_pojecia(tekst, znane_poj, m.system)
            if brak:
                bledy.append(f"B6 {e.id}: pojęcia spoza słownika: {', '.join(sorted(set(brak)))}")

    for p in m.pliki_aktywne():
        for nr, l in M._linie_bez_kodu(p):
            for ref in m.ids_w(l):
                if ref not in po_id:
                    bledy.append(f"B2 {m.wzgledna(p)}:{nr}: nieznany odnośnik {ref}")

    commity = None
    for e in m.elementy:
        t = typy[e.typ]
        if not t.get("pokrycie"):
            continue
        war = t.get("warunek_pokrycia")
        if war:
            pole, wart = war.split("=", 1)
            if e.pola.get(pole.strip()) != wart.strip():
                continue
        for regula in t["pokrycie"].split(","):
            kod, poziom = [x.strip() for x in regula.split(":")]
            if kod == "*":
                if dzieci.get(e.id):
                    continue
                if commity is None:
                    commity = wzmianki_w_commitach(m)
                if e.id not in commity:
                    ekran.append(f"O2 {e.id}: brak dzieci i wzmianki w commitach")
                continue
            if kod not in typy or not typy[kod]["aktywny"]:
                continue
            if not any(po_id[c].typ == kod for c in dzieci.get(e.id, [])):
                wpis = f"{e.id}: brak dzieci typu {kod} ({typy[kod]['nazwa']})"
                if poziom == "blad":
                    bledy.append("B8 " + wpis)
                else:
                    ostrz.append("O1 " + wpis)

    if "WER" in typy and typy["WER"]["aktywny"] and len(m.stany) > 1:
        for e in m.elementy:
            if typy[e.typ].get("produkt") and m.stan(e) in m.stany[1:]:
                if not any(po_id[c].typ == "WER" and po_id[c].pola.get("wynik") == "zgodny" for c in dzieci.get(e.id, [])):
                    ostrz.append(f"O3 {e.id}: stan „{m.stan(e)}” bez weryfikacji WER z wynikiem „zgodny”")

    aktywne = [k for k, t in typy.items() if t["aktywny"]]
    liczby = " · ".join(f"{k} {sum(1 for e in m.elementy if e.typ == k)}" for k in aktywne)
    out = ["# Macierz śladu", "",
           "Plik generowany przez narzedzia/slad.py według narzedzia/id.toml; nie edytuj ręcznie (P-04).", "",
           f"Elementy: {liczby or 'brak'}", "",
           f"Błędy: {len(bledy)} · ostrzeżenia: {len(ostrz)}", "",
           "## W górę: element → rodzice", "",
           "| Element | Typ | Rodzice |", "| --- | --- | --- |"]
    for e in m.elementy:
        if typy[e.typ].get("pola"):
            out.append(f"| {e.id} | {e.typ} | {', '.join(rodzice_el.get(e.id, [])) or '—'} |")
    out += ["", "## W dół: element → dzieci", "", "| Element | Typ | Dzieci |", "| --- | --- | --- |"]
    for e in m.elementy:
        if dzieci.get(e.id) or typy[e.typ].get("pokrycie"):
            out.append(f"| {e.id} | {e.typ} | {', '.join(dzieci.get(e.id, [])) or '—'} |")
    zadania = [e for e in m.elementy if typy[e.typ].get("produkuje")]
    if zadania:
        out += ["", "## Plan → produkty (produkuje:, wyjątek od P-03)", "",
                "| Zadanie | Produkuje | Elementy |", "| --- | --- | --- |"]
        for e in zadania:
            el = m.produkty(e)[0]
            out.append(f"| {e.id} | {e.pola.get('produkuje', '')} | {', '.join(x.id for x in el) or '—'} |")
    out += ["", "## Produkty pracy ISO/IEC 29110-5-1-2", "", "| Produkt | Typ | Elementy |", "| --- | --- | --- |"]
    for k, t in typy.items():
        if t.get("iso"):
            ile = sum(1 for e in m.elementy if e.typ == k) if t["aktywny"] else "nieaktywny"
            out.append(f"| {t['iso']} | {k} {t['nazwa']} | {ile} |")
    for w in m.iso_inne:
        wp, _, gdzie = w.partition(" ")
        out.append(f"| {wp} | {gdzie} | — |")
    if bledy or ostrz:
        out += ["", "## Błędy i ostrzeżenia", ""] + [f"- {x}" for x in bledy + ostrz]
    with open(os.path.join(m.korzen, wyjscie) if not os.path.isabs(wyjscie) else wyjscie, "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")

    for x in bledy + ostrz + ekran:
        print(x)
    print(f"slad.py: {len(m.elementy)} elementów, {len(bledy)} błędów, {len(ostrz) + len(ekran)} ostrzeżeń")
    return 1 if bledy else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "slad.md"))
