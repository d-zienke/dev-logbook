import sqlite3

connection = sqlite3.connect("data.db")

# this allows retrieving rows as dictionaries instead of tuples (by default)
# it may slow down the program a little so use it only when needed
# connection.row_factory = sqlite3.Row

def create_table():
  with connection:
    connection.execute("CREATE TABLE IF NOT EXISTS entry (content TEXT, date TEXT);")
    
def drop_table():
  with connection:
    connection.execute("DROP TABLE IF EXISTS entry;")


def add_entry(entry_body, entry_date):
  with connection:
    connection.execute("INSERT INTO entry VALUES (?, ?)",(entry_body, entry_date))


def get_entries():
  with connection:
    cursor = connection.execute("SELECT * FROM entry;")
    return cursor