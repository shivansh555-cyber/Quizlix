"""
test_results.py
-----------------
Unit tests for saving results and reading back a student's history.
Uses a throwaway results file so the real results.json is never touched
while running tests.
"""

import unittest
from src import result_manager
import src.data_manager as data_manager


class TestResults(unittest.TestCase):

    def setUp(self):
        self.original_file = result_manager.RESULTS_FILE
        result_manager.RESULTS_FILE = "test_results_tmp.json"
        data_manager.save_json(result_manager.RESULTS_FILE, [])

    def tearDown(self):
        path = data_manager.DATA_DIR / result_manager.RESULTS_FILE
        if path.exists():
            path.unlink()
        result_manager.RESULTS_FILE = self.original_file

    def test_save_result_adds_one_record(self):
        result_manager.save_result("bob", 1, "Python Basics", 7, 10, 70.0)
        all_results = result_manager.get_all_results()
        self.assertEqual(len(all_results), 1)
        self.assertEqual(all_results[0]["username"], "bob")
        self.assertEqual(all_results[0]["percentage"], 70.0)

    def test_history_only_returns_matching_user(self):
        result_manager.save_result("bob", 1, "Python Basics", 7, 10, 70.0)
        result_manager.save_result("alice", 1, "Python Basics", 9, 10, 90.0)

        bob_history = result_manager.get_history("bob")
        self.assertEqual(len(bob_history), 1)
        self.assertEqual(bob_history[0]["username"], "bob")

    def test_history_is_empty_for_unknown_user(self):
        history = result_manager.get_history("nobody")
        self.assertEqual(history, [])

    def test_most_recent_attempt_appears_first(self):
        result_manager.save_result("bob", 1, "Python Basics", 5, 10, 50.0)
        result_manager.save_result("bob", 2, "Data Types", 8, 10, 80.0)

        history = result_manager.get_history("bob")
        self.assertEqual(history[0]["quiz_title"], "Data Types")


if __name__ == "__main__":
    unittest.main()
