class BankAccount:
    def __init__(self, account_holder_name, account_number, balance):
        self.account_holder_name = account_holder_name
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount!")
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds!")
    
    def display_balance(self):
        print(f"Account Holder: {self.account_holder_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: ${self.balance}")


# Create an object and call all methods
account = BankAccount("John Doe", "123456789", 1000)

# Display initial balance
print("=== Initial Account Details ===")
account.display_balance()

# Deposit money
print("\n=== After Deposit ===")
account.deposit(500)

# Withdraw money
print("\n=== After Withdrawal ===")
account.withdraw(200)

# Display final balance
print("\n=== Final Account Details ===")
account.display_balance()
