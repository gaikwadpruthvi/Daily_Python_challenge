# Email Validation#
import re

def validate_email(email):
    # Email regex pattern
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

# Taking multiple email inputs from the user
emails = input("Enter email addresses separated by spaces: ").split()

print("\nEmail Validation Results:")
for email in emails:
    status = "Valid" if validate_email(email) else "Invalid"
    print(f"{email}: {status}")
