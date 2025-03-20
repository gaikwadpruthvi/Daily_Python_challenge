#	Write a recursive function to count the number of ways to climb n stairs with steps of 1 or 2.

def count_ways(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    return count_ways(n - 1) + count_ways(n - 2)  # Recurrence relation

# Taking input from user
n = int(input("Enter the number of stairs: "))
ways = count_ways(n)
print(f"Number of ways to climb {n} stairs: {ways}")
