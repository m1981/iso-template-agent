"""Read bundled content at initialization; never evaluate lesson data as code."""
import json
from pathlib import Path
from app.model import Content, Kind, Lesson


def load_lesson():
    path = Path(__file__).resolve().parent.parent / "lessons" / "textstats-i1.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    contents = tuple(Content(**(item | {"kind": Kind(item["kind"]),
                                       "links": tuple(item.get("links", ())) }))
                     for item in data["contents"])
    return Lesson(data["id"], data["version"], contents)
