#Data Parser
#Myles Scholz

f = open("words.txt")
words = []
for x in f:
	x = x.lower()
	x = x.replace("\n","%")
	if "'" not in x:
		words.append(x)

for x in range(0,len(words)):
	words[x] = list(words[x])

print(words)