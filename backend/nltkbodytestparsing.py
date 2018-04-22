#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 17:21:25 2017

@author: seungwooson
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 02:49:33 2017

@author: da_gw3_user1
"""
from nltk.tokenize import sent_tokenize
import pandas as pd
import nltk.data
import re

data = pd.read_excel("./cleaned_crime_data.xlsx")

# data["Body_Text"][123]

regex_by_address = "(of|from|by|)([0-9]* )*([0-9]+[a-z]*|[A-Z]+[a-z]*) ((S|s)t\.|(S|s)treet|(A|a)venue|(A|a)ve|(C|c)ourt|(C|c)t|(D|d)rive|(D|d)r|(L|l)ane|(L|l)n|(R|r)oad|(R|r)d|(B|b)oulevard|(B|b)lvd)( and ([0-9]+[a-z]*|[A-Za-z]+) ((S|s)t\.|(S|s)treet|(A|a)venue|(A|a)ve|(C|c)ourt|(C|c)t|(D|d)rive|(D|d)r|(L|l)ane|(L|l)n|(R|r)oad|(R|r)d|(B|b)oulevard|(B|b)lvd)|)"

data["Body_Text"][0]

space_out_body_sentences(data)

tokenize_body_text(data)


writer = pd.ExcelWriter('final_data_v1.xlsx')
data.to_excel(writer, 'Sheet1')
writer.save()

#58th avenue
#58 avenue
#~avenue and ~avenue

#"((st\.|street|ave|dr)(and st\.|street|ave|dr))|([0-9] (st\.|street|ave|dr))"
def space_out_body_sentences(data):
    x = 0
    while (x < len(data["Body_Text"])):
        data["Body_Text"][x] = str(re.sub(r'(\.)([A-Z0-9"/\\\/])', r'\1 \2', data["Body_Text"][x]))
        x = x + 1

def tokenize_body_text(data):    
    tokenized_list = []
    for body in data["Body_Text"]:
        sent_tokenize_list = sent_tokenize(body)
        tokenized_list.append(sent_tokenize_list)    
    data["Tokenized_List"] = tokenized_list

def filter_sentences(regex, dataset):
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

def filter_actual_values(regex, dataset):
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
#    
#writer = pd.ExcelWriter('cleaned_and_parsed_crime_data.xlsx')
#data.to_excel(writer, 'Sheet1')
#writer.save()
#
##sentence_list = []
#for tokens in data["Tokenized_List"]:
#    for sentences in tokens:
#        regexp = "Street"
#        if re.search(regexp, sentences):
#            sentence_list.append(address)
#sentence_list
#
#tokenizer = nltk.data.load('./Crime/cleaned_data_crime.txt')
#
#
#for paragraph in document:
#    paragraph_sentence_list = tokenizer.tokenize(paragraph)
#    for line in xrange(0,len(paragraph_sentence_list)):
#        if 'could' in paragraph_sentence_list[line]:
#
#            print(paragraph_sentence_list[line])
#
#            try:
#                print(paragraph_sentence_list[line-1])
#            except IndexError as e:
#                print('Edge of paragraph. Beginning.')
#                pass
#
#            try:
#                print(paragraph_sentence_list[line+1])
#            except IndexError as e:
#                print('Edge of paragraph. End.')
#                pass
#            
#            
#
#import re
#
#txt = ...
#regexp = "[0-9]{1,3} .+, .+, [A-Z]{2} [0-9]{5}"
#address = re.findall(regexp, txt)
#
#
#
#>>> text = “this’s a sent tokenize test. this is sent two. is this sent three? sent 4 is cool! Now it’s your turn.”
#>>> from nltk.tokenize import sent_tokenize
#>>> sent_tokenize_list = sent_tokenize(text)
#>>> len(sent_tokenize_list)
#5
#>>> sent_tokenize_list
#[“this’s a sent tokenize test.”, ‘this is sent two.’, ‘is this sent three?’, ‘sent 4 is cool!’, “Now it’s your turn.”]
