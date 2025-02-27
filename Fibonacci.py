# Program to display the Fibonacci series up to n terms

def fibonacci(n):
    """Generate and display the Fibonacci series up to n terms."""
    if n <= 0:
        print("Please enter a positive integer.")
        return
    fib_sequence = [0, 1]
    for _ in range(2, n):
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)
    print(f"Fibonacci series up to {n} terms:")
    print(' '.join(map(str, fib_sequence[:n])))

# Take input from the user
try:
    terms = int(input("Enter the number of terms: "))
    fibonacci(terms)
except ValueError:
    print("Invalid input: Please enter a valid integer.")