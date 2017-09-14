import sqlite3

conn = sqlite3.connect("contacts.sqlite")

name = input("Please enter the name of who you are looking for: ")

# To get a tuple with a single value then we add the value then add a coma with the end bracket.
# for row in conn.execute("SELECT * FROM contacts WHERE name=?", (name,)):
# Not case sensitive and will find something like what you are looking for
for row in conn.execute("SELECT * FROM contacts WHERE name LIKE ?", (name,)):

    print("#"*40)
    print(row)
    print("#"*40)
conn.close()
