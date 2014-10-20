# -*- encoding: utf-8 -*-
#!/usr/bin/python
import os
import MySQLdb
import requests
from bs4 import BeautifulSoup
from subprocess import call



####### Mysql Conection #####
db = MySQLdb.connect(host="localhost",
	user="root",
	passwd="root",
	db="scrp_games")

cur = db.cursor()
cur.execute("truncate table games_game")
db.commit()
cur.execute("ALTER TABLE games_game AUTO_INCREMENT = 1")
db.commit()
db.close()

call(["python","zmart.py"])
call(["python","todojuegos.py"])
#call(["python","microplay.py"])
#call(["python","sniper.py"])

