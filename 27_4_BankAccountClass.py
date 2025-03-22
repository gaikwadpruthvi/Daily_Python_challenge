#Create a BankAccount class with methods to deposit, withdraw, and check balance.

class BankAccount:
    def __init__(self, account_holder, balance=0.0):
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Invalid deposit amount.")
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds or invalid amount.")
    
    def check_balance(self):
        print(f"Account holder: {self.account_holder}, Balance: {self.balance}")

# Example usage:
name = input("Enter account holder name: ")
account = BankAccount(name)

account.deposit(float(input("Enter deposit amount: ")))
account.withdraw(float(input("Enter withdrawal amount: ")))
account.check_balance()
