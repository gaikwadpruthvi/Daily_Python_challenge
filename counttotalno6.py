#Using len() with str()
num = int(input("Enter a number: "))
digit_count = len(str(abs(num)))  # Convert to string and count digits
print("Total digits:", digit_count)

#Using a while loop
num = abs(int(input("Enter a number: ")))  # Absolute value to handle negatives
count = 0

if num == 0:
    count = 1  # Special case for 0
else:
    while num > 0:
        num //= 10  # Remove last digit
        count += 1

print("Total digits:", count)


#Using math.log10()
import math

num = abs(int(input("Enter a number: ")))

if num == 0:
    digit_count = 1  # Special case for 0
else:
    digit_count = math.floor(math.log10(num)) + 1

print("Total digits:", digit_count)
