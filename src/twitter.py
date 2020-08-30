import tweepy
import csv
import json
import pprint
import time

from csv_ops import write_data
from csv_ops import get_hashtags

consumer_key = '87WQdP6nNR6sGCO127y2MZG6E'
consumer_secret = 'FMJ9AExtZJtR6FnhJKqoDuuKsqtdxQ7twtfLGowbFgQTkWhzwN'

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

def writeCSVTest ():
    with open('test_file.csv', mode="w") as test_file:
        test_writer = csv.writer(test_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator = '\n')

        test_writer.writerow(['Jared', '19', 'never learned how to read'])
        test_writer.writerow(['rachel', '17', 'vibing'])

def getTweet ():
    for tweet in tweepy.Cursor(api.user_timeline, id='metrospeedy').items(1):
        dict = tweet
        return dict

# returns list of all tweets from timeline
def getTweetDict ():
    dictList = []
    for tweet in tweepy.Cursor(api.user_timeline, id='metrospeedy').items():
        dict = tweet._json
        dictList.append(dict)
    return dictList

# filters tweets and returns list of original tweets
def filterOriginal (tweetList):
    originalTweets = [] 
    for tweet in tweetList:
        if "retweeted_status" not in tweet:
            originalTweets.append(tweet)
            del tweet['user'] # no need for user object 
    return originalTweets

def writeCSV (tweetDict):
    with open('tweet_data.csv', mode='w') as tweet_data:
        fieldnames = list(tweetDict.keys())
        writer = csv.DictWriter(tweet_data, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'name':'rachel','age':17,'sign':'aries'})

# testDict = {
#     'name':'rachel',
#     'age':17,
#     'sign':'aries'
# }

# tweetList = getTweetDict()
# originals = filterOriginal(tweetList)
# pprint.pprint(originals[0])

# test = getTweetDict()
# test = filterOriginal(test)
# x = len(test)
# pprint.pprint(test[x - 1])

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

# search = ["#avotoast", "#metrospeedy"] # 20 and 0 tweets
# tweet_list = mine_tweets(search)
# count_dict = tweet_count(
#     keys = search,
#     tweet_list = tweet_list
# )

# print(count_dict)

# hashtags = get_hashtags()
# tweet_list = mine_tweets(hashtags)
# count_dict = tweet_count(
#     keys = hashtags,
#     tweet_list = tweet_list
# )
# write_data(
#     file = "twitter_hashtags.csv",
#     fieldnames = ["hashtag", "tweet count"],
#     data = count_dict
# )
# print("all done")

# write_data(
#     file = "twitter_hashtags.csv",
#     fieldnames = ["hashtag", "tweet count"],
#     data = data
# )


for tweet in tweepy.Cursor(api.search, q="avocado toast").items(1):
    pprint.pprint(tweet._json)













