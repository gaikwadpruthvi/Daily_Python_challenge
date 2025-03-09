from collections import deque

# Stack Implementation
class Stack:
    def __init__(self):
        self.stack = deque()
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None  # or raise an exception
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
    def view_stack(self):
        return list(self.stack)

# Example Usage
if __name__ == "__main__":
    stack = Stack()
    
    while True:
        print("\nChoose operation:")
        print("1. Push to Stack")
        print("2. Pop from Stack")
        print("3. Peek Stack")
        print("4. View Full Stack")
        print("5. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            item = input("Enter item to push: ")
            stack.push(item)
        elif choice == "2":
            print("Popped from stack:", stack.pop())
        elif choice == "3":
            print("Top of stack:", stack.peek())
        elif choice == "4":
            print("Full Stack:", stack.view_stack())
        elif choice == "5":
            break
        else:
            print("Invalid choice, try again.")
