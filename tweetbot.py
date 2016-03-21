

from twython import Twython, TwythonError
import time

APP_KEY = 'XXXXXXXX'
APP_SECRET = 'XXXXXXXX'
OAUTH_TOKEN = 'XXXXXXXX'
OAUTH_TOKEN_SECRET = 'XXXXXXXX'

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

try:
	with open('tweets.txt', 'r+') as tweetsfile:
		tweets = tweetsfile.readlines()

	for line in tweets[:]:
		
		print ("Trying to tweet " + line)
		twitter.update_status(status=line) #Send the tweet.
		time.sleep(5)
		
	print ("I have tweeted AllTheThings!") 


except TwythonError as e:
	print (e)
