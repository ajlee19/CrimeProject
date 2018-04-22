from selenium import webdriver      
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import newspaper

ABC_NEWS_HOME_PAGE_URL = "http://abc7news.com/tag/crime/"
PATIENCE_TIME = 60

driver = webdriver.Chrome()
driver.get(ABC_NEWS_HOME_PAGE_URL)

while True:
    try:
        loadMoreButton = driver.find_element(By.CSS_SELECTOR, ".show-button-more.button.button-block")
        time.sleep(2)
        loadMoreButton.click()
        time.sleep(5)
    except Exception as e:
        print (e)
        break
print ("Finished crawling through all. Now will parse.")
time.sleep(10)
parse = newspaper.build(ABC_NEWS_HOME_PAGE_URL)
for article in parse.articles:
	print(article.url)
driver.quit()
