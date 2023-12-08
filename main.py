import requests
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

def get_exchange_rates(base_currency):
    """
    Fetch exchange rates for a given base currency using the Free Currency API.

    Args:
    - base_currency (str): The currency code for the base currency (e.g., USD).

    Returns:
    - dict: A dictionary containing exchange rates for the given base currency.
    """
    api_key = os.getenv("API_KEY")
    url = f"https://api.freecurrencyapi.com/v1/latest?apikey={api_key}"
    
    try:
        response = requests.get(url)
        data = response.json()
        rates = data['data']
        
        # Filter rates for the given base currency
        exchange_rates = {target_currency: rates[target_currency] for target_currency in rates if target_currency != base_currency}
        
        return exchange_rates
    except Exception as e:
        print(f"Error fetching exchange rates: {e}")
        print(f"Response text: {response.text}")
        return None

def main():
    """
    Main function to interact with the user and display exchange rates in a Pandas DataFrame.
    """
    base_currency = input("Enter the base currency code (e.g., USD): ").upper()

    exchange_rates = get_exchange_rates(base_currency)

    if exchange_rates is not None:
        # Create a Pandas DataFrame with the exchange rate information
        data = {'Base Currency': [base_currency] * len(exchange_rates.keys()),
                'Target Currency': list(exchange_rates.keys()),
                'Exchange Rate': list(exchange_rates.values())}
        df = pd.DataFrame(data)
        
        # Display the DataFrame
        print(df)

if __name__ == "__main__":
    main()
