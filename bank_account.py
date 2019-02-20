class BankAccount():
    totalBalance = 0

    def __init__(self, account_type="", name="", balance=0, overdraft_fees=0):
        self.account_type = account_type
        self.name = name
        self.balance = balance
        self.overdraft_fees = overdraft_fees

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.name}'s balance just rose to {self.balance}.")
        BankAccount.totalBalance += amount
        print(f"Total balance just rose to {BankAccount.totalBalance}.")

    def withdraw(self, amount):
        self.balance -= amount
        print(f"{self.name}'s balance just dropped to {self.balance}.")

        if self.balance < 0:
            self.overdraft_fees += 20
            print(f"{self.name}'s balance just dropped below 0 and {self.name} was charged $20.  You now have ${self.overdraft_fees} in overdraft fees.")

        BankAccount.totalBalance -= amount
        print(f"Total balance just dropped to {BankAccount.totalBalance}.")


# class ChildBankAccount(BankAccount):
#     def __init__(self, account_type="", ):
#         BankAccount.__init__(self)
#         print('New account made:', self)



bryant = BankAccount('savings', 'Bryant', 4000000)
print(bryant.balance)

bryant.deposit(1000000)
bryant.withdraw(6000000)