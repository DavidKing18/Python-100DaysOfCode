################################################################
#        Challenge: Create an Automated Game Playing Bot
################################################################

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "C:\\Development\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

URL = "http://orteil.dashnet.org/experiments/cookie/"
driver.get(URL)

cookie = driver.find_element(By.ID, "cookie")
while True:
    cookie.click()

