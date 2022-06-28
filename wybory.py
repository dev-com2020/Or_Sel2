import time
from threading import Thread
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

options = Options()
# options = webdriver.ChromeOptions()
options.headless = True

options.add_argument('--headless')
# options.add_argument('headless')
options.add_argument('--disable-gpu')
# options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
driver = webdriver.Chrome()

driver.get("http://automationpractice.com")
driver.save_screenshot("sklep1.png")
