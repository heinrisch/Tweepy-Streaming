from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import oauthHandler
import json

tweetDict = dict()
parsedTweets = 0

def parseTweet(tweet):
	global tweetDict
	global parsedTweets
	for tag in tweet.hashtags:
		t = tag["text"]
		if(tweetDict.has_key(t)):
			tweetDict[t] += 1
		else:
			tweetDict[t] = 1
	parsedTweets += 1
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
			

class Tweet:
        text = str()
	hashtags = []

        def __init__(self, json):
		self.text = json["text"] 
		self.hashtags = json["entities"]["hashtags"]

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
	stream.filter(track=['android'])


