import json 
import requests 
import sqlite3

def join_tables():
    conn = sqlite3.connect('/Users/JasonWeisenfeld/206FINAL/alldata1.db')
    cur = conn.cursor()
    cur.execute('SELECT ZomatoData.rating, YelpData.rating, YelpData.restaurant_name, YelpData.city FROM ZomatoData INNER JOIN YelpData ON ZomatoData.restaurant_name = YelpData.restaurant_name')
    conn.commit()
    join = cur.fetchall()
    for x in join:
        print(x)

print(join_tables())

def avg_rating_calc():
    conn = sqlite3.connect('/Users/JasonWeisenfeld/206FINAL/alldata1.db')
    cur = conn.cursor()
    cur.execute('SELECT ZomatoData.restaurant_name, ZomatoData.rating, YelpData.rating, round((ZomatoData.rating + YelpData.rating)/2, 2) FROM ZomatoData INNER JOIN YelpData ON ZomatoData.restaurant_name = YelpData.restaurant_name')
    conn.commit()
    join = cur.fetchall()
    tups = []
    for x in join:
        tups.append(x)

    with open('rating_average.txt', 'w') as output:
        output.write("Restaurant Name, Zomato Rating, Yelp Rating, Rating Average\n")
        for x in tups:
            string = ""
            for word in x:
                word = str(word)
                string += word + ' '
            output.write(str(string) + '\n')
        

avg_rating_calc()

def wind_speed_calc():
    conn = sqlite3.connect('/Users/JasonWeisenfeld/206FINAL/alldata1.db')
    cur = conn.cursor()
    cur.execute('SELECT WeatherData.windspeed FROM WeatherData')
    conn.commit()
    join = cur.fetchall()
    all_avg = []
    dal_lst = []
    dal_sum = 0
    dal_avg = 0
    for x in join[0:25]:
        dal_sum += x[0]
        dal_lst.append((x[0], 'Dallas'))
    dal_avg = round(dal_sum / 25, 3)
    all_avg.append(dal_avg)

    LA_sum = 0
    LA_avg = 0
    LA_lst = []
    for x in join[25:50]:
        LA_sum += x[0]
        LA_lst.append((x[0], 'Los Angeles'))
    LA_avg = round(LA_sum / 25, 3)
    all_avg.append(LA_avg)

    NYC_sum = 0
    NYC_avg = 0
    NYC_lst = []
    for x in join[50:75]:
        NYC_sum += x[0]
        NYC_lst.append((x[0], 'New York City'))
    NYC_avg = round(NYC_sum / 25, 3)
    all_avg.append(NYC_avg)

    Mia_sum = 0
    Mia_avg = 0
    Mia_lst = []
    for x in join[75:100]:
        Mia_sum += x[0]
        Mia_lst.append((x[0], 'Miami'))
    Mia_avg = round(Mia_sum / 25, 3)
    all_avg.append(Mia_avg)

    with open('windspeed.txt', 'w') as output:
        output.write("Windspeed, City\n")
        for tup in dal_lst:
            string = ""
            string += str(tup[0]) + '    ' + tup[1]
            output.write(str(string) + '\n')
        for tup in LA_lst:
            string = ""
            string += str(tup[0]) + '    ' + tup[1]
            output.write(str(string) + '\n')
        for tup in NYC_lst:
            string = ""
            string += str(tup[0]) + '    ' + tup[1]
            output.write(str(string) + '\n')
        for tup in Mia_lst:
            string = ""
            string += str(tup[0]) + '    ' + tup[1]
            output.write(str(string) + '\n')
        output.write('---------------------------\n')
        output.write('City, Average Wind Speed\n')
        cities = ['Dallas', 'Los Angeles', 'New York City', 'Miami' ]
        for i in range(4):
            output.write(cities[i] + "    "  + str(all_avg[i]) + "\n")

wind_speed_calc()

