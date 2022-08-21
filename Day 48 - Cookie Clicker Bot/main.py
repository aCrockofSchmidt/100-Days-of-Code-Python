import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = r"C:\Users\Steph\OneDrive\Documents\Home\Development\chromedriver.exe"

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("http://orteil.dashnet.org/experiments/cookie/")


def click_away():
    time_stop = time.time() + 5
    while time.time() < time_stop:
        cookie = driver.find_element(By.ID, "cookie")
        cookie.click()


def stores_list():
    all_tuples = []
    all_stores = driver.find_elements(By.CSS_SELECTOR, "#store b")

    for store in all_stores:
        all_tuples.append(
                          ("buy"+store.get_attribute("textContent").split(" -  ")[0],
                           store.get_attribute("textContent").split(" -  ")[1].replace(",", ""))
                          )
    return all_tuples


def assess_money():
    buy_item = ""
    store_list = stores_list()
    current_money = driver.find_element(By.ID, "money")
    current_money_int = int(current_money.text.replace(",", ""))

    for store in store_list:
        if int(store[1]) <= current_money_int:
            buy_item = store[0]
        if buy_item == "":
            return

    buy_click = driver.find_element(By.ID, buy_item)
    buy_click.click()


game_stop = time.time() + 60 * 5

while time.time() < game_stop:
    click_away()
    assess_money()

rate = driver.find_element(By.ID, "cps")
print(rate.text)







