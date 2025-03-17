#	Write a function that finds the second largest element in a list.

def second_largest(nums):
    # Handle cases where the list has less than 2 elements
    if len(nums) < 2:
        return " List must have at least two distinct elements."

    # Convert to a set to remove duplicates, then sort in descending order
    unique_nums = sorted(set(nums), reverse=True)

    # Check if there are at least two distinct elements
    if len(unique_nums) < 2:
        return " There are no two distinct elements in the list."

    return unique_nums[1]  # Second largest element

# Taking input from the user
try:
    # Input list using map and split
    user_input = list(map(int, input("Enter numbers separated by spaces: ").split()))
    result = second_largest(user_input)
    print(f"Second largest element: {result}")
except ValueError:
    print(" Invalid input! Please enter valid integers.")
