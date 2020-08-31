from bs4 import BeautifulSoup
import json
import requests
import re

page = requests.get("https://um.dk/da/om-os/kontakt/find-os-i-verden/")

data = []

soup = BeautifulSoup(page.text, 'html.parser')

soup2 = soup.find('div', class_='col-sm-12 module richtxt')

#soup3 = soup2.find_all('a', href=True)

for i in soup2.find_all('a', href=True):
    url = i['href']
    data.append(url)
print(data)

with open('url.json', 'w') as data_file:
    json.dump(data, data_file)

