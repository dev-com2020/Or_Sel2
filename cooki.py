import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.solarwinds.com/")
time.sleep(2)
# driver.find_element(By.ID, 'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll').click()
time.sleep(2)
# driver.delete_cookie("secure")
# driver.delete_all_cookies()
driver.add_cookie({"name": "Gabriel", "value": "True"})
time.sleep(2)
print(driver.get_cookie("Gabriel"))
# print(driver.get_cookies())