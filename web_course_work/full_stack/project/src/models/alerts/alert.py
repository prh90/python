import datetime
import uuid
import requests
import src.models.alerts.constants as AlertConstants
from src.common.database import Database


class Alert(object):
    def __init__(self, user, price_limit, item, last_checked=None, _id=None):
        self.user = user
        self.price_limit = price_limit
        self.item = item
        self.last_checked = datetime.datetime.utcnow() if last_checked is None else last_checked
        self._id = uuid.uuid4().hex if _id is None else _id

    def __repr__(self):
        return "<Alert for {} on item {} with price {}>".format(self.user.email, self.item.name, self.price_limit)

    def send(self):
        return requests.post(
            AlertConstants.URL,
            auth=("api", AlertConstants.API_KEY),
            data={
                "from": AlertConstants.FROM,
                "to": AlertConstants.FROM,
                "subject": "Price limit reached for {}".format(self.item.name),
                "text": "We've found a deal for {}! (link here)".format(self.item.price)
            }
        )

    @classmethod
    def find_needing_update(cls, minutes_since_update=AlertConstants.ALERT_TIMEOUT):
        last_updated_limit = datetime.datetime.utcnow() - datetime.timedelta(minutes=minutes_since_update)
        return [cls(**elem) for elem in Database.find(AlertConstants.COLLECTION,
                                                      {"last_checked":
                                                           {"$gte": last_updated_limit}
                                                       })]
