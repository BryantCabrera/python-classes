class BankAccount():
    totalBalance = 0

    def __init__(self, name="", account_type="", balance=0):
        self.name = name
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.name}'s balance just rose to {self.balance}.")
        BankAccount.totalBalance += amount
        print(f"Total balance just rose to {BankAccount.totalBalance}.")

    def withdraw(self, amount):
        self.balance -= amount
        print(f"{self.name}'s balance just dropped to {self.balance}.")
        BankAccount.totalBalance -= amount
        print(f"Total balance just dropped to {BankAccount.totalBalance}.")


bryant = BankAccount('Bryant', 'savings', 4000000)
print(bryant.balance)

bryant.deposit(1000000)