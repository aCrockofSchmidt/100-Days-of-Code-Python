import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


PROMISED_DOWN = 50
PROMISED_UP = 10
CHROME_DRIVER_PATH = r"C:\Users\Steph\OneDrive\Documents\Home\Development\chromedriver.exe"
SPEED_TEST_URL = "https://www.speedtest.net/"
TWITTER_URL = "https://twitter.com/"
TWITTER_EMAIL = "acrockofschmidt@gmail.com"
TWITTER_PASSWORD = os.environ.get("TWITTER_PASSWORD")
TWITTER_USERNAME = "@acrockofschmidt"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.service = Service(CHROME_DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.service)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get(SPEED_TEST_URL)
        go_button = self.driver.find_element(By.CLASS_NAME, "js-start-test")
        go_button.click()
        # print("button clicked")
        time.sleep(60)
        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]'
                                                       '/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        print(f"Down = {self.down}")
        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]'
                                                     '/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        print(f"Up = {self.up}")

    def tweet_at_provider(self):
        self.driver.get(TWITTER_URL)
        time.sleep(10)
        sign_in_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]'
                                                            '/div[1]/div/div[3]/div[5]/a/div')
        sign_in_button.click()
        time.sleep(5)
        email_text_box = self.driver.find_element(By.NAME, 'text')
        email_text_box.send_keys(TWITTER_EMAIL)
        time.sleep(2)
        email_text_box.send_keys(Keys.ENTER)
        time.sleep(2)
        try:
            username_text_box = self.driver.find_element(By.NAME, 'text')
            username_text_box.send_keys(TWITTER_USERNAME)
            time.sleep(2)
            username_text_box.send_keys(Keys.ENTER)
            time.sleep(2)
        except:
            pass
        password_text_box = self.driver.find_element(By.NAME, 'password')
        password_text_box.send_keys(TWITTER_PASSWORD)
        time.sleep(2)
        password_text_box.send_keys(Keys.ENTER)
        time.sleep(2)
        compose_tweet_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div'
                                                                  '/div/div[1]/div[3]/a/div')
        compose_tweet_button.click()
        time.sleep(2)
        compost_tweet = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]'
                                                           '/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]'
                                                           '/div[1]/div/div/div/div/div/div/div/div/div/div/label'
                                                           '/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        compost_tweet.send_keys(f"Hey ISP. Why is my internet speed {self.down}down/{self.up}up when I pay for"
                                f" {PROMISED_DOWN}down/{PROMISED_UP}/up?")
        send_tweet_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]'
                                                               '/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/'
                                                               'div[2]/div[3]/div/div/div[2]/div[4]/div/span/span')
        send_tweet_button.click()
        time.sleep(2)
        self.driver.close()


# sign-in-button xpath = //*[@id="container"]/div/div[2]/div[1]
# continue-gmail xpath = //*[@id="container"]/div/div[2]/div[1]
# account-choose xpath = //*[@id="credentials-picker"]/div[1]/div[1]
# compose-tweet xpath = //*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div
# tweet-text-box xpath = //*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div
# send tweet box xpath = //*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]/div/span/span

