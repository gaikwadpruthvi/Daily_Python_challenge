#	Implement a function that replaces multiple spaces with a single space.

import re

def remove_extra_spaces(text):
    return re.sub(r'\s+', ' ', text).strip()

# Get input from the user
text = input("Enter the text: ")

# Process and display the result
cleaned_text = remove_extra_spaces(text)
print("Text after removing extra spaces:", cleaned_text)
