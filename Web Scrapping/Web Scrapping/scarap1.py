import requests

url = "https://www.moneycontrol.com//india/stockpricequote/miscellaneous/titancompany/TI01"

prop = "UC Limit" #Taking particular property for extraction

r= requests.get(url)

# Just Extracting Data from Web
# print(r)
# print(r.text)
print(r.status_code) #Printing the status_code

t = r.text
# print(t)

#Extract a particular text 

ind = t.index(prop) # extracting index
# print(ind)

redText = t[ind:ind+200]

redText_2 = t[ind:] #After Previous Close proerty all the values extracted
redText_3 = t[ind:].split('<tr>')[0]
#val = redText_3.split('>')[-1]


# print(redText)
# print(redText_2)
print(redText_3)
# print(redText_3[:3])
# print(val)