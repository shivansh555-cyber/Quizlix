"""
quiz_manager.py
----------------
CRUD (Create, Read, Update, Delete) operations for quizzes.
A quiz itself only stores basic info + a list of question IDs that belong
to it. The actual question text lives in questions.json (see
question_bank.py) so that one question could, in theory, be reused by
more than one quiz.
"""

from src import data_manager
from src import validators

QUIZZES_FILE = "quizzes.json"


def list_quizzes():
    return data_manager.load_json(QUIZZES_FILE)


def get_quiz(quiz_id):
    """Return the quiz dictionary matching quiz_id, or None."""
    for quiz in list_quizzes():
        if quiz["quiz_id"] == quiz_id:
            return quiz
    return None


def create_quiz(quiz_id, title, category):
    """
    Add a new quiz. Returns (True, message) or (False, reason).
    New quizzes start with an empty question list; questions are attached
    afterwards using question_bank.add_question().
    """
    quizzes = list_quizzes()
    new_quiz = {"quiz_id": quiz_id, "title": title, "category": category, "questions": []}

    is_valid, reason = validators.is_valid_quiz(new_quiz)
    if not is_valid:
        return False, reason
    if not validators.is_unique_id(quizzes, "quiz_id", quiz_id):
        return False, f"Quiz ID {quiz_id} is already used."

    quizzes.append(new_quiz)
    data_manager.save_json(QUIZZES_FILE, quizzes)
    return True, f"Quiz '{title}' created with ID {quiz_id}."


def update_quiz(quiz_id, new_title=None, new_category=None):
    """Update the title and/or category of an existing quiz."""
    quizzes = list_quizzes()
    for quiz in quizzes:
        if quiz["quiz_id"] == quiz_id:
            if new_title:
                quiz["title"] = new_title
            if new_category:
                quiz["category"] = new_category
            data_manager.save_json(QUIZZES_FILE, quizzes)
            return True, "Quiz updated."
    return False, f"No quiz found with ID {quiz_id}."


def delete_quiz(quiz_id):
    """Remove a quiz completely."""
    quizzes = list_quizzes()
    remaining = [quiz for quiz in quizzes if quiz["quiz_id"] != quiz_id]

    if len(remaining) == len(quizzes):
        return False, f"No quiz found with ID {quiz_id}."

    data_manager.save_json(QUIZZES_FILE, remaining)
    return True, "Quiz deleted."


def attach_question(quiz_id, question_id):
    """Add a question_id to a quiz's list of questions (no duplicates)."""
    quizzes = list_quizzes()
    for quiz in quizzes:
        if quiz["quiz_id"] == quiz_id:
            if question_id not in quiz["questions"]:
                quiz["questions"].append(question_id)
                data_manager.save_json(QUIZZES_FILE, quizzes)
            return True
    return False
