import sqlite3
from sqlite3 import Error

#data base
def createConn():
	 conn = sqlite3.connect("/home/fs/project_scrap/Web_Scrapper/data.sqlite") #ganti dengan lokasi db bro
	 return conn

def createDataBase():
	conn = createConn()
	conn.execute('''CREATE TABLE IF NOT EXISTS bukalapak (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, name TEXT UNIQUE, harga NUMERIC DEFAULT 0, rating INTEGER DEFAULT 0, terjual NUMERIC, getDate DATE, urldetail TEXT)''')
	conn.close()