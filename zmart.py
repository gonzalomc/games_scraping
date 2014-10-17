# -*- encoding: utf-8 -*-
#!/usr/bin/python
import MySQLdb
import requests
from bs4 import BeautifulSoup


####### Mysql Conection #####
db = MySQLdb.connect(host="localhost",
	user="root",
	passwd="root",
	db="scrp_games")

####### PS3 Games : Only in stock ###########

cur = db.cursor()
cur.execute("DELETE FROM games_game WHERE store_id = 2");

for x in range(1, 15):
	url = "http://www.zmart.cl/scripts/prodList.asp?idcategory=187&curPage={0}&sortField=price%2C+idproduct&sinstock=0".format(str(x))
	r = requests.get(url)
	soup = BeautifulSoup(r.content)
	#print soup.prettify().encode('UTF-8')
	games = soup.findAll("div", {"class": "caja_minihome"})
	
	for game in games:
		title = game.find("div", {"class": "caja_secundaria"})
		name = title.find("a")
		game_data = game.find("ul", {"class": "precio_primero"})
		price = game_data.find("li", {"class": "precio"})
		status = game_data.find("li", {"class": "estado"})

		game_name = name.text.encode('UTF-8')
		game_name = game_name.replace("'", "")
		game_price =price.text


		cur.execute("INSERT INTO games_game (name, price, store_id) VALUES ('{0}', '{1}', 2)".format(game_name, game_price))
		
		print game_name
		print game_price
		print '======='

db.commit()
db.close()

