from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
from datetime import datetime, timedelta
import time



chrome_options=ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome_options)
driver.get('https://orteil.dashnet.org/experiments/cookie/')


def make_cookie():
    cookie=driver.find_element(By.XPATH,value='//*[@id="cookie"]')
    cookie.click()
    

end_time = datetime.now() + timedelta(minutes=5)
print(end_time)

while datetime.now() < end_time:
    make_cookie()
    time_remaining = (end_time - datetime.now()).seconds
    if(time_remaining%5==0):
        time.sleep(1)
    
number=driver.find_element(By.ID,value='cps')
print(number.text)

driver.quit()

