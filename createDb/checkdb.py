import sqlite3

conn = sqlite3.connect("contacts.sqlite")

id_1 = input("Please enter the name of who you are looking for: ")

# find = "SELECT * FROM contacts WHERE name = {}".format(name)
# print(find)
for name, phone, email in conn.execute("SELECT * FROM contacts"):
    if name == id_1:
        print("#"*40)
        print("Name: {}".format(name))
        print("Phone: {}".format(phone))
        print("Email: {}".format(email))
        print("#"*40)
conn.close()
