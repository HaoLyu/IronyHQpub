# -*- coding: utf-8 -*-
# This file generates a user’s topic proportions under LDA with 100 topics over all tweets 
# This class HistoryTopic has one parameters: author_name
# author_name: The screen name of specific author 
# The class returns two value: topic_top_10_words & author_topics_proportion
# topic_top_10_words: this list contain 100 topics and there are 10 words representing each topic
# author_topics_proportion: this list contains the author’s topic proportions with 100 topics
from __future__ import division, print_function

import numpy as np
import lda
import Tweet_Transfer_BOW as BOW
import sklearn
from sklearn.feature_extraction.text import CountVectorizer
import AllTweets as AllT

# Function find_author_id helps find a author_id through his/her screen name
def find_author_id(author_name):
	
	for n in range(len(AllT.collect_tweets())):

		if(author_name == AllT.collect_tweets()[n][0]):
			return n
		else:
			next

# HistoryTopic is used to generate topic proportions of one author
class HistoryTopic(object):

	def __init__(self,  author_name):
		self.tweets = AllT.collect_text()
		self.id = find_author_id(author_name)
		
		# build the data matrix and vocabulary by 
		# tokenizing and cleaning stop-words 
		self.vocab = BOW.Get_BOW(self.tweets)[0]
		self.data =  BOW.Get_BOW(self.tweets)[1]

	def show_data(self):
		# data matrix
		print("type(data): {}".format(type(self.data)))
		print("shape: {}\n".format(self.data.shape))
	
		# tweets for each author 
		print("type(tweets): {}".format(type(self.tweets)))
		print("shape: {}\n".format(len(self.tweets)))
	
		# the vocab
		print("type(vocab): {}".format(type(self.vocab)))
		print("len(vocab): {}\n".format(len(slef.vocab)))
	
	def get_topics_proportions(self):
		# Fitting the model
		model = lda.LDA(n_topics=100, n_iter=2000, random_state=1)
		model.fit(self.data)

		# Topic-Word
		topic_top_10_words = []
		topic_word = model.topic_word_
		for n in range(len(topic_word)):
			topic_top_10_words.append(np.array(self.vocab)[np.argsort(topic_word[n])[:-11:-1]])
		
		# Document-Topic
		doc_topic = model.doc_topic_
		author_topics_proportion = doc_topic[self.id]

		return (topic_top_10_words, author_topics_proportion)


if __name__ == "__main__":
	print ("This is used as python file, not imported")
	UserTopic = HistoryTopic('TuomoMa')
	print (UserTopic.get_topics_proportions()[0])
