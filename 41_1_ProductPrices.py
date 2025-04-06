#	Implement a web scraper that tracks product prices online.

import requests
from bs4 import BeautifulSoup
import time

def get_product_price(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                      " AppleWebKit/537.36 (KHTML, like Gecko)"
                      " Chrome/91.0.4472.124 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("Failed to retrieve the page")
        return

    soup = BeautifulSoup(response.content, 'html.parser')

    # Example for http://books.toscrape.com
    title = soup.find('h1').get_text(strip=True)
    price = soup.find('p', class_='price_color').get_text(strip=True)

    print(f"Product: {title}")
    print(f"Price: {price}")

# Example usage
url = 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'

while True:
    get_product_price(url)
    time.sleep(3600)  # Wait an hour before checking again
