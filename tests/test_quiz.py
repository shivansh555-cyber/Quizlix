"""
test_quiz.py
-------------
Unit tests for question validation and the quiz scoring algorithm.
The scoring function evaluate_answers() takes plain lists as input, so we
can test it directly without needing a real quiz file or user input.
"""

import unittest
from src import validators
from src.quiz_engine import evaluate_answers


class TestQuestionValidation(unittest.TestCase):

    def test_valid_mcq_is_accepted(self):
        question = {
            "question": "2 + 2 = ?",
            "options": ["3", "4", "5"],
            "answer": "4",
        }
        ok, reason = validators.is_valid_mcq(question)
        self.assertTrue(ok)

    def test_answer_not_in_options_is_rejected(self):
        question = {
            "question": "2 + 2 = ?",
            "options": ["3", "5", "6"],
            "answer": "4",
        }
        ok, reason = validators.is_valid_mcq(question)
        self.assertFalse(ok)

    def test_too_few_options_is_rejected(self):
        question = {"question": "True or False: Python is a language.", "options": ["True"], "answer": "True"}
        ok, reason = validators.is_valid_mcq(question)
        self.assertFalse(ok)

    def test_empty_question_text_is_rejected(self):
        question = {"question": "", "options": ["A", "B"], "answer": "A"}
        ok, reason = validators.is_valid_mcq(question)
        self.assertFalse(ok)


class TestScoring(unittest.TestCase):

    def setUp(self):
        self.questions = [
            {"question": "Q1", "options": ["a", "b"], "answer": "a"},
            {"question": "Q2", "options": ["a", "b"], "answer": "b"},
            {"question": "Q3", "options": ["a", "b"], "answer": "a"},
        ]

    def test_all_correct_gives_full_score(self):
        result = evaluate_answers(self.questions, ["a", "b", "a"])
        self.assertEqual(result["score"], 3)
        self.assertEqual(result["total"], 3)
        self.assertEqual(result["percentage"], 100.0)

    def test_all_wrong_gives_zero_score(self):
        result = evaluate_answers(self.questions, ["b", "a", "b"])
        self.assertEqual(result["score"], 0)

    def test_partial_score_and_percentage(self):
        result = evaluate_answers(self.questions, ["a", "a", "a"])  # 2 out of 3 correct
        self.assertEqual(result["score"], 2)
        self.assertAlmostEqual(result["percentage"], 66.67, places=1)

    def test_score_never_exceeds_total_questions(self):
        result = evaluate_answers(self.questions, ["a", "b", "a"])
        self.assertLessEqual(result["score"], result["total"])

    def test_empty_quiz_does_not_crash(self):
        result = evaluate_answers([], [])
        self.assertEqual(result["total"], 0)
        self.assertEqual(result["percentage"], 0.0)


if __name__ == "__main__":
    unittest.main()
