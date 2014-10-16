# -*- encoding: utf-8 -*-
#!/usr/bin/python
import MySQLdb
import requests
from bs4 import BeautifulSoup


for x in range(1, 17):
	try:
		url = "http://www.microplay.cl/resultados/page:{0}/?buscar=ps3".format(str(x))
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
	except:
		pass