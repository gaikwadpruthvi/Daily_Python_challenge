# Modify the tuple 
# Sort a tuple of tuples by 2nd item

# Take user input for a tuple
user_tuple = tuple(map(int, input("Enter tuple elements separated by space: ").split()))

# 1. Modify the tuple (convert to list, modify, then convert back to tuple)
mod_list = list(user_tuple)
index = int(input("Enter the index to modify: "))
new_value = int(input("Enter the new value: "))

if 0 <= index < len(mod_list):
    mod_list[index] = new_value  # Modify element at the specified index
    user_tuple = tuple(mod_list)  # Convert back to tuple
    print("Modified tuple:", user_tuple)
else:
    print("Invalid index!")

# 2. Sort a tuple of tuples by the 2nd item
num_tuples = int(input("Enter the number of (x, y) pairs: "))
tuple_list = []

for _ in range(num_tuples):
    x, y = map(int, input("Enter a pair (x y): ").split())
    tuple_list.append((x, y))

sorted_tuples = sorted(tuple_list, key=lambda item: item[1])  # Sort by 2nd item
print("Sorted tuple of tuples:", sorted_tuples)
