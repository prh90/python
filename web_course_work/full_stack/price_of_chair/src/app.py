import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.johnlewis.com/house-by-john-lewis-hinton-office-chair/p2083183?navAction=jump")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("span", {"itemprop": "price", "class": "now-price"})
# <span itemprop="price" class="now-price">£129.00</span>

string_price = element.text.strip()  # "£129.00"

price_without_symbol = string_price[1:]

price = float(price_without_symbol)

if price < 200:
    print("Buy the chair, its only {}".format(string_price))
else:
    print("Do not buy yet its {}".format(string_price))
