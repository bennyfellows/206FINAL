import json 
import requests 
import sqlite3
API_KEY = '-IlEc2KMRXy5QBF8l7evjD7DWvhCbqv8e8S9cEgmAkZ-BvligKz0nLY5jDStCZQ9lEgZTkUsmlnuB-Jg25CxWAkEgsgKMih6DdQYIbfBSsaWpMQWHpQC3aayrJ3OX3Yx'

def yelp_data(API_KEY, location):
    baseurl = "https://api.yelp.com/v3/businesses/search"
    headers = {"Authorization" : "Bearer %s" % API_KEY}
    params = {'term': 'restaurant', 'location': location, 'sort_by': 'rating', 'price': [1,2,3,4] , 'radius': 2500, 'limit': 50}
    request = requests.get(baseurl, headers = headers, params = params)
    response = json.loads(request.text)
    pull_data = []
    for item in response['businesses']:
        if item['id'] not in pull_data:
            pull_data.append((item['name'], item['price'], item['rating'], item['location']['city']))
    return pull_data

def makeDB(data):
    try:
        conn = sqlite3.connect('/Users/JasonWeisenfeld/206FINAL/alldata1.db')
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS YelpData (restaurant_name TEXT, price_range TEXT, rating FLOAT, city TEXT)")
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
            cur.execute("INSERT INTO YelpData (restaurant_name, price_range, rating, city) VALUES (?,?,?,?)", (name_data, price_data, rating_data, city_data))
            conn.commit()
        print("Successfully added")
        cur.close()
    except:
        print('ERROR')

city = input("Enter the name of a city: ") 
makeDB(yelp_data(API_KEY, city))