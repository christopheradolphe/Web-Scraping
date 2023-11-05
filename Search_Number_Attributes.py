from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')
images = bs.find_all(lambda tag: len(tag.attrs) == 2) #Finds all elements with two attributes
for image in images:
  print(image['src'])