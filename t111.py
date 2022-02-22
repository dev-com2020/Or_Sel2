# this test python
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options

options_e = Options()
options_e.add_argument("--headless")

driver = webdriver.Edge(options=options_e)

driver.get("https://paczkadoukrainy.pl/")
driver.set_window_size(1920, 1000)

print("tutaj wpisuje wage")
pole_waga = driver.find_element(By.NAME, "parcelWeight")
pole_waga.click()
pole_waga.send_keys("10")

driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(5)").click()
driver.execute_script("window.scrollTo(0,750)")
driver.find_element(By.XPATH, '//*[@id="offerListCalc"]/div[1]/div[6]/div/div/div[2]/div/div[3]/button').click()
driver.save_screenshot("TEST_Headless.png")
driver.close()

# ALT+ CTRL + L formatowanie kodu!!!
