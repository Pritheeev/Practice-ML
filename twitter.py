import tweepy as tp
from textblob import TextBlob

conskey = 'UC1O2NiKUNRmNq0yLqK3vs1p8'
conssecret = 'ppKqh2x5X5dT50Iqo2LbD01QSXYmykpX8f7M7Dv5oPQLooftbX'

access_token = '185627100-3KAP9iBM3uUZBJ0labpE7k4pWTYjziD8xrX4Ol2K'
access_secret = 'kAH5RQJiQZg7IRGeCWNr0jHlkBD5PStkNwhBFvFE4h7MI'

#authentication 

auth = tp.OAuthHandler(conskey,conssecret)
auth.set_access_token(access_token,access_secret)
api = tp.API(auth)

publictweets = api.search(str(input("Enter a search keyword: ")))

for tweet in publictweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
