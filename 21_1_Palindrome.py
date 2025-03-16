# Write a function that checks if a given string is a palindrome (case insensitive).

def is_palindrome(s):
    # Remove spaces and convert to lowercase for case insensitivity
    cleaned_str = ''.join(char.lower() for char in s if char.isalnum())
    
    # Check if cleaned string is equal to its reverse
    return cleaned_str == cleaned_str[::-1]

# Taking input from the user
user_input = input("Enter a string to check for palindrome: ")

# Checking and displaying the result
if is_palindrome(user_input):
    print(f'"{user_input}" is a palindrome!')
else:
    print(f'"{user_input}" is NOT a palindrome.')
