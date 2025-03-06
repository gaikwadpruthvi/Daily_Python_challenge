# Taking user input
num_str = input("Enter an integer: ")
num_float_str = input("Enter a float number: ")

# Converting string to integer
num_int = int(num_str)
print(f"String to Integer: '{num_str}' -> {num_int} (Type: {type(num_int)})")

# Converting string to float
num_float = float(num_float_str)
print(f"String to Float: '{num_float_str}' -> {num_float} (Type: {type(num_float)})")

# Converting integer to string
str_from_int = str(num_int)
print(f"Integer to String: {num_int} -> '{str_from_int}' (Type: {type(str_from_int)})")

# Converting float to integer (truncates decimal part)
int_from_float = int(num_float)
print(f"Float to Integer: {num_float} -> {int_from_float} (Type: {type(int_from_float)})")

# Converting integer to float
float_from_int = float(num_int)
print(f"Integer to Float: {num_int} -> {float_from_int} (Type: {type(float_from_int)})")

# Converting float to string
str_from_float = str(num_float)
print(f"Float to String: {num_float} -> '{str_from_float}' (Type: {type(str_from_float)})")
