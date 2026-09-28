"""
question_bank.py
-----------------
CRUD operations for individual multiple-choice questions, and helper
functions to fetch all questions that belong to a given quiz.
"""

from src import data_manager
from src import validators
from src import quiz_manager

QUESTIONS_FILE = "questions.json"


def list_questions():
    return data_manager.load_json(QUESTIONS_FILE)


def get_questions_for_quiz(quiz_id):
    """
    Return the full question dictionaries for every question_id listed
    inside the given quiz. This is how quiz_engine.py gets the actual
    questions to ask the student.
    """
    quiz = quiz_manager.get_quiz(quiz_id)
    if quiz is None:
        return []

    all_questions = list_questions()
    wanted_ids = quiz["questions"]
    return [q for q in all_questions if q["question_id"] in wanted_ids]


def add_question(question_id, quiz_id, text, options, answer, difficulty="easy"):
    """
    Add a new MCQ to the question bank and attach it to a quiz.
    Returns (True, message) or (False, reason).
    """
    questions = list_questions()
    new_question = {
        "question_id": question_id,
        "quiz_id": quiz_id,
        "question": text,
        "options": options,
        "answer": answer,
        "difficulty": difficulty,
    }

    is_valid, reason = validators.is_valid_mcq(new_question)
    if not is_valid:
        return False, reason
    if not validators.is_unique_id(questions, "question_id", question_id):
        return False, f"Question ID {question_id} is already used."
    if quiz_manager.get_quiz(quiz_id) is None:
        return False, f"No quiz found with ID {quiz_id}. Create the quiz first."

    questions.append(new_question)
    data_manager.save_json(QUESTIONS_FILE, questions)
    quiz_manager.attach_question(quiz_id, question_id)
    return True, f"Question {question_id} added to quiz {quiz_id}."


def update_question(question_id, **changes):
    """Update one or more fields (question/options/answer/difficulty) of a question."""
    questions = list_questions()
    for question in questions:
        if question["question_id"] == question_id:
            question.update(changes)
            data_manager.save_json(QUESTIONS_FILE, questions)
            return True, "Question updated."
    return False, f"No question found with ID {question_id}."


def delete_question(question_id):
    """Remove a question from the bank."""
    questions = list_questions()
    remaining = [q for q in questions if q["question_id"] != question_id]

    if len(remaining) == len(questions):
        return False, f"No question found with ID {question_id}."

    data_manager.save_json(QUESTIONS_FILE, remaining)
    return True, "Question deleted."
