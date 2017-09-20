class Account(object):

    def __init__(self, name: str, opening_balance: int = 0):
        self.name = name
        self._balance = opening_balance
        print("Account created for {}.".format(self.name, end=''))
        self.show_balance()

    def deposit(self, amount: int) -> float:
            if amount > 0.0:
                self._balance += amount
                print("{:.2f} deposited".format(amount/100))
            return self._balance/100

    def withdraw(self, amount: int) -> float:
        if 0< amount <= self._balance:
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
