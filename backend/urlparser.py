import pandas as pd
import numpy as np
import time
import requests
import time
import logging, logging.handlers
import random
from bs4 import BeautifulSoup
from datetime import datetime

dataset = pd.read_csv('./Crime/abc_news_scraping/data/testurl2.txt', header = None)
dataset.columns = ["URL"]
dataset["Title"] = ""
dataset["Published_Date"] = ""
dataset["Body_Text"] = ""

x = 0 
while (x < 4213):
    dataset["URL"][x] = "http://abc7news.com" + dataset["URL"][x]
    html = requests.get(dataset["URL"][x]).text
    bs = BeautifulSoup(html)
    
    #find title
    bs_title = bs.title.string  
    dataset["Title"][x] = bs_title
    
    #find published time
    bs_time = bs.find("meta", property="article:published_time")
    if bs_time == None:
        x = x + 1 
        # print("finished " + str(x) + "th iteration")
        time.sleep(random.uniform(50, 70))
        continue
    dataset["Published_Date"][x] = bs_time["content"]
    
    #find body text
    #bs.find("div", {"class" : "body-text"})
    dataset["Body_Text"][x] = bs.find("div", {"class" : "body-text"})
    x = x + 1 
    time.sleep(random.uniform(50, 70))
    # print("finished " + str(x) + "th iteration" )

writer = pd.ExcelWriter('parsed_crime_data.xlsx')
dataset.to_excel(writer, 'Sheet1')
writer.save()

