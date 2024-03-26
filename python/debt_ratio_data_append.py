import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import json
import pandas as pd
import time


debt_data = pd.read_excel("data/countryDebtData.xlsx")
countries_data = json.load(open("../data/country_gdp.json"))

countries = debt_data["country"].tolist()
debt_ratios = debt_data["debt_percent"]
for index, country in enumerate(countries):
    countries_data[country]["debt_ratio"] = debt_ratios[index]

file = open("../data/country_gdp.json", "w")
json.dump(countries_data, file)
file.close()

