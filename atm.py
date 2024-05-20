class ATM:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
        self.history = []

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            self.history.append(f"Withdrew: ${amount}")
            print(f"${amount} withdrawn successfully.")

    def deposit(self, amount):
        self.balance += amount
        self.history.append(f"Deposited: ${amount}")
        print(f"${amount} deposited successfully.")

    def transfer(self, amount, recipient_account):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            recipient_account.deposit(amount)
            self.history.append(f"Transferred: ${amount} to Account ID {id(recipient_account)}")
            print(f"${amount} transferred successfully.")

    def transaction_history(self):
        if not self.history:
            print("No transactions yet.")
        else:
            print("Transaction History:")
            for transaction in self.history:
                print(transaction)

    def quit(self):
        print("Exiting ATM interface. Have a great day!")
        exit()

def atm_interface():
    account = ATM(1000)  # Starting balance for this account
    recipient_account = ATM(500)  # Another account to demonstrate transfer

    while True:
        print("\nATM Menu:")
        print("1. Withdraw")
        print("2. Deposit")
        print("3. Transfer")
        print("4. Transaction History")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == '2':
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == '3':
            amount = float(input("Enter amount to transfer: "))
            account.transfer(amount, recipient_account)
        elif choice == '4':
            account.transaction_history()
        elif choice == '5':
            account.quit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    atm_interface()
