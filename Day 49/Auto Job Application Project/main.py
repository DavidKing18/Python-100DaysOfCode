from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import time
import os

chrome_driver_path = "C:\\Development\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

URL = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C" \
      "%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"

EMAIL = "cornflakeschicago@gmail.com"
PASSWORD = os.environ["LinkedinPasswd"]
PHONE = "8083603251"

driver.get(URL)

sign_in = driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/div/a[2]")
sign_in.click()

time.sleep(2)

email_input = driver.find_element(By.ID, "username")
email_input.send_keys(EMAIL)
password_input = driver.find_element(By.ID, "password")
password_input.send_keys(PASSWORD)
password_input.send_keys(Keys.ENTER)

time.sleep(5)

######################################################
#                 EASY APPLY FOR JOB
######################################################
all_jobs = driver.find_elements(By.CLASS_NAME, ".job-card-container--clickable")
for job in all_jobs:
    try:
        job.click()
        job_title = job.text.split('\n')[0]
        company = job.text.split('\n')[1]
    except StaleElementReferenceException:
        print("Caught an Error while clicking.")
        break
    else:
        time.sleep(5)
        try:
            easy_apply_button = driver.find_element(By.XPATH, "/html/body/div[5]/div[3]/div[4]/div/div/main/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[3]/div/div/div/button")
            if easy_apply_button.text == "Apply":
                print(f"Couldn't apply for {job_title} at {company}")
                pass
        except NoSuchElementException:
            print(f"Couldn't apply for {job_title} at {company}")
            pass
        else:
            easy_apply_button.click()
            try:
                phone_input = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div/form/div/div[1]/div[4]/div/div/div[1]/div/input')
            except NoSuchElementException:
                close_apply_btn = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/button")
                close_apply_btn.click()
                discard_btn = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[3]/button[1]')
                discard_btn.click()
                print(f"Couldn't apply for {job_title} at {company}")
                pass
            else:
                phone_input.clear()
                phone_input.send_keys(PHONE)
                try:
                    submit_application_btn = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div/form/footer/div[3]/button')
                except NoSuchElementException:
                    close_apply_btn = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/button")
                    close_apply_btn.click()
                    discard_btn = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[3]/button[1]')
                    discard_btn.click()
                    print(f"Couldn't apply for {job_title} at {company}")
                    pass
                else:
                    submit_application_btn.click()
                    print(f"Successfully applied for {job_title} at {company}")

######################################################
#           SAVE JOB AND FOLLOW COMPANY
######################################################

# save_button = driver.find_element(By.XPATH, '//*[@id="main"]/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div['
#                                             '1]/div[1]/div[3]/div/button')
# save_button.click()
#
# follow_button = driver.find_element(By.CSS_SELECTOR, ".jobs-company__box .align-items-center button span")
# follow_button.click()

time.sleep(5)
driver.quit()
