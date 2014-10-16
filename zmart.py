import requests
from bs4 import BeautifulSoup
### Juegos PS4 ######

r = requests.get("http://www.zmart.cl/scripts/prodList.asp?idCategory=157")
soup = BeautifulSoup(r.content)

#print soup.prettify().encode('UTF-8')

games = soup.findAll("div",{"class":"caja_minihome"})

for game in games:
    for link in game.findAll('a'):
        print link.text
        print '#############'

