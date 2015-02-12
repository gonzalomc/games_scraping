# -*- encoding: utf-8 -*-
#!/usr/bin/python
import MySQLdb
import requests
from bs4 import BeautifulSoup

db = MySQLdb.connect(host="localhost",
	user="root",
	passwd="root",
	db="scrp_games")


for category in (4, 6, 12):
	if category == 4:
		console = 1
		subcat = 12
	elif category == 6:
		console = 2
		subcat = 18
	else:
		console = 3
		subcat = 36

	url = "http://sniper.cl/index.php?id=VerTablaProductos&Cat={0}&SubCat={1}".format(category, subcat)
	r = requests.get(url)

	soup = BeautifulSoup(r.content)
	#print soup.prettify().encode('UTF-8')

	content = soup.find("div", {"id": "cajacontenido"})
	table = content.find("table")

	cur = db.cursor()


	try:
		for game in table.findAll("tr"):
			game_detail = game.findAll("td")
			game_text = game_detail[0]
			game_name = game_text.findAll("a")
			
			game_link = ""
			for f in game_name:
				game_link = "http://www.sniper.cl/%s" % f['href']
				game_name = f.text.encode('UTF-8').replace("'", "")
					
			
			game_price = game_detail[1].text
			
			
			cur.execute("INSERT INTO games_game (name, price, store_id, console_id, link) VALUES ('{0}', '{1}', 5, {2}, '{3}')".format(game_name,
				game_price, console, game_link))
			
			print game_name
			print '========='
	except:
		pass

db.commit()
db.close()