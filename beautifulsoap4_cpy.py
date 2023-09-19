import requests
from bs4 import BeautifulSoup

url= 'https://www.moneycontrol.com//india/stockpricequote/miscellaneous/titancompany/TI01'


respose = requests.get(url)
# print(respose)

t = respose.text
# print(t)

soup = BeautifulSoup(t,features="html.parser")
final_tag = 'UC Limit'
trs = soup.find_all("tr") #each value contains with tr tag

#print(trs[0].span.text)
# print(trs[1].index)
# print(trs[1].contents[3].text)

names =[]
values =[]

namVal = {}

# print(trs)
# print(len(trs[1].contents))
# print(len(trs))
#Extracting data in list and dictionary
for i in range(len(trs)):
    for j in range(len(trs[i].contents)):
        # print(i)
        # print(j)
        if j == 1: #name
            name = trs[i].contents[j].text
            print('name:',name)
            names.append(name)
        if j==3:
            value=trs[i].contents[j].text
            print('value:',value)
            values.append(value)
    if len(values) != 0:
        namVal[name] = value
        if name == final_tag:
            break
    
print(names)
# print(values)

print(namVal)            

