# 1.	Write a lambda function to find the square of a number.

square = lambda x: x ** 2

num = int(input("Enter a number: "))
print("Square:", square(num))


# 2.	Implement a function that filters palindromes from a list of strings.

def filter_palindromes(words):
    return list(filter(lambda word: word == word[::-1], words))

# Taking input from user
words_list = input("Enter words separated by spaces: ").split()

# Filtering palindromes
palindromes = filter_palindromes(words_list)

# Display result
print("Palindromes:", palindromes)


