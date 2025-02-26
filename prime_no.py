# Program to display all prime numbers within a given range

def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def display_primes(start, end):
    """Display all prime numbers within a given range."""
    print(f"Prime numbers between {start} and {end} are:")
    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=" ")
    print()

# Take input for the range
try:
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))

    if start > end:
        print("Invalid range: start should be less than or equal to end.")
    else:
        display_primes(start, end)
except ValueError:
    print("Invalid input: Please enter valid integers.")
