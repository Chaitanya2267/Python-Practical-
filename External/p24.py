from nltk.tokenize import word_tokenize, sent_tokenize

text = "Python is a programming language. It is easy to learn."

words = word_tokenize(text)
print("Word Tokens:")
print(words)

sentences = sent_tokenize(text)
print("Sentence Tokens:")
print(sentences)