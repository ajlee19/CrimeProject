#https://github.com/codelucas/newspaper
# from nltk import tokenize
# import urllib.request
# import html2text
# from BeautifulSoup import BeautifulSoup

# from newspaper import Article
# #get text from URL
# url = "http://www.baltimoresun.com/news/maryland/crime/bs-md-overnight-shootings-20170715-story.html"
# article = Article(url)
# article.download()
# html = article.html
# article.parse()
# date = article.publish_date
# body = article.text

# initiation
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

data["Tokenized_List"][0][0]

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

#def filter_sentences(regex, dataset):
#    only_sentences = []
#    x = 0
#    while x < 4092:
#        y = [w for w in dataset["Tokenized_List"][x] if re.search(regex, w)]
#        if  y != []:
#            only_sentences.append(y)
#        else:
#            only_sentences.append([])
#        x = x + 1
#    dataset["Only_Sentences"] = only_sentences
#
#def filter_actual_values(regex, dataset):
#    only_sentences = []
#    x = 0
#    while x < 4092:
#        sentences = []
#        for sentence in dataset["Tokenized_List"][x]:
#            if re.search(regex, sentence):
#                sentences.append(sentence)
#        if sentences != []:
#            only_sentences.append(sentences)
#        x = x + 1
#    return only_sentences



dataset = data
dataset["Address"] = ""
dataset["Time"] = ""
dataset["Sentence"] = ""

# regex pattern
WORD_DATE_REGEX = "(Jan|January|Feb|February|Mar|March|Apr|April|May|Jun|June|Jul|July|Aug|August|Sep|September|Oct|October|Nov|November|Dec|December)\s[0-3]?[0-9](\s[1|2][0-9][0-9][0-9])?"
MONTH_PATTERN = re.compile("(Jan|January|Feb|February|Mar|March|Apr|April|May|Jun|June|Jul|July|Aug|August|Sep|September|Oct|October|Nov|November|Dec|December)")
TIME_REGEX = "^(1?[0-9]|2[0-3])(\s?:[0-5]?[0-9])?(\s?AM|am|a.m|am|PM|pm|p.m)?"
TIME_PATTERN = re.compile(TIME_REGEX)
LOC_REGEX = "(of|from|by|)([0-9]* )*([0-9]+[a-z]*|[A-Z]+[a-z]*) ((S|s)t\.|(S|s)treet|(A|a)venue|(A|a)ve|(C|c)ourt|(C|c)t|(D|d)rive|(D|d)r|(L|l)ane|(L|l)n|(R|r)oad|(R|r)d|(B|b)oulevard|(B|b)lvd)( and ([0-9]+[a-z]*|[A-Za-z]+) ((S|s)t\.|(S|s)treet|(A|a)venue|(A|a)ve|(C|c)ourt|(C|c)t|(D|d)rive|(D|d)r|(L|l)ane|(L|l)n|(R|r)oad|(R|r)d|(B|b)oulevard|(B|b)lvd)|)"
#CITY = "(?:[A-Z][a-z.-]+[ ]?)+"
#STREET = "\d+[ ](?:[A-Za-z0-9.-]+[ ]?)+(?:(A|a)venue|(L|l)ane|(R|r)oad|(B|b)oulevard|(D|d)rive|(S|s)treet|(A|a)ve|Dr|Rd|Blvd|Ln|St)\.?"

# constants for sentence split
caps = "([A-Z])"
prefixes = "(Mr|St|Mrs|Ms|Dr)[.]"
suffixes = "(Inc|Ltd|Jr|Sr|Co)"
starters = "(Mr|Mrs|Ms|Dr|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
websites = "[.](com|net|org|io|gov)"

# text = str("On March 4 11:30am, he cased a U.S. Bank at 905 First St. in Gilroy before robbing a Wells Fargo two blocks away several hours later.")

# def split_into_senteces(text):
#     text = " " + text + " "
#     text = text.replace("\n"," ")
#     text = re.sub(prefixes,"\\1<prd>",text)
#     text = re.sub(websites,"<prd>\\1",text)
#     # if "Ph.D" in text: text = text.replace("Ph.D.","Ph<prd>D<prd>")
#     text = re.sub("\s" + caps + "[.] "," \\1<prd> ",text)
#     text = re.sub(acronyms+" "+starters,"\\1<stop> \\2",text)
#     text = re.sub(caps + "[.]" + caps + "[.]" + caps + "[.]","\\1<prd>\\2<prd>\\3<prd>",text)
#     text = re.sub(caps + "[.]" + caps + "[.]","\\1<prd>\\2<prd>",text)
#     text = re.sub(" "+suffixes+"[.] "+starters," \\1<stop> \\2",text)
#     text = re.sub(" "+suffixes+"[.]"," \\1<prd>",text)
#     text = re.sub(" " + caps + "[.]"," \\1<prd>",text)
#     # if "”" in text:
#         # text = text.replace(".”","”.")
#     # if "\"" in text:
#         # text = text.replace(".\"","\".")
#     # if "!" in text:
#         # text = text.replace("!\"","\"!")
#     # if "?" in text:
#         # text = text.replace("?\"","\"?")
#     text = text.replace(".",".<stop>")
#     text = text.replace("?","?<stop>")
#     text = text.replace("!","!<stop>")
#     text = text.replace("<prd>",".")
#     sentences = text.split("<stop>")
#     sentences = sentences[:-1]
#     sentences = [s.strip() for s in sentences]
#     return sentences

