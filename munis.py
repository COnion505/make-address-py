# coding: utf_8
import random
import sqlite3

with open('csv/municipalities.csv') as f:
    munis = f.readlines()
conn = sqlite3.connect(r'address.sqlite3')
c = conn.cursor()
try:
    c.execute("DROP TABLE IF EXISTS munis;")
    c.execute("CREATE TABLE munis(kanji, hira);")
    for i in range(0,len(munis)):
        muni = munis[i].split(',')
        c.execute("INSERT INTO munis VALUES (?,?);", (muni[0],muni[1]))
except sqlite3.Error as e:
    print(e)
conn.commit()
conn.close()
