from urllib.request import urlopen
from bs4 import BeautifulSoup 

htmlData = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObject = BeautifulSoup(htmlData)

#print(bsObject.div)
#print(bsObject.find("div" , {"id" : "footer"}))

layer1 = bsObject.find("table" , {"id" : "giftList"})
#import ipdb; ipdb.set_trace()
print(layer1.tr.th.text)

for l in bsObject.find_all("tr" , {"class" : "gift"}):
    print(l.td.text)


#for child in bsObject.find("table" , {"id" : "giftList"}).descendants:
#for child in bsObject.find("table" , {"id" : "giftList"}).children:
#    print(child)