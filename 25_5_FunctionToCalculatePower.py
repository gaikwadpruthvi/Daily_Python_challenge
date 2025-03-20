#	Create a function that calculates the power of a number recursively.

def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)  # Recursive multiplication

# Taking input from user
base = float(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))
result = power(base, exponent)
print(f"{base}^{exponent} = {result}")
