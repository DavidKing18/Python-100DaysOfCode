import os
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

Google_form_URL = "https://forms.gle/BgHqwNUfyq3rwtah9"
edge_driver_path = "c://Development//msedgedriver.exe"

EMAIL = "cornflakeschicago@gmail.com"
PASSWORD = os.environ["LinkedinPasswd"]


class DataEntryBot:

    def __init__(self):
        self.driver = webdriver.Edge(executable_path=edge_driver_path)

    def send_data(self, address, price, link):
        self.driver.get(Google_form_URL)
        sleep(2)
        address_response = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div["
                                                              "1]/div/div/div[2]/div/div[1]/div/div[1]/input")
        address_response.send_keys(address)
        sleep(1)
        price_response = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div["
                                                            "2]/div/div/div[2]/div/div[1]/div/div[1]/input")
        price_response.send_keys(price)
        sleep(1)
        link_response = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div["
                                                           "3]/div/div/div[2]/div/div[1]/div/div[1]/input")
        link_response.send_keys(link)
        sleep(1)
        submit = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div["
                                                    "1]/div/span/span")
        submit.click()
        sleep(2)

    def create_google_sheet(self):
        self.driver.get("https://docs.google.com/forms/")
        sleep(2)
        email_input = self.driver.find_element(By.ID, "identifierId")
        email_input.send_keys(EMAIL)
        email_input.send_keys(Keys.ENTER)
        sleep(5)
        password_input = self.driver.find_element(By.NAME, "Passwd")
        password_input.send_keys(PASSWORD)
        password_input.send_keys(Keys.ENTER)
        sleep(5)
        sheet = self.driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div[3]/div[6]/div/div[2]/div/div[1]")
        sheet.click()
        sleep(3)
        response_tab = self.driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[3]/div[1]/div/div["
                                                          "2]/span/div")
        response_tab.click()
        sleep(2)
        link_to_sheets = self.driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div[2]/div/div[1]/div[1]/div["
                                                            "2]/div[1]/div[1]/div/span/span[1]/div")
        link_to_sheets.click()
        sleep(1)
        create_sheet = self.driver.find_element(By.XPATH,
                                                "/html/body/div[14]/div/div[2]/div[2]/div[3]/div[1]/span/span")
        create_sheet.click()
