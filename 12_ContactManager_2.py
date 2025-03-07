## 1. Contact Manager (Multiple Numbers per Contact)
class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone):
        if name in self.contacts:
            self.contacts[name].append(phone)
        else:
            self.contacts[name] = [phone]
        print(f"Contact {name} added successfully!")

    def search_contact(self, name):
        return self.contacts.get(name, "Contact not found!")

    def display_contacts(self):
        for name, phones in self.contacts.items():
            print(f"{name}: {', '.join(phones)}")

cm = ContactManager()
while True:
    choice = input("1: Add, 2: Search, 3: Display, 4: Exit\n")
    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        cm.add_contact(name, phone)
    elif choice == "2":
        name = input("Enter name to search: ")
        print(cm.search_contact(name))
    elif choice == "3":
        cm.display_contacts()
    elif choice == "4":
        break
