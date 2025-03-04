# Take input from the user
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Square each item in the list
squared_numbers = [num ** 2 for num in numbers]

# Display the result
print("Squared List:", squared_numbers)