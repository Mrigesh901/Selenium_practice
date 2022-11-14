from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driverService = Service(executable_path="E:\setup\chromedriver.exe")
driver = webdriver.Chrome(service=driverService)

driver.get('''https://www.python.org/''')

eventTimes = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget time")
eventDisc = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget li a")
events = {}

for i in range(len(eventTimes)):
    events[i] = {
        "time": eventTimes[i].text,
        "name": eventDisc[i].text
    }

for i in events:
    print(events[i])
driver.quit()
