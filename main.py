import requests
import pandas as pd
from bs4 import BeautifulSoup
url = "https://www.jumia.co.ke/computing/"
r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")
products = (soup.find_all("div",class_ = "name"))
#initialising an empty list to store the products
product_name = []
for i in products:
    item_name = i.text
    product_name.append(item_name)
price = (soup.find_all("div",class_ = "prc"))
#initialising an empty list to store the prices
product_price = []
for i in price:
    item_price = i.text
    product_price.append(item_price)
#(len(product_name)) != (len(product_price))
#The two arrays are not equal, hence, we are replacing missing values with NaN values using pd.Series
jumia_computing_products_data = {
    "Product Name":pd.Series(product_name),
    "Price":pd.Series(product_price)
}
df = pd.DataFrame(jumia_computing_products_data)
#print(df)
df.to_csv("jumia_computing_products_data.csv")

