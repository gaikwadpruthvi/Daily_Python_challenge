# Counts the number of occurrences of item 50 from a tuple 
# Check if all items in the tuple are the same

# Take user input for a tuple
user_tuple = tuple(map(int, input("Enter tuple elements separated by space: ").split()))

# 1. Count the occurrences of item 50
count_50 = user_tuple.count(50)
print("Number of occurrences of 50:", count_50)

# 2. Check if all items in the tuple are the same
if len(set(user_tuple)) == 1:
    print("All items in the tuple are the same.")
else:
    print("Not all items in the tuple are the same.")
