"""
menu.py
--------
All the text-based menus a user sees, and the code that connects a menu
choice to the right function from the other modules. This is the only
file that mixes input()/print() with "calling other modules" -- every
other module stays free of screen text so it can be tested and reused.
"""

from src import auth
from src import quiz_manager
from src import question_bank
from src import quiz_engine
from src import result_manager
from src import reporting
from tests import run_all_tests


def main_menu():
    while True:
        print("\n================ QUIZLIX ================")
        print("1. Student Login")
        print("2. Student Register")
        print("3. Admin Login")
        print("4. View Available Quizzes")
        print("9. Run Tests")
        print("10. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            student_login_flow()
        elif choice == "2":
            student_register_flow()
        elif choice == "3":
            admin_login_flow()
        elif choice == "4":
            show_all_quizzes()
        elif choice == "9":
            run_all_tests.run()
        elif choice == "10":
            print("Thanks for using Quizlix. Goodbye!")
            break
        else:
            print("Invalid choice. Please pick a number from the menu.")


def show_all_quizzes():
    quizzes = quiz_manager.list_quizzes()
    if not quizzes:
        print("No quizzes are available yet.")
        return
    print("\nAvailable quizzes:")
    for quiz in quizzes:
        print(f"  ID {quiz['quiz_id']}: {quiz['title']} "
              f"({quiz['category']}, {len(quiz['questions'])} questions)")


# ---------------------------- Student flows ----------------------------

def student_register_flow():
    print("\n-- Student Registration --")
    username = input("Choose a username: ").strip()
    password = input("Choose a password: ").strip()
    success, message = auth.register(username, password, "student")
    print(message if not success else f"✅ {message}")


def student_login_flow():
    print("\n-- Student Login --")
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    user = auth.login(username, password, expected_role="student")

    if user is None:
        print("❌ Invalid username or password.")
        return

    print(f"Welcome, {user['username']}!")
    student_menu(user)


def student_menu(user):
    while True:
        print(f"\n-------- Student Menu ({user['username']}) --------")
        print("1. View Available Quizzes")
        print("2. Attempt Quiz")
        print("3. View My Results")
        print("4. Logout")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            show_all_quizzes()
        elif choice == "2":
            attempt_quiz_flow(user)
        elif choice == "3":
            view_history_flow(user)
        elif choice == "4":
            print("Logged out.")
            break
        else:
            print("Invalid choice. Please pick a number from the menu.")


def attempt_quiz_flow(user):
    show_all_quizzes()
    raw_id = input("Enter the Quiz ID you want to attempt: ").strip()

    if not raw_id.isdigit():
        print("Quiz ID must be a number.")
        return

    quiz = quiz_manager.get_quiz(int(raw_id))
    if quiz is None:
        print("No quiz found with that ID.")
        return

    result = quiz_engine.take_quiz(quiz)
    if result is None:
        return

    result_manager.save_result(
        user["username"], quiz["quiz_id"], quiz["title"],
        result["score"], result["total"], result["percentage"],
    )

    print("========== QUIZ RESULT ==========")
    print(f"Quiz: {quiz['title']}")
    print(f"Total Questions: {result['total']}")
    print(f"Correct Answers: {result['score']}")
    print(f"Wrong Answers: {result['total'] - result['score']}")
    print(f"Score: {result['score']}/{result['total']}")
    print(f"Percentage: {result['percentage']}%")
    print("==================================")


def view_history_flow(user):
    history = result_manager.get_history(user["username"])
    if not history:
        print("You have not attempted any quiz yet.")
        return

    print(f"\nQuiz history for {user['username']}:")
    for attempt in history:
        print(f"  {attempt['timestamp']} | {attempt['quiz_title']} | "
              f"{attempt['score']}/{attempt['total']} ({attempt['percentage']}%)")


# ----------------------------- Admin flows ------------------------------

def admin_login_flow():
    print("\n-- Admin Login --")
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    user = auth.login(username, password, expected_role="admin")

    if user is None:
        print("❌ Invalid username or password.")
        return

    print(f"Welcome, admin {user['username']}!")
    admin_menu(user)


def admin_menu(user):
    while True:
        print(f"\n-------- Admin Menu ({user['username']}) --------")
        print("1. Create Quiz")
        print("2. Add Question to Quiz")
        print("3. View All Quizzes")
        print("4. Delete Quiz")
        print("5. View Admin Summary")
        print("6. Export Results to CSV")
        print("7. Logout")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            create_quiz_flow()
        elif choice == "2":
            add_question_flow()
        elif choice == "3":
            show_all_quizzes()
        elif choice == "4":
            delete_quiz_flow()
        elif choice == "5":
            show_admin_summary()
        elif choice == "6":
            path = reporting.export_results_csv()
            if path:
                print(f"Results exported to {path}")
        elif choice == "7":
            print("Logged out.")
            break
        else:
            print("Invalid choice. Please pick a number from the menu.")


def create_quiz_flow():
    print("\n-- Create Quiz --")
    raw_id = input("New Quiz ID (number): ").strip()
    if not raw_id.isdigit():
        print("Quiz ID must be a number.")
        return
    title = input("Quiz title: ").strip()
    category = input("Category: ").strip()

    success, message = quiz_manager.create_quiz(int(raw_id), title, category)
    print(("✅ " if success else "❌ ") + message)


def add_question_flow():
    print("\n-- Add Question --")
    show_all_quizzes()
    raw_quiz_id = input("Quiz ID to add this question to: ").strip()
    raw_question_id = input("New Question ID (number): ").strip()

    if not raw_quiz_id.isdigit() or not raw_question_id.isdigit():
        print("IDs must be numbers.")
        return

    text = input("Question text: ").strip()
    options = []
    print("Enter at least 2 options. Type an empty line when done.")
    while True:
        option = input(f"  Option {len(options) + 1}: ").strip()
        if option == "" and len(options) >= 2:
            break
        if option != "":
            options.append(option)

    answer = input("Correct answer (must exactly match one option): ").strip()
    difficulty = input("Difficulty (easy/medium/hard): ").strip() or "easy"

    success, message = question_bank.add_question(
        int(raw_question_id), int(raw_quiz_id), text, options, answer, difficulty
    )
    print(("✅ " if success else "❌ ") + message)


def delete_quiz_flow():
    show_all_quizzes()
    raw_id = input("Quiz ID to delete: ").strip()
    if not raw_id.isdigit():
        print("Quiz ID must be a number.")
        return
    success, message = quiz_manager.delete_quiz(int(raw_id))
    print(("✅ " if success else "❌ ") + message)


def show_admin_summary():
    summary = reporting.admin_summary()
    print("\n-------- Admin Summary --------")
    print(f"Total quizzes:    {summary['total_quizzes']}")
    print(f"Total questions:  {summary['total_questions']}")
    print(f"Total students:   {summary['total_students']}")
    print(f"Total attempts:   {summary['total_attempts']}")
    print(f"Average score:    {summary['average_percentage']}%")
