
##  Inventory Management
inventory = {}
print("Inventory Management\n")
while True:
    choice = input("1: Add Item, 2: Update Stock, 3: Display, 4: Exit\n")
    if choice == "1":
        item = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        inventory[item] = quantity
    elif choice == "2":
        item = input("Enter item name: ")
        quantity = int(input("Enter new quantity: "))
        if item in inventory:
            inventory[item] = quantity
    elif choice == "3":
        print(inventory)
    elif choice == "4":
        break
