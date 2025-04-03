#	Write a function that converts a given date into Monday, January 1, 2024 format.

from datetime import datetime

def format_date(date_str):
    """Converts a given date string (YYYY-MM-DD) into 'Monday, January 1, 2024' format."""
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        formatted_date = date_obj.strftime("%A, %B %d, %Y")
        return formatted_date
    except ValueError:
        return "Invalid date format! Please enter in YYYY-MM-DD format."

# Example usage
date_input = input("Enter a date (YYYY-MM-DD): ")
print(format_date(date_input))
