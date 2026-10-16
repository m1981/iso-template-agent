"""Wczytuje model śledzalności (tools/id.toml) i elementy z artefaktów.

Bez zależności zewnętrznych; działa na Pythonie 3.8+ (tomllib nie jest wymagany).
"""
import glob
import os
import re

TOOLS_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(TOOLS_DIR)


# ---------- id.toml (podzbiór TOML: [tabela], [[tablica]], napisy, true/false, listy napisów)

def _strip_comment(lineno):
    in_string, prev = False, ""
    for i, z in enumerate(lineno):
        if z == '"' and prev != "\\":
            in_string = not in_string
        elif z == "#" and not in_string:
            return lineno[:i]
        prev = z
    return lineno


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


def load_toml(fpath):
    try:
        import tomllib  # Python 3.11+
        with open(fpath, "rb") as f:
            return tomllib.load(f)
    except ImportError:
        pass
    data, current = {}, None
    current = data
    with open(fpath, encoding="utf-8") as f:
        for lineno, lineno in enumerate(f, 1):
            s = _strip_comment(lineno).strip()
            if not s:
                continue
            where = f"{fpath}:{lineno}"
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
            m = re.match(r"^- ([^:]{1,40}):\s*(.*)$", l)
            if m:
                elem.fields[m.group(1).strip().lower()] = m.group(2).strip()


def _feature(type_def, fpath):
    elem = None
    for lineno, l in _lines_outside_code(fpath):
        s = l.strip()
        tags = re.findall(r"@(\S+)", s) if s.startswith("@") else []
        matched = [t for t in tags if type_def["re"].fullmatch(t)]
        if matched:
            elem = Element(type_def["code"], matched[0], "", fpath, lineno)
            yield elem
            continue
        if elem is None:
            continue
        m = re.match(r"^#\s*([^:]{1,40}):\s*(.*)$", s)
        if m:
            elem.fields[m.group(1).strip().lower()] = m.group(2).strip()
        m = re.match(r"^(?:Scenario|Scenariusz)\s*:\s*(.*)$", s)
        if m:
            elem.title = m.group(1).strip()


def _mermaid(type_def, fpath):
    elements = {}
    for lineno, l in _lines_outside_code(fpath):
        m = re.match(r"^\s*%%\s*(\S+)(?:\s+([^:]{1,40}):\s*(.*))?$", l)
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
            t["re"] = re.compile(t["pattern"])
            t["paths"] = sorted(glob.glob(os.path.join(root, t["file"])))
            t["active"] = bool(t["paths"])
            self.types[t["code"]] = t
        self.re_id = re.compile("|".join(f"(?:{t['pattern']})" for t in self.types.values()))
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
