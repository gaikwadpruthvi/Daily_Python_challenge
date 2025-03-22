# 	Write a Calculator class that supports addition, subtraction, multiplication, and division.

class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            return "Error! Division by zero."
        return a / b

# Example usage:
calc = Calculator()
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"Addition: {calc.add(num1, num2)}")
print(f"Subtraction: {calc.subtract(num1, num2)}")
print(f"Multiplication: {calc.multiply(num1, num2)}")
print(f"Division: {calc.divide(num1, num2)}")
