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
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        #
        # query = "SELECT * FROM items WHERE name=?"
        # # item = next(filter(lambda x: x['name'] == name, items), None)
        # # None at the end is if next cant find anything else it returns none
        # # return {'item': item}, 200 if item else 404
        # result = cursor.execute(query, (name,))
        # row = result.fetchone()
        # connection.close()
        # if row:
        #     return {'item': {'name': row[0], 'price': row[1]}}
        item = self.find_by_name(name)
        if item:
            return item
        return {'message': 'Item not found'}, 404

    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()
        if row:
            return {'item': {'name': row[0], 'price': row[1]}}



    def post(self, name):
        if self.find_by_name(name):
            return {'message': "An item with the name '{}' already exists".format(name)}, 400

        # if next(filter(lambda x: x['name'] == name, items), None) is not None:
            # return {'message': "An item with the name '{}' already exists".format(name)}, 400

        data = Item.parser.parse_args()
        item = {'name': name, 'price': data['price']}

        try:
            self.insert(item)
        except:
            return {"message": "An error has occured inserting the item."}, 500
            # 500 = internal server error
        return item, 201

    @classmethod
    def insert(cls, item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO items VALUES (?, ?)"
        cursor.execute(query, (item['name'], item['price']))

        connection.commit()
        connection.close()

    def delete(self, name):
        # items = list(filter(lambda x: x['name'] != name, items))
        if self.find_by_name(name):
            connection = sqlite3.connect('data.db')
            cursor = connection.cursor()

            query = "DELETE FROM items WHERE name=?"
            cursor.execute(query, (name,))

            connection.commit()
            connection.close()

            return {'message': 'Item deleted'}, 200
        return {'message': "Item not found, item not deleted"}, 404

    def put(self, name):
        data = Item.parser.parse_args()
        item = self.find_by_name(name)
        # item = next(filter(lambda x: x['name'] == name, items), None)
        updated_item = {'name': name, 'price': data['price']}

        if item is None:
            try:
                self.insert(updated_item)
            except:
                return {"message": "An error occured inserting the item"}, 500
        else:
            try:
                self.update(updated_item)
            except:
                return {"message": "An error occured updating the item"}, 500
        return updated_item, 200

    @classmethod
    def update(cls, item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "UPDATE items SET price=? WHERE name=?"
        cursor.execute(query, (item['price'], item['name']))

        connection.commit()
        connection.close()


class ItemList(Resource):
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items"
        result = cursor.execute(query)
        items = []
        for row in result:
            items.append({'name': row[0], 'price': row[1]})

        connection.close()

        return {'items': items}
