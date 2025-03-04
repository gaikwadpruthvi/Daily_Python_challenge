# Exercise 6: Remove empty strings from the list of strings
def remove_empty_strings(str_list):
    return [s for s in str_list if s.strip()]

# Exercise 7: Add a new item to list after a specified item
def add_item_after(list_items, specified_item, new_item):
    if specified_item in list_items:
        index = list_items.index(specified_item)
        list_items.insert(index + 1, new_item)
    return list_items

# Take input from the user for two lists (for Exercise 5)
list1 = input("Enter elements of the first list separated by space: ").split()
list2 = input("Enter elements of the second list separated by space: ").split()

# Remove empty strings from list1 (Exercise 6)
list1 = remove_empty_strings(list1)
print(f"List after removing empty strings: {list1}")

# Add a new item to list1 after a specified item (Exercise 7)
specified_item = input("Enter an item from list1 to add after: ")
new_item = input("Enter the new item to add: ")
list1 = add_item_after(list1, specified_item, new_item)
print(f"List after adding new item: {list1}")

# Iterate both lists simultaneously
print("Iterating through both lists simultaneously:")
for item1, item2 in zip(list1, list2):
    print(f"Item from list1: {item1}, Item from list2: {item2}")
