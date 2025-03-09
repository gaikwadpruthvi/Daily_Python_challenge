def prime_generator():
    """Generator function to yield prime numbers indefinitely."""
    primes = []
    num = 2
    while True:
        if all(num % prime != 0 for prime in primes):
            primes.append(num)
            yield num
        num += 1

# Example Usage
if __name__ == "__main__":
    try:
        n = int(input("Enter the number of prime numbers to generate: "))
        if n <= 0:
            print("Please enter a positive integer.")
        else:
            gen = prime_generator()
            for _ in range(n):
                print(next(gen))
    except ValueError:
        print("Invalid input! Please enter an integer.")
