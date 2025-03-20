#	Create a function that finds the longest word in a dictionary with its length.

def longest_word(dictionary):
    if not dictionary:
        return None, 0  # Return None and 0 if dictionary is empty
    
    longest = max(dictionary, key=len)  # Find the longest word
    return longest, len(longest)

# Taking input from user
dictionary = input("Enter words separated by spaces: ").split()
word, length = longest_word(dictionary)
print(f"Longest word: {word}, Length: {length}")
