import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime
import logging, logging.handlers
import random

base_path = "./" #depends on urlcrawler.txt loc
today = datetime.strftime(datetime.now(), "%X%m%d")

ABC_URL_FRONT = "http://abc7news.com/common/modules/pagination/paginationCollapsed?optionsJSONString=%7B%22expandCollapseDivName%22%3A%22more-stories-expanded%22%2C%22displayOptions%22%3A%7B%22lastModifiedDate%22%3A%22false%22%2C%22img_default%22%3A%22false%22%2C%22divClear%22%3A%22false%22%7D%2C%22format%22%3A%22grid%22%2C%22content%22%3A%7B%22collection%22%3A%7B%22startIndex%22%3A%220%22%2C%22finished%22%3A%22false%22%7D%2C%22solr%22%3A%7B%22query%22%3A%7B%22startIndex%22%3A%22"
ABC_URL_BACK = "%22%2C%22contentType%22%3A%22post%22%2C%22tag%22%3A%22crime%22%7D%7D%7D%2C%22numberOfItems%22%3A%2212%22%7D"
x = 0
ABC_URL = ABC_URL_FRONT+str(x)+ABC_URL_BACK

while (True): 
    html = requests.get(ABC_URL).text
    bs = BeautifulSoup(html, "lxml")
    possible_links = bs.find_all('a')
    if possible_links == []:
        print("No More Links! Congratulations")
        break
    for link in possible_links:
        if link.has_attr('href'):
            with open(base_path+"urlcrawler.txt", 'a+') as dataset:
                try:
                    print(link.attrs['href'])
                    dataset.write(link.attrs['href'] + '\n')
                    time.sleep(random.uniform(6, 8))
                except Exception as e:
                    print (e)
                    continue
            dataset.close()
    x = x + 12
    print(str(x) + "th article URL finished crawling.")
    time.sleep(random.uniform(50, 70))
print ("Finished crawling through all. Check file and now will parse.")
time.sleep(random.uniform(5, 10))

 