def modify_time_format(time, pub_date):
    year_formatted, month_formatted, date_formatted = "", "", "" #default
    formatted = ""

    if re.search(MONTH_PATTERN, time):
        print(time)
        #get year
        if re.search(r'[1|2][0-9][0-9][0-9]', time):
            year_formatted = [m.group() for m in re.finditer(r'[1|2][0-9][0-9][0-9]', time)][0]
        else:
            year_formatted = pub_date[:4]

        #get month
        month = [m.group() for m in re.finditer(MONTH_PATTERN, time)][0]
        if "JAN" in month.upper():
            month_formatted = "01"
        elif "FEB" in month.upper():
            month_formatted = "02"
        elif "MAR" in month.upper():
            month_formatted = "03"
        elif "APR" in month.upper():
            month_formatted = "04"
        elif "MAY" in month.upper():
            month_formatted = "05"
        elif "JUN" in month.upper():
            month_formatted = "06"
        elif "JUL" in month.upper():
            month_formatted = "07"
        elif "AUG" in month.upper():
            month_formatted = "08"
        elif "SEP" in month.upper():
            month_formatted = "09"
        elif "OCT" in month.upper():
            month_formatted = "10"
        elif "NOV" in month.upper():
            month_formatted = "11"
        elif "DEC" in month.upper():
            month_formatted = "12"
        else:
            month_formatted = pub_date[5:7]

        #get date
        if re.search(r'[0-3]?[0-9]', month):
            date_formatted = str([m.group() for m in re.finditer(r'[0-3]?[0-9]', month)][0])
        else:
            date_formatted = pub_date[8:10]


    if re.search(TIME_PATTERN, time):
        t = [m.group() for m in re.finditer(r'[0-5]?[0-9]', time)]

        #minute
        if len(t) == 2:
            minute = int(t = [m.group() for m in re.finditer(r'[0-5]?[0-9]', t[1])][0])
            if minute < 10:
                minute_formatted = "0"+str(minute)
            else:
                minute_formatted = str(minute)
        else:
            minute_formatted = ""

        #hour
        hour = int(t[0])
        if re.search(r'PM|pm|p.m', time):
            hour += 12
        if hour < 10:
            hour_formatted = "0"+str(hour)
        else:
            hour_formatted = str(hour)

        formatted = " "+hour_formatted+":"+minute_formatted

    time_formatted = year_formatted+"/"+month_formatted+"/"+date_formatted + formatted

    return time_formatted

# http://abc7news.com/news/bearded-bandit-sought-for-15-bank-robbery-incidents-arrested/1260198/
#NEED TO CHECK EDGE CASES

def keyword_extract(sentences, pub_date):
    #convert text to sentences
#    sentences = split_into_senteces(text)
    #print (sentences)
    pub_date = str(pub_date)

    #iteration over sentences
    for sentence in sentences:
        # sentence = str(sentence)
        #print (sentence, "\n")

        #if time or address exists
        if re.search(LOC_REGEX, sentence):
            print ("HEKKO", sentence)
#            print ("Matched\n", sentence)
            # address
            loc_pattern = re.compile(LOC_REGEX)
            if len([m.group() for m in re.finditer(loc_pattern, sentence)]) != 0:
                
                address = [m.group() for m in re.finditer(loc_pattern, sentence)][0] #CAN MISS SOME DATA

            print (address)
            time = ""
            if (re.search(WORD_DATE_REGEX, sentence) or re.search(TIME_REGEX, sentence)):
                if re.search(WORD_DATE_REGEX, sentence):
                    date_pattern = re.compile(WORD_DATE_REGEX)
                    time += [m.group() for m in re.finditer(date_pattern, sentence)][0]
                if re.search(TIME_REGEX, sentence):
                    time_pattern = re.compile(TIME_REGEX)
                    time += [m.group() for m in re.finditer(time_pattern, sentence)][0]
            time_formatted = modify_time_format(time, pub_date)
                
            print (address, time_formatted, sentence)
            
            return (address, time_formatted, sentence)


dataset["Tokenized_List"][0][1]


x = 0
while (x < len(dataset["Tokenized_List"])):
    if keyword_extract(dataset["Tokenized_List"][x], dataset["Published_Date"][x]) != None:
        address, time, sentence = keyword_extract(dataset["Tokenized_List"][x], dataset["Published_Date"][x])
        dataset["Address"][x] = str(address)
        dataset["Time"][x] = str(time)
        dataset["Sentence"][x] = str(sentence)
    x = x + 1 

dataset[["Address", "Time", "Sentence"]]
dataset["Address"].describe()
# def inter_dataset(dataset):
#     #row by row
#     for i in range(len(dataset)):
#         if dataset["Body_Text"] != None:
#             # date
#             pub_date = str(dataset["Published_Date"][i])

#             # text

#             # text = str(re.sub(r'<.*?>', '', str(dataset["Body_Text"][i]))) #clean text
#             text = str(dataset["Body_Text"][i])
#             # print (text)

#             address, time, sentence = keyword_extract(text, pub_date)
#             print ("ADDRESS:", address, "\n", "TIME:", time, "\n","SENTENCE:", sentence, "\n")

#             # data input
#             dataset["Address"][i] = str(address)
#             dataset["Time"][i] = str(time)
#             dataset["Sentence"][i] = str(sentence)

# # export data
# writer = pd.ExcelWriter('extracted_data.xlsx')
# dataset.to_excel(writer, 'Sheet1')
# writer.save()
