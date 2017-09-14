import sqlite3

conn = sqlite3.connect("contacts.sqlite")

name = input("Please enter the name of who you are looking for: ")

find = ("SELECT * FROM contacts WHERE name = {}".format(name))
print(find)

update_cursor = conn.cursor()

update_cursor.close()
conn.close()
