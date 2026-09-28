"""
main.py
--------
The single entry point for Quizlix. Run this file to start the program:

    python main.py

All it does is show the main menu and let menu.py take over from there.
Keeping main.py this short makes it obvious where the program starts.
"""

from src import menu

if __name__ == "__main__":
    print("Welcome to Quizlix -- Smart Quiz Management System")
    menu.main_menu()
