# python-classes
Exercise: Create Your Own Python Classes
Now that we've seen a dog-based example of Python classes, let's make one a bit more sophisticated. Create a BankAccount class.

Bank accounts should be created with the accountType property (like "savings" or "checking").
Bank accounts should have a class-level variable tracking the total amount of money in all account objects.
Each account should keep track of its own current balance.
Each account should have a deposit and a withdraw method.
Each account should start with its balance set to zero.
Things to think about:

Any starting values for variables should be set in the __init__ method
Class variables are declared inside the class but outside any methods
Instance variables are declared inside the __init__ method
Does your __init__ method need to accept any parameters?
Bonus:

Start each account with an additional overdraftFees property that starts at zero. If a call to withdraw ends with the balance below zero then overdraftFees should be incremented by twenty.
Make a ChildBankAccount class that inherits from BankAccount. The ChildBankAccount should override the withdraw method so that no overdraft fees are applied. Instead, output a message that there are insufficient funds available.