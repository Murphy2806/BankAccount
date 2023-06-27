class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount

class SavingsBankAccount(BankAccount):
    def __init__(self, initial_balance=0):
        super().__init__(initial_balance)
        
    def pay_interest(self):
        interest = self.balance * 0.0035
        self.deposit(interest)
        
    def __repr__(self):
        return f"A SavingsBankAccount with {self.balance} dollars in it."

class HighInterestBankAccount(BankAccount):
    def __init__(self, initial_balance=0, withdrawal_fee=5):
        super().__init__(initial_balance)
        self.withdrawal_fee = withdrawal_fee
        
    def pay_interest(self):
        interest = self.balance * 0.0047
        self.deposit(interest)
        
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance - self.withdrawal_fee:
            self.balance -= amount + self.withdrawal_fee
        
    def __repr__(self):
        return f"A HighInterestBankAccount with {self.balance} dollars in it."

class LockedInBankAccount(HighInterestBankAccount):
    def __init__(self, initial_balance=0, withdrawal_fee=5):
        super().__init__(initial_balance, withdrawal_fee)
        
    def pay_interest(self):
        interest = self.balance * 0.009
        self.deposit(interest)
        
    def withdraw(self, amount):
        raise ValueError("Cannot withdraw from a LockedInBankAccount.")
        
    def __repr__(self):
        return f"A LockedInBankAccount with {self.balance} dollars in it."
