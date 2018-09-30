import nltk

from nltk.tokenize import word_tokenize, sent_tokenize

example = 'Hello Mr. Smith, how are you doing today? The weather is awesome. The water is blueish-pink. I like to eat ' \
          'pizza. Thank you very much.'

print(sent_tokenize(example))
print(word_tokenize(example))

for word in word_tokenize(example):
    print(word)