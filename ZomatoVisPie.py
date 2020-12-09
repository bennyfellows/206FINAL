import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import json
import os
import sqlite3






BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, '/Users/JasonWeisenfeld/206FINAL/alldata1.db')
with sqlite3.connect(db_path) as db:
    cur = db.cursor()
    cur.execute("Select * from ZomatoData")
    rows = cur.fetchall()
    Dal_price = []
    LA_price = []
    NYC_price = []
    Mia_price = []
    for row in rows[0:25]:
        Dal_price.append(row[1])
    for row in rows[25:50]:
        LA_price.append(row[1])  
    for row in rows[25:75]:
        NYC_price.append(row[1])
    for row in rows[75:100]:
        Mia_price.append(row[1]) 
    
Dal_top = []
Dal_mid = []
Dal_low = []
Dal_bot = []

LA_top = []
LA_mid = []
LA_low = []
LA_bot = []

NYC_top = []
NYC_mid = []
NYC_low = []
NYC_bot = []

Mia_top = []
Mia_mid = []
Mia_low = []
Mia_bot = []
for i in Dal_price:
    if i == '4':
        Dal_top.append(i)
    elif i == '3':
        Dal_mid.append(i)
    elif i == '2':
        Dal_low.append(i)
    else:
        Dal_bot.append(i)

for i in LA_price:
    if i == '4':
        LA_top.append(i)
    elif i == '3':
        LA_mid.append(i)
    elif i == '2':
        LA_low.append(i)
    else:
        LA_bot.append(i)

for i in NYC_price:
    if i == '4':
        NYC_top.append(i)
    elif i == '3':
        NYC_mid.append(i)
    elif i == '2':
        NYC_low.append(i)
    else:
        NYC_bot.append(i)

for i in Mia_price:
    if i == '4':
        Mia_top.append(i)
    elif i == '3':
        Mia_mid.append(i)
    elif i == '2':
        Mia_low.append(i)
    else:
        Mia_bot.append(i)

p_daltop = (len(Dal_top)/25)
p_dalmid = (len(Dal_mid)/25)
p_dallow = (len(Dal_low)/25)
p_dalbot = (len(Dal_bot)/25)

labels = '4', '3', '2', '1'
sizes = [p_daltop, p_dalmid, p_dallow, p_dalbot]
colors = ['red', 'blue', 'yellow', 'purple']

p_LAtop = (len(LA_top)/25)
p_LAmid = (len(LA_mid)/25)
p_LAlow = (len(LA_low)/25)
p_LAbot = (len(LA_bot)/25)

labels2 = '4', '3', '2', '1'
sizes2 = [p_LAtop, p_LAmid, p_LAlow, p_LAbot]
colors2 = ['red', 'blue', 'yellow', 'purple']

p_NYCtop = (len(NYC_top)/25)
p_NYCmid = (len(NYC_mid)/25)
p_NYClow = (len(NYC_low)/25)
p_NYCbot = (len(NYC_bot)/25)

labels3 = '4', '3', '2', '1'
sizes3 = [p_NYCtop, p_NYCmid, p_NYClow, p_NYCbot]
colors3 = ['red', 'blue', 'yellow', 'purple']


p_miatop = (len(Mia_top)/25)
p_miamid = (len(Mia_mid)/25)
p_mialow = (len(Mia_low)/25)
p_miabot = (len(Mia_bot)/25)


labels4 = '4', '3', '2', '1'
sizes4 = [p_miatop, p_miamid, p_mialow, p_miabot]
colors4 = ['red', 'blue', 'yellow', 'purple']

#ploting the charts 

fig = plt.figure(figsize= (10,5))
ax1 = fig.add_subplot(141)
ax2 = fig.add_subplot(142)
ax3 = fig.add_subplot(143)
ax4 = fig.add_subplot(144)


ax1.pie(sizes, labels = labels, colors = colors, autopct= '%1.1f%%', shadow=True, startangle=140)
ax1.axis('equal')


ax2.pie(sizes2, labels = labels2, colors = colors2, autopct= '%1.1f%%', shadow=True, startangle=140)
ax2.axis('equal')

ax3.pie(sizes3, labels = labels3, colors = colors3, autopct= '%1.1f%%', shadow=True, startangle=140)
ax3.axis('equal')

ax4.pie(sizes4, labels = labels4, colors = colors4, autopct= '%1.1f%%', shadow=True, startangle=140)
ax4.axis('equal')


plt.suptitle("Zomato: Price Ranges of Highest Ranked Restaurants Per City\n" + "From Left to Right: Dallas, Los Angeles, New York City, Miami\n"+ "with 1 being the cheapest and 4 being most expensive")
plt.show()