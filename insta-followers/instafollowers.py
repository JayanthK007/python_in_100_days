from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
        time.sleep(2)
        self.driver.get(f'https://www.instagram.com/{os.getenv('FIND_PAGE')}/')
        self.search=self.driver.find_element(By.CSS_SELECTOR,f"a[href*='followers']")
        self.search.click()
        time.sleep(3)
        

    # Get the scrollable container inside the popup
        self.popup = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@role='dialog']//div[@class='xyi19xy x1ccrb07 xtf3nb5 x1pc53ja x1lliihq x1iyjqo2 xs83m0k xz65tgg x1rife3k x1n2onr6']")))

        # Scroll the popup
        last_height = self.driver.execute_script("return arguments[0].scrollHeight", self.popup)
        
        while True:
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", self.popup)
            time.sleep(2) # Adjust sleep time if necessary
            
            new_height = self.driver.execute_script("return arguments[0].scrollHeight", self.popup)
            
            if new_height == last_height:
                break
            
            last_height = new_height



    def follow(self):
        time.sleep(3)
        # Get all follow buttons
        follow_buttons = self.popup.find_elements(By.CSS_SELECTOR, "button[type=button]")

        # Follow each user in the popup
        for button in follow_buttons:
            try:
                button.click()
                time.sleep(1)  # Optional: Add a small delay to prevent rate-limiting
            except Exception as e:
                # Handle ElementClickInterceptedException (popup for unfollow confirmation)
                if "ElementClickInterceptedException" in str(e):
                    try:
                        # Click on the "Cancel" button to dismiss the popup
                        cancel_button = self.driver.find_element(By.XPATH, "//button[text()='Cancel']")
                        cancel_button.click()
                    except Exception as e:
                        print(f"Failed to handle popup: {str(e)}")
                else:
                    print(f"Failed to follow: {str(e)}")

