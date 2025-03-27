#  Create a s using heapq.

import heapq

def priority_queue():
    pq = []
    heapq.heappush(pq, (2, "Task 2"))
    heapq.heappush(pq, (1, "Task 1"))
    heapq.heappush(pq, (3, "Task 3"))
    
    print("Priority Queue (Min-Heap):")
    while pq:
        priority, task = heapq.heappop(pq)
        print(f"Priority: {priority}, Task: {task}")

def main():
    priority_queue()

if __name__ == "__main__":
    main()
