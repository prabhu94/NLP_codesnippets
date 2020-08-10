# Basic tokenizers, stemming and lemmatizations methods

import nltk
from nltk.corpus import stopwords,wordnet
from nltk.stem import WordNetLemmatizer 
nltk.download('wordnet')
nltk.download("punkt")

stop_words = set(stopwords.words('english')) 
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
    tagged_sentence = nltk.pos_tag(nltk.word_tokenize(sentence))
    return tagged_sentence

def convert_pos_to_wordnet(word, nltk_tag):
    """This method converts nltk tag to wordnet tag"""
    wn_pos = None
    if nltk_tag.startswith('J'):
        wn_pos = wordnet.ADJ
    elif nltk_tag.startswith('V'):
        wn_pos = wordnet.VERB
    elif nltk_tag.startswith('N'):
        wn_pos = wordnet.NOUN
    elif nltk_tag.startswith('R'):
        wn_pos = wordnet.ADV
    else:          
        wn_pos = wordnet.NOUN
    return word, wn_pos

    
def lemmatize_sentence(sentence, lemmatizer):
    """This method uses an nltk lemmatizer on a sentence"""
    wn_tagged_sent = [convert_pos_to_wordnet(x[0],x[1]) for x in get_part_of_speech(sentence)]
    return " ".join([lemmatizer.lemmatize(x[0], pos=x[1]) for x in wn_tagged_sent if not x[0] in stop_words and x[0].isalnum()])
        
