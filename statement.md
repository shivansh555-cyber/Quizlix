# Problem Statement — Quizlix

## Problem
Manually managing quizzes is repetitive and error-prone: a teacher has to
organize questions by hand, collect student attempts, check every answer
against the correct one, and calculate scores and percentages one at a
time. As the number of students and quizzes grows, this manual process
becomes slow and inconsistent.

## Scope
Quizlix is a **Python, terminal-based Smart Quiz Management System**
(Version 1) that lets an admin create and manage quizzes and questions,
lets students attempt those quizzes, and automatically evaluates answers
and stores results. Data is stored locally in JSON files — there is no
database server, web interface, or network component. This keeps the
project focused on core Python concepts: functions, control flow, data
structures (lists, dictionaries, sets, tuples), file handling, and basic
validation/testing.

**Out of scope for Version 1:** real college authentication, GUI/web
interface, payments, email delivery, cloud deployment, and machine
learning. These are noted as possible future enhancements.

## Target Users
- **Admin / Teacher** — creates and manages quizzes and the question
  bank, and reviews overall results.
- **Student** — registers/logs in, views available quizzes, attempts a
  quiz, and reviews their own score history.

## High-Level Features
1. **User Management** — student registration, student login, admin
   login, with role-based access.
2. **Quiz Management (Admin)** — create, view, and delete quizzes.
3. **Question Bank (Admin)** — add multiple-choice questions to a quiz,
   with input validation (non-empty text, at least 2 options, a correct
   answer that matches one of the options).
4. **Quiz Attempt (Student)** — view available quizzes, select one, and
   answer each question in turn through a simple numbered menu.
5. **Automatic Evaluation** — each submitted answer is compared with the
   stored correct answer; a running score and final percentage are
   calculated automatically.
6. **Results & History** — every attempt is saved with a timestamp; a
   student can view their full attempt history, and the admin can view a
   summary (total quizzes, questions, students, attempts, average score)
   and export all results to a CSV file.
