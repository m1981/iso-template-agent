"""Behavioral oracle derived from scenario.md, not available-action output."""
import unittest

from app.engine import Refused, initial_state, transition


def walk(*actions):
    state = initial_state()
    for action in actions:
        state = transition(state, action)
    return state


PREPARE = ("scope", "plan", "design", "review", "tests")


class FirstSlice(unittest.TestCase):
    def test_test_cases_are_not_test_executions(self):
        state = walk(*PREPARE)
        self.assertEqual({p.id for p in state.products if p.kind == "test"},
                         {"T1", "T2", "T3", "T4", "T5"})
        self.assertFalse(any(p.kind == "run" for p in state.products))
        self.assertFalse(any(p.id == "ACC1" for p in state.products))

    def test_plan_and_design_can_be_created_in_either_order(self):
        state = walk("scope", "design", "plan", "review", "tests")
        self.assertEqual({p.id for p in state.products},
                         {p.id for p in walk(*PREPARE).products})

    def test_cannot_test_without_review(self):
        state = walk("scope", "plan", "design")
        before = repr(state)
        with self.assertRaisesRegex(Refused, "przegląd"):
            transition(state, "tests")
        self.assertEqual(repr(state), before)

    def test_duplicate_scope_is_an_atomic_refusal(self):
        state = walk("scope")
        with self.assertRaises(Refused):
            transition(state, "scope")
        self.assertEqual(len(state.events), 1)


TO_DEMO = PREPARE + ("red", "implement", "unit", "integrate", "integration", "demo")


class FullLesson(unittest.TestCase):
    def test_red_and_green_reference_different_code_revisions(self):
        red = walk(*PREPARE, "red")
        green = walk(*TO_DEMO)
        self.assertEqual(red.latest("RUN1"), green.latest("RUN1"))
        self.assertEqual(green.latest("RUN1").outcome, "FAIL")
        self.assertEqual(green.latest("RUN2").outcome, "PASS")
        self.assertIn(green.latest("CODE1").ref, green.latest("RUN2").links)
        self.assertNotIn(green.latest("CODE1").ref, green.latest("RUN1").links)
        self.assertEqual(red.latest("CODE1").revision, 1)
        self.assertEqual(green.latest("CODE1").revision, 2)
        self.assertTrue(all(p.simulated for p in green.products))

    def test_green_unit_tests_are_not_integration_or_acceptance(self):
        state = walk(*PREPARE, "red", "implement", "unit")
        self.assertIsNone(state.latest("RUN3"))
        self.assertIsNone(state.latest("ACC1"))
        with self.assertRaises(Refused):
            transition(state, "demo")

    def test_accept_requires_demonstration_and_explicit_reason(self):
        state = walk(*TO_DEMO[:-1])
        with self.assertRaises(Refused):
            transition(state, "accept", "Wygląda dobrze")
        state = transition(state, "demo")
        with self.assertRaises(Refused):
            transition(state, "accept")
        accepted = transition(state, "accept", "Rozumiem wynik dla poprawnego pliku.")
        self.assertIsNotNone(accepted.latest("ACC1"))
        self.assertIsNotNone(accepted.latest("Q1"))
        self.assertIn(state.latest("DEMO1").ref, accepted.latest("ACC1").links)
        with self.assertRaises(Refused):
            transition(accepted, "reject", "Zmiana zdania")

    def test_rejection_requires_correction_then_new_demonstration(self):
        demo = walk(*TO_DEMO)
        rejected = transition(demo, "reject", "Wyjaśnij interpunkcję w instrukcji.")
        self.assertIsNone(rejected.latest("ACC1"))
        self.assertIn("interpunkcję", rejected.latest("DEC1").body)
        with self.assertRaises(Refused):
            transition(rejected, "accept", "Jednak dobrze")
        with self.assertRaises(Refused):
            transition(rejected, "demo")
        corrected = transition(rejected, "clarify", "Ala,kot to jedno słowo; Ala, kot to dwa.")
        with self.assertRaises(Refused):
            transition(corrected, "accept", "Gotowe")
        ready = transition(corrected, "demo")
        self.assertEqual(ready.latest("U1").revision, 2)
        self.assertEqual(ready.latest("DEMO1").revision, 2)
        self.assertIn(ready.latest("U1").ref, ready.latest("DEMO1").links)
        accepted = transition(ready, "accept", "Instrukcja jest jasna.")
        self.assertEqual(accepted.latest("DEC1"), rejected.latest("DEC1"))

    def test_all_links_resolve_and_history_remains_immutable(self):
        state = walk(*TO_DEMO)
        for product in state.products:
            for ref in product.links:
                self.assertEqual(state.get(ref).ref, ref)
        with self.assertRaises((AttributeError, TypeError)):
            state.products[0].body = "changed"
        with self.assertRaises(Refused):
            transition(state, "unknown")

    def test_integration_binds_test_requirements_and_both_components(self):
        state = walk(*TO_DEMO)
        self.assertEqual({ref.id for ref in state.latest("RUN3").links},
                         {"T5", "CODE1", "CODE2", "R1", "R2"})
        self.assertEqual(state.latest("RUN3").outcome, "PASS")


class SessionLimits(unittest.TestCase):
    def test_every_allowed_session_fits_the_replay_limit(self):
        state = walk(*TO_DEMO)
        # Repeated clarification is allowed, but a valid export must remain importable.
        from app.session import MAX_COMMANDS, export_session, import_session
        for index in range(len(state.events), MAX_COMMANDS):
            action = ('reject', 'clarify', 'demo')[(index - len(TO_DEMO)) % 3]
            state = transition(state, action, 'Doprecyzowanie w fabule.' if action != 'demo' else '')
        self.assertEqual(import_session(export_session(state))[0], state)
        with self.assertRaisesRegex(Refused, 'limit'):
            transition(state, 'reject', 'Kolejna prośba o korektę.')


if __name__ == "__main__":
    unittest.main()
