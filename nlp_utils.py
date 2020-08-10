# Basic tokenizers, stemming and lemmatizations methods

import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer 
  
lemmatizer = WordNetLemmatizer() # Word net lemmatizer is pretty elaborate in its approach read this : https://www.machinelearningplus.com/nlp/lemmatization-examples-python/
    
def remove_stopwords (sentence, stopwords_list):
    """This method removes stop words from an untokenized/tokenized sentence and returns a token of strings"""
    final_tokens = []
    for each_word in sentence:
        if each_word not in stopwords_list:
            final_tokens.append(each_word)
    return final_tokens

def get_part_of_speech(sentence):
    """This method gets the part of speech in context of the sentence the word is in, 
    this is better than using the vanilla lemmatizer without any part of speech tag. 
    Also this returns Wordnet tags which can directly
    be used in the wordnet lemmatizer. Use this before removing stop words. Note this is NLTK specific"""
    if nltk_tag.startswith('J'):
        return wordnet.ADJ
    elif nltk_tag.startswith('V'):
        return wordnet.VERB
    elif nltk_tag.startswith('N'):
        return wordnet.NOUN
    elif nltk_tag.startswith('R'):
        return wordnet.ADV
    else:          
        return wordnet.NOUN
    
def lemmatize_word(word, part_of_speech, lemmatizer):
    """This method uses an nltk lemmatizer on one word"""
    return lemmatizer.lemmatize(word, pos = part_of_speech)
    

