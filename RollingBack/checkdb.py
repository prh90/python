import sqlite3, pytz

db = sqlite3.connect("accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)

for row in db.execute("SELECT * FROM transactions"):
    utc_time = row[0]
    local_time = pytz.utc.localize(utc_time).astimezone()
    # print(row)
    # local_time = row[0]
    print("{}\t{}".format(utc_time, local_time))

db.close()
