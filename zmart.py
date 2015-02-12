# -*- encoding: utf-8 -*-
#!/usr/bin/python
import MySQLdb
import requests
from bs4 import BeautifulSoup


######################
# Mysql 
######################
db = MySQLdb.connect(host="localhost",
	user="root",
	passwd="root",
	db="scrp_games")

cur = db.cursor()

######################
# Category Games Zmart
# 187 = Ps3 Games
# 159 = Xbox 360 Games
######################

for category in (187, 159, 420):
	######################
	# Console type
	# 1 = PS3
	# 2 = XBOX 360
	# 3 = PS4
	######################
	if category == 187:
		console = 1

	elif category == 159:
		console = 2
	else:
		console = 3
	
	for x in range(1, 20):
		try:
			url = "http://www.zmart.cl/scripts/prodList.asp?idcategory={0}&curPage={1}&sortField=price%2C+idproduct&sinstock=0".format(str(category),
				str(x))
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

				game_link = "http://zmart.cl%s" % name['href']
				
				cur.execute("INSERT INTO games_game (name, price, store_id, console_id, link) VALUES ('{0}', '{1}', 2, {2}, '{3}')".format(game_name,
					game_price, console, game_link))
				
				print game_name 
				print '======='
				
				
		except:
			pass

db.commit()
db.close()