# Experiment 3 - Data pre processing with stop word removal

import nltk
nltk.download('stopwords')

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# tokenizing input string
input_str ="The Wire is an Indian nonprofit news and opinion website which publishes in English, Hindi, Marathi, and Urdu. It was founded in 2015 by Siddharth Varadarajan, Sidharth Bhatia, and M. K. Venu and is organized as a nonprofit organization named the Foundation for Independent Journalism."
lowercase_input_str = input_str.lower()
word_tok = word_tokenize(lowercase_input_str)

#stopwords
stopwords_list = list(stopwords.words('english'))

processed = []

for word in word_tok:
  if word not in stopwords_list:
    processed.append(word)

print(processed)