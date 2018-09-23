import sqlite3
from sqlite3 import Error
from urllib.request import urlopen
from bs4 import BeautifulSoup

def createConn():
	 conn = sqlite3.connect("/home/fs/scrap.sqlite") #ganti dengan lokasi db bro
	 return conn


def getHTML(web):
	html = urlopen(web)
	bs = BeautifulSoup(html.read())
	return bs

def getBukalapak():
	home = "https://www.bukalapak.com/products"
	url1 = "https://www.bukalapak.com/products/s?page="
	url2 = "&search%5Bnew%5D=1&search%5Bused%5D=0"
    
	html = urlopen(home)
	bs = BeautifulSoup(html.read())
	
	maxi = bs.find("span", {"class":"last-page"})
	max = maxi.get_text()
	a = 0
	# for i in range(int(max)): # bukan untuk test 
	for i in range(1): # untuk test 
		url = url1+ (str(i + 1)) +url2
		print("start harvest data from " + url)
		print("nama\t|\tharga")
		htm = urlopen(url)
		bs1 = BeautifulSoup(htm.read())
		dataHTML = bs1.find("div",{"class":"basic-products"}).findAll("div" ,{"class":"product-card"})
		for j in dataHTML:
			# arc = j.find("article")
			productName = j.find("article").attrs["data-name"]
			productPrice = j.find("div", {"class":"product-price"}).attrs["data-reduced-price"]
			print(productName+"\t|\t"+productPrice)