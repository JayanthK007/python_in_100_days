from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)

driver=webdriver.Chrome(options=chrome_options)
# driver.get('https://en.wikipedia.org/wiki/Main_Page')

# article_count=driver.find_element(By.CSS_SELECTOR,value='#articlecount a')
# print(article_count.text)

driver.get('https://secure-retreat-92358.herokuapp.com/')

fname=driver.find_element(By.NAME,value='fName')
fname.send_keys('jajajaj')

lname=driver.find_element(By.NAME,value='lName')
lname.send_keys('siemmeje')

email=driver.find_element(By.NAME,value='email')
email.send_keys('jajakkskkek@gmail.com')

button=driver.find_element(By.CLASS_NAME,value='btn')
button.send_keys(Keys.ENTER)


# driver.quit()