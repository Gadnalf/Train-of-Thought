from twython import Twython
from random import sample
import yweather
import json
import os
from boto.s3.connection import S3Connection

debug = False
if(debug):
    module_dir = os.path.dirname(__file__)  # get current directory
    file_path = os.path.join(module_dir, 'twitter_credentials.json')


def load_twitter():
    # Load credentials from json file if on local
    if(debug):
        with open(file_path, "r") as file:
            creds = json.load(file)
        twitter = Twython(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])
    # Or load credentials from config
    else:
        twitter = Twython(os.environ['CONSUMER_KEY'], os.environ['CONSUMER_SECRET'])

    return twitter

def search_twitter(search_text, num):
    '''
    Returns a number of the search results for the given search text.
    '''
    twitter = load_twitter()

    # Fetch tweets
    tweets = []
    for status in twitter.search(q = search_text, count = num, lang = 'en', tweet_mode = 'extended')['statuses']:
        tweets.append(status['full_text'].split()) # Converts resulting string to a list
    return tweets

def get_trending(city, country):
    '''
    Return a list of the trending topics for a given location.
    '''
    # Get location ID
    client = yweather.Client()
    location_string = city + ", " + country
    location_id = client.fetch_woeid(location_string)
    print(location_id)

    # Get trending topics
    twitter = load_twitter()
    trending = []
    for trend in twitter.get_place_trends(id = location_id)[0]['trends']:
        trending.append(trend['name'])

    return trending

def get_random_trending(city, country, num):
    '''
    Return some random number of trending topics
    '''
    trending_sample = sample(get_trending(city=city,country=country), num)
    return trending_sample