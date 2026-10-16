"""Wczytuje model śledzalności (tools/id.toml) i elementy z artefaktów.

Bez zależności zewnętrznych; działa na Pythonie 3.8+ (tomllib nie jest wymagany).
"""
import glob
import os
import re

KATALOG = os.path.dirname(os.path.abspath(__file__))
KORZEN = os.path.dirname(KATALOG)


# ---------- id.toml (podzbiór TOML: [tabela], [[tablica]], napisy, true/false, listy napisów)

def _bez_komentarza(linia):
    w_napisie, poprz = False, ""
    for i, z in enumerate(linia):
        if z == '"' and poprz != "\\":
            w_napisie = not w_napisie
        elif z == "#" and not w_napisie:
            return linia[:i]
        poprz = z
    return linia


def _napis(s):
    return re.sub(r'\\(["\\])', r"\1", s)


def _wartosc(s, gdzie):
    s = s.strip()
    if s in ("true", "false"):
        return s == "true"
    if s.startswith('"') and s.endswith('"'):
        return _napis(s[1:-1])
    if s.startswith("[") and s.endswith("]"):
        return [_napis(x) for x in re.findall(r'"((?:[^"\\]|\\.)*)"', s)]
    raise ValueError(f"{gdzie}: nieobsługiwana wartość: {s}")


def wczytaj_toml(sciezka):
    try:
        import tomllib  # Python 3.11+
        with open(sciezka, "rb") as f:
            return tomllib.load(f)
    except ImportError:
        pass
    dane, biezacy = {}, None
    biezacy = dane
    with open(sciezka, encoding="utf-8") as f:
        for nr, linia in enumerate(f, 1):
            s = _bez_komentarza(linia).strip()
            if not s:
                continue
            gdzie = f"{sciezka}:{nr}"
            m = re.fullmatch(r"\[\[(\w+)\]\]", s)
            if m:
                biezacy = {}
                dane.setdefault(m.group(1), []).append(biezacy)
                continue
            m = re.fullmatch(r"\[(\w+)\]", s)
            if m:
                biezacy = dane.setdefault(m.group(1), {})
                continue
            m = re.fullmatch(r"(\w+)\s*=\s*(.+)", s)
            if not m:
                raise ValueError(f"{gdzie}: nieobsługiwana składnia: {s}")
            biezacy[m.group(1)] = _wartosc(m.group(2), gdzie)
    return dane


# ---------- elementy

class Element:
    def __init__(self, typ, ident, tytul, plik, linia):
        self.typ, self.id, self.tytul, self.plik, self.linia = typ, ident, tytul, plik, linia
        self.pola = {}

    def __repr__(self):
        return f"{self.id} ({self.typ})"


def _linie_bez_kodu(sciezka):
    """Linie pliku z pominięciem bloków ``` (tam są przykłady formatu)."""
    w_kodzie = False
    with open(sciezka, encoding="utf-8") as f:
        for nr, l in enumerate(f, 1):
            if l.lstrip().startswith("```"):
                w_kodzie = not w_kodzie
                continue
            if not w_kodzie:
                yield nr, l.rstrip("\n")


def _markdown(typ, sciezka):
    el = None
    for nr, l in _linie_bez_kodu(sciezka):
        m = re.match(r"^#{2,4}\s+(\S+)\s*(.*)$", l)
        if m:
            el = None
            if typ["re"].fullmatch(m.group(1)):
                el = Element(typ["code"], m.group(1), m.group(2).strip(), sciezka, nr)
                yield el
            continue
        if el is not None:
            m = re.match(r"^- ([^:]{1,40}):\s*(.*)$", l)
            if m:
                el.pola[m.group(1).strip().lower()] = m.group(2).strip()


