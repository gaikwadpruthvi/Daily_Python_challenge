'''
Find all occurrences of a substring in a given string by ignoring the case 
,Calculate the sum and average of the digits present in a string  
,, Write a program to count occurrences of all characters within a string  
, Reverse a given string  
,Find the last position of a given substring
 input from user
'''

def find_substring_occurrences(text, substring):
    text_lower = text.lower()
    substring_lower = substring.lower()
    positions = []
    start = 0
    while start < len(text_lower):
        start = text_lower.find(substring_lower, start)
        if start == -1:
            break
        positions.append(start)
        start += 1
    return positions


def sum_and_avg_digits(text):
    digits = [int(ch) for ch in text if ch.isdigit()]
    if digits:
        total = sum(digits)
        avg = total / len(digits)
        return total, avg
    return 0, 0


def count_character_occurrences(text):
    occurrences = {}
    for char in text:
        occurrences[char] = occurrences.get(char, 0) + 1
    return occurrences


def reverse_string(text):
    return text[::-1]


def find_last_position(text, substring):
    return text.rfind(substring)


# Taking input from user
text = input("Enter the string: ")
substring = input("Enter the substring to search: ")

# Finding all occurrences of substring (case insensitive)
occurrences = find_substring_occurrences(text, substring)
print(f"Occurrences of '{substring}' (ignoring case): {occurrences}")

# Calculating sum and average of digits in string
total, avg = sum_and_avg_digits(text)
print(f"Sum of digits: {total}, Average of digits: {avg}")

# Counting occurrences of each character
char_counts = count_character_occurrences(text)
print("Character occurrences:")
for char, count in char_counts.items():
    print(f"{char}: {count}")

# Reversing the string
reversed_text = reverse_string(text)
print(f"Reversed string: {reversed_text}")

# Finding last position of given substring
last_position = find_last_position(text, substring)
print(f"Last position of '{substring}': {last_position}")
