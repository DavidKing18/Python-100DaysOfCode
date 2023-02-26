import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os

TWITTER_URL = "https://twitter.com/"
SPEEDTEST_URL = "https://www.speedtest.net/"
TWITTER_EMAIL = "cornflakeschicago@gmail.com"
TWITTER_PASSWORD = os.environ["LinkedinPasswd"]
PROMISED_UP = 10
PROMISED_DOWN = 150
chrome_driver_path = "c:\\Development\\chromedriver.exe"


class InternetSpeedTwitterBot:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get(SPEEDTEST_URL)
        cookies = self.driver.find_element(By.XPATH, "/html/body/div[7]/div[2]/div/div/div[2]/div[1]/div/button")
        cookies.click()
        go = self.driver.find_element(By.XPATH,
                                      "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]")
        go.click()
        time.sleep(60)
        download_speed = self.driver.find_element(By.CLASS_NAME, "download-speed")
        self.down = download_speed.text
        upload_speed = self.driver.find_element(By.CLASS_NAME, "upload-speed")
        self.up = upload_speed.text

    def tweet_at_provider(self):
        message = f"Hey @Spectranet_NG, why is my internet speed {self.down}Mbps down/{self.up}Mbps up when I pay for "\
                  f"higher?"
        self.driver.get(TWITTER_URL)
        twitter_login = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div[1]/div/div/div/div["
                                                           "2]/div[2]/div/div/div[1]/a/div/span/span")
        twitter_login.click()
        time.sleep(15)
        username = self.driver.find_element(By.NAME, "text")
        username.send_keys(TWITTER_EMAIL)
        username.send_keys(Keys.ENTER)
        time.sleep(7)
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)
        time.sleep(15)
        create_tweet = self.driver.find_element(By.XPATH,
                                                "/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a")
        create_tweet.click()
        time.sleep(2)
        tweet_input = self.driver.find_element(By.XPATH,
                                               "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div["
                                               "2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div/div["
                                               "2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div["
                                               "1]/div/div/div/div/div/div[2]/div")
        tweet_input.send_keys(message)
        send_tweet = self.driver.find_element(By.XPATH,
                                              "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div["
                                              "2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div["
                                              "3]/div/div/div[2]/div[4]/div/span/span")
        send_tweet.click()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()

print(f"down: {bot.down}")
print(f"up: {bot.up}")
