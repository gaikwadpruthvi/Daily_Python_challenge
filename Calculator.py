# Simple Calculator Program in Python

# Function to add two numbers
def add(a, b):
    return a + b

# Function to subtract two numbers
def subtract(a, b):
    return a - b

# Function to multiply two numbers
def multiply(a, b):
    return a * b

# Function to divide two numbers, with error handling for division by zero
def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

# Main calculator function

def calculator():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    # Take user input for operation choice
    choice = input("Enter choice (1/2/3/4): ")

    # Validate if choice is a valid operation
    if choice in ('1', '2', '3', '4'):
        try:
            # Take user input for numbers
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            # Handle invalid number input
            print("Invalid input. Please enter numbers only.")
            return

        # Perform the chosen operation and print the result
        if choice == '1':
            print(f"Result: {add(num1, num2)}")
        elif choice == '2':
            print(f"Result: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Result: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"Result: {divide(num1, num2)}")
    else:
        # Handle invalid operation choice
        print("Invalid choice")

# Entry point for the program
if __name__ == "__main__":
    calculator()
