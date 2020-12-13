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
    cur.execute("Select * from WeatherData")
    rows = cur.fetchall()
    Dal_temp = []
    LA_temp = []
    NYC_temp = []
    Mia_temp = []
    for row in rows [0:25]:
        Dal_temp.append(row[0])
    for row in rows [25:50]:
        LA_temp.append(row[0])
    for row in rows [50:75]:
        NYC_temp.append(row[0])
    for row in rows [75:100]:
        Mia_temp.append(row[0])

x_axis =[]
for hour in range(1,26):
    x_axis.append(hour)

fig, ax = plt.subplots()

ax.plot(x_axis, Dal_temp , "r", label = "Dallas, TX")
ax.plot(x_axis, LA_temp, "g", label = "Los Angeles, CA")
ax.plot(x_axis, NYC_temp, "b", label = "New York City, NY")
ax.plot(x_axis, Mia_temp, "m", label = "Miami, FL")
ax.legend()
ax.set_xlabel('hour')
ax.set_ylabel('Temperature')
ax.set_title('Temperature over a 25 hour period in All Four Cities')
ax.grid()
plt.show()