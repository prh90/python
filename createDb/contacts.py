import sqlite3

db = sqlite3.connect("contacts.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contacts(name, phone, email) VALUES('Pablo', 456789, 'pablo@email.com')")
db.execute("INSERT INTO contacts VALUES ('Tim', 456123, 'tim@email.com')")


cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")

# print(cursor.fetchall())

print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())

for name, phone, email in cursor:
    print(name)
    print(phone)
    print(email)
    print("#"*40)

# Once this for loop triggers the database ran through everything already and has nothing
# else to print so it is highly efficient
# for name, phone, email in cursor:
#     print(name)
#     print(phone)
#     print(email)
#     print("#"*40)
cursor.close()
db.commit()
db.close()
# Have to commit the changes made so the database keeps record of what you inserted.
# Else it will be lost once connection is ended.
