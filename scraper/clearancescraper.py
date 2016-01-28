import requests
import re
from bs4 import BeautifulSoup
import csv

url = 'http://www.dod.gov/dodgc/doha/industrial/2015.html'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
#print soup.prettify()

caselist = soup.find('div', attrs={'class': 'case-list'})

keywordslist = []

for keyword in caselist.find_all('div', attrs={'class': 'keywords'}):
	text = keyword.text
	string = str(text)
	keywordslist.append(string)

joined = ', '.join(keywordslist)
split = joined.split('; ')
final = ', '.join(split)

finalfinal = final.split(', ')

finallist = []
for i in finalfinal:
	finallist.append([i])

datafile = open('../data/clearance.csv', 'wb')
writer = csv.writer(datafile)
writer.writerows(finallist)