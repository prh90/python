from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

stores = [
    {
        'name': 'My Wonderful Store',
        'items': [
            {
                'name': 'My item',
                'price': 15.99
            }
        ]
    }
]


# @app.route('/')  # 'http://www.google.com/' it is the slash
# def home():
#     return "Hello World"
#
#  POST - Used to receive data
#  GET - used to send data back only
##########################################
@app.route('/')
def home():
    return render_template('index.html')


#  POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)


#  GET /store/<string:name>
@app.route('/store/<string:name>')  # gets address name and pass it into method
def get_store(name):
    # iterate over stores if store name matches return it
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})
    # if none match return and error


#  GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})


#  POST /store/<strin:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'store not found'})


#  GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store['items'])
    return jsonify({'message': 'store not found'})


app.run(port=5000)
