import tweepy
import csv
import json
import pprint
import time

from csv_ops import write_data
from csv_ops import get_hashtags

from settings import TWITTER_KEY, TWITTER_SECRET

consumer_key = TWITTER_KEY
consumer_secret = TWITTER_SECRET

auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)

# for tweet in tweepy.Cursor(api.search, q='tweepy').items(10):
#     print(tweet.text)

def tweets_from_search (query):
    '''get all tweets from search query'''
    tweet_list = []
    counter = 0
    for tweet in tweepy.Cursor(api.search, q=query, wait_on_rate_limit=True, wait_on_rate_limit_notify=True).items():
        tweet_list.append(tweet)
        counter += 1
        print(counter)
        # counter += 1
        # if counter % 200 == 0:
        #     time.sleep(900) # rest 15 mins
        #     print("sleeping for 15 mins")
    print("mined tweets for {}".format(query))
    return tweet_list

def getTweets ():
    favorite_count_list = []
    for tweet in tweepy.Cursor(api.user_timeline, id='metrospeedy').items():
        favorite_count_list.append(tweet.favorite_count)
    return favorite_count_list

def getTweet ():
    for tweet in tweepy.Cursor(api.user_timeline, id='metrospeedy').items(1):
        dict = tweet
        return dict

def getTweetDict ():
    '''returns list of all tweets from timeline'''
    dictList = []
    for tweet in tweepy.Cursor(api.user_timeline, id='metrospeedy').items():
        dict = tweet._json
        dictList.append(dict)
    return dictList

def filterOriginal (tweetList):
    '''filters tweets and returns list of original tweets'''
    originalTweets = [] 
    for tweet in tweetList:
        if "retweeted_status" not in tweet:
            originalTweets.append(tweet)
            del tweet['user'] # no need for user object 
    return originalTweets

def mine_tweets (search_queries):
    '''takes list of search queries, returns multidimensional list of lists of tweets'''
    query_list = []
    for query in search_queries:
        query_list.append(tweets_from_search(query))
    print("mined all tweets")
    return query_list

def tweet_count (keys, tweet_list):
    '''takes multidimensional list of tweet lists, returns dictionary using len of lists as values'''
    dict_list = []
    for index, key in enumerate(keys):
        dict = {}
        tweet_count = len(tweet_list[index])
        dict["hashtag"] = key
        dict["tweet count"] = tweet_count
        dict_list.append(dict)
    return dict_list









