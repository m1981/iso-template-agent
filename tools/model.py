"""Wczytuje model śledzalności (tools/id.toml) i elementy z artefaktów.

Bez zależności zewnętrznych; działa na Pythonie 3.8+ (tomllib nie jest wymagany).
"""
import glob
import os
import re

TOOLS_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(TOOLS_DIR)


# ---------- id.toml (podzbiór TOML: [tabela], [[tablica]], napisy, true/false, listy napisów)

def _scan(line):
    """Znaki linii poza napisami TOML: (indeks, znak); napisy "…" z ucieczkami \\ są pomijane."""
    in_string, escaped = False, False
    for i, ch in enumerate(line):
        if in_string:
            if escaped:
                escaped = False
            elif ch == "\\":
                escaped = True
            elif ch == '"':
                in_string = False
        elif ch == '"':
            in_string = True
        else:
            yield i, ch


def _strip_comment(line):
    for i, ch in _scan(line):
        if ch == "#":
            return line[:i]
    return line


def _list_closed(value):
    """Czy wartość zaczynająca się od „[” ma już zamykający „]” poza napisami."""
    depth = 0
    for _, ch in _scan(value):
        if ch == "[":
            depth += 1
        elif ch == "]":
            depth -= 1
    return depth <= 0


def _unescape(s):
    return re.sub(r'\\(["\\])', r"\1", s)


def _value(s, where):
    s = s.strip()
    if s in ("true", "false"):
        return s == "true"
    if s.startswith('"') and s.endswith('"'):
        return _unescape(s[1:-1])
    if s.startswith("[") and s.endswith("]"):
        return [_unescape(x) for x in re.findall(r'"((?:[^"\\]|\\.)*)"', s)]
    raise ValueError(f"{where}: nieobsługiwana wartość: {s}")


def load_toml(fpath, fallback=False):
    """TOML przez tomllib (Python 3.11+), a bez niego przez parser podzbioru poniżej.
    fallback=True wymusza parser podzbioru (test zgodności obu dróg)."""
    if not fallback:
        try:
            import tomllib  # Python 3.11+
            with open(fpath, "rb") as f:
                return tomllib.load(f)
        except ImportError:
            pass
    data = {}
    current = data
    with open(fpath, encoding="utf-8") as f:
        lines = list(enumerate(f, 1))
    i = 0
    while i < len(lines):
        lineno, line = lines[i]
        i += 1
        s = _strip_comment(line).strip()
        if not s:
            continue
        where = f"{fpath}:{lineno}"
        # lista rozpisana na kilka linii: "klucz = [" … aż do zamykającego "]" poza napisami
        m = re.fullmatch(r"\w+\s*=\s*(\[.*)", s)
        if m and not _list_closed(m.group(1)):
            while i < len(lines) and not _list_closed(s.split("=", 1)[1]):
                s += " " + _strip_comment(lines[i][1]).strip()
                i += 1
        m = re.fullmatch(r"\[\[(\w+)\]\]", s)
        if m:
            current = {}
            data.setdefault(m.group(1), []).append(current)
            continue
        m = re.fullmatch(r"\[(\w+)\]", s)
        if m:
            current = data.setdefault(m.group(1), {})
            continue
        m = re.fullmatch(r"(\w+)\s*=\s*(.+)", s)
        if not m:
            raise ValueError(f"{where}: nieobsługiwana składnia: {s}")
        current[m.group(1)] = _value(m.group(2), where)
    return data


# ---------- elementy

class Element:
    def __init__(self, type_def, ident, title, file, lineno):
        self.type, self.id, self.title, self.file, self.lineno = type_def, ident, title, file, lineno
        self.fields = {}

    def __repr__(self):
        return f"{self.id} ({self.type})"


def _lines_outside_code(fpath):
    """Linie pliku z pominięciem bloków ``` (tam są przykłady formatu)."""
    in_code = False
    with open(fpath, encoding="utf-8") as f:
        for lineno, l in enumerate(f, 1):
            if l.lstrip().startswith("```"):
                in_code = not in_code
                continue
            if not in_code:
                yield lineno, l.rstrip("\n")


def _markdown(type_def, fpath):
    elem = None
    for lineno, l in _lines_outside_code(fpath):
        m = re.match(r"^#{2,4}\s+(\S+)\s*(.*)$", l)
        if m:
            elem = None
            if type_def["re"].fullmatch(m.group(1)):
                elem = Element(type_def["code"], m.group(1), m.group(2).strip(), fpath, lineno)
                yield elem
            continue
        if elem is not None:
            m = re.match(r"^- (\w+):\s*(.*)$", l)
            if m:
                elem.fields[m.group(1).strip().lower()] = m.group(2).strip()


def _feature(type_def, fpath):
    """Element = tag @ID, komentarze „# pole: wartość” i pierwszy scenariusz po tagu.
    Kolejny tag, nagłówek Feature albo scenariusz bez tagu kończy element."""
    elem, before_scenario = None, False
    for lineno, l in _lines_outside_code(fpath):
        s = l.strip()
        if s.startswith("@"):
            matched = [t for t in re.findall(r"@(\S+)", s) if type_def["re"].fullmatch(t)]
            elem = Element(type_def["code"], matched[0], "", fpath, lineno) if matched else None
            before_scenario = bool(matched)
            if elem is not None:
                yield elem
            continue
        if re.match(r"^(?:Feature|Funkcja)\s*:", s):
            elem = None
            continue
        if elem is None:
            continue
        m = re.match(r"^(?:Scenario|Scenariusz|Scenario Outline|Szablon scenariusza)\s*:\s*(.*)$", s)
        if m:
            if before_scenario:
                elem.title, before_scenario = m.group(1).strip(), False
            else:
                elem = None
            continue
        m = re.match(r"^#\s*(\w+):\s*(.*)$", s)
        if m:
            elem.fields[m.group(1).strip().lower()] = m.group(2).strip()


