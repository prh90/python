import datetime
import pytz


class Account:
    """ A simple account class with balance """

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance
        self._transaction_list = []
        print("Account created for " + self._name)
        if balance > 0:
            self._transaction_list.append((Account._current_time(), balance))
        else:
            print("Initial balance {}".format(self.__balance))

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.show_balance()
            self._transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if amount > 0:
            if self.__balance - amount > 0:
                self.__balance -= amount
                self._transaction_list.append((Account._current_time(), -amount))
        else:
                print("You do not have sufficient funds")
        self.show_balance()

    def show_balance(self):
        print("Balance is {}".format(self.__balance))

    def show_transactions(self):
        for date, amount in self._transaction_list:
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

print("*"*50)

steph = Account("Steph", 800)
steph.deposit(100)
steph.withdraw(200)
steph.show_transactions()

print("*"*50)

# double underscore will negate anything trying to mess with it.
cyn = Account("Cyn", 0)
cyn.__balance = 10000
cyn.deposit(50)
cyn.withdraw(20)
cyn.show_transactions()
cyn.show_balance()

print(cyn.__dict__)
