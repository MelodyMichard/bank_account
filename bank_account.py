class BankAccount:

        def __init__(self, int_rate, balance):
                self.int_rate = int_rate
                self.balance = balance

        def deposit(self, amount):
                self.balance += amount
                return self

        def withdraw(self, amount):
                if(self.balance - amount) >= 0:
                        self.balance -= amount
                else:
                        print(f"Insufficient Funds: A $5 fee has been charged")
                        self.balance -= 5
                return self

        def display_account_info(self):
                print(f"Balance: {self.balance}")
                return self

        def yield_interest(self):
                if self.balance > 0:
                        self.balance += (self.balance * self.int_rate)
                return self

checking = BankAccount(.02, 200)
savings = BankAccount(.03, 500)

checking.deposit(250).deposit(200).deposit(500).withdraw(1185).yield_interest().display_account_info()
savings.deposit(50).deposit(75).withdraw(10).withdraw(50).withdraw(10).withdraw(75).yield_interest().display_account_info()

