from collections import deque

# Queue Implementation
class Queue:
    def __init__(self):
        self.queue = deque()
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        return None  # or raise an exception
    
    def front(self):
        if not self.is_empty():
            return self.queue[0]
        return None
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    
    def view_queue(self):
        return list(self.queue)

# Example Usage
if __name__ == "__main__":
    queue = Queue()
    
    while True:
        print("\nChoose operation:")
        print("1. Enqueue to Queue")
        print("2. Dequeue from Queue")
        print("3. Front of Queue")
        print("4. View Full Queue")
        print("5. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            item = input("Enter item to enqueue: ")
            queue.enqueue(item)
        elif choice == "2":
            print("Dequeued from queue:", queue.dequeue())
        elif choice == "3":
            print("Front of queue:", queue.front())
        elif choice == "4":
            print("Full Queue:", queue.view_queue())
        elif choice == "5":
            break
        else:
            print("Invalid choice, try again.")