def _mermaid(type_def, fpath):
    elements = {}
    for lineno, l in _lines_outside_code(fpath):
        m = re.match(r"^\s*%%\s*(\S+)(?:\s+(\w+):\s*(.*))?$", l)
        if not m or not type_def["re"].fullmatch(m.group(1)):
            continue
        ident = m.group(1)
        if ident not in elements:
            elements[ident] = Element(type_def["code"], ident, "", fpath, lineno)
        if m.group(2):
            elements[ident].fields[m.group(2).strip().lower()] = m.group(3).strip()
    return list(elements.values())


PARSERS = {"markdown": _markdown, "feature": _feature, "mermaid": _mermaid}


class Model:
    def __init__(self, root=ROOT):
        self.root = root
        cfg = load_toml(os.path.join(root, "tools", "id.toml"))
        project = cfg.get("project", {})
        self.system = project.get("system", "System")
        self.states = project.get("product_states", [])
        self.iso_other = project.get("iso_other", [])
        self.field_names = cfg.get("fields", {})  # rola → nazwa pola w artefaktach
        self.common_fields = project.get("common_fields", [])
        self.types = {}
        for t in cfg.get("type", []):
            if t.get("product"):
                t["statuses"] = self.states
                t["required"] = list(t.get("required", [])) + [self.field_names.get("status", "status")]  # D-14
            t["known"] = set(t.get("fields", []) + t.get("required", []) + t.get("optional", []) + self.common_fields)
            if t.get("statuses"):
                t["known"].add(self.field_names.get("status", "status"))
            if t.get("produces"):
                t["known"].add(self.field_names.get("produces", "produces"))
            t["rules"] = {}
            for rule in t.get("parent_rules", []):  # "pole: KOD|KOD [pole=wartość]" (D-28)
                m = re.fullmatch(r"\s*(\w+)\s*:\s*([\w|]+)(?:\s+(\w+)=(\S+))?\s*", rule)
                if not m:
                    raise ValueError(f"tools/id.toml, typ {t['code']}: niepoprawna reguła parent_rules: {rule}")
                t["rules"][m.group(1)] = (m.group(2).split("|"), (m.group(3), m.group(4)) if m.group(3) else None)
            t["re"] = re.compile(t["pattern"])
            t["paths"] = sorted(glob.glob(os.path.join(root, t["file"])))
            t["active"] = bool(t["paths"])
            self.types[t["code"]] = t
        # ID jest osobnym słowem: bez liter, cyfr ani łącznika tuż przed i tuż po (np. nie „SHA-256”, nie „CODE-01”)
        alternatives = "|".join(f"(?:{t['pattern']})" for t in self.types.values())
        self.re_id = re.compile(rf"(?<![\w-])(?:{alternatives})(?![\w-])")
        self.elements, self.duplicates = [], []
        seen = {}
        for t in self.types.values():
            parser = PARSERS[t.get("format", "markdown")]
            for p in t["paths"]:
                for e in parser(t, p):
                    if e.id in seen:
                        self.duplicates.append((e, seen[e.id]))
                        continue
                    seen[e.id] = e
                    self.elements.append(e)
        self.by_id = seen
        self.bad_headings = self._bad_headings()
        self.checklist = self._checklist()

    def _checklist(self):
        """checklist.md (D-31): {kod sekcji: {punkty}} z nagłówków „## KOD …” i linii „- KOD.n …”."""
        fpath = os.path.join(self.root, "checklist.md")
        lists, current = {}, None
        if not os.path.exists(fpath):
            return lists
        for _, l in _lines_outside_code(fpath):
            m = re.match(r"^## ([A-Z]+)\b", l)
            if m:
                current = lists.setdefault(m.group(1), set())
                continue
            m = re.match(r"^- ([A-Z]+\.\d+)\s", l)
            if m and current is not None:
                current.add(m.group(1))
        return lists

    def _bad_headings(self):
        """Nagłówki markdown, w których po ID stoi dwukropek („### UC-02: Tytuł”): (plik, linia, ID)."""
        found = []
        for t in self.types.values():
            if t.get("format", "markdown") != "markdown":
                continue
            for p in t["paths"]:
                for lineno, l in _lines_outside_code(p):
                    m = re.match(r"^#{2,4}\s+(\S+):(?:\s|$)", l)
                    if m and t["re"].fullmatch(m.group(1)):
                        found.append((p, lineno, m.group(1)))
        return found

    def ids_in(self, content):
        return self.re_id.findall(content or "")

    def relative(self, fpath):
        return os.path.relpath(fpath, self.root)

    def value(self, e, role):
        """Wartość pola o danej roli (nazwa pola z [fields] w id.toml)."""
        return e.fields.get(self.field_names.get(role, role), "")

    def state(self, e):
        return self.value(e, "status")

    def products(self, e):
        """Pole produces: (D-09) → (elementy, nieznane kody). Wpis to kod typu albo ID."""
        result, unknown = [], []
        for x in [w.strip() for w in self.value(e, "produces").split(",") if w.strip()]:
            if x in self.types:
                result += [elem for elem in self.elements if elem.type == x]
            elif x in self.by_id:
                result.append(self.by_id[x])
            elif not self.re_id.fullmatch(x):
                unknown.append(x)
        return result, unknown

    def active_files(self):
        return sorted({p for t in self.types.values() for p in t["paths"]})
