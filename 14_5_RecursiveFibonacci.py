# Implement a recursive Fibonacci function.

def fibonacci(n):
    """Recursive function to return the nth Fibonacci number."""
    if n <= 0:
        return "Invalid input! Please enter a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == "__main__":
    try:
        n = int(input("Enter the position (n) of Fibonacci number: "))
        print(f"The {n}th Fibonacci number is:", fibonacci(n))
    except ValueError:
        print("Invalid input! Please enter an integer.")
