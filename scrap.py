import sqlite3
from sqlite3 import Error
import urllib2
from bs4 import BeautifulSoup



if __name__ == '__main__':
    conn = sqlite3.connect("/home/fs/python_project/scrap") #ganti dengan lokasi connect bro

    conn.close()
