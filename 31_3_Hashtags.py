#	Write a function that finds all hashtags in a text.

import re

def extract_hashtags(text):
    hashtag_pattern = r'#\w+'
    hashtags = re.findall(hashtag_pattern, text)
    return hashtags

# Get input from the user
text = input("Enter the text: ")

# Extract and display hashtags
hashtags = extract_hashtags(text)
print("Extracted Hashtags:", hashtags)

