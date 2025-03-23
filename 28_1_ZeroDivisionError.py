# Write a function that raises a ZeroDivisionError with a custom message.

def divide_numbers():
    try:
        num = float(input("Enter numerator: "))
        denom = float(input("Enter denominator: "))
        if denom == 0:
            raise ZeroDivisionError("Custom Error: Division by zero is not allowed!")
        result = num / denom
        print(f"Result: {result}")
    except ZeroDivisionError as e:
        print(e)
    except ValueError:
        print("Invalid input! Please enter numerical values.")

# Example usage
divide_numbers()
