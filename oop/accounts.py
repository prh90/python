class Account:
    """ A simple account class with balance """
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print("Account created for " + self.name)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if amount > 0:
            if self.balance - amount > 0:
                self.balance -= amount
            else:
                print("You do not have sufficient funds")

    def show_balance(self):
        print("Balance is {}".format(self.balance))

pablo = Account("Pablo", 103)
pablo.withdraw(7000)
pablo.show_balance()
pablo.deposit(10000)
pablo.show_balance()
pablo.withdraw(36000)
pablo.show_balance()
pablo.withdraw(300)
pablo.show_balance()
