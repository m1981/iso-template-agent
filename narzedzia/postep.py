"""Rekord postępu (D-10; ISO/IEC 29110-5-1-2 WP.09, zadanie PM.03.01).

Generuje postep.md z plan.md (CEL, KM, ZAD, RP), rekordów (KOR, AKC), stanów
produktów pracy i tagów git. Plik jest deterministyczny: nie zależy od dzisiejszej
daty, tylko od repozytorium, więc pre-commit może sprawdzać jego aktualność.
Planowane i rzeczywiste: termin a pole „zakończono:” zadania, termin kamienia
a data jego tagu baseline.

Użycie: python3 narzedzia/postep.py [plik_wyjściowy=postep.md]
"""
import os
import subprocess
import sys
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import model as M  # noqa: E402


def tagi(korzen):
    try:
        out = subprocess.run(["git", "for-each-ref", "--format=%(refname:short) %(creatordate:short)", "refs/tags"],
                             cwd=korzen, capture_output=True, text=True, check=True).stdout
    except Exception:
        return {}
    return dict(l.split(" ", 1) for l in out.splitlines() if " " in l)


def main(wyjscie):
    m = M.Model()
    if not m.typy.get("ZAD", {}).get("aktywny"):
        print("postep.py: brak plan.md, pomijam")
        return 0
    po_typie = lambda kod: [e for e in m.elementy if e.typ == kod]  # noqa: E731
    t = tagi(m.korzen)
    akc = {}
    for a in po_typie("AKC"):
        for k in m.ids_w(a.pola.get("kamień", "")):
            akc.setdefault(k, []).append(f"{a.id} {a.pola.get('wynik', '')}")
    pola = lambda e, *n: [e.pola.get(x, "") or "—" for x in n]  # noqa: E731

    out = ["# Rekord postępu", "",
           "Plik generowany przez narzedzia/postep.py z plan.md, rekordów, stanów produktów i tagów git; "
           "nie edytuj ręcznie (D-10, ISO/IEC 29110 WP.09).", ""]

    zad = po_typie("ZAD")
    licz = Counter(e.pola.get("status", "") for e in zad)
    out += [f"Zadania: {len(zad)} · " + " · ".join(f"{s} {licz.get(s, 0)}" for s in m.typy["ZAD"]["statusy"]), ""]

    out += ["## Kamienie milowe", "", "| Kamień | Cel | Termin | Tag | Osiągnięty | Akceptacja |",
            "| --- | --- | --- | --- | --- | --- |"]
    for e in po_typie("KM"):
        tag = e.pola.get("tag", "")
        osiag = f"tak, {t[tag]}" if tag in t else "nie"
        out.append(f"| {e.id} {e.tytul} | {', '.join(pola(e, 'cel'))} | {', '.join(pola(e, 'termin'))} | "
                   f"{tag or '—'} | {osiag} | {', '.join(akc.get(e.id, [])) or '—'} |")

    out += ["", "## Zadania: planowane i rzeczywiste", "",
            "| Zadanie | Kamień | Status | Termin | Zakończono | Produkuje | Produkty według stanu |",
            "| --- | --- | --- | --- | --- | --- | --- |"]
    for e in zad:
        el = m.produkty(e)[0]
        st = Counter(m.stan(x) for x in el)
        stany = " · ".join(f"{s} {st[s]}" for s in m.stany if st.get(s)) or "brak elementów"
        kam, status, termin, kon, prod = pola(e, "kamień", "status", "termin", "zakończono", "produkuje")
        out.append(f"| {e.id} {e.tytul} | {kam} | {status} | {termin} | {kon} | {prod} | {stany} |")

    out += ["", "## Ryzyka projektu", "", "| Ryzyko | Status | Dotyczy | Działanie |", "| --- | --- | --- | --- |"]
    for e in po_typie("RP"):
        out.append(f"| {e.id} {e.tytul} | " + " | ".join(pola(e, "status", "dotyczy", "działanie")) + " |")

    kor = [e for e in po_typie("KOR") if e.pola.get("status") != "zakończona"]
    out += ["", "## Korekty niezakończone (WP.04)", "", "| Korekta | Status | Przyczyna | Działanie |",
            "| --- | --- | --- | --- |"]
    for e in kor:
        out.append(f"| {e.id} {e.tytul} | " + " | ".join(pola(e, "status", "przyczyna", "działanie")) + " |")

    out += ["", "## Stan produktów pracy (D-11)", "", "| Typ | ISO | " + " | ".join(m.stany) + " |",
            "| --- | --- | " + " | ".join("---" for _ in m.stany) + " |"]
    for k, typ in m.typy.items():
        if typ.get("produkt") and typ["aktywny"]:
            st = Counter(m.stan(e) for e in po_typie(k))
            out.append(f"| {k} {typ['nazwa']} | {typ.get('iso', '—')} | " + " | ".join(str(st.get(s, 0)) for s in m.stany) + " |")

    sciezka = wyjscie if os.path.isabs(wyjscie) else os.path.join(m.korzen, wyjscie)
    with open(sciezka, "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")
    print(f"postep.py: {len(zad)} zadań, {len(po_typie('KM'))} kamieni, {len(kor)} korekt niezakończonych")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "postep.md"))
