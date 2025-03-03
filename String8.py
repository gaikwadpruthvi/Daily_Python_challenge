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

# Example usage
original_string = "abcdef"
new_string = "XYZ"
result = string_operations(original_string, new_string)
print("First, middle, and last character:", result[0])
print("Middle three characters:", result[1])
print("Modified string:", result[2])
