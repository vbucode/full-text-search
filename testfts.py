import json
from words import Words
from stem import Stemming
import corpus

# load stemming form
st = corpus.stemming()

dlist = []
memo = {}

with open("data.json", "r") as file:
    d = json.load(file)

def tokenize(text):
    w = Words(text)
    wl = w.load()

    # load stop words
    stop = corpus.stopwords("ru")
    stopfiltered = [str(x) for x in wl if x not in stop]

    # stemming text
    stemming = Stemming(*st)
    s = stemming.load(stopfiltered)
    return s

def indexing(arg):
    for i in list(arg.items()):
        k, v = i
        dlist.append(tokenize(v))

    for i in dlist:
        for j in i:
            if j not in memo.keys():
                triallist = []
                for k in dlist:
                    if j in k:
                        triallist.append(dlist.index(k))
                memo[j] = triallist
    #return memo

def fsearch(arg):
    for i in arg:
        if i in memo.keys():
            nlist.append(memo[i])

    for i in nlist:
        for j in i:
            klist.append(j)
    return dlist[max(set(klist), key = lambda x: klist.count(x))]

din = indexing(d)

while True:
    nlist = []
    klist = []
    inp =input("text:")
    t = tokenize(inp)
    print(fsearch(t))
