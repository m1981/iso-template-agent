"""Immutable domain records. Collections remain immutable across revisions."""
from dataclasses import dataclass
from enum import Enum


class Kind(str, Enum):
    CONTEXT = "context"
    REQUIREMENT = "requirement"
    PLAN = "plan"
    DESIGN = "design"
    REVIEW = "review"
    TEST = "test"
    CODE = "code"
    RUN = "run"
    USAGE = "usage"
    DEMO = "demo"
    DECISION = "decision"


@dataclass(frozen=True)
class Ref:
    id: str
    revision: int

    @property
    def key(self):
        return f"{self.id}@{self.revision}"


@dataclass(frozen=True)
class Content:
    key: str
    id: str
    kind: Kind
    title: str
    body: str
    wp: str
    path: str
    container: str
    why: str
    links: tuple[str, ...] = ()
    outcome: str = ""


@dataclass(frozen=True)
class Lesson:
    id: str
    version: int
    contents: tuple[Content, ...]

    def content(self, key):
        return next(c for c in self.contents if c.key == key)


@dataclass(frozen=True)
class Product:
    id: str
    revision: int
    kind: Kind
    title: str
    body: str
    wp: str
    path: str
    container: str
    why: str
    links: tuple[Ref, ...] = ()
    outcome: str = ""
    simulated: bool = True

    @property
    def ref(self):
        return Ref(self.id, self.revision)


@dataclass(frozen=True)
class Event:
    action: str
    note: str
    outputs: tuple[Ref, ...]


@dataclass(frozen=True)
class State:
    lesson: Lesson
    products: tuple[Product, ...] = ()
    events: tuple[Event, ...] = ()

    def latest(self, identifier):
        return next((p for p in reversed(self.products) if p.id == identifier), None)

    def get(self, ref):
        return next(p for p in self.products if p.ref == ref)
