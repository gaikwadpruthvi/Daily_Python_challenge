#	Implement a function to check if a number is an Armstrong number.

def is_armstrong(num):
    # Convert the number to string to iterate through digits
    digits = str(num)
    power = len(digits)  # Number of digits

    # Calculate the sum of each digit raised to the power of the number of digits
    armstrong_sum = sum(int(digit) ** power for digit in digits)

    return armstrong_sum == num

# Taking input from the user
try:
    number = int(input("Enter a number to check if it's an Armstrong number: "))

    if is_armstrong(number):
        print(f" {number} is an Armstrong number!")
    else:
        print(f" {number} is NOT an Armstrong number.")
except ValueError:
    print(" Invalid input! Please enter a valid integer.")
