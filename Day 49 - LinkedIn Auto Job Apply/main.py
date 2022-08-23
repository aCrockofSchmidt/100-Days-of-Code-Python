import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

chrome_driver_path = r"C:\Users\Steph\OneDrive\Documents\Home\Development\chromedriver.exe"

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

JOB_URL = "https://www.linkedin.com/jobs/search/?currentJobId=3226507682&f_AL=true&f_E=2&f_" \
          "WT=2&geoId=101174742&keywords=python&location=Canada&refresh=true"

LINKED_IN_EMAIL = "acrockofschmidt@gmail.com"
LINKED_IN_PASSWORD = os.environ.get("LINKEDIN_PASSWORD")

# open website and click sign in button
driver.get(JOB_URL)
signin_click = driver.find_element(By.CLASS_NAME, "nav__button-secondary")
signin_click.click()


# enter email and password to sign in
email_enter = driver.find_element(By.ID, "username")
email_enter.send_keys(LINKED_IN_EMAIL)
password_enter = driver.find_element(By.ID, "password")
password_enter.send_keys(LINKED_IN_PASSWORD)
signin_enter = driver.find_element(By.CLASS_NAME, "btn__primary--large")
signin_enter.send_keys(Keys.ENTER)
time.sleep(10)


def save_job():
    # click save button
    save_click = driver.find_element(By.CLASS_NAME, "jobs-save-button span")
    if save_click.text == "Save":
        save_click.click()
    else:
        print(f"you have already saved this job")


def follow_company():

    # scroll overflow scrollbar to show bottom of div
    overflow_bar = driver.find_element(By.CLASS_NAME, "overflow-x-hidden")
    scroll_origin = ScrollOrigin.from_element(overflow_bar)
    ActionChains(driver).scroll_from_origin(scroll_origin, 0, 15000).perform()
    time.sleep(3)

    #click follow button
    follow_click = driver.find_element(By.CSS_SELECTOR, ".follow span")
    if follow_click.text == "Follow":
        follow_click.click()
    else:
        print("you are already following this company")

# find a list of all jobs in search results


all_jobs = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")

i = 0

for job in all_jobs:
    print("called")
    job.click()
    print("job clicked")
    time.sleep(5)
    save_job()
    print("job saved")
    time.sleep(2)
    follow_company()
    print("company followed")
    time.sleep(3)

    i += 50
    scroll_bar = driver.find_element(By.CLASS_NAME, "jobs-search-results-list")
    scroll_origin = ScrollOrigin.from_element(scroll_bar)
    ActionChains(driver).scroll_from_origin(scroll_origin, 0, i).perform()
    time.sleep(3)

