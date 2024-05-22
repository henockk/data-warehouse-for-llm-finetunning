import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://waltainfo.com/second-generation-ethiopian-diaspora-encouraged-to-contribute-to-natl-development/"

page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")

print(soup.title.text)