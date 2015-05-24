from nltk.corpus import *
from nltk.tokenize import word_tokenize

sentence = "This is an example of a dumb sentence with no real actual stuff"

words = word_tokenize(sentence)

stop_words = set(stopwords.words("english"))
print(stop_words)
print(type(stop_words))

#stop_words = set(stop_words)
print(stop_words)

[print(word) for word in words if word not in stop_words]
