from twython import Twython
import yweather
import json

def load_twitter():
    # Load credentials from json file
    with open("twitter_credentials.json", "r") as file:
        creds = json.load(file)

    # Get twitter
    twitter = Twython(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])
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


trending = get_trending("toronto", "canada")
print(trending)

tweets = search_twitter("dab", 20)
i = 0
for tweet in tweets:
    i += 1
    print("tweet " + str(i) + ":")
    print(' '.join(tweet))

