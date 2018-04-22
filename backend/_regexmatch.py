#https://github.com/codelucas/newspaper
import re
import pandas as pd
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
dataset = pd.read_excel('./parsed_crime_data.xlsx')
dataset["Address"] = ""
dataset["Time"] = ""
dataset["Sentence"] = ""

# regex pattern
WORD_DATE_REGEX = "(Jan|January|Feb|February|Mar|March|Apr|April|May|Jun|June|Jul|July|Aug|August|Sep|September|Oct|October|Nov|November|Dec|December)\s[0-3]?[0-9](\s[1|2][0-9][0-9][0-9])?"
MONTH_PATTERN = re.compile("(Jan|January|Feb|February|Mar|March|Apr|April|May|Jun|June|Jul|July|Aug|August|Sep|September|Oct|October|Nov|November|Dec|December)")
TIME_REGEX = "^(1?[0-9]|2[0-3])(\s?:[0-5]?[0-9])?(\s?AM|am|a.m|am|PM|pm|p.m)?"
TIME_PATTERN = re.compile(TIME_REGEX)
LOC_REGEX = '\d+\s[A-Z][a-z]+\s(Avenue|Lane|Road|Boulevard|Drive|Street|Ave|Dr|Rd|Blvd|Ln|St)'
#CITY = "(?:[A-Z][a-z.-]+[ ]?)+"
#STREET = "\d+[ ](?:[A-Za-z0-9.-]+[ ]?)+(?:(A|a)venue|(L|l)ane|(R|r)oad|(B|b)oulevard|(D|d)rive|(S|s)treet|(A|a)ve|Dr|Rd|Blvd|Ln|St)\.?"

# constants for sentence split
caps = "([A-Z])"
prefixes = "(Mr|St|Mrs|Ms|Dr)[.]"
suffixes = "(Inc|Ltd|Jr|Sr|Co)"
starters = "(Mr|Mrs|Ms|Dr|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
websites = "[.](com|net|org|io|gov)"

text = str("On March 4 11:30am, he cased a U.S. Bank at 905 First St. in Gilroy before robbing a Wells Fargo two blocks away several hours later.")

def split_into_senteces(text):
	text = " " + text + " "
	text = text.replace("\n"," ")
	text = re.sub(prefixes,"\\1<prd>",text)
	text = re.sub(websites,"<prd>\\1",text)
	# if "Ph.D" in text: text = text.replace("Ph.D.","Ph<prd>D<prd>")
	text = re.sub("\s" + caps + "[.] "," \\1<prd> ",text)
	text = re.sub(acronyms+" "+starters,"\\1<stop> \\2",text)
	text = re.sub(caps + "[.]" + caps + "[.]" + caps + "[.]","\\1<prd>\\2<prd>\\3<prd>",text)
	text = re.sub(caps + "[.]" + caps + "[.]","\\1<prd>\\2<prd>",text)
	text = re.sub(" "+suffixes+"[.] "+starters," \\1<stop> \\2",text)
	text = re.sub(" "+suffixes+"[.]"," \\1<prd>",text)
	text = re.sub(" " + caps + "[.]"," \\1<prd>",text)
	# if "”" in text:
		# text = text.replace(".”","”.")
	# if "\"" in text:
		# text = text.replace(".\"","\".")
	# if "!" in text:
		# text = text.replace("!\"","\"!")
	# if "?" in text:
		# text = text.replace("?\"","\"?")
	text = text.replace(".",".<stop>")
	text = text.replace("?","?<stop>")
	text = text.replace("!","!<stop>")
	text = text.replace("<prd>",".")
	sentences = text.split("<stop>")
	sentences = sentences[:-1]
	sentences = [s.strip() for s in sentences]
	return sentences

def modify_time_format(time, pub_date):
	year_formatted, month_formatted, date_formatted = None #default
	formatted = ""

	if re.search(MONTH_PATTERN, time):
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
			if minute < 10;:
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
# NEED TO CHECK EDGE CASES
def keyword_extract(text, pub_date):
	#convert text to sentences
	sentences = split_into_senteces(text)
	sentences = tokenize.sasdjflonteces(text)
	# print (sentences)

	#iteration over sentences
	for sentence in sentences:
		# sentence = str(sentence)
		# print (sentence, "\n")

		#if both time and address exists
		if re.search(LOC_REGEX, sentence) and (re.search(WORD_DATE_REGEX, sentence) or re.search(TIME_REGEX, sentence)):			
			print ("Matched\n", sentence)

			# address
			loc_pattern = re.compile(LOC_REGEX)
			address = [m.group() for m in re.finditer(loc_pattern, sentence)][0] #CAN MISS SOME DATA
			print (address)

			# time
			time = ""
			if re.search(WORD_DATE_REGEX, sentence):
  				date_pattern = re.compile(WORD_DATE_REGEX)
  				time += [m.group() for m in re.finditer(date_pattern, sentence)][0]
			if re.search(TIME_REGEX, sentence):
				time_pattern = re.compile(NUM_DATE_REGEX)
  				time += [m.group() for m in re.finditer(time_pattern, sentence)][0]

			time_formatted = modify_time_format(time, pub_date)

  			print (address, time_formatted, sentence)
  			return (address, time_formatted, sentence)


def inter_dataset(dataset):
	#row by row
	for i in range(len(dataset)):
		if dataset["Body_Text"] != None:
			# date
			pub_date = str(dataset["Published_Date"][i])

			# text

			# text = str(re.sub(r'<.*?>', '', str(dataset["Body_Text"][i]))) #clean text
			text = str(dataset["Body_Text"][i])
			# print (text)

			address, time, sentence = keyword_extract(text, pub_date)
			print ("ADDRESS:", address, "\n", "TIME:", time, "\n","SENTENCE:", sentence, "\n")

			# data input
			dataset["Address"][i] = str(address)
			dataset["Time"][i] = str(time)
			dataset["Sentence"][i] = str(sentence)

# export data
writer = pd.ExcelWriter('extracted_data.xlsx')
dataset.to_excel(writer, 'Sheet1')
writer.save()
