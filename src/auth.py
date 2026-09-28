"""
auth.py
-------
Handles everything related to a person proving who they are:
registering a new account and logging in to an existing one.

This module does NOT read or write files directly -- it always goes
through data_manager.py, and it does NOT decide if input is valid on its
own -- it asks validators.py. This separation (top-down design) keeps
each file responsible for exactly one job.
"""

from src import data_manager
from src import validators

USERS_FILE = "users.json"


def load_users():
    return data_manager.load_json(USERS_FILE)


def register(username, password, role):
    """
    Try to create a new account.
    Returns (True, "Success message") or (False, "Reason it failed").
    """
    users = load_users()

    is_valid, reason = validators.is_valid_registration(users, username, password, role)
    if not is_valid:
        return False, reason

    new_user = {
        "username": username.strip(),
        "password": password,
        "role": role,
    }
    users.append(new_user)
    data_manager.save_json(USERS_FILE, users)
    return True, f"Account created for '{username}'. You can now log in."


def login(username, password, expected_role=None):
    """
    Check username + password against stored users.
    If expected_role is given (e.g. "admin"), the user's role must match it.
    Returns the user dictionary on success, or None on failure.
    """
    users = load_users()

    for user in users:
        same_username = user["username"].lower() == username.lower()
        same_password = user["password"] == password
        if same_username and same_password:
            if expected_role is not None and user["role"] != expected_role:
                return None
            return user

    return None
