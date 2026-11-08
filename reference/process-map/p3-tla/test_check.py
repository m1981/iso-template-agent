"""Protect evidence classification against false success (stdlib only)."""
import unittest
from check import classify


class ClassificationTests(unittest.TestCase):
    def test_completed_safety_check(self):
        self.assertEqual(classify(0, 'Model checking completed. No error has been found.', None), 'bounded_pass')

    def test_zero_exit_without_completion_is_not_success(self):
        self.assertEqual(classify(0, 'Parsing completed', None), 'unexpected_result')

    def test_surviving_mutant_is_failure(self):
        self.assertEqual(classify(0, 'Model checking completed. No error has been found.', 'V3_SingleCompletion'), 'unexpected_result')

    def test_expected_semantic_counterexample(self):
        text = 'Error: Invariant V3_SingleCompletion is violated.\nThe behavior up to this point is:'
        self.assertEqual(classify(12, text, 'V3_SingleCompletion'), 'expected_counterexample')

    def test_wrong_invariant_does_not_kill_mutant(self):
        text = 'Error: Invariant V1_TypedAndBound is violated.\nThe behavior up to this point is:'
        self.assertEqual(classify(12, text, 'V3_SingleCompletion'), 'unexpected_result')

    def test_parser_or_runtime_failure_is_not_a_counterexample(self):
        self.assertEqual(classify(150, 'Error: Parsing or semantic analysis failed.', 'NotGoal'), 'unexpected_result')

    def test_missing_trace_is_not_a_witness(self):
        self.assertEqual(classify(12, 'Error: Invariant NotGoal is violated.', 'NotGoal'), 'unexpected_result')

    def test_nonzero_exit_is_not_safety_success(self):
        self.assertEqual(classify(1, 'Model checking completed. No error has been found.', None), 'unexpected_result')


if __name__ == '__main__':
    unittest.main()
