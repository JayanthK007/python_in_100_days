from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions
import time

chrome_options=ChromeOptions()
chrome_options.add_experimental_option('detach',True)

driver=webdriver.Chrome(options=chrome_options)
driver.get('https://tinder.com/')


cookie_decline=driver.find_element(By.XPATH,'//*[@id="t1755874407"]/div/div[2]/div/div/div[1]/div[2]/button')
cookie_decline.send_keys(Keys.ENTER)
time.sleep(1)

login=driver.find_element(By.XPATH,'//*[@id="t1755874407"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login.click()

time.sleep(2)

google_login=driver.find_element(By.XPATH,'//*[@id="container"]/div')
google_login.send_keys(Keys.ENTER)
