# Find words with both alphabets and numbers

import re

def find_alphanumeric_words(text):
    # Regular expression to match words with both letters and numbers
    pattern = r'\b(?=.*\d)[A-Za-z0-9]+\b'
    return re.findall(pattern, text)

# Take input from the user
user_input = input("Enter a sentence: ")

# Find words with both alphabets and numbers
words_with_alphanum = find_alphanumeric_words(user_input)

# Display the result
print("Words with both alphabets and numbers:", words_with_alphanum)
