# 	Implement a lambda function that finds the maximum value in a list.

find_max = lambda numbers: max(numbers)

# Taking input from user
numbers_list = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Finding maximum value
maximum_value = find_max(numbers_list)

# Display result
print("Maximum value:", maximum_value)
