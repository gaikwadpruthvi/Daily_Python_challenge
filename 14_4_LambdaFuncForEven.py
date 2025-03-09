# Write a Lambda function to filter even numbers
even_numbers = lambda numbers: list(filter(lambda x: x % 2 == 0, numbers))

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print("Even numbers:", even_numbers(numbers))
