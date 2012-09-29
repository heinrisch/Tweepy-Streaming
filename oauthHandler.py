# module oath
import tweepy

# == OAuth Authentication ==
#
# This mode of authentication is the new preferred way
# of authenticating with Twitter.

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
consumer_key="CONSUMER KEY HERE"
consumer_secret="CONSUMER SECRET HERE"

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located 
# under "Your access token")
access_token="ACCESS TOKEN HERE"
access_token_secret="ACCESS TOKEN SECRET HERE"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


def getAPI():
	api = tweepy.API(auth)
	print "DEBUG: " + api.me().name + " is no logged in!"
	return api

def getAuth():
	return auth
