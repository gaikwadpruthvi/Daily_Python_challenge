#Create a program that calculates the factorial of a given number using iteration.

def factorial(n):
    # Factorial is undefined for negative numbers
    if n < 0:
        return " Factorial is not defined for negative numbers."
    
    result = 1  # Start with 1 since factorial of 0 is 1
    for i in range(1, n + 1):
        result *= i  # Multiply each number in the range

    return result

# Taking input from the user
try:
    number = int(input("Enter a number to calculate its factorial: "))
    print(f"Factorial of {number} is {factorial(number)}")
except ValueError:
    print(" Invalid input! Please enter a valid integer.")
