import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import json
import pandas as pd
from util.worldometer_population import WorldometerPopulation


url = "https://www.usdebtclock.org/world-debt-clock.html"
population_urls = pd.read_excel("data/populationUrls.xlsx")
print(population_urls)
#print(population_urls[population_urls["country"] == "USA"]["url"].iloc[0])

data_ids = {
    "USA" : {'population': 'X1a56929BW', 'debt': 'X2a5BWRG', 'gdp': 'X4a79R9BW'},
    "China" : {'population': 'M1a76329IN', 'debt': 'M2a0923KLS', 'gdp': 'M4a951MKWX'},
    "Japan" : {'population': 'R1a82529HG', 'debt': 'R2a9163KRX', 'gdp': 'R4a189MKIK'},
    "Germany" : {'population': 'E1a67529UJ', 'debt': 'E2a8263KGD', 'gdp': 'E4a59MKOP'},
    "UK" : {'population': 'H1a31529HG', 'debt': 'H2a6763MKJ', 'gdp': 'H4a17MKKN'},
    "France" : {'population': 'E1a56329CV', 'debt': 'E2a9323KMG', 'gdp': 'E4a651MKOM'},
    "India" : {'population': 'U1a21329GB', 'debt': 'U2a7623KMY', 'gdp': 'U4a391MKLNI'},
    "Italy" : {'population': 'K1a56629RE', 'debt': 'K2a4563MHD', 'gdp': 'K4a12MK6T'},
    "Brazil" : {'population': 'F1a62329FV', 'debt': 'F2a2923KNS', 'gdp': 'F4a691MKLA'},
    "Canada" : {'population': 'W1a64329TB', 'debt': 'W2a9223KMJ', 'gdp': 'W4a831MKEC'},
    "Argentina" : {'population': 'Z1a75329FV', 'debt': 'Z2a2823KEC', 'gdp': 'Z4a101MKRV'},
    "Australia" : {'population': 'L1a16329DC', 'debt': 'L2a2323KNF', 'gdp': 'L4a231MKMJ'},
    "Belgium" : {'population': 'N1a79329EV', 'debt': 'N2a3223KYN', 'gdp': 'N4a281MKWB'},
    "Greece" : {'population': 'Q1a32629OU', 'debt': 'Q2a3263MLB', 'gdp': 'Q4a36MKLP'},
    "Indonesia" : {'population': 'A1a23329VD', 'debt': 'A2a6523KLM', 'gdp': 'A4a491MKPD'},
    "Ireland" : {'population': 'T1a34329FB', 'debt': 'T2a1523KMY', 'gdp': 'T4a151MKMI'},
    "Korea" : {'population': 'Y1a12329CV', 'debt': 'Y2a6423KMG', 'gdp': 'Y4a941MKOM'},
    "Mexico" : {'population': 'P1a73329DC', 'debt': 'P2a8223KMG', 'gdp': 'P4a911MKWS'},
    "Netherlands" : {'population': 'O1a23329FV', 'debt': 'O2a6523KWB', 'gdp': 'O4a491MKLN'},
    "Nigeria" : {'population': 'XB1a6132KH', 'debt': 'XB2a212KPL', 'gdp': 'XB4a18MKPM'},
    "Norway" : {'population': 'C1a12329HN', 'debt': 'C2a6323KLB', 'gdp': 'C4a611MKEX'},
    "Poland" : {'population': 'V1a93329JM', 'debt': 'V2a2123KRV', 'gdp': 'V4a371MKMI'},
    "Portugal" : {'population': 'S1a56629BQ', 'debt': 'S2a4563KRI', 'gdp': 'S4a72M9LM'},
    "Russia" : {'population': 'G1a51329HN', 'debt': 'G2a5723KEC', 'gdp': 'G4a411MKMG'},
    "Saudi Arabia" : {'population': 'D1a41529KN', 'debt': 'D2a8563KWX', 'gdp': 'D4a289MKWA'},
    "Spain" : {'population': 'J1a31529HG', 'debt': 'J2a1463MMJ', 'gdp': 'J4a16MKLS'},
    "Sweden" : {'population': 'P1a35329SD', 'debt': 'P2a9223KEC', 'gdp': 'P4a941MKON'},
    "Switzerland" : {'population': 'I1a19329GB', 'debt': 'I2a3123KWT', 'gdp': 'I4a171MKPL'},
    "Taiwan" : {'population': 'EB1a5332EB', 'debt': 'EB2a932KMS', 'gdp': 'EB4a49MKMU'},
    "Turkey" : {'population': 'B1a52329WV', 'debt': 'B2a7523KUM', 'gdp': 'B4a281MKOL'},
}


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

def get_population_data(country):
    row = population_urls[population_urls["country"] == country]
    print(country)
    if row.size==0:
        return
    driver.get(row["url"].iloc[0])
    html_content = driver.page_source
    soup = BeautifulSoup(html_content)
    data = soup.find("span", {"class": row["class"].iloc[0]})
    print(data)
    return parse_population_from_woldometer_span(str(data))


def parse_population_from_woldometer_span(data):
    new_data = []
    for i in data.split("</span>"):
        temp = i.split(">")
        if len(temp)==2:
            new_data.append(temp[1])

    print("".join(new_data))
    return "".join(new_data)


driver = webdriver.Firefox()
# driver.get(url)
# html_content = driver.page_source
population = WorldometerPopulation()
file = open("abc.txt", "r")
html_content = file.read()
soup = BeautifulSoup(html_content)
country_data = {"country_data": []}
for country in data_ids:
    curr_data = {
        "country_name": country,
        #"population": extract_number_from_span(soup.find("span", {"id": data_ids[country]["population"]})),
        "population": population.get_population_data(country),
        "debt": extract_number_from_span(soup.find("span", {"id": data_ids[country]["debt"]})),
        "gdp": extract_number_from_span(soup.find("span", {"id": data_ids[country]["gdp"]})),
    }
    #print(country+": "+get_population_data(country))

    curr_data["dg_ratio"] = calculate_debt_gdp_ratio(curr_data["debt"], curr_data["gdp"])
    country_data["country_data"].append(curr_data)

def get_order(iteam):
    return int("".join(iteam["gdp"][1:].split(",")))

country_data["country_data"] = sorted(country_data["country_data"], key=get_order, reverse=True)
country_data["country_data"].insert(0, {
    "country_name": "Country",
    "population": "Population",
    "debt": "Total Debt",
    "gdp": "GDP",
    "dg_ratio": "Debt to GDP Ratio"
})
print(country_data["country_data"])
file = open("../data/country.json", "w")
json.dump(country_data, file)
file.close()
print(country_data)
