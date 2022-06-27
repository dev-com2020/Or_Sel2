import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.solarwinds.com/")
driver.maximize_window()
element = driver.find_element(By.XPATH, '//*[@id="custom-bootstrap-menu"]/ul[1]/li[3]/a')
action = ActionChains(driver)
action.move_to_element(element).click().perform()
# element.screenshot("test2.png")
driver.save_screenshot("strona.png")
