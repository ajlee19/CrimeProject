#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 17:58:56 2017

@author: seungwooson
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 04:38:22 2017

@author: da_gw3_user1
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 02:49:33 2017

@author: da_gw3_user1
"""
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import string
from nltk.tokenize import sent_tokenize
import pandas as pd
import nltk.data
import re

data = pd.read_excel("./cleaned_crime_data.xlsx")
sentence_spaceout_period(data)
body_to_sentence(data)
regex_by_address = "(of|from|by|)([0-9]* )*([0-9]+[a-z]*|[A-Z]+[a-z]*) ((S|s)t\.|(S|s)treet|(A|a)venue|(A|a)ve|(C|c)ourt|(C|c)t|(D|d)rive|(D|d)r|(L|l)ane|(L|l)n|(R|r)oad|(R|r)d|(B|b)oulevard|(B|b)lvd)( and ([0-9]+[a-z]*|[A-Za-z]+) ((S|s)t\.|(S|s)treet|(A|a)venue|(A|a)ve|(C|c)ourt|(C|c)t|(D|d)rive|(D|d)r|(L|l)ane|(L|l)n|(R|r)oad|(R|r)d|(B|b)oulevard|(B|b)lvd)|)"

# data["Body_Text"][123]
list_sentence_by_regex = filter_compile_justsentence(regex_by_address, data)

stop = set(stopwords.words('english'))
exclude = set(string.punctuation)
lemma = WordNetLemmatizer()

def clean(doc):
    stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
    punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
    normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
    return normalized

doc_clean = [clean(doc).split() for doc in list_sentence_by_regex]

import gensim
from gensim import corpora

dictionary = corpora.Dictionary(doc_clean)

doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]

Lda = gensim.models.ldamodel.LdaModel
ldamodel = Lda(doc_term_matrix, num_topics=3, id2word = dictionary, passes=50)

print(ldamodel.print_topics(num_topics=3, num_words=3))

#58th avenue
#58 avenue
#~avenue and ~avenue
def filter_compile_justsentence(regex, dataset):
    just_sentences = []
    x = 0
    while x < 4092:
        for sentence in dataset["Tokenized_List"][x]:
            if re.search(regex, sentence):
                just_sentences.append(sentence)
        x = x + 1
    return just_sentences
        
#"((st\.|street|ave|dr)(and st\.|street|ave|dr))|([0-9] (st\.|street|ave|dr))"
def sentence_spaceout_period(data):
    x = 0
    while (x < len(data["Body_Text"])):
        data["Body_Text"][x] = str(re.sub(r'(\.)([A-Z0-9"/\\\/])', r'\1 \2', data["Body_Text"][x]))
        x = x + 1

def body_to_sentence(data):    
    tokenized_list = []
    for body in data["Body_Text"]:
        sent_tokenize_list = sent_tokenize(body)
        tokenized_list.append(sent_tokenize_list)    
    data["Tokenized_List"] = tokenized_list

def filter_sentence_add(regex, dataset):
    only_sentences = []
    x = 0
    while x < 4092:
        y = [w for w in dataset["Tokenized_List"][x] if re.search(regex, w)]
        if  y != []:
            only_sentences.append(y)
        else:
            only_sentences.append([])
        x = x + 1
    dataset["Only_Sentences"] = only_sentences

def filter_sentence(regex, dataset):
    only_sentences = []
    x = 0
    while x < 4092:
        sentences = []
        for sentence in dataset["Tokenized_List"][x]:
            if re.search(regex, sentence):
                sentences.append(sentence)
        if sentences != []:
            only_sentences.append(sentences)
        x = x + 1
    return only_sentences
    
#writer = pd.ExcelWriter('cleaned_and_parsed_crime_data.xlsx')
#data.to_excel(writer, 'Sheet1')
#writer.save()
#
#https://www.analyticsvidhya.com/blog/2016/08/beginners-guide-to-topic-modeling-in-python/
#https://github.com/Theano/Theano/issues/6099
#https://www.analyticsvidhya.com/blog/2016/10/17-ultimate-data-science-projects-to-boost-your-knowledge-and-skills/
#https://www.analyticsvidhya.com/blog/2017/07/debugging-neural-network-with-tensorboard/
#https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present/ijzp-q8t2
#https://www.analyticsvidhya.com/blog/2017/07/word-representations-text-classification-using-fasttext-nlp-facebook/
#http://www.nltk.org/book/ch06.html
#https://www.google.co.jp/search?q=topic+classification+python&rlz=1C1CHBD_enJP736JP736&oq=topic+classification+python&aqs=chrome..69i57.9007j0j7&sourceid=chrome&ie=UTF-8
#https://docs.python.org/2/library/re.html
#https://www.google.co.jp/search?q=regex+plus+sign&rlz=1C1CHBD_enJP736JP736&oq=regex+plus+sign+&aqs=chrome..69i57j0l5.3654j0j4&sourceid=chrome&ie=UTF-8
#https://stackoverflow.com/questions/199059/im-looking-for-a-pythonic-way-to-insert-a-space-before-capital-letters
#https://stackoverflow.com/questions/16327405/syntaxerror-unexpected-eof-while-parsing
#https://stackoverflow.com/questions/3028642/regular-expression-for-letters-numbers-and
#https://stackoverflow.com/questions/2912894/how-to-match-any-character-in-java-regular-expression
#https://en.wikipedia.org/wiki/Bass_diffusion_model
#https://docs.python.org/2/library/re.html
#http://regexr.com/
#http://www.latlong.net/
#https://stackoverflow.com/questions/3652951/google-maps-api-get-coordinates-of-address
#https://developers.google.com/maps/documentation/geocoding/intro#ComponentFiltering
#http://machinelearningmastery.com/tune-lstm-hyperparameters-keras-time-series-forecasting/

