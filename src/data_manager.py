"""
data_manager.py
----------------
This is the ONLY module that talks directly to the JSON files on disk.
Every other module asks this file to load or save data for it.
Keeping all file-reading code in one place means that if we ever changed
HOW we store data (for example moving from JSON to a database), we would
only need to change this one file.

Concepts used: functions, parameters, exception handling (try/except),
the built-in json module, and pathlib for safe file paths.
"""

import json
from pathlib import Path

# BASE_DIR points to the "quizlix" project folder itself, no matter which
# folder the program is actually run from. This avoids "file not found"
# errors that happen when relative paths like "data/users.json" are used.
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"


def load_json(filename):
    """
    Read a JSON file from the data/ folder and return it as a Python
    list or dictionary.

    If the file does not exist, or the file exists but has broken/invalid
    JSON inside it, we do NOT let the program crash. Instead we print a
    friendly message and return an empty list, so the rest of the program
    can keep running.
    """
    file_path = DATA_DIR / filename

    if not file_path.exists():
        print(f"[data_manager] Warning: '{filename}' not found. Starting with empty data.")
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print(f"[data_manager] Error: '{filename}' is corrupted or not valid JSON.")
        return []
    except OSError as error:
        print(f"[data_manager] Error while reading '{filename}': {error}")
        return []


def save_json(filename, data):
    """
    Write a Python list or dictionary back to a JSON file inside data/.
    Returns True if saving worked, False if something went wrong.
    """
    file_path = DATA_DIR / filename

    try:
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2)
        return True
    except OSError as error:
        print(f"[data_manager] Error while saving '{filename}': {error}")
        return False
