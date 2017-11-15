import requests

request = requests.get("https://www.johnlewis.com/house-by-john-lewis-hinton-office-chair/p2083183?navAction=jump")

# <span itemprop="price" class="now-price">£129.00</span>

print(request.content)
