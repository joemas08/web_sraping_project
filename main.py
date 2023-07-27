from bs4 import BeautifulSoup
import requests

url_link = "https://slickdeals.net"

result = requests.get(url_link).text

doc = BeautifulSoup(result, "html.parser")

frontpage_grid = doc.find(class_="frontpageGrid")


with open("frontpage.txt", "w") as file:
    file.write("")


with open("frontpage.txt", "w") as file:
    frontpage_items_title = frontpage_grid.find_all(class_="dealCard__title")
    frontpage_items_price = frontpage_grid.find_all(class_="dealCard__price")
    frontpage_items_original_price = frontpage_grid.find_all(class_="dealCard__originalPrice")
 

    for title, price, og_price in zip(frontpage_items_title, frontpage_items_price, frontpage_items_original_price):
        file.write(title.text + "\nSale Price: " + price.text + " \nOriginal Price: " + og_price.text + "\n\n")

