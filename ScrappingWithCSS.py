from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html") 

bsObject = BeautifulSoup(html) 
l = bsObject.findAll("span" , {"class" : "green"})

for item in l:
    print(item.get_text())

l = bsObject.findAll("" , {"id" : "text"})
import ipdb; ipdb.set_trace()