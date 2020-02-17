from urllib.request import urlopen
from bs4 import BeautifulSoup 
import re 

f = open("htmlDump" , "w")

URL = "https://spark.adobe.com/video/SURSphvyCEhXV"

htmlData = urlopen(URL)
bsObject = BeautifulSoup(htmlData)

f.write(str(bsObject))

f.close()
layer = bsObject.find_all("div" , {"class":re.compile("info-.*")})
#print(layer.beau)
import ipdb; ipdb.set_trace()
print(layer.src)