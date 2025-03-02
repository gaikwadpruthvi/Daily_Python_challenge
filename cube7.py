# Take input from the user
n = int(input("Enter a number: "))

# Loop through numbers from 1 to n and calculate the cube
print("Cubes of numbers from 1 to", n, ":")
for i in range(1, n + 1):
    print(f"Cube of {i} is {i ** 3}")