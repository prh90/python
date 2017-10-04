import sqlite3, pytz, datetime

db = sqlite3.connect("accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)
db.execute("CREATE TABLE IF NOT EXISTS accounts (name TEXT PRIMARY KEY NOT NULL, balance INTEGER NOT NULL)")
db.execute("CREATE TABLE IF NOT EXISTS  transactions (time TIMESTAMP NOT NULL, account TEXT NOT NULL, "
           "amount INTEGER NOT NULL, PRIMARY KEY (time, account))")
db.execute("CREATE VIEW IF NOT EXISTS localhistory AS "
           "SELECT strftime('%Y-%m-%d %H:%M:%f', transactions.time,'localtime' )AS localtime,"
           "transactions.account, transactions.amount FROM transactions ORDER BY transactions.time")


class Account(object):

    @staticmethod
    def _current_time():
        # return 1
        return pytz.utc.localize(datetime.datetime.utcnow())
        # local_time = pytz.utc.localize(datetime.datetime.utcnow())
        # return local_time.astimezone()

    def __init__(self, name: str, opening_balance: int = 0):
        cursor = db.execute("SELECT name, balance FROM accounts WHERE (name = ?)", (name,))
        row = cursor.fetchone()

        if row:
            self.name, self._balance = row
            print("Retrieved record for {}, ".format(self.name), end='')
        else:
            self.name = name
            self._balance = opening_balance
            cursor.execute("INSERT INTO accounts VALUES(?,?)", (name, opening_balance))
            cursor.connection.commit()
            print("Account created for {}.".format(self.name, end=''))
        self.show_balance()

    def _save_update(self, amount):
        new_balance = self._balance + amount
        deposit_time = Account._current_time()

        try:
            db.execute("UPDATE accounts SET balance = ? WHERE (name=?)", (new_balance, self.name))
            db.execute("INSERT INTO transactions VALUES(?, ?, ?)", (deposit_time, self.name, amount))
        except sqlite3.Error:
            db.rollback()
            # pass
        else:
            db.commit()
            self._balance = new_balance

    def deposit(self, amount: int) -> float:
            if amount > 0.0:
                # self._balance += amount
                # new_balance = self._balance + amount
                # deposit_time = Account._current_time()
                # db.execute("UPDATE accounts SET balance = ? WHERE (name=?)", (new_balance, self.name))
                # db.execute("INSERT INTO transactions VALUES(?, ?, ?)",(deposit_time, self.name, amount))
                # db.commit()
                # self._balance = new_balance
                self._save_update(amount)
                print("{:.2f} deposited".format(amount/100))
            return self._balance/100

    def withdraw(self, amount: int) -> float:
        if 0 < amount <= self._balance:
            # self._balance -= amount
            # new_balance = self._balance - amount
            # withdrawal_time = Account._current_time()
            # db.execute("UPDATE accounts SET balance = ? WHERE (name=?)", (new_balance, self.name))
            # db.execute("INSERT INTO transactions VALUES(?, ?, ?)", (withdrawal_time, self.name, -amount))
            # db.commit()
            # self._balance = new_balance
            self._save_update(-amount)
            print("{:.2f} withdrew".format(amount/100))
            return amount/100
        else:
            print("The amount must be greater than 0 and no more than your account balance")

    def show_balance(self):
        print("Balance on {}'s account is {:.2f}".format(self.name, self._balance / 100))


if __name__ == '__main__':
    pablo = Account("Pablo")
    pablo.deposit(10000)
    pablo.withdraw(57)
    pablo.show_balance()
    pablo.deposit(4200)
    pablo.withdraw(3500)
    pablo.show_balance()

    print("*"*50)
    tim = Account("TimL")
    print("*"*50)
    eric = Account("Eric", 9000)
    mom = Account("Mom")
    Account("Pablo")

    db.close()
