import json
from words import Words
from stem import Stemming
import corpus

# load stemming form
st = corpus.stemming()

tlist = []
memo = {}

with open("data.json", "r") as file:
    d = json.load(file)

for i in list(d.items()):
    k, v = i
    # tokenize to words
    w = Words(v)
    wl = w.load()

    # load stop words
    stop = corpus.stopwords("ru")
    stopfiltered = [str(x) for x in wl if x not in stop]

    # stemming text
    stemming = Stemming(*st)
    s = stemming.load(stopfiltered)
    tlist.append(s)


for i in tlist:
    for j in i:
        if j not in memo.keys():
            triallist = []
            for k in tlist:
                if j in k:
                    triallist.append(tlist.index(k))
            memo[j] = triallist
print(memo)
