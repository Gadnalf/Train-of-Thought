# Train-of-Thought
Choo choo, lads. To see what's currently up, visit:
http://train-of-thought.herokuapp.com/

To run/test locally, make sure DEBUG is true in settings.py and twitterTools.py

The twitterTools module in debug mode pulls from a file called twitter_credentials.json, so you'll need to make one of those as well in order to use it. When deployed, it uses Heroku's config variables instead.

The Django settings in debug mode pull from a file called django_credentials.json, which works the same as the twitter creds above.
