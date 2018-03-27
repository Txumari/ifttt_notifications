import requests
import time
import sys
from datetime import datetime

from database import persist_bitcoin_price, get_last_five_minutes_price

BITCOIN_PRICE_THRESHOLD = 7600

def main():
    key = sys.argv[1]

    price = get_last_five_minutes_price()
    if price:
        post_ifttt_webhook('bitcoin_price_update', round(price, 2), key)
        print('{}€'.format(price))
        return

    price = get_latest_bitcoin_price()
    persist_bitcoin_price(price)

    if price > BITCOIN_PRICE_THRESHOLD:
        post_ifttt_webhook('bitcoin_price_emergency', round(price, 2), key)
        print('{}€'.format(price))
        return

    post_ifttt_webhook('bitcoin_price_update', round(price, 2), key)
    print('{}€'.format(price))
    return


BITCOIN_API_URL = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/?convert={}'
IFTTT_WEBHOOK_URL = 'https://maker.ifttt.com/trigger/{}/with/key/{}'

def get_latest_bitcoin_price(currency='EUR'):
    response = requests.get(BITCOIN_API_URL.format(currency))
    response_json = response.json()
    return float(response_json[0]['price_{}'.format(currency.lower())])


def post_ifttt_webhook(event, value, ifttt_key):
    data = {'value1': value}
    requests.post(IFTTT_WEBHOOK_URL.format(event,ifttt_key), json=data)

 
if __name__ == '__main__':
    main()
