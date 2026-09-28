"""
test_auth.py
-------------
Unit tests for registration and login rules. We do NOT touch the real
data/users.json here -- each test builds its own small in-memory list of
users so tests stay fast and never mess up real project data.

Run all tests with:
    python -m unittest discover -s tests -p "test_*.py"
"""

import unittest
from src import validators
from src import auth
import src.data_manager as data_manager


class TestValidators(unittest.TestCase):

    def setUp(self):
        self.users = [
            {"username": "student01", "password": "1234", "role": "student"},
        ]

    def test_valid_registration_is_accepted(self):
        ok, reason = validators.is_valid_registration(self.users, "newstudent", "pass", "student")
        self.assertTrue(ok)
        self.assertEqual(reason, "")

    def test_duplicate_username_is_rejected(self):
        ok, reason = validators.is_valid_registration(self.users, "student01", "pass", "student")
        self.assertFalse(ok)

    def test_empty_username_is_rejected(self):
        ok, reason = validators.is_valid_registration(self.users, "   ", "pass", "student")
        self.assertFalse(ok)

    def test_empty_password_is_rejected(self):
        ok, reason = validators.is_valid_registration(self.users, "someone", "", "student")
        self.assertFalse(ok)


class TestLogin(unittest.TestCase):
    """
    These tests temporarily point auth.py at a throwaway test file
    (test_users_tmp.json) instead of the real users.json, so running the
    test suite never changes real project data.
    """

    def setUp(self):
        self.original_file = auth.USERS_FILE
        auth.USERS_FILE = "test_users_tmp.json"
        data_manager.save_json(auth.USERS_FILE, [
            {"username": "alice", "password": "secret", "role": "student"},
            {"username": "admin01", "password": "admin123", "role": "admin"},
        ])

    def tearDown(self):
        path = data_manager.DATA_DIR / auth.USERS_FILE
        if path.exists():
            path.unlink()
        auth.USERS_FILE = self.original_file

    def test_correct_login_succeeds(self):
        user = auth.login("alice", "secret", expected_role="student")
        self.assertIsNotNone(user)
        self.assertEqual(user["username"], "alice")

    def test_wrong_password_fails(self):
        user = auth.login("alice", "wrongpass", expected_role="student")
        self.assertIsNone(user)

    def test_wrong_role_fails(self):
        # alice is a student, so logging in as admin should fail
        user = auth.login("alice", "secret", expected_role="admin")
        self.assertIsNone(user)


if __name__ == "__main__":
    unittest.main()
