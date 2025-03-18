#	Write a program that capitalizes the first letter of each word in a string.

def capitalize_words(text):
    # Capitalize the first letter of each word
    return text.title()

# Taking input from the user
user_input = input("Enter a sentence: ")
print("Capitalized sentence:", capitalize_words(user_input))
