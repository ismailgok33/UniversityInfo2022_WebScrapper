from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from decimal import Decimal
import re

f = open("departments-data.txt", "a")

# --------------- departments for 4 years education -------------

mainUrl = 'https://www.basarisiralamalari.com/4-yillik-bolumlerin-basari-siralamalari-taban-puanlari-osym/'
# Opens up the connection and gets the html page from it
uClient = uReq(mainUrl)
pageHtml = uClient.read()

# Closes the connection
uClient.close()

pageSoup = soup(pageHtml.decode('utf-8', 'ignore'), 'html.parser')

uniDiv = pageSoup.find('div', {'id': 'singleContent'})
uniList = uniDiv.find('ul')
allRows = uniList.findAll('li')

allURLs = []
department = ""

index = 1

for row in allRows:
    departmentLink = row.find('a')
    if departmentLink is None:
        continue
    department = departmentLink.text.split('Taban')[0]
    f.write('{0}, {1} # \n'.format(index, department.strip()))
    index = index + 1

# --------------- departments for 2 years education -------------

mainUrl2Years = 'https://www.basarisiralamalari.com/2-yillik-universite-onlisans-bolumleri/'
# Opens up the connection and gets the html page from it
uClient2 = uReq(mainUrl2Years)
pageHtml2 = uClient2.read()

# Closes the connection
uClient2.close()

pageSoup2 = soup(pageHtml2.decode('utf-8', 'ignore'), 'html.parser')

uniDiv2 = pageSoup2.find('div', {'id': 'singleContent'})
uniList2 = uniDiv2.find('ul')
allRows2 = uniList2.findAll('li')

allURLs2 = []
department2 = ""

for row in allRows2:
    departmentLink2 = row.find('a')
    if departmentLink2 is None:
        continue
    department2 = departmentLink2.text.split('Taban')[0]
    f.write('{0}, {1} # \n'.format(index, department2.strip()))
    index = index + 1

f.close()
print('success')
