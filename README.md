# 🧠 Quizlix — Smart Quiz Management System

> A menu-driven, terminal-based quiz management system built in pure Python. No external libraries, no database setup. Just run it and start quizzing.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Storage](https://img.shields.io/badge/Storage-JSON-green)
![Dependencies](https://img.shields.io/badge/Dependencies-None-brightgreen)
![Status](https://img.shields.io/badge/Status-Complete-success)

---

## 📌 About the Project

**Quizlix** lets an admin create and manage quiz questions, and lets students log in, attempt quizzes, and see their results, all from the command line. It was built as a **VITyarthi "Build Your Own Project"** submission at **VIT Bhopal University**, using only fundamental Python concepts.

**Why Quizlix?**
- Simple enough for a beginner to read and understand end to end
- Clean modular structure, with each file doing one job
- Data is saved in JSON files, so nothing is lost when you close the program

---

## ✨ Features

| Area | What it does |
|------|--------------|
| 🔐 **Authentication** | Register and log in with validated credentials |
| 📚 **Question Bank** | Add, view, edit and delete quiz questions |
| 📝 **Quiz Engine** | Attempt a quiz, answer MCQs, get instant scoring |
| 📊 **Results** | Every attempt is saved and can be reviewed later |
| 📈 **Reports** | Summary of scores, performance and attempts |
| ✅ **Input Validation** | Handles wrong or empty input without crashing |
| 💾 **Persistent Storage** | All data stored in JSON files |

---

## 🛠️ Tech Stack

- **Language:** Python 3.8+
- **Storage:** JSON files (`json` module)
- **Libraries:** Python standard library only (no `pip install` needed)
- **Interface:** Menu-driven command line

### Python concepts used
Variables and expressions · Conditionals · Loops · Functions · Lists · Tuples · Sets · Dictionaries · File handling · Basic searching and sorting

---

## 📁 Project Structure

```
Quizlix/
│
├── main.py               # Entry point, starts the program
├── menu.py               # All menus and navigation
├── auth.py               # Registration and login
├── validators.py         # Input checking helpers
├── data_manager.py       # Reads and writes JSON files
├── question_bank.py      # Add / view / edit / delete questions
├── quiz_manager.py       # Create and manage quizzes
├── quiz_engine.py        # Runs a quiz and calculates the score
├── result_manager.py     # Saves and fetches results
├── reporting.py          # Score summaries and reports
│
├── data/
│   ├── users.json
│   ├── questions.json
│   └── results.json
│
└── README.md
```

> 💡 Adjust file names above to match your final code if they differ.

---

## 🚀 Getting Started

### Prerequisites
- Python **3.8 or higher**. Check with:
  ```bash
  python --version
  ```

### Installation & Run

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/Quizlix.git

# 2. Go into the project folder
cd Quizlix

# 3. Run the program
python main.py
```

That's it. No dependencies to install.

---

## 🎮 How to Use

1. **Run** `python main.py`
2. **Register** a new account or **log in**
3. From the main menu, choose an option:

```
========== QUIZLIX ==========
1. Register
2. Login
3. Exit
=============================
```

4. After login you can manage questions, take a quiz, view results and see reports.
5. Enter the number of the option you want and press **Enter**.

---

## 🖥️ Sample Output

```
========== QUIZLIX ==========
Welcome back, Student!

Q1. Which keyword is used to define a function in Python?
   1) func
   2) def
   3) define
   4) function
Your answer (1-4): 2
✅ Correct!

----------------------------
Quiz Finished!
Score: 8 / 10  (80%)
Result: PASS
----------------------------
```

*(Replace with a real screenshot of your program for extra impact.)*

---

## 🧩 How It Works

```
        ┌────────────┐
        │  main.py   │
        └─────┬──────┘
              ▼
        ┌────────────┐      ┌───────────────┐
        │  menu.py   │─────▶│    auth.py    │
        └─────┬──────┘      └───────────────┘
              ▼
   ┌──────────┼───────────┬────────────────┐
   ▼          ▼           ▼                ▼
question_  quiz_       result_         reporting.py
bank.py    engine.py   manager.py
   └──────────┴───────────┴────────────────┘
                     ▼
              data_manager.py  ⇄  JSON files
```

---

## 🔮 Future Improvements

- Timer for each question
- Difficulty levels and categories
- Random question selection
- Leaderboard
- Export reports to CSV
- GUI version using Tkinter

---

## 🐛 Known Limitations

- Runs in the terminal only (no GUI)
- Passwords are stored as plain text, which is fine for a learning project, not for production
- Single-machine use (no network or multi-user sync)

---

## 👨‍💻 Author

Shivansh Sharma
- 🎓 B.Tech CSE, VIT Bhopal University
- 🆔 Reg. No: 26BCE11410
- 🔗 GitHub: [@shivansh555-cyber](https://github.com/shivansh555-cyber)

---

## 📄 License

This project is created for academic purposes as part of the VITyarthi *Build Your Own Project* submission. Free to use for learning.

---

⭐ *If you found this project helpful, consider giving it a star!*
