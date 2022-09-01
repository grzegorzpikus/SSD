import sqlite3
import os

_database_name = os.path.dirname(__file__) + r'/database_file.db'

def create_table():
    """This function creates the table in the database if it does not exist."""

    conn = sqlite3.connect(_database_name)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (name varchar(255), email 
    varchar(255), username varchar(255), password varchar(255), admin int)''')
    conn.commit()
    conn.close()


def sql_add_user(details: list):
    """This function adds a user to the database."""

    conn = sqlite3.connect(_database_name)
    conn.set_trace_callback(print)
    c = conn.cursor()

    name = details[2]
    email = details[3]
    username = details[0]
    password = details[1]
    admin = details[4]

    x = c.execute(f'''INSERT INTO users (name, email, username, password, admin) 
    VALUES ("{name}", "{email}", "{username}", "{password}", {admin});''')
    conn.commit()
    conn.close()


def sql_user_exist(username):
    """
    This function checks if the user exists in the database.
    It returns int 1 if it does.
    It returns int 0 if it does not.
    """
    
    conn = sqlite3.connect(os.path.dirname(__file__) + r'/database_file.db')
    c = conn.cursor()
    result = c.execute(f'''SELECT EXISTS(SELECT 1 FROM users WHERE username = "{username}");''')
    result_to_return = result.fetchone()
    conn.commit()
    conn.close()
    return result_to_return[0]


def sql_password_correct(username):
    """This function checks if password that has been provided by a user is
    valid, i.e. its hashed value is equal to those stored in the database."""

    conn = sqlite3.connect(_database_name)
    c = conn.cursor()
    result = c.execute(f"""SELECT password FROM users WHERE username = 
    '{username}';""")
    result_to_return = result.fetchone()
    conn.commit()
    conn.close()
    return result_to_return[0]


def sql_print_all():
    """This function prints all records form the users table in the database,
    and returns a list of all records."""
    user_list = []

    conn = sqlite3.connect(_database_name)
    c = conn.cursor()
    c.execute("""SELECT * FROM users;""")
    rows = c.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
        user_list.append(row)
    return user_list


def sql_change_user_status(selected_user):
    """This function upgrade a chosen user to be an administrator.
    This function can be use by an existing administrator only."""

    conn = sqlite3.connect(_database_name)
    c = conn.cursor()
    c.execute(f"""UPDATE users SET admin = 1 WHERE username =
     '{selected_user}';""")
    conn.commit()
    conn.close()


def sql_delete_user(selected_user):
    """This function deletes a chosen user from the database.
    This function can be use by an existing administrator only."""

    conn = sqlite3.connect(_database_name)
    c = conn.cursor()
    c.execute(f"""DELETE FROM users WHERE username = '{selected_user}'""")
    conn.commit()
    conn.close()

# sql_print_all()
# sql_delete_user('johnsmith')
