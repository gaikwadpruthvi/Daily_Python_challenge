from collections import deque

def stack_operations():
    stack = deque()
    while True:
        print("\nStack Operations:")
        print("1. Push")
        print("2. Pop")
        print("3. Display")
        print("4. Exit Stack")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            element = input("Enter element to push: ")
            stack.append(element)
            print(f"{element} pushed onto stack.")
        elif choice == '2':
            if stack:
                print(f"Popped element: {stack.pop()}")
            else:
                print("Stack is empty!")
        elif choice == '3':
            print("Stack contents:", list(reversed(stack)))
        elif choice == '4':
            break
        else:
            print("Invalid choice! Try again.")

def queue_operations():
    queue = deque()
    while True:
        print("\nQueue Operations:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Display")
        print("4. Exit Queue")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            element = input("Enter element to enqueue: ")
            queue.append(element)
            print(f"{element} enqueued into queue.")
        elif choice == '2':
            if queue:
                print(f"Dequeued element: {queue.popleft()}")
            else:
                print("Queue is empty!")
        elif choice == '3':
            print("Queue contents:", list(queue))
        elif choice == '4':
            break
        else:
            print("Invalid choice! Try again.")

def main():
    while True:
        print("\nChoose a Data Structure:")
        print("1. Stack")
        print("2. Queue")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            stack_operations()
        elif choice == '2':
            queue_operations()
        elif choice == '3':
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
