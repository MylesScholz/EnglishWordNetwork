#Data Parser
#Myles Scholz

import re
import numpy as np
import pickle as p

def make_data():
    f = open("words.txt")
    abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","-","%"]
    words = []
    word_tuples = []
    tr_d = []
    te_d = []
    va_d = []
    switch = True

    for x in f:
        x = x.lower()
        x = x.replace("\n","%")
        x = re.sub("[^a-z\-%]+","'",x)
        if "'" not in x:
            if switch:
                words.append(x)
            switch = not switch

    for x in range(0,len(words)):
        words[x] = list(words[x])

    for word in words:
        word_list = list(zip(word[:], word[1:]))
        for i in word_list:
            word_tuples.append(i)
    tuples = [(vector(abc.index(i[0])), vector(abc.index(i[1]))) for i in word_tuples]

    np.random.shuffle(tuples)

    tr_i = int(0.7*len(tuples))
    for i in range(0, tr_i): tr_d.append(tuples[i])

    te_i = int(0.2*len(tuples))
    for j in range(tr_i, tr_i + te_i): te_d.append(tuples[j])

    va_i = int(0.1*len(tuples))
    for k in range(te_i, te_i + va_i): va_d.append(tuples[k])
    
    tr_d = np.array(tr_d)
    te_d = np.array(te_d)
    va_d = np.array(va_d)
    
    f = open("data.p","wb")
    p.dump((tr_d, te_d, va_d),f)
    f.close()
    
def load_data():
    f = open("data.p","rb")
    tr_d, te_d, va_d = p.load(f)
    f.close()
    return (tr_d, te_d, va_d)

def vector(j):
    e = np.zeros((28,1))
    e[j] = 1.0
    return e