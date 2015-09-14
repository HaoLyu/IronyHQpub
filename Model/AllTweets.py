# This file has two functions
# collect_tweets get the list 'tweets', which contain all tweetAuthors and tweetTexts
# collect_text get the list 'tweets_text', which contain all tweetText
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('127.0.0.1', 27017)
db = client['IronyHQ']
dbtweets = db.tweets

# Collect all tweets from MongoDB
def collect_tweets():
	tweets = []

	for n in range(dbtweets.find().count()):
		tweetAuthor = dbtweets.find()[n]['author']
		tweetText = dbtweets.find()[n]['text']
		tweets.append([tweetAuthor, tweetText])

	return tweets

# Collect all tweets text 
def collect_text():
	tweets_text = []

	for n in range(len(collect_tweets())):
		tweets_text.append(collect_tweets()[n][1])

	return tweets_text

if __name__ == '__main__':
	print "This is used as python file, not imported"
