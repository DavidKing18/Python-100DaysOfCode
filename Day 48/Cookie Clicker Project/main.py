################################################################
#        Challenge: Create an Automated Game Playing Bot
################################################################

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import threading

chrome_driver_path = "C:\\Development\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)


URL = "http://orteil.dashnet.org/experiments/cookie/"
driver.get(URL)


cookie = driver.find_element(By.ID, "cookie")

should_continue = True
start_time = int(time.time())  # Start time in seconds
five_mins_later = start_time + 60*5

items = ["Cursor", "Grandma", "Factory", "Alchemy\ lab", "Mine", "Shipment", "Portal", "Time\ machine"]  # Upgrades

while should_continue:  # Clicking loop
    cookie.click()
    if ((int(time.time()) - start_time) % 5 == 0) and (int(time.time()) != start_time):
        most_expensive_item = 0

        # Default item to buy
        item_to_buy = driver.find_element(By.CSS_SELECTOR, "#buyCursor b")

        #  Loop through upgrade to get price and name to see most expensive and affordable.
        for i in range(0, 8):
            item = driver.find_element(By.CSS_SELECTOR, f"#buy{items[i]} b")
            item_name = items[i].replace('\\', '')
            item_price = int(item.text.replace(f"{item_name} - ", "").replace(",", ""))
            cookies = driver.find_element(By.ID, 'money')
            account_balance = int(cookies.text)
            if (item_price > most_expensive_item) and (account_balance > item_price):
                print(item_price)
                item_to_buy = item
        item_to_buy.click()

    if five_mins_later == int(time.time()):
        should_continue = False
        cookies_per_second = driver.find_element(By.ID, "cps").text
        print(cookies_per_second)
