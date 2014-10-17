# -*- encoding: utf-8 -*-
#!/usr/bin/python
import MySQLdb
import requests
from bs4 import BeautifulSoup

db = MySQLdb.connect(host="localhost",
	user="root",
	passwd="root",
	db="scrp_games")


url = "http://sniper.cl/index.php?id=VerTablaProductos&Cat=4&SubCat=12"
r = requests.get(url)

soup = BeautifulSoup(r.content)
#print soup.prettify().encode('UTF-8')

content = soup.find("div", {"id": "cajacontenido"})
table = content.find("table")

cur = db.cursor()
cur.execute("DELETE FROM games_game WHERE store_id = 5");

try:
	for game in table.findAll("tr"):
		game_detail = game.findAll("td")
		game_text = game_detail[0]
		game_name = game_text.findAll("a")
		for f in game_name:
			game_name = f.text.encode('UTF-8')
		game_price = game_detail[1].text
		print '========='

		cur.execute("INSERT INTO games_game (name, price, store_id) VALUES ('{0}', '{1}', 5)".format(game_name, game_price))

	db.commit()
except:
	pass


db.close()