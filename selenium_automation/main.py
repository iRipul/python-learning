from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def launch_browser(website):
    chrome_driver_path = './driver/chromedriver'
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service)
    driver.get(website)
    return driver


d = launch_browser("https://python.org")
upcoming_events = d.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul')
list_of_events = upcoming_events.find_elements(By.CSS_SELECTOR, "li")
event_dict = {}
counter = 0
for event in list_of_events:
    time = event.find_element(By.CSS_SELECTOR, "time")
    anchor = event.find_element(By.CSS_SELECTOR, "a")
    event_dict[counter] = {
        "time": time.text,
        "name": anchor.text
    }
    counter += 1

print(event_dict)
d.close()
