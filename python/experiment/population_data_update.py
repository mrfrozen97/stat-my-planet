import pandas as pd
from util.worldometer_population import WorldometerPopulation

population = WorldometerPopulation("../data/populationUrls.xlsx")
population_data = {"country": [], "population": []}

data = population.get_all_population()

for country in data:
    population_data["country"].append(country)
    population_data["population"].append(data[country])

df = pd.DataFrame(population_data)
df.to_excel("../data/countryPopulationData.xlsx")
