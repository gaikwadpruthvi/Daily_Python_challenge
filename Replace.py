# Replace each special symbol with # in the following string

import re

def replace_special_symbols(text):
    # Replace any character that is NOT a letter, digit, or space with #
    return re.sub(r'[^A-Za-z0-9\s]', '#', text)

# Take input from the user
user_input = input("Enter a sentence: ")

# Replace special symbols
modified_text = replace_special_symbols(user_input)

# Display the result
print("Modified Text:", modified_text)
