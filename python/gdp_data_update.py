import pandas as pd
import json
import datetime
from datetime import timezone

gdp_data = pd.read_excel("../data/countryGdpData.xlsx")
data = {"Country": {"gdp": "GDP", "percent": "Percent"}}

new_year = datetime.datetime(datetime.date.today().year, 1, 1).timestamp()

countries = gdp_data["country"].tolist()
percentages = gdp_data["percent"].tolist()

def cal_gdp(base_gdp, percent):
     year_progress = (datetime.datetime.now().timestamp()-new_year)/(60*60*24*366)
     gdp = base_gdp + base_gdp*(percent/100)*year_progress
     return int(gdp)

for index, base_gdp in enumerate(gdp_data["gdp"].tolist()):

    data[countries[index]] = {"gdp": base_gdp, "percent": percentages[index]}
    print(base_gdp, data[countries[index]])

file = open("../data/country_gdp.json", "w")
json.dump(data, file)
file.close()

