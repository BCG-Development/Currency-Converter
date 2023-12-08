# Currency Exchange Rate Retrieval Script

This Python script utilizes the [Free Currency API](https://freecurrencyapi.com/) to fetch and display exchange rates for a specified base currency against all other currencies.

## How it works:

1. The script prompts the user to input the base currency code (e.g., USD).
2. It loads the Free Currency API key from the `.env` file.
3. It then sends a request to the [Free Currency API](https://freecurrencyapi.com/), providing the API key and the base currency.
4. Upon successful retrieval, it filters the exchange rates for the given base currency from the API response.
5. The script creates a Pandas DataFrame with the obtained exchange rates, including the base and target currencies.
6. Finally, it displays the DataFrame showing the exchange rates.

## Usage:

1. Replace "YOUR_API_KEY" in the `.env` file with your actual Free Currency API key.
2. Run the script, and it will prompt you to input the base currency.
3. It will then fetch and display the exchange rates against all other currencies.

**Note:** Ensure you have the 'requests', 'os', 'dotenv', and 'pandas' libraries installed (`pip install requests os-dotenv pandas`) before running the script.
