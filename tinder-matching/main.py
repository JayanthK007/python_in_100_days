from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time,os , dotenv

dotenv.load_dotenv()

chrome_options=ChromeOptions()
chrome_options.add_experimental_option('detach',True)
chrome_options.add_argument('--disable-web-security' )
chrome_options.add_argument('--allow-running-insecure-content')

driver=webdriver.Chrome(options=chrome_options)
driver.get('https://tinder.com/')


cookie_decline=driver.find_element(By.XPATH,'//*[@id="s-48153592"]/div/div[2]/div/div/div[1]/div[2]/button')
cookie_decline.send_keys(Keys.ENTER)
time.sleep(1)

login=driver.find_element(By.XPATH,'//*[@id="s-48153592"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login.click()

time.sleep(2)

wait = WebDriverWait(driver, 20)

    # Locate the iframe
iframe = wait.until(
        EC.presence_of_element_located((By.XPATH, "//iframe"))
    )
    
    # Switch to the iframe
driver.switch_to.frame(iframe)
    
    # Locate the "Continue with Google" button within the iframe using XPath
google_signin_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Continue with Google']"))
    )
    
    # Click the button
google_signin_button.click()

    # Switch back to the default content
driver.switch_to.default_content()

    # Allow time for the new page or popup to load
wait.until(EC.number_of_windows_to_be(2))
    
    # Switch to the new window or popup
driver.switch_to.window(driver.window_handles[1])

email=os.getenv('GOOGLE_EMAIL')
password=os.getenv('GOOGLE_PASS')

email_input=driver.find_element(By.XPATH,'//*[@id="identifierId"]')
email_input.send_keys(Keys.ENTER,email)

button_email=driver.find_element(By.XPATH,'//*[@id="identifierNext"]/div/button')
button_email.send_keys(Keys.ENTER)

time.sleep(1)

password_input=driver.find_element(By.XPATH,'')
password_input.send_keys(Keys.ENTER,password)

button_pass=driver.find_element(By.XPATH,'')
button_email.send_keys(Keys.ENTER)