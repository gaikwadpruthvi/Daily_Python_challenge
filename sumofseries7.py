# Find the sum of the series upto n terms 
def sum_natural(n):
    return (n * (n + 1)) // 2

def sum_squares(n):
    return (n * (n + 1) * (2 * n + 1)) // 6

def sum_cubes(n):
    return ((n * (n + 1)) // 2) ** 2

def sum_geometric(n, r):
    return (1 - r ** n) / (1 - r) if r != 1 else n

# Main function
def main():
    print("Choose a series to sum:")
    print("1. Sum of first N natural numbers")
    print("2. Sum of squares of first N numbers")
    print("3. Sum of cubes of first N numbers")
    print("4. Sum of geometric series")

    choice = int(input("Enter your choice (1-4): "))
    n = int(input("Enter the number of terms (n): "))

    if choice == 1:
        print(f"Sum of first {n} natural numbers: {sum_natural(n)}")
    elif choice == 2:
        print(f"Sum of squares of first {n} numbers: {sum_squares(n)}")
    elif choice == 3:
        print(f"Sum of cubes of first {n} numbers: {sum_cubes(n)}")
    elif choice == 4:
        r = float(input("Enter the common ratio (r): "))
        print(f"Sum of geometric series: {sum_geometric(n, r)}")
    else:
        print("Invalid choice! Please select a valid option.")

# Run the program
if __name__ == "__main__":
    main()
