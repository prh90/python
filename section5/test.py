import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, username text, password text)"

cursor.execute(create_table)

user = (1, 'pablo', 'asdf')
insert_query = "INSERT INTO users VALUES(?, ?, ?)"

cursor.execute(insert_query, user)  # cursor is smart enough to replace fields

users = [
     (2, 'jose', 'qwerty'),
     (3, 'rolf', 'zxcvb')
]

cursor.executemany(insert_query, users)  # same as execute but for all in list

select_query = "SELECT * FROM users"

for row in cursor.execute(select_query):
    print(row)

connection.commit()
connection.close()
