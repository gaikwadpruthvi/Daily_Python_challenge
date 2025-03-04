#Exercise 1: Reverse a list in Python 
#Exercise 2: Concatenate two lists index-wise 

def reverse_and_concatenate(list1, list2):
    # Reverse the first list
    reversed_list1 = list1[::-1]

    # Concatenate index-wise
    concatenated_list = [a + b for a, b in zip(reversed_list1, list2)]

    return concatenated_list

# Take input from the user
list1 = input("Enter elements of first list separated by space: ").split()
list2 = input("Enter elements of second list separated by space: ").split()

# Ensure both lists are of the same length for zip() to work properly
min_length = min(len(list1), len(list2))
list1, list2 = list1[:min_length], list2[:min_length]

# Function call
result = reverse_and_concatenate(list1, list2)

# Display the result
print("Reversed List 1:", list1[::-1])
print("Concatenated List:", result)

