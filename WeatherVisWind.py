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
    Dal_wind = []
    LA_wind = []
    NYC_wind = []
    Mia_wind = []
    for row in rows [0:25]:
        Dal_wind.append(row[1])
    for row in rows [25:50]:
        LA_wind.append(row[1])
    for row in rows [50:75]:
        NYC_wind.append(row[1])
    for row in rows [75:100]:
        Mia_wind.append(row[1])

x_axis =[]
for hour in range(1,26):
    x_axis.append(hour)

fig, ax = plt.subplots()

ax.plot(x_axis, Dal_wind , "r", label = "Dallas, TX")
ax.plot(x_axis, LA_wind, "g", label = "Los Angeles, CA")
ax.plot(x_axis, NYC_wind, "b", label = "New York City, NY")
ax.plot(x_axis, Mia_wind, "m", label = "Miami, FL")
ax.legend()
ax.set_xlabel('hour')
ax.set_ylabel('Wind Speed')
ax.set_title('Wind Speed over a 25 hour period in All Four Cities')
ax.grid()
plt.show()