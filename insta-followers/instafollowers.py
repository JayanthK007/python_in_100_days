from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions
import os,dotenv,time

dotenv.load_dotenv()


class InstaFollower:
    def __init__(self):
        self.options=ChromeOptions()
        self.options.add_experimental_option('detach',True)
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get("https://www.instagram.com/")

    def login(self):
        self.username=self.driver.find_element(By.CSS_SELECTOR,'input[name=username]')
        self.username.send_keys(os.getenv('INSTA_USERNAME'))
        self.password=self.driver.find_element(By.CSS_SELECTOR,'input[name=password]')
        self.password.send_keys(os.getenv("INSTA_PASSWORD"))
        self.button=self.driver.find_element(By.CSS_SELECTOR,'button[type=submit]')
        self.button.click()
        time.sleep(3)
        self.dont_save_login=self.driver.find_element(By.CSS_SELECTOR,'div[role=button]')
        self.dont_save_login.click()
        time.sleep(3)
        self.notifications=self.driver.find_element(By.XPATH,'/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
        self.notifications.click()

    def find_follower(self):
        self.search=self.driver.find_element(By.CSS_SELECTOR,'svg[aria-label=Search]')
        self.search.click()
        time.sleep(1)
        self.search_input=self.driver.find_element(By.CSS_SELECTOR,'input[placeholder=Search]')
        self.search_input.send_keys(os.getenv('FIND_PAGE'))

    def follow(self):
        ...            