#Data Parser
#Myles Scholz

import re
import numpy as np

def load_data():
	f = open("words.txt")
	abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","-","%"]
	words = []
	tuples = []
	tr_d = []
	te_d = []
	va_d = []

	for x in f:
		x = x.lower()
		x = x.replace("\n","%")
		x = re.sub("[^a-z\-%]+","'",x)
		if "'" not in x:
			words.append(x)

	for x in range(0,len(words)):
		words[x] = list(words[x])

	for x in range(0,len(words)):
		word_tuples = list(zip(words[x][:], words[x][1:]))
		for i in range(0, len(word_tuples)):
			tuples.append((abc.index(word_tuples[i][0]), abc.index(word_tuples[i][1])))

	np.random.shuffle(tuples)
	print(tuples)

	tr_i = int(0.7*len(tuples))
	tr_d = np.array(tuples[i] for i in range(0, tr_i))

	te_i = int(0.2*len(tuples))
	te_d = np.array(tuples[j] for j in range(tr_i, tr_i + te_i))

	va_i = int(0.1*len(tuples))
	va_d = np.array(tuples[k] for k in range(te_i, te_i + va_i))

	return (tr_d, te_d, va_d)

def load_data_wrapper():
	data = load_data()
	

def vectorized_result(j):
	e = np.zeros((28,1))
	e[j] = 1.0
	return e