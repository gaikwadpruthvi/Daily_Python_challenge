#	Write a program that identifies unique elements across multiple sets.

def unique_elements(*sets):
    unique = set()
    all_elements = set()
    
    for s in sets:
        unique ^= s  # Symmetric difference to find unique elements
        all_elements |= s  # Union to track all elements
    
    return unique

# Taking input from user
num_sets = int(input("Enter the number of sets: "))
sets = []
for i in range(num_sets):
    elements = set(map(int, input(f"Enter elements of set {i+1} separated by spaces: ").split()))
    sets.append(elements)

unique_vals = unique_elements(*sets)
print("Unique elements across sets:", unique_vals)
