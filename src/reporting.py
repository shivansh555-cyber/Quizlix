"""
reporting.py
-------------
Turns raw result records into human-friendly summaries, and can export
all results to a CSV file (a simple spreadsheet format) inside output/.
"""

import csv
from pathlib import Path
from src import result_manager
from src import user_manager
from src import quiz_manager

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "output"


def admin_summary():
    """
    Return simple statistics an admin cares about:
    total quizzes, total questions, total attempts, average score %.
    """
    results = result_manager.get_all_results()
    quizzes = quiz_manager.list_quizzes()
    total_questions = sum(len(q["questions"]) for q in quizzes)

    if results:
        average_percentage = round(sum(r["percentage"] for r in results) / len(results), 2)
    else:
        average_percentage = 0.0

    return {
        "total_quizzes": len(quizzes),
        "total_questions": total_questions,
        "total_attempts": len(results),
        "total_students": len(user_manager.list_students()),
        "average_percentage": average_percentage,
    }


def export_results_csv(filename="result_report.csv"):
    """
    Write every result record to a CSV file inside output/.
    Returns the path written to, or None if there was nothing to export.
    """
    results = result_manager.get_all_results()
    if not results:
        print("No results to export yet.")
        return None

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    file_path = OUTPUT_DIR / filename

    fieldnames = ["username", "quiz_title", "score", "total", "percentage", "timestamp"]
    with open(file_path, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for result in results:
            writer.writerow({key: result[key] for key in fieldnames})

    return file_path
