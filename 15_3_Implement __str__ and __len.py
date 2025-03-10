# Implement __str__ and __len__ methods in a Book class

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages"

    def __len__(self):
        return self.pages

# User input
title = input("Enter book title: ")
author = input("Enter author name: ")
pages = int(input("Enter number of pages: "))

book = Book(title, author, pages)

print(book)
print("Length of book:", len(book), "pages")