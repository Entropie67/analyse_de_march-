"""Choisissez n'importe quelle page Produit sur le site de Books to Scrape. Écrivez un script Python qui visite cette page et en extrait les informations suivantes :

product_page_url
universal_ product_code (upc)
title
price_including_tax
price_excluding_tax
number_available
product_description
category
review_rating
image_url"""

import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/catalogue/sophies-world_966/index.html"

req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")

print(soup)