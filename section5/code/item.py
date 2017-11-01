import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',  # only defined price, any else will be deleted
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )

    @jwt_required()  # can use it for any method that needs auth
    def get(self, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items WHERE name=?"
        # item = next(filter(lambda x: x['name'] == name, items), None)
        # # None at the end is if next cant find anything else it returns none
        # return {'item': item}, 200 if item else 404
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()
        if row:
            return {'item': {'name': row[0], 'price': row[1]}}
        return {'message': 'Item not found'}, 404

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None) is not None:
            return {'message': "An item with the name '{}' already exists".format(name)}, 400

        data = Item.parser.parse_args()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201

    def delete(self, name):
        global items  # if not declared it will think items is only local
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'Item deleted'}, 200

    def put(self, name):
        data = Item.parser.parse_args()
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
        return item, 200


class ItemList(Resource):
    def get(self):
        return {'items': items}
