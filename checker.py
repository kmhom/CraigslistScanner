import csv
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen

#List of sample urls 
miata_url = "https://sfbay.craigslist.org/d/for-sale/search/sss?query=miata&sort=rel"
roadbike_50cm_url="https://sfbay.craigslist.org/d/for-sale/search/sss?query=road%20bike%2050cm&sort=rel"
roadbike_52cm_url="https://sfbay.craigslist.org/search/sss?query=road+bike+52cm&sort=rel&purveyor-input=all"

miata_page = urlopen(miata_url)
html_decode_miata = miata_page.read().decode("utf-8")
soup = BeautifulSoup(html_decode_miata, "html.parser")

#print(soup.get_text())
#print(soup.title())
print(soup.prettify())