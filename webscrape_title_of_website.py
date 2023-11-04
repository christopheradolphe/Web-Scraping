from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

def getTitle(url):
  try:
    html = urlopen(ulr)
  except HTTPError as e:
    return None
  try:
    bs = BeautifulSoup(html.read(), 'html.parser')
    title = bs.body.h1
  except AttributeError as e:
    return None

link = ''
title = getTitle(link)
if title == None:
  print("No title found. Ran into error")
else:
  print(title)