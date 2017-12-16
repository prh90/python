import uuid
import requests
from bs4 import BeautifulSoup
import re
from src.common.database import Database
import src.models.items.constants as ItemConstants
from src.models.stores.store import Store


class Item(object):
    def __init__(self, name, url, price=None,_id=None):
        self.url = url
        store = Store.find_by_url(url)
        self.tag_name = store.tag_name
        self.query = store.query
        self.name = name
        # self.name = self.load_name(tag_name, query)
        # self.price = self.load_price(tag_name, query)
        self.price = None if price is None else price
        self._id = uuid.uuid4().hex if _id is None else _id

    def __repr__(self):
        return "<Item {} with URL {}>".format(self.name, self.url)

    def load_price(self):
        # <span id="priceblock_ourprice" class="a-size-medium a-color-price">$2,899.00</span> amazon span
        request = requests.get(self.url)
        content = request.content
        soup = BeautifulSoup(content, "html.parser")
        element = soup.find(self.tag_name, self.query)
        string_price = element.text.strip()

        pattern = re.compile("(\d+.\d+)")
        match = pattern.search(string_price)

        self.price = float(match.group())
        # return match.group()
        return self.price

    # def load_name(self, tag_name, query):
        # # <span id="priceblock_ourprice" class="a-size-medium a-color-price">$2,899.00</span> amazon span
        # request = requests.get(self.url)
        # content = request.content
        # soup = BeautifulSoup(content, "html.parser")
        # element = soup.find(tag_name, query)
        # string_price = element.text.strip()
        #
        # pattern = re.compile("(\d+.\d+)")
        # match = pattern.search(string_price)

        # return match.group()

    def save_to_mongo(self):
        Database.update(ItemConstants.COLLECTION, {'_id': self._id}, self.json())

    def json(self):
        return {
            "_id": self._id,
            "name": self.name,
            "url": self.url,
            "price": self.price
        }

    @classmethod
    def get_by_id(cls, item_id):
        return cls(**Database.find_one(ItemConstants.COLLECTION, {"_id": item_id}))
