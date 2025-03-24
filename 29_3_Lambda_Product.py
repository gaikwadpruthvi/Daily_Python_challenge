# 	Write a program that calculates the product of all even numbers in a list using reduce().

from functools import reduce

def product_of_evens(numbers):
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    return reduce(lambda x, y: x * y, evens, 1)  # Using 1 as the initial value to handle empty lists

# Example usage
numbers_list = [2, 3, 4, 5, 6, 7, 8]
product = product_of_evens(numbers_list)
print("Product of even numbers:", product)
