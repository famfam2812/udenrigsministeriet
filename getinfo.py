import json
import requests
from bs4 import BeautifulSoup

with open('url.json') as json_file:
    data = json.load(json_file)

countryinfo = []

for url in data:
    page = requests.get(url)
    print(url)



#dict = {}
    soup = BeautifulSoup(page.text, 'html.parser')

    soup2 = soup.find('div', class_='module module-country-contact countryContact')

    #for i in soup2.find_all('span', class_='newLineAddress'):
    #    info.append(i.text.replace('\r\n', '').replace(' ', ''))

    info = soup2.find_all('span', class_='newLineAddress')
    title = soup2.find('div', class_='groupTitle')

    print(title.text.strip())
    address = info[0].text.strip()
    zip = info[1].text.strip()
    telefon= info[2].text.replace('Tlf.:', '').strip()
    email = info[3].text.replace('E-mail:', '').strip()
    timeopen = info[4].text.replace('Åbningstider:', '').strip()

    print("Address:", address)
    print("Zip + postcode:", zip)
    print("Telefon:", telefon)
    print("Email:", email)
    print("Åbningstider:", timeopen)

    dictionary = {"address": address, "zipcode": zip, "telefonnummer": telefon, "email": email, "open": timeopen}
    countryinfo.append(dictionary)


final = json.dumps(countryinfo, sort_keys=True, indent=4)
print(final)

with open('info.json', 'w') as outfile:
    json.dump(countryinfo, outfile, indent=4, sort_keys=True)
#print(dictionary["zipcode"])


#print(info)

#print(soup2)