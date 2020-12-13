import json 
import requests 
import sqlite3
API_KEY =  '82d1198ffb1c122e548fc317f7472bf4'

def weather_data(API_KEY, lat, lon, part):
    baseurl = 'https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude={}&appid={}'.format(lat, lon, part, API_KEY)
    request = requests.get(baseurl)
    response = json.loads(request.text)
    pull_data = []
    for item in response['hourly']:
        pull_data.append((item['temp'], item['wind_speed'], lat, lon))
    return pull_data

def conidtions(API_KEY, lat, lon):
    baseurl = 'https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude={}&appid={}'.format(lat, lon, part, API_KEY)
    request = requests.get(baseurl)
    response = json.loads(request.text)
    pull_data = []
    for item in response['hourly']:
        pull_data.append(item['weather'][0]['main'])
    return pull_data
 
def shared_table(API_KEY, lat, lon): 
    new_lst = conidtions(API_KEY, lat, lon)
    key_lst = []
    for item in new_lst: 
        if item == "Clouds": 
            key_lst.append(1)
        elif item == "Clear": 
            key_lst.append(2)
        elif item == "Snow": 
            key_lst.append(3)
        elif item == "Rain": 
            key_lst.append(4)
        elif item == "Drizzle": 
            key_lst.append(5)
        elif item == "Thunderstorm": 
            key_lst.append(6)
        else:
            key_lst.append(item)               
    return key_lst 

def makeDB(data, shared_data): 
    try:
        conn = sqlite3.connect('/Users/JasonWeisenfeld/206FINAL/alldata1.db')
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS WeatherData (temperature FLOAT, windspeed FLOAT, condition_id INTEGER, latitude FLOAT, longitude FLOAT, FOREIGN KEY(condition_id) REFERENCES WeatherType(condition_id))")
        temperature = []
        wind_speed = []
        latitude = []
        longitude =[]
        condition_id = []
        for tup in data:
            temperature.append(tup[0])
            wind_speed.append(tup[1])
            latitude.append(tup[2])
            longitude.append(tup[3])
        for item in shared_data: 
            condition_id.append(item)
        for i in range(25):
            condition = condition_id[i]
            temp = temperature[i]
            wind = wind_speed[i]
            lat1 = latitude[i]
            lon1 = longitude[i]
            cur.execute("INSERT INTO WeatherData (temperature, windspeed, condition_id, latitude, longitude) VALUES (?,?,?,?,?)", (temp, wind, condition, lat1, lon1))
            conn.commit()
        print("Successfully added")
        cur.close()
    except:
        print('ERROR')

def second_table(condition_id, condition): 
    try: 
        conn = sqlite3.connect('/Users/JasonWeisenfeld/206FINAL/alldata1.db')
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS WeatherType (condition_id INTEGER PRIMARY KEY, condition TEXT)")
        cur.execute("INSERT INTO WeatherType (condition_id, condition) VALUES(?,?)", (condition_id, condition))
        conn.commit()
        cur.close() 
        print('Successfully added')
    except: 
        print("Already in table")
part = ['current','minutely','daily','alerts']
city = input("Enter the name of a city: ")
if city == 'Dallas':
    userlat = 32.7767
    userlon = 96.797
elif city == 'Miami':
    userlat = 25.7617
    userlon = 80.1918
elif city == 'Los Angeles':
    userlat = 34.0522
    userlon = 118.2437
elif city == 'New York City':
    userlat = 40.7128
    userlon = 74.0060
makeDB(weather_data(API_KEY, userlat, userlon, part), shared_table(API_KEY, userlat, userlon)) 
second_table(1, 'Clouds')
second_table(2, 'Clear')
second_table(3, "Snow")
second_table(4, "Rain")
second_table(5, "Drizzle")
second_table(6, "Thunderstorm")
