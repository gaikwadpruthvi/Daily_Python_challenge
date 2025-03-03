'''Create a new string made of the first, middle, and last characters of each input string 
Exercise 4: Arrange string characters such that lowercase letters should come first 
Exercise 5: Count all letters, digits, and special symbols from a given string 
Exercise 6: Create a mixed String using the following rules 
Exercise 7: String characters balance Test '''

def string_operations(s, new_str):
    # First, middle, and last character
    first_middle_last = s[0] + s[len(s)//2] + s[-1]
    
    # Middle three characters
    mid_index = len(s) // 2
    middle_three = s[mid_index-1:mid_index+2] if len(s) >= 3 else s
    
    # Insert new string in the middle
    mid_pos = len(s) // 2
    modified_string = s[:mid_pos] + new_str + s[mid_pos:]
    
    return first_middle_last, middle_three, modified_string

def first_middle_last_combined(s1, s2):
    return s1[0] + s1[len(s1)//2] + s1[-1] + s2[0] + s2[len(s2)//2] + s2[-1]

def arrange_lowercase_first(s):
    return "".join(sorted(s, key=lambda x: (x.isupper(), x)))

def count_chars_digits_symbols(s):
    letters = sum(c.isalpha() for c in s)
    digits = sum(c.isdigit() for c in s)
    symbols = len(s) - letters - digits
    return letters, digits, symbols

def create_mixed_string(s1, s2):
    return "".join(a + b for a, b in zip(s1, s2)) + s1[len(s2):] + s2[len(s1):]

def string_balance_test(s1, s2):
    return all(c in s2 for c in s1)

# User input
original_string = input("Enter the original string: ")
new_string = input("Enter the new string to insert in the middle: ")
string1 = input("Enter first string: ")
string2 = input("Enter second string: ")
check_string = input("Enter string to check balance: ")
balance_with = input("Enter string to check against: ")
arrange_string = input("Enter string to arrange lowercase first: ")
count_string = input("Enter string to count letters, digits, and symbols: ")
mix_string1 = input("Enter first string for mixing: ")
mix_string2 = input("Enter second string for mixing: ")

# Processing results
result = string_operations(original_string, new_string)
print("First, middle, and last character:", result[0])
print("Middle three characters:", result[1])
print("Modified string:", result[2])
print("Combined first, middle, last characters:", first_middle_last_combined(string1, string2))
print("Arranged string with lowercase first:", arrange_lowercase_first(arrange_string))
print("Letter, digit, symbol count:", count_chars_digits_symbols(count_string))
print("Mixed String:", create_mixed_string(mix_string1, mix_string2))
print("Balance Test:", string_balance_test(check_string, balance_with))
