#	Implement a function that finds the sum of all digits in a number recursively.


def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)  # Extract last digit and recurse

# Taking input from user
num = int(input("Enter a number: "))
result = sum_of_digits(abs(num))  # Handle negative numbers
print(f"Sum of digits: {result}")
