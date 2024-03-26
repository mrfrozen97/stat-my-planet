import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import json
import pandas as pd
import time


population_data = pd.read_excel("data/countryPopulationData.xlsx")
countries_data = json.load(open("../data/country_gdp.json"))

countries = population_data["country"].tolist()
population_ratios = population_data["population"]

def get_filtered_value(num):
    if num == "retrieving data... ":
        return "No Data"
    return num

for index, country in enumerate(countries):
    if country in countries_data:
        countries_data[country]["population"] = get_filtered_value(population_ratios[index])

print(countries_data)
file = open("../data/country_gdp.json", "w")
json.dump(countries_data, file)
file.close()

