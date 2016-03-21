

from twython import Twython, TwythonError
import time

APP_KEY = 'YourAppKey'
APP_SECRET = 'YourAppSecret'
OAUTH_TOKEN = 'YourOauthToken'
OAUTH_TOKEN_SECRET = 'YourOauthTokenSecret'

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

try:
	with open('tweets.txt', 'r+') as tweetfile:
		tweets = tweetfile.readlines()

	for line in tweets[:]:
		
		print ("Tweeting.....")
		twitter.update_status(status=line) #Send the tweet.
		time.sleep(5)
		
	print ("I have tweeted AllTheThings!") 


except TwythonError as e:
	print (e)
