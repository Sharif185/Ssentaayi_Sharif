class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def transaction(self, amount=None, recipient=None):
        if amount is None and recipient is None:
            print(f"{self.owner}'s balance: ${self.balance}")
        elif recipient is None:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            if self.balance >= amount:
                self.balance -= amount
                recipient.balance += amount
                print(f"Transferred ${amount} to {recipient.owner}")
            else:
                print("Insufficient funds for transfer.")

# Example usage
john = BankAccount("John", 100)
mary = BankAccount("Mary", 50)

john.transaction()                   # View balance
john.transaction(50)                # Deposit
john.transaction(30, mary)          # Transfer to Mary
mary.transaction()                  # Mary's updated balance
