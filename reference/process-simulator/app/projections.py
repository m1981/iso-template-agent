"""Three projections of one immutable history; no independent view state."""
from dataclasses import asdict

from app.engine import ACTIONS, NOTE_ACTIONS, reason
from app.session import at_step

GROUPS = {"context": 0, "requirement": 1, "plan": 1, "design": 2, "review": 2,
          "test": 2, "code": 3, "run": 3, "usage": 4, "demo": 4, "decision": 4}


def project(state, cursor=None, version=0):
    cursor = len(state.events) if cursor is None else cursor
    shown = at_step(state, cursor)
    read_only = cursor != len(state.events)
    cards = []
    for product in shown.products:
        card = asdict(product) | {"key": product.ref.key,
                                   "current": product == shown.latest(product.id)}
        card["links"] = [{"key": ref.key, "title": shown.get(ref).title} for ref in product.links]
        card["used_by"] = [{"key": other.ref.key, "title": other.title} for other in shown.products
                           if product.ref in other.links]
        cards.append(card)
    nodes = {}
    for product in shown.products:
        group = nodes.setdefault(product.path, {"id": product.path, "title": "Raporty testów" if product.path == "reports/tests.md" else product.container,
                                                "wp": product.wp, "column": GROUPS[product.kind], "cards": []})
        group["cards"].append(product.ref.key)
    edges = sorted({(shown.get(ref).path, product.path)
                    for product in shown.products for ref in product.links
                    if shown.get(ref).path != product.path})
    actions = []
    for spec in ACTIONS:
        refusal = "Oglądasz historię. Wróć do bieżącego kroku, aby działać." if read_only else reason(shown, spec.id)
        actions.append({"id": spec.id, "title": spec.title, "phase": spec.phase, "actor": spec.actor,
                        "enabled": not refusal, "reason": refusal or spec.why,
                        "needs_note": spec.id in NOTE_ACTIONS,
                        "done": any(e.action == spec.id for e in shown.events)})
    specs = {a.id: a for a in ACTIONS}
    history = [{"step": i, "title": specs[event.action].title,
                "actor": specs[event.action].actor, "note": event.note,
                "outputs": [ref.key for ref in event.outputs]}
               for i, event in enumerate(state.events, 1)]
    return {"lesson": state.lesson.id, "lesson_version": state.lesson.version, "simulated": True,
            "version": version, "cursor": cursor, "total": len(state.events), "read_only": read_only,
            "cards": cards, "nodes": list(nodes.values()), "edges": edges,
            "actions": actions, "history": history,
            "accepted": shown.latest("ACC1") is not None, "release_ready": False,
            "open_questions": ["Q1: kontrakt błędu odczytu — do ustalenia przed wydaniem."]
            if shown.latest("Q1") else []}
