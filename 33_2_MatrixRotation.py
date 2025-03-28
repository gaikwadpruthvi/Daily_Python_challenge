#	Create a function that rotates a matrix by 90 degrees.

# Function to rotate a matrix by 90 degrees
def rotate_matrix_90(matrix):
    return [list(row) for row in zip(*matrix[::-1])]

# Taking input from user
def get_matrix(rows, cols):
    print(f"Enter elements for a {rows}x{cols} matrix:")
    return [[int(input(f"Element [{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]

# Get dimensions from user
rows = int(input("Enter number of rows for the matrix: "))
cols = int(input("Enter number of columns for the matrix: "))

matrix = get_matrix(rows, cols)

# Rotate the matrix by 90 degrees
rotated_matrix = rotate_matrix_90(matrix)

print("Rotated Matrix by 90 degrees:")
for row in rotated_matrix:
    print(row)
