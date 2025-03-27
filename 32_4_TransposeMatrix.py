#  Write a function to transpose a matrix.

def transpose_matrix(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def main():
    # Taking matrix input from user
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    
    matrix = []
    print("Enter the matrix row by row:")
    for _ in range(rows):
        matrix.append(list(map(int, input().split())))
    
    print("Original Matrix:")
    for row in matrix:
        print(row)
    
    transposed = transpose_matrix(matrix)
    
    print("Transposed Matrix:")
    for row in transposed:
        print(row)

if __name__ == "__main__":
    main()
