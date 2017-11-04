import sqlite3
from db import db


class UserModel(db.Model):
    __tablename__ = 'users'
    # A table created in db with columns defined below
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))
    # the properties above need to match init to save into db
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE username=?"
        result = cursor.execute(query, (username,))  # single value tuple
        row = result.fetchone()
        if row:
            user = cls(*row)  # displays the whole row
        else:
            user = None

        connection.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query, (_id,))  # single value tuple
        row = result.fetchone()
        if row:
            user = cls(*row)  # displays the whole row
        else:
            user = None

        connection.close()
        return user
