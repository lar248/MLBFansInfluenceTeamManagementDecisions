__author__ = 'LaurenceRosenzweig'

#Came from tutorial: http://adilmoujahid.com/posts/2014/07/twitter-analytics/

#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import Cursor
from tweepy import API
import time

#Variables that contains the user credentials to access Twitter API
access_token = "3300938639-wOqh3kNzoq7XQfHDS4g7ywLO16fh5IryeypOotd"
access_token_secret = "QlF4awsLV55FodGrtSUiEgHd9t6MswBcafE4AURO177SR"
consumer_key = "lFV1kFxvXac4yQUV0gqAZC78t"
consumer_secret = "XOsojLuqrKk1MhwJB5uTLWVKwRKmcBx3RR9vFFmSztjJCTPwJo"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status

def parseTwitterHandles(fileToReadFrom, fileToWriteTo):
    f = open(fileToReadFrom, 'r')

    with open(fileToWriteTo, 'w') as x:
        for line in iter(f):
            index = line.find("@")
            if index != -1:
                x.write(line[index+1:])
            else:
                x.write(line)

    f.close()


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    api = API(auth)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    # stream.filter(track=['Cespedes'])
    # https://api.twitter.com/1.1/followers/ids.json?cursor=-1&screen_name=andypiper&count=5000

    # for user in Cursor(api.followers, screen_name="ynscspds").items():
    #     print user.screen_name


    #this link: http://stackoverflow.com/questions/29635706/how-to-get-twitter-followers-list
    # list= open('twitter_followers_jasonheyward.txt','w')

    parseTwitterHandles('twitter_followers_BenZobrist.txt', 'twitter_followers_final_BenZobrist.txt')

    # if(api.verify_credentials):
    #     print 'We successfully logged in'

    # user = Cursor(api.followers, screen_name="jasonheyward").items()

    # while True:
    #     try:
    #         u = next(user)
    #         print u.screen_name
    #         list.write(u.screen_name +' \n')

    #     except:
    #         # time.sleep(15*60)
    #         print 'We got a timeout ... Sleeping for 15 minutes'
    #         u = next(user)
    #         list.write(u.screen_name +' \n')
    # list.close()