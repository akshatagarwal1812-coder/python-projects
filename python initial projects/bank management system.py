import random


class Account:
    def __init__(self, account_number, account_holder_name, balance):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit successful. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient balance. Withdrawal denied.")
        else:
            self.balance -= amount
            print(f"Withdrawal successful. New balance: {self.balance}")

    def get_balance(self):
        return self.balance

    def display_account_info(self):
        print("Account Number:", self.account_number)
        print("Account Holder Name:", self.account_holder_name)
        print("Balance:", self.balance)


class SavingAccount(Account):
    def __init__(self, account_number, account_holder_name, balance, interest_rate):
        super().__init__(account_number, account_holder_name, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print(f"Interest added. New balance: {self.balance}")

    def withdraw(self, amount):
        # Savings account: no overdraft allowed at all
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient balance. Savings accounts cannot go negative.")
        else:
            super().withdraw(amount)


class CheckingAccount(Account):
    def __init__(self, account_number, account_holder_name, balance, overdraft_limit):
        super().__init__(account_number, account_holder_name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        # Checking account: can go negative up to overdraft_limit
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance + self.overdraft_limit:
            print("Withdrawal denied. Exceeds overdraft limit.")
        else:
            self.balance -= amount
            print(f"Withdrawal successful. New balance: {self.balance}")


class Bank:
    def __init__(self):
        self.all_accounts = []

    def create_account(self, account_type, account_holder_name, balance):
        account_number = random.randint(100000, 999999)

        if account_type == "saving":
            interest_rate = 3.25
            new_account = SavingAccount(account_number, account_holder_name, balance, interest_rate)
        elif account_type == "checking":
            overdraft_limit = 5000
            new_account = CheckingAccount(account_number, account_holder_name, balance, overdraft_limit)
        else:
            print("Invalid account type.")
            return

        self.all_accounts.append(new_account)
        print("Account created successfully. Account Number:", account_number)

    def find_account(self, account_number):
        for acc in self.all_accounts:
            if acc.account_number == account_number:
                return acc
        return None

    def total_balance(self):
        return sum(acc.get_balance() for acc in self.all_accounts)

    def display_all_accounts(self):
        if not self.all_accounts:
            print("No accounts yet.")
            return
        for acc in self.all_accounts:
            acc.display_account_info()
            print("-" * 20)


def main():
    bank = Bank()  # created ONCE, before the loop, so it persists across menu choices

    while True:
        print("\nEnter 1 for create account")
        print("Enter 2 for deposit")
        print("Enter 3 for withdraw")
        print("Enter 4 for display account info")
        print("Enter 5 for total balance")
        print("Enter 6 for display all accounts")
        print("Enter 7 to exit")

        choice = int(input("Your choice: "))

        if choice == 1:
            account_type = input("Enter account type (saving/checking): ")
            account_holder_name = input("Enter account holder name: ")
            balance = float(input("Enter initial balance: "))
            bank.create_account(account_type, account_holder_name, balance)

        elif choice == 2:
            account_number = int(input("Enter account number: "))
            amount = float(input("Enter deposit amount: "))
            account = bank.find_account(account_number)
            if account:
                account.deposit(amount)
            else:
                print("Account not found.")

        elif choice == 3:
            account_number = int(input("Enter account number: "))
            amount = float(input("Enter withdrawal amount: "))
            account = bank.find_account(account_number)
            if account:
                account.withdraw(amount)
            else:
                print("Account not found.")

        elif choice == 4:
            account_number = int(input("Enter account number: "))
            account = bank.find_account(account_number)
            if account:
                account.display_account_info()
            else:
                print("Account not found.")

        elif choice == 5:
            print("Total balance of all accounts:", bank.total_balance())

        elif choice == 6:
            bank.display_all_accounts()

        elif choice == 7:
            print("Exiting the program.")
            break

        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()