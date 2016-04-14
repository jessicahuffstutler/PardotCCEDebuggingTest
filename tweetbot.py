from twython import Twython, TwythonError
import time
# Api info goes here
APP_KEY = 'XXXXXXXX'
APP_SECRET = 'XXXXXXXX'
OAUTH_TOKEN = 'XXXXXXXX'
OAUTH_TOKEN_SECRET = 'XXXXXXXX'
# Use Twython to set up api access to twitter
api = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

try:
    # Read the things we need to tweet
    with open('tweets.txt', 'r+') as tweetsfile:
        tweets = tweetsfile.readlines()
    L = []
    # Loop through all the tweets
    for line in tweets[:]:
        # Attempt to send the tweet
        if line != "\n" and line not in L and len(line) <= 140:
            # What are we tweeting
            print ("Trying to tweet " + line)
            api.update_status(status=line)
            L.append(line)
            # Rate limit
            time.sleep(5)
    # Yey it worked
    print ("I have tweeted AllTheThings!")


except TwythonError, e:
    print str(e)
    # in case it didn't work
    # print("Something Broke :(")
