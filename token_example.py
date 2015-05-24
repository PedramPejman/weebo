from nltk.tokenize import sent_tokenize, word_tokenize

#nltk.download()


text = "Hello there, how are you doing today? The weather is great and python is awesome. The sky is pinkish-blue. You should not eat cardboard."

#print(sent_tokenize(text))
#print(word_tokenize(text))

[print(word) for word in word_tokenize(text)]
