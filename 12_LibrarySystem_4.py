## Library System
library = {}
print("Library System\n")
while True:
    

    choice = input("1: Add Book, 2: Borrow Book, 3: Return Book, 4: Display, 5: Exit\n")
    if choice == "1":
        book = input("Enter book title: ")
        library[book] = "Available"
    elif choice == "2":
        book = input("Enter book title to borrow: ")
        if library.get(book) == "Available":
            library[book] = "Borrowed"
            print("Book borrowed successfully.")
        else:
            print("Book not available.")
    elif choice == "3":
        book = input("Enter book title to return: ")
        library[book] = "Available"
    elif choice == "4":
        print(library)
    elif choice == "5":
        break