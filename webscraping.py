import pandas as pd
import requests
from bs4 import BeautifulSoup

page= requests.get('https://www.koovs.com/tags/new-lines-special-prices')
soup = BeautifulSoup(page.content, 'html.parser')
warehouse = soup.find(id ='prodBox')

items=(warehouse.find_all(class_= 'infoView'))

print(items[0].find(class_ = 'product_title clip-text productName').get_text())
print(items[0].find(class_ = 'product_price').get_text())

product_names=[item.find(class_ = 'product_title clip-text productName').get_text() for item in items]
cost=[item.find(class_ = 'product_price').get_text() for item in items]

#print(product_names)
#print(cost)

item_vs_cost = pd.DataFrame(
    {
        'Name_of_item':product_names,
        'price':cost,
    })

print(item_vs_cost)

item_vs_cost.to_csv('webscrapping.csv')