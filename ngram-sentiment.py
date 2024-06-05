from nltk.stem import WordNetLemmatizer, PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
import sklearn.naive_bayes
import random

def calcNGrams_train(trainFile):
	"""
	trainFile: a text file, where each line is arbitratry human-generated text
	Outputs n-grams (n=2, or n=3, your choice). Must run in under 120 seconds
	"""
	trainF = open(trainFile, "r", encoding="utf8")

	corpus = []
	global probability_dict
	probability_dict = dict()

	train_line = trainF.readline() # read first line
	while train_line != '': # read until EOF
		corpus.append(train_line)
		train_line = trainF.readline()
	# corpus now contains each line from our trainingFile
	vectorizer = CountVectorizer(ngram_range=(1, 2))
	document_feature_matrix = vectorizer.fit_transform(corpus).toarray() # document-feature matrix of 1-grams and 2-grams
	vocab_dict = vectorizer.vocabulary_ # vocabulary from trainFile

	for key in vocab_dict:
		aggregate_probability = 0
		Ngram = key.split()
		if len(Ngram) == 1:
			continue
		for document in document_feature_matrix:
			aggregate_probability += document[vocab_dict[key]]+1/(document[vocab_dict[Ngram[0]]]+len(vectorizer.vocabulary_)) # C(w_n-1*w_n)+1/C(w_n-1)+|V|
		average_probability = aggregate_probability/len(document_feature_matrix)
		probability_dict[key] = average_probability

	trainF.close()
	pass #don't return anything from this function!

def calcNGrams_test(sentences):
	"""
	sentences: A list of single sentences. All but one of these consists of entirely random words.
	Return an integer i, which is the (zero-indexed) index of the sentence in sentences which is non-random.
	"""
	vectorizer = CountVectorizer(ngram_range=(2, 2))
	sentence_feature_matrix = vectorizer.fit_transform(sentences).toarray()
	sentences_vocab_dict = vectorizer.vocabulary_

	index = saved_index = 0
	largest_perplexity = -1
	for sentence in sentence_feature_matrix:
		perplexity = 1
		for vocab in sentences_vocab_dict:
			if sentence[sentences_vocab_dict[vocab]] == 0: # vocab isn't in this sentence
				continue
			elif vocab not in probability_dict: # vocab didn't show up in our trainFile (<UNK>)
				perplexity *= 1/.0001 # continue
			else:
				perplexity *= 1/probability_dict[vocab]
		perplexity = perplexity**(1/len(sentences_vocab_dict)) # taking Nth root
		if perplexity > largest_perplexity:
			largest_perplexity = perplexity
			saved_index = index # keep the index of the sentence with the largest perplexity
		index+=1

	return saved_index

def calcSentiment_train(trainFile):
	"""
	trainFile: A jsonlist file, where each line is a json object. Each object contains:
		"review": A string which is the review of a movie
		"sentiment": A Boolean value, True if it was a positive review, False if it was a negative review.
	"""
	import json
	global gnb, vector # Guassian Naive Bayes Classifier, CountVectorizer()

	trainF = open(trainFile, 'r', encoding='utf8')
	jsonObjects = [json.loads(line) for line in trainF.readlines()]
	data_reviews = []
	data_labels = []

	for obj in jsonObjects: # create list of reviews (texts) and list of labels (sentiments)
		data_reviews.append(obj["review"])
		data_labels.append(obj["sentiment"])

	vector = CountVectorizer()
	data_reviews = vector.fit_transform(data_reviews).toarray() # learn vocab of reviews and return vectorized matrix

	gnb = sklearn.naive_bayes.GaussianNB()
	gnb.fit(data_reviews, data_labels) #

	trainF.close()
	pass #don't return anything from this function!

def calcSentiment_test(review):
	"""
	review: A string which is a review of a movie
	Return a boolean which is the predicted sentiment of the review.
	Must run in under 120 seconds, and must use Naive Bayes
	"""
	return gnb.predict(vector.transform([review]).toarray()) # prediction