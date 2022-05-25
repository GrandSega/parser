import reqests
from bs4 import BeautifulSoup
import csv

HOST = 'https://hidemy.name/ru'
URL = 'https://hidemy.name/ru/proxy-list/?type=s45#list'
HEADERS = {

}

def get_html(url, params=''):
    r = requests.get(url,headrs=HEADERS,params=params )
    return r
html = get_html(url)
print(html)