#	Write a program that calculates the cumulative sum of a list.

def cumulative_sum(nums):
    if not nums:
        return "List is empty."
    
    cum_sum = [nums[0]]  # Start with the first element
    for i in range(1, len(nums)):
        cum_sum.append(cum_sum[-1] + nums[i])  # Add previous cumulative sum + current element

    return cum_sum

# Taking input from the user
try:
    user_list = list(map(int, input("Enter numbers separated by spaces: ").split()))
    print(f"Cumulative sum: {cumulative_sum(user_list)}")
except ValueError:
    print("Invalid input! Please enter valid integers.")
