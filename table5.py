# Write a program to print multiplication table of a given number 
# Get user input
num = int(input("Enter a number: "))

# Initialize counter
i = 1

# Use while loop to print multiplication table
while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1
