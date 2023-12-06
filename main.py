import requests

def get_exchange_rate(base_currency, target_currency):
    api_key = "YOUR_API_KEY"  # Replace with your Free Currency API key
    url = f"https://www.freecurrencyapi.net/api/v1/rates?apikey={api_key}&base={base_currency}"
    
    try:
        response = requests.get(url)
        data = response.json()
        rate = data['data']['rates'][target_currency]
        return rate
    except Exception as e:
        print(f"Error fetching exchange rate: {e}")
        return None

def main():
    base_currency = input("Enter the base currency code (e.g., USD): ").upper()
    target_currency = input("Enter the target currency code (e.g., EUR): ").upper()

    exchange_rate = get_exchange_rate(base_currency, target_currency)

    if exchange_rate is not None:
        print(f"1 {base_currency} = {exchange_rate} {target_currency}")

if __name__ == "__main__":
    main()
