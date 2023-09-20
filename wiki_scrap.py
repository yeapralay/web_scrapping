import requests
from bs4 import BeautifulSoup

wikiUrl = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"

respose = requests.get(wikiUrl)
# print(respose)

t = respose.text
# print(t)

soup = BeautifulSoup(t,features="html.parser")
tbody = soup.find_all("tbody")

# print(tbody[0].contents[0])
print(tbody[0].contents[2].contents[1].text)

#Extract All the data from table
tickerSymbol = []
endSymbol = 'ZTS'

for i in range(len(tbody[0].contents)):
    if i<2:
        continue
    if i%2 != 0:
        continue
    data = tbody[0].contents[i].contents[1].text.strip('\n')
    tickerSymbol.append(data)
    if endSymbol == data:
        break

print(tickerSymbol)