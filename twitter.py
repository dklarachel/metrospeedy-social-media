import tweepy
import csv
import json
import pprint

consumer_key = '87WQdP6nNR6sGCO127y2MZG6E'
consumer_secret = 'FMJ9AExtZJtR6FnhJKqoDuuKsqtdxQ7twtfLGowbFgQTkWhzwN'

auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)

# for tweet in tweepy.Cursor(api.search, q='tweepy').items(10):
#     print(tweet.text)

def getAnyTweets ():
    for tweet in tweepy.Cursor(api.search, q='delivery').items(10):
        return tweet.author

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
    return originalTweets

def writeCSV (tweetDict):
    with open('tweet_data.csv', mode='w') as tweet_data:
        fieldnames = list(tweetDict.keys())
        writer = csv.DictWriter(tweet_data, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'name':'rachel','age':17,'sign':'aries'})

testDict = {
    'name':'rachel',
    'age':17,
    'sign':'aries'
}

tweetList = getTweetDict()
originals = filterOriginal(tweetList)
print(len(originals))













