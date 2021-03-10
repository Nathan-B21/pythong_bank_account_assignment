class BankAccount:
    def __init__(self, int_rate = 0.01, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdrawal(self, amount):
        if(self.balance - amount < 0):
            print("Insufficient funds: Charging a $5 fee")
            self.balance - 5
        else:
            self.balance -= amount
        return self
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
    def yield_interest(self):
        if(self.balance > 0):
            
            self.balance += (self.balance*self.int_rate)
        return self

account1 = BankAccount()
account2 = BankAccount()
account1.deposit(500).deposit(500).deposit(500).yield_interest().display_account_info()

account2.deposit(500).deposit(500).withdrawal(100).withdrawal(100).withdrawal(100).withdrawal(100).yield_interest().display_account_info()