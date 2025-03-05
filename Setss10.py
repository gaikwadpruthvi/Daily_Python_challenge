# Check if two sets have any elements in common. If yes, display the common elements 
# Update set1 by adding items from set2, except common items 
# Remove items from set1 that are not common to both set1 and set2

# Get user input for two sets
set1 = set(map(int, input("Enter elements of first set separated by space: ").split()))
set2 = set(map(int, input("Enter elements of second set separated by space: ").split()))

# Exercise 7: Check if two sets have common elements and display them
common_items = set1 & set2
if common_items:
    print("Common elements in both sets:", common_items)
else:
    print("No common elements found.")

# Exercise 8: Update set1 by adding items from set2, except common items
set1.update(set2 - common_items)
print("Updated set1 after adding items from set2 except common elements:", set1)

# Exercise 9: Remove items from set1 that are not common to both sets
set1.intersection_update(set2)
print("Updated set1 after keeping only common elements:", set1)
