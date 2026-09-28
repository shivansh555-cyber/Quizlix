"""
quiz_engine.py
---------------
The heart of Quizlix: showing questions, collecting answers, and working
out the score. The scoring logic is written as a separate, "pure"
function (evaluate_answers) that does NOT use input()/print(). This makes
it easy to unit-test, because tests can just pass in a list of answers
without needing a real person typing at a keyboard.

Top-down algorithm (from the build guide):
  1. Load the quiz's questions.
  2. Show each question, one at a time.
  3. Take the student's answer.
  4. Compare it to the correct answer.
  5. Add up the score and work out the percentage.
"""

from src import question_bank


def evaluate_answers(questions, student_answers):
    """
    Pure scoring function (no input/print here -- easy to unit test).

    questions:       list of question dictionaries (with "answer" key)
    student_answers: list of the option text the student picked, in the
                      SAME order as 'questions'

    Returns a dictionary: {"score": int, "total": int, "percentage": float}
    """
    total = len(questions)
    score = 0

    for question, given_answer in zip(questions, student_answers):
        if given_answer == question["answer"]:
            score += 1

    percentage = round((score / total) * 100, 2) if total > 0 else 0.0
    return {"score": score, "total": total, "percentage": percentage}


def take_quiz(quiz):
    """
    Interactive version used by the real menu: shows each question on
    screen, reads the student's typed choice, and returns the same kind
    of result dictionary as evaluate_answers().
    """
    questions = question_bank.get_questions_for_quiz(quiz["quiz_id"])

    if not questions:
        print("This quiz has no questions yet. Please try another quiz.")
        return None

    print(f"\nStarting quiz: {quiz['title']} ({len(questions)} questions)\n")
    student_answers = []

    for index, question in enumerate(questions, start=1):
        print(f"Q{index}. {question['question']}")
        for option_index, option in enumerate(question["options"], start=1):
            print(f"   {option_index}. {option}")

        choice = _ask_valid_choice(len(question["options"]))
        selected_option = question["options"][choice - 1]
        student_answers.append(selected_option)
        print()

    return evaluate_answers(questions, student_answers)


def _ask_valid_choice(num_options):
    """
    Keep asking until the student types a whole number between 1 and
    num_options. This is basic input validation using a while loop.
    """
    while True:
        raw_choice = input(f"Your answer (1-{num_options}): ").strip()
        if raw_choice.isdigit() and 1 <= int(raw_choice) <= num_options:
            return int(raw_choice)
        print(f"Please enter a number between 1 and {num_options}.")
