from flask import Flask

app = Flask(__name__)

stores = [
    {
        'name': 'My wonderfule store',
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
#  POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
    pass


#  GET /store/<string:name>
@app.route('/store/<string:name>')  # gets address name and pass it into method
def get_store(name):
    pass


#  GET /store
@app.route('/store')
def get_stores():
    pass


#  POST /store/<strin:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    pass


#  GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    pass


app.run(port=5000)
