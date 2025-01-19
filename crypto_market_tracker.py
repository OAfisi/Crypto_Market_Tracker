import requests
from prettytable import PrettyTable

# Function to fetch cryptocurrency market data from CoinGecko
def fetch_crypto_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",  # Get prices in USD
        "order": "market_cap_desc",  # Order by market cap
        "per_page": 10,  # Limit to top 10 cryptocurrencies
        "page": 1,  # First page
        "sparkline": False,  # Disable sparkline data
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an error for bad HTTP responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return []

# Function to display data in a table
def display_crypto_data(data):
    if not data:
        print("No data available.")
        return

    # Create a table to display data
    table = PrettyTable()
    table.field_names = ["Rank", "Name", "Symbol", "Price (USD)", "Market Cap (USD)", "24h Change (%)"]

    # Populate the table with cryptocurrency data
    for coin in data:
        table.add_row([
            coin["market_cap_rank"],  # Rank
            coin["name"],  # Name
            coin["symbol"].upper(),  # Symbol
            f"${coin['current_price']:,.2f}",  # Price in USD
            f"${coin['market_cap']:,.2f}",  # Market cap in USD
            f"{coin['price_change_percentage_24h']:.2f}%",  # 24h percentage change
        ])

    print(table)

# Main function
if __name__ == "__main__":
    print("Fetching cryptocurrency market data...")
    crypto_data = fetch_crypto_data()
    display_crypto_data(crypto_data)
