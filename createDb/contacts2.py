import sqlite3

db = sqlite3.connect("contacts.sqlite")

new_email = "TRYupdate@update.com"
phone = input("Please enter the phone number: ")

# update_sql = "UPDATE contacts SET email = '{}' WHERE contacts.phone = {}".format(new_email, phone)
update_sql = "UPDATE contacts SET email = ? WHERE phone = ?"

print(update_sql)

update_cursor = db.cursor()
# It executes multiple statements that can lead to an injection attack. execute only runs 1 command.
# 456123;drop table contacts this it input to inject
# update_cursor.executescript(update_sql)

# update_cursor.execute(update_sql)
update_cursor.execute(update_sql, (new_email, phone))
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
