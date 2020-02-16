from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError

#print(data.read())

try:
    data = urlopen("http://www.pythonscraping.com/exercises/exercise1.html") 
except HTTPError as e:
    print(e)
else:
    #Nothing to do 
    if data is None :
        print("Problem with url ! ")
    else:
        b = BeautifulSoup(data.read() , "html.parser");

print(b.h1)
print(b.html.body.h1)
print(b.body.h1)
print(b.html.h1)
