# Calculate the sum of all numbers from 1 to a given number 
n = int(input("Enter a number: "))

# Initialize sum and counter
sum = 0
i = 1

# Use while loop to calculate sum
while i <= n:
    sum += i
    i += 1

# Print the result
print(f"The sum of numbers from 1 to {n} is {sum}")
