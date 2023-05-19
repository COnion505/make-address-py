# coding: utf_8
import random
import sqlite3

with open('csv/cities.csv') as f:
    cities = f.readlines()
conn = sqlite3.connect(r'address.sqlite3')
c = conn.cursor()
try:
    c.execute("DROP TABLE IF EXISTS cities;")
    c.execute("CREATE TABLE cities(kanji, hira);")
    for i in range(0,len(cities)):
        city = cities[i].split(',')
        c.execute("INSERT INTO cities VALUES (?,?);", (city[0],city[1]))
except sqlite3.Error as e:
    print(e)
conn.commit()
conn.close()
