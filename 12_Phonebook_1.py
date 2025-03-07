class PhoneBook:
    def __init__(self):
        self.contacts = {}
    
    def add_contact(self, name, phone):
        self.contacts[name] = phone
        print(f"Contact {name} added successfully!")
    
    def search_contact(self, name):
        return self.contacts.get(name, "Contact not found!")
    
    def update_contact(self, name, phone):
        if name in self.contacts:
            self.contacts[name] = phone
            print(f"Contact {name} updated successfully!")
        else:
            print("Contact not found!")
    
    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact {name} deleted successfully!")
        else:
            print("Contact not found!")
    
    def display_contacts(self):
        if self.contacts:
            print("\nPhone Book:")
            for name, phone in self.contacts.items():
                print(f"{name}: {phone}")
        else:
            print("Phone book is empty!")

# User interaction
if __name__ == "__main__":
    pb = PhoneBook()
    while True:
        print("\nPhone Book Menu:")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Display Contacts")
        print("6. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            pb.add_contact(name, phone)
        elif choice == "2":
            name = input("Enter name to search: ")
            print(pb.search_contact(name))
        elif choice == "3":
            name = input("Enter name to update: ")
            phone = input("Enter new phone number: ")
            pb.update_contact(name, phone)
        elif choice == "4":
            name = input("Enter name to delete: ")
            pb.delete_contact(name)
        elif choice == "5":
            pb.display_contacts()
        elif choice == "6":
            print("Exiting phone book. Visit Again!")
            break
        else:
            print("Invalid choice. Please try again.")
