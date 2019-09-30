# Import the necessary package to process data in JSON format

try:
    import json
except ImportError:
    import simplejson as json

# Import the tweepy library
import tweepy
# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = 'key'
ACCESS_SECRET = 'key'
CONSUMER_KEY = 'key'
CONSUMER_SECRET = 'key'

# Setup tweepy to authenticate with Twitter credentials:
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

# Create the api to connect to twitter with your creadentials
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)
file=open('/home/ece-student//Desktop/EC 601 Mini 1/twitter_stream_10tweets.txt',"w+")
file.write("There are 10 twitters here.")
file.write('\n')
a=0
for status in tweepy.Cursor(api.search, q='restaurant', lang='en').items(10):
 a= a+1
 file.write(str(a)+"."+" ")
 file.write(status.text+'\n')

file.close()
#---------------------------------------------------------------------------------------------------------------------
# Twitter API development use pagination for Iterating through timelines, user lists, direct messages, etc. 
# To help make pagination easier and Tweepy has the Cursor object.
#---------------------------------------------------------------------------------------------------------------------
