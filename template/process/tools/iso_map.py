"""Strona „ISO 29110 a nasz model śladu” (szablon D-25), generowana do reports/iso-map.html.

Dane normy: process/tools/iso29110.toml (23 produkty pracy, 84 zależności z zadań PM i SI).
Nasz model: process/tools/id.toml (pole iso typów); ocena pokrycia: project/settings.toml projektu
(iso_other, iso_partial, iso_out_of_scope; szablon D-55). Strona zależy tylko od tych plików, więc jest
deterministyczna, a pre-commit sprawdza jej aktualność jak trace.md.

Pokrycie produktu normy:
  partial       wpis w iso_partial (z powodem)
  covered       typ z polem iso albo wpis w iso_other
  out_of_scope  wpis w iso_out_of_scope (etap kodu, utrzymania)
  missing       żadne z powyższych

Diagramy są w Mermaid (<pre class="mermaid">); opublikowana strona renderuje je sama.
Użycie: python3 process/tools/iso_map.py [plik_wyjściowy=reports/iso-map.html]
"""
import html
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import model as M  # noqa: E402

LABEL = {"covered": "mamy", "partial": "częściowo", "missing": "brak", "out_of_scope": "poza etapem"}
ORDER = ["covered", "partial", "missing", "out_of_scope"]
# Produkty, do których prowadzi prawie każde zadanie; na diagramie rdzenia pomijamy krawędzie do nich.
SINKS = {"WP.11": "repozytorium", "WP.23": "rekord weryfikacji", "WP.03": "wniosek o zmianę"}
CLASSDEFS = [
    "classDef covered fill:#dcefe2,stroke:#2f7d4a,color:#13311d",
    "classDef partial fill:#fbeccf,stroke:#a9761a,color:#3a2906",
    "classDef missing fill:#f9dad3,stroke:#b2412f,color:#3d120b",
    "classDef out_of_scope fill:#eceef1,stroke:#7a828e,color:#22262c,stroke-dasharray:4 3",
]


def entries(items):
    """["WP.nn tekst", …] → {"WP.nn": "tekst"}."""
    out = {}
    for item in items:
        wp, _, text = item.partition(" ")
        out[wp] = text
    return out


def node(wp_id):
    return wp_id.replace(".", "")


def coverage(m, wps):
    ours = {}
    for code, t in m.types.items():
        for wp in [w.strip() for w in t.get("iso", "").split(",") if w.strip()]:
            ours.setdefault(wp, []).append(f"{code} · {t['file']}")
    for wp, where in entries(m.iso_other).items():
        ours.setdefault(wp, []).append(where)
    project = m.project  # reguły z id.toml i ustawienia projektu (szablon D-55)
    partial = entries(project.get("iso_partial", []))
    out_of_scope = entries(project.get("iso_out_of_scope", []))
    result = {}
    for wp in wps:
        i = wp["id"]
        if i in partial:
            state, note = "partial", partial[i]
        elif i in ours:
            state, note = "covered", ""
        elif i in out_of_scope:
            state, note = "out_of_scope", out_of_scope[i]
        else:
            state, note = "missing", ""
        result[i] = (state, ours.get(i, []), note)
    return result


def flowchart(wps, edges, cov, direction="LR"):
    lines = [f"flowchart {direction}"]
    used = {e["from"] for e in edges} | {e["to"] for e in edges}
    for wp in wps:
        if wp["id"] in used:
            lines.append(f'  {node(wp["id"])}["{wp["id"]} {wp["name"]}"]')
    for e in edges:
        lines.append(f'  {node(e["from"])} --> {node(e["to"])}')
    lines += ["  " + c for c in CLASSDEFS]
    for state in ORDER:
        ids = [node(w["id"]) for w in wps if w["id"] in used and cov[w["id"]][0] == state]
        if ids:
            lines.append(f"  class {','.join(ids)} {state}")
    return "\n".join(lines)


def trace_model(m):
    """Model śladu z id.toml: strzałka od dziecka do rodzica z nazwą pola (P-03)."""
    lines = ["flowchart BT"]
    for code, t in m.types.items():
        iso = f" · {t['iso']}" if t.get("iso") else ""
        lines.append(f'  {code}["{code} {t["name"]}{iso}"]')
    for code, t in m.types.items():
        for parent in t.get("parents", []):
            fields = [f for f in t.get("fields", []) if f not in t["rules"] or parent in t["rules"][f][0]]
            conds = [f"{k}={v}" for f in fields if f in t["rules"] and t["rules"][f][1] for k, v in [t["rules"][f][1]]]
            label = ", ".join(fields) + (f" ({', '.join(conds)})" if conds else "")
            lines.append(f'  {code} -->|"{label}"| {parent}')
    for code, t in m.types.items():
        if t.get("produces"):
            lines.append(f'  {code} -.->|"produces (w dół)"| PRODUCTS["produkty pracy: dowolny kod typu albo ID"]')
    return "\n".join(lines)


