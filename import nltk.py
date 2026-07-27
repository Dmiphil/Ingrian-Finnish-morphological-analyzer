from nltk import translate
import nltk
nltk.download('popular')
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')
nltk.download('omw-1.4')

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

from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

lemmatizer = WordNetLemmatizer()
text = "The lemmatized form of leaves is leaf"
tokens = word_tokenize(text)
lemmatized_words = [lemmatizer.lemmatize(word) for word in tokens]
print(lemmatized_words)

