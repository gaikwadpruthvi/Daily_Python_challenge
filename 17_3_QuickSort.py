# Quick Sort


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]  # Choosing the first element as the pivot
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

try:
    user_input = input("Enter numbers separated by spaces: ")
    numbers = list(map(int, user_input.split()))
    sorted_numbers = quick_sort(numbers)
    print("Sorted list:", sorted_numbers)
except ValueError:
    print("Invalid input. Please enter integers only.")
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]  # Choosing the first element as the pivot
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

# Taking input from the user
try:
    user_input = input("Enter numbers separated by spaces: ")
    numbers = list(map(int, user_input.split()))
    sorted_numbers = quick_sort(numbers)
    print("Sorted list:", sorted_numbers)
except ValueError:
    print("Invalid input. Please enter integers only.")
