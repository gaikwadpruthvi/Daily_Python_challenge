# Unpack the tuple into 4 variables 
# Swap two tuples in Python 
# Copy specific elements from one tuple to a new tuple 

# Take user input for tuple elements
user_tuple = tuple(map(int, input("Enter at least 4 tuple elements separated by space: ").split()))

# 1. Unpack the tuple into 4 variables
if len(user_tuple) >= 4:
    a, b, c, d = user_tuple[:4]  # Unpacking first four elements
    print("Unpacked values:", a, b, c, d)
else:
    print("Please enter at least 4 elements to unpack.")

# 2. Swap two tuples
tuple1 = tuple(map(int, input("Enter elements for first tuple separated by space: ").split()))
tuple2 = tuple(map(int, input("Enter elements for second tuple separated by space: ").split()))

tuple1, tuple2 = tuple2, tuple1  # Swapping tuples
print("Swapped tuple1:", tuple1)
print("Swapped tuple2:", tuple2)

# 3. Copy specific elements from one tuple to a new tuple
indices = list(map(int, input("Enter indices of elements to copy (space-separated): ").split()))
new_tuple = tuple(user_tuple[i] for i in indices if i < len(user_tuple))
print("New tuple with selected elements:", new_tuple)
