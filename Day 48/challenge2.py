##########################################################################################
# Challenge: Use Selenium in a Blank Project & Scrape a Different Piece of Data
##########################################################################################

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\\Development\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

URL = "https://en.wikipedia.org/wiki/Main_Page"

driver.get(URL)

article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
print(article_count.text)
