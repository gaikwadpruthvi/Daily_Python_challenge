#	Implement a function that queries a cryptocurrency price API.

import requests

def get_crypto_price_from_user():
    crypto_id = input("Enter the cryptocurrency ID (e.g., bitcoin, ethereum): ").lower().strip()
    currency = input("Enter the currency (e.g., usd, eur, inr): ").lower().strip()

    url = f"https://api.coingecko.com/api/v3/simple/price"
    params = {
        'ids': crypto_id,
        'vs_currencies': currency
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        price = data[crypto_id][currency]
        print(f"\n💰 The current price of {crypto_id.capitalize()} in {currency.upper()} is: {price}")
    except requests.RequestException as e:
        print(f"⚠️ Request failed: {e}")
    except KeyError:
        print(f"⚠️ Could not find price for '{crypto_id}' in '{currency}'. Please check the inputs.")

# Call the function
get_crypto_price_from_user()
