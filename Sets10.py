# Update the first set with items that don‟t exist in the second set 
# Remove items from the set at once 
# Return a set of elements present in Set A or B, but not both 

# Get user input for two sets
set1 = set(map(int, input("Enter elements of first set separated by space: ").split()))
set2 = set(map(int, input("Enter elements of second set separated by space: ").split()))

# Exercise 1: Add multiple elements to set1 from user input
new_elements = set(map(int, input("Enter elements to add to the first set: ").split()))
set1.update(new_elements)
print("Updated set1:", set1)

# Exercise 2: Get a new set of identical items from both sets (intersection)
common_items = set1 & set2
print("Identical items in both sets:", common_items)

# Exercise 3: Get only unique items from both sets (symmetric difference)
unique_items = set1 ^ set2
print("Unique items from both sets:", unique_items)

# Exercise 4: Update the first set with items that don’t exist in the second set
set1.difference_update(set2)
print("Updated set1 after removing elements present in set2:", set1)

# Exercise 5: Remove multiple items from set1 at once (user input)
remove_elements = set(map(int, input("Enter elements to remove from the first set: ").split()))
set1.difference_update(remove_elements)
print("Set1 after removing specified elements:", set1)

# Exercise 6: Return a set of elements present in Set A or B, but not both (symmetric difference)
symmetric_diff = set1 ^ set2
print("Elements present in either Set1 or Set2 but not both:", symmetric_diff)
