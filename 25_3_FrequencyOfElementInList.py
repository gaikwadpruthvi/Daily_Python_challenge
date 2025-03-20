#	Implement a function that counts the frequency of elements in a list using a dictionary.

def count_frequencies(lst):
    frequency_dict = {}
    
    for item in lst:
        frequency_dict[item] = frequency_dict.get(item, 0) + 1  # Increment count
    
    return frequency_dict

# Taking input from user
user_input = input("Enter elements separated by spaces: ").split()
frequency = count_frequencies(user_input)

print("Element frequencies:")
for key, value in frequency.items():
    print(f"{key}: {value}")
