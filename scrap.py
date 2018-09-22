import sqlite3
from sqlite3 import Error
from urllib.request import urlopen
from bs4 import BeautifulSoup

def createConn(loc):
	 conn = sqlite3.connect("/home/fs/scrap.sqlite") #ganti dengan lokasi db bro
	 return conn


def getHTML(web):
	html = urlopen(web)
	bs = BeautifulSoup(html.read())
	return bs
