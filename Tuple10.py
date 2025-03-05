# Reverse the tuple 
# Access value 20 from the tuple  
# Create a tuple with single item 50 

# Take user input for tuple elements
user_tuple = tuple(map(int, input("Enter tuple elements separated by space: ").split()))

# 1. Reverse the tuple
reversed_tuple = user_tuple[::-1]
print("Reversed tuple:", reversed_tuple)

# 2. Access value 20 from the tuple (if it exists)
if 20 in user_tuple:
    index_20 = user_tuple.index(20)
    print("Accessed value 20 at index:", index_20)
else:
    print("Value 20 not found in the tuple.")

# 3. Create a tuple with a single item (taking input from user)
single_item = int(input("Enter a single value to create a tuple: "))
single_item_tuple = (single_item,)  # Comma is necessary to define a single-element tuple
print("Single item tuple:", single_item_tuple)
