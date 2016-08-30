#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "37426914-RixhdpIrAY73ux90jeUVsLDSKSjBW1osWbqrU3HGX"
access_token_secret = "lCCgHbkv9deebtFvjAaZphqMlyuTqrRYJROZaTud0F9Wt"
consumer_key = "2OsY5fCZCYX6Zw5VEQ6XKsyLQ"
consumer_secret = "ub3a2nRD7Dx9kVESEewKqvbEvF6DKuJxScumLHEvez14xeSUlc"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['hilary', 'hillary', 'trump'])