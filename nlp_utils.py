# Basic tokenizers, stemming and lemmatizations methods

import nltk
from nltk.corpus import stopwords
print(stopwords.words('english'))

def remove_stopwords (sentence, stopwords_list):
    """This method removes stop words from an untokenized sentence and returns a token of strings"""
    final_tokens = []
    for each_word in sentence:
        if each_word not in stopwords_list:
            final_tokens.append(each_word)
    return final_tokens

