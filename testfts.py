import json
from sentences import Sentences
from words import Words
from punctuation import Punctuation
from stem import Stemming
import corpus

# load stemming form
st = corpus.stemming()

tlist = []

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
print(tlist)
