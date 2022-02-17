# Experiment 2 - Data pre processing with tokenization

import nltk
nltk.download('punkt') # if it is not downloaded already

# input_str = "The Wire is an Indian nonprofit news and opinion website which publishes in English, Hindi, Marathi, and Urdu."
input_str ="The Wire is an Indian nonprofit news and opinion website which publishes in English, Hindi, Marathi, and Urdu. It was founded in 2015 by Siddharth Varadarajan, Sidharth Bhatia, and M. K. Venu and is organized as a nonprofit organization named the Foundation for Independent Journalism."
lowercase_input_str = input_str.lower()

from nltk.tokenize import word_tokenize, sent_tokenize

sentence_tok = sent_tokenize(lowercase_input_str)
word_tok = word_tokenize(lowercase_input_str)

print(sentence_tok)
print(word_tok)