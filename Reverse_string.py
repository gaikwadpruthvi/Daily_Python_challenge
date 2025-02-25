def reverse_number(num):
    # Convert the number to a string, reverse it, and convert it back to an int
    reversed_num = int(str(abs(num))[::-1])
    
    # Add back the negative sign if the number was negative
    return reversed_num if num >= 0 else -reversed_num

# Get user input
num = int(input("Enter an integer: "))
print(f"Reversed number: {reverse_number(num)}")
