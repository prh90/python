import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
#  To have auto increment you cant use int you spell it out
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name text, price real)"
#  To have auto increment you cant use int you spell it out
cursor.execute(create_table)

# cursor.execute("INSERT INTO items VALUES ('test', 10.99)")

connection.commit()

connection.close()

"""
Code above was used to create the tables until this code below was used
the code in each class tells the db what it needs

@app.before_first_request
def create_tables():
    db.create_all()

"""
