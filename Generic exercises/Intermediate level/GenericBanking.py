#Exercise 2: Object-Oriented Programming
#Objective: Implement a class to model a simple banking system.

#Instructions:

#Create a BankAccount class with attributes: account_number, account_holder, and balance.
#Implement methods for deposit, withdrawal, and displaying the account balance.
#Add a method to transfer money between two BankAccount instances.
#Example Task:

#Initialize two accounts: account1 and account2.
#Deposit $500 into account1.
#Withdraw $100 from account2.
#Transfer $200 from account1 to account2.
#Display the balance of both accounts.

class BankAccount():
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

#    def __str__(self):
        #return f"{self.__class__.__name__}: {", ".join([f'{key}: {value}'for key, value in self.__dict__.items()])}"
    
    def deposit(self, deposit_amount):
        print(f"Depositing: ${deposit_amount} into account: {self.account_number}")
        self.balance += deposit_amount
        print(f"New balance: ${self.balance}")
    
    def withdraw(self, withdraw_amount):
        print(f"Withdrawing: ${withdraw_amount} from account: {self.account_number}")
        self.balance -= withdraw_amount
        print(f"New balance: ${self.balance}")


    def withdraw(self, amount):
        print(f"Withdrawing: ${amount} from account: {self.account_number}")
        self.balance -= amount
        print(f"New balance: ${self.balance}")
        
    def transfer(self, amount, reciver_account):
        print(f"Tranfering: ${amount} for account: {reciver_account.account_number}")
        self.balance -= amount
        reciver_account.balance += amount
        print(f"New balance: ${self.balance}")
    
account1 = BankAccount(1, "yato", 156.52)
account2 = BankAccount(2, "master", 253.70)

account1.deposit(500)
account2.withdraw(100)
account1.transfer(200, account2)
print(account1.balance)
print(account2.balance)
