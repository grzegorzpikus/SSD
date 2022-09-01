import os
import sys
sys.path.append(os.path.dirname(__file__) + "/../")
from session import session_manager_singleton
import Authentication_checker as Ac
from Authentication_checker import hashing
from Authentication import create_user_object, add_user


def log_in(inp_username=None, inp_password=None):
    """This is a log-in checker function that examines inputs provided by the
    user before the user object is created."""

    def username_fn(inp):
        """The function checks if username is provided correctly and if it
        exists in the database."""

        # correct format of username?
        if len(inp.split()) != 1:
            print("No space are allowed, try again")
            raise RuntimeError("login failed")
            # inp = username_fn()
        # does username exist in the database?
        user_name_verification = Ac.user_exists(inp)
        # if user_name_verification is not 1:
        if user_name_verification != 1:
            print(' The username does not exist. Try again.')
            raise RuntimeError("login failed")

        return inp

    def password_fn(inp1, inp):
        """The function checks if password of a user is provided correctly."""

        password_verification = Ac.password_correct(inp1, inp)
        if password_verification is not True:
            print(' Wrong password, please try again.')
            raise RuntimeError("login failed")
        return hashing(inp)
    
    username = username_fn(inp_username)
    password = password_fn(inp_username, inp_password)
    user = create_user_object(username)
    print(f"Welcome {user.user_name}!")
    return user


def sign_up(inp_name, inp_email, inp_username, inp_password):
    """
    This is a sign-up checker function that examines inputs provided by the
    user before the sign-up details are passed through and a new user
    is added to the database.
    """

    def name_fn(inp):
        """The function checks if name of the user is provided correctly."""

        if len(inp.split()) != 2:
            print(" Provide your first name and surname separated by space! "
                  "Try again.")
            raise RuntimeError("login failed")
        return inp

    def email_fn(inp):
        """The function checks if e-mail of the user is provided correctly."""

        # if "@cern.ch" not in inp:
        if not inp.endswith("@cern.ch"):
            print(" Wrong e-mail! Try again.")
            raise RuntimeError("login failed")
        return inp

    def username_fn(inp):
        """The function checks if username is provided correctly."""

        # is the username a singe word (no spaces)?
        if len(inp.split()) != 1:
            print(" No space is allowed, try again.")
            raise RuntimeError
        # does the username name exist in the database?
        if Ac.user_exists(inp) == 1:
            print('User name already exists. Provide a different one.')
            raise RuntimeError("login failed")
        return inp

    def password_fn(inp):
        """The function checks if password of a user is provided correctly."""

        # checks if the password is strong enough
        check_list = Ac.password_strength(inp)
        if check_list[0] is False:
            print("Password is too short.")
            raise RuntimeError("login failed")
        if check_list[1] is False:
            print("Password needs to have at least one lowercase character.")
            raise RuntimeError("login failed")
        if check_list[2] is False:
            print("Password needs to have at least one uppercase character.")
            raise RuntimeError("login failed")
        if check_list[3] is False:
            print("Password needs to have at least one number.")
            raise RuntimeError("login failed")
        if check_list[4] is False:
            print("Password needs to have at least one special character.")
            raise RuntimeError("login failed")
        return hashing(inp)

    name = name_fn(inp_name)
    email = email_fn(inp_email)
    username = username_fn(inp_username)
    password = password_fn(inp_password)
    details = [username, password, name, email, 0]
    add_user(details)


def log_in_with_http(inp_username=None, inp_password=None):
    user = log_in(inp_username, inp_password)
    print(f"login : {session_manager_singleton}")
    return session_manager_singleton.add(user)
