import sys
import requests
from lxml import html
from bs4 import BeautifulSoup

twitterPage = 'http://www.twitter.com/realDonaldTrump'
page = BeautifulSoup(requests.get(twitterPage).content, "html.parser")
print(page.p)
# for link in page.findAll('a'):
#     print(link.get('href'))

