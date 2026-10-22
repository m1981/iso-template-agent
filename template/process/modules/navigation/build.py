"""Buduje navigation-map.html z mapy ekranów (spec/navigation/screens.mmd) i wyniku check.py.

Użycie: python3 process/modules/navigation/build.py [wyjście] [mapa=spec/navigation/screens.mmd]
Wyjście domyślnie: navigation-map.html w katalogu mapy.
Szablon strony (template.html) leży obok skryptu, w pakiecie procesu.
"""
import html
import io
import contextlib
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import check  # noqa: E402

SCREENS = sys.argv[2] if len(sys.argv) > 2 else os.path.join("spec", "navigation", "screens.mmd")
OUTPUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(SCREENS), "navigation-map.html")


def md_to_table(rows):
    out = ["<table><thead><tr>"]
    out += [f"<th>{html.escape(c)}</th>" for c in rows[0]]
    out.append("</tr></thead><tbody>")
    for r in rows[1:]:
        out.append("<tr>")
        for c in r:
            if c in ("OK", "UWAGA", "INFO"):
                cls = {"OK": "ok", "UWAGA": "warn", "INFO": "info"}[c]
                out.append(f'<td><span class="pill {cls}">{c}</span></td>')
            elif re.fullmatch(r"\d+|brak ścieżki", c):
                out.append(f'<td class="num">{c}</td>')
            else:
                out.append(f"<td>{html.escape(c)}</td>")
        out.append("</tr>")
    out.append("</tbody></table>")
    return "".join(out)


buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    check.main(SCREENS)
blocks = [b for b in buf.getvalue().strip().split("\n\n")]
tables = []
for b in blocks:
    lines = [l for l in b.splitlines() if not l.startswith("| ---")]
    tables.append([[c.strip() for c in l.strip("|").split("|")] for l in lines])

mmd = "\n".join(l for l in open(SCREENS, encoding="utf-8").read().splitlines()
                if not l.strip().startswith("%%"))
page = open(os.path.join(HERE, "template.html"), encoding="utf-8").read()
page = page.replace("{{MERMAID}}", html.escape(mmd, quote=False))
page = page.replace("{{RULES}}", md_to_table(tables[0]))
page = page.replace("{{PATHS}}", md_to_table(tables[1]))
open(OUTPUT, "w", encoding="utf-8").write(page)
print("ok")
