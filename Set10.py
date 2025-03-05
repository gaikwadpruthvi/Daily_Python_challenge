#Add a list of elements to a set 
#Return a new set of identical items from two sets  
#Get Only unique items from two sets
# Get user input for two sets
set1 = set(map(int, input("Enter elements of first set separated by space: ").split()))
set2 = set(map(int, input("Enter elements of second set separated by space: ").split()))

# Add multiple elements to set1 from user input
new_elements = set(map(int, input("Enter elements to add to the first set: ").split()))
set1.update(new_elements)
print("Updated set1:", set1)

# Get a new set of identical items from both sets (intersection)
common_items = set1 & set2
print("Identical items in both sets:", common_items)

# Get only unique items from both sets (symmetric difference)
unique_items = set1 ^ set2
print("Unique items from both sets:", unique_items)
