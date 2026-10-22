"""Sprawdza mapę nawigacji zapisaną w Mermaid (screens.mmd).

Reguły:
  R1 Osiągalność      - każdy ekran da się osiągnąć ze Startu (E01).
  R2 Brak pułapek     - z każdego ekranu da się wrócić do Startu.
  R3 Wyjście z modala - każdy modal ma krawędź wyjścia (-.->) do ekranu spoza modali.
  R4 Postęp: sukces   - każdy ekran sukcesu ma wezwanie (==>) do dalszej pracy.
  R5 Postęp: wycieki  - ekrany, z których wychodzi się tylko wyjściem/powrotem,
                        bez żadnego kroku naprzód; świadome wyjątki deklaruje
                        komentarz `%% exception-dp01: ID (decyzja)`.
  R6 Elastyczność     - najkrótsze ścieżki (liczba kliknięć) dla par z KEY_PAIRS.
  R7 Ślad ekranów     - każdy ekran ma komentarz `%% E-nn realizes: UC-nn`
                        (powiązanie z modelem śladu, tools/id.toml).
Ekrany klasy `screen` mają pasek nawigacji, więc dostają niejawną krawędź do NAV.
Użycie: python3 check.py screens.mmd
"""
import re
import sys
from collections import deque

EDGE = re.compile(r'^\s*(\w+)\s*(-->|==>|-\.->)\s*(?:\|"?(.*?)"?\|)?\s*(\w+)\s*$')
CLASS = re.compile(r'^\s*class\s+([\w,]+)\s+(\w+)\s*$')
REALIZES_RE = re.compile(r'^\s*%%\s*E-(\d{2})\s+realizes:\s*\S')
EXCEPTION_RE = re.compile(r'^\s*%%\s*exception-dp01:\s*(\w+)\s*(.*)$')
NODE = re.compile(r'^\s*(\w+)\s*[\[\(\/]+"?([^"\]\)]*)')

# Pary (skąd, dokąd, opis) do pomiaru liczby kliknięć; uzupełnij dla swojej mapy.
KEY_PAIRS = [
    ("E01", "E03", "Start → szczegóły"),
]


def parse_map(path):
    edges, node_classes, labels, exceptions_map = [], {}, {}, {}
    realizes_set = set()
    for line in open(path, encoding="utf-8"):
        m = REALIZES_RE.match(line)
        if m:
            realizes_set.add("E" + m.group(1))
            continue
        m = EXCEPTION_RE.match(line)
        if m:
            exceptions_map[m.group(1)] = m.group(2).strip()
            continue
        if line.strip().startswith("%%"):
            continue
        m = EDGE.match(line)
        if m:
            edges.append((m.group(1), m.group(2), m.group(3) or "", m.group(4)))
            continue
        m = CLASS.match(line)
        if m:
            for n in m.group(1).split(","):
                node_classes[n] = m.group(2)
            continue
        m = NODE.match(line)
        if m and not line.strip().startswith(("classDef", "flowchart")):
            labels[m.group(1)] = m.group(2).strip()
    return edges, node_classes, labels, exceptions_map, realizes_set


def graph(edges, node_classes):
    g = {}
    for a, _, _, b in edges:
        g.setdefault(a, set()).add(b)
        g.setdefault(b, set())
    for n, k in node_classes.items():
        if k == "screen":
            g.setdefault(n, set()).add("NAV")
    return g


def bfs(g, start):
    dist = {start: 0}
    q = deque([start])
    while q:
        u = q.popleft()
        for v in g.get(u, ()):
            if v not in dist:
                dist[v] = dist[u] + 1
                q.append(v)
    return dist


def clicks(g, a, b):
    """Kliknięcia: przejście przez NAV liczy się jako jedno kliknięcie (pasek)."""
    g2 = {u: set(vs) for u, vs in g.items()}
    for u, vs in g2.items():
        if "NAV" in vs:
            vs.discard("NAV")
            vs |= g.get("NAV", set())
    return bfs(g2, a).get(b)


def main(path):
    edge_list, node_class, labels, exceptions, realized = parse_map(path)
    g = graph(edge_list, node_class)
    # ekrany: węzły z krawędzi oraz zadeklarowane bez krawędzi (etykieta albo klasa), żeby R1–R7 widziały sieroty
    declared = list(dict.fromkeys(list(g) + list(labels) + list(node_class)))
    screens = [n for n in declared if n != "NAV" and node_class.get(n) != "external"]
    label_of = lambda n: labels.get(n, n)
    results = []

    reached = bfs(g, "E01")
    r1 = [n for n in screens if n not in reached]
    results.append(("R1 Osiągalność ze Startu", r1))

    r2 = [n for n in screens if "E01" not in bfs(g, n)]
    results.append(("R2 Brak pułapek (powrót do Startu)", r2))

    r3 = []
    for n in screens:
        if node_class.get(n) != "modal":
            continue
        ok = any(a == n and t == "-.->" and node_class.get(b) != "modal" for a, t, _, b in edge_list)
        if not ok:
            r3.append(n)
    results.append(("R3 Każdy modal ma wyjście", r3))

    r4 = []
    for n in screens:
        if node_class.get(n) != "success":
            continue
        if not any(a == n and t == "==>" for a, t, _, _ in edge_list):
            r4.append(n)
    results.append(("R4 Postęp: sukces z wezwaniem do dalszej pracy", r4))

    r5 = []
    for n in screens:
        outgoing = [(t, b) for a, t, _, b in edge_list if a == n and b != n]
        if outgoing and all(t == "-.->" for t, _ in outgoing) and n not in exceptions:
            r5.append(n)
    results.append(("R5 Postęp: miejsca bez kroku naprzód", r5))

    r7 = [n for n in screens if n not in realized]
    results.append(("R7 Każdy ekran realizuje przypadek użycia", r7))

    print("| Reguła | Wynik | Ekrany |")
    print("| --- | --- | --- |")
    for r, offenders in results:
        print(f"| {r} | {'OK' if not offenders else 'UWAGA'} | {', '.join(label_of(x) for x in offenders) or '—'} |")
    if exceptions:
        print(f"| Świadome wyjątki od zasady postępu | INFO | {', '.join(label_of(x) + ' ' + d for x, d in exceptions.items())} |")
    print()
    print("| R6 Para | Kliknięcia |")
    print("| --- | --- |")
    for a, b, desc in KEY_PAIRS:
        k = clicks(g, a, b)
        print(f"| {desc} | {k if k is not None else 'brak ścieżki'} |")
    return 1 if any(l for _, l in results) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "screens.mmd"))
