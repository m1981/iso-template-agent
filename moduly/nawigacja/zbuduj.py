"""Buduje mapa-nawigacji.html z ekrany.mmd i wyniku sprawdz.py."""
import html
import io
import contextlib
import re
import sys

import sprawdz


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
    sprawdz.main("ekrany.mmd")
blocks = [b for b in buf.getvalue().strip().split("\n\n")]
tables = []
for b in blocks:
    lines = [l for l in b.splitlines() if not l.startswith("| ---")]
    tables.append([[c.strip() for c in l.strip("|").split("|")] for l in lines])

mmd = "\n".join(l for l in open("ekrany.mmd", encoding="utf-8").read().splitlines()
                if not l.strip().startswith("%%"))
page = open("szablon.html", encoding="utf-8").read()
page = page.replace("{{MERMAID}}", html.escape(mmd, quote=False))
page = page.replace("{{REGULY}}", md_to_table(tables[0]))
page = page.replace("{{SCIEZKI}}", md_to_table(tables[1]))
open(sys.argv[1] if len(sys.argv) > 1 else "mapa-nawigacji.html", "w", encoding="utf-8").write(page)
print("ok")
