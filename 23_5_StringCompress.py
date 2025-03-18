#	Implement a function that compresses a string using run-length encoding.

def run_length_encode(text):
    if not text:
        return ""
    
    encoded_str = ""
    count = 1

    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            encoded_str += text[i - 1] + str(count)
            count = 1

    # Add the last character sequence
    encoded_str += text[-1] + str(count)

    return encoded_str

# Taking input from the user
user_input = input("Enter a string: ")
print("Compressed string:", run_length_encode(user_input))
