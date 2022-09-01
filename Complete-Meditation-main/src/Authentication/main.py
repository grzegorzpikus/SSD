"""
This module is a playground to test Authentication as a separated,
individual module form the software we provided. To check the
functionalities within the authentication module (login and sign up),
this file (main.py) has to be executed.
author: G. Pikus
"""

from Input_checker import log_in, sing_up
from main_user import user_managment


def main():
    """This function starts the script."""

    print("*"*80 + "\n Welcome in personal CERN application (pCERNa). Choose "
          "one of the options below:" + "\n" + "*" * 80 + "\n [1] to log-in "
          "type 1\n [2] to sign-up type 2\n [3] to go back to the main menu "
          "type 3\n [4] to quit the application type exit" + "\n" + "*" * 80)

    inp = input()

    if inp == '1':
        inp1 = input("Provide a username: ")
        inp2 = input("Provide a password: ")
        try:
            user = log_in(inp1, inp2)
            user_managment(user)
        except RuntimeError:
            print("*"*80)
    elif inp == '2':
        inp1 = input("Provide your first name and last name separaded "
                     "by space: ")
        inp2 = input("Provide your CERN e-mail: ")
        inp3 = input("Provide your username: ")
        inp4 = input("Provide your password: ")
        try:
            user_data = sing_up(inp1, inp2, inp3, inp4)
        except RuntimeError:
            print("*" * 80)
    elif inp == '3':
        main()
    elif inp == 'exit':
        print("You quite the application.")
        quit()
    else:
        print("Wrong command, try again")
        main()


if __name__ == "__main__":
    main()


