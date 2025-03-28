#	Implement matrix multiplication.

def matrix_multiplication(A, B):
    # Get the dimensions of the matrices
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])
    
    # Check if multiplication is possible
    if cols_A != rows_B:
        raise ValueError("Number of columns of A must match number of rows of B")
    
    # Initialize result matrix with zeros
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    
    # Perform matrix multiplication
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    
    return result

# Taking input from user
def get_matrix(rows, cols):
    print(f"Enter elements for a {rows}x{cols} matrix:")
    return [[int(input(f"Element [{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]

# Get dimensions from user
rows_A = int(input("Enter number of rows for matrix A: "))
cols_A = int(input("Enter number of columns for matrix A: "))
rows_B = int(input("Enter number of rows for matrix B: "))
cols_B = int(input("Enter number of columns for matrix B: "))

# Ensure valid matrix multiplication condition
if cols_A != rows_B:
    print("Error: Number of columns of A must match number of rows of B")
else:
    A = get_matrix(rows_A, cols_A)
    B = get_matrix(rows_B, cols_B)
    result = matrix_multiplication(A, B)
    
    print("Resultant Matrix:")
    for row in result:
        print(row)
