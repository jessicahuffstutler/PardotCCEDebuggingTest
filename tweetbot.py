from twython import Twython, TwythonError
import time
#Api info goes here
APP_KEY = 'XXXXXXXX'
APP_SECRET = 'XXXXXXXX'
OAUTH_TOKEN = 'XXXXXXXX'
OAUTH_TOKEN_SECRET = 'XXXXXXXX'
#Use Twython to set up api access to twitter
api = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

try:
	#Read the things we need to tweet
	with open('tweets.txt', 'r+') as tweetsfile:
		tweets = tweetsfile.readlines()
	#Loop through all the tweets
	for line in tweets[:]:
		#What are we tweeting
		print ("Trying to tweet " + line)
		#Attemp to send the tweet
		api.update_status(status=line)
		#Rate limit 
		time.sleep(5)
	#Yey it worked
	print ("I have tweeted AllTheThings!") 


except TwythonError:
	#in case it didn't work
	print("Something Broke :(")