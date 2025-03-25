#  Write a Calculator class that supports addition, subtraction, multiplication, and division.
class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

# Example usage
if __name__ == "__main__":
    calc = Calculator()
    
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    operation = input("Choose operation (add, subtract, multiply, divide): ").strip().lower()
    
    if operation == "add":
        print("Result:", calc.add(a, b))
    elif operation == "subtract":
        print("Result:", calc.subtract(a, b))
    elif operation == "multiply":
        print("Result:", calc.multiply(a, b))
    elif operation == "divide":
        try:
            print("Result:", calc.divide(a, b))
        except ValueError as e:
            print(e)
    else:
        print("Invalid operation")
