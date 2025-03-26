#	Implement a function that extracts URLs from a given text.

import re

def extract_urls(text):
    url_pattern = r'https?://(?:www\.)?\S+'
    urls = re.findall(url_pattern, text)
    return urls

# Get input from the user
text = input("Enter the text: ")

# Extract and display URLs
urls = extract_urls(text)
print("Extracted URLs:", urls)
