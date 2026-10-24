"""Pure transitions: guards and execution share one rule per command."""
from dataclasses import dataclass
from app.lesson import load_lesson
from app.model import Event, Product, Ref, State


class Refused(ValueError):
    """An explained refusal which leaves the original state intact."""


@dataclass(frozen=True)
class Action:
    id: str
    title: str
    phase: str
    actor: str
    requires: tuple[str, ...]
    creates: tuple[str, ...]
    why: str


ACTIONS = (
    Action("scope", "Uzgodnij zakres w fabule", "Potrzeba", "Odbiorca w fabule", ("N1",),
           ("SCOPE", "G1", "R1", "R1a", "R2", "Q1"), "Najpierw ustalamy znaczenie i granice."),
    Action("plan", "Przygotuj plan I1", "Planowanie", "Zespół w fabule", ("R1", "R1a", "R2"),
           ("P1",), "Plan opisuje zamiar przed wykonaniem."),
    Action("design", "Zaprojektuj kontrakty C1/C2", "Projekt", "Zespół w fabule", ("R1", "R2"),
           ("C1", "C2"), "Oddzielamy obliczenie i adapter."),
    Action("review", "Przejrzyj wymagania i projekt", "Przegląd", "Recenzent w fabule", ("P1", "C1", "C2"),
           ("V1",), "Przegląd przed kodem; zapis nie jest testem."),
    Action("tests", "Przygotuj przypadki T1–T5", "Testy", "Zespół w fabule", ("V1",),
           ("T1", "T2", "T3", "T4", "T5"), "Przypadek opisuje oczekiwanie, nie wynik."),
)

ACTIONS += (
    Action("red", "Uruchom próbę na szkielecie", "RED", "Zespół w fabule", ("T1", "T2", "T3", "T4", "T5"),
           ("CODE1-stub", "RUN1"), "Odtwarzamy niepowodzenie, nie wykonujemy prawdziwego kodu."),
    Action("implement", "Zaimplementuj obliczenie", "Kod", "Zespół w fabule", ("RUN1",),
           ("CODE1-done",), "Nowy kod wymaga nowej próby."),
    Action("unit", "Ponów testy jednostkowe", "GREEN", "Zespół w fabule", ("CODE1",),
           ("RUN2",), "Sprawdzamy poprawioną rewizję obliczenia."),
    Action("integrate", "Dołącz adapter CLI", "Integracja", "Zespół w fabule", ("RUN2",),
           ("CODE2",), "Wynik jednostkowy nie potwierdza jeszcze integracji."),
    Action("integration", "Sprawdź integrację T5", "Integracja", "Zespół w fabule", ("CODE2", "T5"),
           ("RUN3",), "Sprawdzamy plik, JSON, kod wyjścia i niezmienność wejścia."),
    Action("demo", "Przeprowadź demonstrację", "Demonstracja", "Odbiorca w fabule", ("RUN2", "RUN3"),
           ("DEMO1",), "Ocena przydatności jest osobnym krokiem."),
    Action("accept", "Odbierz I1 w fabule", "Odbiór", "Odbiorca w fabule", ("DEMO1",),
           ("ACC1",), "Podaj ocenę przydatności; Q1 pozostaje otwarte."),
    Action("reject", "Zgłoś korektę instrukcji", "Odbiór", "Odbiorca w fabule", ("DEMO1",),
           ("DEC1",), "Podaj, co w objaśnieniu wymaga korekty. Zmiana zakresu jest poza I1."),
    Action("clarify", "Popraw objaśnienie użycia", "Korekta", "Zespół w fabule", ("DEC1",),
           ("U1",), "Zapisz konkretne doprecyzowanie instrukcji; potem ponów demonstrację."),
)
MAX_EVENTS = 200
NOTE_ACTIONS = {"accept", "reject", "clarify"}
REPEATABLE = {"demo", "reject", "clarify"}


def current_run(state, identifier):
    run = state.latest(identifier)
    return bool(run and run.outcome == "PASS" and
                all(state.latest(ref.id).ref == ref for ref in run.links))


def linked_revision(product, identifier):
    return next(ref.revision for ref in product.links if ref.id == identifier)


def add_product(state, key, note=""):
    content = state.lesson.content(key)
    previous = state.latest(content.id)
    links = tuple(Ref(id, state.latest(id).revision) for id in content.links)
    product = Product(content.id, previous.revision + 1 if previous else 1,
                      content.kind, content.title, content.body + ("\n\n" + note if note else ""),
                      content.wp, content.path, content.container, content.why, links, content.outcome)
    return State(state.lesson, state.products + (product,), state.events)


def initial_state(lesson=None):
    return add_product(State(lesson or load_lesson()), "N1")


def reason(state, action):
    if action not in {a.id for a in ACTIONS}:
        return "Nieznane działanie."
    if len(state.events) >= MAX_EVENTS:
        return "Osiągnięto limit 200 kroków tej lekcji. Zapisz sesję; dalsza praca wymaga nowego ćwiczenia."
    if state.latest("ACC1"):
        return "Przyrost odebrany w fabule. Ćwiczenie zakończone; wydanie nadal czeka na Q1."
    spec = next(a for a in ACTIONS if a.id == action)
    if action not in REPEATABLE and any(e.action == action for e in state.events):
        return "To działanie zostało już wykonane."
    missing = [id for id in spec.requires if state.latest(id) is None]
    if missing:
        return "Brakuje podstawy: " + ", ".join("przegląd V1" if id == "V1" else id for id in missing)
    if action == "unit" and state.latest("CODE1").revision != 2:
        return "Najpierw popraw obliczenie po RED."
    if action in {"integrate", "integration", "demo"} and not current_run(state, "RUN2"):
        return "Brakuje aktualnego wyniku testów jednostkowych."
    if action == "demo" and not current_run(state, "RUN3"):
        return "Brakuje aktualnego wyniku integracji."
    demo, rejection, usage = (state.latest(id) for id in ("DEMO1", "DEC1", "U1"))
    if action == "demo" and demo and linked_revision(demo, "U1") == usage.revision:
        return "Ta instrukcja była już demonstrowana; najpierw zgłoś i wykonaj korektę."
    if action in {"accept", "reject"} and rejection:
        if linked_revision(rejection, "DEMO1") == demo.revision:
            return "Po odmowie potrzebna jest korekta i nowa demonstracja."
    if action == "clarify" and linked_revision(rejection, "U1") != usage.revision:
        return "Korekta została już zapisana; teraz ponów demonstrację."
    return ""


def transition(state, action, note=""):
    if not isinstance(action, str) or not isinstance(note, str):
        raise Refused("Polecenie i opis muszą być tekstem.")
    if len(note) > 2000:
        raise Refused("Opis może mieć najwyżej 2000 znaków.")
    if action in NOTE_ACTIONS and not note.strip():
        raise Refused("Podaj uzasadnienie lub opis korekty; milczenie nie jest decyzją.")
    if action not in NOTE_ACTIONS and note:
        raise Refused("To polecenie nie przyjmuje opisu.")
    refusal = reason(state, action)
    if refusal:
        raise Refused(refusal)
    spec = next(a for a in ACTIONS if a.id == action)
    result = state
    outputs = []
    if action == "demo" and state.latest("U1") is None:
        result = add_product(result, "U1")
        outputs.append(result.products[-1].ref)
    for key in spec.creates:
        result = add_product(result, key, note)
        outputs.append(result.products[-1].ref)
    return State(result.lesson, result.products,
                 state.events + (Event(action, note, tuple(outputs)),))
