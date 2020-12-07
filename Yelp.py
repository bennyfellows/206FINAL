import json 
import requests 
import sqlite3

API_KEY = "-IlEc2KMRXy5QBF8l7evjD7DWvhCbqv8e8S9cEgmAkZ-BvligKz0nLY5jDStCZQ9lEgZTkUsmlnuB-Jg25CxWAkEgsgKMih6DdQYIbfBSsaWpMQWHpQC3aayrJ3OX3Yx"

def yelp_data(API_KEY, location):
    baseurl = "https://api.yelp.com/v3/businesses/search"
    headers = {"Authorization" : "Bearer %s" % API_KEY}
    params = {'term': 'restaurant', 'location': location, 'sort_by': 'rating', 'limit': 50,}
    request = requests.get(baseurl, headers = headers, params = params)
    response = json.loads(request.text)
    pull_data = []
    for item in response['businesses']:
        if item['id'] not in pull_data:
            pull_data.append((item['price'], item['name'], item['rating'], item['location']['city']))
    return pull_data

print(yelp_data(API_KEY, "New York City"))