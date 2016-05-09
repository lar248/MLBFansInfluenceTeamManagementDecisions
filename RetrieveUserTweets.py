#!/usr/bin/env python
# encoding: utf-8

# Script taken from https://gist.github.com/yanofsky/5436496#file-tweet_dumper-py

import tweepy #https://github.com/tweepy/tweepy
import csv
import time
from os import path

#Variables that contains the user credentials to access Twitter API
access_key = "3300938639-wOqh3kNzoq7XQfHDS4g7ywLO16fh5IryeypOotd"
access_secret = "QlF4awsLV55FodGrtSUiEgHd9t6MswBcafE4AURO177SR"
consumer_key = "lFV1kFxvXac4yQUV0gqAZC78t"
consumer_secret = "XOsojLuqrKk1MhwJB5uTLWVKwRKmcBx3RR9vFFmSztjJCTPwJo"


def get_all_tweets(screen_name):
	#Twitter only allows access to a users most recent 3240 tweets with this method
	
	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
	
	#initialize a list to hold all the tweepy Tweets
	alltweets = []	
	print "made it before asking for user_timeline"
	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name,count=200)
	print "AFTER asking for user_timeline"
	#save most recent tweets
	alltweets.extend(new_tweets)
	
	#save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1

	print "Starting download"
	
	#keep grabbing tweets until there are no tweets left to grab
	while len(new_tweets) > 0:
		# print "getting tweets before %s" % (oldest)
		
		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
		
		#save most recent tweets
		alltweets.extend(new_tweets)
		
		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1
		
		# print "...%s tweets downloaded so far" % (len(alltweets))
	
	#transform the tweepy tweets into a 2D array that will populate the csv	
	outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]
	
	print "Download complete"

	file_path_string = "Mets/"+screen_name+".csv"
	file_path = path.relpath(file_path_string)
	#write the csv	
	with open(file_path, 'wb') as f:
		writer = csv.writer(f)
		writer.writerow(["id","created_at","text"])
		writer.writerows(outtweets)
	
	pass

	print "Successful write: " + screen_name


if __name__ == '__main__':
	#pass in the username of the account you want to download
	filename = open('finalList.txt', 'r')
	line = filename.readline()
	## If the file is not empty keep reading line one at a time
	## till the file is empty
	while line:
		try:
			line = line.strip()
			get_all_tweets(line)
			line = filename.readline()
		except:
			print "Sleep for 15 min"
			time.sleep(15*60)
	filename.close()