# Parent class
class Transaction:

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    # Method that will be overridden
    def process(self):
        print("Processing a transaction")


# Child class - Deposit
class Deposit(Transaction):

    # Method overriding
    def process(self):
        print("Processing deposit transaction")

    # Method overloading using default argument
    def deposit(self, amount, source="Cash"):

        self.balance += amount

        print(f"{self.account_holder} deposited {amount}")
        print(f"Source: {source}")
        print(f"New balance: {self.balance}")


# Child class - Withdrawal
class Withdrawal(Transaction):

    # Method overriding
    def process(self):
        print("Processing withdrawal transaction")


    # Method overloading
    def withdraw(self, amount, reason="Personal use"):

        if amount <= self.balance:
            self.balance -= amount

            print(f"{self.account_holder} withdrew {amount}")
            print(f"Reason: {reason}")
            print(f"New balance: {self.balance}")

        else:
            print("Insufficient funds")


# Child class - Transfer
class Transfer(Transaction):

    # Method overriding
    def process(self):
        print("Processing transfer transaction")


    # Method overloading
    def transfer(self, amount, receiver="Another Account"):

        if amount <= self.balance:

            self.balance -= amount

            print(f"{self.account_holder} transferred {amount}")
            print(f"Receiver: {receiver}")
            print(f"Remaining balance: {self.balance}")

        else:
            print("Insufficient funds")



# -------- DEMONSTRATION --------

# Employer account
employer_deposit = Deposit("Employer", 5000)

employer_deposit.process()
employer_deposit.deposit(2000)
print("----------------")


# Withdrawal
employee_withdrawal = Withdrawal("Employer", 7000)

employee_withdrawal.process()
employee_withdrawal.withdraw(1500, "Salary payment")
print("----------------")


# Transfer
employer_transfer = Transfer("Employer", 5500)

employer_transfer.process()
employer_transfer.transfer(1000, "Employee Account")