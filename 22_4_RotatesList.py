# 	Implement a function that rotates a list to the left by k steps.

def rotate_left(nums, k):
    # Handle empty lists or no rotation
    if not nums:
        return "List is empty."
    
    # Handle cases where k is greater than the list length
    k %= len(nums)  # Prevent excessive rotations

    # Perform the left rotation
    rotated_list = nums[k:] + nums[:k]

    return rotated_list

# Taking input from the user
try:
    user_list = list(map(int, input("Enter numbers separated by spaces: ").split()))
    k = int(input("Enter the number of steps to rotate: "))
    
    print(f"Rotated list: {rotate_left(user_list, k)}")
except ValueError:
    print("Invalid input! Please enter valid integers.")
