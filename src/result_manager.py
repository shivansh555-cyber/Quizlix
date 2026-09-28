"""
result_manager.py
-------------------
Saves quiz attempt results and lets a student look back at their history.
Each result record remembers who took the quiz, which quiz, and the
score/percentage they earned, along with a timestamp.
"""

from datetime import datetime
from src import data_manager

RESULTS_FILE = "results.json"


def save_result(username, quiz_id, quiz_title, score, total, percentage):
    """Append a new result record to results.json."""
    results = data_manager.load_json(RESULTS_FILE)

    new_result = {
        "username": username,
        "quiz_id": quiz_id,
        "quiz_title": quiz_title,
        "score": score,
        "total": total,
        "percentage": percentage,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    results.append(new_result)
    data_manager.save_json(RESULTS_FILE, results)
    return new_result


def get_history(username):
    """Return every result belonging to this student, most recent first."""
    results = data_manager.load_json(RESULTS_FILE)
    history = [r for r in results if r["username"].lower() == username.lower()]
    return list(reversed(history))


def get_all_results():
    return data_manager.load_json(RESULTS_FILE)
