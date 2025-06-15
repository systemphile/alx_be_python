#This script contains a class for creating bankaccount objects

#define BankAccount class
class BankAccount:
    
    #Initialize
    def __init__(self, account_balance):
        self.account_balance = account_balance
        account_balance = 0
    
    #define actions
    def deposit(self, amount):
        self.account_balance += amount
    def withdraw(self, amount): #returns true if account_balance is available
        if self.account_balance >= amount:
            self.account_balance -= amount
            return True
        else:
            return False
    def display_balance(self):
        print(f"Current Balance: ${float(self.account_balance)}")