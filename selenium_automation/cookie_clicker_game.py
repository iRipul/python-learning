from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

chrome_driver_path = './driver/chromedriver'
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.implicitly_wait(20)
driver.get("https://orteil.dashnet.org/cookieclicker/")
wait = WebDriverWait(driver, 10)

sleep(10)
lang = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.langSelectButton")))
lang.click()
sleep(2)

cookie = driver.find_element(By.ID, "bigCookie")
while True:
    cookie.click()




