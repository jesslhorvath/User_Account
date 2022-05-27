"""
Author: Jessie Horvath
Program: user_account.py and user_account_tests.py
Date Modified: 05/27/2022

The purpose of this program is to create a bank account class with 
attributes, deposit/withdrawl methods, and unit tests to test the class and 
objects created from the class. 
"""
class user_account():
    def __init__(self, account_type, account_owner, account_num, account_balance):
        self.type = account_type
        self.owner = account_owner
        self.number = account_num
        self.balance = account_balance

    def deposit(self, amount):
        new_balance = self.balance + amount
        self.balance = new_balance
        return f"Deposited ${amount}, New balance:${self.balance}"

    def withdrawal(self, amount):
        new_balance = self.balance - amount
        if new_balance < 0:
            return "Not enough funds to withdraw that amount"
        else:
            self.balance = new_balance
            return f"Withdrew ${amount}, New balance:${self.balance}"

    def display(self):
        return f"Account type: {self.type}\nAccount owner: {self.owner}\nAccount number: {self.number}\nAccount balance: ${self.balance:.2f}"


if __name__ == '__main__':
    account1 = user_account("Checking", "Jessie Horvath", 14, 0)

    account1.deposit(400)
    account1.withdrawal(250)
    print(account1.display())

    account2 = user_account("Savings", "Jessie Horvath", 15, 0)
    account2.deposit(50)
    print(account2.withdrawal(100))
    print(account2.display())