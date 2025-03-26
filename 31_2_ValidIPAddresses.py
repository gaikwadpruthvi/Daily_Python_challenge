#	Create a regex pattern that detects valid IP addresses.

import re

# Strict regex pattern for valid IPv4 addresses (0-255 range)
ip_pattern = r'\b((25[0-5]|2[0-4][0-9]|1?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|1?[0-9][0-9]?)\b'

def is_valid_ip(ip):
    return bool(re.fullmatch(ip_pattern, ip))

# Get user input
ip = input("Enter an IP address: ")

# Validate and display result
if is_valid_ip(ip):
    print(f"{ip} is a valid IPv4 address.")
else:
    print(f"{ip} is NOT a valid IPv4 address.")
