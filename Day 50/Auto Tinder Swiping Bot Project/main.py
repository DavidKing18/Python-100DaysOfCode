import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import os

chrome_driver_path = "c:\\Development\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

URL = "https://tinder.com/"
EMAIL = "cornflakeschicago@gmail.com"
PASSWORD = os.environ["LinkedinPasswd"]

driver.get(URL)
time.sleep(2)

accept_cookies = driver.find_element(By.XPATH,
                                     "/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]")
accept_cookies.click()
time.sleep(2)

tinder_login = driver.find_element(By.XPATH,
                                   "/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]")
tinder_login.click()
time.sleep(3)

login_with_fb = driver.find_element(By.XPATH,
                                    "/html/body/div[2]/main/div/div/div[1]/div/div/div[3]/span/div[2]/button/div[2]/div[2]/div")
login_with_fb.click()
time.sleep(5)

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]

driver.switch_to.window(fb_login_window)

email_input = driver.find_element(By.ID, "email")
email_input.send_keys(EMAIL)

password_input = driver.find_element(By.ID, "pass")
password_input.send_keys(PASSWORD)
password_input.send_keys(Keys.ENTER)
time.sleep(5)

driver.switch_to.window(base_window)

time.sleep(20)

# continue_as_user = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div/div/div")
# continue_as_user.click()
# time.sleep(5)

allow_location = driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/div/div[3]/button[1]/div[2]/div[2]")
allow_location.click()
time.sleep(7)
not_interested = driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/div/div[3]/button[2]/div[2]/div[2]")
not_interested.click()
time.sleep(5)

for i in range(20):

    time.sleep(8)
    try:
        like_button = driver.find_element(By.XPATH,
                                          "/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div/div[4]/button")
        like_button.click()
        print(f"Liked: {i + 1}")

    except NoSuchElementException:
        time.sleep(5)
        like_button = driver.find_element(By.XPATH,
                                          "/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div/div[4]/button")
        like_button.click()
        print(f"Liked: {i + 1}...")

    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
            match_popup.click()
            # Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            time.sleep(2)

time.sleep(10)
driver.quit()
