# Write a program that calculates the number of days between two dates.

from datetime import datetime
from dateutil.relativedelta import relativedelta  # Requires `pip install python-dateutil`

# Function to calculate time difference between two dates
def time_difference(date1, date2):
    date_format = "%Y-%m-%d %H:%M:%S"  # Expected format: YYYY-MM-DD HH:MM:SS
    d1 = datetime.strptime(date1, date_format)
    d2 = datetime.strptime(date2, date_format)
    
    delta = abs(d2 - d1)  # Absolute time difference
    months = abs(relativedelta(d2, d1).months + (relativedelta(d2, d1).years * 12))  # Months difference
    
    return {
        "Days": delta.days,
        "Hours": delta.total_seconds() // 3600,
        "Minutes": delta.total_seconds() // 60,
        "Weeks": delta.days // 7,
        "Months": months
    }

# Taking input from the user
date1 = input("Enter the first date (YYYY-MM-DD HH:MM:SS): ")
date2 = input("Enter the second date (YYYY-MM-DD HH:MM:SS): ")

# Calculating the difference
result = time_difference(date1, date2)

# Displaying results
print("\nTime Difference:")
for unit, value in result.items():
    print(f"{unit}: {int(value)}")
