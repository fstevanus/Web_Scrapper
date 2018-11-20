from db import createConn
from datetime import date, datetime
import sqlite3

# class class
class BukalapakData:
	def __init__(self, name, harga, rating, terjual, urlDetail):
		self.name = name
		self.harga = harga
		self.rating = rating
		self.terjual = terjual
		self.urlDetail = urlDetail

	def saveData(self):
		today = date.today()
		conn = createConn()
		conn.execute('''insert into bukalapak(name, harga, rating, terjual, getDate, urldetail) values(?, ?, ?, ?, ?, ?)''', (self.name, self.harga, self.rating, self.terjual, today, self.urlDetail))
		conn.commit()
		print("berhasil simpan " + self.name)
		conn.close()
		
	def showAll():
		conn = createConn()
		conn.row_factory = sqlite3.Row
		c = conn.cursor()
		c.execute('''select * from (select distinct name, terjual,rating, harga, urldetail from bukalapak where rating > 3 order by terjual desc) limit 40''')
		# c.execute('''select * from (select * from bukalapak where rating > 3 order by terjual desc) limit 20''')
		results = c.fetchall()
		conn.close()
		return results

class TokopediaData:
	def __init__(self, productURL, productId, productName, productImage, productRating, productSold, productPrice):
		self.productURL = productURL
		self.productId = productId
		self.productName = productName
		self.productImage = productImage
		self.productRating = productRating
		self.productSold = productSold
		self.productPrice = productPrice

	def saveData(self):
		today = date.today()
		conn = createConn()
		conn.execute('''insert into tokopedia(productURL, productId, productName, productImage, productRating, productSold, productPrice, getDate) values(?, ?, ?, ?, ?, ?, ?, ?)''', 
			(self.productURL, self.productId, self.productName, self.productImage, self.productRating, self.productSold, self.productPrice, today))
		conn.commit()
		print("berhasil simpan " + self.productName)
		conn.close()

	def showAll():
		conn = createConn()
		conn.row_factory = sqlite3.Row
		c = conn.cursor()
		c.execute('''select * from (select distinct productName, productSold, productRating, productPrice, productURL, productImage from tokopedia where productRating > 3 order by productSold desc) limit 40''')
		# c.execute('''select * from (select * from bukalapak where rating > 3 order by terjual desc) limit 20''')
		results = c.fetchall()
		conn.close()
		return results

def showBukalapak():
	bukalapaks = BukalapakData.showAll()
	for bl in bukalapaks:
		print(bl)
		print("\n")