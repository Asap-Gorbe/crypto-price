from fileinput import filename
from datetime import datetime
import requests


def get_crypto_price(crypto_id):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": crypto_id, "vs_currencies": "usd"}
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data[crypto_id]["usd"]
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
    except KeyError:
        return None

coin_symbol = {
    'ton': 'the-open-network',
    'btc': 'bitcoin',
    'eth': 'ethereum',
    'sol': 'solana',
    'doge': 'dogecoin',
    'xrp': 'ripple',
    'bnb': 'binancecoin',
    'ada': 'cardano',
    'dot': 'polkadot',
    'usdt': 'tether',
    'ltc': 'litecoin'
}
current_time = datetime.now()
formatted_time = current_time.strftime("%H:%M:%S")
current_date = datetime.now()
formatted_date = current_date.strftime("%Y-%m-%d")

def write_to_text_file(prices, filename="crypto_prices.txt"):
    try:
        with open(filename, 'w') as file:
            file.write("Crypto currency Prices\n")
            file.write("======================\n")
            file.write(f"{formatted_date}   {formatted_time} \n")
            file.write("======================\n")
            for name, price in prices.items():
                file.write(f"{name}: {price} USD\n")
        print(f"Prices written to {filename} successfully!")
    except Exception as e:
        print(f"Error writing to file: {e}")


def main():
    all_prices = {}

    while True:
        search = input("Enter cryptocurrency name (or 'save' to save to file, 'exit' to quit): ").strip().lower()
        if search == "exit":
            print("Exiting the program. Goodbye!")
            break

        if search == "save":
            text_file_name = input('please enter the file name tou want to save ')
            if all_prices:
                write_to_text_file(all_prices,filename=text_file_name)
            else:
                print("No prices available to save. Try fetching some prices first!")
            continue


        crypto_id = coin_symbol.get(search, search)
        price = get_crypto_price(crypto_id)

        if price is not None:
            print(f"The price of {crypto_id} is {price} USD.")
            all_prices[search] = price
        else:
            print("Currency not found. Please try something else.")


if __name__ == "__main__":
    main()
