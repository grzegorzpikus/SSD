import sqlite3

# initial connection to database
# cursor prepared
initial_connection = sqlite3.connect("cern.db")
initial_cursor = initial_connection.cursor()


# creating Employee table once
initial_cursor.execute("""CREATE TABLE IF NOT EXISTS Employee(
                Patient_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name varchar (255),
                last_name varchar (255),
                Branch varchar(255)          
                )""")

# commit changes to database
initial_connection.commit()

# commit changes to database
initial_connection.commit()
# close the initial cursor
initial_cursor.close()
# close the connection to not have it running when not in use
initial_connection.close()

# initial connection to database
# cursor prepared
initial_connection = sqlite3.connect("cern.db")
initial_cursor = initial_connection.cursor()


# creating Employee table once
initial_cursor.execute("""CREATE TABLE IF NOT EXISTS User(
                Name varchar (255),
                Email varchar (255),
                Username varchar (255),
                Password varchar(255),
                Administrator int
                )""")

# commit changes to database
initial_connection.commit()

# commit changes to database
initial_connection.commit()
# close the initial cursor
initial_cursor.close()
# close the connection to not have it running when not in use
initial_connection.close()

# create dummy data
initial_connection = sqlite3.connect("cern.db")
# create a cursor
initial_cursor = initial_connection.cursor()

# another way to insert data
sql_Employee = """INSERT INTO Employee (First_name, Last_name, Branch) VALUES (?, ?, ?)"""
values_Employee = [("Harry", "Potter", "Magical Law Enforcement"),
        ("Ron ", "Weasly", "Magical Law Enforcement"),
        ("Hermoine", "Granger", "Magical law enforcement"),
        ("Molly", "Weasly", "Project Management Office"),
        ("Arthur", "Weasly", "Misuse of Muggle Artifacts"),
        ("George", "Weasly", "Procurment"),
        ("Fleur", "Delacour", "Finance")]


# creating cursor to execute dummy data
# all dummy data has been created and inserted, commit and close the connection to database
initial_cursor.executemany(sql_Employee, values_Employee)
initial_connection.commit()
initial_cursor.close()
