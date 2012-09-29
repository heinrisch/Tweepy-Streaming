#This is a simple example of the Tweepy streaming functinallity. It will listen to
#all tweets containing "android" and will keep track of the hashtags used in the tweets.

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import oauthHandler
import json

tweetDict = dict() 
parsedTweets = 0

#Handeling tweets, updating dict, and writing a log
def parseTweet(tweet):
	global tweetDict
	global parsedTweets
	#Look for all tags and update our tweetDict
	for tag in tweet.hashtags:
		t = tag["text"]
		if(tweetDict.has_key(t)):
			tweetDict[t] += 1
		else:
			tweetDict[t] = 1
	parsedTweets += 1
	#Every 10th tweet we will output the most popular tag and write the info to the log
	if(parsedTweets > 10):
		parsedTweets = 0
		maxi = 0
		maxTag = str()
		count = 0
		for tag in tweetDict:
			num = tweetDict[tag]
			count += num
			if(num > maxi and tag.lower() != "android"):
				maxi = num
				maxTag = tag
		output = "Most Popular: " + maxTag + " with " + str(maxi) + ". Dict Entries: " + str(len(tweetDict)) + ". Tags parsed: " + str(count)
		f = open("log.txt","a")
		f.write(output + "\n")
		print output 
			

#Tweet class with all the information we need for this program (Hashtags and the actual tweet text)
class Tweet:
        text = str()
	hashtags = []

        def __init__(self, json):
		self.text = json["text"] 
		self.hashtags = json["entities"]["hashtags"]

#Basic listener which parses the json, creates a tweet, and sends it to parseTweet
class TweetListener(StreamListener):
	def on_data(self, data):
		jsonData = json.loads(data)
		tweet = Tweet(jsonData)
		parseTweet(tweet)
		return True

	def on_error(self, status):
		print status


if __name__ == '__main__':
	parsedTweets = 0
	listener = TweetListener()
	auth = oauthHandler.getAuth()
	stream = Stream(auth, listener)	
	stream.filter(track=['android']) #This will start the stream and make callbacks to the listener for all tweets containing "android"


