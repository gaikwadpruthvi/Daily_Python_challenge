# Taking input from user
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Displaying the numbers
print("Displaying the numbers:")
for num in numbers:
    print(num)
print("List in Reverse Order:")
for num in reversed(numbers):
    print(num)