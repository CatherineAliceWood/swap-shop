import requests
import json


def get_item_list():
    result = requests.get(
        'http://127.0.0.1:5000/items',
        headers={'content-type': 'application/json'}
    )
    print("\nHere's our current catalogue:")
    for item in result.json():
        print(item[0])


def buy_item(item):
    requests.delete(
        'http://127.0.0.1:5000/items',
        headers={'content-type': 'application/json'},
        data=json.dumps(item)
    )
    print(f'You bought a {item}')


def sell_item(item):
    requests.post(
        'http://127.0.0.1:5000/items',
        headers={'content-type': 'application/json'},
        data=json.dumps(item)
    )
    print(f'You sold a {item}')


def run():
    print('\nHello, welcome to the Swap Shop, where you buy or sell whatever you like!')
    get_item_list()
    buy_or_sell = input('\nWould you like to buy something, or sell something (buy/sell)? ')
    if buy_or_sell == 'buy':
        item_to_buy = input('\nWhat would you like to buy? ')
        buy_item(item_to_buy)
        get_item_list()
    elif buy_or_sell == 'sell':
        item_to_sell = input('\nWhat would you like to sell? ')
        sell_item(item_to_sell)
        get_item_list()
    else:
        print('Invalid answer, please start again.')
    print('\nThank you for your custom!')


if __name__ == '__main__':
    run()

