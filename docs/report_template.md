# Quizlix — VITyarthi Project Report

> **How to use this template:** This covers every section required by
> the "Build Your Own Project" PDF report guidelines. Fill in the
> `[ ... ]` placeholders — especially the screenshots — with your own
> details and REAL output from running the program. Do not submit fake
> or invented screenshots. Once filled in, convert this Markdown file to
> Word/PDF (Word, LibreOffice, Pandoc, or "Print to PDF" all work).

---

## 1. Cover Page
- Project Title: **Quizlix — Smart Quiz Management System**
- Student Name: `[Your Name]`
- Registration Number: `[Your Reg. No.]`
- Course Title & Code: `[Course Title & Code]`
- Faculty Name: `[Faculty Name]`
- Submission Semester: `[Semester]`
- GitHub Repository Link: `[Paste your repo URL here]`

## 2. Introduction
Manually running quizzes — organizing questions, collecting attempts,
checking answers, and calculating scores — is repetitive and easy to get
wrong at scale. Quizlix is a Python, terminal-based application that
manages quizzes and a question bank, lets students attempt quizzes, and
automatically evaluates and records their results.

## 3. Problem Statement
*(Copy from [`statement.md`](../statement.md), or write it in your own
words.)*

## 4. Functional Requirements
1. User registration and role-based login (student/admin)
2. Quiz management: create, list, and delete quizzes (admin)
3. Question bank management: add multiple-choice questions with
   validation (admin)
4. Quiz attempt flow: view quizzes, select one, answer each question
   (student)
5. Automatic evaluation and scoring of submitted answers
6. Result history per student, and an admin summary + CSV export

## 5. Non-Functional Requirements
1. **Performance** — quiz loading and scoring complete instantly for
   realistic class-sized datasets (tens of quizzes, hundreds of
   questions/results).
2. **Reliability** — missing or corrupted JSON files are handled with a
   clear message instead of crashing the program.
3. **Usability** — every menu is numbered and re-prompts on invalid
   input instead of failing silently.
4. **Maintainability** — the code is split into 10+ small, single-purpose
   modules (top-down design), each with its own docstring.
5. **Security (basic)** — usernames must be unique; only real (non-fake)
   demo credentials are stored, and no private data goes into GitHub.
6. **Resource efficiency** — data is loaded only when needed and JSON
   files stay small and human-readable.

## 6. System Architecture
See [`docs/architecture.md`](architecture.md) for the full diagram.
`[Paste a screenshot/render of the diagram here]`

**Summary:** a menu layer (`menu.py`) is the only place that talks to the
user; it calls logic modules (`auth`, `quiz_manager`, `question_bank`,
`quiz_engine`, `result_manager`, `reporting`); every module that needs to
read/write data goes through a single `data_manager.py`, and
`validators.py` is shared by anything that creates or edits data.

## 7. Design Diagrams
- Use Case Diagram → [`docs/use_case.md`](use_case.md) `[paste render here]`
- Workflow Diagram → [`docs/workflow.md`](workflow.md) `[paste render here]`
- Sequence Diagram → [`docs/sequence.md`](sequence.md) `[paste render here]`
- Class/Component Diagram → [`docs/class_diagram.md`](class_diagram.md) `[paste render here]`
- ER Diagram → [`docs/er_diagram.md`](er_diagram.md) `[paste render here]`

*(Tip: paste the ```mermaid code blocks from each file into the [Mermaid
Live Editor](https://mermaid.live) to get an image you can screenshot
and paste in here.)*

## 8. Design Decisions & Rationale
- **Why JSON for storage?** It's human-readable, needs no extra setup or
  server, and Python's built-in `json` module makes it very beginner
  friendly for a small demo dataset.
- **Why split into so many modules?** Top-down design: each file has one
  job (e.g. `validators.py` only checks data, `data_manager.py` only
  reads/writes files). This makes debugging and testing much easier.
- **Why functions instead of classes?** The syllabus focuses on
  functions, control flow and core data structures; plain functions and
  dictionaries keep the code approachable while still being organized.
- **Why automatic scoring?** Removes repetitive manual marking and keeps
  results consistent and instant.

## 9. Implementation Details
Briefly describe, in your own words, how you implemented each module —
for example:
- `data_manager.py`: `[explain load_json/save_json and error handling]`
- `validators.py`: `[explain the MCQ and registration checks]`
- `quiz_engine.py`: `[explain evaluate_answers() and the scoring formula]`
- `[continue for the remaining modules you feel are worth explaining]`

## 10. Screenshots / Results
`[Insert REAL terminal screenshots here: main menu, student login,
attempting a quiz, the QUIZ RESULT screen, viewing history, admin menu,
admin summary, and the exported CSV opened in Excel/Sheets.]`

## 11. Testing Approach
Automated unit tests (20 total) were written with Python's `unittest`
module, covering:
- Registration validation (empty fields, duplicate usernames)
- Login (correct credentials, wrong password, wrong role)
- MCQ validation (too few options, answer not among options)
- Scoring algorithm (all correct, all wrong, partial score, empty quiz)
- Saving and reading result history (per-user filtering, most-recent-first)

Run with: `python -m unittest discover -s tests -p "test_*.py"`
`[Paste a screenshot of the test run output here]`

## 12. Challenges Faced
`[Write 3–5 genuine challenges you personally faced while building this
— e.g. keeping quizzes and questions linked correctly by ID, deciding
how to validate MCQs, structuring modules cleanly, etc.]`

## 13. Learnings & Key Takeaways
`[What did you personally learn — e.g. practical use of JSON file
handling, writing testable functions, structuring a multi-file Python
project, using Git for version control, etc.]`

## 14. Future Enhancements
- A graphical interface (Tkinter) instead of a text menu
- Quiz timers and negative marking
- Randomized question order per attempt
- Migrating storage from JSON files to a real database (e.g. SQLite)
- Basic analytics/charts on the admin summary

## 15. References
- Python official documentation — https://docs.python.org/3/
- Python `json` module documentation
- Python `unittest` module documentation
