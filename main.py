from bs4 import BeautifulSoup
import requests

url_link = "https://slickdeals.net"

result = requests.get(url_link).text

doc = BeautifulSoup(result, "html.parser")

frontpage_grid = doc.find(class_="frontpageGrid")

frontpage_items = frontpage_grid.find_all(class_="dealCard__title")
for item in frontpage_items:
    print(item.text)

