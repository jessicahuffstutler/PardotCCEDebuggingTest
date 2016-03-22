

from twython import Twython, TwythonError
import time
#Api info goes here
APP_KEY = 'PUhCsjVEHBorDRLQeQ9cHS4gR'
APP_SECRET = '3GAM3vBnHA9AgzJsBPjvkpl4BSLdP2wSkyyv4AC393itY8iJ2S'
OAUTH_TOKEN = '710914192438468608-uHq6GGpscik0vhT67QDgn6K4zJJyCAe'
OAUTH_TOKEN_SECRET = '3Ge7BKUfxEMVthEstT8VeNJKd1Dhrt3RXKdeqeQnfphWA'
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