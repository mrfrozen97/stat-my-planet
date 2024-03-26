from bs4 import BeautifulSoup

file = open("abc.txt", "r")
html_content = file.read()

soup = BeautifulSoup(html_content)

def get_id(data):
    if data is None:
        return
    data = str(data).split("span id=\"")[1].split("\"")[0]
    print(data)
    return data

ids = []
for i in range(2, 152):
    temp = soup.find("div", {"id": "layer"+str(i)})
    ids.append(get_id(temp))
    #print(temp)

i = 0
new_ids = []
while i+4<len(ids):
    new_ids.append([ids[i], ids[i+1], ids[i+3]])
    print(i)
    i+=5

data_ids = {}
for index, i in enumerate(new_ids):
    print(i)
    data_ids["ABC"+str(index)] = {
        "population": i[0],
         "debt": i[1],
         "gdp": i[2]
    }


for i in data_ids:
    print("\""+i + "\" : " + str(data_ids[i])+",")


