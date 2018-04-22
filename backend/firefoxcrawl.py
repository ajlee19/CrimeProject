import os
import sys
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time
import newspaper
from datetime import datetime
import logging, logging.handlers

base_path = "./abc_news_scraping/"
log_path = base_path + "logs/"
data_path = base_path + "data/"
#today = datetime.strftime(datetime.now(), "%X%m%d")

#IS_SUCCESS = False
#PATIENCE_TIME = 60

ABC_NEWS_HOME_PAGE_URL = "http://abc7news.com/tag/crime/"

binary = FirefoxBinary(r'C:\Users\da_gw3_user1\AppData\Local\Mozilla Firefox\firefox.exe')

#driver = webdriver.Firefox(path="C://Users//da_gw3_user1//Crime//geckodriver.exe")
#driver = webdriver.Firefox("C:\\Users\\da_gw3_user1\\Crime\\geckodriver.exe")
driver = webdriver.Firefox(firefox_binary=binary)
driver.get(ABC_NEWS_HOME_PAGE_URL)

with open(data_path+"urlcollection.txt", 'a+') as dataset:
    while True:
        try:
            loadMoreButton = driver.find_element(By.CSS_SELECTOR, ".show-button-more.button.button-block")
            time.sleep(2)
            loadMoreButton.click()
            time.sleep(5)
        except Exception as e:
            print (e)
            break
        parse = newspaper.build(ABC_NEWS_HOME_PAGE_URL)
        for article in parse.articles:
            if article in dataset:
                continue
            dataset.write(article.url + '\n')
dataset.close()
print ("Finished crawling through all. Now will parse.")
time.sleep(10)
driver.quit()
