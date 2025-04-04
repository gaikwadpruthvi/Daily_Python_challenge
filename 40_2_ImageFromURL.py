#	Create a web scraper that downloads images from a URL.

import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def download_images(url, folder="downloaded_images"):
    if not os.path.exists(folder):
        os.makedirs(folder)

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        img_tags = soup.find_all("img")

        for img in img_tags:
            img_url = img.get("src")
            if not img_url:
                continue

            full_url = urljoin(url, img_url)
            filename = os.path.join(folder, os.path.basename(full_url.split("?")[0]))

            try:
                img_data = requests.get(full_url).content
                with open(filename, "wb") as f:
                    f.write(img_data)
                print(f"Downloaded: {filename}")
            except Exception as e:
                print(f"Failed to download {full_url} - {e}")
    except Exception as e:
        print(f"Failed to fetch page - {e}")

# Prompt user for input
if __name__ == "__main__":
    user_url = input("Enter the URL of the website to scrape images from: ").strip()
    download_images(user_url)
