#Fetch random jokes using the requests module.

import requests

def fetch_jokes(count):
    url = f"https://official-joke-api.appspot.com/random_joke"

    try:
        for i in range(count):
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            
            joke_data = response.json()
            setup = joke_data.get('setup', 'No setup available.')
            punchline = joke_data.get('punchline', 'No punchline available.')
            
            # Display the joke
            print(f"\nJoke {i + 1}:")
            print(f"😂 {setup}")
            print(f"🤣 {punchline}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching joke: {e}")

# Taking user input
try:
    num_jokes = int(input("How many jokes would you like to hear? "))
    if num_jokes <= 0:
        print("Please enter a positive number.")
    else:
        fetch_jokes(num_jokes)
except ValueError:
    print("Invalid input. Please enter a valid number.")
