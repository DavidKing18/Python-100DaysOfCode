from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\\Development\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

URL1 = "https://www.amazon.com/Instant-Pot-Ultra-Programmable-Sterilizer/dp/B06Y1MP2PY/ref=ex_alt_wg_d?_encoding=UTF8" \
      "&pd_rd_i=B06Y1MP2PY&pd_rd_w=b9rt4&pf_rd_p=4e1b46a8-daf9-4433-b97e-d6df97cf3699&pf_rd_r=AYY05P8FZJ7YZ6MQW4KH" \
      "&pd_rd_wg=ESIIX&pd_rd_r=7edd828f-7837-4cf6-b923-9f73f819ced9&content-id=amzn1.sym.4e1b46a8-daf9-4433-b97e" \
      "-d6df97cf3699&th=1"

URL2 = "https://www.python.org/"

# driver.get(URL1)
driver.get(URL2)

# How to Find and Select Elements on a Website with Selenium
# price = driver.find_element(By.CLASS_NAME, 'a-price-whole')
# print(price.text)

search_bar = driver.find_element(By.NAME, "q")
print(search_bar.get_attribute("placeholder"))

logo = driver.find_element(By.CLASS_NAME, "python-logo")
print(logo.size)

documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
print(documentation_link.text)

bug_link = driver.find_element(By.XPATH, "//*[@id=\"site-map\"]/div[2]/div/ul/li[3]/a")
print(bug_link.text)

# driver.close()  # To close browser tab
driver.quit()  # To close browser window
