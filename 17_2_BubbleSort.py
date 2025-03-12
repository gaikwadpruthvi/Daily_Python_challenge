# Bubble Sort

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Track if any swaps are made
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap
                swapped = True
        # If no swaps were made, the array is sorted
        if not swapped:
            break
    return arr

# Taking input from the user
try:
    user_input = input("Enter numbers separated by spaces: ")
    numbers = list(map(int, user_input.split()))
    sorted_numbers = bubble_sort(numbers)
    print("Sorted list:", sorted_numbers)
except ValueError:
    print("Invalid input. Please enter integers only.")
