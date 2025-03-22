# Implement a class to model a shopping cart system.

class ShoppingCart:
    def __init__(self):
        self.items = {}  # Dictionary to store items and their quantities
    
    def add_item(self, item, quantity=1):
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity
        print(f"Added {quantity} x {item} to the cart.")
    
    def remove_item(self, item, quantity=1):
        if item in self.items:
            if self.items[item] > quantity:
                self.items[item] -= quantity
                print(f"Removed {quantity} x {item} from the cart.")
            else:
                del self.items[item]
                print(f"Removed {item} from the cart.")
        else:
            print(f"Item {item} not found in the cart.")
    
    def view_cart(self):
        if not self.items:
            print("Your shopping cart is empty.")
        else:
            print("Shopping Cart:")
            for item, quantity in self.items.items():
                print(f"{item}: {quantity}")
    
    def clear_cart(self):
        self.items.clear()
        print("Shopping cart has been cleared.")

# Example usage:
cart = ShoppingCart()
while True:
    print("\n1. Add Item\n2. Remove Item\n3. View Cart\n4. Clear Cart\n5. Exit")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        item = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        cart.add_item(item, quantity)
    elif choice == '2':
        item = input("Enter item name to remove: ")
        quantity = int(input("Enter quantity to remove: "))
        cart.remove_item(item, quantity)
    elif choice == '3':
        cart.view_cart()
    elif choice == '4':
        cart.clear_cart()
    elif choice == '5':
        print("Exiting shopping cart system.")
        break
    else:
        print("Invalid choice. Please try again.")
