import Classes as Cls
import database_managment as DB
import sqlite3
import os


def add_user(details: list):
    """Function creates a new account and adds in to the database."""

    DB.sql_add_user(details)


def create_user_object(user_name):
    """
    If user logs in successfully, this function creates a user object.
    If an admin attribute is 1 (int), the function creates Administrator object.
    If it is 0 (int), the function creates User object.
    """

    conn = sqlite3.connect(os.path.dirname(__file__) + r'/database_file.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM users;""")
    rows = c.fetchall()
    for row in rows:
        if row[2] == user_name:
            # The user has an administrator status.
            if row[4] == 1:
                user_object = Cls.Administrator(row[0], row[1], row[2],
                                                row[3], row[4])
                return user_object
            # The user does not have an administrator status.
            elif row[4] == 0:
                user_object = Cls.User(row[0], row[1], row[2],
                                                row[3], row[4])
                return user_object
            else:
                return None
