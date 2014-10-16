import requests
from bs4 import BeautifulSoup


## PS4 Games.
## Only games in stock
for x in range(1, 15):
	url = "http://www.zmart.cl/scripts/prodList.asp?idcategory=187&curPage={0}&sortField=price%2C+idproduct&sinstock=0".format(str(x))
	r = requests.get(url)
	soup = BeautifulSoup(r.content)
	#print soup.prettify().encode('UTF-8')

	games = soup.findAll("div", {"class": "caja_minihome"})
	
	for game in games:
		title = game.find("div", {"class": "caja_secundaria"})
		nombre = title.find("a")
		game_data = game.find("ul", {"class": "precio_primero"})
		precio = game_data.find("li", {"class": "precio"})
		estado = game_data.find("li", {"class": "estado"})
		print nombre.text.encode('UTF-8')
		print precio.text
		print estado.text
		print '======='

