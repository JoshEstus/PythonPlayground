import urllib
from bs4 import BeautifulSoup
from datetime import datetime, date, time

page = urllib.urlopen('http://explosm.net')

soup = BeautifulSoup(page)

comicUrl = soup.find(id="featured-comic")['src']

today = datetime.today().strftime("%m-%d-%Y")

comicDest = "/home/josh/Pictures/Cyanide&HappinessComics/"

urllib.urlretrieve("http:" + comicUrl, comicDest + today + ".png")