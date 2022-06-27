import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("https://crossbrowsertesting.github.io/selenium_example_page.html")

driver.find_element(By.NAME, "checkbox").click()
val = driver.find_element(By.NAME, "checkbox").value_of_css_property('color')
print(val)
# text = driver.find_element(By.CSS_SELECTOR, "h2").text

res = driver.find_element(By.CSS_SELECTOR, "h2").rect
# print(text)
print(res)
is_button = driver.find_element(By.ID, "btn").is_displayed()
print(is_button)


l = driver.find_elements(By.CSS_SELECTOR, "li")
for i in l:
    print(i.text)



# print(zna)
