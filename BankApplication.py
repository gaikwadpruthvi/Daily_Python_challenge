class BankAccount:
    def __init__(self, customer_name, customer_id):
        self.bal = 0.0
        self.prev_trans = 0.0
        self.customer_name = customer_name
        self.customer_id = customer_id

    def deposit(self, amount):
        if amount != 0:
            self.bal += amount
            self.prev_trans = amount

    def withdraw(self, amount):
        if amount != 0 and self.bal >= amount:
            self.bal -= amount
            self.prev_trans = -amount
        elif self.bal < amount:
            print("Bank balance insufficient")

    def get_previous_trans(self):
        if self.prev_trans > 0:
            print("Deposited:", self.prev_trans)
        elif self.prev_trans < 0:
            print("Withdrawn:", abs(self.prev_trans))
        else:
            print("No transaction occurred")

    def menu(self):
        print("Welcome", self.customer_name)
        print("Your ID:", self.customer_id)
        print("\n")
        print("a) Check Balance")
        print("b) Deposit Amount")
        print("c) Withdraw Amount")
        print("d) Previous Transaction")
        print("e) Exit")

        while True:
            print("********************************************")
            option = input("Choose an option: ").lower()
            print("\n")

            if option == 'a':
                print("......................")
                print("Balance =", self.bal)
                print("......................")
                print("\n")
            elif option == 'b':
                print("......................")
                amount = float(input("Enter an amount to deposit: "))
                print("......................")
                self.deposit(amount)
                print("\n")
            elif option == 'c':
                print("......................")
                amount = float(input("Enter an amount to withdraw: "))
                print("......................")
                self.withdraw(amount)
                print("\n")
            elif option == 'd':
                print("......................")
                print("Previous Transaction:")
                self.get_previous_trans()
                print("......................")
                print("\n")
            elif option == 'e':
                print("......................")
                break
            else:
                print("Choose a correct option to proceed")

        print("Thank you for using our banking services")


if __name__ == "__main__":
    name = input("Enter your 'Name' and 'CustomerId' to access your Bank account:\nName: ")
    customer_id = input("CustomerId: ")
    account = BankAccount(name, customer_id)
    account.menu()
