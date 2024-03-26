from bs4 import BeautifulSoup
import requests
import pandas as pd

request = requests.get("https://www.worldometers.info/world-population/population-by-country/")
base_url = "https://www.worldometers.info/"
soup = BeautifulSoup(request.text)

countries = soup.find("tbody").findAll("tr")

data = {"country": [], "url": [], "class": []}

for i in countries:
    a = str(i.find_next("a"))
    if a is None:
        continue
    country = a.split(">")[1].split("<")[0]
    url = a.split("href=\"")[1].split("\"")[0]
    data["country"].append(country)
    data["url"].append(base_url+url)
    data["class"].append("rts-counter")

df = pd.DataFrame(data)
df.to_excel("../data/populationUrls.xlsx")
