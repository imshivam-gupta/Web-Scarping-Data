# URL="https://www.boat-lifestyle.com/collections/wireless-headphones"
URL="https://www.boat-lifestyle.com/collections/true-wireless-earbuds"
html = req.get(URL).text

# beautiful soup library
from bs4 import BeautifulSoup
data = BeautifulSoup(html,'html.parser')
data = data.find_all(class_ = "product-item__aspect-ratio aspect-ratio")
links = []
for link in data:
  links.append("https://www.boat-lifestyle.com/"+link.get("href"))
# print(links)
import re
links = [links[0],links[5]]
scrapped = []

for link in links:
  html = req.get(link).text
  data=BeautifulSoup(html,'html.parser')
  title = data.find('h1',attrs={"class":"product-meta__title heading h3"}).text.lstrip().rstrip()
  price = data.find('span',attrs={"class":"price"}).text.split("Sale price")[1].rstrip().lstrip()
  tagline = data.find('span',attrs={"class":"pdp-title-extra-info"}).text.rstrip().lstrip()
  rating = data.find('div',attrs={"class":"rating__stars"}).text.rstrip().lstrip()
  try:
    rating=float(rating)
  except ValueError:
    rating=3
  image = data.find('div',attrs={"class":"product__media-image-wrapper"}).img
  main_img_url = image['src'].split("//")[-1]
  brand = "Boat"
  seller_name ="Boat"
  seller_email = "info@imaginemarketingindia.com"
  scrapped.append([title,price,rating,tagline,brand,seller_name,seller_email,main_img_url])


import pandas as pd
df = pd.DataFrame(scrapped,columns=["Title","Price","Rating","Tagline","Brand","Seller Name","Seller Email","Image URL"])
df