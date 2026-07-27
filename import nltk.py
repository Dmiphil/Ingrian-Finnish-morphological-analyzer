import nltk
nltk.download('popular')
nltk.download('punkt')
nltk.download('stopwords')

nltk.download('punkt_tab')

text = "The quick brown fox jumps over the lazy dog. This is a test sentence."
tokenizer = nltk.word_tokenize(text)

print(tokenizer)

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

stemmer = PorterStemmer()
text = "The stemmed form of leaves is leaf"
tokens = word_tokenize(text)
stemmed_words = [stemmer.stem(word) for word in tokens]
print(stemmed_words)
