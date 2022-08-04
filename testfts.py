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

for i in list(d.items()):
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
while True:
    nlist = []
    klist = []
    inp =input("text:")
    t = tokenize(inp)
    for i in t:
        if i in memo.keys():
            nlist.append(memo[i])

    for i in nlist:
        for j in i:
            klist.append(j)
    print(dlist[max(set(klist), key = lambda x: klist.count(x))])
