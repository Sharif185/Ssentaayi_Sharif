class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def calculate_interest(self):
        # Default interest for general account (e.g., 1%)
        interest = self.balance * 0.01
        print(f"{self.owner}'s interest: ${interest:.2f}")
        return interest


class SavingsAccount(BankAccount):
    def calculate_interest(self):
        # Savings accounts earn 4% interest
        interest = self.balance * 0.04
        print(f"{self.owner}'s savings interest: ${interest:.2f}")
        return interest


class CurrentAccount(BankAccount):
    def calculate_interest(self):
        # Current accounts earn no interest
        print(f"{self.owner}'s current account earns no interest.")
        return 0.0


# Example usage
john = BankAccount("John", 1000)
mary = SavingsAccount("Mary", 2000)
paul = CurrentAccount("Paul", 3000)

john.calculate_interest()  # Uses base method
mary.calculate_interest()  # Overridden in SavingsAccount
paul.calculate_interest()  # Overridden in CurrentAccount
