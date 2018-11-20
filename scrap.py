
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
from model import BukalapakData

#scrap
def getHTML(web):
	html = urlopen(web)
	bs = soup(html.read(), "html.parser")
	return bs

def getBukalapak():
	home = "https://www.bukalapak.com/products"
	url1 = "https://www.bukalapak.com/products/s?page="
	url2 = "&search%5Bnew%5D=1&search%5Bused%5D=0"

	html = urlopen(home)
	bs = soup(html.read(), features="html.parser")

	maxi = bs.find("span", {"class":"last-page"})
	max = maxi.get_text()
	a = 0
	for i in range(int(max)): # bukan untuk test
#	for i in range(1): # untuk test
		url = url1+ (str(i + 1)) +url2
		print("start harvest data from " + url)
		print("PAGE\t" + str(i + 1) + "\tof\t" + max)
#		print("Nama\t|\tHarga\t|\tRating\t|\tTerjual\t|\tBerat")
		htm = urlopen(url)
		bs1 = soup(htm.read(), features="html.parser")
		dataHTML = bs1.find("div",{"class":"basic-products"}).findAll("div" ,{"class":"product-card"})
		for j in dataHTML:
			# arc = j.find("article")
			try:
			    productName = j.find("article").attrs["data-name"]
			except:
			    productName = "noname"
			
			try:
			    productPrice = j.find("div", {"class":"product-price"}).attrs["data-reduced-price"]
			except:
			    productPrice = "0"
			try:
				urlDetail = "https://www.bukalapak.com" + j.find("a",{"class":"product-media__link"}).attrs["href"]
			except:
				urlDetail = "none"
			if urlDetail != "none":
				try:
					htmlDetail = getHTML(urlDetail)
				except:
					htmlDetail = "none"
				#print(htmlDetail)
				if htmlDetail != "none":
					try:
					    productSold = htmlDetail.find("dd",{"class":"c-deflist__value qa-pd-sold-value"}).text.strip()
					except:
					    productSold = "0"
					try:
					    productWeight = htmlDetail.find("dd",{"class":"c-deflist__value qa-pd-weight-value qa-pd-weight"}).text.strip()
					except:
					    productWeight = "0"

					try:
						productRating = j.find("span",{"class":"rating"}).attrs["title"]
					except:
						productRating = "0"

					dataBukalapak = BukalapakData(productName, productPrice, productRating, productSold, urlDetail)
					
		#			print(productName+"\t|\t"+productPrice+"\t|\t"+productRating+"\t|\t"+productSold+"\t|\t"+productWeight)

					dataBukalapak.saveData()


def getTokopedia():
	home = "https://www.tokopedia.com/hot"
	url1 = "https://www.tokopedia.com/hot?page="

	html = urlopen(home)
	bs = soup(html.read(), features="html.parser")

	maxi = bs.find("div", {"class":"z8han1fd"}).findAll("span",{"class":"_1IJwmLlr"})
	last = maxi[len(maxi)-1]
	lastPage = (last.find("a",{"class":"GUHElpkt"}).attrs["href"]).split('/hot?page=')[1]

	# for i in range(int(lastPage)): # bukan untuk test
	for i in range(1): # untuk test
		url = url1+str(i+1)
		print("start harvest data from " + url)
		print("Nama\t|\tHarga\t|\tRating\t|\tTerjual\t|\tBerat")
		htm = urlopen(url)
		bs1 = soup(htm.read(),"html.parser")
		dataHTML = bs1.find("div",{"class":"page-container"}).findAll("div" ,{"class":"_15GzL2eL"}) #entuk produk tiap kategori
		kategori = 0
		for j in dataHTML:
			urlDetail = j.find("a").attrs["href"]
			htmlDetail = getHTML("https://www.tokopedia.com"+urlDetail)
			dataHTML2 = htmlDetail.find("div",{"class":"clearfix VQBjDYtm"}).findAll("div",{"class":"_33JN2R1i pcr"}) #produk perkategori
			for k in dataHTML2:
				productName = k.find("h3",{"class":"_18f-69Qp"}).text.strip()
				productPrice = k.find("span", {"itemprop":"price"}).text.strip()
				productSold = "not yet"
				productWeight = "not yet"
				print(productName+"\t|\t"+productPrice) #+"\t|\t"+productRating+"\t|\t"+productSold+"\t|\t"+productWeight)
			
			########nggo tes#########
			kategori = kategori + 1 #
			if(kategori>=2):		#
				break				#
			#########################
