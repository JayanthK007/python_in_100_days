from bs4 import BeautifulSoup
import os,dotenv
import requests,time
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


dotenv.load_dotenv()

response=requests.get('https://appbrewery.github.io/Zillow-Clone/')


soup=BeautifulSoup(response.text,'html.parser')


links=[]
all_links=soup.find_all('a',attrs={'data-test':'property-card-link','class':'property-card-link'})
for link in all_links:
    links.append(link.get('href'))

prices=[]
all_prices=soup.find_all('span',attrs={'data-test':'property-card-price'})
for price in all_prices:
    prices.append(price.text[0:6])


address=[] 
all_address=soup.find_all('address',attrs={'data-test':'property-card-addr'})
for addrr in all_address:
    addrr=addrr.text.replace(' |',",").strip()
    address.append(addrr)
    
chrome_options=ChromeOptions()
chrome_options.add_experimental_option('detach',True)   


driver=webdriver.Chrome(options=chrome_options)
driver.get(os.getenv('GOOGLE_FORM_LINK'))

time.sleep(2)
for index in range(len(prices)):
    address_text=driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_text.send_keys(address[index])
    price_text=driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_text.send_keys(prices[index])
    link_text=driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_text.send_keys(links[index])
    button=driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    button.click()
    time.sleep(2)
    next_response=driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    next_response.click()
    time.sleep(2)

driver.quit()

# driver=webdriver.Chrome(options=chrome_options)
# driver.get(os.getenv('RESPONSE_COLLECTION'))
# link_to_google_form=driver.find_element(By.XPATH,'//*[@id="ResponsesView"]/div/div[1]/div[1]/div[2]/div[1]/div[1]/div')
# link_to_google_form.click()