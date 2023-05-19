# coding: utf_8
import random
import sqlite3

with open('csv/prefectures.csv') as f:
    prefs = f.readlines()
conn = sqlite3.connect(r'address.sqlite3')
c = conn.cursor()
try:
    c.execute("DROP TABLE IF EXISTS prefs;")
    c.execute("CREATE TABLE prefs(kanji, hira);")
    for i in range(0,len(prefs)):
        pref = prefs[i].split(',')
        c.execute("INSERT INTO prefs VALUES (?,?);", (pref[0],pref[1]))
except sqlite3.Error as e:
    print(e)
conn.commit()
conn.close()
