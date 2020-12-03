import json 
import requests 
import sqlite3
API_KEY = '601d041d3b257f8a3debb069cde93bfa'
LosAngeles_ID = 281
NYC_ID = 280
ent_type = 'city'
def zomato_data(API_KEY, entity_id, entity_type):
    start = 0
    pull_data = []
    while start < 50:
        baseurl = "https://developers.zomato.com/api/v2.1/search?"
        headers = {'Accept': 'application/json', 'user-key': API_KEY}
        params = {'entity_id': entity_id, 'entity_type': entity_type, 'start': start, 'count': 25, 'sort': 'rating', 'order': 'desc'}
        request = requests.get(baseurl, headers = headers, params = params)
        response = json.loads(request.text)
        for item in response['restaurants']:
            if item['restaurant']['id']:
                pull_data.append((item['restaurant']['name'], item['restaurant']['price_range'], float(item['restaurant']['user_rating']['aggregate_rating']), item['restaurant']['location']['city']))
        start += 25
    return pull_data

def new_database(): 
    conn = sqlite3.connect('/Users/JasonWeisenfeld/206FINAL/alldata1.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS ZomatoData (restaurant_name TEXT, price_range TEXT, rating FLOAT, city TEXT)")

def create_database(data):
    try:
        conn = sqlite3.connect('/Users/JasonWeisenfeld/206FINAL/alldata1.db')
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS ZomatoData (restaurant_name TEXT, price_range TEXT, rating FLOAT, city TEXT)")
        names = []
        price_range = []
        rating = []
        city = []
        for tup in data:
            names.append(tup[0])
            price_range.append(tup[1])
            rating.append(tup[2])
            city.append(tup[3])
        for i in range(25):
            name_data = names[i]
            price_data = price_range[i]
            rating_data = rating[i]
            city_data = city[i]
            cur.execute("INSERT INTO ZomatoData (restaurant_name, price_range, rating, city) VALUES (?,?,?,?)", (name_data, price_data, rating_data, city_data))
            conn.commit()
        print("Successfully added")
        cur.close()
    except:
        print('ERROR')
zomato_data(API_KEY, LosAngeles_ID, ent_type) 
zomato_data(API_KEY, NYC_ID, ent_type)
new_database()
create_database(zomato_data(API_KEY, LosAngeles_ID, ent_type)[0:50])
#create_database(zomato_data(API_KEY, LosAngeles_ID, ent_type)[25:50])
create_database(zomato_data(API_KEY, NYC_ID, ent_type)[0:50])
#create_database(zomato_data(API_KEY, NYC_ID, ent_type)[25:50])