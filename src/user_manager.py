"""
user_manager.py
----------------
Small helper functions for looking up and listing users, used by the
admin menu and by other modules that need user information but should
not need to know HOW users are stored.
"""

from src import data_manager

USERS_FILE = "users.json"


def get_user(username):
    """Return the user dictionary for this username, or None if not found."""
    users = data_manager.load_json(USERS_FILE)
    for user in users:
        if user["username"].lower() == username.lower():
            return user
    return None


def list_students():
    """Return a list of usernames for all users with role 'student'."""
    users = data_manager.load_json(USERS_FILE)
    return [user["username"] for user in users if user["role"] == "student"]


def total_users():
    """Return how many accounts exist in total."""
    return len(data_manager.load_json(USERS_FILE))
