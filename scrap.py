import sqlite3
from sqlite3 import Error
import urllib2
from bs4 import BeautifulSoup

def create_connection(dbFile):
    try:
        conn = sqlite3.connect(dbFile)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        conn.close()

if __name__ == '__main__':
    create_connection("/home/fs/python_project/scrap")
