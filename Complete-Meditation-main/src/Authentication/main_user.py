"""A part of the main.py module"""

import database_managment as dbm


def user_managment(user_object):
    """This function starts the script there a user can do actions."""

    user = user_object
    print("*"*80)
    print(f"Welcome {user.user_name}! Please select your action by typing "
          f"a number:")
    print("*" * 80)
    print(" [1] Print all experiments.\n [2] Add an experiment.\n [3] Delete an"
          "experiment.\n [4] Download an experiment.\n [5] Admin section. ")
    print("*" * 80)

    inp = input()

    if inp == '5':
        if user.admin == 1:
            admin(user_object)
        else:
            print("You do not have privilege to do this action.")
    else:
        print("the rest functionalities are not added yet. Please come back"
              "later")
        user_managment(user)


def admin(user_object):

    user = user_object

    print("*" * 80)
    print(f"Welcome admin! Please select your action by typing "
          f"a number:")
    print("*" * 80)
    print(" [1] To print all registered users.\n [2] To delete a user.\n [3] "
          "To upgrade another user to be an administrator.\n [4] Go back to the"
          " administrator menu.\n [5] Go back to the user menu.\n [6] Exit.")
    print("*" * 80)

    inp = input()

    if inp == '1':
        dbm.sql_print_all()
        admin(user)
    elif inp == '2':
        print("Provide a username of an account to be deleted")
        inp_delete = input()
        try:
            dbm.sql_delete_user(inp_delete)
            print(f"A user {inp_delete} has been removed.")
        except ValueError:
            print("Wrong username.")
        admin(user)
    elif inp == '3':
        print("Provide a username of an account to be upgraded")
        inp_upgrade = input()
        try:
            dbm.sql_change_user_status(inp_upgrade)
            print(f"The user {inp_upgrade} has been promoted to be an admin.")
        except ValueError:
            print("Wrong username.")
        admin(user)
    elif inp == '4':
        admin(user)
    elif inp == '5':
        user_managment(user)
    elif inp == '6' or inp == 'exit':
        exit()
    else:
        "Wrong command please try again."
        admin(user)
