from src.common.database import Database
from src.models.alerts.alert import Alert
import schedule

Database.initialize()

alerts_needing_update = Alert.find_needing_update()


def update():
    for alert in alerts_needing_update:
        alert.load_item_price()
        alert.send_email_if_price_reached()


schedule.every().day.at("00:00").do(update)
schedule.every().day.at("06:00").do(update)
schedule.every().day.at("12:00").do(update)
schedule.every().day.at("18:00").do(update)




