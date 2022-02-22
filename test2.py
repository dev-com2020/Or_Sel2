import asyncio
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

async def driver1():
    service = Service(executable_path="msedgedriver.exe")
    driver = webdriver.Edge(service=service)
    driver.maximize_window()
    driver.get("https://www.google.pl")
    driver.find_element(By.XPATH, '//*[@id="L2AGLb"]/div').click()
    time.sleep(5)
    print("---Teraz klikam w pole szukaj---")
    pole_sz = driver.find_element(By.NAME, "q")
    pole_sz.click()
    driver.find_element(By.NAME, "q").send_keys("makowiec")
    driver.find_element(By.NAME, "q").send_keys(Keys.ENTER)
    time.sleep(3)
    print(driver.title)
    print(driver.current_url)
    driver.back()
    driver.forward()
    driver.refresh()
    driver.save_screenshot("wynik_mysz_pocz1.png")

async def driver2():
    service = Service(executable_path="msedgedriver.exe")
    driver = webdriver.Edge(service=service)
    driver.maximize_window()
    driver.get("https://www.google.pl")
    driver.find_element(By.XPATH, '//*[@id="L2AGLb"]/div').click()
    time.sleep(5)
    print("---Teraz klikam w pole szukaj---")
    pole_sz = driver.find_element(By.NAME, "q")
    pole_sz.click()
    driver.find_element(By.NAME, "q").send_keys("selenium")
    driver.find_element(By.NAME, "q").send_keys(Keys.ENTER)
    time.sleep(3)
    driver.save_screenshot("wynik_mysz_pocz2.png")

loop = asyncio.get_event_loop()

tasks = [
driver1(),
# driver2()
]

loop.run_until_complete(asyncio.wait(tasks))
loop.close()