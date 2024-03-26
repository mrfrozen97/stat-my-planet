import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import json
import pandas as pd
from util.worldometer_population import WorldometerPopulation



url = "https://www.usdebtclock.org/world-debt-clock.html"

population_data = pd.read_excel("data/countryPopulationData.xlsx")
debt_data = pd.read_excel("data/countryDebtData.xlsx")
gdp_data = json.load(open("../data/country_gdp.json", "r"))


def extract_number_from_span(data):
    if data == None:
        return data

    data = str(data).split(">")[1].split("<")[0]
    print(data)
    return data

def calculate_debt_gdp_ratio(debt, gdp):
    debt = int("".join(debt[1:].split(",")))
    gdp = int("".join(gdp[1:].split(",")))
    return str(((debt/gdp) * 100))[:6] + "%"



country_data = {"country_data": []}
for country in gdp_data:
    curr_data = {
        "country_name": country,
        "gdp": gdp_data[country]["gdp"],
    }
    population_row = population_data[population_data["country"] == country]["population"]
    if population_row.size>0:
        curr_data["population"] = population_row.iloc[0]

    debt_row = debt_data[debt_data["country"] == country]["debt_percent"]
    if population_row.size>0:
        curr_data["dg_ratio"] = debt_row.iloc[0]
        curr_data["debt"] = curr_data["dg_ratio"]
    country_data["country_data"].append(curr_data)

def get_integer(num):
    try:
        return int(num)
    except:
        return 0
def get_order(iteam):
    return get_integer(iteam["gdp"])

country_data["country_data"] = sorted(country_data["country_data"], key=get_order, reverse=True)
country_data["country_data"].insert(0, {
    "country_name": "Country",
    "population": "Population",
    "debt": "Total Debt",
    "gdp": "GDP",
    "dg_ratio": "Debt to GDP Ratio"
})
print(country_data["country_data"])
file = open("../data/country_all.json", "w")
json.dump(country_data, file)
file.close()
for i in country_data["country_data"]:
    print(i)
print(country_data)
