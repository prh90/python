import datetime
import pytz


class Account:
    """ A simple account class with balance """

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transaction_list = []
        print("Account created for " + self.name)
        print("Initial balance {}".format(self.balance))

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.show_balance()
            self.transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if amount > 0:
            if self.balance - amount > 0:
                self.balance -= amount
                self.transaction_list.append((Account._current_time(), -amount))
        else:
                print("You do not have sufficient funds")
        self.show_balance()

    def show_balance(self):
        print("Balance is {}".format(self.balance))

    def show_transactions(self):
        for date, amount in self.transaction_list:
            if amount > 0:
                trans_type = "deposited"
            else:
                trans_type = "withdrawn"
                amount *= -1
            print("{:6} {} on (local time was {})".format(amount, trans_type, date, date.astimezone()))



pablo = Account("Pablo", 103)
# pablo.withdraw(7000)
pablo.deposit(500)
pablo.withdraw(303)
pablo.show_transactions()

