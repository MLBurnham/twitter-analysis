from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from tweepy import API
from tweepy import Cursor
import csv
from Twitter_keys import *
import os
os.chdir(r'C:\Users\Mike\Desktop\Projects\Twitter')

class TwitterListener(StreamListener):
    """
    A Basic listener for printing out tweets and writing in csv
    """
    # redefine the on_status method from the StreamListener class. determines what to do with data when a status is retrieved
    def on_status(self, status):
        # print statement just to verify it's streaming
        print(status.author.screen_name, status.created_at, status.text)
        # opens the file to append, uses dictionary writer to separate into columns
        with open('tweetDB.csv', 'a') as file:
            csvWriter = csv.DictWriter(file, fieldnames=['Username', 'Screenname', 'Time', 'Text', 'Retweets', 'Favorites'],
                                        lineterminator='\n')
            csvWriter.writerow({'Username': status.author.name.encode('UTF-8'),
                             'Screenname': status.author.screen_name.encode('UTF-8'),
                             'Time': status.created_at,
                             'Text': status.text.encode('UTF-8'),
                             'Retweets': status.retweet_count,
                             'Favorites': status.favorite_count})

    def on_error(self, status):
        if status == 420:
            # return false on data method in case rate limit occurs
            return False
        print(status)

# set my Authenticators
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

# set parameters for csv and write column header
with open('tweetDB.csv', 'a') as file:
    csvWriter = csv.DictWriter(file, fieldnames=['Username', 'Screenname', 'Time', 'Text', 'Retweets', 'Favorites'],
                               lineterminator='\n')
    csvWriter.writeheader()

# activate streamer
streamingAPI = Stream(auth, TwitterListener())
streamingAPI.filter(track=['test'])
