# Implement a function that flattens a 2D matrix into a 1D list.

def flatten_matrix(matrix):
    return [item for row in matrix for item in row]

# Taking user input
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []
print("Enter the elements row by row:")
for i in range(rows):
    row = list(map(int, input().split()))
    if len(row) != cols:
        print(f"Error: Expected {cols} elements in row {i+1}. Try again.")
        exit()
    matrix.append(row)

# Flattening the matrix
flattened = flatten_matrix(matrix)

print("Flattened list:", flattened)
