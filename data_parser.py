#Data Parser
#Myles Scholz

import re

f = open("words.txt")
words = []
tuples = []

for x in f:
	x = x.lower()
	x = x.replace("\n","%")
	x = re.sub("[^a-zA-Z\-%]+","'",x)
	if "'" not in x:
		words.append(x)

for x in range(0,len(words)):
	words[x] = list(words[x])

for x in range(0,len(words)):
	tuples.append(list(zip(words[x][:], words[x][1:])))

print(tuples)