def table(wps, cov):
    rows = ["<table><thead><tr><th>Produkt</th><th>Nazwa w normie</th><th>Źródło</th><th>U nas</th>"
            "<th>Pokrycie</th><th>Uwagi</th></tr></thead><tbody>"]
    for wp in wps:
        state, ours, note = cov[wp["id"]]
        rows.append(
            f"<tr><td>{wp['id']}</td><td>{html.escape(wp['name'])}</td><td>{html.escape(wp['source'])}</td>"
            f"<td>{'<br>'.join(html.escape(x) for x in ours) or '—'}</td>"
            f'<td><span class="pill {state}">{LABEL[state]}</span></td><td>{html.escape(note) or "—"}</td></tr>')
    rows.append("</tbody></table>")
    return "\n".join(rows)


PAGE = """<title>ISO 29110 a nasz model śladu</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Literata:opsz,wght@7..72,600&family=Public+Sans:wght@400;600&family=JetBrains+Mono:wght@400;600&display=swap">
<style>
/* Układ: arkusz zgodności — podsumowanie, rdzeń zależności, tabela produkt po produkcie, model śladu, pełny graf */
:root {
  --bg: #f5f6f8; --panel: #ffffff; --fg: #1b2433; --muted: #586477; --line: #d6dce5;
  --covered: #2f7d4a; --covered-bg: #e3f2e8; --partial: #8a5a00; --partial-bg: #fcf0d8;
  --missing: #a33a2a; --missing-bg: #fbe4df; --out: #5d6674; --out-bg: #eceef1;
  --f-display: "Literata", Georgia, serif; --f-body: "Public Sans", system-ui, sans-serif;
  --f-mono: "JetBrains Mono", ui-monospace, monospace;
}
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) {
  --bg: #12161d; --panel: #1a2029; --fg: #e3e8ef; --muted: #9aa6b6; --line: #2e3744;
  --covered: #86d3a0; --covered-bg: #17321f; --partial: #f0b35c; --partial-bg: #3a2a12;
  --missing: #f19a8c; --missing-bg: #3b1b16; --out: #a8b1be; --out-bg: #232a34; color-scheme: dark } }
:root[data-theme="dark"] {
  --bg: #12161d; --panel: #1a2029; --fg: #e3e8ef; --muted: #9aa6b6; --line: #2e3744;
  --covered: #86d3a0; --covered-bg: #17321f; --partial: #f0b35c; --partial-bg: #3a2a12;
  --missing: #f19a8c; --missing-bg: #3b1b16; --out: #a8b1be; --out-bg: #232a34; color-scheme: dark }
body { background: var(--bg); color: var(--fg); font: 15px/1.55 var(--f-body);
  padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); }
.wrap { max-width: 1180px; margin: 0 auto; padding-block: 28px 48px; display: grid; gap: 32px; }
.wrap > * { min-width: 0; }
h1 { font: 600 clamp(1.6rem, 3vw, 2.2rem)/1.15 var(--f-display); margin: 0; text-wrap: balance; }
h2 { font: 600 1.2rem/1.3 var(--f-display); margin: 0 0 8px; text-wrap: balance; }
p { margin: 0; }
.lead, .note { color: var(--muted); max-width: 75ch; }
.lead { margin-top: 8px; }
.note { font-size: 0.86rem; margin-top: 8px; }
code { font-family: var(--f-mono); font-size: 0.85em; }
.summary { display: flex; flex-wrap: wrap; gap: 8px 20px; margin-top: 16px; font-variant-numeric: tabular-nums; }
.summary span { display: inline-flex; align-items: center; gap: 8px; }
.diagram, .tbl { background: var(--panel); border: 1px solid var(--line); border-radius: 6px; overflow-x: auto; }
.diagram { padding: 12px; }
.diagram pre { margin: 0; min-width: 900px; }
table { border-collapse: collapse; width: 100%; font-size: 0.9rem; }
th, td { text-align: left; padding: 7px 10px; border-bottom: 1px solid var(--line); vertical-align: top; }
th { font-size: 0.74rem; text-transform: uppercase; letter-spacing: 0.06em; color: var(--muted); font-weight: 600; }
td:first-child { font-family: var(--f-mono); font-size: 0.82rem; white-space: nowrap; }
.pill { font: 600 0.72rem/1 var(--f-mono); padding: 4px 8px; border-radius: 999px; white-space: nowrap; }
.pill.covered { color: var(--covered); background: var(--covered-bg); }
.pill.partial { color: var(--partial); background: var(--partial-bg); }
.pill.missing { color: var(--missing); background: var(--missing-bg); }
.pill.out_of_scope { color: var(--out); background: var(--out-bg); }
</style>

<div class="wrap">
  <header>
    <h1>ISO 29110 a nasz model śladu</h1>
    <p class="lead">Produkty pracy profilu Basic (ISO/IEC 29110-5-1-2) i zależności między nimi, wyprowadzone z wejść i wyjść 72 zadań procesów PM i SI, oraz to, jak pokrywa je model z <code>process/tools/id.toml</code>. Strona jest generowana przez <code>process/tools/iso_map.py</code>; pre-commit pilnuje, żeby nie odbiegała od modelu.</p>
    <div class="summary">{SUMMARY}</div>
  </header>

  <section>
    <h2>Rdzeń zależności</h2>
    <div class="diagram"><pre class="mermaid">
{CORE}
</pre></div>
    <p class="note">{CORE_NOTE}</p>
  </section>

  <section>
    <h2>Produkt po produkcie</h2>
    <div class="tbl">{TABLE}</div>
    <p class="note">Elementy naszego modelu bez osobnego odpowiednika w normie: zasady projektowe (DP), ryzyka produktu (RSK; norma zna tylko ryzyka projektu w planie), kolejka tematów (Q) i ślad na poziomie commitów. Norma traktuje profil Basic jako minimum, więc takie dodatki są z nią zgodne.</p>
  </section>

  <section>
    <h2>Model śladu</h2>
    <p class="note" style="margin:0 0 10px">Strzałka biegnie od dziecka do rodzica, tak jak zapisuje się ją w pliku (P-03); etykieta to pole, w którym dziecko wskazuje rodzica. Kierunek w dół liczy <code>tools/trace.py</code>. Jedyny wyjątek, pole <code>produces</code> zadania, jest przerywane.</p>
    <div class="diagram"><pre class="mermaid">
{MODEL}
</pre></div>
  </section>

  <section>
    <h2>Pełny graf zależności</h2>
    <p class="note" style="margin:0 0 10px">Strzałka biegnie od produktu wejściowego do wyjściowego dowolnego zadania PM lub SI; {EDGES} zależności.</p>
    <div class="diagram"><pre class="mermaid">
{FULL}
</pre></div>
  </section>
</div>
"""


