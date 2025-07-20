from binance.client import Client

def send_crypto(api_key, api_secret, asset, amount, address):
    client = Client(api_key, api_secret)
    client.withdraw(coin=asset, amount=amount, address=address)
