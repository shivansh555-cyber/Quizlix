"""
validators.py
--------------
Small, focused functions that check whether data is valid BEFORE we try
to use or save it. Keeping validation separate from the "business logic"
(auth, quizzes, questions) makes each function easy to test on its own.

Concepts used: functions, conditionals (if/elif/else), booleans, loops,
lists, sets (for duplicate checking).
"""


def is_non_empty(value):
    """Return True if value is a non-empty string once spaces are trimmed."""
    return isinstance(value, str) and len(value.strip()) > 0


def username_exists(users, username):
    """
    Return True if a user with this username already exists.
    'users' is a list of user dictionaries, e.g. {"username": ..., ...}.
    """
    for user in users:
        if user["username"].lower() == username.lower():
            return True
    return False


def is_valid_registration(users, username, password, role):
    """
    Check that a new registration is acceptable.
    Returns (True, "") if valid, otherwise (False, "reason").
    """
    if not is_non_empty(username):
        return False, "Username cannot be empty."
    if not is_non_empty(password):
        return False, "Password cannot be empty."
    if role not in ("student", "admin"):
        return False, "Role must be 'student' or 'admin'."
    if username_exists(users, username):
        return False, "This username is already taken."
    return True, ""


def is_unique_id(items, id_field, new_id):
    """
    Check that new_id does not already exist among items (quizzes or
    questions), where each item is a dictionary containing id_field.
    """
    existing_ids = set(item[id_field] for item in items)
    return new_id not in existing_ids


def is_valid_quiz(quiz):
    """A quiz must have a title and a positive integer quiz_id."""
    if not is_non_empty(quiz.get("title", "")):
        return False, "Quiz title cannot be empty."
    if not isinstance(quiz.get("quiz_id"), int) or quiz["quiz_id"] <= 0:
        return False, "Quiz ID must be a positive whole number."
    return True, ""


def is_valid_mcq(question):
    """
    A multiple-choice question must have:
      - non-empty question text
      - at least 2 options
      - an answer that is exactly one of those options
    """
    text = question.get("question", "")
    options = question.get("options", [])
    answer = question.get("answer", "")

    if not is_non_empty(text):
        return False, "Question text cannot be empty."
    if not isinstance(options, list) or len(options) < 2:
        return False, "A question needs at least 2 options."
    if answer not in options:
        return False, "The correct answer must be one of the given options."
    return True, ""
