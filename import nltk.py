import nltk
nltk.download('popular')
nltk.download('punkt')
nltk.download('stopwords')

nltk.download('punkt_tab')

text = "The quick brown fox jumps over the lazy dog. This is a test sentence."
tokenizer = nltk.word_tokenize(text)

print(tokenizer)
