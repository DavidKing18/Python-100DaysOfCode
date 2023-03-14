from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import os


edge_driver_path = "c:\\Development\\msedgedriver.exe"
INSTAGRAM_URL = "https://www.instagram.com"
USERNAME = "cornflakeschicago"
PASSWORD = os.environ["LinkedinPasswd"]
INSTA_ACCOUNT = "chefsteps"
ACCOUNTS_TO_FOLLOW = 50


class InstaFollower:

    def __init__(self):
        self.driver = webdriver.Edge(executable_path=edge_driver_path)

    def login(self):
        self.driver.get(INSTAGRAM_URL)
        sleep(3)
        username_input = self.driver.find_element(By.NAME, "username")
        username_input.send_keys(USERNAME)

        password_input = self.driver.find_element(By.NAME, "password")
        password_input.send_keys(PASSWORD)
        password_input.send_keys(Keys.ENTER)
        sleep(10)

    def find_followers(self):
        self.driver.get(f"{INSTAGRAM_URL}/{INSTA_ACCOUNT}/")
        sleep(15)
        followers = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div["
                                                       "1]/div[2]/section/main/div/header/section/ul/li[2]/a")
        followers.click()
        sleep(20)
        followers_popup = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/div/div["
                                                             "1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]")
        all_followers = int(self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div/div["
                                                               "1]/div[1]/div["
                                                               "2]/section/main/div/header/section/ul/li["
                                                               "2]/a/div/span").get_attribute("title").replace(",", ""))
        print(all_followers)
        for _ in range(int(ACCOUNTS_TO_FOLLOW / 2)):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers_popup)
            sleep(2)
        self.driver.execute_script("arguments[0].scrollTop = 0", followers_popup)
        sleep(20)

    def follow(self):
        follows = self.driver.find_elements(By.CSS_SELECTOR, "._aano div div div ._ab8w ._acan")
        for follow in follows[:ACCOUNTS_TO_FOLLOW + 1]:
            try:
                follow.click()
            except ElementClickInterceptedException:
                cancel = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/div/div["
                                                            "2]/div/div/div[1]/div/div[2]/div/div/div/div/div["
                                                            "2]/div/div/div[3]/button[2]")
                cancel.click()
            sleep(3)


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
