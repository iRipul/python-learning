from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep


chrome_driver_path = './driver/chromedriver'
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.implicitly_wait(10)
driver.get("https://twitter.com")

wait = WebDriverWait(driver, 10)
login_btn = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Log in")))
login_btn.click()
username = driver.find_element(By.NAME, "text")
username.send_keys("xxxxxxxxxx")
username.send_keys(Keys.ENTER)
sleep(3)
try:
    user_suspect = driver.find_element(By.XPATH,
                    '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
    user_suspect.send_keys("xxxxxxxxxx")
    user_suspect.send_keys(Keys.ENTER)
except Exception as err:
    print(err)

pwd = driver.find_element(By.NAME, "password")
pwd.send_keys("xxxxxxxxxx")
pwd.send_keys(Keys.ENTER)

sleep(10)
tweet_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')))
tweet_btn.click()
sleep(2)
text_box = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                  '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[1]')))
try:
    text_box.click()
except Exception as err:
    print(err)
sleep(1)
tb = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
tb.send_keys("""Day 58 | Web Scraping | Python | Selenium today
Automated Tweet using Selenium
     
#100daysofcoding 
#pythonprogramming
#100daysofcodingchallenge 
#Python3
#Python 
#webscraping
#HTML 
#CSS
#selenium
""")

sleep(3)

send_btn = driver.find_element(By.XPATH, "//div[@data-testid='tweetButton']")
send_btn.click()

driver.quit()




