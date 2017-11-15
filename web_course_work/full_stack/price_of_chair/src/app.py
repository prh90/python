import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.johnlewis.com/house-by-john-lewis-hinton-office-chair/p2083183?navAction=jump")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("span", {"itemprop": "price", "class": "now-price"})
# <span itemprop="price" class="now-price">£129.00</span>

print(element.text.strip().pop())
