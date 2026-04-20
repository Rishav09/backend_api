def add(x:int, y:int):
    return x + y

class InsufficientFunds(Exception):
    pass

class BankAccount():
    def __init__(self, starting_balance=0):
        self.balance = starting_balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFunds("Insufficient funds")
        self.balance -= amount
    def collect_interest(self):
        self.balance *= 1.1
    def get_balance(self):
        return self.balance