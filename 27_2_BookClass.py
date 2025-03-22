# 	Implement a Book class with methods for borrowing and returning books.

class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies  # Number of available copies
    
    def borrow_book(self):
        if self.copies > 0:
            self.copies -= 1
            print(f"You have borrowed '{self.title}' by {self.author}.")
        else:
            print(f"Sorry, '{self.title}' is currently out of stock.")
    
    def return_book(self):
        self.copies += 1
        print(f"You have returned '{self.title}' by {self.author}.")
    
    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Available Copies: {self.copies}")

# Example usage:
title = input("Enter book title: ")
author = input("Enter book author: ")
copies = int(input("Enter number of copies available: "))

book = Book(title, author, copies)
book.display_info()

# Borrowing and returning example
book.borrow_book()
book.display_info()
book.return_book()
book.display_info()
