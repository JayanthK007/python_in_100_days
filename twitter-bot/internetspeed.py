from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os,dotenv


dotenv.load_dotenv()


class InternetSpeedTwitterBot:
    def __init__(self):
        self.options=ChromeOptions()
        self.options.add_experimental_option('detach',True)
        self.down=0
        self.up=0

    def get_internet_speed(self):
        self.driver=webdriver.Chrome(options=self.options)
        self.driver.get('https://www.speedtest.net/')
        self.speed_button=self.driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        self.speed_button.click()
        sleep(40)
        self.down=self.driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.up=self.driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.driver.close()

    def tweet_at_provider(self):
        self.driver=webdriver.Chrome(options=self.options)
        self.driver.get('https://twitter.com/i/flow/login')
        wait = WebDriverWait(self.driver, 10)

        username = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[autocomplete=username]'))
        )
        username.send_keys(os.getenv('TWITTER_EMAIL'))

        login_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[role=button].r-13qz1uu'))
        )
        login_button.click()
        
        alt_user=wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR,'input[autocomplete=on]'))       
              )
        alt_user.send_keys(os.getenv('TWITTER_ALT'))  

        next_button=wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/button'))
        )
        next_button.click()

        password = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[type=password]'))
        )
        password.send_keys(os.getenv('TWITTER_PASSWORD'))

        login_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid*=Login_Button]'))
        )
        login_button.click()

        direct_message_link = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid=tweetTextarea_0]'))
        )

        direct_message_link.send_keys(f'You promised that you will provide 100mbps downspeed and 50 mbps upspeed, but you provided {self.down}mbps dowmspeed and {self.up}mbps upspeed')
        
        tweet_button=wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid=tweetButtonInline]'))
        )

        tweet_button.click()
        
