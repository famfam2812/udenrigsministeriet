import json
import requests
from bs4 import BeautifulSoup
import re

with open('url.json') as json_file:
    data = json.load(json_file)

info = []

dictionary = {}

y = 0
for url in data:

    x = 1
    y = y+1
    page = requests.get(url)

    soup = BeautifulSoup(page.text, 'html.parser')



    country = soup.find('span', class_="logo_txt").text.lower().replace('denmark in', '').replace('danmark i', '').replace('denmark in', '').replace('danamrk i', '')
    print(country)

    dictionary[country] = []


    found = soup.find_all('a', href=re.compile(r"^mailto:"))

    print(f"Found: {len(found)} on {url}")

    for a in found:
        mail = a['href'].replace('mailto:', '')
        print(f"{x}: {mail}")
        x = x+1
        dictionary[country].append(mail)


"""
    for a in soup.find_all('a', href=re.compile(r"^mailto:")):
        print(a['href'], url)
        mail = a['href'].replace('mailto:', '')

        print(f"Found {len(a)} in {url}")
        print(f"{x}: {mail}")
"""

with open('email.json', 'w') as outfile:
    json.dump(dictionary, outfile, indent=4, sort_keys=True)

print(json.dumps(dictionary, indent=4, sort_keys=True))
#print(y)




