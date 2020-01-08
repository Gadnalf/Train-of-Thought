from twython import Twython
import json


def search_twitter(search_text, num):
    '''
    Search twitter with the given text and returns a number of tweets.
    '''
    
    # Load credentials from json file
    with open("twitter_credentials.json", "r") as file:
        creds = json.load(file)

    # Get twitter
    twitter = Twython(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])

    # Fetch tweets
    tweets = []
    for status in twitter.search(q = search_text, count = num, lang = 'en', tweet_mode = 'extended')['statuses']:
        tweets.append(status['full_text'].split()) # Converts resulting string to a list
    return tweets

tweets = search_twitter("dab", 20)
i = 0
for tweet in tweets:
    i += 1
    print("tweet " + str(i) + ":")
    print(' '.join(tweet))

