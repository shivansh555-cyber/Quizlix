"""
run_all_tests.py
------------------
A tiny helper so menu option "9. Run Tests" can run the whole test suite
from inside the running program itself (handy for a quick demo), without
needing to open a separate terminal.
"""

import unittest


def run():
    print("\nRunning all unit tests...\n")
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir="tests", pattern="test_*.py")
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
