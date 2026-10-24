"""Replay commands, never trust imported statuses or work-product contents."""
from app.engine import MAX_EVENTS, Refused, initial_state, transition

FORMAT_VERSION = 1
MAX_COMMANDS = MAX_EVENTS
FIELDS = {"format_version", "lesson_id", "lesson_version", "simulated", "commands", "cursor"}


def valid_cursor(cursor, length):
    if type(cursor) is not int or not 0 <= cursor <= length:
        raise Refused("Kursor historii jest poza zakresem.")


def at_step(state, cursor):
    valid_cursor(cursor, len(state.events))
    result = initial_state(state.lesson)
    for event in state.events[:cursor]:
        result = transition(result, event.action, event.note)
    return result


def export_session(state, cursor=None):
    cursor = len(state.events) if cursor is None else cursor
    valid_cursor(cursor, len(state.events))
    return {"format_version": FORMAT_VERSION, "lesson_id": state.lesson.id,
            "lesson_version": state.lesson.version, "simulated": True,
            "commands": [{"action": e.action, "note": e.note} for e in state.events],
            "cursor": cursor}


def import_session(data):
    if type(data) is not dict or set(data) != FIELDS:
        raise Refused("Nieprawidłowe pola zapisu sesji.")
    state = initial_state()
    if type(data["format_version"]) is not int or data["format_version"] != FORMAT_VERSION:
        raise Refused("Nieobsługiwana wersja zapisu.")
    if (data["lesson_id"] != state.lesson.id or type(data["lesson_version"]) is not int
            or data["lesson_version"] != state.lesson.version or data["simulated"] is not True):
        raise Refused("Zapis nie pasuje do wersji tej lekcji symulacyjnej.")
    commands = data["commands"]
    if type(commands) is not list or len(commands) > MAX_COMMANDS:
        raise Refused("Nieprawidłowa lista poleceń (limit 200).")
    valid_cursor(data["cursor"], len(commands))
    for index, command in enumerate(commands, 1):
        if type(command) is not dict or set(command) != {"action", "note"}:
            raise Refused(f"Nieprawidłowe pola polecenia {index}.")
        try:
            state = transition(state, command["action"], command["note"])
        except Refused as error:
            raise Refused(f"Krok {index}: {error}") from error
    return state, data["cursor"]
