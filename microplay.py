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

for category in ('ps3', 'xbox-360'):
	if category == 'ps3':
		console = 1
	else:
		console = 2
	try:
		for x in range(1, 36):
			try:
				url = "http://www.microplay.cl/resultados/page:{0}/?buscar={1}".format(str(x), category)
				r = requests.get(url)
				soup = BeautifulSoup(r.content)

				#print soup.prettify().encode('UTF-8')
				games = soup.findAll("li", {"class": "ps2"})

				for game in games:
					name_span = game.find("span")
					name_span = name_span.find("a")
					game_name = name_span.text
					game_price =  game.find("strong")
					print game_name.encode('UTF-8').strip()
					print game_price.text
					print '####'
					cur.execute("INSERT INTO games_game (name, price, store_id, console_id) VALUES ('{0}', '{1}', 4, {2})".format(
						game_name.encode('UTF-8').strip(), game_price.text, console))
			except:
				pass
			db.commit()
	except:
		pass

db.close()
