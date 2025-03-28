# Write a program that finds the diagonal sum of a square matrix
def diagonal_sum(matrix):
    return sum(matrix[i][i] for i in range(len(matrix)))

# Taking input from user
def get_square_matrix(size):
    print(f"Enter elements for a {size}x{size} matrix:")
    return [[int(input(f"Element [{i}][{j}]: ")) for j in range(size)] for i in range(size)]

# Get matrix size from user
size = int(input("Enter the size of the square matrix: "))

matrix = get_square_matrix(size)

diag_sum = diagonal_sum(matrix)
print(f"Diagonal Sum: {diag_sum}")
