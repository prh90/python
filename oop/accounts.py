class Account:
    """ A simple account class with balance """
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print("Account created for " + self.name)
        print("Initial balance {}".format(self.balance))

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.show_balance()

    def withdraw(self, amount):
        if amount > 0:
            if self.balance - amount > 0:
                self.balance -= amount
            else:
                print("You do not have sufficient funds")
        self.show_balance()

    def show_balance(self):
        print("Balance is {}".format(self.balance))

pablo = Account("Pablo", 103)
# pablo.withdraw(7000)
pablo.deposit(500)

