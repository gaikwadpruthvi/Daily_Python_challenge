#	Implement a function that finds the longest consecutive sequence in a list.

def longest_consecutive_sequence(nums):
    if not nums:
        return "List is empty."

    # Convert list to a set for O(1) lookup
    num_set = set(nums)
    longest_streak = 0

    for num in num_set:
        # Start counting only from the beginning of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            # Continue checking consecutive numbers
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            # Update the longest streak if found
            longest_streak = max(longest_streak, current_streak)

    return longest_streak

# Taking input from the user
try:
    user_list = list(map(int, input("Enter numbers separated by spaces: ").split()))
    print(f"Longest consecutive sequence length: {longest_consecutive_sequence(user_list)}")
except ValueError:
    print("Invalid input! Please enter valid integers.")