def main(output):
    m = M.Model()
    iso = M.load_toml(os.path.join(M.TOOLS_DIR, "iso29110.toml"))
    wps, edges = iso["wp"], iso["edge"]
    cov = coverage(m, wps)
    counts = {s: sum(1 for c in cov.values() if c[0] == s) for s in ORDER}
    summary = "".join(f'<span><span class="pill {s}">{LABEL[s]}</span> {counts[s]}</span>' for s in ORDER)
    core = [e for e in edges if e["to"] not in SINKS]
    core_ids = {e["from"] for e in core} | {e["to"] for e in core}
    skipped = [wp["id"] for wp in wps if wp["id"] not in core_ids]
    core_note = ("Pominięte krawędzie do produktów, do których prowadzi prawie każde zadanie: "
                 + ", ".join(f"{k} ({v})" for k, v in SINKS.items())
                 + (f". Produkty bez innych zależności: {', '.join(skipped)}." if skipped else ".")
                 + " Wszystkie zależności są na pełnym grafie niżej.")
    page = (PAGE.replace("{SUMMARY}", summary)
            .replace("{CORE}", html.escape(flowchart(wps, core, cov), quote=False))
            .replace("{CORE_NOTE}", html.escape(core_note))
            .replace("{TABLE}", table(wps, cov))
            .replace("{MODEL}", html.escape(trace_model(m), quote=False))
            .replace("{EDGES}", str(len(edges)))
            .replace("{FULL}", html.escape(flowchart(wps, edges, cov), quote=False)))
    with open(M.output_path(m.root, output), "w", encoding="utf-8") as f:
        f.write(page)
    print("iso_map.py: " + " · ".join(f"{LABEL[s]} {counts[s]}" for s in ORDER))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else os.path.join("reports", "iso-map.html")))
