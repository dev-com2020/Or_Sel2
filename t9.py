import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

service = Service(executable_path="msedgedriver.exe")
driver = webdriver.Edge(service=service)
driver.maximize_window()

driver.get("https://paczkadoukrainy.pl/")
time.sleep(5)
driver.save_screenshot("stronaPrzedUstawieniem.png")
#input("jestem tu1 ...")
driver.find_element(By.CLASS_NAME, "input-group").click()
#input("jestem tu2 ...")
driver.find_element(By.NAME, "parcelWeight").click()
time.sleep(5)
driver.find_element(By.NAME, "parcelWeight").send_keys("10")

zobaczCeny = driver.find_element(By.XPATH, "//button[contains(.,'Zobacz ceny')]")
zobaczCeny.click()
input("jestem tu3 ...")
time.sleep(1)


nadajPaczkeGLS = driver.find_element(By.XPATH, "//div[6]/div/div/div[2]/div/div[3]/button")
time.sleep(1)
nadajPaczkeGLS.location_once_scrolled_into_view
time.sleep(1)
nadajPaczkeGLS.click()
input("jestem tu4 ...")

time.sleep(1)
driver.save_screenshot("stronaPoUstawienieu.png")

time.sleep(1)
driver.quit()