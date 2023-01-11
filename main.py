#This will not run on online IDE
import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.etmoney.com/mutual-funds/equity/large-cap/32')
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup)
fundname = soup.find(id='fundListing')
#print(fundname)
items=(fundname.find_all(class_='mfFund-block media'))
#itemsm=(fundname.find_all(class_='collpase-arrow'))
items1=(fundname.find_all(class_='mfFund-block media hide'))

#print(items1[16])
#print(items1[0])
#print(items1[16].find(class_='fund-name scheme-name').get_text())
#print(items[0].find(class_='fund-amount').get_text())
#print(items[0].find(class_='rating-num').get_text())
funds_names = [item.find(class_='fund-name scheme-name').get_text() for item in items]
funds_amount = [item.find(class_='fund-amount').get_text() for item in items]
funds_rating = [item.find(class_='rating-num').get_text() for item in items]
funds_name1 = [item.find(class_='fund-name scheme-name').get_text() for item in items1]
funds_amount1 = [item.find(class_='fund-amount').get_text() for item in items1]
funds_rating1 = [item.find(class_='rating-num').get_text() for item in items1]
#print(funds_name1)
#print(funds_amount1)
#print(funds_rating1)

Mutual_funds_Data = pd.DataFrame(
    {'Fund Name': funds_names ,'Fund Size':funds_amount,'Fund Rating':funds_rating,}

)
print(Mutual_funds_Data)
Mutual_funds_Data1 = pd.DataFrame(
    {'Fund Name': funds_name1 ,'Fund Size':funds_amount1,'Fund Rating':funds_rating1,}

)
print(Mutual_funds_Data1)

Mutual_funds_Data.to_csv('MutualFund.csv')
Mutual_funds_Data1.to_csv('MutualFund1.csv')