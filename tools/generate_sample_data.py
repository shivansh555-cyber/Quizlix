"""
generate_sample_data.py
--------------------------
Run this once to fill data/ with a realistic DEMO dataset so the project
has something to show immediately: 3 users, 2 quizzes, 12 questions and a
few past results. All data here is fictional -- never put real student
credentials in this file or in the GitHub repository.

Run from the project's root folder with:
    python tools/generate_sample_data.py
"""

import sys
from pathlib import Path

# Allow running this script directly (adds the project root to the path
# so "from src import ..." works even though this file lives in tools/).
sys.path.append(str(Path(__file__).resolve().parent.parent))

from src import data_manager  # noqa: E402


def build_users():
    return [
        {"username": "student01", "password": "1234", "role": "student"},
        {"username": "student02", "password": "abcd", "role": "student"},
        {"username": "admin01", "password": "admin123", "role": "admin"},
    ]


def build_quizzes():
    return [
        {"quiz_id": 1, "title": "Python Basics", "category": "Programming",
         "questions": [101, 102, 103, 104, 105, 106]},
        {"quiz_id": 2, "title": "Data Types & Structures", "category": "Programming",
         "questions": [201, 202, 203, 204, 205, 206]},
    ]


def build_questions():
    return [
        {"question_id": 101, "quiz_id": 1,
         "question": "Which keyword defines a function in Python?",
         "options": ["def", "func", "define", "function"], "answer": "def", "difficulty": "easy"},
        {"question_id": 102, "quiz_id": 1,
         "question": "Which symbol starts a comment in Python?",
         "options": ["//", "#", "<!--", "*"], "answer": "#", "difficulty": "easy"},
        {"question_id": 103, "quiz_id": 1,
         "question": "What is the output of print(2 ** 3)?",
         "options": ["6", "8", "9", "23"], "answer": "8", "difficulty": "medium"},
        {"question_id": 104, "quiz_id": 1,
         "question": "Which loop is best when the number of repeats is already known?",
         "options": ["for", "while", "if", "try"], "answer": "for", "difficulty": "easy"},
        {"question_id": 105, "quiz_id": 1,
         "question": "What does the len() function return for a string?",
         "options": ["Its memory address", "Its number of characters", "Its data type", "Nothing"],
         "answer": "Its number of characters", "difficulty": "easy"},
        {"question_id": 106, "quiz_id": 1,
         "question": "Which of these is a valid variable name?",
         "options": ["2total", "total_2", "total-2", "total 2"], "answer": "total_2", "difficulty": "medium"},

        {"question_id": 201, "quiz_id": 2,
         "question": "Which data type stores items that CANNOT be changed after creation?",
         "options": ["list", "tuple", "dict", "set"], "answer": "tuple", "difficulty": "medium"},
        {"question_id": 202, "quiz_id": 2,
         "question": "Which data type stores key-value pairs?",
         "options": ["list", "tuple", "dictionary", "set"], "answer": "dictionary", "difficulty": "easy"},
        {"question_id": 203, "quiz_id": 2,
         "question": "Which data type automatically removes duplicate values?",
         "options": ["list", "tuple", "set", "string"], "answer": "set", "difficulty": "medium"},
        {"question_id": 204, "quiz_id": 2,
         "question": "Which square brackets create a list in Python?",
         "options": ["()", "{}", "[]", "<>"], "answer": "[]", "difficulty": "easy"},
        {"question_id": 205, "quiz_id": 2,
         "question": "What is the index of the first item in a Python list?",
         "options": ["-1", "0", "1", "It depends"], "answer": "0", "difficulty": "easy"},
        {"question_id": 206, "quiz_id": 2,
         "question": "Which method adds one item to the end of a list?",
         "options": ["append()", "add()", "insert(0)", "push()"], "answer": "append()", "difficulty": "medium"},
    ]


def build_results():
    return [
        {"username": "student01", "quiz_id": 1, "quiz_title": "Python Basics",
         "score": 5, "total": 6, "percentage": 83.33, "timestamp": "2026-09-20 10:15:00"},
        {"username": "student02", "quiz_id": 1, "quiz_title": "Python Basics",
         "score": 4, "total": 6, "percentage": 66.67, "timestamp": "2026-09-21 11:05:00"},
        {"username": "student01", "quiz_id": 2, "quiz_title": "Data Types & Structures",
         "score": 6, "total": 6, "percentage": 100.0, "timestamp": "2026-09-22 09:40:00"},
    ]


def main():
    data_manager.save_json("users.json", build_users())
    data_manager.save_json("quizzes.json", build_quizzes())
    data_manager.save_json("questions.json", build_questions())
    data_manager.save_json("results.json", build_results())
    print("Sample data generated successfully in the data/ folder:")
    print("  users.json     -> 3 demo accounts (2 students, 1 admin)")
    print("  quizzes.json   -> 2 quizzes")
    print("  questions.json -> 12 questions")
    print("  results.json   -> 3 past attempts")
    print("\nDemo logins:")
    print("  Student -> username: student01 | password: 1234")
    print("  Admin   -> username: admin01   | password: admin123")


if __name__ == "__main__":
    main()
