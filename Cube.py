# Program to calculate the cube of all numbers from 1 to a given number

def calculate_cubes(n):
    """Calculate and display the cube of numbers from 1 to n."""
    print(f"Cubes of numbers from 1 to {n}:")
    for num in range(1, n + 1):
        print(f"{num}^3 = {num ** 3}")

# Take input from the user
try:
    number = int(input("Enter a number: "))

    if number < 1:
        print("Please enter a number greater than or equal to 1.")
    else:
        calculate_cubes(number)
except ValueError:
    print("Invalid input: Please enter a valid integer.")
