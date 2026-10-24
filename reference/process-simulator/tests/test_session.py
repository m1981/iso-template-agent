import json
import unittest

from app.engine import Refused, initial_state, transition
from app.session import at_step, export_session, import_session
from test_engine import TO_DEMO, walk


class SessionContract(unittest.TestCase):
    def test_roundtrip_including_note_cursor_and_relations(self):
        state = transition(walk(*TO_DEMO), "accept", "Rozumiem wynik.")
        saved = json.loads(json.dumps(export_session(state, 5)))
        restored, cursor = import_session(saved)
        self.assertEqual(restored, state)
        self.assertEqual(cursor, 5)
        self.assertTrue(saved["simulated"])
        self.assertNotIn("products", saved)

    def test_historical_view_has_no_future_products(self):
        state = walk(*TO_DEMO)
        before = at_step(state, 5)
        self.assertIsNotNone(before.latest("T5"))
        self.assertIsNone(before.latest("RUN1"))
        self.assertEqual(len(state.events), 11)
        self.assertEqual(at_step(state, 0), initial_state())

    def test_invalid_version_fields_commands_cursor_and_payload_are_rejected(self):
        good = export_session(walk(*TO_DEMO))
        variants = [None, [], {}, good | {"format_version": 99},
                    good | {"format_version": True}, good | {"lesson_version": 2},
                    good | {"lesson_id": "other"}, good | {"simulated": False},
                    good | {"cursor": -1}, good | {"cursor": True},
                    good | {"cursor": 999}, good | {"extra": "ignored?"},
                    good | {"commands": "scope"},
                    good | {"commands": [{"action": "accept", "note": "pass"}], "cursor": 1},
                    good | {"commands": [{"action": "scope", "note": "", "result": "PASS"}], "cursor": 1},
                    good | {"commands": [{"action": [], "note": ""}], "cursor": 1}]
        for invalid in variants:
            with self.subTest(invalid=invalid):
                with self.assertRaises(Refused):
                    import_session(invalid)
        self.assertEqual(good, export_session(walk(*TO_DEMO)))

    def test_all_prefixes_replay_deterministically(self):
        state = walk(*TO_DEMO)
        for cursor in range(len(state.events) + 1):
            prefix = at_step(state, cursor)
            self.assertEqual(import_session(export_session(prefix))[0], prefix)
