# Create a function that maps each element in a list to its factorial.

import math

def map_factorials(numbers):
    return list(map(math.factorial, numbers))

# Taking input from user
numbers_list = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Mapping factorials
factorials = map_factorials(numbers_list)

# Display result
print("Factorials:", factorials)