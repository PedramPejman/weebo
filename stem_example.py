from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

sent = "It is very impornt to do impornt-looking things just so we know how to do them."
words =  word_tokenize(sent)

[print(ps.stem(w)) for w in words]
