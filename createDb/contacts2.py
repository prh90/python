import sqlite3

db = sqlite3.connect("contacts.sqlite")

update_sql = "UPDATE contacts SET email = 'update@update.com' WHERE contacts.phone = 456123"
update_cursor = db.cursor()
update_cursor.execute(update_sql)
print("{} rows updated".format(update_cursor.rowcount))

update_cursor.connection.commit()
update_cursor.close()

# using the cursor to make the connection is a way to commit.

for name, phone, email in db.execute("SELECT * FROM contacts "):
    print(name)
    print(phone)
    print(email)
    print("#"*40)
db.close()
