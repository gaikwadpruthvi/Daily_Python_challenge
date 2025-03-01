# Factorial Calculation in Different Ways

import math

def factorial_iterative(num):
    """Calculates factorial using a for loop."""
    factorial = 1
    if num < 0:
        return "Factorial is not defined for negative numbers."
    elif num == 0 or num == 1:
        return 1
    else:
        for i in range(1, num + 1):
            factorial *= i
        return factorial

def factorial_recursive(n):
    """Calculates factorial using recursion."""
    if n < 0:
        return "Factorial is not defined for negative numbers."
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

def factorial_math(num):
    """Calculates factorial using math module."""
    if num < 0:
        return "Factorial is not defined for negative numbers."
    return math.factorial(num)

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    
    print("Factorial using Iterative Method:", factorial_iterative(num))
    print("Factorial using Recursion:", factorial_recursive(num))
    print("Factorial using math.factorial():", factorial_math(num))
