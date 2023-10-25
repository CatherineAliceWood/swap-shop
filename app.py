from flask import Flask, jsonify, request
from db_utils import get_item_list_util, buy_item_util, sell_item_util

app = Flask(__name__)


@app.route('/items')
def get_item_list_app():
    return jsonify(get_item_list_util())


@app.route('/items', methods=['DELETE'])
def buy_item_app():
    item = request.get_json()
    buy_item_util(item)
    return item


@app.route('/items', methods=['POST'])
def sell_item_app():
    item = request.get_json()
    sell_item_util(item)
    return item


if __name__ == '__main__':
    app.run(debug=True)

