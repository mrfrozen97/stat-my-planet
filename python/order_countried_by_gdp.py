import json

country_file = open("../data/country.json", "r")
gdp_file = open("../data/country_gdp.json", "r")

data = json.load(country_file)
gdp_data = json.load(gdp_file)

data["country_data"] = data["country_data"][1:]

for index, i in enumerate(data["country_data"]):
    print(i["country_name"])
    data["country_data"][index]["gdp"] = gdp_data[str(i["country_name"])]["gdp"]


def get_order(iteam):
    return int(iteam["gdp"])

data["country_data"] = sorted(data["country_data"], key=get_order, reverse=True)
data["country_data"].insert(0, {
    "country_name": "Country",
    "population": "Population",
    "debt": "Total Debt",
    "gdp": "GDP",
    "dg_ratio": "Debt to GDP Ratio"
})

for i in data["country_data"]:
    print(i)

file = open("../data/country.json", "w")
json.dump(data, file)
file.close()


