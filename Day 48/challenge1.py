####################################################
#        Use Selenium to Scrape Website Data
####################################################

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\\Development\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

URL = "https://www.python.org/"

driver.get(URL)

events = driver.find_elements(By.CSS_SELECTOR, ".event-widget li")

count = 0
event_dict = {}
for event in events:
    event_data = event.text.split("\n")
    event_date = event_data[0]
    event_title = event_data[1]
    data = {"time": event_date, "name": event_title}
    event_dict[count] = data
    count += 1

print(event_dict)

###########
# OR
###########

event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
events = {}

for n in range(len(event_names)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text
    }
print(events)

driver.quit()
