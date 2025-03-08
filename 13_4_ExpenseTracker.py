# Store and categorize daily expenses, allowing users to view total expenses by category.

class ExpenseTracker:
    def __init__(self):
        self.expenses = {}

    def add_expense(self, category, amount):
        if category in self.expenses:
            self.expenses[category] += amount
        else:
            self.expenses[category] = amount
        print(f"Added ${amount:.2f} to {category}.")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded yet.")
            return
        print("\nTotal Expenses by Category:")
        for category, amount in self.expenses.items():
            print(f"{category}: ${amount:.2f}")

def main():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            category = input("Enter category: ")
            amount = float(input("Enter amount: "))
            tracker.add_expense(category, amount)
        elif choice == '2':
            tracker.view_expenses()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
