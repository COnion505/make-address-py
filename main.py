# coding: utf_8
import random
import sqlite3
COUNT = 1000000

with open('csv/cities.csv') as f:
    cities = f.readlines()

with open('csv/prefectures.csv') as f:
    prefectures = f.readlines()

with open('csv/municipalities.csv') as f:
    municipalities = f.readlines()
banchi = random.randrange(100) 
cho = random.randrange(10)

conn = sqlite3.connect(r'address.sqlite3')
c = conn.cursor()
try:
#    c.execute("DROP TABLE address;")
    c.execute("CREATE TABLE IF NOT EXISTS address(address);")
    for _ in range(0,COUNT):
        banchi = random.randrange(1, 100) 
        cho = random.randrange(1, 10)
        city = cities[random.randrange(len(cities)-1)].split(',')
        pref = prefectures[random.randrange(len(prefectures)-1)].split(',')
        muni = municipalities[random.randrange(len(municipalities)-1)].split(',')
        c.execute("INSERT INTO address VALUES (?);", ("{}{}{}{}-{}".format(pref[0],city[0],muni[0], cho, banchi),))
except sqlite3.Error as e:
    print(e)
conn.commit()
conn.close()
