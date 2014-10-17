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

cur = db.cursor()
cur.execute("DELETE FROM games_game WHERE store_id = 3");
offset = 0
try:
	for x in range(1, 11):
		offset = offset + 50
		url = "http://www.todojuegos.cl/Productos/PS3/_juegos/?ListMaxShow=50&ListOrderBy=&offset={0}".format(offset)
		r = requests.get(url)
		soup = BeautifulSoup(r.content)
		#print soup.prettify().encode('UTF-8')

		games = soup.find("div", {"id": "ListadoResultados"})
		games_table = games.find("table")
		games_row = games_table.findAll("tr")

		a = 1
		games_count = 0
		for game in games_row:
			if(a%2==0):
				pass
			else:
				try:
					game_detail = game.find("table")
					game_name = game_detail.find("a", {"target": "_self"})
					
					price = game.find("p")
					price_detail = price.text
					
					games_count += 1
					print game_name.text
					print price_detail.strip()
					cur.execute("INSERT INTO games_game (name, price, store_id) VALUES ('{0}', '{1}', 3)".format(game_name.text, price_detail.strip()))

				except:
					pass
				
			a += 1 

		db.commit()
except:
	pass

db.close()
	
		

	
