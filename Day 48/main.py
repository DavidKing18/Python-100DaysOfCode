from selenium import webdriver

chrome_driver_path = "C:\\Development\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://irontrade.com")
# driver.close()  # To close browser tab
# driver.quit()  # To close browser window

# How to Find and Select Elements on a Website with Selenium
