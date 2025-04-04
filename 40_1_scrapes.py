#	Write a program that scrapes the title of a web page.

import requests
from bs4 import BeautifulSoup

def get_page_title(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
        
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string if soup.title else "No title found"
        
        return title
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

# Example usage:
url = input("Enter the URL: ")
print("Page Title:", get_page_title(url))

