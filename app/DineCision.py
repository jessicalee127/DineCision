import argparse
import json
import pprint
import requests
import sys
import urllib
import random
import os

API_KEY = os.environ["DINECISION_API_KEY"]

from urllib.error import HTTPError
from urllib.parse import quote
from urllib.parse import urlencode



# API constants, you shouldn't have to change these.
API_HOST = 'https://api.yelp.com'
SEARCH_PATH = '/v3/businesses/search'
BUSINESS_PATH = '/v3/businesses/'  # Business ID will come after slash.
SEARCH_LIMIT = 5



def yelprequest(host, path, api_key, url_params=None):
    url_params = url_params or {}
    url = '{0}{1}'.format(host, quote(path.encode('utf8')))
    headers = {
        'Authorization': 'Bearer %s' % api_key,
    }

    print(u'Querying {0} ...'.format(url))

    response = requests.request('GET', url, headers=headers, params=url_params)
    return response.json()


def main():

    location_input = input("Please enter the area you want to search for (e.g. 3 Times Square, New York City): ")
    rating_input = input("Do you care about ratings (e.g. 4 or 4.5): ")
    price_input = input("Do you care about price (e.g. 1 is the lowest, 4 is the highest): ")

    url_params = {
        'location': location_input.replace(' ', '+'),
        'radius': 500,
        'is_closed': "false",
        'rating': rating_input,
        'limit': SEARCH_LIMIT,
        'categories': "restaurants, All",
        'price': price_input
    }

    result = yelprequest(API_HOST, SEARCH_PATH, API_KEY, url_params)
    business_list = result["businesses"]
    random_business = random.choice(business_list)
    print("Please go to " + random_business["name"] + " !")
    Show_more = input("Do you want to learn more about it (y/n): ")
    if Show_more == "y":
        print(random_business["name"] + ", located at " + str(random_business["location"]['display_address'][0]) + ", " + str(random_business["location"]['state']) + " " + str(random_business["location"]['zip_code']))
    else:
        print("enjoy!")


if __name__ == '__main__':
    main()
