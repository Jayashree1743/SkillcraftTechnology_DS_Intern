import datetime
import matplotlib.pyplot as plt

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.transactions = []  # store (timestamp, type, amount, balance)

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        self._log_transaction("DEPOSIT", amount)

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        self._log_transaction("WITHDRAW", amount)

    def _log_transaction(self, t_type, amount):
        self.transactions.append(
            (datetime.datetime.now(), t_type, amount, self.balance)
        )

    def show_balance(self):
        print(f"{self.owner}'s Current Balance: ${self.balance:,.2f}")

    def plot_balance_history(self):
        if not self.transactions:
            print("No transactions to plot.")
            return
        
        timestamps = [t[0] for t in self.transactions]
        balances = [t[3] for t in self.transactions]

        plt.figure(figsize=(8,5))
        plt.plot(timestamps, balances, marker="o", linestyle="-")
        plt.title(f"{self.owner}'s Account Balance Over Time")
        plt.xlabel("Time")
        plt.ylabel("Balance ($)")
        plt.grid(True)
        plt.show()


# --- DEMO ---
if __name__ == "__main__":
    account = BankAccount("Alice", 500)
    account.deposit(200)
    account.withdraw(150)
    account.deposit(400)
    account.withdraw(100)

    account.show_balance()
    account.plot_balance_history()
