#	Implement a function that prints the current date and time in YYYY-MM-DD HH:MM:SS format.

from datetime import datetime

def print_current_datetime():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(current_time)

# Call the function
print_current_datetime()
