import sqlite3

def get_database():
    # connects to the database
    connection = sqlite3.connect("cern.py")
    return connection

# The name of the table is 'userfiles'
def create_table():
    table =  """CREATE TABLE IF NOT EXISTS userfiles(
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT NOT NULL,
              format TEXT NOT NULL,
              subject TEXT NOT NULL)"""
      

    database = get_database()

    # cursor(): is a method which acts as middleware between SQLite database connection and SQL query.
    cursor = database.cursor()

    
    # executes the query and fetch the records from the database. 
    cursor.execute(table)
