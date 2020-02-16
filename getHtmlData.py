from urllib.request import urlopen

data = urlopen("https://pythonprogramming.net/parsememcparseface/")
print(data.read())


