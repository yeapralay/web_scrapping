import requests
from bs4 import BeautifulSoup

url= 'https://www.moneycontrol.com//india/stockpricequote/miscellaneous/titancompany/TI01'


respose = requests.get(url)
# print(respose)

t = respose.text
# print(t)

soup = BeautifulSoup(t,features="html.parser")
trs = soup.find_all("tr")

#print(trs[0].span.text)
print(trs[1].index)
print(trs[1].contents[3].text)