def _feature(typ, sciezka):
    el = None
    for nr, l in _linie_bez_kodu(sciezka):
        s = l.strip()
        tagi = re.findall(r"@(\S+)", s) if s.startswith("@") else []
        trafione = [t for t in tagi if typ["re"].fullmatch(t)]
        if trafione:
            el = Element(typ["code"], trafione[0], "", sciezka, nr)
            yield el
            continue
        if el is None:
            continue
        m = re.match(r"^#\s*([^:]{1,40}):\s*(.*)$", s)
        if m:
            el.pola[m.group(1).strip().lower()] = m.group(2).strip()
        m = re.match(r"^(?:Scenario|Scenariusz)\s*:\s*(.*)$", s)
        if m:
            el.tytul = m.group(1).strip()


def _mermaid(typ, sciezka):
    elementy = {}
    for nr, l in _linie_bez_kodu(sciezka):
        m = re.match(r"^\s*%%\s*(\S+)(?:\s+([^:]{1,40}):\s*(.*))?$", l)
        if not m or not typ["re"].fullmatch(m.group(1)):
            continue
        ident = m.group(1)
        if ident not in elementy:
            elementy[ident] = Element(typ["code"], ident, "", sciezka, nr)
        if m.group(2):
            elementy[ident].pola[m.group(2).strip().lower()] = m.group(3).strip()
    return list(elementy.values())


FORMATY = {"markdown": _markdown, "feature": _feature, "mermaid": _mermaid}


class Model:
    def __init__(self, korzen=KORZEN):
        self.korzen = korzen
        cfg = wczytaj_toml(os.path.join(korzen, "tools", "id.toml"))
        projekt = cfg.get("project", {})
        self.system = projekt.get("system", "System")
        self.stany = projekt.get("product_states", [])
        self.iso_inne = projekt.get("iso_other", [])
        self.pole = cfg.get("fields", {})  # rola → nazwa pola w artefaktach
        self.wspolne = projekt.get("common_fields", [])
        self.typy = {}
        for t in cfg.get("type", []):
            if t.get("product"):
                t["statuses"] = self.stany
                t["required"] = list(t.get("required", [])) + [self.pole.get("status", "status")]  # D-14
            t["znane"] = set(t.get("fields", []) + t.get("required", []) + t.get("optional", []) + self.wspolne)
            if t.get("statuses"):
                t["znane"].add(self.pole.get("status", "status"))
            if t.get("produces"):
                t["znane"].add(self.pole.get("produces", "produces"))
            t["re"] = re.compile(t["pattern"])
            t["pliki"] = sorted(glob.glob(os.path.join(korzen, t["file"])))
            t["aktywny"] = bool(t["pliki"])
            self.typy[t["code"]] = t
        self.re_id = re.compile("|".join(f"(?:{t['pattern']})" for t in self.typy.values()))
        self.elementy, self.duplikaty = [], []
        widziane = {}
        for t in self.typy.values():
            parser = FORMATY[t.get("format", "markdown")]
            for p in t["pliki"]:
                for e in parser(t, p):
                    if e.id in widziane:
                        self.duplikaty.append((e, widziane[e.id]))
                        continue
                    widziane[e.id] = e
                    self.elementy.append(e)
        self.po_id = widziane

    def ids_w(self, tekst):
        return self.re_id.findall(tekst or "")

    def wzgledna(self, sciezka):
        return os.path.relpath(sciezka, self.korzen)

    def p(self, e, rola):
        """Wartość pola o danej roli (nazwa pola z [fields] w id.toml)."""
        return e.pola.get(self.pole.get(rola, rola), "")

    def stan(self, e):
        return self.p(e, "status")

    def produkty(self, e):
        """Pole produces: (D-09) → (elementy, nieznane kody). Wpis to kod typu albo ID."""
        wynik, nieznane = [], []
        for x in [w.strip() for w in self.p(e, "produces").split(",") if w.strip()]:
            if x in self.typy:
                wynik += [el for el in self.elementy if el.typ == x]
            elif x in self.po_id:
                wynik.append(self.po_id[x])
            elif not self.re_id.fullmatch(x):
                nieznane.append(x)
        return wynik, nieznane

    def pliki_aktywne(self):
        return sorted({p for t in self.typy.values() for p in t["pliki"]})
