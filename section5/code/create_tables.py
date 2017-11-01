import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
#  To have auto increment you cant use int you spell it out
cursor.execute(create_table)

connection.commit()

connection.close()
