# Handle multiple exceptions gracefully in a division function
def safe_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except TypeError:
        return "Error: Invalid input type. Please provide numbers."
    except Exception as e:
        return f"Unexpected error: {e}"
    else:
        return f"Result: {result}"
    finally:
        print("Execution completed.")

# Example usage
print(safe_division(10, 2))   # Result: 5.0
print(safe_division(10, 0))   # Error: Division by zero is not allowed.
print(safe_division(10, 'a')) # Error: Invalid input type.
