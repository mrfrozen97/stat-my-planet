import requests
from bs4 import BeautifulSoup
import os

data = {}

def filter_data(data):
    if "(" in data:
        return data.split(" (")[0]
    return data

def add_to_data(element):
    element = str(element).split("<td>")
    if len(element) < 3:
        return
    data[element[2].split("</td>")[0].lower()]= filter_data(element[1].split("</td>")[0])

url = "https://www.iban.com/country-codes"
request = requests.get(url)
soup = BeautifulSoup(request.text)


for i in soup.findAll("tr"):
    add_to_data(i)



for country in data:
    print(country, data[country])
    old_dir = "../../resources/flags/" + country +".png"

    if os.path.exists(old_dir):

        new_file_name = data[country]+".png"

        # get the directory path of the old file
        dir_path = os.path.dirname(old_dir)

        # construct the new file path
        new_file_path = os.path.join(dir_path, new_file_name)

        # use the rename() method to rename the file
        os.rename(old_dir, new_file_path)

