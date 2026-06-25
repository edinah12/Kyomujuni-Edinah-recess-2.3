# Lab 1 Exercise 1: method overloading and overriding in a banking system
# Parent class: Transaction
# Child classes: Deposit, Withdrawal, Transfer


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def show_balance(self):
        print(f"{self.owner}'s balance: {self.balance}")


class Transaction:
    def __init__(self, amount):
        self.amount = amount

    def process(self, account, *args):
        print(f"Processing transaction of amount: {self.amount}")


class Deposit(Transaction):
    def process(self, account, *args):
        account.balance += self.amount
        print(f"Deposited {self.amount} into {account.owner}'s account.")
        account.show_balance()


class Withdrawal(Transaction):
    def process(self, account, *args):
        if self.amount > account.balance:
            print(f"Withdrawal failed: insufficient funds in {account.owner}'s account.")
            return

        account.balance -= self.amount
        print(f"Withdrew {self.amount} from {account.owner}'s account.")
        account.show_balance()


class Transfer(Transaction):
    def __init__(self, amount, target_account):
        super().__init__(amount)
        self.target_account = target_account

    def process(self, account, *args):
        if self.amount > account.balance:
            print(f"Transfer failed: insufficient funds in {account.owner}'s account.")
            return

        account.balance -= self.amount
        self.target_account.balance += self.amount
        print(
            f"Transferred {self.amount} from {account.owner}'s account to {self.target_account.owner}'s account."
        )
        account.show_balance()
        self.target_account.show_balance()


if __name__ == "__main__":
    employer_account = BankAccount("Employer", 1000)
    employee_account = BankAccount("Employee", 200)

    print("Initial balances:")
    employer_account.show_balance()
    employee_account.show_balance()

    print("\nDeposit example:")
    Deposit(300).process(employer_account)

    print("\nWithdrawal example:")
    Withdrawal(150).process(employer_account)

    print("\nTransfer example:")
    Transfer(250, employee_account).process(employer_account)
    
    # operator overloading
    
    '''
    
    
    '''
    
    #automation and webscrapping
    
    #what is automation in python?
    '''
    he auomaion pipeline:
    input ->, Transform ->, Output ->, Reliability  -> Run
    
    #ke libraries for automation in python:
    pathlib -file path
    shutil-copy,move, archive
    Scedule -task scheduling
    Wachdog - file System events monitoring
    openpyxl -excel file read/write
    '''
    
    #file automation #organising files on our compuer
    
    