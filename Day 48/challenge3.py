from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "C:\\Development\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

URL = "https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp"

driver.get(URL)

firstName = driver.find_element(By.ID, "firstName")
firstName.send_keys("Chicago")

lastName = driver.find_element(By.ID, "lastName")
lastName.send_keys("Cornflakes")

username = driver.find_element(By.ID, "username")
username.send_keys("ccchicagocornflakes")

password = driver.find_element(By.NAME, "Passwd")
password.send_keys("mypassword")

confirm_password = driver.find_element(By.NAME, "ConfirmPasswd")
confirm_password.send_keys("mypassword")

login = driver.find_element(By.TAG_NAME, "button")
login.send_keys(Keys.ENTER)

time.sleep(30)

title = driver.find_element(By.TAG_NAME, "h1")
print(title.text)
