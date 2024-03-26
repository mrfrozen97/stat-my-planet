import time

from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd

class WorldometerPopulation:

    def __init__(self, population_url_dir="data/populationUrls.xlsx"):
        self.driver = webdriver.Firefox()
        self.population_urls = pd.read_excel(population_url_dir)

    def get_population_data(self, country):
        row = self.population_urls[self.population_urls["country"] == country]
        print(country)
        if row.size==0:
            return "No Data"
        self.driver.get(row["url"].iloc[0])
        time.sleep(2)
        html_content = self.driver.page_source
        soup = BeautifulSoup(html_content)
        data = soup.find("span", {"class": row["class"].iloc[0]})
        print(data)
        return self.parse_population_from_woldometer_span(str(data))

    def get_all_population(self):

        data = {}
        for country in self.population_urls["country"].tolist():
            data[country] = self.get_population_data(country)
        return data

    def parse_population_from_woldometer_span(self, data):
        new_data = []
        for i in data.split("</span>"):
            temp = i.split(">")
            if len(temp) == 2:
                new_data.append(temp[1])
        return "".join(new_data)
