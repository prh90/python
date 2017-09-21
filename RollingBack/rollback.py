import sqlite3

db = sqlite3.connect("accounts.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS accounts (name TEXT PRIMARY KEY NOT NULL, balance INTEGER NOT NULL)")
db.execute("CREATE TABLE IF NOT EXISTS  transactions (time TIMESTAMP NOT NULL, account TEXT NOT NULL, "
           "amount INTEGER NOT NULL, PRIMARY KEY (time, account))")


class Account(object):

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

    def deposit(self, amount: int) -> float:
            if amount > 0.0:
                # self._balance += amount
                new_balance = self._balance + amount
                print("{:.2f} deposited".format(amount/100))
            return self._balance/100

    def withdraw(self, amount: int) -> float:
        if 0 < amount <= self._balance:
            self._balance -= amount
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
    pablo.withdraw(42)
    pablo.show_balance()

    print("*"*50)
    tim = Account("TimL")
    print("*"*50)
    eric = Account("Eric", 9000)
    mom = Account("Mom")

    db.close()
