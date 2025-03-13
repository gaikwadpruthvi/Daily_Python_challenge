import requests
from bs4 import BeautifulSoup

def get_news_headlines(url):
    try:
        # Send a request to the news website
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses

        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract headlines (example for BBC News)
        headlines = soup.find_all('h3')

        # Display extracted headlines
        print("Latest News Headlines:\n")
        for idx, headline in enumerate(headlines[:10], start=1):  # Limiting to top 10
            print(f"{idx}. {headline.get_text(strip=True)}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Example usage
news_url = "https://www.bbc.co.uk/news"
get_news_headlines(news_url)
