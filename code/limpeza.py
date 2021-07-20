import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

separator = ' '
useless = ["n't", ".", "!", "(", ")", "$", "[", "]", "'", "*", "&", "%", "#"]
stop_words = set(stopwords.words('english'))

data = pd.read_csv("filmes.txt", sep="\t", header=None)

col = []

for sentence in data[0]:
    print(sentence)
    splited = word_tokenize(sentence)
    print(splited)
    sentence = [s for s in sentence if not s in useless]
    sentence = [splt for splt in splited if not splt.lower() in stop_words]
    print(sentence)
    col.append(separator.join(sentence))


data[0] = list(map(lambda x: x.lower(), col))
data.to_csv("base-final.csv", header=None, index=False)



