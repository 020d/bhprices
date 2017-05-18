#!/usr/local/bin/python3
from lxml import html
import requests

headers = {'user-agent': 'Firefox Safari Whatevz'}
rooturl = 'https://www.blackhat.com/us-17/training/'
page = requests.get(rooturl+'index.html', headers=headers)
tree = html.fromstring(page.content)
desc = tree.xpath('//div[contains(@class,"course-description")]/h2/a')

for div in desc:
	title = div.text
	divref = div.attrib['href']
	coursepage = requests.get(rooturl+divref, headers=headers)
	classtree = html.fromstring(coursepage.content)
	price = classtree.xpath('//h2[contains(@class,"price-active")]')
	print title," = ",price[0].text
