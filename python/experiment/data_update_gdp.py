import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import json
import pandas as pd
import time


base_url = "https://www.imf.org/external/datamapper/profile/"
gdp_urls = pd.read_excel("../data/gdpUrls.xlsx")
print(gdp_urls)

def extract_value_from_div(data):
    if data is None:
        return "0"
    return str(data).split(">")[1].split("<")[0]

def get_number(number):
    try:
        return float(number)
    except:
        return 0

def calculate_number(value, unit):
    multiplier = 1000000000
    value = get_number(value)

    if unit == "thousand":
        return multiplier*value*1000
    else:
        return multiplier*value

driver = webdriver.Firefox()
country_data = {"country": [], "gdp": [], "percent": []}

country_names = gdp_urls["country"].tolist()
for index,a in enumerate(gdp_urls["url"].tolist()):
    url = base_url + a
    print(url)
    driver.get(url)
    time.sleep(4)
    html_content = driver.page_source
    soup = BeautifulSoup(html_content)

    value = extract_value_from_div(soup.find("imf-indicator-panel", {"indicator": "NGDPD"}).find("div", {"class": "value"}))
    unit = extract_value_from_div(soup.find("imf-indicator-panel", {"indicator": "NGDPD"}).find("div", {"class": "wordify"}))
    percent = extract_value_from_div(soup.find("imf-indicator-panel", {"indicator": "NGDP_RPCH"}).find("div", {"class": "value"}))
    print(value)
    print(unit)
    print(percent, get_number(percent))
    number = calculate_number(value, unit)
    country_data["country"].append(country_names[index])
    country_data["gdp"].append(int(number))
    country_data["percent"].append(get_number(percent))
    print(number)

df = pd.DataFrame(country_data)
df.to_excel("../data/countryGdpData.xlsx")
