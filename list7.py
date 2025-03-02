# Take input from the user and convert it into a list
user_input = input("Enter numbers separated by spaces: ")
my_list = list(map(int, user_input.split()))

# Loop through odd index positions
print("Elements at odd index positions:")
for i in range(1, len(my_list), 2):
    print(f"Element at index {i}: {my_list[i]}")
