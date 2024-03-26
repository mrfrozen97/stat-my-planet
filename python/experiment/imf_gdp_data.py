from bs4 import BeautifulSoup
from selenium import webdriver
import json
import pandas as pd
import time


url = "https://www.imf.org/external/datamapper/profile"

driver = webdriver.Firefox()
driver.get(url)
time.sleep(4)
html_content = driver.page_source
soup = BeautifulSoup(html_content)

def add_name_and_url(data, a):
    data["country"].append(str(a).split(">")[1].split("<")[0])
    data["url"].append(str(a).split("data-geoitem=\"")[1].split("\"")[0])

data = {"country": [], "url": []}

for a in soup.find("div", {"data-title": "Country"}).findAll("a"):
    add_name_and_url(data, a)

df = pd.DataFrame(data)
df.to_excel("../data/gdpUrls.xlsx")
