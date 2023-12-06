## Exchange Rate Retrieval Script

This Python script utilizes the Free Currency API to fetch and display the exchange rate between two specified currencies.

### How it works:

1. The script prompts the user to input the base currency code (e.g., USD) and the target currency code (e.g., EUR).
2. It then sends a request to the Free Currency API, providing the API key and the base currency.
3. Upon successful retrieval, it extracts the exchange rate for the target currency from the API response.
4. The script displays the obtained exchange rate in the format: `1 [base_currency] = [exchange_rate] [target_currency]`.

### Usage:

1. Replace “YOUR_API_KEY” with your actual Free Currency API key.
2. Run the script, and it will prompt you to input the base and target currencies.
3. It will then display the corresponding exchange rate.

Note: Ensure you have the ‘requests’ library installed (`pip install requests`) before running the script.