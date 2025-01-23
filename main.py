import requests

def get_crypto_price(crypto_id):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": crypto_id, "vs_currencies": "usd"}
    response = requests.get(url, params=params)
    data = response.json()
    return data[crypto_id]["usd"]
    print(str(crypto))

coin_symbole = ({
    'ton' : 'the-open-network',
    'btc' : 'bitcoin',
    'eth' : 'ethereum',
    'sol' : 'solana',
    'doge': 'dogecoin'
})
def main() :
    search = input('enter name : ')
    search = search.lower()
    if search in coin_symbole :
        search = coin_symbole[search]
        price = get_crypto_price(search)
        print(f'{search} price is {price}'' $')
    else :
        price = get_crypto_price(search)
        print(f'{search} price is {price}'' $')
    main()

if __name__ == '__main__' :
    main()
