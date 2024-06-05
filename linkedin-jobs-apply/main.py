from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


chrome_options=ChromeOptions()
chrome_options.add_experimental_option('detach',True)


driver=webdriver.Chrome(options=chrome_options)
driver.get('https://www.linkedin.com/jobs/search/?currentJobId=3922791484&f_AL=true&keywords=python%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true')


sign_in=driver.find_element(By.CSS_SELECTOR,'a.nav__button-secondary')
sign_in.send_keys(Keys.ENTER)

time.sleep(2)

user_name=driver.find_element(By.ID,'username')
user_name.send_keys('jayanthkumarkarthik@gmail.com')

password=driver.find_element(By.ID,'password')
password.send_keys('d=C5bDLbz/f&LW$')

login_button=driver.find_element(By.CSS_SELECTOR,'button.btn__primary--large')
login_button.send_keys(Keys.ENTER)

time.sleep(3)


save_job=driver.find_element(By.CSS_SELECTOR,'button.jobs-save-button')
save_job.send_keys(Keys.ENTER)

company=driver.find_element(By.CSS_SELECTOR,'div.job-details-jobs-unified-top-card__company-name a.app-aware-link ')
company.send_keys(Keys.ENTER)

time.sleep(2)

follow=driver.find_element(By.CSS_SELECTOR,'div.org-top-card-primary-actions__inner span')
follow.click()


driver.quit()