# Implement a function that removes all vowels from a string.

def remove_vowels(text):
    vowels = "aeiouAEIOU"
    result = ''.join(char for char in text if char not in vowels)
    return result

# Taking input from the user
user_input = input("Enter a sentence: ")
print("Sentence without vowels:", remove_vowels(user_input))
