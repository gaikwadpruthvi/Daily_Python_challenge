#	Implement a recursive function to solve the Tower of Hanoi problem.
def tower_of_hanoi(n, source, auxiliary, destination, moves=[0]):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        moves[0] += 1
        return
    
    tower_of_hanoi(n - 1, source, destination, auxiliary, moves)  # Move n-1 disks to auxiliary
    print(f"Move disk {n} from {source} to {destination}")  # Move nth disk to destination
    moves[0] += 1
    tower_of_hanoi(n - 1, auxiliary, source, destination, moves)  # Move n-1 disks from auxiliary to destination

# Taking input from user
num_disks = int(input("Enter the number of disks: "))
moves = [0]
tower_of_hanoi(num_disks, 'A', 'B', 'C', moves)
print(f"Total moves required: {moves[0]}")

