#Write a program that gracefully handles TypeError in arithmetic operations.

def safe_arithmetic_operation():
    try:
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")

        # Convert input to float (this will catch non-numeric input early)
        num1 = float(num1)
        num2 = float(num2)

        operation = input("Choose an operation (+, -, *, /): ")

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                raise ZeroDivisionError("Custom Error: Division by zero is not allowed!")
            result = num1 / num2
        else:
            raise ValueError("Invalid operation selected!")

        print(f"Result: {result}")

    except ValueError:
        print("TypeError: Invalid input! Please enter numerical values.")
    except TypeError:
        print("TypeError: Unsupported operation between given types.")
    except ZeroDivisionError as e:
        print(e)

# Example usage
safe_arithmetic_operation()
