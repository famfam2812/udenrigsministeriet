import json
import requests
from bs4 import BeautifulSoup
import re

with open('email.json')as json_file:
    data = json.load(json_file)

print(data[' afghanistan'][0])